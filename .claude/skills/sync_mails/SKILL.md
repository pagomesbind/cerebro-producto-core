---
name: sync_mails
description: Ingesta diaria de la bandeja de entrada de Gmail. Triage en 3 capas para descartar basura sin gastar tokens (notificaciones Jira/Workvivo/RRHH/promos/Gemini), y análisis con mirada de copiloto PM de lo que importa — mails de clientes, del banco, internos de equipo, comunicaciones Bind PSP, proveedores (Coelsa, Global Processing). Rutea lo aprendido igual que /sync_meetings: conocimiento a detalle_productos/, novedades a proyectos vivos de 1_proyectos/ + comentario automático en la IDEA de Jira, acciones al backlog global tareas.md, candidatas a IDEA nueva al banco de oportunidades (2_areas/direccion/oportunidades.md) + reporte, decisiones a decisiones.md. Registra cada thread analizado en log_mails.md. Apto para scheduled action diaria L-V 9:30 (procesa el delta desde el último barrido).
when_to_use: Se activa cuando el usuario ejecuta el comando de barra /sync_mails (sin argumento para el delta diario; `backfill [días]` para historia; una fecha YYYY-MM-DD para una corrida puntual), o como scheduled action diaria de lunes a viernes a las 9:30.
disable-model-invocation: true
argument-hint: "[opcional: backfill [días] | YYYY-MM-DD]"
---

# 📬 INGESTA DIARIA DE MAILS: /sync_mails

## 🎯 Por qué existe esta skill

El PM recibe a diario mails con conocimiento que muere en la bandeja: tickets con Coelsa donde se aprende funcionamiento nuevo y lecciones aprendidas, avisos de Global Processing, comunicaciones de clientes y del banco, definiciones internas del equipo y de Bind PSP. `/sync_mails` es el flujo de captura diario del correo: corre cada mañana a las 9:30, levanta los mails nuevos desde el último barrido, descarta la basura al menor costo posible y convierte lo valioso en activos del Cerebro.

**Qué aporta que las otras skills no ven:** `/sync_meetings` captura las conversaciones habladas; esta skill captura **las conversaciones escritas y las comunicaciones formales** — tickets con proveedores, reclamos de clientes, avisos regulatorios, decisiones comunicadas por mail. Es la **segunda skill autorizada a escribir en Jira** (comentarios en IDEAs, decisión del usuario 2026-07-14), junto con `/sync_meetings`.

## 🔌 Conexión técnica

### Fuente: Gmail (SOLO LECTURA)

- **Tools:** `search_threads` (descubrimiento + metadata), `get_thread` (lectura completa de un hilo), `get_message` (un mensaje puntual).
  - ⚠️ **Carga de tools:** el prefijo hash del conector varía entre sesiones — si fallan por nombre, `ToolSearch query:"gmail search threads message"` (keyword, no `select:`).
  - **Verificado 2026-07-14 (smoke test):** la query base completa (con `-category:` y múltiples `-from:`) es aceptada por el conector. Usar `view: "THREAD_VIEW_MINIMAL"` — devuelve remitente, asunto, snippet, labels y destinatarios por mensaje: suficiente para el triage sin abrir cuerpos. `pageSize` máximo 50; paginar por `nextPageToken`.
  - ⚠️ **El match es a nivel thread:** un hilo viejo con un mensaje nuevo en la ventana vuelve COMPLETO (todos sus mensajes, incluso los `SENT` propios). Para el dedupe, comparar las fechas/ids de los mensajes contra el último barrido y analizar solo los nuevos.
- **Cero escrituras en Gmail:** el tracking de procesados es por archivo de control (threadId), NUNCA por labels ni marcando leídos.
- **Cuenta:** la del campo `email` en `identidad.local.md` (raíz del repo de cada instalación) — nunca hardcodeada, cada PM/PO tiene la suya.

### 💰 Estrategia de eficiencia de tokens — pipeline en 3 capas (núcleo del diseño)

**Capa 1 — Filtro en la query (costo ~0).** La query de `search_threads` ya excluye la basura en origen. Query base:

```
in:inbox after:YYYY/MM/DD before:YYYY/MM/DD -category:promotions -category:social -category:updates -from:jira -from:atlassian.net -from:workvivo -from:gemini-notes@google.com -from:meet-recordings-noreply@google.com -from:drive-shares-dm-noreply@google.com -from:calendar-notification@google.com -from:noreply -from:no-reply
```

- **Exclusión explícita de mails de Gemini/Meet:** las minutas y grabaciones de reuniones ya las cubre `/sync_meetings` — procesarlas acá sería duplicado.
- Si el conector rechaza parte de la sintaxis (ej. `-category:`), degradá a una query más simple (`in:inbox after:X before:Y`) y compensá con la Capa 2. Registrá el hallazgo y actualizá esta SKILL.md.
- 📝 **Lista de exclusión viva:** cuando el triage detecte remitentes-basura recurrentes que la query no filtra, agregalos acá.

**Capa 2 — Triage por metadata (barato).** Sobre el resultado de `search_threads` (remitente + asunto + snippet), clasificar cada thread en DESCARTAR / ANALIZAR **sin abrir ningún cuerpo**:

- ✅ **ANALIZAR:**
  - Proveedores: `coelsa.com.ar`, Global Processing (`globalprocessing`), y cualquier procesador/proveedor conocido avisando algo.
  - Banco: mails corporativos de `bind.com.ar` con contenido de negocio (definiciones, avisos, escalamientos).
  - Clientes: dominios/nombres que matcheen contra `wiki/2_areas/clientes/` o clientes conocidos del Cerebro.
  - Internos de equipo y comunicaciones oficiales de Bind PSP (novedades de la empresa, decisiones, reestructuraciones, riesgos).
- ❌ **DESCARTAR (con motivo, sin abrir) — ruido residual REAL observado en el smoke test 2026-07-14:**
  - **Invitaciones de calendario:** llegan del mail del organizador (no de `calendar-notification@`), asunto empieza con `Invitación:` / `Invitación actualizada:` / `Invitation:` → descartar por asunto.
  - **Minutas de Gemini reenviadas por personas:** asunto empieza con `Minuta:` → "cubierto por /sync_meetings".
  - **Marketing de dominios conservados:** ej. `soluciones@coelsa.com.ar` con promos (E-CHEQ etc.) — el dominio no alcanza, mirar el asunto.
  - **RRHH/capital humano:** `capitalhumano@...` (ciclos de evaluación, beneficios) y cualquier trámite personal del PM (privacidad, regla dura 7).
  - Notificaciones automáticas residuales (Jira, CI, monitoreo, apps), Workvivo, newsletters, spam.
- Ante la duda con un remitente desconocido y asunto que suene a negocio → ANALIZAR (falso positivo barato > conocimiento perdido).

**Capa 3 — Lectura completa solo de lo que pasa.** `get_thread` de a UN thread por vez. En threads largos ya vistos en barridos anteriores, leé solo los mensajes nuevos desde el último barrido.

### Archivos de control y destino

- **[`wiki/1_proyectos/logs_sync/log_mails.md`](../../../wiki/1_proyectos/logs_sync/log_mails.md)** — store personal de dedupe: fecha, threadId y asunto de cada thread ya analizado + contador agregado de descartados. **Leelo siempre antes de arrancar.**
- **[`wiki/1_proyectos/contexto_vivo/index.md`](../../../wiki/1_proyectos/contexto_vivo/index.md)** — leelo también antes de arrancar, para no capturar dos veces algo ya `capturado`/`en_cola` sobre el mismo tema (incluido lo que haya dejado `/sync_meetings`).
- **`wiki/1_proyectos/tareas.md`** (personal) y el `proyecto.md`/`gaps.md`/`decisiones.md` del proyecto afectado — escritura **directa**, nunca vía `contexto_vivo/`.
- **Todo lo demás que esta skill aprenda para el canon** (`3_recursos/detalle_productos/`, `2_areas/clientes/`, `2_areas/direccion/oportunidades.md`, `2_areas/direccion/decisiones.md`, `2_areas/gaps_y_preguntas.md`, `2_areas/overview_empresa/`) **nace como item en `wiki/1_proyectos/contexto_vivo/`** — nunca directo. Ver Paso 3.

### Jira (escritura de comentarios)

`addCommentToJiraIssue` (si no está: `ToolSearch query:"select:addCommentToJiraIssue"`), instancia `bindpsp.atlassian.net`, cloudId `d07593ee-e5cd-4b6c-a371-d360063c167b`, IDEAs del espacio `PRD`.

## ⚖️ Reglas duras

1. **Comentario en Jira: auto-post, pero solo en modo incremental/puntual.** Toda novedad sobre un proyecto vivo genera comentario en su IDEA sin pedir confirmación. En modo `backfill` NUNCA se comenta — la novedad ya es vieja y sería ruido.
2. **Un solo comentario por PRD por corrida**, consolidando todas las novedades de todos los mails del día sobre esa IDEA.
3. **Delta, no volcado:** antes de escribir en la wiki, leé lo que el destino ya dice; solo agregá lo nuevo. Nunca guardes el mail entero — se destila.
4. **IDEAs nuevas: solo proponer.** Al reporte con título sugerido, problema y evidencia. NUNCA crear el ticket en Jira.
5. **No pisar a las otras skills:** no toques changelog de releases (`/sync_releases`), ni `<producto>/apis_expuestas/` (`/sync_web`), ni `2_areas/overview_productos/*_overview.md` (escritura restringida al usuario), ni la carga/baja de clientes en `log_clientes.md` (eso es de `/sync_customers` desde Notion — esta skill solo complementa fichas ya existentes, ver Paso 3a-bis).
6. **Gmail es solo-lectura:** nunca crear labels, marcar leídos, archivar, mover, responder ni draftear.
7. **Privacidad:** mails personales, de RRHH o sobre temas de personas se ignoran por completo — ni a la wiki ni al log de temas.
8. **Nombres dudosos:** ante un cliente/producto que no matchee contra `wiki/2_areas/clientes/` ni los productos conocidos, registralo como gap con el texto literal — no lo "corrijas" inventando.

## 🏃 Pipeline

### Paso 0 — Estado y modo

0. Leé `identidad.local.md` (raíz del repo) para resolver el campo `email` — es la cuenta de Gmail sobre la que corre toda la skill (query, dedupe de remitente propio, etc.). Nunca asumas ni hardcodees un mail.
1. Leé [`wiki/1_proyectos/logs_sync/log_mails.md`](../../../wiki/1_proyectos/logs_sync/log_mails.md): fecha/hora del último barrido, threadIds ya analizados, pendientes. Leé también [`contexto_vivo/index.md`](../../../wiki/1_proyectos/contexto_vivo/index.md) para no duplicar un item ya capturado.
2. **Modo incremental (sin argumento — el de la scheduled action):** ventana = desde la fecha del último barrido (inclusive) hasta hoy. Cubre fines de semana y días salteados — nunca asumas "solo ayer". No interactivo: procesá todo el delta sin preguntas.
3. **Modo `backfill [N]`:** hasta N días atrás (default 30, tope 31). Cronológico viejo→nuevo. Sin comentarios Jira (regla dura 1). Interactivo: tandas de ~10 threads con checkpoint al usuario; commit por tanda.
4. **Modo puntual (`YYYY-MM-DD`):** solo ese día. Comentarios Jira permitidos si es de los últimos 7 días.

### Paso 1 — Descubrimiento + triage

1. `search_threads` con la query filtrada de la Capa 1 sobre la ventana.
2. Triage por metadata (Capa 2) sobre los resultados.
3. **Dedupe por threadId** contra el log de control (un thread ya analizado solo se reabre si tiene mensajes nuevos).
4. Sin threads nuevos para analizar → reporte de una línea "sin novedades desde <último barrido>" (más el conteo de descartados) y fin — actualizá igual la cabecera del log.

### Paso 2 — Lectura y análisis, UN thread por vez

Fetch con `get_thread` y análisis con mirada de copiloto PM. Extraé y clasificá cada hallazgo en:

- **(a) Conocimiento de producto** (funcionamiento, configuración, lecciones aprendidas de tickets con Coelsa/GP, contexto de procesadores/clientes, aprendizaje no técnico de otras áreas) → Paso 3a.
- **(a-bis) Novedad o complemento sobre un cliente conocido** (nuevo dato de negocio, cambio de modelo/pricing/volumen, riesgo de churn, particularidad operativa) → Paso 3a-bis.
- **(b) Novedad sobre proyecto vivo** (decisión, cambio de alcance, bloqueo, avance, riesgo) — match contra la tabla maestra de [`wiki/1_proyectos/index.md`](../../../wiki/1_proyectos/index.md) §2, que resuelve la ruta real de cada IDEA (nunca asumas `1_proyectos/prd-XXX_<slug>/` directo) → Pasos 3b + 3c.
- **(c) Acción donde Producto queda responsable** (pedido de cliente importante, prerequisito de proyecto, seguimiento comprometido por mail) → Paso 3d.
- **(d) Candidata a IDEA nueva de backlog** (proyecto nuevo a analizar) → Paso 3e (regla dura 4: nunca crear el ticket en Jira).
- **(e) Decisión confirmada de empresa/producto** (no de un proyecto puntual — esas van directo al `decisiones.md` del proyecto en el Paso 3b) → item `tipo: decision` en `contexto_vivo/`.
- **(f) Gap o contradicción con la wiki** → item `tipo: gap` en `contexto_vivo/` (o el `gaps.md` del proyecto si es específico de uno).
- **(g) Contexto de empresa** (novedades organizacionales, comunicaciones oficiales) → item `tipo: conocimiento` en `contexto_vivo/`, `destino_propuesto` en `wiki/2_areas/overview_empresa/`.
- **(h) Riesgo latente de producto** → Seguimiento PM del `proyecto.md` afectado (directo) si hay proyecto que lo contenga, o item `tipo: riesgo` en `contexto_vivo/` si es de contexto fijo.

### Paso 3 — Escritura por destino

**3a. Conocimiento de producto → item `tipo: conocimiento` en `contexto_vivo/`.** `destino_propuesto` = el archivo temático candidato en `wiki/3_recursos/detalle_productos/<producto>/` (leé primero el `index.md` del producto); `tipo_destino` = `actualizar`/`crear` según corresponda. Cuerpo destilado, nunca el mail entero, con `> Fuente: Mail "<asunto>" — <remitente> (YYYY-MM-DD)`. Si contradice algo documentado, completá `contradice`. Aplica a 2+ productos → un item por producto (nunca `transversal/`); sin producto dueño claro → `destino_propuesto` en `arquitectura_sistema/`; si ni eso aplica, capturalo como `tipo: gap` (regla anti-cajón, la resuelve `/context_merge`).

**3a-bis. Novedad sobre un cliente conocido → item `tipo: conocimiento` en `contexto_vivo/`**, `destino_propuesto: 2_areas/clientes/casos_de_uso_clientes.md`. **Dedupe-first contra [`log_clientes.md`](../../../wiki/2_areas/clientes/log_clientes.md)** (léelo, no lo toques): el cliente debe existir ahí. El cuerpo trae el hallazgo fechado para que el merge lo fusione en `Particularidades / cronología` (mismo formato que `/sync_customers`) — nunca reemplaza la ficha entera. Si el cliente **no tiene ficha propia**, `tipo_destino: crear` con `Fuente: mail, no brochure de Notion` explícito en el cuerpo. Si el cliente **no aparece en absoluto** en `log_clientes.md` → capturalo como `tipo: gap` para que `/sync_customers` lo levante en su próximo barrido de Notion. **Esta skill nunca toca `log_clientes.md`** — la carga/baja de clientes sigue siendo dominio exclusivo de `/sync_customers`.

**3b. Actualizar el `proyecto.md`** del proyecto vivo afectado — **escritura directa**, `1_proyectos/` no pasa por `contexto_vivo/`: decisiones → Decisiones; riesgos/pendientes → Seguimiento PM; y una entrada `## Mail YYYY-MM-DD — <asunto>` en "Notas de sesiones" con qué se comunicó, qué se resolvió y qué quedó abierto. Resumen ejecutivo solo si la foto cambió. **Altitud correcta:** específico de una IDEA → `proyecto.md` del miembro; transversal a varios miembros de un mismo proyecto general → `proyecto.md` del padre, sin duplicarlo en cada miembro. Si hubo novedad real, sumá un item `tipo: iniciativa` en `contexto_vivo/` (con `pm_destino` si el proyecto no es tuyo) — ver CLAUDE.md.

**3c. Comentario en la IDEA de Jira** (solo incremental/puntual — regla dura 1): un comentario por PRD consolidando las novedades del día, redactado como PM (qué se definió/detectó y qué implica), citando asunto y fecha. Cierre estándar: `— Registrado automáticamente por el Cerebro desde el mail "<asunto>" (YYYY-MM-DD).` Acción externa a Jira, no pasa por `contexto_vivo/`.

**3d. Registrar la acción en `wiki/1_proyectos/tareas.md`** (backlog **personal** — escritura directa): ID correlativo `T-NNN`, tarea, producto/proyecto, interesados, urgencia (🔴/🟡/🟢), fecha detectada, fecha límite si el mail la da (si no `—`), fuente, estado `Pendiente`. **Dedupe primero:** si ya está trackeada, actualizá su fila. Si está ligada a un proyecto vivo, referenciala por ID desde "Seguimiento PM" de su `proyecto.md`. Si la tarea es de interés de **todo el equipo**, sumá además un item `tipo: tarea_equipo` en `contexto_vivo/`. Urgencia 🔴 = destacada arriba del reporte.

**3e. Candidata a IDEA nueva → item `tipo: oportunidad` en `contexto_vivo/`**, `destino_propuesto: 2_areas/direccion/oportunidades.md`. Cuerpo: oportunidad, producto, origen (`Mail "<asunto>" (YYYY-MM-DD)`), señal de demanda (quién la pidió/cuantificó), foco estratégico que alimentaría (o `—`). Nunca crea el ticket en Jira (regla dura 4).

### Paso 4 — Registro en el log de mails

En [`wiki/1_proyectos/logs_sync/log_mails.md`](../../../wiki/1_proyectos/logs_sync/log_mails.md):
- **Fila por thread ANALIZADO:** solo **Fecha | threadId | Asunto** — store de dedupe, no de narrativa (los temas y destinos ya quedaron en los items de `contexto_vivo/` y en el `proyecto.md` que se haya tocado).
- **Descartados: contador agregado por categoría por corrida** (ej. "2026-07-15: 34 descartados — 12 notificaciones, 9 RRHH/Workvivo, 8 promos, 5 Gemini/Meet"), NO fila por fila.

### Paso 5 — Reporte del barrido

Generá `outputs/reportes_sync/YYYY-MM-DD_reporte_mails.md` **y mostralo en la terminal**, en este orden:

1. **🔴 Urgencias y acciones de Producto** detectadas (las 🔴 primero).
2. **Novedades por proyecto** (qué se actualizó en cada `proyecto.md` + link al comentario Jira posteado).
3. **💡 Candidatas a IDEA nueva** (título sugerido, problema, evidencia — ya registradas en `oportunidades.md` por el Paso 3e).
4. **Hallazgos a wiki** (qué se aprendió y dónde quedó).
5. **Mails analizados / descartados** (tabla corta de analizados + conteo de descartados por categoría).
6. **Gaps nuevos.**

### Paso 6 — Cierre estándar

1. Actualizá la cabecera del log de dedupe (último barrido, modo, pendientes) y regenerá `contexto_vivo/index.md` si capturaste items nuevos.
2. Regla de integridad de índices: solo aplica a lo que tocaste directo en `1_proyectos/`. Los índices de `2_areas/`/`3_recursos/` los actualiza `/context_merge`.
3. **Sin git.** El commit del repo personal lo hace el hook `SessionStart` una vez al día.
4. En modo backfill: checkpoint con el usuario al cierre de cada tanda.

## 📌 Notas operativas

- **Threads, no mensajes:** la unidad de trabajo es el thread. Un hilo de ticket con Coelsa puede tener 15 mensajes — se analiza una vez y en barridos futuros solo sus mensajes nuevos.
- **Forwards y cadenas internas:** el conocimiento suele estar en el mensaje original forwardeado; los "FYI" de arriba rara vez agregan — no los destiles como si fueran contenido.
- **Adjuntos:** si el valor está en un adjunto (especificación, circular de Coelsa, manual), registralo como pendiente en el log y avisá en el reporte — no intentes descargarlo automáticamente.
- **Volumen observado (smoke test 2026-07-14):** ~30 threads devueltos para ~1.5 días con la query base (estimación del conector: ~200 matches en la ventana por el match a nivel thread) — el triage por metadata de la Capa 2 es esencial; esperá conservar una minoría (~5-10 threads/día con contenido real).
- **Ejemplos reales de lo que SÍ pasa el triage** (observados 2026-07-14): tickets de Coelsa (`icm@`/`soporte@coelsa.com.ar` — homologaciones, rechazos QR, transferencias pull), avisos de mantenimiento de Coelsa, cambios de recursos Fintexa, escalamientos internos (`🔥 Demoras críticas de Mastercard...`), threads de negocio con banco/compliance (apertura CC menores/PJ), negociaciones con proveedores (FaceTec).
- **Rutina agendada:** `sync-mails-daily` (L-V 9:30 ART, con jitter). Corre en paralelo con `sync-meetings-daily` (mismo horario) — sin conflicto de git posible, ninguna de las dos toca el repo (eso lo hace el hook `SessionStart` una vez al día).
- **Primera corrida real (pendiente):** validar la clasificación fina y el costo total; ajustar la lista de exclusión con lo observado.

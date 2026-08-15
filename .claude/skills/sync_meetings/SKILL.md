---
name: sync_meetings
description: Ingesta diaria de reuniones de Google Meet (minutas de Gemini). Descubre las reuniones en las que participó el PM (propias o de otros) vía Google Drive con red de seguridad por Gmail, lee la minuta completa del Doc de Gemini, y rutea lo aprendido con mirada de copiloto PM — conocimiento a detalle_productos/, novedades a los proyectos vivos de 1_proyectos/ + comentario automático en la IDEA de Jira, acciones del equipo de Producto al backlog global tareas.md, candidatas a IDEA nueva al banco de oportunidades (2_areas/direccion/oportunidades.md) + reporte. Registra cada reunión leída con sus temas en log_reuniones.md. Apto para scheduled action diaria (mañana temprano, procesa el delta desde el último barrido).
when_to_use: Se activa cuando el usuario ejecuta el comando de barra /sync_meetings (sin argumento para el delta diario; `backfill [días]` para historia; una fecha YYYY-MM-DD o URL de Doc para una corrida puntual), o como scheduled action diaria de lunes a viernes a primera hora.
disable-model-invocation: true
argument-hint: "[opcional: backfill [días] | YYYY-MM-DD | URL de Doc de Gemini]"
---

# 🎙️ INGESTA DIARIA DE REUNIONES: /sync_meetings

## 🎯 Por qué existe esta skill

El PM participa a diario en reuniones de Meet y Gemini genera minuta + transcripción de cada una — pero ese conocimiento muere en el correo y en Drive. Las conversaciones son la fuente más fresca del Cerebro: ahí se toman decisiones antes de que lleguen a Jira, se detectan urgencias de clientes, nacen ideas de backlog y queda claro quién debe hacer qué. `/sync_meetings` es el flujo de captura diario: corre cada mañana temprano, lee las reuniones del día anterior (o el delta acumulado) y las convierte en activos del Cerebro.

**Qué aporta que las otras skills no ven:** `/sync_jira_ideas` mira el estado de las IDEAs, `/sync_releases` el delivery por versión, `/debrief` las sesiones del PM con el Cerebro. Esta skill captura **lo que pasa en las conversaciones humanas** — es además la **única skill autorizada a escribir en Jira** (comentarios en IDEAs, decisión del usuario 2026-07-14).

## 🔌 Conexión técnica

### Fuentes
- **Google Drive (fuente primaria de contenido):** los Docs de Gemini — minuta detallada, y Doc de transcripción aparte si hace falta (link "Transcripción" dentro del `contentSnippet`). Las reuniones propias viven en `Meet Recordings` de Mi Unidad; las creadas por otros llegan como "Compartidos conmigo". La búsqueda de Drive cubre ambos orígenes en una pasada.
  - ⚠️ **Carga de tools:** el prefijo hash del conector varía entre sesiones — si fallan por nombre, `ToolSearch query:"google drive search file read content"` (keyword, no `select:`). Tools usados: `search_files`, `read_file_content`, `get_file_metadata`.
  - **Patrón de título verificado (2026-07-14):** `"<Título de la reunión> - YYYY/MM/DD HH:MM GMT-03:00 - Notas de Gemini"` (minuta en español) o `"... - Notes by Gemini"` (minuta en inglés — pasa cuando hay invitados que solo hablan inglés, ej. la daily técnica). Buscar SIEMPRE ambos sufijos.
  - **Query de `search_files` verificada funcionando** (encontró las 4 reuniones reales del 2026-07-13, 1:1 contra Gmail): `(title contains 'Notas de Gemini' or title contains 'Notes by Gemini') and createdTime > 'YYYY-MM-DDT00:00:00Z' and createdTime < 'YYYY-MM-DDT00:00:00Z'`. Rango exclusivo en UTC — Argentina es GMT-3, así que una reunión de última hora ART puede caer en el día UTC siguiente; usar el rango de días en UTC sin asumir que coincide con el calendario ART. `pageSize=20` alcanza para un día; en backfill iterar por `nextPageToken` o acotar por semana.
  - **Origen (propia/compartida), se deriva del resultado, sin query aparte:** `parentId` presente + `owner = pagomes@bind.com.ar` → **propia** (carpeta Meet Recordings, id `1lUQ_IvZn7KyRvzKtfjH8h3KGNGOn7UOe`). Sin `parentId` + `sharedWithMeTime` presente + `owner` ≠ usuario → **compartida**.
  - **Lectura:** `read_file_content(fileId)` devuelve la minuta completa en texto plano (resumen + próximos pasos con responsable + detalles con timestamps) — alcanza para el 90% de los casos. La transcripción cruda solo hace falta si un punto queda ambiguo y es relevante.
  - Si el conector no aparece en la sesión → avisar al usuario y correr en modo degradado (solo Gmail, ver abajo).
- **Gmail (detector / red de seguridad):** por cada reunión con notas llega un mail de `gemini-notes@google.com`, asunto `Notas: <título> <fecha>`, cuerpo con resumen + temas + action items con responsables + **link al Doc con su docId** (`https://docs.google.com/document/d/<docId>/...`). Tools: `search_threads` / `get_message` (si no están: `ToolSearch query:"gmail search threads message"`). Query detector: `from:gemini-notes@google.com after:YYYY/MM/DD before:YYYY/MM/DD`.
- **Jira (escritura de comentarios):** `addCommentToJiraIssue` (si no está: `ToolSearch query:"select:addCommentToJiraIssue"`), instancia `bindpsp.atlassian.net`, cloudId `d07593ee-e5cd-4b6c-a371-d360063c167b`, IDEAs del espacio `PRD`.

### Archivos de control y destino
- **[`wiki/1_proyectos/logs_sync/log_reuniones.md`](../../../wiki/1_proyectos/logs_sync/log_reuniones.md)** — store personal de dedupe: fecha, docId y título de cada reunión ya leída. **Leelo siempre antes de arrancar.**
- **[`wiki/1_proyectos/contexto_vivo/index.md`](../../../wiki/1_proyectos/contexto_vivo/index.md)** — leelo también antes de arrancar, para no capturar dos veces algo que ya está `capturado`/`en_cola` sobre el mismo tema.
- **`wiki/1_proyectos/tareas.md`** (personal) y el `proyecto.md`/`gaps.md`/`decisiones.md` del proyecto afectado — estos sí se escriben **directo**, nunca vía `contexto_vivo/`.
- **Todo lo demás que esta skill aprenda para el canon** (`3_recursos/detalle_productos/`, `2_areas/clientes/`, `2_areas/direccion/oportunidades.md`, `2_areas/direccion/decisiones.md`, `2_areas/gaps_y_preguntas.md`) **nace como item en `wiki/1_proyectos/contexto_vivo/`** — esta skill nunca escribe esas rutas directo, ni redactadas ni por atajo. Ver Paso 3.

## ⚖️ Reglas duras

1. **Comentario en Jira: auto-post, pero solo en modo incremental.** Toda novedad sobre un proyecto vivo genera comentario en su IDEA sin pedir confirmación (decisión del usuario). En modo `backfill` NUNCA se comenta en Jira — la novedad ya es vieja y sería ruido para el equipo; va a la wiki y al reporte.
2. **Un solo comentario por PRD por corrida**, consolidando todas las novedades del día sobre esa IDEA. Nunca N comentarios por N reuniones.
3. **Delta, no volcado:** antes de escribir en la wiki, leé lo que el destino ya dice; solo agregá lo nuevo. Nunca guardes la minuta entera — se destila.
4. **IDEAs nuevas: solo proponer.** Una idea que amerite backlog va al reporte con título sugerido, problema y evidencia. NUNCA crear el ticket en Jira.
5. **No pisar a las otras skills:** no toques el estado/entrega de las IDEAs (eso es de `/sync_jira_ideas`), ni el changelog de releases (`/sync_releases`), ni la carga/baja de clientes en `log_clientes.md` (eso es de `/sync_customers` desde Notion — esta skill solo complementa fichas ya existentes, ver Paso 3a-bis). Esta skill agrega contexto conversacional.
6. **Nunca escribir en `<producto>/apis_expuestas/`** (dominio exclusivo de `/sync_web`).
7. **Privacidad:** las minutas pueden contener temas personales/RRHH ajenos al negocio — se ignoran por completo; ni a la wiki ni al log de temas.

## 🏃 Pipeline

### Paso 0 — Estado y modo

1. Leé [`wiki/1_proyectos/logs_sync/log_reuniones.md`](../../../wiki/1_proyectos/logs_sync/log_reuniones.md): fecha/hora del último barrido, docIds ya ingestados, pendientes. Leé también [`contexto_vivo/index.md`](../../../wiki/1_proyectos/contexto_vivo/index.md) para no duplicar un item ya capturado sobre el mismo tema.
2. **Modo incremental (sin argumento — el de la scheduled action):** ventana = desde el día del último barrido (inclusive) hasta ayer (inclusive). Cubre solo fines de semana y días salteados — nunca asumas "solo ayer". No interactivo: procesá todo el delta sin preguntas.
3. **Modo `backfill [N]`:** hasta N días atrás (default 30, tope 31). Cronológico viejo→nuevo. Sin comentarios Jira (regla dura 1). Interactivo: tandas de ~5 reuniones con checkpoint al usuario; commit por tanda.
4. **Modo puntual (`YYYY-MM-DD` o URL de Doc):** solo ese día / ese Doc. Comentarios Jira permitidos si la reunión es de los últimos 7 días.

### Paso 1 — Descubrimiento de reuniones

1. **Drive:** buscá Docs con patrón de título de Gemini (`"Notas de Gemini"` / `"Notes by Gemini"`) creados dentro de la ventana. Registrá origen: **propia** (Mi Unidad / Meet Recordings) o **compartida** (Compartidos conmigo / owner ≠ usuario).
2. **Cross-check Gmail (1 llamada, siempre):** `search_threads` con `from:gemini-notes@google.com after:X before:Y`. Toda reunión presente en el mail pero ausente del resultado de Drive (la indexación de "Compartidos conmigo" puede demorar) se recupera igual: extraé el docId del link del mail (`get_message` → href `document/d/<docId>`) y hacé fetch directo del Doc.
3. **Dedupe por docId** contra el log de control. Sin reuniones nuevas → reporte de una línea "sin novedades desde <último barrido>" y fin (actualizá igual la cabecera del log).

### Paso 2 — Lectura y análisis, UNA reunión por vez

1. **Fetch del Doc completo** (minuta detallada de Gemini). Si la minuta es ambigua en un punto que importa (ej. "un ticket del cliente" sin nombres) y el Doc referencia una transcripción, abrila y buscá solo ese pasaje. Si aun así queda ambiguo → registralo como gap, no inventes.
2. **Triage liviano para recurrentes operativas** (ej. "Daily Equipo Técnico Bind PSP"): lectura rápida en diagonal; escala a análisis completo SOLO si aparece decisión, urgencia de cliente o riesgo. Si no: fila en el log con temas y nada más (motivo: "recurrente operativa, sin excepciones").
3. **Análisis con mirada de copiloto PM** — extraé y clasificá cada hallazgo en:
   - **(a) Conocimiento de producto** (mecánica, configuración, comportamiento, contexto de procesadores/clientes, aprendizaje no técnico de otras áreas) → Paso 3a.
   - **(a-bis) Novedad o complemento sobre un cliente conocido** (nuevo dato de negocio, cambio de modelo/pricing/volumen, riesgo de churn, particularidad operativa) → Paso 3a-bis.
   - **(b) Novedad sobre proyecto vivo** (decisión, cambio de alcance, bloqueo, avance, riesgo) — match contra la tabla maestra de [`wiki/1_proyectos/index.md`](../../../wiki/1_proyectos/index.md) §2, que resuelve la ruta real de cada IDEA (nunca asumas `1_proyectos/prd-XXX_<slug>/` directo) → Pasos 3b + 3c.
   - **(c) Acción donde Producto queda responsable** (desarrollo urgente por problema de cliente, prerequisito para empujar un proyecto, seguimiento comprometido) → Paso 3d.
   - **(d) Candidata a IDEA nueva de backlog** → Paso 3e (regla dura 4: nunca crear el ticket en Jira).
   - **(e) Decisión confirmada de contexto fijo** (no de un proyecto puntual — esas van directo al `decisiones.md` del proyecto en el Paso 3b) → item `tipo: decision` en `contexto_vivo/`.
   - **(f) Gap o contradicción con la wiki** → item `tipo: gap` en `contexto_vivo/` (o el `gaps.md` del proyecto si es específico de uno).

### Paso 3 — Escritura por destino

**3a. Conocimiento de producto → item `tipo: conocimiento` en `contexto_vivo/`.** `destino_propuesto` = el archivo temático candidato en `wiki/3_recursos/detalle_productos/<producto>/` (leé primero el `index.md` del producto para elegir bien); `tipo_destino` = `actualizar` si ya existe algo del tema, `crear` si no. El cuerpo del item lleva el conocimiento ya destilado (nunca la minuta cruda), con `> Fuente: Reunión "<título>" (YYYY-MM-DD), minuta Gemini`. Si contradice algo ya documentado, completá `contradice` con la cita exacta. Aplica a 2+ productos → un item por producto afectado (nunca un archivo `transversal/`); sin producto dueño claro (infra/arquitectura) → `destino_propuesto` en `arquitectura_sistema/`; si ni eso aplica, capturalo igual con `tipo: gap` y preguntale al usuario (regla anti-cajón sigue aplicando, solo que ahora la resuelve `/context_merge` en vez de esta skill).

**3a-bis. Novedad sobre un cliente conocido → item `tipo: conocimiento` en `contexto_vivo/`**, `destino_propuesto: 2_areas/clientes/casos_de_uso_clientes.md`. **Dedupe-first contra [`log_clientes.md`](../../../wiki/2_areas/clientes/log_clientes.md)** (léelo, no lo toques): el cliente debe existir ahí. El cuerpo del item trae el hallazgo fechado, listo para que el merge lo fusione en `Particularidades / cronología` (mismo formato que usa `/sync_customers`) — nunca reemplaza la ficha entera. Si el cliente **no tiene ficha propia** todavía, marcá `tipo_destino: crear` y dejá explícito en el cuerpo `Fuente: reunión, no brochure de Notion`. Si el cliente **no aparece en absoluto** en `log_clientes.md` (posible cliente nuevo aún no cargado en Notion) → no propongas ficha, capturalo como `tipo: gap` para que `/sync_customers` lo levante en su próximo barrido de Notion. **Esta skill nunca toca `log_clientes.md`** — la carga/baja de clientes y sus columnas comerciales siguen siendo dominio exclusivo de `/sync_customers`.

**3b. Actualizar el `proyecto.md`** del proyecto vivo afectado — **esto sí es escritura directa**, `1_proyectos/` no pasa por `contexto_vivo/`: decisiones → sección Decisiones; riesgos/pendientes → Seguimiento PM; y una entrada `## Reunión YYYY-MM-DD — <título>` en "Notas de sesiones" con qué se habló del proyecto, qué se resolvió y qué quedó abierto. Actualizá el resumen ejecutivo solo si la foto cambió. **Altitud correcta:** si lo que se habló es específico de una IDEA, escribí en el `proyecto.md` del miembro; si es una decisión de arquitectura/riesgo que aplica a varios miembros de un mismo proyecto general, escribí en el `proyecto.md` del padre (§4/§5) en vez de duplicarlo en cada miembro. Si hubo una novedad real (no solo "sin cambios"), sumá además un item `tipo: iniciativa` en `contexto_vivo/` con `proyecto` completado (y `pm_destino` si el proyecto no es tuyo) — ver CLAUDE.md, "Items `tipo: iniciativa`".

**3c. Comentario en la IDEA de Jira** (solo modo incremental/puntual — regla dura 1): un comentario por PRD consolidando las novedades del día, redactado como PM (qué se definió/detectó y qué implica, no el minuto a minuto), citando reunión y fecha. Cierre estándar: `— Registrado automáticamente por el Cerebro desde la minuta de la reunión "<título>" (YYYY-MM-DD).` Acción externa a Jira, no a la wiki — no pasa por `contexto_vivo/`.

**3d. Registrar la acción en `wiki/1_proyectos/tareas.md`** (backlog **personal** — escritura directa): ID correlativo `T-NNN`, tarea, producto/proyecto relacionado, interesados, urgencia (🔴/🟡/🟢), fecha detectada, fecha límite si la minuta la da (si no `—`), fuente, estado `Pendiente`. **Dedupe primero:** si la acción ya está trackeada, actualizá su fila en vez de duplicar. Si está ligada a un proyecto vivo, referenciala por ID desde "Seguimiento PM" de su `proyecto.md`. Si la tarea es de interés de **todo el equipo** (no solo tuya), sumá además un item `tipo: tarea_equipo` en `contexto_vivo/` — el merge decide si entra a `wiki/2_areas/tareas.md`. Urgencia 🔴 = va destacada arriba del reporte.

**3e. Candidata a IDEA nueva → item `tipo: oportunidad` en `contexto_vivo/`**, `destino_propuesto: 2_areas/direccion/oportunidades.md`. Cuerpo: oportunidad, producto, origen (`Reunión "<título>" (YYYY-MM-DD)`), señal de demanda (quién la pidió/cuantificó), foco estratégico que alimentaría (o `—` si ninguno de los 3 vigentes). Nunca crea el ticket en Jira (regla dura 4).

**Decisión o gap de contexto fijo (no de un proyecto puntual) → item `tipo: decision` o `tipo: gap` en `contexto_vivo/`**, `destino_propuesto` en `2_areas/direccion/decisiones.md` o `2_areas/gaps_y_preguntas.md` según corresponda.

### Paso 4 — Registro en el log de reuniones

Fila por reunión en [`wiki/1_proyectos/logs_sync/log_reuniones.md`](../../../wiki/1_proyectos/logs_sync/log_reuniones.md): solo **Fecha | docId | Título** — es un store de dedupe, no de narrativa (los temas y destinos ya quedaron en los items de `contexto_vivo/` y en el `proyecto.md` que se haya tocado). Las excluidas por triage también se registran, para no releerlas.

### Paso 5 — Reporte del barrido

Generá `outputs/reportes_sync/YYYY-MM-DD_reporte_reuniones.md` **y mostralo en la terminal**, en este orden:

1. **🔴 Urgencias y acciones de Producto** detectadas (las nuevas de `tareas.md`, las 🔴 primero).
2. **Novedades por proyecto** (qué se actualizó en cada `proyecto.md` + link al comentario Jira posteado).
3. **💡 Candidatas a IDEA nueva** (título sugerido, problema, evidencia — ya registradas en `oportunidades.md` por el Paso 3e).
4. **Hallazgos a wiki** (qué se aprendió y dónde quedó).
5. **Reuniones leídas** (tabla corta: título, origen, tratamiento — completo/triage).
6. **Gaps nuevos.**

### Paso 6 — Cierre estándar

1. Actualizá la cabecera del log de dedupe (último barrido, modo, pendientes) y regenerá `contexto_vivo/index.md` si capturaste items nuevos.
2. Regla de integridad de índices: solo aplica a lo que tocaste directo en `1_proyectos/` (índices locales de proyectos, `1_proyectos/index.md`). Los índices de `2_areas/`/`3_recursos/` los actualiza `/context_merge`, no esta skill.
3. **Sin git.** El commit del repo personal lo hace el hook `SessionStart` una vez al día — no lo hagas vos.
4. En modo backfill: checkpoint con el usuario al cierre de cada tanda.

## 📌 Notas operativas

- **Volumen típico:** ~3-8 reuniones/día hábil (verificado vía Gmail 2026-07-14: ~5/día). Un backfill de 30 días ronda 60-120 reuniones — solo por tandas.
- **Las minutas de Gemini pueden venir en inglés** (ej. la daily técnica) — el análisis y todo lo escrito en el Cerebro va siempre en español.
- **La minuta puede contener errores de transcripción** (nombres de clientes/productos deformados). Ante un nombre dudoso, cruzá contra `wiki/2_areas/clientes/` y los productos conocidos antes de escribirlo; si no matchea nada, registralo como gap con el texto literal.
- **Reuniones sin minuta:** si el usuario menciona una reunión que no aparece (Gemini no estuvo activo), no hay fuente — sugerile usar `/debrief` para volcarla de memoria.
- **Primera corrida (pendiente):** confirmar tools reales del conector de Drive + patrón exacto de títulos de los Docs y actualizar esta SKILL.md (sección Conexión técnica) con lo aprendido.

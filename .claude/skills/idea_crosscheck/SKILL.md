---
name: idea_crosscheck
description: Revisión cruzada de la solución ya diseñada con los ojos de cada área de Bind PSP (Comercial, Soporte, Administración y recaudaciones, Impuestos y contabilidad, Fraude, Legales, Cumplimiento/PLD, IT, Clientes externos). Recorre un catálogo fijo de preguntas por área, responde si le afecta o no con el porqué, y convierte cada impacto en un requerimiento nuevo al alcance, una tarea previa al go-live (T-NNN) o una contingencia operativa. Se activa con /idea_crosscheck.
when_to_use: Se activa cuando el usuario ejecuta /idea_crosscheck, después de que /idea_solution cerró con el análisis aprobado (`-solution.md` en `Aprobado por PM`) y antes de /idea_risks y /idea_prd. En una alternativa del carril operativo (sin desarrollo), corre directo sobre el shaping aprobado (`-start.md`).
disable-model-invocation: true
argument-hint: "[nombre_corto_proyecto o PRD-XXX]"
---

# 🔀 REVISIÓN CRUZADA POR ÁREA: /idea_crosscheck

## Por qué existe esta skill

El fraude de Transferencias Pull de marzo 2026 no fue solo un bug. La funcionalidad salió a producción sin que Conciliación supiera que tenía que cuadrarla, sin monitoreo de negocio que avisara que algo andaba mal, y sin integración al motor antifraude. Ninguna de esas tres áreas estaba en la conversación antes del lanzamiento.

El Assessment de auditoría del banco posterior al incidente lo dijo explícito: la validación con legales, cumplimiento (PLD), riesgos y soporte antes de cada lanzamiento "no es obligatoria y genera vulnerabilidades operativas". Pidió formalizarla.

Esta skill es esa instancia formal. Se pone en los ojos de cada área de Bind PSP, una por una, y recorre la solución ya diseñada con las preguntas que esa área se haría. El objetivo es que ningún impacto se descubra en producción. Cada impacto sale de acá con destino concreto: algo que hay que construir (y entra al alcance), algo que hay que hacer antes de salir (y nace como tarea del PM), o algo con lo que se va a convivir (y alguien lo absorbe).

No reemplaza la conversación con cada área: la prepara. La respuesta de esta skill queda en `Contemplado pero no validado` hasta que el área la confirma.

## Cuándo NO usarla

- El análisis técnico-funcional todavía no está aprobado → [`/idea_solution`](../idea_solution/SKILL.md) primero. No se puede evaluar el impacto de algo que todavía no se sabe cómo funciona. Excepción: si la alternativa aprobada en [`/idea_start`](../idea_start/SKILL.md) es del carril operativo (sin desarrollo), esta skill corre directo sobre el `-start.md` — un cambio de proceso también impacta áreas.
- Ya hay un `-crosscheck.md` aprobado y la solución no cambió desde entonces → no hay nada que revisar. Si la solución cambió, sí: esta corrida lo actualiza in place (ver Paso 0).

## ⚖️ Reglas duras

1. **Gate de entrada.** El artefacto de arriba tiene que estar en `Aprobado por PM`: `-solution.md` (o `-start.md` en carril operativo). Si está en `Propuesta`, pará y ofrecé dos salidas: revisarlo y aprobarlo ahora, o volver a esa skill. Nunca se construye una revisión cruzada sobre una propuesta.
2. **Ninguna respuesta pelada.** Toda fila responde Sí, No o No aplica **más el porqué**, en una oración que alguien de esa área reconozca como su propio problema (ej. "Sí, porque aparece un estado nuevo de la operación que el cliente tiene que contemplar en su conciliación diaria").
   - El Sí/No **siempre contesta "¿hay algo que esta área tenga que atender?"**, no la pregunta textual. En las preguntas de capacidad ("¿Soporte puede ver…?", "¿se puede testear…?"), si la capacidad falta es **Sí** (hay impacto), y si ya existe es **No**. Así todo Sí tiene salida y todo No es "sin impacto", sin importar cómo esté redactada la pregunta.
   - **Sí** = hay un impacto real para el área.
   - **No** = la pregunta aplica y el impacto no ocurre.
   - **No aplica** = la pregunta, tal como está, no tiene sentido para este proyecto.
3. **Nunca se fabrica una respuesta.** Si no hay información para evaluar una pregunta, la fila queda `Pendiente` con la pregunta abierta — nunca con una explicación inventada para que la tabla quede completa.
4. **Conciliación, monitoreo y fraude se evalúan juntos, nunca por separado** (el patrón de causa raíz del incidente de marzo 2026). Si la solución genera un movimiento de fondos, un comprobante o un tipo de operación nuevo (pregunta A1), en ese mismo momento se responden A2 (conciliación), S4 y F3 (monitoreo), F1-F2 (fraude) e I1 (impuestos). Ninguna de esas filas se da por cerrada hasta que estén todas respondidas.
5. **El catálogo es un piso, no un menú.** Las 9 áreas y todas sus preguntas se recorren siempre. Si una pregunta no aplica, la fila se arma igual con "No aplica" y el motivo — la ausencia de una fila es indistinguible de un olvido. Ampliar el catálogo con preguntas específicas del proyecto está bien y se alienta; podarlo, nunca.
6. **Un requerimiento nuevo al alcance nunca entra solo.** Si un impacto pide construir algo que no está en el alcance vigente de `proyecto.md` §3, se presenta al PM como candidato. Entra al alcance solo con su OK literal. Si además necesita diseño funcional (un reporte nuevo, un estado nuevo, una integración), la skill lo dice y propone volver a `/idea_solution` antes de seguir — nunca lo diseña acá.
7. **Toda tarea previa al go-live nace como tarea del PM, en el momento.** Se da de alta en `wiki/1_proyectos/tareas.md` con ID `T-NNN` correlativo: el PM como responsable y el área como interesada, fuente = este crosscheck. Dedupe primero. `/idea_golive` después la toma, no la crea de nuevo.
8. **Los hechos los busca Claude; las decisiones son del PM.** No preguntes lo que ya responde la wiki, el `-solution.md` o el `-start.md` — presentalo como hecho con su cita para que el PM lo confirme. Preguntá solo lo que es una decisión suya o un dato que solo él o el área tienen.
9. **Todo queda en `Propuesta` hasta el OK literal del PM** (ver Paso 3).
10. **El documento es autocontenido.** Sin links a la wiki, sin nombres de archivo o de skill, sin jerga de proceso interno. Los `T-NNN` se citan solo en la columna de tarea, que `/idea_prd` no transcribe.
11. Todo output en español.

## Catálogo de preguntas de referencia por área

Adaptá la redacción al proyecto, nunca completes mecánicamente. Cada pregunta tiene un ID fijo — es la trazabilidad entre corridas y hacia `/idea_risks`.

**1. Comercial**
- C1 — ¿Cambia el pricing, el packaging o lo que se le puede prometer a un cliente?
- C2 — ¿Hace falta material de preventa o actualizar el perfil del cliente?
- C3 — ¿Hay clientes en pipeline cuya integración cambia por esto?

**2. Soporte / Operaciones e Integraciones**
- S1 — ¿Cambia lo que Soporte tiene que responder o diagnosticar, y hace falta actualizar guías o capacitar?
- S2 — ¿Aparecen errores o estados nuevos que Soporte va a ver en un reclamo y hoy no sabe interpretar?
- S3 — ¿Requiere credenciales, configuración o habilitación nueva por cliente o por ambiente?
- S4 — ¿Soporte puede darse cuenta —de forma agregada, no solo cuando llega un reclamo puntual— de que esto no está funcionando con normalidad, para escalarlo a tiempo? No alcanza con que pueda resolver sin escalar: el mínimo exigible es poder ver que algo anda mal, aunque la resolución dependa de otro equipo.
- S5 — ¿Por qué canales pueden llegar reclamos sobre esta funcionalidad (Soporte, comercial, directo del banco, redes), y todos saben a dónde derivarlos?
- S6 — ¿Queda registro suficiente de cada operación para responder un reclamo ante BCRA o Defensa del Consumidor?

**3. Administración y recaudaciones**
- A1 — ¿Genera movimientos de dinero, comprobantes o tipos de operación nuevos? *(dispara la regla dura 4)*
- A2 — ¿La herramienta de conciliación puede identificarlos y cuadrarlos desde el día 1 del go-live, o hace falta parametrizarla antes?
- A3 — ¿Impacta la liquidación a comercios (monto, momento, forma)?
- A4 — ¿Crea o modifica saldos? Si sí, ¿el control de ese saldo queda en un sistema interno de Bind, o depende de que un proveedor externo lo mueva sin control propio?

**4. Impuestos y contabilidad**
- I1 — ¿Cambia el cálculo o la imputación de impuestos sobre la operatoria (percepciones, retenciones, IIBB, IVA)?
- I2 — ¿Cambia la facturación, el costo que se le cobra al cliente o cómo se le cobra?
- I3 — ¿Cambia la registración contable o la información que se le reporta al fisco?

**5. Fraude**
- F1 — ¿Abre un vector de riesgo nuevo o cambia el perfil transaccional que se monitorea?
- F2 — ¿Hacen falta reglas, parámetros o límites nuevos en el motor antifraude?
- F3 — ¿Necesita un esquema de monitoreo operativo nuevo (tablero, alerta de anomalía de negocio) que hoy no existe?
- F4 — ¿Cambia la información disponible para responder un reclamo de fraude de otra entidad?

**6. Legales**
- L1 — ¿Requiere cambio contractual, anexo o consentimiento nuevo del cliente o del usuario final?
- L2 — ¿Cambian los términos y condiciones, o quién responde frente al cliente o a un tercero si la operación falla?

**7. Cumplimiento / PLD**
- P1 — ¿Tiene implicancias regulatorias BCRA (comunicaciones vigentes sobre PSP, fraude, medios de pago)?
- P2 — ¿Toca UIF/PLD: debida diligencia del cliente, monitoreo de operaciones inusuales, límites o reportes (ROS, RTE, RMTC)?
- P3 — ¿Toca datos personales o datos de tarjeta (protección de datos personales, PCI DSS)?
- P4 — ¿Genera o cambia una obligación de reportería regulatoria (BCRA, UIF, proveedor de listas/legajo)?

**8. IT**
- T1 — ¿Qué volumen adicional se espera, y el sistema está dimensionado (picos, batch, storage)?
- T2 — ¿Requiere accesos, secretos o cambios en la superficie expuesta (seguridad informática)?
- T3 — ¿Toca el modelo de datos, requiere migración o una política de retención nueva?
- T4 — ¿Hay tracking/logging suficiente para medir el criterio de éxito acordado en el shaping?
- T5 — ¿Se puede testear en staging con datos representativos, incluidos los casos de falla del proveedor?
- T6 — ¿Depende de un desarrollo de un proveedor externo, y con qué lead time?
- T7 — ¿Depende de credenciales o APIs que hoy administra solo el proveedor de tecnología, sin que Bind pueda ver o administrar qué consume cada cliente?

**9. Clientes externos en producción**
- E1 — ¿Es un breaking change para alguien ya integrado, y requiere que el cliente haga algo?
- E2 — ¿Hace falta preaviso, plan de comunicación y ventana de migración?
- E3 — ¿Hay que actualizar la documentación pública?

## 🏃 Pipeline

### Paso 0 — Contexto y gate de entrada

1. Resolvé la ruta real en [`wiki/1_proyectos/index.md`](../../../wiki/1_proyectos/index.md) §2 — nunca asumas `prd-XXX_<slug>/` directo.
2. **Gate de entrada (regla dura 1):** leé el frontmatter de `artefactos/{{nombre_corto_proyecto}}-solution.md` (o `-start.md` si el carril es operativo). Si no está en `Aprobado por PM`, pará acá. En carpetas legacy sin campo `estado`, preguntale al PM una sola vez si lo da por aprobado y registrá la respuesta en el historial de ese artefacto.
3. Leé completos:
   - `proyecto.md` — sobre todo §3 Alcance vigente: es lo que permite distinguir "ya está en alcance" de "requerimiento nuevo".
   - `-start.md` — alternativa aprobada, frontera del foco, criterio de éxito.
   - `-solution.md` — actores, contrato, errores (Sección 8), convivencia con lo existente (Sección 10), NFR (Sección 11).
   - `decisiones.md`, `gaps.md`, `riesgos.md` del proyecto; si es miembro de un proyecto general, el §4 del padre.
4. Contexto de áreas y de la auditoría:
   - `wiki/2_areas/overview_empresa/overview_equipo.md` — quién lidera cada área (el interesado de cada tarea).
   - `wiki/2_areas/direccion/oportunidades.md`, filas OP-022 a OP-025 (hallazgos del Assessment de auditoría).
   - `wiki/2_areas/riesgos.md` — riesgos generales que toquen este producto (ej. control del ledger).
   - `wiki/3_recursos/cumplimiento_normativo/index.md` y lo que aplique para el área 7.
   - `wiki/3_recursos/detalle_productos/<producto>/` si hace falta entender cómo funciona hoy lo que se toca.
   - `wiki/1_proyectos/contexto_vivo/index.md` — citando como no-canon lo que haya.
5. **Si ya existe `artefactos/{{nombre_corto_proyecto}}-crosscheck.md`**, leelo completo: esta corrida lo actualiza in place.
6. **Detección de desfasaje:** si el `-crosscheck.md` existente está `Aprobado por PM` pero su `basado_en` apunta a una versión anterior del `-solution.md` vigente, decile al PM qué cambió en la solución y qué filas pueden verse afectadas. Esta corrida revisa esas filas; el resto se confirma.

### Paso 1 — Recorrido por las 9 áreas

Una fila por cada pregunta del catálogo, en las 9 áreas, en orden. Por cada una, en este orden de preferencia:

- **✅ Resuelta desde fuentes** — la respuesta sale del `-solution.md`, el `-start.md` o la wiki. Se presenta con su cita para que el PM confirme o corrija.
- **❓ Pregunta al PM** — solo lo que es genuinamente suyo. Formato `❓ **C2** - **<título>**: <pregunta>` y en la línea siguiente `➡️ <tu recomendación>`. Nunca preguntes sin recomendar.
- **⏳ Pendiente con un área** — ni la wiki ni el PM lo saben; lo sabe el área. La fila queda `Pendiente` con la pregunta abierta, y se convierte en tarea del PM ("confirmar con <área> si …").

Presentá el recorrido por área, no las 9 de golpe: un área por bloque, así el PM puede corregir antes de que sigas. Aplicá la regla dura 4 apenas A1 da Sí.

### Paso 2 — Clasificación de cada impacto

Por cada fila con respuesta **Sí**, una de tres salidas, siempre explícita (si fue No o No aplica, va "—"):

- **Requerimiento en el alcance** — si ya está en el alcance vigente, nombrá la funcionalidad tal como aparece ahí. Si es nuevo, marcalo `🆕 Requerimiento nuevo` y aplicá la regla dura 6.
- **Tarea previa al go-live** — algo a hacer antes de producción que no es desarrollo: capacitar a un área, actualizar documentación, comunicar a clientes integrados, cargar una configuración, validar un cálculo con el área. Nace como `T-NNN` (regla dura 7).
- **Contingencia operativa** — se convive con el impacto; decir cómo y quién lo absorbe. Una contingencia sin dueño claro es insumo directo de `/idea_risks`.

Y un **Estado** por fila: `Pendiente` | `Contemplado pero no validado` | `Contemplado y validado`. "Validado" significa que el área lo confirmó, no que se asumió.

### Paso 3 — Revisión iterativa con el PM

**No se da por cerrado en la primera pasada.** Presentá el documento completo, destacando:
- cada `🆕 Requerimiento nuevo` — necesita el OK literal del PM para entrar al alcance, y su decisión sobre si hace falta volver a `/idea_solution`;
- cada fila `Pendiente` que el PM pueda resolver ahí mismo;
- el resumen de impactos que va a consolidar el PRD.

Si el PM corrige algo, reescribí la fila limpia — nunca una nota "corregido" superpuesta. Cada vuelta suma una entrada al historial de revisiones. Recién con su confirmación literal ("aprobado", "ok, cerralo") el artefacto pasa a `Aprobado por PM (YYYY-MM-DD)`. Ni el silencio ni "dale, seguí" cuentan como aprobación. Si el PM quiere avanzar sin aprobar, el artefacto queda en `Propuesta` y la próxima skill de la cadena lo va a frenar en su gate.

Las filas `Pendiente` no impiden aprobar: el PM aprueba la revisión tal como está, con esas preguntas abiertas y sus tareas creadas.

## 📄 Formato de salida

Usá [`references/TEMPLATE.md`](references/TEMPLATE.md): frontmatter con `estado` y `basado_en`, **Resumen de impactos** al tope (filas con Sí o Pendiente + una línea por cada área sin impacto — es lo que `/idea_prd` transcribe), una tabla por área, y el historial de revisiones al pie.

Ver [`references/EXAMPLE.md`](references/EXAMPLE.md) para un ejemplo completo (cifras ilustrativas).

## ✅ Checklist de calidad

- [ ] El artefacto de arriba estaba en `Aprobado por PM` antes de empezar (Paso 0.2)
- [ ] Se recorrieron las 9 áreas y todas las preguntas del catálogo — ninguna fila falta sin explicación
- [ ] Ninguna fila tiene un Sí/No/No aplica sin el porqué, ni un porqué fabricado donde el dato no se conocía
- [ ] Si A1 dio Sí, A2, S4, F1, F2, F3 e I1 se respondieron en el mismo momento (regla dura 4)
- [ ] Cada Sí tiene su salida clasificada (requerimiento / tarea previa al go-live / contingencia)
- [ ] Todo `🆕 Requerimiento nuevo` tiene la decisión explícita del PM (entra / no entra / vuelve a `/idea_solution`)
- [ ] Toda tarea previa al go-live y toda fila `Pendiente` con un área tiene su `T-NNN` en `tareas.md`, sin duplicados
- [ ] El Resumen de impactos está al tope y es consistente con las tablas
- [ ] El documento es autocontenido: sin links a wiki, sin nombres de archivo/skill, sin jerga interna
- [ ] El PM dio su OK literal y el frontmatter dice `Aprobado por PM (YYYY-MM-DD)`, o quedó explícito en `Propuesta`

## Paso 4 — Cierre estándar

1. **Persistir** en `artefactos/{{nombre_corto_proyecto}}-crosscheck.md` — `{{nombre_corto_proyecto}}` es la carpeta si nació de `/idea_start`, o el `<slug>` después de `prd-XXX_` en carpetas legacy. Frontmatter: `version`, `estado`, `basado_en` (versiones del `-start.md` y del `-solution.md` usadas). Si ya existía, se reescribe limpio y se suma una entrada al historial; si estaba aprobado y cambió el cuerpo, vuelve a `Propuesta` con versión nueva hasta la re-aprobación.
2. **Requerimientos nuevos:**
   - Aprobados por el PM → se suman a §3 Alcance de `proyecto.md` y se registran en `decisiones.md` (formato `## [YYYY-MM-DD] — <título>` con Contexto/Problema, Decisión tomada, Impacto, Estado).
   - Sin decisión del PM → `gaps.md`, severidad Alta, marcado como bloqueante del alcance del PRD.
   - Si el PM decidió volver a `/idea_solution`, anotalo como próximo paso en §7 Seguimiento PM.
3. **Tareas** → `wiki/1_proyectos/tareas.md` (regla dura 7), referenciadas desde §7 Seguimiento PM de `proyecto.md`. Si alguna es de interés de todo el equipo, sumá además un item `tipo: tarea_equipo` en `contexto_vivo/`.
4. **Filas `Pendiente`** → además de su tarea, una entrada en `gaps.md` si la falta de respuesta es una inconsistencia con lo ya documentado (no si es solo algo por consultar — eso ya es la tarea).
5. **`proyecto.md` §4 Entrega** → fila del crosscheck en la tabla "Cadena de artefactos" con versión y estado. Nota en §8 Notas de sesiones.
6. **Conocimiento de contexto fijo** que haya surgido (ej. cómo concilia hoy Administración un tipo de operación) → item `tipo: conocimiento` en `contexto_vivo/`, nunca directo al canon.
7. **Índices:** `wiki/1_proyectos/index.md` §2 (Última actividad). Sin changelog y sin git.
8. Siguiente paso sugerido: [`/idea_risks`](../idea_risks/SKILL.md) — toma las filas `Pendiente` y las contingencias sin dueño de este artefacto como insumo directo. Si el PM decidió sumar un requerimiento nuevo que necesita diseño, antes va [`/idea_solution`](../idea_solution/SKILL.md).

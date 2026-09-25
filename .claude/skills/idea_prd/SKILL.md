---
name: idea_prd
description: Define el alcance y consolida todo lo ya trabajado y aprobado en la cadena de discovery (shaping, análisis de solución, revisión cruzada por área, riesgos) en el Product Requirements Document — el documento final, autocontenido, que leen ingeniería, stakeholders y externos, y que va a la descripción de la IDEA en Jira. Se activa con /idea_prd.
when_to_use: Se activa cuando el usuario ejecuta /idea_prd, después de /idea_risks, con el shaping, el análisis de solución, la revisión cruzada y los riesgos ya aprobados por el PM. Es el último paso de especificación antes de /idea_us.
disable-model-invocation: true
argument-hint: "[PRD-XXX o nombre de la iniciativa a especificar]"
---

<!-- Adaptado de product-on-purpose/pm-skills (deliver-prd), licencia Apache-2.0. https://github.com/product-on-purpose/pm-skills -->
<!-- Estructura de Alineación de la solución adaptada del PRD Template de un Head of Product de Stripe (mayo 2025). -->

# 📋 PRD FORMAL: /idea_prd

## Por qué existe esta skill

`proyecto.md` en `wiki/1_proyectos/` es el estado vivo de una IDEA — decisiones, gaps, seguimiento PM, todo en evolución constante. Un PRD es otra cosa: un documento **congelado en un momento dado**, pensado para que ingeniería, QA, stakeholders y externos a Bind PSP lean una sola vez y entiendan qué se va a construir, por qué, dónde están los límites del alcance, a quién impacta y qué riesgos tiene. Es el documento que va a la descripción de la IDEA en Jira.

Esta skill **no analiza: consolida.** Cada pieza del PRD ya fue trabajada y aprobada por el PM en su propio paso de la cadena:

| Sección del PRD | Viene de |
|---|---|
| Problema, Contexto, Objetivos, Caso de negocio | El shaping aprobado (`/idea_start`) |
| Resumen de la solución, Flujos y Lógica clave, Definiciones | El análisis técnico-funcional aprobado (`/idea_solution`) |
| Impactos por área | La revisión cruzada aprobada (`/idea_crosscheck`) |
| Riesgos | El relevamiento de riesgos aprobado (`/idea_risks`) |

Lo único que se decide acá es el **alcance**: qué entra, qué no y qué se difiere, priorizado con MoSCoW (Paso 7). Todo lo demás se destila, sin re-analizar ni inventar.

## Cuándo NO usarla

- El problema, el foco o la alternativa no están aprobados → [`/idea_start`](../idea_start/SKILL.md).
- El análisis técnico-funcional no existe o no está aprobado → [`/idea_solution`](../idea_solution/SKILL.md). Excepción: en una alternativa del carril operativo (sin desarrollo), el PRD es liviano y se arma sin `-solution.md`.
- La revisión cruzada por área no se hizo o no está aprobada → [`/idea_crosscheck`](../idea_crosscheck/SKILL.md). El PRD consolida sus impactos; no los descubre.
- Los riesgos no se relevaron o no están aprobados → [`/idea_risks`](../idea_risks/SKILL.md).
- Solo hace falta bajar trabajo a historias para un sprint, sin documento de especificación → [`/idea_us`](../idea_us/SKILL.md).
- Lo que se necesita es registrar una decisión técnica o arquitectónica puntual, no especificar una iniciativa completa.

## ⚖️ Reglas duras

1. **Gate de entrada.** Todos los artefactos de arriba tienen que estar en `Aprobado por PM`: `-start.md`, `-solution.md` (salvo carril operativo), `-crosscheck.md` y `-risks.md`. Si alguno está en `Propuesta` o no existe, pará, decí cuál y ofrecé dos salidas: revisarlo y aprobarlo ahora, o volver a esa skill. Nunca se escribe una sección del PRD a partir de una propuesta.
2. **Consolidar, no re-analizar.** Impactos por área y Riesgos se transcriben desde `-crosscheck.md` y `-risks.md` tal como quedaron aprobados — nunca se agrega, se quita ni se reinterpreta una fila acá. Si al consolidar aparece algo que falta o no cierra, no se corrige en el PRD: se le avisa al PM y se propone volver a la skill que lo produjo.
3. **No prescribas implementación de bajo nivel.** El PRD no elige lenguaje, framework, esquema de base de datos ni topología de despliegue. Explicar cómo funciona la solución de cara al negocio (quiénes participan, en qué orden pasan las cosas, qué ocurre cuando algo falla) **no es prescribir implementación** — es justo lo que exige el Paso 3.
4. **Todo objetivo es SMART y medible.** Alguien tiene que poder verificar en el futuro si se cumplió.
5. **Alcance explícito**: qué entra, qué no entra y qué queda diferido — nunca implícito. La Alineación de la solución dibuja el perímetro, no llena el interior: el equipo decide cómo construir dentro de ese borde.
6. **Nombrá la solución por lo que efectivamente se construye**, no por una abstracción ambigua que suene a un proceso o servicio existente (ej. "nuevas funcionalidades por API para favorecer X", no "el proceso de X").
7. **El PRD es siempre autocontenido, sin excepción.** Lo lee alguien sin acceso a este sistema: sin links a la wiki, sin nombres de archivo o de skill, sin códigos de ticket (PRD-XXX, T-NNN) usados como si el lector los reconociera, sin jerga de proceso interno ("gap registrado en...", "según el artefacto..."). La trazabilidad hacia la wiki vive en el Paso 0 y en cómo `proyecto.md` referencia al PRD, nunca en el cuerpo.
8. **Legible en menos de 15 minutos** y dentro del límite práctico de ~28KB de la descripción de Jira. Si no entra, el alcance es demasiado grande para un solo PRD. Por eso Impactos por área lleva solo las filas con impacto, no la revisión completa (Paso 8).
9. **Todo queda en `Propuesta` hasta el OK literal del PM** (Paso 10).
10. Todo output en español.

## 🏃 Pipeline

### Paso 0 — Contexto y gate de entrada

1. Resolvé la ruta real de la IDEA en [`wiki/1_proyectos/index.md`](../../../wiki/1_proyectos/index.md) §2 — nunca asumas `prd-XXX_<slug>/` directo. Leé `proyecto.md` completo, en particular §3 Alcance vigente (incluye los requerimientos nuevos que sumó la revisión cruzada) y la tabla "Cadena de artefactos" de §4.
2. **Gate de entrada (regla dura 1):** leé el frontmatter (`estado`, `version`) de `-start.md`, `-solution.md`, `-crosscheck.md` y `-risks.md`. En carpetas legacy sin campo `estado`, preguntale al PM una sola vez si da cada uno por aprobado y registralo en el historial de ese artefacto.
3. **Detección de desfasaje:** compará el `basado_en` de cada artefacto con la versión vigente de los de arriba (ej. un `-crosscheck.md` aprobado sobre la versión 1.0 del `-solution.md` cuando ya existe la 1.1). Si hay desfasaje, decíselo al PM con qué cambió y proponé revisar el artefacto afectado antes de consolidar. No lo re-abras solo.
4. **Si es miembro de un proyecto general**, leé el §4 "Definiciones y decisiones heredadas" del `proyecto.md` padre — decisiones ya cerradas que el PRD no re-litiga.
5. Leé completos los cuatro artefactos de la cadena:
   - `-start.md` — problema, foco, alternativa elegida y descartes, criterio de éxito, tamaño preliminar.
   - `-solution.md` — insumo de los Pasos 3, 6 y 7.
   - `-crosscheck.md` — insumo del Paso 8 (su "Resumen de impactos") y de los requerimientos nuevos del Paso 7.
   - `-risks.md` — insumo del Paso 9 (su "Resumen para el PRD").
6. `decisiones.md` y `gaps.md`: **si hay un gap abierto marcado como bloqueante del alcance** (típicamente un requerimiento nuevo de la revisión cruzada sin decisión del PM), pará y resolvelo con el PM antes del Paso 7.
7. Contexto de producto y estratégico: `wiki/2_areas/overview_productos/overview_<producto>.md`, `wiki/2_areas/direccion/north_star.md`, `wiki/2_areas/direccion/estrategia/`.
8. **Si ya existe `artefactos/{{nombre_corto_proyecto}}-prd.md`**, leelo completo — esta corrida lo actualiza in place.

### Paso 1 — Problema

Recapitulación breve del problema que se resuelve u oportunidad que se aprovecha, en prosa propia, destilada del shaping. El lector tiene que entender el *por qué* antes de llegar al *qué*.

### Paso 2 — Contexto

Por qué atacar esto ahora: de dónde surgió, si es urgente, si es parte de algo más grande. Conectá con el foco/OKR vigente si aplica. Si el shaping evaluó alternativas, una o dos líneas de por qué se eligió esta y no las otras.

### Paso 3 — Resumen de la solución planteada

Qué se construye y cómo funciona, de cara al negocio. Nombrala por lo que efectivamente se construye (regla dura 6).

No alcanza con describir qué es: explicá **cómo se resuelve el problema** — quiénes participan, en qué orden ocurren las cosas, y qué pasa cuando algo falla (consecuencia de negocio, no manejo técnico del error). Destilalo del `-solution.md` sin mencionarlo ni linkearlo, y sin bajar al detalle que le corresponde a ese documento: nada de contrato de endpoints, tablas de reintentos ni mapa de procedencia campo por campo. Si el lector no puede explicar con sus palabras cómo se resuelve el problema, la sección quedó incompleta.

### Paso 4 — Objetivos

Objetivos y beneficios de negocio u operativos, SMART y medibles, anclados en el criterio de éxito que acordó el shaping (misma métrica, baseline y meta).

### Paso 5 — Caso de negocio

Beneficio monetizado esperado contra el costo de construir, desde el shaping (medida e impacto del problema, tamaño preliminar de la alternativa). Si `/idea_estimate` ya corrió, usá su número.

### Paso 6 — Definiciones, suposiciones y límites

Decisiones, limitantes, restricciones y situaciones que condicionaron el camino elegido — técnicas, regulatorias (BCRA/UIF/PCI DSS) y de proveedores. Fuente directa: las decisiones de diseño de la Sección 11 del `-solution.md` y los descartes del shaping, resumidos en prosa. Sumá acá todo concepto o taxonomía que el lector necesite para el resto del documento (tipos de cliente, modalidades de integración, estados de una operación) — definido una vez, no repartido.

### Paso 7 — Alineación de la solución (el alcance)

Es la única sección donde esta skill decide, y la decisión es del PM. Dibuja el perímetro: qué la compone, cómo se experimenta, qué reglas la gobiernan.

**Funcionalidades clave.** Todas las funcionalidades del proyecto, con etiqueta **MoSCoW** (Must/Should/Could/Won't) por item. **Traducí el alcance vigente de `proyecto.md` §3 y el roadmap ya acordado, no inventes una priorización nueva** — incluidos los requerimientos que sumó la revisión cruzada con el OK del PM. El corte entre 🔴 Must y el resto define el MVP. Desafiá el tamaño: si un componente puede salir solo, antes que el resto, decilo. Lo que no entra (⚫ Won't) lleva la razón si ayuda a entenderlo. Lo que se guarda para después pero condiciona cómo se construye hoy va a Consideraciones futuras.

**Flujos clave.** La experiencia end-to-end del cliente: prosa, diagrama, capturas o exploraciones de diseño — el formato que este proyecto necesite, destilado de los caminos del `-solution.md`.

**Lógica clave.** Reglas de negocio que deciden qué pasa en cada caso: escenarios comunes y casos borde. No es el contrato de endpoints ni el manejo técnico del error.

Presentá las Funcionalidades clave con su MoSCoW al PM **antes** de seguir — es la decisión central del PRD. Si el PM cambia una prioridad o el perímetro, registralo en `decisiones.md`.

### Paso 8 — Impactos por área

Transcribí el **Resumen de impactos** del `-crosscheck.md` aprobado:
- las áreas con impacto, fila por fila: el impacto, qué se propone (funcionalidad en el alcance, tarea previa al go-live o contingencia) y el estado;
- una línea por cada área evaluada sin impacto, con su motivo — así el lector ve que se revisaron las nueve, sin leer cada pregunta.

Adaptá solo la forma para que quede autocontenido: sin IDs de pregunta, sin `T-NNN`, y con las funcionalidades nombradas igual que en Funcionalidades clave. Nunca agregues, quites ni reinterpretes una fila (regla dura 2). La revisión completa, pregunta por pregunta, queda en el artefacto de la revisión cruzada.

### Paso 9 — Riesgos

Transcribí el **Resumen para el PRD** del `-risks.md` aprobado: riesgo, familia (entrega del proyecto / producto en producción), probabilidad, impacto y mitigación. Mismo criterio que el Paso 8: forma autocontenida, contenido intacto.

### Paso 10 — Revisión iterativa con el PM

**No se da por cerrado en la primera consolidación.** Presentá el PRD completo, no un resumen. Si el PM corrige algo:
- si es de alcance (Paso 7) o de redacción del PRD, se corrige acá: reescribí la sección limpia;
- si es de fondo sobre algo que viene de otro artefacto (un impacto, un riesgo, cómo funciona la solución), se corrige en su origen — proponé volver a esa skill, y después se re-consolida.

Cada vuelta suma una entrada al historial de revisiones. Recién con la confirmación literal del PM el PRD pasa a `Aprobado por PM (YYYY-MM-DD)`. Ni el silencio ni "dale, seguí" cuentan como aprobación.

## 📄 Formato de salida

Usá [`references/TEMPLATE.md`](references/TEMPLATE.md) — el estándar de PRD de la casa. En este orden: Problema; Contexto; Resumen de la solución planteada; Objetivos; Caso de negocio; Definiciones, suposiciones y límites; Alineación de la solución (Funcionalidades clave, Flujos clave, Lógica clave); Impactos por área; Riesgos.

Ver [`references/EXAMPLE.md`](references/EXAMPLE.md) para un ejemplo completo (cifras ilustrativas).

## ✅ Checklist de calidad

- [ ] Los cuatro artefactos de arriba estaban en `Aprobado por PM` y sin desfasaje de versiones (o el PM decidió explícitamente seguir)
- [ ] El problema y el "por qué ahora" están claramente articulados, consistentes con el shaping
- [ ] La solución está nombrada por lo que efectivamente se construye
- [ ] El resumen de la solución explica el mecanismo — quiénes participan, en qué orden, qué pasa cuando algo falla — sin caer en contrato de endpoints
- [ ] Los objetivos son SMART y usan la métrica del criterio de éxito del shaping
- [ ] El caso de negocio contempla beneficio y costo de construir
- [ ] Funcionalidades clave marca el perímetro (dentro/fuera/futuro) con MoSCoW por item, e incluye los requerimientos nuevos de la revisión cruzada aprobados por el PM
- [ ] Impactos por área y Riesgos consolidan fielmente los artefactos aprobados — ninguna fila agregada, quitada ni reinterpretada
- [ ] Impactos por área muestra las nueve áreas (con impacto en detalle, sin impacto en una línea)
- [ ] El documento es autocontenido: sin links a wiki, sin nombres de archivo/skill, sin códigos de ticket, sin jerga interna
- [ ] Se lee en menos de 15 minutos y entra en el límite de la descripción de Jira
- [ ] El PM dio su OK literal y el frontmatter dice `Aprobado por PM (YYYY-MM-DD)`, o quedó explícito en `Propuesta`

## Paso 11 — Cierre estándar

1. **Persistir** en `artefactos/{{nombre_corto_proyecto}}-prd.md` — `{{nombre_corto_proyecto}}` es la carpeta si nació de `/idea_start`, o el `<slug>` después de `prd-XXX_` en carpetas legacy (sin fecha en el nombre; versión en el frontmatter + historial al pie). Frontmatter: `version`, `estado`, `basado_en` con las versiones de `-start`, `-solution`, `-crosscheck` y `-risks` consolidadas. Si el archivo ya existe, se reescribe limpio el cuerpo con el estado vigente y se suma una entrada al historial; si estaba aprobado y cambió el cuerpo, vuelve a `Propuesta` hasta la re-aprobación. Los metadatos que después escriben otras skills (`sp_estimado`, `sp_estimado_proyecto`) no revocan la aprobación.
2. **Decisiones de alcance confirmadas** → `decisiones.md` del proyecto (directo). Si es una decisión de contexto fijo, item `tipo: decision` en `contexto_vivo/`.
3. **Preguntas abiertas** → `gaps.md` del proyecto; item `tipo: gap` en `contexto_vivo/` solo si son de contexto fijo.
4. **`proyecto.md`** — §3 Alcance alineado con Funcionalidades clave; §4 Entrega, fila del PRD en la tabla "Cadena de artefactos" con versión y estado.
5. **Índices:** `wiki/1_proyectos/index.md` §2; `wiki/index.md` solo si cambió una sección de nivel PARA.
6. **Sin changelog y sin git.** El commit del repo personal lo hace el hook `SessionStart` una vez al día.
7. **Jira:** nunca crear ni editar tickets a partir de este PRD sin confirmación explícita del usuario — eso es [`/idea_jira`](../idea_jira/SKILL.md).
8. Siguiente paso sugerido: [`/idea_us`](../idea_us/SKILL.md) para bajar el PRD aprobado a historias de sprint, o [`/idea_estimate`](../idea_estimate/SKILL.md) en Modo Proyecto si hace falta dimensionar la IDEA antes de tener historias (priorizarla contra otras o conversar capacidad con Ingeniería). Las tareas previas al go-live y los bloqueadores ya están registrados: [`/idea_golive`](../idea_golive/SKILL.md) los toma cuando se acerque el lanzamiento.

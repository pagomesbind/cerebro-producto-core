---
name: idea_jira
description: Crea (o actualiza) en Jira la jerarquía completa IDEA→Epic→Historia de una IDEA ya especificada — clasifica la IDEA (Categoría, Producto, Cliente, SP estimado, prioridad), la deja en estado EN APROBACION, deja en la Epic el análisis técnico-funcional completo (autocontenido, con diagramas Mermaid) para que Ingeniería tenga todo el contexto antes de las historias, y crea las historias de usuario confirmadas como tickets Historia en BACKLOG. Se activa con /idea_jira.
when_to_use: Se activa cuando el usuario ejecuta /idea_jira, siempre después de que el PRD esté cerrado (/idea_prd), las historias de usuario estén confirmadas (/idea_us, Paso 5ter cerrado) y exista una estimación de SP (/idea_estimate). Nunca antes — esta skill no redacta contenido nuevo, solo lo traslada a Jira.
disable-model-invocation: true
argument-hint: "[nombre_corto_proyecto o PRD-XXX]"
---

# 🎫 CREACIÓN EN JIRA: /idea_jira

## Por qué existe esta skill

El discovery y la especificación de una IDEA viven en la wiki (`proyecto.md`, PRD, historias de usuario) hasta que llega el momento de bajarlos a Jira para que el resto de la organización — comité de aprobación, Ingeniería, QA — pueda verlos y actuar. Ese paso tiene reglas propias que no son parte del contenido de producto (a qué estado queda cada tipo de ticket, qué prioridad, cómo se clasifica, qué campos son obligatorios) y es fácil pisar el pie: crear un link en la dirección equivocada, duplicar una historia que ya existía, dejar un ticket en un estado que no le correspondía. Esta skill encapsula esas reglas para que crear en Jira sea mecánico y consistente cada vez, no una decisión ad hoc por sesión.

## Cuándo NO usarla

- El PRD todavía no está cerrado, o tiene preguntas abiertas que bloquean el alcance → cerralo primero con [`/idea_prd`](../idea_prd/SKILL.md).
- Las historias de usuario no fueron confirmadas por el PM (Paso 5ter de [`/idea_us`](../idea_us/SKILL.md) sigue abierto) → no crees tickets a partir de una historia a medio revisar.
- No existe una estimación de SP para la IDEA (`sp_estimado` ausente del frontmatter del PRD) → corré primero [`/idea_estimate`](../idea_estimate/SKILL.md). Esta skill nunca inventa un número de esfuerzo.
- Lo que hace falta es actualizar el *contenido* de una historia ya creada en Jira (no crear una nueva) → editá el artefacto con `/idea_us` y traé el delta acá solo para que la Regla dura 3 decida si corresponde tocar el ticket ya existente.

## ⚖️ Reglas duras

1. **La IDEA siempre queda en estado `EN APROBACION` al cerrar esta skill — nunca más allá.** Pasar a `LISTO PARA EMPEZAR` o después es una decisión del comité de aprobación, no de esta skill. Si la IDEA ya estaba en un estado posterior (porque alguien la avanzó a mano en Jira), no la retrocedas — avisá al PM y dejala como está.
2. **Detectá si la IDEA ya existe en Jira antes de decidir qué crear.** La señal es la columna "IDEA" de la fila de este proyecto en `wiki/1_proyectos/index.md` §2: si ya tiene una clave `PRD-XXX` real (no `—` ni vacío), la IDEA existe — pasás a modo actualización (Paso 2B). Si no, es la primera vez que este proyecto toca Jira — creás todo de cero (Paso 2A). Nunca lo asumas por memoria de la sesión: confirmalo siempre contra el índice y, si hay dudas, contra Jira directo (`getJiraIssue`).
3. **En modo actualización, las historias se crean o se actualizan — nunca se duplican.** Traé las Historias ya creadas bajo la Epic vinculada (`"Epic Link" = <EPIC-KEY>`) y comparalas contra las historias confirmadas en el artefacto: creá solo las que falten. Si una historia ya creada cambió de contenido en el artefacto, no la reescribas en Jira sin que el PM lo pida explícitamente — mostrale el delta y esperá su decisión.
4. **Las Historias siempre se crean en estado `BACKLOG`, nunca más allá.** El PM las mueve a `Asignado` a mano después de revisarlas en Jira — esta skill no lo hace por él, ni siquiera si la IDEA es urgente.
5. **Prioridad — un valor por ticket, según su propio nivel MoSCoW, nunca un solo valor para toda la IDEA por default:**
   - Historia que viene de una funcionalidad 🔴 Must have → **High**.
   - Historia que viene de una funcionalidad 🟠 Should have → **Medium**.
   - Historia que viene de una funcionalidad 🟡 Could have → **Low** (o **Lowest** si el PM la marca como la más prescindible del lote).
   - La IDEA y la Epic toman la prioridad más alta entre sus propias historias (por defecto, la del Must have — **High**).
   - **`Highest` nunca sale de esta tabla por default.** Se reserva para lo que el PM marca explícitamente como urgente-ya (típicamente un bug productivo) — si no hay esa indicación explícita del PM en la sesión, no la uses aunque el PRD suene urgente en su prosa.
6. **Categoría de la IDEA — `BAU`, `BUILD` o `NORMATIVO`, nunca sin clasificar.** Inferila del contexto ya documentado en `proyecto.md`/PRD (ej. "tratado como BAU técnico" ya deja la respuesta escrita) — si no es evidente, preguntale al PM antes de asumir, no hay valor por defecto seguro acá.
7. **Cliente — `SOPORTE` si la IDEA nace de un pedido interno (Soporte, Operaciones, Administración, Integraciones) o es un bug transversal sin cliente puntual; el cliente real si nace de un pedido concreto y puntual de una organización.** Si no se conoce el cliente y tampoco es un caso claro de `SOPORTE`, dejá el campo sin completar — no fuerces un valor.
8. **SP estimado siempre en la IDEA, nunca en la Historia.** Tomalo del frontmatter del PRD (`sp_estimado`, cargado por `/idea_estimate`) — nunca lo recalculás ni lo estimás vos.
9. **La IDEA y todos los tickets que crea esta skill (Epic y cada Historia) quedan asignados al PM que la está corriendo** — el `pm`/`email` de `identidad.local.md` de esta instancia del Cerebro, nunca un valor genérico ni el reporter por defecto de Jira. Resolvé su `accountId` una sola vez al principio de la corrida (Paso 0.7) y reusalo en cada creación — no hace falta resolverlo de nuevo por ticket. En modo actualización, si algún ticket ya existente quedó sin asignar o asignado a otra persona, avisá al PM y solo reasigná con su confirmación explícita (mismo criterio que el resto de los deltas de la Regla dura 3/Paso 2B.2).
10. **El link IDEA↔Epic es "Polaris work item link", con la IDEA del lado `outward` ("implements") y la Epic del lado `inward` ("is implemented by")** — ver [`references/campos_jira.md`](references/campos_jira.md) §2.2 para la dirección exacta y por qué importa verificar antes de crear (evita el problema real de doble link que motivó esta regla).
11. **La Epic contenedora no se transiciona a ningún estado en particular** — queda en su estado de creación por defecto, coherente con la Regla dura 4 (nada bajo la IDEA se "asigna" solo por correr esta skill).
12. **La descripción de la Epic siempre lleva el análisis técnico-funcional completo, cuando existe `*-solution.md`.** No es un resumen ni una referencia a la IDEA — es el contenido real de ese artefacto (actores, contrato, mapa de procedencia de datos, camino feliz, caminos alternativos/errores, máquina de estados, NFR, decisiones de diseño) reescrito para que un desarrollador que nunca vio el Cerebro tenga todo el contexto técnico junto antes de encarar las historias, sin tener que ir a buscarlo a otro lado. Ver Paso 2A.3 para el detalle de cómo armarla.
13. **Todo diagrama del artefacto de solución (o de las historias, si aplica) va embebido en la descripción correspondiente como bloque de código, marcado explícitamente como Mermaid** (ej. ` ```mermaid ` seguido del diagrama) — el conector no soporta subir archivos, así que esta es la única forma de que el diagrama llegue al desarrollador. Nunca omitas un diagrama que el artefacto tenga, y nunca lo menciones sin incluirlo ("ver diagrama en la wiki" no vale acá).
14. **Nada se crea en Jira sin que el PM vea antes qué se va a crear/actualizar y dé su OK explícito** — es una acción visible para todo el equipo (comité de aprobación, Ingeniería), no una escritura silenciosa como el resto de esta wiki.
15. Todo output en español.

## 🏃 Pipeline

### Paso 0 — Contexto y precondiciones

1. Resolvé la ruta real del proyecto en la tabla maestra de [`wiki/1_proyectos/index.md`](../../../wiki/1_proyectos/index.md) §2 — y de paso, leé ahí mismo la columna "IDEA" (ver Regla dura 2).
2. Leé el PRD completo (`artefactos/{{nombre_corto_proyecto}}-prd.md`) — necesitás su frontmatter (`sp_estimado`) y su contenido íntegro para la descripción de la IDEA.
3. Leé el artefacto de historias de usuario (`artefactos/{{nombre_corto_proyecto}}-us.md`) — confirmá que el Paso 5ter de `/idea_us` está cerrado (sin `[pendiente revisión]` abierto). Si no lo está, avisá y no sigas.
4. Si `artefactos/{{nombre_corto_proyecto}}-solution.md` existe, leelo completo — es la fuente de la descripción de la Epic (Reglas duras 11-12) y no alcanza con hojearlo: necesitás cada sección y cada diagrama para reescribirlos autocontenidos en el Paso 2A.3.
5. Si `sp_estimado` no está en el frontmatter del PRD, parate acá — avisá al PM que hace falta correr `/idea_estimate` primero.
6. Cargá [`references/campos_jira.md`](references/campos_jira.md) — es la fuente de todos los IDs de campo, opción y transición que vas a usar en los pasos siguientes. Si algún ID de ese archivo falla al usarlo, no lo reintentes a ciegas: confirmá el valor real contra Jira (`getJiraIssueTypeMetaWithFields`, `getTransitionsForJiraIssue`) y corregí el archivo de referencia en la misma corrida.
7. **Resolvé el `accountId` del PM que está corriendo esta skill** (Regla dura 9) — leé `pm`/`email` de `identidad.local.md` (raíz del repo personal) y resolvé el `accountId` real con `lookupJiraAccountId` (ver `references/campos_jira.md` §1.6). Hacelo una sola vez acá, no por cada ticket.

### Paso 1 — Resolver clasificación y prioridades

1. **Categoría** (BAU/BUILD/NORMATIVO) — Regla dura 6.
2. **Producto** — de qué producto(s) trata la IDEA (ver tabla de `references/campos_jira.md` §1.3); de ahí sale también el espacio de desarrollo (WS/AD/OB/ARD/SER) donde va a vivir la Epic y las Historias.
3. **Cliente** — Regla dura 7.
4. **Prioridad de cada historia** — mapeá cada historia de usuario confirmada contra la funcionalidad MoSCoW de la que salió en el PRD (🔴/🟠/🟡) y aplicá la tabla de la Regla dura 5. Si el PM marcó la IDEA como urgente/bug productivo en la sesión, confirmá explícitamente con él que corresponde `Highest` antes de aplicarlo.
5. **SP estimado** — leído del frontmatter del PRD (Regla dura 8), no se recalcula acá.

### Paso 2A — La IDEA no existe todavía: crear todo de cero

1. **Crear la IDEA** (`createJiraIssue`, proyecto `PRD`, issuetype `Idea`) — resumen = título de la IDEA; descripción = el PRD completo en markdown (autocontenido, tal como está en el artefacto); `additional_fields` con prioridad, Categoría, Producto, Cliente (si se conoce), SP estimado y `assignee` con el `accountId` resuelto en el Paso 0.7 (Regla dura 9; ver `references/campos_jira.md` §1.1-1.6 para los payloads exactos).
2. **Transicionar la IDEA a `EN APROBACION`** (transition id de `references/campos_jira.md` §1.7).
3. **Crear la Epic contenedora** en el espacio de desarrollo resuelto en el Paso 1.2 — resumen igual al de la IDEA, misma prioridad que la IDEA (Regla dura 5), `assignee` con el mismo `accountId` del Paso 0.7 (Regla dura 9). No transicionarla (Regla dura 11).

   **Descripción de la Epic — el contexto técnico completo, listo para que Ingeniería lo lea de una sola vez:**
   - **Si existe `*-solution.md`:** la descripción es ese análisis técnico-funcional completo, reescrito como documento autocontenido (Reglas duras 12-13) — no un link, no un resumen de una línea, no "ver el PRD para más detalle". Recorré cada sección relevante del artefacto (actores/sistemas involucrados, contrato con sus datos de entrada/salida, de dónde sale cada dato, camino feliz, caminos alternativos y errores conocidos, máquina de estados si la tiene, decisiones de diseño y sus motivos, requisitos no funcionales, limitaciones/gaps técnicos conocidos) y volcala completa — no elijas cuáles secciones "valen la pena", todas las que tengan contenido real van. Al reescribir, sacá todo lo que solo tiene sentido para alguien que usa el Cerebro: nombres de archivo (`*-solution.md`, `proyecto.md`), nombres de skill (`/idea_solution`, `/idea_us`), rutas de la wiki, referencias a "el PM decidió" sin explicar qué se decidió y por qué (explicalo en la propia descripción, no lo des por sabido), y cualquier cita tipo "ver `gaps.md`" — si el dato importa, va explicado ahí mismo; si no importa para encarar el desarrollo, no va.
   - **Todo diagrama que tenga `*-solution.md`** (secuencia, flujo, máquina de estados) va embebido tal cual, en un bloque de código con el lenguaje `mermaid` explícito y una frase antes aclarando qué representa — nunca lo omitas ni lo resumas en prosa en su lugar.
   - **Si no existe `*-solution.md`:** la descripción es un resumen técnico breve armado a partir de lo que sí haya (PRD, `proyecto.md`) — igual autocontenido, sin referencias al Cerebro — dejando explícito que no hubo análisis técnico-funcional formal para esta IDEA.
4. **Crear el link IDEA↔Epic** — Regla dura 10, verificando primero que no exista ya (no debería, en este modo, pero confirmá igual).
5. **Por cada historia de usuario confirmada** (todas las que el PM cerró en `/idea_us`, salvo que pida un subconjunto distinto): crear un ticket **Historia** en el mismo espacio, con `parent` = la Epic recién creada, descripción = el contenido completo de esa historia (enunciado, contexto, contrato de API o AC según corresponda, diagrama si aplica, notas técnicas, fuera de alcance, preguntas abiertas — todo tal cual está en el artefacto, sin resumir), prioridad según el Paso 1.4, `assignee` con el mismo `accountId` del Paso 0.7 (Regla dura 9). Confirmá el `status` inmediato tras la creación — si no nació en `Backlog`, transicionala (Regla dura 4, id de transición en `references/campos_jira.md` §2.1).

### Paso 2B — La IDEA ya existe: actualizar

1. Traé la IDEA real (`getJiraIssue`, `fields: ["*all"]` o al menos los campos de clasificación + `status` + `issuelinks`).
2. Si algún campo de clasificación cambió respecto de lo ya cargado (Categoría/Producto/Cliente/SP/prioridad/`assignee`), mostrále el delta al PM antes de tocar nada — solo actualizá (`editJiraIssue`) lo que confirme (Regla dura 9, incluye reasignar si quedó sin asignar o con otra persona).
3. Si la IDEA no está todavía en `EN APROBACION` ni en un estado posterior, transicionala (Regla dura 1). Si ya está en un estado posterior, no la toques — avisá.
4. Traé la Epic vinculada desde `issuelinks` (tipo Polaris) y las Historias ya creadas bajo ella (`"Epic Link" = <EPIC-KEY>`, `fields: ["summary", "status"]`). Si `*-solution.md` cambió de contenido desde la última corrida (versión de frontmatter distinta a la que se usó para la descripción actual de la Epic, si quedó registrada — ver Paso 4.2), mostrale el delta al PM y actualizá la descripción de la Epic (Paso 2A.3) solo con su OK.
5. Comparé esa lista contra las historias de usuario confirmadas del artefacto — creá solo las que falten, con el mismo detalle del Paso 2A.5. Las que ya existen quedan intactas salvo pedido explícito del PM (Regla dura 3).

### Paso 3 — Confirmación con el PM

Antes de ejecutar cualquier `createJiraIssue`/`editJiraIssue`/`transitionJiraIssue`/`createIssueLink`, mostrale al PM un resumen claro de lo que vas a hacer: IDEA nueva o existente (con su clave si ya existe), Epic nueva o reusada, cuántas Historias se van a crear y con qué prioridad cada una, y los valores de Categoría/Producto/Cliente/SP resueltos. Esperá su OK explícito (Regla dura 14) antes de tocar Jira.

## ✅ Checklist de calidad

- [ ] Se resolvió correctamente si la IDEA ya existía (columna "IDEA" de `1_proyectos/index.md` §2), no por memoria de la sesión
- [ ] La IDEA queda en `EN APROBACION` (nunca más allá, nunca menos si ya estaba ahí)
- [ ] Ninguna Historia quedó en un estado distinto de `Backlog`
- [ ] Cada Historia tiene la prioridad que corresponde a su nivel MoSCoW real — `Highest` solo si el PM lo confirmó explícitamente
- [ ] Categoría, Producto y SP estimado están completos en la IDEA; Cliente está completo si se conocía o correspondía `SOPORTE`
- [ ] La IDEA, la Epic y cada Historia quedaron asignadas al PM que corrió la skill (`accountId` resuelto una sola vez, reusado en todos los tickets)
- [ ] El link IDEA↔Epic existe una sola vez, en la dirección correcta (IDEA outward/"implements", Epic inward/"is implemented by") — se verificó antes de crear, no se creó a ciegas
- [ ] No se duplicó ninguna historia ya existente en modo actualización
- [ ] El PM dio su OK explícito al resumen del Paso 3 antes de crear o tocar nada en Jira
- [ ] Si existía `*-solution.md`, la descripción de la Epic tiene su contenido técnico completo (no un resumen ni un link) y está limpia de nombres de archivo/skill, rutas de la wiki y jerga interna — se lee sola
- [ ] Todos los diagramas del artefacto de solución quedaron embebidos en la descripción, en bloques de código marcados como `mermaid`, ninguno omitido

## Paso 4 — Cierre estándar

1. **`wiki/1_proyectos/index.md` §2:** completá/actualizá la columna "IDEA" con la clave `PRD-XXX` real y "Estado Jira" con `EN APROBACION` (o el estado real, si ya venía de un estado posterior que no se tocó) — es el resolver de rutas del que depende la Regla dura 2 en la próxima corrida de esta skill sobre el mismo proyecto.
2. **`proyecto.md` del proyecto:** agregá en la sección de Entrega/Seguimiento PM las claves reales creadas (IDEA, Epic, Historias) con sus links a Jira — el próximo `/debrief` o sesión de seguimiento parte de ahí, no de memoria. Si usaste `*-solution.md` para la descripción de la Epic, anotá también qué versión de ese artefacto (frontmatter) volcaste — es lo que el Paso 2B.4 compara en la próxima corrida para saber si la Epic quedó desactualizada.
3. **`contexto_vivo/`:** emití un item `tipo: iniciativa` con la novedad (creación en Jira, o el delta si fue una actualización) — completá `pm_destino` si corresponde (Regla General de Control #5).
4. **Índices:** verificá que ningún índice tocado (`1_proyectos/index.md`, el del proyecto si tiene subcarpetas) haya quedado desactualizado.
5. **Sin changelog manual y sin git.** El commit del repo personal lo hace el hook `SessionStart` una vez al día.
6. Siguiente paso sugerido: ninguno automático — de acá en adelante el ciclo de vida del ticket lo llevan el comité de aprobación (la IDEA) y el Project Manager de desarrollo (las Historias, una vez que las mueva a `Asignado`), fuera del alcance de esta skill.

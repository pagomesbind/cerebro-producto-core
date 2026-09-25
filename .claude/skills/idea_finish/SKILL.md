---
name: idea_finish
description: Cierre formal de una IDEA/proyecto que llegó a producción — dos gates obligatorios (checklist de go-live cubierto, riesgos mitigados) antes de relevar completo lo entregado en Jira (historias, comentarios, bugs, pruebas), ingerir todo lo aprendido al canon, transicionar la IDEA a Finalizada en Jira y archivar la carpeta del proyecto. Se activa con /idea_finish.
when_to_use: Se activa cuando el usuario ejecuta /idea_finish, cuando el PM confirma que una IDEA/proyecto llegó a producción y quiere darlo por cerrado formalmente — no un cierre casual de sesión (eso es /debrief), sino el gate final que verifica que nada quedó suelto antes de archivar.
disable-model-invocation: true
argument-hint: "[nombre_corto_proyecto o PRD-XXX]"
---

# 🏁 CIERRE FORMAL DE PROYECTO: /idea_finish

## 🎯 Por qué existe esta skill

`/debrief` (Paso 3bis) ya sabe archivar una IDEA finalizada: destila conocimiento generalizable, registra la calibración de SP y mueve la carpeta a `4_archivos/proyectos_finalizados/`. Pero es deliberadamente liviano — nace para un cierre mencionado de pasada en una sesión de trabajo libre, nunca escribe en Jira (Regla dura 1 de esa skill) y no audita nada: confía en que el PM ya dijo que está todo bien.

Esa confianza no siempre estuvo justificada. Los cierres reales de este Cerebro (PRD-200, PRD-216, PRD-70) muestran el mismo patrón cada vez que alguien se toma el trabajo de auditar antes de cerrar: aparecen pendientes que nadie había registrado — un dato de producción sin restaurar, un cambio de comportamiento nunca comunicado, una aprobación formal que nunca se confirmó, un Epic técnico que sigue en Backlog en Jira pese a que todo lo que contiene está Finalizado. `/idea_finish` es el gate que fuerza esa auditoría **siempre**, en vez de dejarla al criterio de si el PM se acuerda de pedirla: no se archiva nada ni se toca Jira hasta que el checklist de go-live y el registro de riesgos estén explícitamente resueltos, y hasta que se haya releído Jira completo — IDEA, Epic, historias y **todos sus comentarios** — porque ahí es donde suelen vivir los bugs corregidos y las observaciones de QA que nunca llegaron a la wiki.

## Cuándo NO usarla

- Cierre casual de una sesión de trabajo libre, sin necesidad de auditoría ni de tocar Jira → [`/debrief`](../debrief/SKILL.md) (Paso 3bis) sigue siendo la vía liviana para eso.
- El proyecto se cancela o queda en stand-by sin haber llegado a producción → también `/debrief` (Paso 3bis, caminos "Cancelada"/"Pausada"). Esta skill es solo para el camino "llegó a producción y se cierra formalmente".
- Nunca se corrió un checklist de go-live y no hay siquiera una fecha real de producción confirmada → correr primero [`/idea_golive`](../idea_golive/SKILL.md); si el lanzamiento todavía no pasó, no hay nada que auditar en retrospectiva todavía.
- El argumento es un **proyecto general** (con miembros activos todavía en curso) → esta skill cierra una IDEA/slice puntual, no un proyecto general completo. Si el PM quiere cerrar el proyecto general porque ya no le quedan miembros activos, avisar que es un caso aparte (no cubierto acá) y proceder manualmente con criterio, actualizando `proyecto.md` del padre.

## ⚖️ Reglas duras

1. **No se archiva la carpeta ni se transiciona nada en Jira sin que las dos gates (Paso 1 y Paso 2) estén explícitamente resueltas, ítem por ítem, con el PM.** Ninguna pregunta se salta por parecer menor.
2. **Nunca inventar que un ítem ya se hizo.** Todo pendiente sin resolución explícita del PM bloquea el avance — se pregunta, no se asume "probablemente ya se resolvió". Si el PM no puede confirmar algo en el momento, queda como tarea en `tareas.md` con dueño y el cierre formal espera a esa resolución (no se fuerza el archivado con un pendiente colgando).
3. **El relevamiento de Jira es completo, no un resumen superficial:** IDEA + Epic(s) + todas las Historias/subtareas vinculadas, con **todos** sus comentarios — no solo el estado final. Un ticket "Finalizada" sin leer sus comentarios puede esconder un bug encontrado y corregido en el camino, una decisión de alcance tomada ahí y nunca volcada a la wiki, o un cambio de comportamiento que nadie comunicó (precedentes reales: PRD-200 — 2 pendientes descubiertos recién en la auditoría; PRD-216 — cambio de código de rechazo nunca documentado).
4. **SP real nunca es el SP estimado reciclado.** Sale de sumar el campo real de Story Points de los tickets de desarrollo (`customfield_10107`), igual criterio que `log_iniciativas_producto.md` — si no hay SP real cargado en algún ticket, decilo explícito en vez de sustituirlo por el estimado.
5. **Nada se transiciona en Jira sin mostrarle antes al PM qué se va a transicionar y a qué estado, con su OK explícito** (mismo criterio que la Regla dura 14 de `/idea_jira`) — es una acción visible para todo el equipo, no una escritura silenciosa.
6. **`2_areas/` y `3_recursos/` nunca se escriben directo.** Todo conocimiento generalizable que deje el cierre nace como item en `contexto_vivo/` (regla central del CLAUDE.md) — esta skill no es una excepción por ser "el cierre".
7. **El archivado de la carpeta es siempre la última acción**, después de que Jira, la ingesta y las dos gates ya cerraron — nunca archivar dejando algo pendiente de ingesta "para después": una vez movida la carpeta, nada la vuelve a mirar de rutina.
8. Todo output en español.

## 🏃 Pipeline

### Paso 0 — Contexto y confirmación

1. Resolvé la ruta real en la tabla maestra de [`wiki/1_proyectos/index.md`](../../../wiki/1_proyectos/index.md) §2 — y de paso confirmá la clave de IDEA (columna "IDEA"). Si está vacía o en `—`, esto no es un cierre formal típico: avisá al PM y confirmá cómo proceder (lo más probable es que el cierre real sea un `/debrief`, no esta skill).
2. Leé completo el `proyecto.md` del miembro (y el §4/§5 del padre si es miembro de un proyecto general), `gaps.md`, `decisiones.md` y `riesgos.md` si existen.
3. **Confirmá explícitamente con el PM** que el proyecto llegó a producción y que quiere el cierre formal ahora — esta skill dispara una auditoría pesada (dos gates + relectura completa de Jira), no arranques sin esa confirmación.

### Paso 1 — Gate de go-live

1. Buscá el artefacto `artefactos/{{nombre_corto_proyecto}}-golive.md`. **Si no existe, generalo ahora mismo como auditoría retroactiva** — mismo pipeline de [`/idea_golive`](../idea_golive/SKILL.md) (Paso 0 a Paso 7 de esa skill: overview del lanzamiento, relevar cada función — ingeniería, QA, diseño/UX, comunicación, soporte, legal/cumplimiento, operaciones, analítica — con el estado real verificado contra Jira/reuniones/mails, no planificado a futuro), marcado `status: complete (auditoría retroactiva — el lanzamiento ya ocurrió)` en el frontmatter (mismo formato que el precedente de `arcos_dorados_productos_resolve-golive.md`). No bloquees el cierre por la sola ausencia del checklist — generarlo es parte de este paso.
2. Repasá cada ítem del checklist que no esté marcado `[x]`/Hecho/N/A. Por cada uno, preguntale al PM (una pregunta por ítem, mismo criterio que `/gaps` — nunca agrupar varios en una sola pregunta): *¿ya se resolvió (con qué evidencia) o se omite explícitamente, y por qué?*
3. Esto incluye explícitamente cualquier impacto que haya surgido del relevamiento por área del checklist (legal/cumplimiento, soporte, operaciones) aunque no estuviera en el radar original del PM al lanzar — es exactamente lo que ese checklist existe para sacar a la luz.
4. Actualizá el `-golive.md` in place con cada resolución (Paso 8 de `/idea_golive`: cuerpo limpio, historial de revisiones al pie, no notas superpuestas). Al cerrar este paso, ningún ítem puede seguir en blanco — todos terminan **Hecho** (con evidencia) u **Omitido** (con la justificación textual del PM).

### Paso 2 — Gate de riesgos

1. Leé `riesgos.md` del proyecto (y del padre si el proyecto es miembro y comparte riesgos — filtrá solo los que aplican a este miembro puntual).
2. Por cada entrada sin `**Estado:** Cerrado` / `Mitigado` (o equivalente ya resuelto), preguntale al PM, una por una: *¿ya se ejecutó la acción de mitigación (cuál, cuándo) o se omite con justificación (ej. el riesgo ya no aplica, se acepta tal cual)?*
3. Actualizá `riesgos.md` con el cierre de cada entrada (mismo formato de actualización que usa `/gaps` sobre `gaps.md`: agregar debajo de la entrada, nunca reescribir el texto original).

### Paso 3 — Relevamiento completo de lo entregado en Jira

1. Traé la IDEA completa (`getJiraIssue`, campos explícitos: `summary`, `description`, `status`, `comment`, `fixVersions`, `issuelinks`, SP estimado y SP real).
2. Traé la(s) Epic(s) vinculada(s) y **todas** las Historias y subtareas bajo ella(s) — `summary`, `status`, `comment`, `fixVersions`, SP real (`customfield_10107`) de cada una. Sin excepción: leé el comentario completo de cada ticket, no solo el estado final.
3. De esos comentarios, extraé y documentá:
   - Bugs/defectos levantados durante desarrollo o QA y cómo se resolvieron (o si quedaron abiertos sin resolver — en ese caso, van al Paso 1 o a una tarea nueva, nunca se pierden en silencio).
   - Observaciones de prueba relevantes (casos que no salieron como esperado, escenarios que terminaron sin cubrir).
   - Decisiones de alcance tomadas directo en el comentario de un ticket y nunca volcadas a `decisiones.md` de la wiki.
   - Cualquier cambio de comportamiento respecto de lo especificado en el PRD/historias que no haya sido comunicado (precedente: AD-1434, un código de rechazo distinto al documentado).
4. Calculá el **SP real** (suma de Story Points reales de los tickets de desarrollo, Regla dura 4) y la **fecha de entrega real** (`releaseDate` de la `fixVersion` más antigua entre los tickets de Entrega, mismo criterio que `log_iniciativas_producto.md`).
5. Presentale al PM un resumen de qué se entregó realmente contra lo especificado (PRD, historias de usuario) — señalando explícitamente cualquier delta: funcionalidad no entregada, agregada de más, o con comportamiento distinto al documentado.

### Paso 4 — Ingesta del conocimiento aprendido

Este paso es el que decide si el Cerebro queda genuinamente experto en lo que se acaba de construir o si el cierre se reduce a un archivo movido de carpeta. Mismo criterio general que el Paso 3bis de `/debrief` (nunca resumido, nunca crudo, siempre con cita de fuente), pero más exhaustivo en dos sentidos: el triage cubre **todas** las vías del canon que el cierre haya tocado, no solo la del producto (punto 1), y siempre suma una entrada de historial de esfuerzo real (punto 4) — la que casi siempre se olvida:

1. **Triage por altitud y por vía — antes de escribir un solo item.** Un cierre de proyecto casi nunca deja conocimiento de un solo tipo: repasá todo lo trabajado en los Pasos 0-3 (proyecto.md, gaps/decisiones/riesgos, y sobre todo lo que salió de leer los comentarios de Jira) y separalo, mismo criterio de altitud que el Paso 3 de `/debrief` pero exhaustivo sobre las **tres vías de `3_recursos/` por separado, nunca mezcladas** (regla del CLAUDE.md: "vías que no se mezclan entre sí") más lo que exceda a producto:
   - **Mecánica de un producto concreto** (qué hace, cómo se configura, contrato real) → `3_recursos/detalle_productos/<producto>/`.
   - **Infraestructura/IT no ligada a un producto puntual** — algo aprendido sobre la nube, seguridad de plataforma, un NFR/performance, o la relación técnica con Fintexa que el proyecto haya dejado (ej. un límite de su API, un patrón de timeout, una restricción de ambiente) → `3_recursos/arquitectura_sistema/`.
   - **Obligación regulatoria aprendida o confirmada en el camino** — algo sobre PLD/BCRA/UIF, PCI DSS, reportería, que haya salido del discovery o de la ejecución (ej. un requisito de auditoría que apareció recién al implementar) → `3_recursos/cumplimiento_normativo/`.
   - **Decisión de contexto fijo** (no específica de este proyecto — política, convención, prioridad entre áreas que quedó sentada por este cierre) → `2_areas/direccion/decisiones.md`.
   - **Riesgo general del equipo que sigue vivo más allá de este proyecto puntual** (ej. una dependencia de un proveedor que va a afectar a otros desarrollos futuros) → `2_areas/riesgos.md`, `tipo: riesgo`. Esto es distinto del Paso 2: ahí cerrás los riesgos **de este proyecto** antes de archivar; acá emitís uno **nuevo y general** si el cierre reveló algo que trasciende este proyecto.
   Es normal cerrar un proyecto con dos, tres o más items de `tipo: conocimiento` en vías distintas — nunca fuerces todo a `detalle_productos/` solo porque es el destino más común.

2. **Para cada vía que aplique, leé su índice** (`detalle_productos/<producto>/index.md`, `arquitectura_sistema/index.md`, `cumplimiento_normativo/index.md`, según corresponda) y los archivos temáticos existentes que ya tocan el tema. `destino_propuesto` tiene que nombrar el archivo (y, si corresponde, la sección) donde esto se integra — nunca una carpeta a secas. Si de verdad no hay ningún archivo temático que lo cubra, `tipo_destino: crear` es válido; si existe uno cercano, es `actualizar`, nunca un archivo nuevo disperso por comodidad (regla del CLAUDE.md: 1 tema = 1 archivo).

3. **Cada item de mecánica/infraestructura/cumplimiento**, con `> Fuente: Proyecto <IDEA> "<título>", finalizado YYYY-MM-DD`. No alcanza con un resumen de qué problema resolvió — tiene que quedar reusable para el próximo discovery que toque el mismo componente:
   - **Contrato o mecanismo real construido:** endpoints/eventos con su forma real (no la especificada, la que terminó en producción si difieren — Paso 3.5), flags/kill-switches y su nombre real, límites configurables, catálogos cerrados, códigos de evento/error reales.
   - **Limitaciones conocidas / bugs y su causa raíz** como subsección propia (no diluida en prosa general) — todo lo que salió del Paso 3.3: qué falló, por qué, cómo se corrigió o por qué se dejó así a propósito. Es exactamente lo que `/idea_us` va a buscar ahí antes de inventar un detalle técnico la próxima vez que se toque este mismo endpoint.
   - Si además generaste la entrada del punto 4 (historial de esfuerzo), crucen entre sí con un link — un lector que llega por mecánica encuentra el costo real, y al revés.

4. **`tipo: conocimiento` — historial de esfuerzo real**, `destino_propuesto: 2_areas/procesos/referencia_estimaciones.md` (sección "Jira"), **nunca omitido aunque parezca redundante con el punto 3**: es el archivo que `/idea_estimate` compara por analogía y donde `/idea_us` busca "endpoints con historial de bugs" antes de redactar AC — sin esta entrada, la próxima estimación de un desarrollo similar vuelve a partir de cero. Mismo formato que las entradas Jira ya existentes ahí:
   - `### <Título> — IDEA <PRD-XXX> (Finalizada, Go Live YYYY-MM-DD)`
   - **Qué se construyó:** una frase + link a la entrada de mecánica del punto 3.
   - **Esfuerzo:** SP real (Paso 3.4), cuántos tickets tuvo la Epic y de qué tipo (funcional / no funcional / bug de QA) — el ratio de bugs sobre el total es la señal más valiosa que deja este archivo.
   - **Lectura para estimaciones futuras:** una frase de patrón explícito, no solo el número — ej. *"tocar de nuevo este endpoint expuesto a múltiples medios de pago tiende a acumular bugs de caso no contemplado proporcional a esa variedad"*. Si no hay ningún patrón real que valga la pena dejar (desarrollo sin sorpresas), decilo así en vez de forzar una lectura que no existe.

5. **`tipo: iniciativa`** con `cierre: true`, SP estimado (del PRD) vs. SP real (Paso 3.4), fecha de entrega real y dónde quedó cada pieza de conocimiento (todas las vías del punto 1 que aplicaron) — alimenta `3_recursos/datos/log_iniciativas_producto.md` en el próximo `/context_merge`.
6. **Deltas del Paso 3.3/3.5 que abren una decisión o un gap nuevo** (ej. un comportamiento no comunicado que hay que decidir si se corrige o se documenta como limitación conocida) → `decisiones.md`/`gaps.md` del proyecto, directo — nunca los des por resueltos vos mismo, quedan para que el PM los cierre en la próxima corrida de `/gaps` si no se resuelven ahora mismo.
7. **Cualquier pendiente que el PM no pudo resolver en los Pasos 1-3** (Regla dura 2) → tarea nueva en `wiki/1_proyectos/tareas.md`, con dueño y, si aplica, item `tipo: tarea_equipo`. El cierre formal (Pasos 5-6) espera a que estas queden resueltas — no se archiva con un pendiente de este tipo abierto.

### Paso 5 — Cierre en Jira

1. Presentale al PM exactamente qué se va a transicionar: la IDEA a `Finalizada`, y cualquier Epic/Historia/subtarea que siga en un estado que no refleje la realidad pese a estar todo entregado (precedente: PRD-200, Epic WS-1312 quedó en Backlog pese a que su única Historia y subtareas estaban Finalizadas — deuda de higiene de Jira que el cierre formal debería corregir, no arrastrar).
2. Con el OK explícito del PM (Regla dura 5), transicioná. **Confirmá el id de transición real con `getTransitionsForJiraIssue` sobre cada ticket antes de asumirlo** — los ids de "Finalizar"/"Listo" difieren por espacio de desarrollo (WS/AD/OB/ARD/SER), ver `../idea_jira/references/campos_jira.md` §1.7/2.1 como punto de partida, nunca como valor definitivo sin verificar.
3. Si el PM prefiere no tocar algún ticket puntual (ej. una deuda de higiene menor que no le importa corregir ahora), respetalo y dejalo anotado en el resumen de cierre — no insistas.

### Paso 6 — Archivado

1. Refrescá `proyecto.md` con el estado final: fecha real de producción, SP real vs. estimado, resumen de qué se entregó (Paso 3.5) y qué quedó como limitación conocida.
2. Movés vos mismo (directo, no vía merge) la carpeta completa a `wiki/4_archivos/proyectos_finalizados/` — si era miembro de un proyecto general, solo su carpeta, quitando su fila de la tabla de miembros del `proyecto.md` padre (§3.2, ver `proyecto-onboarding-estrategico/proyecto.md` como referencia de formato de esa tabla).
3. Sacala de la tabla maestra de `1_proyectos/index.md` §2 y agregala a la lista de "IDEAs Finalizadas" del §3.
4. Si el padre tenía riesgos compartidos en su propio `riesgos.md` que ya no aplican a ningún miembro activo restante, señalalo — no los cierres vos mismo sin confirmarlo con el PM, es información del proyecto general completo, no de este cierre puntual.

## ✅ Checklist de calidad

- [ ] Las dos gates (golive, riesgos) terminaron sin ningún ítem en blanco — todo Hecho (con evidencia) u Omitido (con justificación explícita del PM)
- [ ] Se generó el checklist de go-live si no existía, en vez de saltear el gate por su ausencia
- [ ] Se leyeron **todos** los comentarios de la IDEA, la(s) Epic(s) y cada Historia/subtarea — no solo el estado final de cada ticket
- [ ] Todo bug/observación de prueba/decisión de alcance encontrado en un comentario de Jira quedó documentado (ingerido, o como decisión/gap/tarea nueva)
- [ ] El SP real sale de sumar Story Points reales de los tickets, nunca reciclado del estimado
- [ ] El PM dio su OK explícito antes de cualquier transición en Jira, y los ids de transición se confirmaron con `getTransitionsForJiraIssue` en vez de asumirse
- [ ] Ningún pendiente sin resolución explícita del PM quedó "colgando" al momento de archivar — o se resolvió, o es una tarea con dueño que pospone el cierre formal
- [ ] El conocimiento generalizable nació como item en `contexto_vivo/`, nunca escrito directo en `2_areas/`/`3_recursos/`
- [ ] Se hizo el triage por vía (Paso 4.1) antes de escribir — ningún conocimiento de arquitectura, cumplimiento normativo, decisión de dirección o riesgo general quedó forzado dentro de un item de `detalle_productos/` solo por comodidad
- [ ] Cada item de mecánica/infraestructura/cumplimiento nombra un archivo temático existente (o justifica por qué hace falta uno nuevo) en vez de una carpeta a secas, e incluye contrato/mecanismo real construido + una subsección propia de limitaciones conocidas/bugs
- [ ] Se generó la entrada de `referencia_estimaciones.md` (Paso 4.4) — nunca se saltea por parecer redundante con el item de mecánica; tiene su propia frase de patrón para estimaciones futuras, no solo el número de SP
- [ ] Los items de mecánica/infraestructura/cumplimiento e historial de esfuerzo quedaron cruzados entre sí
- [ ] La carpeta se archivó solo después de que Jira y la ingesta ya habían cerrado, nunca antes

## Paso 7 — Cierre estándar

1. **`wiki/1_proyectos/index.md`:** ver Paso 6.3 (§2 → §3).
2. **`wiki/1_proyectos/tareas.md`:** cualquier pendiente que quedó pospuesto (Regla dura 2 / Paso 4).
3. **`contexto_vivo/`:** todos los items del Paso 4 — conocimiento, iniciativa de cierre, y cualquier decisión/gap nuevo que sea de contexto fijo (no del proyecto que ya se archivó).
4. **Índices:** verificá que ningún índice de `1_proyectos/` haya quedado apuntando a la carpeta ya archivada (ej. la tabla de miembros del proyecto padre, Paso 6.2).
5. **Sin changelog manual y sin git.** El commit del repo personal lo hace el hook `SessionStart` una vez al día.
6. Cerrá con un resumen al PM: qué se auditó en cada gate, qué se transicionó en Jira, qué conocimiento quedó pendiente de `/context_merge`, y confirmación de que la carpeta ya no está en `1_proyectos/`.

---
id: 2026-08-27_transversal_checklist_cierre_revisar_items_parciales_ya_capturados
pm: pablo
fecha_captura: 2026-08-27
fuente: "Sesión de /idea_solution de convenios_configuracion — se descubrió que un item de contexto_vivo capturado incompleto a propósito (24/08, 'ver /idea_solution en curso') ya había sido mergeado a canon antes de que el /idea_solution real terminara, sin que quedara ningún recordatorio para volver a completarlo"
producto: transversal
tema: 2 reglas nuevas de proceso para que ningún item de contexto_vivo/ capturado incompleto quede sin revisar cuando el trabajo pendiente que lo completaría termina
tipo: decision
destino_propuesto: CLAUDE.md
tipo_destino: actualizar
contradice: "no"
confianza: alta
estado: ingestado
merge_commit: c4148e7
---

## Qué pasó

El 2026-08-24, en una sesión de discovery técnico de `convenios_configuracion`, se capturó un item de `contexto_vivo/` con la destilación del contrato OpenAPI de convenios — pero la propia sesión sabía que estaba incompleta (el análisis técnico de `/idea_solution` recién había arrancado) y lo dejó explícito en el cuerpo del item: "7 hallazgos... ver `/idea_solution` en curso". Nada en el proceso de `/context_push`/`/context_merge` respeta esa señal de "todavía no es la versión final" — el item se subió y se mergeó a `3_recursos/detalle_productos/adquirencia/gestion_convenios_comisiones.md` como si fuera completo, y se archivó.

El 2026-08-27, al cerrar el `/idea_solution` real (con una destilación mucho más completa — 11 hallazgos en vez de 7-8, más el detalle línea-a-línea de los 16 endpoints), nadie recordó volver a revisar si el item provisional del 24/08 ya había sido mergeado — se descubrió por casualidad, al intentar editarlo directamente y encontrar que ya no existía en `contexto_vivo/` (se había archivado). El PM preguntó explícitamente cómo evitar que esto vuelva a pasar, en cualquier skill, no solo en `/idea_solution`.

## Decisión / propuesta de redacción para `CLAUDE.md`

**Regla 1 — recordatorio obligatorio cuando se captura algo sabiendo que está incompleto.** En la sección `contexto_vivo/` — el buzón de todo aporte al canon, agregar:

> Si un item se captura sabiendo que está incompleto (el cuerpo dice algo como "en curso", "pendiente de que termine X", "versión parcial") — no confiar en la memoria de que "ya se va a revisar": sumar también una tarea en `tareas.md` (o en el `gaps.md` del proyecto si aplica) que diga explícitamente qué sesión/skill lo va a completar y qué item de `contexto_vivo/` hay que revisar cuando eso pase. `/context_push` y `/context_merge` no distinguen un item "provisional" de uno terminado — lo suben y lo mergean igual, así que el recordatorio tiene que vivir en un lugar que la propia sesión mire de rutina (el backlog personal), no solo en el texto del item.

**Regla 2 — paso nuevo en el checklist de cierre, para TODA skill, no solo la que originó el item provisional.** En la sección `### Checklist de cierre de sesión/skill`, ampliar el paso "todo aporte al canon como item de `contexto_vivo/`" para que incluya explícitamente una revisión hacia atrás, no solo captura de lo nuevo:

> Antes de capturar lo nuevo de esta sesión, repasar si el trabajo de hoy **completa o corrige** algo que ya estaba capturado en `contexto_vivo/` (todavía sin mergear) o ya mergeado en el canon (`2_areas/`/`3_recursos/`) sobre el mismo tema — no asumir que un aporte anterior sigue reflejando el estado actual solo porque nadie avisó lo contrario. Si el proyecto tiene una tarea de la Regla 1 pendiente sobre esto, resolverla acá. Si el item anterior ya se mergeó y archivó (`4_archivos/contexto_ingestado/`), no se edita — se captura un item nuevo con `tipo_destino: actualizar` sobre el mismo archivo canon, citando qué cambia respecto de lo ya mergeado.

## Por qué importa

Sin la Regla 1, cualquier item "a propósito incompleto" queda a merced de que alguien se acuerde sin ningún gancho externo — que es exactamente lo que falló acá. Sin la Regla 2, aunque el recordatorio exista en `tareas.md`, ninguna skill tiene instruido revisarlo al cerrar — el checklist actual solo dice "capturá lo nuevo", no "revisá si lo viejo sigue vigente". Juntas, cierran el mismo hueco por los dos lados: que quede un gancho, y que alguien lo mire.

## Estado de propagación

No se puede editar `CLAUDE.md` directo desde esta instalación — está espejado desde `CEREBRO_CORE` y bloqueado por el hook `PreToolUse`, sin excepciones. Este item queda capturado para que `/context_merge` (corrido sobre el clon de `CEREBRO_CORE`) aplique la redacción propuesta. Guardado también como memoria de sesión (`feedback`) para aplicar el criterio a mano en cualquier cierre de sesión futuro, hasta que `CLAUDE.md` lo refleje — mismo patrón que las 3 decisiones de `/idea_solution` capturadas en esta misma sesión.

---
id: 2026-08-27_transversal_idea_solution_ux_discusion_antes_de_mockups
pm: pablo
fecha_captura: 2026-08-27
fuente: "/idea_solution — sesión de convenios_configuracion, pedido explícito del PM sobre el orden correcto de trabajo cuando el alcance toca front end"
producto: transversal
tema: Orden de trabajo en /idea_solution cuando el alcance incluye front end — discutir la experiencia de usuario con el PM antes de documentar mockups para el developer
tipo: decision
destino_propuesto: .claude/skills/idea_solution/SKILL.md
tipo_destino: actualizar
contradice: "no"
confianza: alta
estado: ingestado
merge_commit: c4148e7
---

## Qué pasó

En la sesión de `/idea_solution` de `convenios_configuracion` (2026-08-27), el PM señaló que, cuando el alcance de una solución incluye trabajo de front end (UX/UI), la skill debería favorecer explícitamente una discusión de la experiencia de usuario con el PM (mismo método de grilling que ya usa el resto de la skill: presentar recomendación, dejar la decisión al PM) **antes** de documentar los mockups/especificación de pantallas para el developer — no saltar directo a redactar la especificación.

Es exactamente el orden que se siguió naturalmente en esta sesión, sin que la skill lo pidiera explícitamente: se diseñó la pantalla "Canal y Forma de Pago" conversando con el PM (3 estados, diálogo de doble nivel, formulario), esa experiencia se validó en vivo con el usuario real (Gonzalo Rivera, Integraciones/Soporte de Cobro) en una sesión previa de discovery, y **solo entonces**, en esta sesión, se armó el Anexo de especificación completa de pantallas (`convenios_configuracion-solution.md`) para que Fintexa supiera exactamente qué construir/ajustar en el front. El PM confirmó que este orden es el correcto y pidió que la skill lo refleje siempre que el alcance toque front end, no solo cuando surja naturalmente.

## Decisión / propuesta de redacción para la skill

Agregar una regla explícita en `.claude/skills/idea_solution/SKILL.md`, en la línea de las "Reglas duras" existentes (o como nota dentro del Paso 1, junto a la instanciación de las 12 ramas):

> **Si el alcance del proyecto (Sección 1) incluye trabajo nuevo o modificado de front end (UX/UI), la especificación de pantallas para el developer nunca es el primer paso.** Antes de documentarla, corré una discusión dedicada de experiencia de usuario con el PM — mismo método de grilling que el resto de la skill: presentá alternativas con tu recomendación, dejá la decisión de diseño de UX al PM. Si hay un usuario final real accesible (el operador o cliente que va a usar la pantalla), sumá además una validación en vivo con esa persona antes de cerrar la especificación — el acuerdo del PM solo no alcanza para dar la UX por resuelta. Recién con la experiencia acordada y validada, documentá el detalle completo de pantallas (layout, catálogo de casos estado/acción, formularios, diálogos) — como parte de la Sección 7 (Caminos alternativos) o como Anexo dedicado si el volumen lo justifica.

## Por qué importa

Evita el riesgo inverso: que la skill documente una especificación de pantallas "razonable" sin haber pasado por la discusión de UX con el PM (o sin validación de un usuario real cuando corresponde), y que esa especificación termine siendo la base de las historias de usuario sin que nadie la haya cuestionado a nivel de experiencia — el mismo tipo de riesgo que la regla dura #3 de la skill ya cubre para decisiones de negocio/alcance, aplicado ahora específicamente a UX.

## Estado de propagación

No se puede editar `.claude/skills/idea_solution/SKILL.md` directo desde esta instalación — está espejado desde `CEREBRO_CORE` y bloqueado por el hook `PreToolUse`, sin excepciones. Este item queda capturado para que `/context_merge` (corrido sobre el clon de `CEREBRO_CORE`) aplique la redacción propuesta. Guardado también como memoria de sesión (`feedback`) para aplicar el criterio a mano en cada corrida de `/idea_solution` con alcance de front end, hasta que la SKILL.md lo refleje — mismo patrón ya usado para la convención de slicing de `/idea_us` (ver `2026-08-26_transversal_idea_us_slicing_por_frontera_de_equipo`, ya ingerido).

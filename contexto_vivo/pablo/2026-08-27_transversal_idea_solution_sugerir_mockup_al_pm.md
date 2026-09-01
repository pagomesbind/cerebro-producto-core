---
id: 2026-08-27_transversal_idea_solution_sugerir_mockup_al_pm
pm: pablo
fecha_captura: 2026-08-27
fuente: "/idea_solution — sesión de convenios_configuracion, pedido explícito del PM de sumar un paso que sugiera armar el mockup/diseño cuando hay pantallas involucradas"
producto: transversal
tema: /idea_solution debe sugerir explícitamente armar el diseño/mockup con el PM cuando la solución involucra pantallas y todavía no existe uno
tipo: decision
destino_propuesto: .claude/skills/idea_solution/SKILL.md
tipo_destino: actualizar
contradice: "no"
confianza: alta
estado: ingestado
merge_commit: c4148e7
---

## Qué pasó

Cierra la secuencia de 3 decisiones sobre el mismo tema, todas de la sesión de `/idea_solution` de `convenios_configuracion` (2026-08-27):

1. Cuando el alcance toca front end, discutir la experiencia de usuario con el PM antes de documentar pantallas (`2026-08-27_transversal_idea_solution_ux_discusion_antes_de_mockups`).
2. Si ya existe un mock/prototipo aprobado, ilustrar el Anexo con imágenes fieles a ese mock (`2026-08-27_transversal_idea_solution_imagenes_reales_de_mock_en_anexo`).
3. **Esta:** si todavía **no** existe ningún mock/prototipo, la skill no debe limitarse a discutir la UX en la conversación y después caer directo a un wireframe SVG liviano en el documento — tiene que **sugerir explícitamente al PM armar el diseño/mockup** como paso propio, antes de seguir. El PM lo pidió después de ver el resultado de reconstruir imágenes fieles de un mock ya existente en `convenios_configuracion` — quiere que la misma calidad de insumo esté disponible incluso cuando el proyecto arranca sin ningún mock previo.

## Decisión / propuesta de redacción para la skill

Agregar, como continuación de la regla de "discutir la UX antes de documentar" (decisión #1 arriba), un paso explícito:

> **Si el árbol de diseño (Paso 1) marca que el alcance incluye pantallas y no existe todavía ningún mock/mockup/prototipo aprobado, la ronda de grilling dedicada a UX debe incluir una sugerencia explícita al PM de armar el diseño/mockup como paso propio** — no alcanza con conversar la experiencia en el chat y pasar directo a un wireframe interno. Formato de la sugerencia (mismo criterio `❓`/`➡️` del resto de la skill): ofrecer armar el mockup con una herramienta de diseño real (ej. la skill `design`, que publica un canvas editable como Artifact, o el visualizador para algo más liviano) antes de seguir, dejando en manos del PM decidir si vale la inversión para esta pantalla puntual o si un wireframe liviano alcanza. Si el PM confirma armar el mockup, ese mockup pasa a ser la fuente real para la Sección 7/Anexo (ver decisión #2, imágenes fieles vía `Artifact.read`) — no queda como un artefacto separado sin conexión con el documento.
>
> Si el PM prefiere no invertir en un mockup formal para esta pantalla puntual, la skill cae al criterio ya vigente: wireframe SVG liviano generado en el momento, dejando explícito en el documento que es una aproximación, no un diseño validado con UX/Diseño.

## Por qué importa

Sin este paso, la calidad del Anexo de pantallas queda librada a que el proyecto tenga la suerte de ya contar con un mock aprobado (como pasó en `convenios_configuracion`, donde el mock nació en una sesión anterior). Sugerirlo activamente sube el piso de calidad de cualquier `/idea_solution` con alcance de front, en vez de dejarlo a la iniciativa espontánea del PM.

## Estado de propagación

No se puede editar `.claude/skills/idea_solution/SKILL.md` directo desde esta instalación — está espejado desde `CEREBRO_CORE` y bloqueado por el hook `PreToolUse`, sin excepciones. Este item queda capturado para que `/context_merge` (corrido sobre el clon de `CEREBRO_CORE`) aplique la redacción propuesta, junto con las otras 2 decisiones de la misma secuencia. Guardado también como memoria de sesión (`feedback`) para aplicar el criterio a mano en cualquier corrida futura de `/idea_solution` con pantallas, hasta que la SKILL.md lo refleje.

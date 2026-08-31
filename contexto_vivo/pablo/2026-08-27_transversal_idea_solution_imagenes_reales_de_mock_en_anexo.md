---
id: 2026-08-27_transversal_idea_solution_imagenes_reales_de_mock_en_anexo
pm: pablo
fecha_captura: 2026-08-27
fuente: "/idea_solution — sesión de convenios_configuracion, pedido explícito del PM de estandarizar la técnica de imágenes reales en el Anexo de pantallas"
producto: transversal
tema: Técnica y regla para documentar pantallas en /idea_solution con imágenes fieles al mock/prototipo ya aprobado, no solo texto
tipo: decision
destino_propuesto: .claude/skills/idea_solution/SKILL.md
tipo_destino: actualizar
contradice: "no"
confianza: alta
estado: en_cola
merge_commit:
---

## Qué pasó

En la misma sesión de `/idea_solution` de `convenios_configuracion` donde se decidió que la skill debe discutir la UX con el PM antes de documentar pantallas (ver `2026-08-27_transversal_idea_solution_ux_discusion_antes_de_mockups`, sesión previa), el PM pidió avanzar con capturas del mock ya aprobado para el Anexo de especificación de pantallas, en vez de dejarlo solo en texto. Se probaron dos caminos:

1. **Browser pane** (`mcp__Claude_Browser__*`) — falló dos veces: el `screenshot` requiere que el panel esté desplegado del lado del cliente ("the Browser pane is not displayed"), y encima el navegador sandboxeado no tenía sesión iniciada contra `claude.ai`, así que ni siquiera podía cargar un artifact privado del usuario.
2. **`Artifact` con `action: "read"`** — funcionó de punta a punta: para un artifact propio del usuario, devuelve el HTML/CSS/JS **real y completo** (guardado en un archivo local de la sesión). Con ese contenido se reconstruyeron 4 imágenes SVG fieles al mock (mismos textos, mismos colores exactos vía las custom properties CSS, mismo layout) — no una captura de píxeles, pero tampoco un wireframe inventado.

Detalle importante encontrado en el camino: existían dos versiones del mismo diseño (un mockup estático de 2026-08-24 y un prototipo interactivo refinado el 2026-08-27) y **no coincidían** — el mockup estático tenía el diálogo de doble nivel con texto ya superado por una corrección posterior, capturada solo en el prototipo interactivo. Hubo que grepear el HTML de ambos para confirmar cuál reflejaba el diseño vigente antes de reconstruir la imagen.

El PM confirmó que esta técnica debería aplicarse siempre que una solución de `/idea_solution` incluya pantallas, no solo en este proyecto puntual.

## Decisión / propuesta de redacción para la skill

Agregar, junto a la regla ya propuesta sobre discutir la UX antes de documentar (`2026-08-27_transversal_idea_solution_ux_discusion_antes_de_mockups`), una regla operativa sobre CÓMO documentar una vez que la UX ya está acordada:

> **Si la solución incluye pantallas y ya existe un mock/mockup/prototipo aprobado publicado como Artifact de Claude, la especificación de pantallas del Anexo se ilustra con imágenes reconstruidas fielmente de ese mock — nunca solo texto, y nunca un wireframe inventado si el mock real está disponible.** Técnica: usar la herramienta `Artifact` con `action: "read"` sobre la URL del mock (funciona para artifacts propios del usuario — devuelve el HTML/CSS/JS real completo, guardado en un archivo local de la sesión). De ese contenido extraer el texto exacto y la paleta de colores (custom properties CSS) y reconstruir una imagen SVG fiel por cada pantalla/estado relevante — guardada en `artefactos/imagenes/` del proyecto y embebida en el documento vía sintaxis `![]()`, con una nota de fuente aclarando que es una reconstrucción fiel (no una captura de píxeles). **No usar el Browser pane para esto** — en este entorno no es una vía confiable (requiere el panel desplegado del lado del cliente y una sesión autenticada contra `claude.ai` que no está garantizada). **Si hay más de una versión publicada del mismo mock** (ej. un mockup estático más viejo y un prototipo interactivo más nuevo), grepear el HTML guardado de cada una para confirmar cuál refleja el diseño vigente antes de reconstruir — no asumir que la más vieja (o la primera que se encuentra) sigue siendo la fuente de verdad; si divergen, usar la versión vigente y dejar explícita la discrepancia con la más vieja.
>
> Si no existe ningún mock/prototipo real todavía (la UX se está diseñando en esta misma sesión, sin nada previamente publicado), cae el criterio anterior de la skill: un wireframe SVG liviano generado en el momento es la alternativa aceptable, con la salvedad de reemplazarlo por la imagen fiel si más adelante se publica un mock aprobado.

## Por qué importa

Cierra el círculo de la regla anterior (discutir UX antes de documentar): una vez que la UX está acordada y validada, la especificación para el developer debe ser lo más fiel posible al diseño real — texto solo es un piso aceptable cuando no hay mock, pero si el mock ya existe, no usarlo es dejar valor sobre la mesa (y una fuente más de desalineación entre lo diseñado y lo que el developer entiende). También documenta una técnica concreta y ya probada, para que la próxima sesión no pierda tiempo probando el Browser pane primero.

## Estado de propagación

No se puede editar `.claude/skills/idea_solution/SKILL.md` directo desde esta instalación — está espejado desde `CEREBRO_CORE` y bloqueado por el hook `PreToolUse`, sin excepciones. Este item queda capturado para que `/context_merge` (corrido sobre el clon de `CEREBRO_CORE`) aplique la redacción propuesta, junto con la de `2026-08-27_transversal_idea_solution_ux_discusion_antes_de_mockups`. Guardado también como memoria de sesión (`feedback`) para aplicar la técnica a mano en cualquier corrida futura de `/idea_solution` con pantallas, hasta que la SKILL.md lo refleje.

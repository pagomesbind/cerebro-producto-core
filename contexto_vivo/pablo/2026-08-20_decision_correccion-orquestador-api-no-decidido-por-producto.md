---
id: 2026-08-20_decision_correccion-orquestador-api-no-decidido-por-producto
pm: pablo
fecha_captura: 2026-08-20
fuente: "Pablo Gomes, directo en chat (sesión /idea_start sobre convenios_configuracion), 2026-08-20 — corrección sobre el item 2026-08-19_decision_api-configuracion-requisito-productos"
producto: transversal
tema: El orquestador de configuración de entidades vía API no fue una decisión formal de Producto
tipo: decision
destino_propuesto: 2_areas/direccion/decisiones.md
tipo_destino: actualizar
contradice: "2026-08-19_decision_api-configuracion-requisito-productos (mismo tema, versión previa sin esta corrección)"
confianza: alta
estado: en_cola
merge_commit:
---

**Corrección aportada por Pablo Gomes (PM líder de Producto), 2026-08-20:** el item `2026-08-19_decision_api-configuracion-requisito-productos` (todavía sin `/context_merge`) capturó que el equipo "priorizó" desarrollar un orquestador de configuración de entidades vía API en lugar de invertir en el panel Admin. Al correr `/idea_start` sobre el proyecto `convenios_configuracion` (mismo dominio — configuración de entidades/comercios), Pablo Gomes aclaró explícitamente: **esa decisión se tomó sin involucrar formalmente a Producto** — no pasó por el criterio de priorización del equipo (`2_areas/procesos/criterios_de_priorizacion.md`) ni por una evaluación de capacidad real contra el resto de la cartera.

**Decisión corregida:** el orquestador de API **no debe tratarse como una decisión de roadmap vigente ni como superador/bloqueante** de otras mejoras sobre configuración de entidades (ej. convenios). Producto evaluará y priorizará esa iniciativa de forma independiente cuando corresponda, con el mismo criterio que cualquier otra candidata de la cartera.

**Impacto en el roadmap/producto:** cualquier discovery o decisión que se apoye en "ya existe una decisión de ir por el orquestador" (incluyendo el criterio anotado en `1_proyectos/tareas.md` T-022 sobre exigir API de configuración a todo producto nuevo) debe tratarse como **propuesta pendiente de evaluación por Producto**, no como decisión cerrada. Ver la decisión de alcance equivalente tomada en `1_proyectos/convenios_configuracion/decisiones.md` (2026-08-20).

**Estado:** Corrección aportada por el PM líder — pendiente que `/context_merge` concilie ambos items (el original del 2026-08-19 y esta corrección) al escribir `2_areas/direccion/decisiones.md`.

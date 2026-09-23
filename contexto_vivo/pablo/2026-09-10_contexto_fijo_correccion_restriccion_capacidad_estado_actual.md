---
id: 2026-09-10_contexto_fijo_correccion_restriccion_capacidad_estado_actual
pm: pablo
fecha_captura: 2026-09-10
fuente: "Sesión de trabajo directa con el PM (Pablo Gomes), 2026-09-10 — corrección explícita a pedido del PM"
producto: transversal
tema: retiro de la restricción de capacidad hardcodeada (~1 IDEA/3 meses vs. ~6 abiertas) como dato duro de Gate 2
tipo: decision
destino_propuesto: 2_areas/direccion/estado_actual.md
tipo_destino: actualizar
contradice: "2_areas/direccion/estado_actual.md §Restricción de capacidad (líneas 34-38) — ese bloque afirma como dato duro '~1 IDEA entregada cada 3 meses, frente a ~6 IDEAs abiertas simultáneamente en Jira', citando la reunión de validación de estrategia del 2026-07-20. El PM aclara ahora que ese número fue un comentario coloquial dicho al pasar en esa reunión, no una medición real, y pide sacarlo como regla dura del Cerebro."
confianza: alta
estado: ingestado
merge_commit:
---

**Decisión (2026-09-10, Pablo Gomes):** sacar del canon la "Restricción de capacidad" de `2_areas/direccion/estado_actual.md` (líneas 34-38) tal como está redactada hoy — el dato "~1 IDEA entregada cada 3 meses, frente a ~6 IDEAs abiertas simultáneamente en Jira" fue un decir coloquial de una reunión (T-035, validación de estrategia del 2026-07-20), no una medición real de capacidad, y no debería seguir funcionando como el dato que "vetaría cualquier lectura optimista" en la evaluación de Gate 2 de las IDEAs.

**Reemplazo de criterio:** la capacidad real del equipo debe medirse a partir de `/sync_releases` — esa skill releva, por versión publicada, cuántos Story Points entrega cada equipo por mes, y ahí se puede distinguir cuántos de esos SP van a BAU y cuántos a Build (usando el criterio ya definido en `2026-09-03_contexto_fijo_criterios_build_bau`, item de contexto vivo pendiente de merge). Esa es la fuente que debería alimentar cualquier restricción de capacidad futura en `estado_actual.md`, no una cifra suelta de reunión.

**Acción concreta para `/context_merge` sobre `2_areas/direccion/estado_actual.md`:**
- Retirar el bloque completo "## Restricción de capacidad (contexto obligatorio para leer cualquier gap de arriba)" (líneas 34-38 al momento de esta captura).
- No reemplazarlo todavía por una cifra nueva — la cifra real de capacidad (SP/mes por equipo, split BAU/Build) todavía no se calculó a partir de `/sync_releases` (ver tarea T-083 en `1_proyectos/tareas.md`, que hace seguimiento de este pendiente). Cuando esa cifra exista, se captura un item nuevo `tipo: decision` con `tipo_destino: actualizar` sobre este mismo archivo, en vez de reescribir esta captura.

**Impacto conocido, no resuelto acá:** al menos `1_proyectos/convenios_configuracion/proyecto.md` (§ tabla de encaje, fila "Costo de oportunidad") cita textualmente esta restricción como parte de la evaluación de Gate 2/3 de ese proyecto. No se toca esa referencia desde este item — es historial de una evaluación ya hecha en una fecha puntual, y queda a criterio del PM si amerita una nota de pie ahí cuando se dé seguimiento a `convenios_configuracion/`.

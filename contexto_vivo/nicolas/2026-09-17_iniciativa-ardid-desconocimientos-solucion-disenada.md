---
id: 2026-09-17_iniciativa-ardid-desconocimientos-solucion-disenada
pm: nicolas
fecha_captura: 2026-09-17
fuente: "Sesión /idea_solution sobre ardid_desconocimientos (PRD-248), 2026-09-17"
producto: ardid
tema: ardid_desconocimientos — análisis técnico-funcional de la solución cerrado
tipo: iniciativa
destino_propuesto: 2_areas/direccion/iniciativas.md
tipo_destino: actualizar
contradice: "no"
confianza: alta
estado: en_cola
proyecto: ardid_desconocimientos
---

Novedad sobre el proyecto `ardid_desconocimientos` (PRD-248, foco Ardid de Nicolás Colón): se cerró con OK del PM el análisis técnico-funcional de la solución (vía `/idea_solution`), después del problem statement ya cerrado el 2026-09-15.

- **Diseño confirmado:** la automatización se engancha de forma síncrona al final del endpoint interno que ya usa Administración para marcar un contracargo como "desconocimiento" (no consume el webhook de contracargo ya existente, aunque ese webhook sí distingue el tipo — decisión explícita de simplicidad). Informa al motor antifraude vía el endpoint de carga masiva ya identificado en el discovery, con `motiveId` fijo (decisión del PM, sin necesidad de catálogo de motivos). La reconciliación se basa en logs propios contra la tabla de contracargos, sin consulta masiva al proveedor. El fallback manual del área de Fraude queda condicionado a que la reconciliación detecte una discrepancia, no de uso libre.
- **Hallazgo técnico relevante:** el motor antifraude identifica la transacción por el `PaymentId` de Botón Simple (el mismo ID que ya usa para el análisis original), no por el ID interno de Cobro — la resolución de ese identificador queda delegada al equipo de desarrollo tercerizado como detalle de implementación.
- **El pedido pendiente a Pentass** (mecanismo de carga individual, todavía sin construir del lado del proveedor) entra en la estimación de costo total del proyecto (~1 SP de referencia, dado por el PM) aunque no tenga diseño técnico propio todavía.
- **Quedan 7 puntos técnicos a validar con Fintexa/Pentass** antes de implementar (ninguno bloquea el diseño funcional ya cerrado) — ver `1_proyectos/ardid_desconocimientos/gaps.md` y la tarea T-060 en `tareas.md`.

Detalle completo en `1_proyectos/ardid_desconocimientos/artefactos/ardid_desconocimientos-solution.md` (v1.1).

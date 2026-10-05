---
id: 2026-10-02_transversal_decision_jira_tipo_observacion_vs_defecto
pm: pablo
fecha_captura: 2026-10-05
fuente: "/sync_meetings — reunión 'Revisión Pruebas QA', 2026-10-02 15:00, Drive docId 16r7p9ju0LLiqe6S0oU9t39Gl_kAbznyrvOB4njR8NUc"
producto: transversal
tema: Nuevo tipo de incidencia en Jira para separar observaciones de QA de defectos formales
tipo: decision
destino_propuesto: 2_areas/procesos/gestion_jira.md
tipo_destino: actualizar
contradice: "no"
confianza: alta
estado: en_cola
merge_commit:
---

**Contexto (reunión "Revisión Pruebas QA", Bind PSP + Fintexa, 2026-10-02):** hoy QA (Bind) reporta errores/incidencias detectados en pruebas, pero es Producto quien decide finalmente qué observaciones entran a una versión — sin que Jira distinga formalmente entre una "observación" (hallazgo de QA, no necesariamente bloqueante) y un "defecto" confirmado.

**Decisión acordada:** incorporar un **nuevo tipo de tarea en Jira** para separar y distinguir formalmente observaciones de QA vs. defectos. Matías Alzogaray coordina con Daniel Romano (Fintexa) la implementación técnica y evalúa si hace falta una migración masiva de tickets históricos o si el cambio aplica desde la versión 74 en adelante. Reglas acordadas para los tickets, independientemente del tipo:
- El **título** de la historia/ticket mantiene una descripción funcional clara (no se reemplaza por detalle de cliente).
- Los **detalles del cliente afectado e impacto de negocio** se agregan en el cuerpo del ticket, no en el título — pedido explícito de Andrea Orsini (QA) para poder evaluar impacto sin perder la función de búsqueda por título.
- Melisa Belpassi (Fintexa) pide además que Producto aclare en el ticket si una observación corresponde o no a la versión en curso.

**Además, en la misma reunión:** se acordó documentar formalmente la "Definition of Done" (Melisa Belpassi, en construcción junto con Andrea Orsini, tomando como base los requerimientos de QA Bind) y crear una fuente documental tipo wiki compartida entre BIN PCP y Fintexa para flujos/integraciones/productos (propuesta de Andrea Orsini, sin fecha ni owner confirmado todavía).

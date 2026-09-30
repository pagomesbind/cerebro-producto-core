---
id: 2026-09-29_transversal_salud_api_clientes_creado_en_jira
pm: pablo
fecha_captura: 2026-09-29
fuente: "/idea_jira — sesión de creación en Jira de PRD-262, tras un bloqueo intermedio por caída del conector Atlassian"
producto: transversal
tema: API Health — creación completa en Jira (IDEA, Epic, Historias)
tipo: iniciativa
proyecto: PRD-262
pm_destino:
destino_propuesto: 2_areas/direccion/iniciativas.md
tipo_destino: actualizar
contradice: "no"
confianza: alta
estado: ingestado
merge_commit:
---

La IDEA "API Health" (PRD-262 — API de consulta de salud y disponibilidad de productos para clientes externos, incluyendo terceros como Coelsa/el banco emisor) completó su ciclo de especificación de Producto y quedó totalmente creada en Jira el 2026-09-29:

- IDEA PRD-262 transicionada de DISCOVERY a EN APROBACION, prioridad High, SP estimado 16 (Modo Historias, rango de riesgo 16-31), descripción actualizada con el PRD completo.
- Epic SER-70 creada en el proyecto **SER (Servicios)** — decisión explícita del PM de que el desarrollo de este proyecto (ejecutado por un equipo ad hoc externo, Keepit Simple) se registre en ese espacio, reservado a los proyectos asignados a Keepit.
- 2 Historias en Backlog bajo la Epic: SER-71 (endpoint `GET /v1/health`, prioridad High) y SER-72 (límite de consultas, prioridad Medium).

Sigue pendiente de Ingeniería/Keepit el dimensionamiento técnico real de la parte de terceros (tamaño, plazo y granularidad de la integración con la fuente de observabilidad de red) — esa es la próxima novedad esperada de este proyecto.

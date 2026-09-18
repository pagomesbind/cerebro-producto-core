---
id: 2026-09-18_iniciativa_la_virginia_ob_pj_deploy_confirmado_17_09
pm: pablo
fecha_captura: 2026-09-18
fuente: "/sync_meetings — 5 reuniones (2026-09-09 a 2026-09-16), ver proyecto-la-virginia-ob-pj/proyecto.md §20"
producto: onboarding
tema: PRD-223 (La Virginia OB PJ) — salida a producción confirmada el 17/09, corrida 1 día por falla de coordinación Fintexa↔Soluciones Andinas
tipo: iniciativa
proyecto: PRD-223
destino_propuesto: 2_areas/direccion/iniciativas.md
tipo_destino: actualizar
contradice: "no"
confianza: alta
estado: en_cola
merge_commit:
---

La entrega de onboarding jurídico asistido por operador para La Virginia (PRD-223), que venía con fecha en duda desde el 2026-09-02, se confirmó y ejecutó: la fecha final de salida a producción terminó siendo el **jueves 17 de septiembre de 2026** (no el 18 originalmente comprometido, ni el 16 que se intentó adelantar) — el corrimiento de 1 día se debió exclusivamente a que Fintexa no le comunicó a tiempo a Soluciones Andinas qué documentación de análisis de riesgo hacía falta, no a un problema de QA (que venía sin bloqueantes de alta prioridad) ni de infraestructura (Cristian Bonafede, Fintexa, calificó el riesgo técnico como mínimo por ser una aplicación aislada). Se confirmó contra registros de producción que **La Virginia usa activamente** el flujo (solicitudes recientes de agosto y septiembre); **Octagon** tiene la entidad creada pero con uso incierto (última solicitud en junio). El despliegue no requirió cambio de URL/backoffice visible para el cliente. Detalle completo en `1_proyectos/proyecto-la-virginia-ob-pj/proyecto.md` §20.

---
id: 2026-09-23_iniciativa-titularidad-tarjeta-historias-y-jira
pm: nicolas
fecha_captura: 2026-09-23
fuente: "Skills /idea_us e /idea_jira sobre titularidad_tarjeta (PRD-25), sesión 2026-09-23"
producto: Adquirencia (Botón Simple)
tema: Validación de titularidad de tarjeta — historias confirmadas y bajadas a Jira
tipo: iniciativa
destino_propuesto: 2_areas/direccion/iniciativas.md
tipo_destino: actualizar
contradice: "no"
confianza: alta
estado: ingestado
merge_commit: 2bc1252
proyecto: titularidad_tarjeta
---

El proyecto de validación de titularidad de tarjeta en Botón Simple (PRD-25) tiene sus historias de usuario confirmadas por el PM y ya bajadas a Jira:
- **Epic:** AD-1814, con el análisis técnico-funcional completo y vinculada a PRD-25.
- **AD-1815:** validación con MODO después de Ardid (Must, High).
- **AD-1816:** registro del motivo específico de rechazo (Should, Medium).
- **AD-1817:** caché opcional de validaciones (Could, Low). No está comprometida; se decide si se construye junto con la aprobación.

Las tres historias quedaron en Backlog. PRD-25 sigue en EN APROBACION, ahora con prioridad High, Cliente SOPORTE y el PRD v1.3 sincronizado.

Definiciones nuevas de la sesión:
- Los rechazos se registran con motivo "Rechazada por Ardid" o "Rechazo por MODO".
- El procesador de pagos no valida la titularidad en todos los casos, que es la justificación de fondo del proyecto.
- La caché opcional no incluye un mecanismo manual de invalidación para Soporte.

Queda pendiente la revisión de Emma Vignoles (COO).

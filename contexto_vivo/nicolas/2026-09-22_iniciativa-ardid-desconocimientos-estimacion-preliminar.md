---
id: 2026-09-22_iniciativa-ardid-desconocimientos-estimacion-preliminar
pm: nicolas
fecha_captura: 2026-09-22
fuente: "Sesiones /idea_prd y /idea_estimate sobre ardid_desconocimientos (PRD-248), 2026-09-22"
producto: ardid
tema: ardid_desconocimientos — PRD escrito y estimación preliminar de Producto (14 SP)
tipo: iniciativa
destino_propuesto: 2_areas/direccion/iniciativas.md
tipo_destino: actualizar
contradice: "no"
confianza: alta
estado: en_cola
proyecto: ardid_desconocimientos
---

Novedad sobre el proyecto `ardid_desconocimientos` (PRD-248, foco Ardid de Nicolás Colón): se escribió el PRD formal (v1.1) y se corrió una estimación preliminar de Producto en Modo Proyecto.

- **PRD:** recapitula problema, solución, objetivos y caso de negocio ya cerrados en sesiones anteriores. Propone una priorización MoSCoW (automatización MUST, retención y pedido al proveedor SHOULD) que todavía no tiene confirmación literal del PM. Checklist operativo por las 7 áreas completo, mayoría "no aplica" por ser un proyecto interno sin impacto comercial/legal/facturación; quedan preguntas abiertas en Soporte, Fraude, Legales e IT antes del go-live.
- **Estimación:** 14 SP totales, rango de riesgo 14–24 (con OK del PM) — 3 SP el aviso automático (analogía con la extensión de Pago QR al motor antifraude, 5 SP), 7 SP el mecanismo de reconciliación (sin precedente en el historial de Ardid, la pieza más cara — el PM la va a llevar a Emma Vignoles como una decisión de construir o no, no solo un número a aprobar), 3 SP la ampliación de retención, 1 SP el pedido al proveedor (cifra ya dada por el propio PM). El rango sube por tocar código de validación antifraude (gate de CI/CD más exigente) y por gaps técnicos todavía sin confirmar con el equipo de desarrollo/proveedor.
- **Carga en Jira:** tanto la descripción del PRD como el campo de SP estimado fallaron repetidamente (4 intentos) con un error de permisos del conector de Atlassian ("app not installed" en la instancia) — no es un problema de contenido. El contenido completo se entregó al PM para pegarlo manualmente mientras se resuelve el permiso.

Detalle completo en `1_proyectos/ardid_desconocimientos/artefactos/ardid_desconocimientos-prd.md` (v1.1) y `proyecto.md` §4.

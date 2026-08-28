---
id: 2026-08-25_iniciativa_prd147_zip_worldsys
pm: pablo
fecha_captura: 2026-08-25
fuente: "/sync_meetings — reunión técnica 'API KYC - Documentos' con Worldsys (Matias Quimey Larumbe) y María Victoria Simonetti (PLD, Banco Industrial), 2026-08-25"
producto: onboarding
tema: "PRD-147 (legajo Worldsys) — mecanismo de envío acordado (ZIP por onboarding) y cierre de la convivencia batch/API"
tipo: iniciativa
proyecto: PRD-147
destino_propuesto: 2_areas/direccion/iniciativas.md
tipo_destino: actualizar
contradice: "no"
confianza: alta
estado: ingestado
merge_commit: 75959e2
---

## Novedad puntual — PRD-147, 2026-08-25

Reunión técnica con Worldsys cerró 2 preguntas abiertas de arquitectura de la integración con ComplianceOne: (1) confirmó que el batch diario existente (`LAVADOCLIENTES`) y la nueva API online no colisionan — mismo registro de persona, deduplicado por CUIT, conviven sin fecha de corte de baja del batch; (2) definió que el envío de documentación pasa a ser un **ZIP consolidado por onboarding** (no un documento por documento como estaba diseñado hasta ahora), con un TXT de auditoría embebido cuando el onboarding fue delegado a un tercero. Quedó abierto y en revisión con Worldsys el esquema exacto del campo de código de entidad que hace falta agregar a `POST`/`PATCH profile/customers` (hoy no documentado, específico del modelo multientidad de BIN PCP). Detalle completo en `1_proyectos/proyecto-onboarding-estrategico/prd-147_legajo_worldsys/proyecto.md` §5, `decisiones.md` y `gaps.md` (2026-08-25).

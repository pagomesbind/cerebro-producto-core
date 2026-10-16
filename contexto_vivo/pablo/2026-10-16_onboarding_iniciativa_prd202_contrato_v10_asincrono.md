---
id: 2026-10-16_onboarding_iniciativa_prd202_contrato_v10_asincrono
pm: pablo
fecha_captura: 2026-10-16
fuente: "Reunión 'Checkpoint OB+Wallet' del 2026-10-15 (Gemini) + sesión de análisis del 2026-10-16 con Pablo Gomes"
producto: onboarding
tema: PRD-202 (API KYC fase 1) pasa a contrato v10.0 con alta asíncrona y aviso por eventos
tipo: iniciativa
proyecto: PRD-202
pm_destino:
destino_propuesto: wiki/2_areas/direccion/iniciativas.md
tipo_destino: actualizar
contradice: "no"
confianza: alta
estado: en_cola
merge_commit:
---

**Novedad PRD-202 (API wallet orquestando OB — Fase 1), 2026-10-16:** tras el primer checkpoint de refinamiento con los desarrolladores de Wallet (Juan Pablo Carubelli, Martín Hovanyecz) y de Onboarding (Cristian Bonafede), el contrato pasa a v10.0. Cambios de fondo: el alta (`POST /cuenta/kyc`) responde `PENDIENTE` apenas Onboarding confirma recepción y el resultado llega por aviso → webhook a la organización; se eliminan el estado `PROCESANDO` y el timeout de degradación; la respuesta de Wallet es plana, con identificador propio; el aviso interno Onboarding → Wallet se resuelve como evento encolado (RabbitMQ, colas quorum) —integración nueva para Onboarding, hoy aislado, que es el principal riesgo de plazo—; se rechazan CUIT de persona jurídica; se suman TTLs a `VENCIDA` para las esperas y retención de archivos con metadata permanente en Onboarding; el resguardo de legajo/evidencia queda para una segunda etapa. Meta de producción: noviembre, con margen a mediados de diciembre, sin subir legajos a Worldsys. Historias de Jira (WS-1560…1564, OB-235…238) y Epics (WS-1559, OB-234) actualizadas el mismo día.

Fuente: reunión "Checkpoint OB+Wallet" (2026-10-15) y decisiones del PM del 2026-10-16 (`prd-202_onboarding_consolidado/decisiones.md`).

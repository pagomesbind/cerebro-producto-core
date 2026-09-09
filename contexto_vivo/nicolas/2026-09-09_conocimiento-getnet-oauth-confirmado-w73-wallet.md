---
id: 2026-09-09_conocimiento-getnet-oauth-confirmado-w73-wallet
pm: nicolas
fecha_captura: 2026-09-09
fuente: "Mail \"RE: Version W 73 Wallet Service\" — Nicolas Pomponio (Fintexa), 2026-09-08 20:59"
producto: wallet
tema: Alcance técnico confirmado del desarrollo Getnet dentro de W73 — autenticación configurable del aceptador y modelo de datos con soporte OAuth
tipo: conocimiento
destino_propuesto: 3_recursos/detalle_productos/wallet/interoperabilidad_qr_getnet.md
tipo_destino: actualizar
contradice: "no"
confianza: alta
estado: en_cola
---

Fintexa confirmó (mail "RE: Version W 73 Wallet Service", 2026-09-08) el alcance técnico definitivo del desarrollo de Getnet dentro de la versión **W73** de Wallet, ya documentado a nivel de especificación en `interoperabilidad_qr_getnet.md` pero sin fecha de versión/entrega concreta hasta ahora:

- **Autenticación configurable del aceptador** al resolver un código QR (el circuito interoperable de Getnet expone el endpoint `/resolve` con OAuth2 `client_credentials`, ver especificación ya documentada en este mismo archivo).
- **Gestión de aceptadores con mecanismo de autenticación configurable** — esto implica **adaptar el modelo de datos de aceptadores** (hoy en producción con el feature flag de OAuth apagado) para soportar OAuth **además** del esquema de autenticación actual, no en reemplazo.
- **Entrega a QA Externo: 21/09.**

Esto confirma que el desarrollo pasó de fase de análisis (ticket levantado por Fintexa el 05/09, sin fecha) a alcance de versión con fecha concreta de QA — ver actualización del riesgo asociado en `[[2026-09-09_riesgo-getnet-resuelto-via-w73-wallet-qa-21-09]]`, incluida la alta probabilidad de que sea la misma migración que el proyecto `getnet_oauth2_resolve/` (PRD-237/PRD-238) de Pablo Gomes.

> Fuente: Mail "RE: Version W 73 Wallet Service" (hilo 2026-09-03 → 2026-09-09), mensaje del 2026-09-08 20:59 de Nicolas Pomponio (Fintexa).

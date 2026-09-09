---
id: 2026-09-09_riesgo-getnet-resuelto-via-w73-wallet-qa-21-09
pm: nicolas
fecha_captura: 2026-09-09
fuente: "Mail \"RE: Version W 73 Wallet Service\" — Nicolas Pomponio (Fintexa), 2026-09-08 20:59"
producto: wallet
tema: Actualización del riesgo Getnet (deadline 30/09) — Fintexa reformuló el alcance de W73 para incluir el desarrollo sin correr la fecha, entrega a QA Externo 21/09
tipo: riesgo
destino_propuesto: 2_areas/riesgos.md
tipo_destino: actualizar
contradice: "no"
confianza: alta
estado: ingestado
---

**Actualiza el riesgo ya mergeado** `2026-09-06_riesgo-getnet-deadline-30-09-billetera-circuito-interoperable` (archivado en `4_archivos/contexto_ingestado/`, producto wallet, deadline duro 30/09 confirmado por Emma Vignoles) — este item no se edita, se resume acá el cambio de estado para que `/context_merge` lo aplique como delta sobre `2_areas/riesgos.md`.

Fintexa (Nicolas Pomponio, PM) informó el 2026-09-08 el cierre de la reunión de revisión de la versión **W73 de Wallet**: evaluaron 3 opciones para incorporar el desarrollo de Getnet sin correr la fecha de fin de mes — reformular W73 recortando alcance (**adoptada**), estirar Getnet para más adelante (descartada), o mantener W73 como estaba y patear todo (descartada). El desarrollo de Getnet queda dentro de W73: "autenticación configurable del aceptador al resolver un código QR y gestión de aceptadores con mecanismo de autenticación configurable" (detalle técnico completo en el item de conocimiento `[[2026-09-09_conocimiento-getnet-oauth-confirmado-w73-wallet]]`).

**Fecha de entrega a QA Externo confirmada: 21/09** (lunes) — antes del deadline duro del 30/09, aunque el propio mail advierte que "dado lo ajustado del cronograma es posible que se necesite correr QA en paralelo para algunos de los desarrollos". Sigue sin haber, en este mail, un plan de contingencia explícito si QA o el pase a producción se corren más allá del 30/09.

**Resuelve además la pregunta abierta en T-031** (`1_proyectos/tareas.md`, actualizada 2026-09-08 vía `/context_pull`) sobre si este riesgo es la misma migración que el proyecto `getnet_oauth2_resolve/` de Pablo Gomes (PRD-237/PRD-238): la descripción técnica de este mail (autenticación configurable del aceptador, adaptar el modelo de datos de aceptadores para soportar OAuth) coincide con "mismo proveedor, mismo endpoint `/resolve`, mismo mecanismo OAuth2 `client_credentials`, mismo deadline 30/09" ya anotado en T-031 — **alta probabilidad de que sea la misma migración vista desde dos fuentes** (mail técnico a Wallet/Integraciones vs. proyecto formal de Pablo Gomes). Sigue pendiente confirmación explícita con Pablo Gomes antes de fusionar ambos registros para evitar doble conteo.

> Fuente: Mail "RE: Version W 73 Wallet Service" (hilo 2026-09-03 → 2026-09-09), mensaje del 2026-09-08 20:59 de Nicolas Pomponio (Fintexa).

---
id: 2026-09-04_wallet_versión_intermedia_qr_getnet
pm: pablo
fecha_captura: 2026-09-04
fuente: "Reunión 'Producto - Prioridades v1 + v2' (2026-09-04) — retirado el 2026-09-07, confirmado por el PM como descripción imprecisa del mismo hecho ya capturado en 2026-09-04_wallet_decision_migracion_getnet_hard_deadline"
producto: wallet
tema: RETIRADO — falso requerimiento de "versión intermedia de código QR" para Getnet
tipo: conocimiento
destino_propuesto: ninguno — no crear nada en el canon a partir de este item
tipo_destino: crear
contradice: "no — corrige/retira una captura propia anterior, no contradice otra fuente"
confianza: baja (premisa técnica desmentida)
estado: ingestado
merge_commit:
---

**RETIRADO (2026-09-07).** Este item capturaba, a partir de una transcripción de reunión, un supuesto requerimiento de que Wallet debía desarrollar una "versión intermedia de código QR" para seguir leyendo los QR de los POS de Getnet tras su migración de arquitectura. El PM confirmó que es una descripción imprecisa del mismo hecho ya capturado en `2026-09-04_wallet_decision_migracion_getnet_hard_deadline` (ese item ya quedó corregido) — el problema real es que Getnet cambió el **mecanismo de autenticación** de su API Resolve (OAuth2 `client_credentials` en vez de un token fijo), no el formato del código QR. El estándar del QR (EMVCo/CIMPRA) no cambia.

**No hace falta ningún parser ni "versión intermedia" de QR.** El requerimiento real ya está completamente cubierto por el proyecto `getnet_oauth2_resolve/` (Pablo Gomes) — PRD formal, historias de usuario confirmadas y creación completa en Jira (IDEA PRD-237, Epic WS-1599, Historias WS-1600/WS-1601).

**Instrucción para `/context_merge`:** no crear ningún archivo ni sección nueva a partir de este item — queda retirado, sin destino. La única corrección real de canon a aplicar por este hallazgo vive en `2026-09-04_wallet_decision_migracion_getnet_hard_deadline` (ya corregido).

> Fuente original: Reunión "Producto - Prioridades v1 + v2" (2026-09-04 14:01 + 14:12), minutas y transcripción Gemini. Retiro confirmado por el PM el 2026-09-07.

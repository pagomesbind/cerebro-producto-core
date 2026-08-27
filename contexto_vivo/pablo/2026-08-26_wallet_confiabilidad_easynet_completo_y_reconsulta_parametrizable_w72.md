---
id: 2026-08-26_wallet_confiabilidad_easynet_completo_y_reconsulta_parametrizable_w72
pm: pablo
fecha_captura: 2026-08-26
fuente: "/sync_releases — Jira bindpsp.atlassian.net, versión W 72 (publicada 2026-08-18), tickets WS-1416, WS-1273"
producto: wallet
tema: Migración EasyNet de transferencias entrantes completada; tiempo de reconsulta de operaciones ahora parametrizable
tipo: conocimiento
destino_propuesto: 3_recursos/detalle_productos/wallet/historial_confiabilidad_transferencias_y_comprobantes.md
tipo_destino: actualizar
contradice: "3_recursos/detalle_productos/wallet/historial_confiabilidad_transferencias_y_comprobantes.md §10 — el párrafo de WS-1387 (W 71.1 FIX) dice 'Deuda técnica reconocida: la migración debería extenderse al resto del flujo... todavía no migrados'. WS-1416 (W 72) cierra exactamente esa deuda."
confianza: alta
estado: ingestado
merge_commit: 75959e2
---

**1. Migración a EasyNet del flujo completo de Transferencias Entrantes — cierra la deuda técnica de §10 ([WS-1416](https://bindpsp.atlassian.net/browse/WS-1416), 3 SP, Epic WS-564):**

§10 ya documenta que W 71.1 FIX (WS-1387) migró solo el evento `ProcesarTransferenciaEntranteEvent` en MS BIND a EasyNet (mecanismo que reintenta automáticamente en otro POD si el actual falla), a raíz del incidente del 2026-07-14 (`Channel unusable due to continuation timeout` de RabbitMQ, mala gestión de MassTransit), dejando explícito que la migración **debía extenderse** al resto del flujo en MS Operaciones y MS Comprobantes.

WS-1416 completa esa extensión: se migran a EasyNet los 3 microservicios/colas restantes del flujo de Transferencias Entrantes — **MS Bind, MS Operaciones, MS Comprobantes**, colas `BindWebHookTransferEvent`, `ComprobanteDeOperacionCreadoEvent`, `OperacionSinComprobanteEvent`. Con esto el flujo completo de transferencias entrantes queda cubierto por el mecanismo de reintento entre PODs, ya no solo el primer tramo. Validado por Andrea Orsini el 2026-08-04 con regresión de transferencias entrantes exitosa.

**2. Tiempo de reconsulta de operaciones ahora parametrizable por especificación — ⚠️ publicado aún EN QA ([WS-1273](https://bindpsp.atlassian.net/browse/WS-1273), 3 SP, Epic WS-1310):**

A diferencia del resto de los tickets de esta versión, este quedó en estado **"EN QA"** al momento de la publicación de W 72 (no "Finalizada") — coherente con la regla de la skill de que el criterio de publicación es de la versión, no del ticket.

Nueva funcionalidad: especificaciones de Wallet parametrizan (en segundos, hasta 2 decimales) el tiempo con el que se hace la primera reconsulta de una operación después de creada, por cada uno de 3 tipos: **Pago QR, Transferencias Salientes, Debin Recurrente**. Si la especificación no existe o vale "0", se usa el AppSetting actual (fallback sin romper nada). Se agregó además una **segunda reconsulta**, configurable por una especificación aparte, que se ejecuta solo si la primera no logró resolver la operación (y solo si existe la especificación de la primera — si no existe, la segunda ni se evalúa). Objetivo de negocio: reducir el tiempo de finalización de operaciones ajustando estos tiempos sin necesidad de deploy. Relacionado conceptualmente con el StateMonitor y su historial de ajustes ya documentado en este archivo (§7, §9).

**Al mergear:** en §10, reemplazar/ampliar el párrafo de WS-1387 con la confirmación de que la migración EasyNet de transferencias entrantes quedó completa en W 72 (agregar la entrada de WS-1416); agregar WS-1273 como nueva entrada del tramo W72, dejando explícito su estado "EN QA" al momento de esta ingesta (a confirmar en el próximo barrido si ya pasó a Finalizada).

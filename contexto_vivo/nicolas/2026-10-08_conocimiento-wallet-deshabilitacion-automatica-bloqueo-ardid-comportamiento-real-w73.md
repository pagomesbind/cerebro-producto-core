---
id: 2026-10-08_conocimiento-wallet-deshabilitacion-automatica-bloqueo-ardid-comportamiento-real-w73
pm: nicolas
fecha_captura: 2026-10-08
fuente: "Jira PRD-187 (IDEA en Shipping) + WS-1398, WS-1399 y WS-1857 (historias, reportes de QA de Fintexa y comentarios de desarrollo, 2026-07-31 → 2026-10-07)"
producto: wallet
tema: Deshabilitación automática de cuentas de Wallet por bloqueo de Ardid (W73) — comportamiento real implementado, motivos que la disparan, webhook y auditoría
tipo: conocimiento
destino_propuesto: 3_recursos/detalle_productos/ardid/integracion_con_productos_bind.md
tipo_destino: actualizar
contradice: "Parcial: integracion_con_productos_bind.md §21 describe el webhook como 'nuevo'; en realidad se reutiliza el evento DESHABILITAR_CUENTA existente con campos opcionales nuevos"
confianza: alta
estado: en_cola
---

Completa §21 de `integracion_con_productos_bind.md` (WS-1398) con lo que efectivamente se implementó y testeó en W73, según los comentarios de los tickets.

**Motivos de Ardid que deshabilitan la cuenta** (definición final del PM del 01/10, comentario en WS-1398, y código `AnalyzeTransferDtoResponse.IsBlocked`):
- `TRANSFER_BLOCK_ACCOUNT` (exacto).
- `CLIENT_BLOCKED` (exacto): el cliente ya fue bloqueado por un análisis anterior, o a mano desde el front de Ardid. También llega así la transferencia saliente frenada por una regla estándar (QA propone unificar ese texto, observación no frenante).
- Cualquier `reason` que contenga `BLOCK_USER` (ej. `CUIT/CUIL_IN_BLACKLIST_BLOCK_USER`).
- `ReputationalRules Riesgo alto` (sumado el 01/10 tras un caso de QA). Con "Riesgo medio" solo se rechaza la operación.
- `TRANSFER_BLOCKED` **no** deshabilita: estaba en el texto original de la historia y el PM lo descartó explícitamente el 01/10.
- Cualquier otro `reason` no deshabilita (decisión aprobada el 12/08, AgDR-DEM-1698-001).

**Flujos alcanzados** (QA Fintexa, 05/10): transferencias salientes y entrantes, Pago QR, DEBIN Recurrente y Pago FX. En **transferencias entrantes Wallet siempre acredita** y después deshabilita. En DEBIN iniciado por el titular, Ardid analiza antes de acreditar y puede rechazar.

**Webhook:** se reutiliza el evento `DESHABILITAR_CUENTA` existente (no hay evento nuevo). Así ninguna organización necesita una fila nueva en `NotificacionParametros`. Motivo `BLOQUEO_MONITOREO_TRANSACCIONAL`. Suma los campos opcionales `fecha` (UTC-3), `detalle` (= `reason` de Ardid) y `referencia` (`"{Operacion}: {ArdidTransactionId}"`), que no viajan en el flujo de contracargo de DEBIN. Se mantiene `cuentaId` (no `IdCuenta`) para no romper a quienes ya lo consumen. WS-1857 pedía alinear esto con el texto de la historia y se cerró como "No aplica" (07/10). Idempotente por `CuentaId + ArdidTransactionId`: un reintento no duplica, pero un bloqueo nuevo sobre una cuenta ya deshabilitada sí manda otro webhook y deja otra fila.

**Auditoría (WS-1399):** el PATCH `/Habilitado/Cuenta/{id}` acepta `motivo` opcional (máx. 100 caracteres, inclusivo; con 101 devuelve 400). Con `x-entidad` de otra organización devuelve 422 (código 1028). Todo cambio queda en `dbo.CuentasAuditoria` (singular), incluso las llamadas sin cambio de estado (el PM lo aceptó el 06/10). Hay un flag `RehabilitadaPostBloqueoArdid` que vale 1 si la última baja fue por `BLOQUEO_MONITOREO_TRANSACCIONAL`. Se agregan `ArdidRequestBody`/`ArdidResponseBody`, sin PII (se emite el warning EventId 1283 si llega PII). Desde este deploy, PRD deja de loguear los parámetros SQL, y hay que avisarle a Soporte.

**Fricción detectada (cliente COTO, comentario del PM 2026-10-08):** COTO bloquea y desbloquea usuarios desde el front de Ardid (Reporte de Clientes, switch "Bloqueado"). El desbloqueo en Ardid no llega a Wallet, así que ahora además tienen que llamar al PATCH de habilitación, algo que no está en su flujo. Producto armó una guía de integración: `outputs/2026-10-08_guia-cuentas-bloqueadas-ardid-wallet.html`.

# Recycle — Cobro automático de deudas pendientes en Wallet

> Estado: en producción.

> Contenido destilado de las Epics de Notion "Motor general de recycle" (Recycle V2, 75 SP estimados) y "Parche de recycles de viajes" (Recycle V1, específico de TIN). Ambas Epics están etiquetadas explícitamente `wallet back`/`wallet app` en el backlog — se reclasifican como Wallet, no como Agente de Cobros y Pagos, pese a que el nombre "recycle" evoca cobranza.

## 1. Qué problema resuelve

Cuando una organización intenta cobrar un comprobante de débito a un usuario (ej. impuesto, cuota, viaje QR) y el usuario no tiene saldo suficiente en el momento, ese comprobante queda **pendiente**. Recycle es el mecanismo que monitorea esas cuentas con deuda pendiente y, en cuanto detecta que ingresó saldo (cash-in, transferencia, etc.), dispara automáticamente el cobro de la deuda antes de permitir otros usos del dinero recién acreditado — sin intervención manual.

## 2. Recycle V1 — origen específico de TIN (Viajes QR)

La primera versión de Recycle nació acotada al caso de uso de **TIN**: viajes QR de colectivo que no se pudieron debitar en el momento (viaje offline, tardanza del colectivo en informar el viaje, saldo insuficiente).

- **Regla de negocio central**: ante un crédito en la cuenta, se ejecutan los comprobantes de viaje pendientes ordenados por fecha de creación (más viejo primero); no se permiten pagos parciales de un viaje individual — se salda el total o se deja la deuda intacta.
- **Límite de viajes pendientes**: para prevenir fraude (viajar gratis indefinidamente combinando el modo offline con la demora del colectivo en informar), un usuario no puede generar un nuevo Viaje QR válido (online u offline) si ya tiene más de N viajes pendientes de recycle (configurable por organización, default 3 para TIN).
- Alcance explícitamente acotado a comprobantes de TIN (viajes) — no a cualquier tipo de comprobante pendiente; y sin flag especial en el comprobante que distinga un débito "reciclado" de uno normal (se decidió que ya alcanza con comparar fecha de aviso del viaje vs. fecha de creación del comprobante).
- **Nunca construido**: poder aplicar débitos de recycle a una cuenta deshabilitada (para poder deshabilitar cuentas fraudulentas sin perder la posibilidad de recuperar la deuda si vuelven a fondearse) — quedó en estado "Refinar", sin desarrollo.

### Cluster de bugs de Recycle V1 (TIN Viajes QR)

- El límite de viajes pendientes se activaba con solo **1** comprobante pendiente en vez del valor configurado (3) en Especificaciones de la Organización.
- Mensajes de error genéricos (app y backend) cuando se alcanzaba el límite de pendientes — no orientaban al usuario a que la solución dependía de él (pagar la deuda).
- Mensaje de error incorrecto ("error al conectar con el servidor") al intentar hacer login sin viajes pendientes disponibles — mismo problema de transparencia de errores visto en otras Epics de Wallet.
- El límite de viajes QR **offline** tenía un tope fijo de 5, independiente del límite configurable online (3) — permitía más reintentos sin conexión que los que debería.
- Bug de seguridad: un usuario que alcanzaba el límite online podía desconectarse de internet y seguir generando viajes QR offline, evadiendo el límite.
- `FechaReintento` se recalculaba cada vez que se reprocesaba un comprobante pendiente, en vez de conservar la fecha del primer reintento — rompía la trazabilidad de cuánto tiempo lleva pendiente una deuda.
- Los débitos pendientes no se procesaban de forma inmediata ante el crédito entrante, sino que esperaban al ciclo de reintento programado normal.
- Con dos débitos pendientes, si el crédito entrante solo alcanzaba para pagar el segundo (más reciente), el sistema no lo intentaba — solo reintentaba el primero de la cola y se detenía ahí aunque hubiera saldo para el otro.
- El Viaje QR relacionado a veces quedaba en estado `EN_PROCESO` en `dbo.ViajesQR` a pesar de que el comprobante de débito ya se había efectivizado — bug de sincronización de estado entre el comprobante y la entidad de negocio del viaje. **Confirmado en producción y corregido con hotfix dedicado** ([WS-908](https://bindpsp.atlassian.net/browse/WS-908), versión **W 69.3 HF (Tin)** publicada 2026-05-13, a raíz de reclamo real de TINPAY/EM-379: al usuario le aparecía el cartel de deuda por un viaje que ya tenía debitado; el registro en `WalletTinDB` no tenía reintentos). Fix validado con pruebas de stress del lado de Fintexa.

## 3. Recycle V2 — motor general (MS `Shared.Recycle`)

Rediseño completo como microservicio dedicado, event-driven, integrado por bus de eventos con las APIs de Wallet (Cuenta, Operaciones, Comprobantes) — generalizando el mecanismo para **cualquier tipo de comprobante pendiente**, no solo viajes de TIN. Habilitación por tipo de comprobante vía Especificación de Organización (`ID_TIPO_COMPROBANTE_RECYCLE`).

Diseñado y documentado como 11 pasos incrementales:

1. **Modelo de datos + Consumers**: nuevo MS con consumers para los eventos de entrada (`AccountMarkedForMonitoringEvent`, `AccountCreditReceivedEvent`, `OperationPaidEvent`).
2. **Registro de cuenta para monitoreo**: si un débito no tiene saldo suficiente, se marca la cuenta como `MONITORED_ACCOUNT` (`IsActive=true`) y se registra la operación pendiente en `DEBT_OPERATION`.
3. **Detección de créditos entrantes**: ante `AccountCreditReceivedEvent` en una cuenta monitoreada activa con saldo suficiente, se dispara `RecycleProcessRequestedEvent`.
4. **Priorización y cálculo de cobros**: ordena las deudas pendientes (FIFO por defecto, configurable) y calcula cuánto cobrar según el saldo disponible, generando el plan de cobro (`RECYCLE_PROCESS_ITEM`).
5. **Ejecución del cobro y actualización de estados**: crea `RECYCLE_PROCESS` + items, actualiza operaciones a `COMPLETED`/`PARTIALLY_PAID`, dispara `DebtFullyPaidEvent`/`DebtPartiallyPaidEvent`. Quedó pendiente una revisión de este paso para poder atender más de un evento de crédito por cuenta en simultáneo (hoy solo se procesa 1) y explorar paralelización.
6. **Verificación de cobros con sistemas externos**: confirma que Wallet/Operaciones/Comprobantes efectivamente reflejaron el pago (`IsVerified=true`), registrando discrepancias si las hay.
7. **Finalización del monitoreo sin deudas**: cuando `TotalDebtAmount=0` y no hay operaciones pendientes, dispara `AccountMonitoringEndedEvent` y desactiva el monitoreo (`IsActive=false`).
8. **Auditoría y trazabilidad completa**: consulta de todos los eventos y correlaciones del proceso, para auditoría.
9. **Manejo de errores y reintentos**: si falla un sistema externo, el `RECYCLE_PROCESS` pasa a `FAILED` con `ErrorDetails`, y reintenta según `ProcessingRetryCount` — las operaciones que no se logran reciclar quedan pendientes hasta el próximo crédito.
10. **Prevención de procesos concurrentes duplicados**: lock/flag de proceso activo por cuenta (parámetro `MaxConcurrentProcesses`) para que dos eventos simultáneos no cobren dos veces sobre el mismo saldo.
11. **Actualización diaria del estado de monitoreo**: job periódico que revisa cuentas activas, expira el monitoreo de cuentas con más de 90 días sin operaciones pendientes (pasan a revisión manual) y actualiza métricas (`TotalDebtAmount`, `PendingOperationsCount`).

> **Atribución de release**: los pasos 9 ([WS-39](https://bindpsp.atlassian.net/browse/WS-39), "Manejo de errores y reintentos") y 11 ([WS-38](https://bindpsp.atlassian.net/browse/WS-38), "Actualización diaria del estado de monitoreo") de esta lista se publicaron en **W 65** (2025-11-17, lanzamiento del espacio WS, vía `/sync_releases`).

### Novedades publicadas en W 69 (2026-04-29) — visibilidad de pendientes para las organizaciones

> Fuente: Jira bindpsp.atlassian.net, versión W 69, tickets WS-543, WS-584, WS-987 (Epic "Mejorar recaudación de impuestos wallet").

- **Endpoint de consulta de comprobantes pendientes de Recycle** ([WS-543](https://bindpsp.atlassian.net/browse/WS-543), 7 SP): hasta acá, una organización no tenía forma de saber qué cuentas adeudaban comprobantes hasta que el débito se concretaba. Nuevo endpoint en API Comprobantes que consulta `SharedRecycleDB.dbo.DEBT_OPERATION` con filtros (`idCuenta`, `estado` PENDING/PROCESSING/COMPLETED, rango de fechas de creación, `idTipoComprobante`, `signo`), paginado (default 10×pág 1), validando `x-entidad`; requiere al menos 1 filtro (422 si no).
- **Nuevo webhook `COMPROBANTE_PENDIENTE_RECICLADO`** ([WS-584](https://bindpsp.atlassian.net/browse/WS-584)): cuando un comprobante falla su creación por falta de saldo y queda registrado para Recycle, la organización recibe aviso inmediato (antes solo se enteraba al concretarse el cobro con `COMPROBANTE_RECICLADO`). Payload igual al de reciclado pero con `comprobanteId` y `fecha` en null (el comprobante no existe aún). El nombre del evento se decidió explícitamente PM↔Fintexa para diferenciarlo del existente.
- El bug de formato PascalCase del webhook `COMPROBANTE_RECICLADO` (documentado más abajo en los bugs de regresión) **se corrigió y publicó en esta versión** ([WS-987](https://bindpsp.atlassian.net/browse/WS-987)).

### Bug de concurrencia corregido — comprobantes de impuestos faltantes en cobros por Recycle

> Fuente: Jira bindpsp.atlassian.net, versión W 70.1 (publicada 2026-06-03), ticket [WS-1082](https://bindpsp.atlassian.net/browse/WS-1082) (SOPORTE, EM-555).

Un cliente (Max Pay) reportó una transferencia saliente con impuesto cobrado según los registros de liquidación de impuestos (`LIQ_IMP_PERSONA`), pero **sin el comprobante de impuesto correspondiente** en la tabla de comprobantes de Wallet — el impuesto se calculó pero el comprobante nunca se generó. Causa: condición de carrera en el servicio que resuelve cobros de comprobantes de impuestos vía Recycle. Fix: uso de caché para controlar la concurrencia en ese punto específico del flujo. Complementa (sin reemplazar) el mecanismo de lock por cuenta de Recycle V2 (paso 10 arriba) — este bug era específico del sub-flujo de comprobantes de impuestos, no del lock general de proceso por cuenta.

### Webhook de notificación (`COMPROBANTE_RECICLADO`)

Cuando Recycle V2 logra crear un comprobante de cobro, se envía un webhook a la organización (configurable por tipo de comprobante, habilitado por defecto para los que pasan por recycle) con `mensajeId`, `evento="COMPROBANTE_RECICLADO"`, `cuentaId`, `importe`, `comprobanteId`, `tipoComprobanteId/Nombre/Signo`, `idRecycle`, `fechaInicioRecycle`, `idOperacion`. Se envía por la cola de baja prioridad del webhook sender de Wallet, para no competir con eventos operativos de mayor prioridad.

**Bugs de este webhook detectados en regresión**:
- `FechaInicioRecycle` traía una fecha "genérica" en vez de la fecha real en que el débito quedó pendiente (`CreationDate` de `dbo.DEBT_OPERATION`).
- `IdOperacion` traía el `OperationId` interno de la tabla de deuda en vez del Id de Operación de Wallet real asociada (ej. el viaje QR de TIN), o `null` si no había ninguna relacionada.
- `mensajeId` iba al final del JSON en vez de al principio, rompiendo la convención de formato del resto de los webhooks de Wallet.

Nota aparte (mismo lote de regresión, no específico de Recycle): un bug de la API de Comprobantes exponía un atributo `detalle` (incluso en `null`) en la respuesta de creación exitosa de cualquier comprobante — atributo que solo debería aparecer cuando el comprobante entra al circuito de Recycle V1 por falta de saldo.

### Contracargo de débito recurrente pasa a producción + fix de trazabilidad (semana del 2026-08-18)

> Fuente: minuta de Gemini de "Productos - Weekly Seguimiento" (2026-08-18).

**Contracargo de débito recurrente — pruebas finalizadas, pasa a producción la semana del 2026-08-18.** En la misma reunión se decidió el criterio de cuándo pasar una funcionalidad a "shipping": recién cuando esté **enteramente en producción** (no cuando solo falte el propio pase), a diferencia del criterio anterior que la marcaba shipping con trabajo pendiente del lado de Bind PSP.

**Hallazgo de trazabilidad (encontrado durante las pruebas):** existe una especificación de Wallet que habilita el aviso de "reciclado" (Recycle) en operaciones — Recycle se usa normalmente para impuestos, cuyas operaciones no tienen una operación relacionada. Con el contracargo de débito recurrente, en cambio, sí existe una operación original relacionada al momento del cobro. Sin esta especificación habilitada, cuando Recycle cobraba el contracargo, **no le avisaba a la operación original que debía cambiar de estado** — se perdía la trazabilidad entre el contracargo y la operación que lo originó. Ya se dio de alta esa especificación en **todas las organizaciones en producción** (no solo la nueva) para resolverlo de forma retroactiva.

**Decisión de comunicación:** no hace falta avisar a los clientes del contracargo en sí — el aviso relevante es interno (Comercial/todo el equipo), para que sepan que ya se le puede ofrecer a cualquier organización, con el riesgo estándar de contracargo ya conocido.

## Ver también

- [tin_tarjetero.md](tin_tarjetero.md) — TIN es el cliente de origen de Recycle V1 (Viajes QR); Recycle V2 generaliza el mecanismo para cualquier comprobante Wallet.
- [debin_y_fondeo.md](debin_y_fondeo.md) — contracargos de DEBIN recurrente, mecanismo de origen del contracargo que dispara el cobro vía Recycle documentado arriba.

---
*Fuente: Notion histórico, Epics "Motor general de recycle" (75 SP, 19 tickets) y "Parche de recycles de viajes" (13 tickets) — ingesta 2026-07-06.*

# Historial de Confiabilidad — Transferencias, Comprobantes y Reportes PLD (W65 → W70.2.1)

> Estado: histórico de versiones, mayormente en producción (bugs ya corregidos, salvo donde se indica lo contrario). Consolidado desde `detalle_productos/wallet/otros_manuales.md §2, §2.1, §4.1, §8, §8.0, §8.1, §8.4-8.7, §9, §9.1` en la reestructuración PARA en cascada (2026-08-12) — es un único tema (historial de confiabilidad por versión) que estaba disperso en secciones sueltas de un archivo-cajón. Fuente: Jira `bindpsp.atlassian.net`, versiones W65 (2025-11-17) a W70.2.1 (2026-06-16).
>
> 📌 Patrón de fondo que atraviesa todo este historial: fallos silenciosos de conexión (Redis, DB, entre microservicios) que dejaban operaciones "a medio camino" — sin comprobante, sin webhook, o con dinero debitado sin acreditar — porque el mecanismo de reintentos automático nunca se disparaba al no lanzarse ninguna excepción. El arco narrativo completo (W67→W70.2.1) es la evolución de ese problema hasta su solución estructural.

## 1. Estados de transferencia (referencia vigente)

| Código | Estado | Descripción |
|---|---|---|
| 1 | A procesar | La transacción recién nace. Inmediatamente cambiará a un nuevo estado. |
| 2 | Aprobada | Transacción acreditada. **Estado definitivo.** |
| 3 | Rechazada | La transacción tuvo un error y ya no se acreditará. No se descuenta saldo al usuario. **Estado definitivo.** |
| 4 | A consultar | Coelsa aún no resolvió el estado definitivo. Entra en proceso de consulta por un tiempo hasta actualizarlo. Generalmente pasa a estado definitivo a los pocos segundos. |
| 5 | Auditar | Coelsa no puede actualizar el estado a uno definitivo. Se marca "A Auditar" para resolución manual tras recibir el archivo batch de Coelsa y poder conciliar. Al próximo día hábil se actualiza a un estado definitivo. |
| 6 | Devuelta | El comercio (lado aceptador QR) puede devolver la compra al cliente. Si la devolución es total, la operación queda en este estado. |
| 7 | Devuelta parcial | Si la devolución del comercio es parcial, la operación queda en este estado. |

## 2. Bug crítico W70.2 — transferencia devolvía HTTP 500 pero debitaba igual, sin rollback ni webhooks

> [WS-1254](https://bindpsp.atlassian.net/browse/WS-1254) (SOPORTE, EM-640), publicado W 70.2 (2026-06-10).

**Síntoma:** en transferencias internas (particularmente las que involucraban un CVU de tipo SMSV), el guardado de la entidad fallaba y la API devolvía `HTTP 500`, pero **la transacción no hacía rollback**: el importe se debitaba de la cuenta origen y la operación quedaba en estado **Aprobada** en base de datos — sin acreditar en destino y sin disparar ningún webhook. Quedaba dinero "perdido" en tránsito desde la perspectiva del cliente.

**Causa raíz:** el nombre de la contraparte (`NombreContraparte`) superaba el límite de longitud aceptado por la entidad al guardar — el intento de persistir un nombre de más de 100 caracteres rompía el `SaveChanges` de Entity Framework a mitad de la operación, después de ya haber debitado.

**Fix:** se trunca el nombre de la contraparte en los métodos de transferencia antes de persistir.

**Hallazgo adicional durante la validación QA (no confirmado si es el mismo root cause o un caso aparte):** en algunas pruebas los webhooks sí se generaban pero llegaban a una **URL distinta** a la configurada para la organización — quedó registrado como observación, sin resolución documentada en el ticket.

## 3. Fix de confiabilidad — reintentos de creación de Comprobante ante errores de conexión (3 tickets, 2 versiones)

> [WS-1027](https://bindpsp.atlassian.net/browse/WS-1027) (W 70.1, 2026-06-03), [WS-1250](https://bindpsp.atlassian.net/browse/WS-1250) (W 70.2, 2026-06-10), [WS-1267](https://bindpsp.atlassian.net/browse/WS-1267) (W 70.2.1 Fix, 2026-06-16).

**Contexto:** `Wallet.Comprobantes` es el único microservicio de Wallet con **dos contratos** de implementación de caché (dos flujos/consumers independientes con su propia lógica de caché).

**Comportamiento anterior (bug):** ante un error de conexión (base de datos, caché Redis, o entre microservicios), el flujo de creación de comprobante no reintentaba — en el caso puntual de Redis, `CSRedisResilientCacheService.GetDataAsync` devolvía un valor **default** en lugar de lanzar excepción, lo que hacía que el flujo siguiera como si la `OperacionId` ya existiera en caché (no la procesaba) y la operación quedaba **sin `ComprobanteId`**. Al no dispararse ninguna excepción, el mecanismo de reintentos automáticos del consumer nunca se activaba: el fallo quedaba completamente silencioso.

**Cronología del fix (3 rondas — el alcance original no cubrió todos los casos):**

1. **WS-1027** (W 70.1) — ticket origen, a raíz de un reclamo de Soporte (EM-532). Incorpora reintentos de corto plazo ante errores no-de-negocio en los consumers de `ProcesarTransferenciaEntranteEventConsumer` (MS BIND), `BindWebHookTransferEventConsumer`/`ComprobanteDeOperacionCreadoEventConsumer` (MS Operaciones) y `AltaOperacionSinComprobanteEventConsumer` (MS Comprobantes); más un mecanismo de **redelivery a largo plazo** para fallos en el consumidor del mensaje.
2. **WS-1250** (W 70.2) — a raíz de un reclamo de Soporte (EM-628) que detectó casos **posteriores** al fix de WS-1027 que seguían sin reintentar. Fix puntual: `GetDataAsync` pasa de devolver default a lanzar excepción (`THROW`) ante error de conexión Redis. Aplicado solo a **uno** de los dos contratos de caché.
3. **WS-1267** (W 70.2.1 Fix) — el mismo fix, aplicado ahora al **segundo** contrato de caché (el que había quedado afuera en la ronda anterior).

**Deuda técnica reconocida y abierta** (registrada explícitamente en WS-1250): falta revisión con Infraestructura de **por qué se dan tantos errores de conexión a Redis en producción** — el fix resuelve el síntoma, no la causa raíz de la inestabilidad de conexión.

## 4. Reportes PLD — historial de problemas de generación (W68 → W70.2)

> [WS-1074](https://bindpsp.atlassian.net/browse/WS-1074) (hotfix dedicado W 69.2 HF (PLD), 2026-05-12), [WS-1177](https://bindpsp.atlassian.net/browse/WS-1177) y [WS-1257](https://bindpsp.atlassian.net/browse/WS-1257) (W 70.2, 2026-06-10).

**Bug corregido con hotfix dedicado — operaciones del filo de medianoche fuera del archivo diario** (WS-1074, EM-546): una operación creada a las **23:59:59** no aparecía en el archivo de operaciones PLD de ese día **ni en el del día siguiente**. Detectado conciliando archivo contra base (operación 210601115).

**Observaciones posteriores sin resolución técnica documentada en Jira** (W 70.2):
- **WS-1177** (SOPORTE, EM-589): archivos de **domicilios** y **actividades** de PLD no coincidían en cantidad de registros con el archivo de **clientes** del mismo día. Cerrado como Finalizada, sin detalle de causa/fix.
- **WS-1257** (PLD): el endpoint `POST /api/v1/lavado-clientes-cuentas` con `separarPorPsp: true` y `psp: 1` devolvía cuentas de **otros PSP**. Cerrado en estado "No aplica", sin comentarios — no queda claro si se determinó que no era un bug real.

**Cluster PLD de W69 (2026-04-29):**
- Criterios de fecha inconsistentes entre endpoints PLD (WS-702, reportado por Worldsys) — normalizados.
- Timeout del reporte de Operaciones PLD (WS-727) — se aumentó la tolerancia.

**Prehistoria del patrón — cluster PLD/reportes de W68 (2026-03-11):** `codigoActividadAfip` no numérico rompía el archivo completo (WS-358); IDs de operación duplicados en el archivo (WS-502); diferencias de cantidades en archivos de Cuentas y Operaciones (WS-605/606) y valor inválido que bloqueaba el archivo de Cuentas (WS-698); OOM en la generación de reportes (WS-597, solución de corto plazo, la de largo plazo quedó atada a un proyecto de reporte con "3NG").

📌 **Patrón a tener presente:** la generación de archivos PLD/reportes acumula **al menos 9 tickets entre marzo y junio 2026**, todos de conciliación archivo-vs-base, límites de corte u OOM — es un área estructuralmente frágil, no una serie de bugs aislados. Si Cumplimiento reporta inconsistencias similares a futuro, revisar el estado real de WS-1177/WS-1257 antes de asumir que están resueltos. Ver también [3_recursos/cumplimiento_normativo/reporteria_worldsys_bcra.md](../../cumplimiento_normativo/reporteria_worldsys_bcra.md).

## 5. Prehistoria W68 (2026-03-11) — confiabilidad de transferencias y comprobantes

> Tickets WS-397, WS-490, WS-514, WS-556, WS-284, WS-479, WS-561, WS-575, WS-674. Los problemas de consistencia comprobante↔operación que en mayo-junio 2026 derivaron en la saga de la sección 3 ya venían de antes:

- **Comprobante duplicado / comprobante sin operación** (WS-397, SOPORTE): en transferencias entrantes, ambas casuísticas. Primer uso del **message redelivery de MassTransit** — antecedente directo del mecanismo que WS-1027 (W 70.1) generalizó.
- **Transferencias salientes: comprobante creado pero operación falla** (WS-490): si el guardado de la operación fallaba después de crear el comprobante, el cliente recibía 500 con el dinero ya debitado. Fix: `cancellationToken` entre MS Operaciones→Comprobantes (Comprobantes aborta o genera devolución automática) + chequeo de conexión a DB antes de avanzar. Es el espejo "saliente" del bug crítico WS-1254 (sección 2).
- **Pagos QR cursados en el banco sin registro en BD Operaciones** (WS-514, SOPORTE, varias organizaciones en PROD).
- **State Monitor: timeout de 3h → 1h** (WS-556; despliegue efectivo hotfix **W 67.3 HF**, WS-558): tras un incidente (API Bank colgado un sábado a la noche), se bajó el tiempo para que las operaciones pasen antes a **Auditar** y Soporte pueda resolverlas a mano.
- **State Monitor: tratamiento especial del código TX019** (WS-284): si Api Bank responde `TX019` para una saliente y pasaron más de ~5 minutos, la operación pasa directo a **Rechazada** — antes se consultaba infinitamente en vano.
- **Infra de eventos**: WS-479 — EasyNet reemplaza MassTransit en el evento `ComprobanteCreado`; WS-561 — POC de colas Quorum sobre `ProcesarTransferenciaEntranteQueue`, precursor de la migración masiva a Quorum de W 70.1 (WS-917).
- **Contrato del GET /CuentaCorriente normalizado** (WS-575): PAGOQR responde `VendedorCuit`/`VendedorCbuCvu`/`VendedorNombre`; transferencias responden `CuitCuilContraparte`/`NombreContraparte`/`CvuCbuContraparte` — nunca `CompradorNombre`.
- **Menor** (WS-674): el campo `EmpresaTransaccional` guardaba comillas espurias cuando el nombre de la entidad terminaba en espacio.

## 6. Lanzamiento y estabilización (W65 → W66.x, nov-2025 → ene-2026)

La era fundacional del producto en Jira — mayormente estabilización post-lanzamiento.

- **El contrato actual de los webhooks de operaciones nace acá** (WS-37, W 65.1): se agregaron `comprobanteId`, `comprobanteDevolucionId`, `fechaCreacion` y `fechaActualizacion` a TODOS los webhooks de operaciones (los de impuestos/reciclado sumaron `comprobanteRelacionadoId`+`codigoTipoComprobante` en WS-34, W 65).
- **Cuentas nacían deshabilitadas y el PATCH no las habilitaba** (WS-94, W 65, reclamo Gallo/Banza).
- **Saldo no reflejado inmediatamente tras crear comprobante** (WS-83, W 65, reclamo Astropay).
- **Servicio de "auditar" parametrizable por BD** (WS-27, W 65): la parametría pasó a BD modificable por script (antes corría cada 8hs tomando 50 operaciones fijas).
- **Regla de manejo de excepciones en consumers** (WS-30, W 66): excepción de negocio → el flujo termina; excepción NO controlada → política de reintentos espaciados. Base conceptual de toda la saga de confiabilidad posterior.
- **Contrato de webhooks de transferencias internas** (WS-208 W66: la ENTRANTE informaba el `cuentaId` de origen en vez del de destino; WS-263 hotfix W66.1: tras un deploy desapareció `operacionIdRelacionada`) — las regresiones de contrato de webhooks son un patrón repetido.
- **QR**: pagos quedaban todos en INICIADO por problema de Api Bank (WS-168); error Coelsa `0440 OTROS PROBLEMAS` (WS-139); hotfix **W 66.2 HF** (WS-359): Coelsa empezó a exigir el campo `SUCURSAL` obligatorio y el QR quedó roto en STG — precursor del fix definitivo de W67 (WS-381, sección 7).
- **Operaciones colgadas en "A consultar" masivas** (hotfix **W 66.3 HF**, WS-351): resolución masiva + origen de la lógica TX019 formalizada en W68 (WS-284).
- **Duplicidad por pods paralelos** (WS-52, W66): devoluciones duplicadas porque el background service del State Monitor corre en varios pods — delay aleatorio (mismo patrón repetido en W67 con WS-374/375).
- **Impuestos**: liquidaciones que no se enviaban a SISCRI (WS-122, W66); hotfix **W 66.4 HF** (WS-415): alta manual masiva de todos los tipos de comprobante en SISCRI (el mapeo automático llegó recién con WS-462/WS-726); campo **`CTRL_SIRTAC`** (WS-169, W65.2).
- **Archivos fiscales IDYCB** (WS-257, W66): presentaciones al fisco, sin impacto en el flujo online.
- **Mejora estructural de creación de comprobantes** (WS-279, W66): reordenamiento/adelgazamiento del procesamiento, tocó todos los flujos que generan comprobantes.
- **Atributo `detalle` expuesto por error** (WS-56, W66): filtrado del contrato público.

## 7. Pagos QR, webhooks y performance (W67, 2026-01-27)

- **Origen histórico de los webhooks sin `comprobanteId`** (WS-135/136/137, detectados nov-2025): primera aparición del síntoma "operación/webhook sin comprobante" cuya causa de fondo se terminó de atacar recién en W 70.1→70.2.1 (sección 3).
- **Pago QR con 500 al cliente pero que luego se acredita** (WS-296, SOPORTE, cliente BSF): `NullReferenceException` respondía 500, el cliente devolvía la plata a su usuario, y el pago se acreditaba igual (doble egreso). Espejo temprano del patrón del bug crítico WS-1254 (sección 2).
- **Cobro QR sin sucursal** (WS-381): cuando el vendedor es CVU, `banco`/`sucursal` van con `"000"`/`"0000"` a Coelsa.
- **QR rechazado por Coelsa 7171 "ADQUIRIENTE DENIEGA OPERACION"** (WS-207, Maxiconsumo/Tienda Júbilo): código sumado al repertorio conocido.
- **`redId` unificado en las consultas** (WS-264): GET /Movimientos y /CuentaCorriente agregan `datosOperacion.redId`.
- **Webhooks de impuestos normalizados** (WS-268 camelCase total; WS-295 schema sin campos espurios de Recycle).
- **Performance de creación de transferencias** (WS-303): validación de `idExterno` con índice compuesto + `EXISTS`.
- **Primera aplicación de EasyNet** (WS-280): nueva librería de RabbitMQ aplicada primero a MS Comprobantes — inicio de la línea EasyNet que siguió en W68 (WS-479) y W70 (WS-616).

## 8. Ardid en pagos QR, trazabilidad y confiabilidad (W69, 2026-04-29)

- **Los pagos QR de Wallet pasan por Ardid** (WS-549/550/551): cada Pago QR se analiza en Ardid antes de ir a Coelsa, vía `/Analyze` con `scope=4` (reservado para Pagos QR) y `transferType=2`, habilitable por organización. Si el cliente no existe en Ardid, el pago continúa normal.
- **Trazabilidad del Pago QR ante fallas de Coelsa** (WS-757): desde W69 el `QrIdTrx` se persiste en `OperacionesPagosQR` **antes** de invocar a Coelsa (antes, si Coelsa fallaba, no quedaba registrado en ningún lado).
- **Contracargos de Pagos QR acreditados pero sin registrar en Operaciones** (WS-777, SOPORTE): errores en MS SharedDebin — fix: migración a EasyNet + filtro temprano del payload.
- **State Monitor: 1h → 3h (de nuevo)** (WS-1023): a la inversa de W68 (3h→1h, WS-556), para el pasaje a producción — el valor es un dial operativo que se mueve según contexto.
- **Transferencia pull: exploit de fondos sin respaldo corregido** (WS-736, bug crítico, precedente directo del incidente de fraude de marzo 2026 — ver [transferencias_pull.md §5](transferencias_pull.md)): una pull débito fallida por saldo insuficiente generaba un comprobante de crédito sin débito exitoso previo.

## 9. Herramientas internas de administración/Soporte (W70.1, 2026-06-03)

> WS-978, WS-985, WS-953. Ninguno expuesto en APIM — uso exclusivo interno.

- **Inhabilitación masiva de cuentas** (WS-978): `POST /ProcesarCuentas` en MS Cuentas — array de `{id, habilitar, motivo}`, procesado async, con auditoría en `CuentasAuditoria`.
- **Alta de tipo de comprobante sin organización** (WS-985): `POST /TipoComprobanteSinOrganizacion` en MS Comprobantes con `IdOrganizacion=NULL` — no puede eliminarse ni modificarse una vez creado.
- **ABM de PSPs** (WS-953): `POST`/`PUT`/`DELETE /api/v1/PSP` en MS Cuentas — reemplaza scripts de base de datos.

**Precursor de W69 — gestión de bajas de cuenta/CVU sin Fintexa:** "Revertir eliminación de Cuenta" (WS-771) — nuevo POST que valida que la cuenta esté efectivamente eliminada y revierte los campos, con tabla de auditoría `CuentasAuditoria` (campo `Motivo` obligatorio). ⚠️ Nota post-cierre: en una revisión se reportó que no se desarrolló todo lo pedido (fecha y motivo por cada tipo de evento) — quedó anotado para re-verificar.

## Ver también
- [debin_y_fondeo.md](debin_y_fondeo.md) — contracargos de DEBIN recurrente, mismo dominio de confiabilidad.
- [cuenta_remunerada_fci.md](cuenta_remunerada_fci.md) — validaciones de cuenta comitente.
- [3_recursos/arquitectura_sistema/idempotencia_de_plataforma.md](../../arquitectura_sistema/idempotencia_de_plataforma.md) — patrón transversal relacionado.

---
*Última actualización: 2026-08-12 — Consolidado desde `detalle_productos/wallet/otros_manuales.md §2, §2.1, §4.1, §8, §8.0, §8.1, §8.4-8.7, §9, §9.1` (reestructuración PARA en cascada). Contenido sin cambios de fondo, reorganizado bajo un único tema.*

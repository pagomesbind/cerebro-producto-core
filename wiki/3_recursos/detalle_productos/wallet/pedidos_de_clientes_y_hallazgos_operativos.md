# Pedidos de Clientes y Hallazgos Operativos Históricos — Wallet

> Estado: mezcla de en producción y pendientes (marcado por ítem). Consolidado en la reestructuración PARA en cascada (2026-08-12) desde 3 archivos-cola de `detalle_productos/transversal/` (`pedidos_puntuales_de_clientes.md`, `dolores_soporte_y_administracion.md`, `mejoras_e_iniciativas_tecnicas.md`) que mezclaban pedidos de varios productos en un solo archivo.

## Pedidos puntuales por cliente

- **Banza**: endpoint GET de webhooks configurados (Pendiente).
- **PLD/Worldsys**: envío de interfaz de actividad de cuentas Wallet — ver [3_recursos/cumplimiento_normativo/reporteria_worldsys_bcra.md](../../cumplimiento_normativo/reporteria_worldsys_bcra.md) (en producción).
- **GST (Hipódromo)**, pedido en aprobación al 2026-08-18 — dos mejoras sobre consultas existentes de Wallet, cada una estimada en ~1 MD (jornada) de desarrollo: (1) `GET cuenta corriente` — agregar filtro por **IDSA**; (2) `GET movimientos` — traer **comprobantes relacionados que no estén asociados a una operación**, pensado especialmente para comprobantes de impuestos. Ambas ya estimadas por el equipo; falta la reunión de aprobación final con Emma Vignoles antes de avanzar el desarrollo. Fuente: minutas de Gemini de "Producto" y "Productos - Weekly Seguimiento" (2026-08-18).

### COTO — diff confirmado entre `GET Movimientos` (legacy) y `GET /CuentaCorriente` (vigente)

> Estado: documentación desactualizada / en disputa — hay una discrepancia confirmada entre lo documentado en el portal público y lo que la API devuelve en la práctica.
>
> Nota de ruteo: esta nota compara el payload real de un endpoint de la API pública de Wallet contra su propia documentación (`apis_expuestas/`, dominio exclusivo de `/sync_web`) — se integra acá, no en `apis_expuestas/`, porque ese directorio no admite ediciones fuera de esa skill.

COTO fue transicionado del endpoint legacy `GET Movimientos` (ya no existe en el portal público — `https://psp.bind.com.ar/developers/apis/movimientos` redirige a home) al endpoint vigente `GET /CuentaCorriente` (`walletentidad-operaciones/v1/api/v1.201/CuentaCorriente`). El usuario aportó dos payloads reales para el **mismo `ComprobanteId` (14648633)**, uno de cada endpoint, lo que permitió un diff 1:1 confirmado (no inferido).

**Nivel comprobante (raíz de `movimientos[]`):** sin pérdida de datos, solo renombres — `tipoComprobanteId`→`idTipoComprobante`, `cuentaId`→`idCuenta`. El resto de los campos (`idComprobante`, `descripcionTipoComprobante`, `fecha`, `importe`, `saldo`, `signo`, `referencia`) se mantiene igual.

**Nivel operación (`operacion{}` en Movimientos vs. `datosOperacion{}` en CuentaCorriente) — ausentes del payload real pese a estar documentados como parte del esquema en el portal público:**
- `fechaCreacion` (era `FechaCreacion` en Movimientos, con valor real no nulo).
- `fechaActualización` (era `FechaActualizacion` en Movimientos, con valor real no nulo).
- `comprobanteDevolucionId` (era `null` en Movimientos para este caso, pero la key ni aparece en CuentaCorriente).

Esto es más que un renombre: es una discrepancia entre lo que documenta `https://psp.bind.com.ar/developers/apis/consultarmovimientoscuentacorriente` (que sí lista estos 3 campos como parte de `datosOperacion`) y lo que la API devuelve en la práctica. `importeOperacion` está ausente por diseño (nunca documentado para `datosOperacion`).

**Array `detalle` (Movimientos) vs. `detalles` (CuentaCorriente) — mismo shape clave-valor, contenido distinto:**

| Campo en `Movimientos.detalle` | Presente en `CuentaCorriente.detalles` |
|---|---|
| `CuitCuilContraparte` / `NombreContraparte` / `CvuCbuContraparte` | Sí, igual |
| `CoelsaId` | Sí, pero renombrado a `IdTxProcesador` — confirmado mismo valor exacto |
| `MotivoRechazo` | No — ausente, sin equivalente |
| `EstadoExterno` (`"COMPLETED"`/`"FAILED"`/etc.) | No — ausente; lo más cercano es `EstadoOperacionId`/`ProcesoCoelsa`, que no es lo mismo |

`CuentaCorriente.detalles` agrega campos nuevos que `Movimientos.detalle` no tenía: `AliasContraparte`, `CodigoBancoContraparte`, `ComprobanteId`, `EstadoOperacionId`, `IdExterno`, `TipoOperacionCodigo`, `ProcesoCoelsa`.

**`idComprobanteRelacionado` — el problema principal reportado por COTO:** el ejemplo comparado no era un caso de devolución, así que no lo muestra en ninguno de los dos endpoints — pero el usuario confirmó directamente que este es el problema principal que motivó el análisis: `GET Movimientos` sí lo traía (a nivel raíz de cada comprobante) y `GET /CuentaCorriente` no.

**Recomendación, en orden de prioridad si se decide extender `/CuentaCorriente`:** (1) `idComprobanteRelacionado` a nivel raíz de `movimientos[]`; (2) `MotivoRechazo` dentro de `datosOperacion.detalles[]`; (3) `EstadoExterno` dentro de `datosOperacion.detalles[]`; (4) `importeOperacion` dentro de `datosOperacion`; (5) `fechaCreacion`/`fechaActualización`/`comprobanteDevolucionId` en `datosOperacion` — este último punto es reproducir un bug contra la documentación existente, no pedir desarrollo nuevo.

> Fuente: charla directa con el usuario sobre migración de COTO de GET Movimientos a GET /CuentaCorriente; comparación 1:1 con payloads reales para el mismo ComprobanteId (14648633), contrastados contra la documentación pública (2026-08-25).

### Deuda técnica — trazabilidad de transferencias internas salientes (discusión 2026-08-18)

> Fuente: minutas de Gemini de "Producto" y "Productos - Weekly Seguimiento" (2026-08-18), surgida al analizar el pedido de GST de arriba.

El equipo identificó que hoy no hay forma de relacionar una transferencia interna saliente con la entrante que origina del otro lado. Se descartó la opción de obligar un ID externo propagado (podría chocar con la creación de una operación externa hecha directamente por el cliente con ese mismo ID). Se acordó, como mínimo, implementar el campo de **"comprobante relacionado"** (comprobante ↔ comprobante) para sostener la trazabilidad — deuda técnica reconocida, no bloqueante hoy porque el campo de referencia libre (que ya se completa desde la app) resuelve el caso de uso de forma parcial.

## Cluster de confiabilidad — Astropay (cliente de mayor volumen)

Conjunto de Spikes y mejoras sobre el mismo dolor: transferencias entrantes de Astropay que tardaban demasiado en notificarse a la organización, o cuya operación existía pero sin comprobante asociado:
- Gestión de colas y políticas ante errores para transferencias entrantes sin comprobante.
- Mejoras al endpoint de conciliar: aceptar una lista de ids (en vez de uno a uno) e indicar explícitamente si se quiere que dispare notificación — ambas para poder re-conciliar en lote sin generar notificaciones duplicadas.
- Limpieza de la base de datos `NotificacionesWallet` (acumulación de registros).
- Operaciones que quedaban en estado "a auditar" (acreditadas o fallidas) durante mucho tiempo sin revisión automática — se agregó una consulta que recorre todas las operaciones en ese estado.
- **Endpoint dedicado de conciliación optimizado** (paginado grande, campos mínimos) — construido específicamente para el volumen de Astropay.

Ver también `detalle_productos/wallet/clientes_white_label.md` (Astropay como cliente de mayor volumen relevado).

## Resiliencia del backend de eventos (comprobantes/operaciones)

Cluster de manejo de excepciones y contingencia para operaciones que podían quedar sin su comprobante asociado en el flujo event-driven (consumers de Cuenta/Comprobantes/Operaciones):
- Manejo de excepciones centralizado en los consumers.
- Contingencia para operaciones sin comprobante, específicamente en transferencias salientes (mismo patrón de bug — WS-490 — que la mecánica equivalente del Agente de Cobros y Pagos, ver [agente_cobros_y_pagos/transferencia_saliente_mecanica.md](../agente_cobros_y_pagos/transferencia_saliente_mecanica.md)).
- API "Comprobantes Espejo" dedicada a generación masiva de comprobantes (mecanismo de reconciliación/backfill).
- Delay aleatorio (random) en un background service para evitar la duplicidad de devoluciones de transferencias — mitigación de una condición de carrera conocida más que un fix de raíz.

## Operación de Wallet (pedidos de Soporte)

- No permitir transferir si `monto + costo > saldo` (validación de saldo insuficiente considerando el costo de la operación, no solo el monto).
- Guardar el saldo del día de la cuenta recaudadora por organización.
- Las cuadraturas (conciliación contable) no deberían generarse si no se encuentra el extracto correspondiente.
- **Bug de segmentación cruzada**: las cuentas de **TIN** se daban de alta en el calculador de costos con el segmento de **SUR FINANZAS** (mezcla de configuración entre dos clientes white-label distintos) — ver [ecosistema_wallet_adquirencia/sur_finanzas_multi_comercio.md](../ecosistema_wallet_adquirencia/sur_finanzas_multi_comercio.md).

### Bugs y pedidos operativos — tramo W71 (releaseDate 2026-07-15 a 2026-07-23)

> Fuente: Jira bindpsp.atlassian.net, versión W 71 (publicada 2026-07-15) y W 71.2 FIX (tickets WS-1389/WS-1394/WS-1395).

- **Cluster "eliminar cuenta debe deshabilitar"** ([WS-1077](https://bindpsp.atlassian.net/browse/WS-1077), [WS-1078](https://bindpsp.atlassian.net/browse/WS-1078), W 71): los endpoints de eliminar cuenta/eliminar cuenta+CVU no deshabilitaban la cuenta al mismo tiempo, dejando cuentas eliminadas con `habilitado = 1`. Fix en dos partes: (1) WS-1078, que la eliminación deshabilite siempre; (2) WS-1077, que el endpoint de reactivación deje de exigir `habilitado = 0` como precondición (para poder reactivar las cuentas ya eliminadas antes del fix, que quedaron con `habilitado = 1`). **Regresión detectada después** ([WS-1324](https://bindpsp.atlassian.net/browse/WS-1324), mismo release W 71): con el fix ya aplicado, el ciclo baja→intento de habilitar (dice "no existe")→intento de reactivar seguía fallando con "La cuenta ya está habilitada" pese a que en la base la cuenta seguía dada de baja y deshabilitada — bug de inconsistencia entre la respuesta del endpoint y el estado real en base, sin causa raíz documentada en el ticket.
- **Duplicidad de comprobantes de Cobro QR interoperable** ([WS-1292](https://bindpsp.atlassian.net/browse/WS-1292), W 71): cuando Aceptador invoca a Wallet más de una vez en un lapso muy corto para el mismo `IdExterno`, Wallet no llega a ejecutar a tiempo la validación de duplicidad y se generan comprobantes duplicados (Tipo Comprobante 393). Propuesta técnica: constraint compuesto `IdExterno + IdOrganizacion` (solo cuando `IdExterno` no es null), con paso previo de limpieza de duplicados existentes; se advierte posible impacto en performance de INSERT a monitorear.
- **TX019 (transferencia no encontrada) en estado "A consultar"** ([WS-1249](https://bindpsp.atlassian.net/browse/WS-1249), W 71): si el StateMonitor consulta el estado externo en API Bank de una transferencia saliente y da `TX019`, y ya pasaron más de 5 minutos desde la primera consulta, ahora se la pasa directo a **Rechazada** (con el motivo que indique API Bank) en vez de seguir reintentando indefinidamente. Antes de los 5 minutos sigue el comportamiento normal de reintento.
- **Validación faltante al dar de alta un PSP por Swagger** ([WS-1232](https://bindpsp.atlassian.net/browse/WS-1232), "Con defecto" — quedó sin cerrar del todo): no se valida cantidad de dígitos de `CoelsaId` (debe ser 3) ni de `BcraId` (4-5 dígitos); tampoco se valida que `Nombre` no vaya vacío, que `Cuit` tenga formato/11 dígitos numéricos, ni que se envíe `Owner`.
- **Consulta de cuenta por CBU/CVU/alias no devuelve cotitulares** ([WS-1300](https://bindpsp.atlassian.net/browse/WS-1300), W 71): el endpoint `GET .../CuentaCVUByCbuCvuOrAlias` solo devolvía el primer titular. Nueva propuesta: agregar un array `cotitulares[]` con `cuitCuil`/`nombre` de cada cotitular (null si no hay), manteniendo retrocompatibilidad — los campos de primer nivel (`cuitCuil`, `nombre`, `nombreCVU`) siguen respondiendo al primer titular.
- **Crear/consultar comprobantes por `CodigoComprobante` además de `IdTipoComprobante`** ([WS-1044](https://bindpsp.atlassian.net/browse/WS-1044), W 71): pedido recurrente de clientes por la disparidad de IDs de TipoComprobante entre STG y PRD en comprobantes fijos cross-organización (ej. impuestos). Se agrega la opción de usar `Codigo` en `GET ComprobantesByFilters`, `POST ComprobantesByCuenta` y `POST Comprobante`, con validación de unicidad (no ambos, no ninguno) y existencia del código para la organización; en creación por lote mixta (algunos por Id, otros por Código), si algún comprobante no cumple validación se rechaza con 422 y no se crea ninguno del lote.
- **Pago QR quedando en "A Consultar"/"Auditar"** ([WS-1050](https://bindpsp.atlassian.net/browse/WS-1050), W 71): el método `CreatePagoQr` del StateMonitor intentaba leer un objeto `ErrorDtoResponse` inexistente cuando la respuesta no traía ningún objeto (dejaba la operación en estado 4 "A Consultar"); y `ValidarDatosPagoQrResponse` no resolvía el estado 5 "Auditar" cuando `Vendedor.CuentaVirtual` no tenía datos — se corrige para que tome `Vendedor.Cuit`/`Vendedor.Cuenta.CBU` directamente en ese caso.
- **Transferencia saliente devuelve 500 pero queda Aprobada en base — cliente La Virginia** ([WS-1206](https://bindpsp.atlassian.net/browse/WS-1206), W 71): transferencia interna saliente respondió `500 Internal Server Error` ("Invalid URI: The URI is empty") pero la operación se aprobó igual en base — inconsistencia entre la respuesta al cliente y el estado real, mismo patrón que otros incidentes de confiabilidad ya documentados (ver [historial_confiabilidad_transferencias_y_comprobantes.md](historial_confiabilidad_transferencias_y_comprobantes.md)).
- **Reportes de Movimientos con `CodigoPSP = 0`** ([WS-1395](https://bindpsp.atlassian.net/browse/WS-1395), W 71.2 FIX): un cambio previo en la consulta de PSPs reemplazó el atributo de respuesta `Codigo` por `CoelsaId`; el MS Reportes seguía esperando `Codigo`, y al no encontrarlo asignaba 0 — corregido para que MS Reportes lea el campo correcto.
- **Transferencias entrantes sin datos de contraparte en conciliación** ([WS-1389](https://bindpsp.atlassian.net/browse/WS-1389), W 71.2 FIX): operaciones con los campos `cuit`/`cuil` y `cbu`/`cvu` de contraparte vacíos, reportado por cliente (org 56) sobre 3 operaciones puntuales — sin causa raíz documentada en el ticket, solo el reporte y su resolución puntual.
- **PagosQR en estado "Auditar" sin poder resolverse** ([WS-1394](https://bindpsp.atlassian.net/browse/WS-1394), W 71.2 FIX): dos problemas reportados por Soporte: (1) operaciones sin `IdCoelsa` que no se pueden resolver (reincidencia de un reclamo anterior); (2) las que sí tienen `IdCoelsa` tiran error al intentar resolverlas por Swagger. Sin detalle técnico de la resolución en el ticket (secciones de PR quedaron sin completar).
- **Ruido — sin contenido de producto:** WS-614 (ticket con descripción corrupta/vacía — parece un prompt de IA pegado por error en vez del contenido real; título sugiere validación de estado en ejecución de pasos de FCI, Epic WS-1/PRD-103 ya finalizada, sin info recuperable).

### Bugs y pedidos operativos — tramo W72 (publicada 2026-08-18)

> Fuente: Jira bindpsp.atlassian.net, versión W 72, tickets WS-1437, WS-1287.

- **Eliminar CVU deshabilitaba la cuenta como efecto colateral** ([WS-1437](https://bindpsp.atlassian.net/browse/WS-1437)): bug espejo del cluster "eliminar cuenta debe deshabilitar" (WS-1077/WS-1078, W71, arriba) — pero del lado opuesto. El endpoint `DELETE /api/v1/CVU/{id}` (eliminar **solo** el CVU, sin tocar la cuenta) estaba deshabilitando la cuenta como efecto colateral no deseado; solo `DELETE Cuenta` y `DELETE CuentaYCVU` deben deshabilitar la cuenta. **Causa:** en `CuentaCVU.DeleteCuentaCVU` se asignaba `cuentaCVU.Cuenta.Habilitado = false` (la entidad hija CVU mutando el agregado padre Cuenta) y `DeleteCuentaCVUCommandHandler` persistía con `_cuentaRepository.UpdateAsync(cuentaCVU.Cuenta)` (EF marcaba toda la fila de `Cuentas` como modificada). **Fix:** se remueve esa mutación cruzada. Nicolás Colón pidió explícitamente que el ticket pasara como hotfix (2026-07-28). Sin cambio de status HTTP; el cambio es solo de efecto en base. Las cuentas ya dañadas antes del fix **no se corrigen** con este PR (no hay migración de datos retroactiva). Validado por Andrea Orsini el 2026-08-14 (CVU activo→DELETE CVU→cuenta sigue habilitada; DeleteCuentaYCVU sigue inhabilitando como antes).
- **`GET OperacionByIdExterno` amplía la ventana de búsqueda de 3 a 180 días** ([WS-1287](https://bindpsp.atlassian.net/browse/WS-1287), Epic WS-518): pedido de negocio — `GET /api/v1/OperacionByIdExterno/{IdExterno}` solo encontraba operaciones de hasta 3 días de antigüedad, insuficiente para que una organización conozca el estado real de una operación más vieja. **Cambio de comportamiento (relevante para Soporte/integraciones): antes de esta versión, una operación entre 3 y 180 días devolvía 404 — ahora devuelve 200 con datos.** Ventana ampliada a 180 días, configurable en caliente vía la Especificación de Wallet `Operaciones/DIAS_CONSULTA_ID_EXTERNO` (sin deploy; si no existe o no es parseable, cae a `appsettings.DíasConsultaIdExterno = 180`). El mensaje 404 ahora incluye la cantidad de días consultados (`"No se encontró la operación para el id externo: {IdExterno}, ó es anterior a los {N} días"`), y el logging distingue `Warning` (existe pero excede la ventana) de `Information` (no existe). Mejora de performance acompañante: nuevo índice `IX_Operaciones_IdExterno_OrganizacionId` — **prerequisito externo gestionado por DBA, no incluido en este PR de código**; el valor de 180 días no debe activarse operativamente hasta que DBA confirme índice + especificación en cada ambiente (el código puede desplegarse antes, pero sin efecto real hasta ese paso). Se corrigió además `DateTime.Now` → `DateTimeOffset.Now` (alineado con `FechaCreacion`) y se agregó cache de 15 minutos a la lectura de la especificación. Alcance del PR: solo `Wallet.Operaciones.Queries`.

## Ver también
- [3_recursos/arquitectura_sistema/idempotencia_de_plataforma.md](../../arquitectura_sistema/idempotencia_de_plataforma.md) — patrón transversal de falta de idempotencia centralizada.

---
*Fuente: Epics Notion "Dolores de clientes", "Dolores de Soporte y administración" y "Mejoras e Iniciativas Técnicas" — ingesta 2026-07-06.*
*Última actualización: 2026-08-25/26 — `/context_merge`: nueva sección "Bugs y pedidos operativos — tramo W72" (WS-1437, WS-1287) y nota comparativa COTO (`GET Movimientos` vs. `GET /CuentaCorriente`).*
*Última actualización anterior: 2026-08-15/18 — `/sync_releases` + `/sync_meetings`: nueva sección "Bugs y pedidos operativos — tramo W71", pedido de GST y deuda técnica de comprobante relacionado.*
*Última actualización anterior: 2026-08-12 — Creado en la reestructuración PARA en cascada, consolidando las secciones de Wallet de 3 archivos-cola de `detalle_productos/transversal/`.*

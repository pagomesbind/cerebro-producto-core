# Pedidos de Clientes y Hallazgos Operativos Históricos — Wallet

> Estado: mezcla de en producción y pendientes (marcado por ítem). Consolidado en la reestructuración PARA en cascada (2026-08-12) desde 3 archivos-cola de `detalle_productos/transversal/` (`pedidos_puntuales_de_clientes.md`, `dolores_soporte_y_administracion.md`, `mejoras_e_iniciativas_tecnicas.md`) que mezclaban pedidos de varios productos en un solo archivo.

## Pedidos puntuales por cliente

- **Banza**: endpoint GET de webhooks configurados (Pendiente).
- **PLD/Worldsys**: envío de interfaz de actividad de cuentas Wallet — ver [3_recursos/cumplimiento_normativo/reporteria_worldsys_bcra.md](../../cumplimiento_normativo/reporteria_worldsys_bcra.md) (en producción).
- **GST (Hipódromo)**, pedido en aprobación al 2026-08-18 — dos mejoras sobre consultas existentes de Wallet, cada una estimada en ~1 MD (jornada) de desarrollo: (1) `GET cuenta corriente` — agregar filtro por **IDSA**; (2) `GET movimientos` — traer **comprobantes relacionados que no estén asociados a una operación**, pensado especialmente para comprobantes de impuestos. Ambas ya estimadas por el equipo; falta la reunión de aprobación final con Emma Vignoles antes de avanzar el desarrollo. Fuente: minutas de Gemini de "Producto" y "Productos - Weekly Seguimiento" (2026-08-18).

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

## Ver también
- [3_recursos/arquitectura_sistema/idempotencia_de_plataforma.md](../../arquitectura_sistema/idempotencia_de_plataforma.md) — patrón transversal de falta de idempotencia centralizada.

---
*Fuente: Epics Notion "Dolores de clientes", "Dolores de Soporte y administración" y "Mejoras e Iniciativas Técnicas" — ingesta 2026-07-06.*
*Última actualización: 2026-08-15/18 — `/sync_releases` + `/sync_meetings`: nueva sección "Bugs y pedidos operativos — tramo W71", pedido de GST y deuda técnica de comprobante relacionado.*
*Última actualización anterior: 2026-08-12 — Creado en la reestructuración PARA en cascada, consolidando las secciones de Wallet de 3 archivos-cola de `detalle_productos/transversal/`.*

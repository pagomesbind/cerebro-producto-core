# Devoluciones y Contracargos — Botón Simple y QR

> Estado: en producción. Reubicado desde `detalle_productos/adquirencia/liquidaciones_y_devoluciones.md` en la reestructuración PARA en cascada (2026-08-12) — el producto **Liquidador** (para terceros como Traditum/Newpay PMC) se extrajo a [liquidador_terceros_traditum_newpay.md](liquidador_terceros_traditum_newpay.md) por ser un tema distinto.
>
> Fuente: `wiki/3_recursos/conocimiento_interno/manual_para_configuraciones/` y `wiki/3_recursos/conocimiento_interno/documentacion_para_clientes/` (ingesta Notion). Contenido sustantivo transcripto tal cual (curls, IDs reales, pasos) — sin redactar.
>
> Ver [mecanica_qr_coelsa.md](mecanica_qr_coelsa.md#parte-4--interchange-y-comisiones-de-qr--especificación-técnica-coelsa) para el mecanismo de liquidación de comisiones de Interchange en Coelsa (distinto del proceso de liquidación al comercio documentado acá).

---

## 0. Desconocimientos de tarjeta (Botón Simple) — contracargo total de uso interno

> Fuente: Notion histórico, Epic **"Desconocimientos de tarjeta"** (Dolor). No confundir con las devoluciones/contracargos estándar documentados abajo — un "desconocimiento" es el caso donde el titular de la tarjeta niega haber hecho la compra.

- **Endpoint de uso exclusivamente interno** (Operaciones Bind PSP, vía Swagger o luego desde el Admin) — nunca expuesto a las entidades/comercios. Marca una transacción de Botón Simple como desconocimiento por transacción.
- Efecto: crea un **contracargo de tipo "desconocimiento"** (total, no parcial — distinto de los contracargos tipo "devolución" ya soportados), pasa la transacción a estado `DEVUELTA`, y registra el timestamp del desconocimiento.
- **Se liquida exactamente igual que una devolución** (mismo criterio de impuestos, archivos y PDF de comercio) — resta en la liquidación al comercio en el siguiente día hábil a la fecha de desconocimiento. Es decir: técnicamente reutiliza todo el motor de devoluciones existente, solo cambia el tipo de contracargo y quién puede dispararlo.

**Implementación en curso (agosto 2026, PRD-146/AD-1360):** > Fuente: Mail "Análisis COBRO: Lun, 10 de ago de 2026" — malzogaray@bind.com.ar, 2026-08-10.
- **Código `004`** identifica el desconocimiento como tipo de contracargo diferenciado de la devolución en el archivo/registro de liquidación — resuelve un bug de importes en cero que ocurría al no distinguirlos.
- El PDF de liquidación suma un apartado propio "Detalle de desconocimientos" + columna nueva en el resumen, sin alterar el total liquidado.
- **No existe el concepto de "desconocimiento parcial"**: cualquier desconocimiento se aplica sobre el remanente total de la transacción.
- **Estrategia de emisión tolerante a fallos:** el PDF de liquidación se emite siempre, incluso con inconsistencias de datos — se prioriza la disponibilidad del comprobante sobre la consistencia (correcciones reactivas post-emisión).
- Detalle completo del seguimiento de este desarrollo en PRD-146 (Tratamiento de contracargos de tarjeta) — proyecto de Nicolás Colón, vive en su propio Cerebro desde 2026-08-13.

## 1. Documentación: devoluciones parciales

## Documentación: devoluciones parciales

> Alcance: informativo y apto para desarrollo. Dirigido específicamente al flujo QR.

### Objetivo
Explicar en general cómo utilizar la funcionalidad de contracargo (total y parcial) de la forma más óptima, aprovechando los nuevos endpoints y webhook.

### Webhook de evento tipo contracargo

Se envía la información de la Transacción actualizada junto a la del Contracargo que sufrió.

> Este endpoint/webhook se consume con credenciales de API del producto **WALLET**.

**Ejemplo de payload:**
```json
{
   "When":"2025-12-29T12:28:23.8012893Z",
   "Payload":{
      "TipoEvento":"CONTRACARGO",
      "TipoOrigen":"ENTIDAD",
      "IdentificadorOrigen":"EDNO",
      "TipoDestino":"ENTIDAD",
      "IdentificadorDestino":"EDNO",
      "DestinoPrincipal":"https://webhook.site/6abc4b11-ba9e-47d2-97fa-4ef97eb78ea4",
      "DestinoSecundario":"string",
      "FechaEmision":"2025-12-29T12:28:23.7292582+00:00",
      "IdMensaje":"69fe7d0e-777f-4099-9ae9-aff863efd233",
      "MensajePago":{
         "IdentificadorProcesador":"0WGRXJE27Z8GPDE97MYQL3",
         "IdentificadorTransaccion":"1322137",
         "IdentificadorOrdenVenta":"9OC3496963658029B00000623438000000153248ET9EDNOTOC1CB30B5AAC",
         "IdentificadorReferencia":"YY1218T0001322137O0000153248",
         "IdOrdenVentaQr":"153248",
         "TipoTransaccion":"Transferencia30",
         "RubroMovimiento":"PagoQrTransferencia30",
         "FechaNegocio":"2025-12-29T09:28:16.0162519-03:00",
         "FechaProceso":"2025-12-18T16:14:34.8220787+00:00",
         "FormaPago":"Transf30",
         "Moneda":"ARS",
         "ImporteBruto":640.0000000,
         "EstadoTransaccion":"DEVUELTA",
         "Retenciones":[],
         "Mcc":"0763",
         "Cpa":"M5525DAK",
         "Cuit":"30715472828",
         "CuentaVendedor":"0000531907879067229001",
         "IdentificadorVendedor":"CVU:0000531907879067229001WAL:20230621|CBU:3220001805007352560018",
         "IdentificadorPagador":"20959468568",
         "CuentaPagador":"0000532609180000170008",
         "CodigoComercio":"C22900",
         "CodigoSucursal":"S18799",
         "CodigoCaja":"B00000623438",
         "InformacionAdicionalPagador":[],
         "Entidad":"EDNO",
         "Psp":"531",
         "Procesador":"0WGRXJE27Z8GPDE97MYQL3",
         "InformacionAdicionalMensaje":[
            {"Descripcion":"motivoContracargo","Valor":""},
            {"Descripcion":"importe","Valor":"640.00"},
            {"Descripcion":"contracargoParcial","Valor":"False"},
            {"Descripcion":"idContracargo","Valor":"4535"},
            {"Descripcion":"fechaContracargo","Valor":"12/29/2025 09:24:41"},
            {"Descripcion":"estadoContracargo","Valor":"ACEPTADO"},
            {"Descripcion":"importeContracargo","Valor":"640.00"},
            {"Descripcion":"tipoContracargo","Valor":"contracargo"},
            {"Descripcion":"idDebin","Valor":"DLMORZP901Z8EEP2EGJ468"},
            {"Descripcion":"debinIdApiBank","Valor":"WZ0KV87941L0XX09PEYDX4"}
         ],
         "FechaLiquidacion":null,
         "FechaPago":null,
         "MotivoRechazo":null
      }
   },
   "Type":"CONTRACARGO"
}
```

### Request — atributos del webhook

| Atributo | Tipo | Descripción |
|---|---|---|
| `When` | datetime | Fecha y hora en que fue enviada la notificación (UTC+0). |
| `Payload` | object | Objeto con información de la notificación. |
| `TipoEvento` | string | Valor fijo: "CONTRACARGO". |
| `TipoOrigen` | string | Valor fijo: "ENTIDAD". |
| `IdentificadorOrigen` | string | Código unívoco de la Entidad a la que pertenece el comercio. |
| `TipoDestino` | string | Valor fijo: "ENTIDAD". |
| `IdentificadorDestino` | string | Código unívoco de la Entidad a la que pertenece el comercio. |
| `DestinoPrincipal` | string | URL del destino principal donde se envía el webhook. |
| `DestinoSecundario` | string | URL del destino secundario. |
| `FechaEmision` | datetime | Fecha y hora en que se envió la notificación (UTC+0). |
| `IdMensaje` | string | Id guid de la notificación. |
| `MensajePago` | object | Objeto con la información del pago. |
| `IdentificadorProcesador` | string | Id del contracargo enviado por el procesador del pago (Coelsa, Global Processing, Decidir, etc). Identificador usado para conciliar con procesadores. |
| `IdentificadorTransaccion` | string | Id único de la transacción para Bind PSP. |
| `IdentificadorOrdenVenta` | string | Identificador adicional según canal: para `Transferencia30` es el order id de la API Resolve en Coelsa; para `Botón simple` es el PaymentId (id del link de pago); para `CVUCollect` es el CVU en que se recibió el pago; para `MPOS` es el identificador correspondiente. |
| `IdentificadorReferencia` | string | Identificador adicional de referencia por canal. Para Botón Simple 2.0 es el `IdExterno` asignado. |
| `IdOrdenVentaQR` | string | Identificador de la orden de venta de QR. Para Botón Simple 2.0 es el `IdDeuda`. |
| `TipoTransaccion` | string | `Transferencia30` = QR; `BotonSimple` = Botón de pagos de cobro no presente; `CVUCollect` = Recaudación por transferencia a CVU; `MPOS` = Smartpos de cobro presente. |
| `RubroMovimiento` | string | Rubro interno de la transacción. |
| `FechaNegocio` | datetime | Fecha y hora en que el cliente realizó el pago (UTC-3). |
| `FechaProceso` | datetime | Fecha y hora en que se procesó el cobro (UTC-3). |
| `FormaPago` | string | `"Transf30"` = QR interoperable; `"TTDD"` = tarjeta débito; `"TTCC"` = tarjeta crédito; `"Transfer"` = recaudación por transferencia a CVU. |
| `Moneda` | string | Valor fijo: "ARS". |
| `ImporteBruto` | decimal | Importe bruto total de la transacción (lo que pagó el cliente final). |
| `EstadoTransaccion` | string | `"DEVUELTA"` = devolución exitosa (estado definitivo); `"ACREDITADO"` = devolución parcial o fallida. |
| `Retenciones` | string | Valor fijo: "None". |
| `Mcc` | string | Código de rubro según VISA MCC del comercio. |
| `Cpa` | string | Código postal argentino del comercio. |
| `Cuit` | string | CUIT del comercio. |
| `CuentaVendedor` | string | CVU del comercio. |
| `IdentificadorVendedor` | string | Concatena CVU, CBU e ID Wallet del comercio (aplica para pagos con QR). |
| `IdentificadorPagador` | string | CUIT del cliente pagador. |
| `CuentaPagador` | string | CBU/CVU del cliente pagador. |
| `CodigoComercio` / `CodigoSucursal` / `CodigoCaja` | string | Códigos identificadores en el sistema. |
| `InformacionAdicionalPagador` | object | Tuplas llave-valor con información adicional del pagador. |
| `Psp` | string | Código del PSP al que pertenece la Entidad. |
| `Procesador` | string | Id del pago enviado por el procesador. Identificador de conciliación. |
| `InformacionAdicionalMensaje` | object | Tuplas llave-valor: `motivoContracargo`, `importe` (monto devuelto hasta el momento), `contracargoParcial` (boolean), `idContracargo`, `fechaContracargo`, `estadoContracargo` (`"ACEPTADO"`/`"RECHAZADO"`), `importeContracargo`, `tipoContracargo` (fijo "contracargo"), `idDebin` (id del procesador para el contracargo), `debinIdApiBank` (id del procesador que debita al comercio y acredita en la cuenta recaudadora de BindPSP, solo comercios con Split). |
| `Type` | string | `"CONTRACARGO"` = webhook de devolución. |

### Consultar contracargo

> Este endpoint se consume con credenciales de API del producto **COBRO**.

**Endpoint:**

| Ambiente | Método | URL |
|---|---|---|
| STAGING | GET | `https://gw-staging-qrbind.epays.services/bindentidad-transaccionquery-v2/v2/api/v1/contracargos/{{Id}}` |
| PRODUCCIÓN | GET | (no documentada en la fuente) |

**Request:** `Id` (int, REQUERIDO) — al final de la URL, id del contracargo a consultar.

```json
curl --location 'https://gw-staging-qrbind.epays.services/bindentidad-transaccionquery-v2/v2/api/v1/contracargos/3226' \
--header 'Cache-Control: no-cache' \
--header 'Authorization: Bearer {{access_token}}'
```

**Response:**

| Atributo | Tipo | Descripción |
|---|---|---|
| `id` | int | Id del Contracargo. |
| `transaccionId` | int | Id de la Transacción contracargada relacionada. |
| `fechaNegocioOrigen` | string | Fecha y hora en que se realizó el Contracargo. |
| `importeContracargo` | decimal | Monto del Contracargo. |
| `motivoContracargo` | string | Razón por la cual se realizó el Contracargo. |
| `importeTransaccion` | decimal | Monto total original de la Transacción. |
| `parcial` | boolean | Indica si el Contracargo se hizo por el monto total o parcial respecto a la Transacción original o su restante (más de un contracargo parcial). |
| `tipo` | string | Valor fijo: "contracargo". |
| `estado` | string | `"PENDIENTE"`, `"APROBADO"`, `"RECHAZADO"`. |
| `motivoRechazo` | string | Razón por la cual el Contracargo falló, si `estado` = "RECHAZADO". |
| `vendedorCuit` | string | CUIT del Comercio que recibió la Transacción. |
| `vendedorCbu` | string | CBU/CVU del Comercio que recibió la Transacción. |
| `idDebin` | string | Id Coelsa con el que se realizó la devolución final de cara al cliente pagador. |
| `debinIdApiBank` | string | Id Coelsa (Debin) con el cual se debitan los fondos al Comercio y se acreditan en la cuenta recaudadora de BindPSP (exclusivo para QR Split). |
| `usuario` | string | Usuario que realizó la devolución. |

**Ejemplo de response:**
```json
{
    "id": 3226,
    "transaccionId": 1278414,
    "fechaNegocioOrigen": "2025-10-08T15:51:39.3633088",
    "importeContracargo": 6817.00,
    "motivoContracargo": "string",
    "importeTransaccion": 6817.00,
    "parcial": false,
    "tipo": "contracargo",
    "estado": "ACEPTADO",
    "motivoRechazo": null,
    "vendedorCuit": "20322678275",
    "vendedorCbu": "0000531908320067229030",
    "idDebin": "5L18MKX9RMQPMZK2O6WYV4",
    "debinIdApiBank": "4XJ8G7V95VZ7MG49EMPYR0",
    "usuario": "string"
}
```

---

## 2. AD V72 (despliegue 27/08/2026) — bug de tipo de operación en contracargos de devolución/anulación POS GP (AD-1020/AD-1579)

> Fuente: Mail "Análisis de riesgos AD V 72: Vie, 21 de ago de 2026" (threadId `1a025f5dceef64ef`), mensaje de Nicolás Colón, 2026-08-21.

Durante la reunión de análisis de riesgos de la versión AD V72 (pase a producción programado 27/08/2026, 21:00hs, ventana de 3hs), Nicolás Colón detectó un bug asociado al ticket **AD-1020/DAD-1673** ("Lógica de devolución/anulación POS GP — Guardar detalle en contracargo"), que forma parte de esa misma versión:

**El problema:** la tabla de Contracargos debe guardar siempre el tipo de operación como `Tipo="contracargo"` cuando se registra una devolución o anulación hecha desde POS con Global Processing — hoy ese campo queda con el valor genérico "Devolucion" en vez de distinguir explícitamente el tipo real de operación (anulación same-day vs. devolución de días previos).

**La corrección:** un ticket adicional, **AD-1579**, resuelve este comportamiento. Nico recomendó sumar AD-1579 a la misma versión AD V72, "mitigando así el riesgo que presenta el ticket original [AD-1020] por sí solo" — es decir, sin AD-1579, el ticket AD-1020 se desplegaría con este bug de tipo mal guardado.

**Contexto de la versión** (para ubicar el hallazgo): AD V72 modifica el esquema de devolución/anulación en POS distinguiendo transacciones del mismo día (anulación) de días anteriores (devolución), afecta ~20 microservicios (PaymentAcceptor.Deuda, Bff.CardPresent, PaymentAcceptor.CardOrchestrator, etc.) y aplica cambios estructurales a CVU Collect. El ticket AD-1020 fue marcado en la minuta de riesgo con semáforo 🔴🔴🔴 (riesgo alto) y acción "PRE-IMPLEMENTACIÓN: Avisar a clientes" — la tabla de contracargos que consumen los clientes en sus archivos podría verse afectada por el cambio de estructura.

## 3. Historial operativo — cliente COTO (rendiciones, BOTONLIQ)

> La historia completa de producto, cluster de bugs, y seguimiento operativo semana a semana sobre devoluciones/rendiciones para el cliente COTO (IDEA Jira PRD-81 y su evolución posterior: Botón LCK, BOTONLIQ, DAD-2171, DAD-2209) se extrajo a su propio archivo por umbral de tamaño (2026-08-27): ver [cliente_coto_historial_operativo.md](cliente_coto_historial_operativo.md).

---

> El producto **Liquidador** (API "Informar nueva Transacción para Liquidar", clientes Traditum y Newpay PMC) se extrajo a [liquidador_terceros_traditum_newpay.md](liquidador_terceros_traditum_newpay.md) por ser un tema distinto de las devoluciones/contracargos.

## Crear archivo BATCH DEVOLUCIÓN en STG

Swagger a utilizar: `http://10.210.1.32/swagger/index.html`

Endpoint: **`POST /api/v1/rendicion-contracargo`** — genera una rendición de las transacciones con contracargos (job).

**Parameters:** entidad y fecha.

## Discrepancia de saldo Coto vía API: no es error de cálculo, es corte bancario antes de medianoche — 2026-08-05

> Fuente: reunión "Migra PSP 164" (2026-08-05), minuta Gemini.

Investigando un reclamo de descuadre de saldo de la cuenta recaudadora de **Coto**, el equipo (Gonzalo Rivera, Maria Eugenia Vila, Pablo Gomes) determinó que **no hay error de cálculo** en el saldo que expone la API — el saldo total, consultado vía APIBank (`transactions`, filtrando por `collectorId`/`accountId`), siempre está bien calculado incluyendo todos los movimientos.

**Causa real:** el banco (PIBán) hace su corte de día antes de la medianoche (ej. 23:10-23:41). Un movimiento ocurrido, por ejemplo, a las 23:13 ya queda con **fecha de valor del día siguiente** en el extracto bancario, mientras que la API lo sigue devolviendo como el último movimiento del día en que realmente ocurrió. Resultado: al comparar el saldo que informa la cuadratura (basada en extractos con el corte del banco) contra una consulta directa a la API a otra hora, aparece un desfasaje que en realidad es de **atribución de fecha**, no de monto.

**Recomendación operativa:** para obtener el saldo "cerrado" de un día sin ambigüedad, consultar los movimientos de la cuenta vía API en un horario fijo de la mañana (ej. 11:00-11:30), después de que el corte bancario ya haya sido absorbido, en vez de consultar en horario nocturno cercano al corte. El equipo decidió llevar este hallazgo a Emma Vignoles para explicar la limitación técnica y evaluar si la reunión de cuadratura nocturna sigue siendo necesaria.

---
*Ver también: [botones_de_pago_y_qr.md](botones_de_pago_y_qr.md) para el manejo de órdenes de venta e identificadores externos, [mecanica_qr_coelsa.md](mecanica_qr_coelsa.md) para el mecanismo de comisiones/interchange que precede a la liquidación, [liquidador_terceros_traditum_newpay.md](liquidador_terceros_traditum_newpay.md) para el producto Liquidador (clientes que cobran por su cuenta), y [cliente_coto_historial_operativo.md](cliente_coto_historial_operativo.md) para el historial operativo detallado del cliente COTO.*
*Última actualización: 2026-08-27 — `/context_merge`: nueva §2 (bug de tipo de operación en contracargos POS GP, AD-1020/AD-1579, AD V72); §1.1 (historial operativo cliente COTO) extraída a [cliente_coto_historial_operativo.md](cliente_coto_historial_operativo.md) por umbral de tamaño de archivo.*
*Última actualización anterior: 2026-08-12 — Renombrado desde `liquidaciones_y_devoluciones.md`; sección del producto Liquidador extraída a archivo propio (reestructuración PARA en cascada).*

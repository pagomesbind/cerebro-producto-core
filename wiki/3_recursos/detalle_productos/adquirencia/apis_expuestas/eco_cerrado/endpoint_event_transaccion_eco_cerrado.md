# EVENT — Webhook: Aviso de Transacción Eco Cerrado

> Extraído el: 2026-06-30
> Fuente: https://psp.bind.com.ar/developers/apis/webhook-adecocerrado
> Producto: Adquirencia > Eco Cerrado

## Descripción

Se envía notificación HTTP POST cuando se crea una transacción de canal eco cerrado en estado "ACREDITADO". La entidad debe responder con código HTTP 200 para confirmar recepción; de lo contrario, el sistema reintentará el envío.

Requisito previo: "la entidad debe tener parametrizada la URL destino para el producto."

## ⚠️ Notas y Advertencias del Portal

> "No debe validarse la estructura del mensaje; Bind PSP puede agregar nuevos atributos opcionales sin previo aviso para funcionalidades futuras."

> Reintentos: Solo responder con HTTP 200 confirma recepción exitosa. Otros códigos activan esquema de reintentos automáticos.

## Campos del Payload

| Campo | Tipo | Descripción |
|-------|------|-------------|
| `When` | datetime | Fecha/hora de envío de notificación (UTC +0) |
| `Payload.TipoEvento` | string | Valor fijo: "PAGO" |
| `Payload.TipoOrigen` | string | Valor fijo: "ENTIDAD" |
| `Payload.IdentificadorOrigen` | string | Código único de la Entidad |
| `Payload.FechaEmision` | datetime | Fecha/hora de envío (UTC +0) |
| `Payload.IdMensaje` | string | ID guid de la notificación |
| `MensajePago.IdentificadorTransaccion` | string | ID de la transacción |
| `MensajePago.ImporteBruto` | decimal | Importe total pagado |
| `MensajePago.EstadoTransaccion` | string | "ACREDITADO" o "RECHAZADA" |
| `MensajePago.FormaPago` | string | "SALDO_VIRTUAL" |
| `MensajePago.Moneda` | string | "ARS" (Pesos argentinos) |
| `MensajePago.FechaNegocio` | datetime | Fecha/hora del pago (UTC -3) |
| `MensajePago.IdentificadorPagador` | string | CUIT del cliente |
| `MensajePago.CodigoComercio` | string | Identificador del comercio |

## Payload de Ejemplo

```json
{
   "When":"2026-06-10T15:27:48.8183594Z",
   "Payload":{
      "TipoEvento":"PAGO",
      "TipoOrigen":"ENTIDAD",
      "IdentificadorOrigen":"A106",
      "TipoDestino":"ENTIDAD",
      "IdentificadorDestino":"A106",
      "DestinoPrincipal":"https://amorenobind.pythonanywhere.com/webhook",
      "DestinoSecundario":"",
      "FechaEmision":"2026-06-10T15:27:47.4981133+00:00",
      "IdMensaje":"29446201-3838-4be0-aefc-e20ab4a53717",
      "MensajePago":{
         "IdentificadorProcesador":"identificadorProcesadorEcoC",
         "IdentificadorTransaccion":"1397141",
         "IdentificadorOrdenVenta":"9OC35E6E026A3BCAB00000650901000000189879ET9A106TOC6D145ACCB9",
         "IdentificadorReferencia":"identificadorReferenciaEcoC",
         "IdOrdenVentaQr":"189879",
         "TipoTransaccion":"EcoCerrado",
         "RubroMovimiento":"EcoCerrado",
         "FechaNegocio":"2026-06-10T12:27:42.544-03:00",
         "FechaProceso":"2026-06-10T15:27:42.544-03:00",
         "FormaPago":"SALDO_VIRTUAL",
         "Moneda":"ARS",
         "ImporteBruto":458.9900000,
         "EstadoTransaccion":"ACREDITADO",
         "Retenciones":[],
         "Mcc":"5734",
         "Cpa":"C1006ACT",
         "Cuit":"",
         "CuentaVendedor":"",
         "IdentificadorVendedor":"CVU:0000532609800015076822|CBU:0000532609800015076822",
         "IdentificadorPagador":"20322678275",
         "CuentaPagador":"0000532609800015076822",
         "CodigoComercio":"C22951",
         "CodigoSucursal":"S18894",
         "CodigoCaja":"B00000650901",
         "InformacionAdicionalPagador":[],
         "Entidad":"A106",
         "Psp":"532",
         "Procesador":"SaldoVirtual",
         "InformacionAdicionalMensaje":[
            {
               "Descripcion":"idProvinciaSicore",
               "Valor":"00"
            }
         ],
         "FechaLiquidacion":null,
         "FechaPago":null,
         "MotivoRechazo":null
      }
   },
   "Type":"PAGO"
}
```

### Respuesta esperada al Webhook

| Código | Descripción |
|--------|-------------|
| `200` | Evento recibido correctamente |

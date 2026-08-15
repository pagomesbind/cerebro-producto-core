# EVENT — Webhook: Aviso de Devolución QR Estático

> Sincronizado el: 2026-06-30
> Fuente: https://psp.bind.com.ar/developers/apis/webhook-addevqrest
> Producto: Adquirencia > QR Estático

## Descripción

Se envía una notificación a través de un HTTP POST cada vez que se registra un contracargo asociado a una transacción.

Cada webhook debe responderse simplemente con un HTTP code 200, así se considerará que la Entidad recibió la notificación satisfactoriamente. De otra manera, el envío del webhook ingresará en un esquema de reintentos.

El webhook se enviará a la URL del destino que se haya configurado previamente en la Entidad.

Puede ser que el importe de la transacción no haya sido completamente devuelto, entonces el estado su estado seguirá siendo ACREDITADO.

## Payload del Evento

### Campos del Payload

| Campo | Tipo | Descripción |
|-------|------|-------------|
| `When` | datetime | Fecha y hora en que fue enviada la notificación (UTC + 0). |
| `Payload` | object | Objeto con información de la notificación. |
| `Payload.TipoEvento` | string | Valor fijo: `"CONTRACARGO"` |
| `Payload.TipoOrigen` | string | Valor fijo: `"ENTIDAD"` |
| `Payload.IdentificadorOrigen` | string | Código unívoco de la Entidad a la que pertenece el comercio. |
| `Payload.TipoDestino` | string | Valor fijo: `"ENTIDAD"` |
| `Payload.IdentificadorDestino` | string | Código unívoco de la Entidad a la que pertenece el comercio. |
| `Payload.DestinoPrincipal` | string | Es la URL del destino principal en donde se envía el webhook de notificación. |
| `Payload.DestinoSecundario` | string | Es la URL del destino secundario en donde se envía el webhook de notificación. |
| `Payload.FechaEmision` | datetime | Fecha y hora en que se envió la notificación (UTC + 0). |
| `Payload.IdMensaje` | string | Id guid de la notificación. |
| `Payload.MensajePago` | object | Objeto con la información del contracargo. |
| `Payload.MensajePago.IdentificadorProcesador` | string | Id de la transacción original en el procesador de pago (Coelsa, Global Processing, Decidir, etc). |
| `Payload.MensajePago.IdentificadorTransaccion` | string | Id de la transacción original. |
| `Payload.MensajePago.IdentificadorOrdenVenta` | string | Es un identificador adicional de interés para cada canal de pago. Para TipoTransaccion = Transferencia30 es el order id de la API Resolve en Coelsa. Para TipoTransaccion = Botón simple es el PaymentId. Para TipoTransaccion = CVUCollect es el CVU en el que se recibió el pago. Para TipoTransaccion = MPOS es el RRNN. |
| `Payload.MensajePago.IdentificadorReferencia` | string | Es un identificador adicional de referencia para cada canal de pago. |
| `Payload.MensajePago.IdOrdenVentaQr` | string | Es el identificador de la orden de venta de QR. |
| `Payload.MensajePago.TipoTransaccion` | string | Identifica al canal por el cuál se realizó el pago. Valores permitidos: `Transferencia30` = QR, `BotonSimple` = Botón de pagos de cobro no presente, `CVUCollect` = Recaudación por transferencia a CVU, `MPOS` = Smartpos de cobro presente. |
| `Payload.MensajePago.RubroMovimiento` | string | Rubro interno de la transacción. |
| `Payload.MensajePago.FechaNegocio` | datetime | Fecha y hora en que el cliente realizó el pago (UTC - 3). |
| `Payload.MensajePago.FechaProceso` | datetime | Fecha y hora en que se procesó el cobro (UTC - 3). |
| `Payload.MensajePago.FormaPago` | string | Medio de pago con que se realizó el pago. Valores permitidos: `"Transf30"` = QR interoperable, `"TTDD"` = Tarjeta de débito, `"TTCC"` = Tarjeta de crédito, `"Transfer"` = Recaudación por transferencia a CVU. |
| `Payload.MensajePago.Moneda` | string | Valor fijo: `"ARS"` = Pesos argentinos. |
| `Payload.MensajePago.ImporteBruto` | decimal | Importe bruto total de la transacción. Es lo que pagó el cliente final. |
| `Payload.MensajePago.EstadoTransaccion` | string | Estado de la transacción. Valores permitidos: `"DEVUELTA"` (Devolución exitosa - Estado definitivo). |
| `Payload.MensajePago.Retenciones` | array of objects | Por defecto es null. |
| `Payload.MensajePago.Mcc` | string | Código de rubro según VISA MCC del comercio. |
| `Payload.MensajePago.Cpa` | string | Código postal argentino del comercio. |
| `Payload.MensajePago.Cuit` | string | CUIT del comercio. |
| `Payload.MensajePago.CuentaVendedor` | string | CVU del comercio. |
| `Payload.MensajePago.IdentificadorVendedor` | string | Información relativa al comercio. Concatena el CVU, el CBU y el ID Wallet (aplica para pagos con QR). |
| `Payload.MensajePago.IdentificadorPagador` | string | CUIT del cliente pagador. |
| `Payload.MensajePago.CuentaPagador` | string | CBU/CVU del cliente pagador. |
| `Payload.MensajePago.CodigoComercio` | string | Código identificador del comercio en el sistema. |
| `Payload.MensajePago.CodigoSucursal` | string | Código identificador de la sucursal en el sistema. |
| `Payload.MensajePago.CodigoCaja` | string | Código identificador de la caja en el sistema. |
| `Payload.MensajePago.InformacionAdicionalPagador[]` | array of object | Objeto con tuplas llave-valor con información adicional referente al cliente pagador. |
| `Payload.MensajePago.Entidad` | string | Es un código unívoco de la Entidad en el sistema. |
| `Payload.MensajePago.Psp` | string | Es el código del PSP al que pertenece la Entidad. |
| `Payload.MensajePago.Procesador` | string | Id del pago enviado por el procesador del pago (Coelsa, Global Processing, Decidir, etc). Es el identificador que utilizamos para conciliar con nuestros procesadores. |
| `Payload.MensajePago.InformacionAdicionalMensaje[{}]` | object | Objeto con tuplas llave-valor con información adicional referente a la notificación. |
| `Payload.MensajePago.InformacionAdicionalMensaje[{}].Descripcion` | string | Nombre del dato de información adicional. Valores posibles: `"motivoContracargo"`, `"importe"`, `"contracargoParcial"`, `"idContracargo"`, `"fechaContracargo"`, `"estadoContracargo"`, `"importeContracargo"`, `"tipoContracargo"`, `"idDebin"`, `"debinIdApiBank"`. Pueden agregarse nuevos objetos por necesidades de negocio u operativos. |
| `Payload.MensajePago.InformacionAdicionalPagador[{}].Valor` | string | Valor del dato de información adicional según la Descripción correspondiente. |
| `Type` | string | Indica el tipo de evento al que corresponde el presente webhook. Valores permitidos: `"CONTRACARGO"` = Se trata de un webhook de devolución. |

## Ejemplo de Payload

```json
{
  "When": "2026-06-16T14:23:40.1630666Z",
  "Payload": {
    "TipoEvento": "CONTRACARGO",
    "TipoOrigen": "ENTIDAD",
    "IdentificadorOrigen": "BS20",
    "TipoDestino": "ENTIDAD",
    "IdentificadorDestino": "BS20",
    "DestinoPrincipal": "https://123456.com/webhook",
    "DestinoSecundario": "https://123456e.com/webhook",
    "FechaEmision": "2026-06-16T14:23:39.7751462+00:00",
    "IdMensaje": "1457ab39-170b-409d-9a6b-c19d1b332d0c",
    "MensajePago": {
      "IdentificadorProcesador": "67REZ8NP1MKY3M124KVGOP",
      "IdentificadorTransaccion": "1398916",
      "IdentificadorOrdenVenta": "0000532600009999034401",
      "IdentificadorReferencia": "NCQA-BS2.0-5932",
      "IdOrdenVentaQr": "999903440",
      "TipoTransaccion": "Boton20",
      "RubroMovimiento": "TransferenciaEntranteCvu",
      "FechaNegocio": "2026-06-16T11:23:37.5581857-03:00",
      "FechaProceso": "2026-06-16T11:18:58.6846225+00:00",
      "FechaLiquidacion": null,
      "FechaPago": null,
      "FormaPago": "TransferCvu",
      "Moneda": "ARS",
      "ImporteBruto": 5912,
      "EstadoTransaccion": "DEVUELTA",
      "Retenciones": [],
      "Mcc": null,
      "Cpa": "C1006ACT",
      "Cuit": null,
      "CuentaVendedor": "322-20-1-735135-8-5",
      "IdentificadorVendedor": "CVU:00005319083200672123456WAL:|CBU:3220001805007352123458",
      "IdentificadorPagador": "20415865091",
      "CuentaPagador": "0000532609240002744097",
      "CodigoComercio": "C22903",
      "CodigoSucursal": "S18803",
      "CodigoCaja": "B00000623451",
      "InformacionAdicionalPagador": null,
      "Entidad": "BS20",
      "Psp": "531",
      "Procesador": "67REZ8NP1MKY3M124KVGOP",
      "MotivoRechazo": null,
      "InformacionAdicionalMensaje": [
        { "Descripcion": "motivoContracargo", "Valor": "NCQA-BS2.0" },
        { "Descripcion": "importe", "Valor": "5912.00" },
        { "Descripcion": "contracargoParcial", "Valor": "False" },
        { "Descripcion": "idContracargo", "Valor": "7835" },
        { "Descripcion": "fechaContracargo", "Valor": "06/16/2026 11:23:37" },
        { "Descripcion": "estadoContracargo", "Valor": "ACEPTADO" },
        { "Descripcion": "importeContracargo", "Valor": "5912.00" },
        { "Descripcion": "tipoContracargo", "Valor": "contracargo" },
        { "Descripcion": "idDebin", "Valor": "7L8GYKNXR4EYKZXNMPRZ50" },
        { "Descripcion": "debinIdApiBank", "Valor": "" }
      ]
    }
  },
  "Type": "CONTRACARGO"
}
```

## Respuesta esperada al Webhook

| Código | Descripción |
|--------|-------------|
| `200` | Evento recibido correctamente |

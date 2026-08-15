# EVENT — Webhook: Aviso de Transacción QR Estático

> Sincronizado el: 2026-06-30
> Fuente: https://psp.bind.com.ar/developers/apis/webhook-adqrestatico
> Producto: Adquirencia > QR Estático

## Descripción

Se envía una notificación a través de un HTTP POST cada vez que una se crea una transacción de canal QR en estado "ACREDITADO" o "RECHAZADO".

Cada webhook debe responderse simplemente con un HTTP code 200, así se considerará que la Entidad recibió la notificación satisfactoriamente. De otra manera, el envío del webhook ingresará en un esquema de reintentos.

El webhook se enviará a la URL del destino que se haya configurado previamente en la Entidad.

## Payload del Evento

### Campos del Payload

| Campo | Tipo | Descripción |
|-------|------|-------------|
| `When` | datetime | Fecha y hora en que fue enviada la notificación (UTC +0). |
| `Payload` | object | Objeto con información del mensaje. |
| `Payload.TipoEvento` | string | Identifica el tipo de evento de webhook. Valor fijo: `"PAGO"` |
| `Payload.TipoOrigen` | string | Valor fijo: `"ENTIDAD"` |
| `Payload.IdentificadorOrigen` | string | Código unívoco de la Entidad a la que pertenece el comercio. |
| `Payload.TipoDestino` | string | Valor fijo: `"ENTIDAD"` |
| `Payload.IdentificadorDestino` | string | Código de la Entidad del comercio. |
| `Payload.DestinoPrincipal` | string | Es la URL del destino principal en donde se envía el webhook de notificación. |
| `Payload.DestinoSecundario` | string | Es la URL del destino secundario en donde se envía el webhook de notificación. |
| `Payload.FechaEmision` | datetime | Fecha y hora en que se envió la notificación (UTC +0). |
| `Payload.IdMensaje` | string | Id guid de la notificación. |
| `Payload.MensajePago` | object | Objeto con la información del pago. |
| `Payload.MensajePago.IdentificadorProcesador` | string | Id del pago enviado por el procesador del pago. Es el identificador que utilizamos para conciliar con nuestros procesadores. |
| `Payload.MensajePago.IdentificadorTransaccion` | string | Id de la transacción. |
| `Payload.MensajePago.IdentificadorOrdenVenta` | string | Es un identificador adicional de interés para cada canal de pago. Para QR es el order id de la API Resolve (el que usó la billetera para iniciar el pago en Coelsa). |
| `Payload.MensajePago.IdentificadorReferencia` | string | Es el identificador externo indicado opcionalmente por la entidad. |
| `Payload.MensajePago.IdOrdenVentaQr` | string | Es el identificador de la orden de venta o de la deuda. |
| `Payload.MensajePago.TipoTransaccion` | string | Identifica al canal por el cuál se realizó el pago. Valores posibles: `"Transferencia30"` (QR interoperable) |
| `Payload.MensajePago.RubroMovimiento` | string | Rubro interno de la transacción. Valores posibles: `"PagoQrTransferencia30"` (QR interoperable) |
| `Payload.MensajePago.FechaNegocio` | datetime | Fecha y hora en que el cliente realizó el pago (UTC -3). |
| `Payload.MensajePago.FechaProceso` | datetime | Fecha y hora en que se procesó el cobro (UTC -3). |
| `Payload.MensajePago.FormaPago` | string | Medio de pago con que se realizó el pago. Valores permitidos: `"Transf30"` (QR interoperable) |
| `Payload.MensajePago.Moneda` | string | Valor fijo: `"ARS"` (Pesos argentinos) |
| `Payload.MensajePago.ImporteBruto` | decimal | Importe bruto total de la transacción. Es lo que pagó el cliente final. |
| `Payload.MensajePago.EstadoTransaccion` | string | Estado de la transacción. Valores permitidos: `"ACREDITADO"` (Pago exitoso), `"RECHAZADA"` (Pago rechazado) |
| `Payload.MensajePago.Retenciones` | array | Array de objetos vacío por defecto en este evento. |
| `Payload.MensajePago.Mcc` | string | Código de rubro según VISA MCC del comercio. |
| `Payload.MensajePago.Cpa` | string | Código postal argentino del comercio. |
| `Payload.MensajePago.Cuit` | string | CUIT del comercio. |
| `Payload.MensajePago.CuentaVendedor` | string | CVU del comercio. |
| `Payload.MensajePago.IdentificadorVendedor` | string | Información relativa al comercio. Concatena el CVU, el CBU y el ID de la billetera con la que se pagó (lo último aplica para pagos con QR). |
| `Payload.MensajePago.IdentificadorPagador` | string | CUIT del cliente pagador. |
| `Payload.MensajePago.CuentaPagador` | string | CBU/CVU del cliente pagador. |
| `Payload.MensajePago.CodigoComercio` | string | Código identificador del comercio. |
| `Payload.MensajePago.CodigoSucursal` | string | Código identificador de la sucursal. |
| `Payload.MensajePago.CodigoCaja` | string | Código identificador de la caja. |
| `Payload.MensajePago.InformacionAdicionalPagador[{}]` | array of objects | Array de objetos con tuplas llave-valor con información adicional referente al cliente pagador. |
| `Payload.MensajePago.InformacionAdicionalPagador[{}].Descripcion` | string | Nombre del dato de información adicional. Valores posibles: `"idBilletera"`. Pueden agregarse nuevos objetos por necesidades de negocio u operativos. |
| `Payload.MensajePago.InformacionAdicionalPagador[{}].Valor` | string | Valor del dato de información adicional. Si es `"idBilletera"` = Identificador de la billetera virtual que pagó el QR. |
| `Payload.MensajePago.Entidad` | string | Es un código unívoco de la Entidad en el sistema. |
| `Payload.MensajePago.Psp` | string | Es el código del PSP al que pertenece la Entidad. |
| `Payload.MensajePago.Procesador` | string | Es el nombre del procesador externo. |
| `Payload.MensajePago.InformacionAdicionalMensaje[{}]` | array of objects | Objeto con tuplas llave-valor con información adicional referente a la notificación. |
| `Payload.MensajePago.InformacionAdicionalMensaje[{}].Descripcion` | string | Nombre del dato de información adicional. Valores posibles: `"idProvinciaSicore"`, `"IdComprobante"`. Pueden agregarse nuevos objetos por necesidades de negocio u operativos. |
| `Payload.MensajePago.InformacionAdicionalMensaje[{}].Valor` | string | Valor del dato. Si es `"idProvinciaSicore"` = Código de provincia para cálculo de impuestos. Si es `"IdComprobante"` = Id del comprobante creado en la cuenta de wallet asociada al comercio para acreditar el cobro neto de comisiones. |
| `Payload.MensajePago.FechaLiquidacion` | datetime | Fecha en que se liquidó la transacción. Por defecto es null si no se liquida en línea. |
| `Payload.MensajePago.FechaPago` | datetime | Fecha en que se pagó la transacción. Se utiliza cuando una transacción se inserta más tarde por un proceso de conciliación. |
| `Payload.MensajePago.MotivoRechazo` | string | Descripción del motivo de rechazo. |
| `Type` | string | Indica el tipo de evento al que corresponde el presente webhook. Valor fijo: `"PAGO"` (Se trata de un webhook de aviso de pago). |

## Ejemplo de Payload

```json
{
    "When": "2026-06-10T12:13:00.6127715Z",
    "Payload": {
        "TipoEvento": "PAGO",
        "TipoOrigen": "ENTIDAD",
        "IdentificadorOrigen": "B",
        "TipoDestino": "ENTIDAD",
        "IdentificadorDestino": "B",
        "DestinoPrincipal": "https://urldestino.com/webhook",
        "DestinoSecundario": "https://urldestino.com/webhook",
        "FechaEmision": "2026-06-10T12:13:00.530638+00:00",
        "IdMensaje": "5395782e-343c-4833-9ceb-cddfcfaa6f26",
        "MensajePago": {
            "IdentificadorProcesador": "PDX4OGNYG3Y1YLPQN0L6EY",
            "IdentificadorTransaccion": "27165171",
            "IdentificadorOrdenVenta": "9OA23FD204D354CAB00000362573000000000000ET9000BTOA88C5108116",
            "IdentificadorReferencia": null,
            "IdOrdenVentaQr": "14928213",
            "TipoTransaccion": "Transferencia30",
            "RubroMovimiento": "PagoQrTransferencia30",
            "FechaNegocio": "2026-06-10T09:12:51.1471001-03:00",
            "FechaProceso": "2026-06-10T09:12:51.3816306-03:00",
            "FormaPago": "Transf30",
            "Moneda": "ARS",
            "ImporteBruto": 170000,
            "EstadoTransaccion": "ACREDITADO",
            "Retenciones": [],
            "Mcc": "5422",
            "Cpa": "4400",
            "Cuit": "30710345992",
            "CuentaVendedor": "0000164506600067023747",
            "IdentificadorVendedor": "CVU:0000164506600067023747WAL:9|CBU:3220031505006895500019",
            "IdentificadorPagador": "20213111931",
            "CuentaPagador": "0000003100013410873887",
            "CodigoComercio": "C02374",
            "CodigoSucursal": "S04661",
            "CodigoCaja": "B00000362573",
            "InformacionAdicionalPagador": [
                { "Descripcion": "idBilletera", "Valor": "9" }
            ],
            "Entidad": "B",
            "Psp": "164",
            "Procesador": "PDX4OGNYG3Y1YLPQN0L6EY",
            "InformacionAdicionalMensaje": [
                { "Descripcion": "idProvinciaSicore", "Valor": "09" }
            ],
            "FechaLiquidacion": null,
            "FechaPago": null,
            "MotivoRechazo": null
        }
    },
    "Type": "PAGO"
}
```

## Respuesta esperada al Webhook

| Código | Descripción |
|--------|-------------|
| `200` | Evento recibido correctamente |

## ⚠️ Notas y Advertencias del Portal

> Para recibir este evento la entidad debe tener parametrizada la URL destino para el producto.

> No debe validarse la estructura del mensaje. Bind PSP puede agregar arbitrariamente nuevos atributos opcionales al request por nuevas funcionalidades o mejoras.

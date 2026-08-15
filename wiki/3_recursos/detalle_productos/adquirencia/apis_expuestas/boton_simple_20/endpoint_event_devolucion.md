# Endpoint — Aviso de devolución botón simple 2.0 (EVENT)

> Fuente: https://psp.bind.com.ar/developers/apis/webhook-addevbs20
> Producto: Adquirencia — Botón Simple 2.0

## Descripción

Se envía una notificación a través de un HTTP POST cada vez que se registra un contracargo asociado a una transacción.

Cada webhook debe responderse simplemente con un HTTP code 200, así se considerará que la Entidad recibió la notificación satisfactoriamente. De otra manera, el envío del webhook ingresará en un esquema de reintentos.

El webhook se enviará a la URL del destino que se haya configurado previamente en la Entidad.

## ⚠️ Notas y Advertencias del Portal

> Puede ser que el importe de la transacción no haya sido completamente devuelto, entonces el estado su estado seguirá siendo ACREDITADO.

> Los desconocimientos de tarjetas se informan como contracargos de tipo "desconocimiento".

## Payload (Body del webhook)

| Campo | Tipo | Descripción |
|-------|------|-------------|
| `When` | datetime | Fecha y hora en que fue enviada la notificación (UTC +0). |
| `Payload.TipoEvento` | string | Valor fijo: `"CONTRACARGO"` |
| `Payload.TipoOrigen` | string | Valor fijo: `"ENTIDAD"` |
| `Payload.IdentificadorOrigen` | string | Código unívoco de la Entidad a la que pertenece el comercio. |
| `Payload.TipoDestino` | string | Valor fijo: `"ENTIDAD"` |
| `Payload.IdentificadorDestino` | string | Código unívoco de la Entidad a la que pertenece el comercio. |
| `Payload.DestinoPrincipal` | string | URL del destino principal del webhook. |
| `Payload.DestinoSecundario` | string | URL del destino secundario del webhook. |
| `Payload.FechaEmision` | datetime | Fecha y hora en que se envió la notificación (UTC +0). |
| `Payload.IdMensaje` | string | Id guid de la notificación. |
| `Payload.MensajePago.IdentificadorProcesador` | string | Id de la transacción original en el procesador de pago (Coelsa, Global Processing, Decidir, etc). |
| `Payload.MensajePago.IdentificadorTransaccion` | string | Id de la transacción original. |
| `Payload.MensajePago.IdentificadorOrdenVenta` | string | Para TipoTransaccion=Boton20: el PaymentId (id del link de pago). |
| `Payload.MensajePago.IdentificadorReferencia` | string | Identificador adicional de referencia para el canal de pago. |
| `Payload.MensajePago.TipoTransaccion` | string | Valores: `"Transferencia30"` (QR), `"BotonSimple"` (Botón de pagos), `"CVUCollect"` (Recaudación CVU), `"MPOS"` (Smartpos) |
| `Payload.MensajePago.RubroMovimiento` | string | Rubro interno de la transacción. |
| `Payload.MensajePago.FechaNegocio` | datetime | Fecha y hora en que el cliente realizó el pago (UTC -3). |
| `Payload.MensajePago.FechaProceso` | datetime | Fecha y hora en que se procesó el cobro (UTC -3). |
| `Payload.MensajePago.FormaPago` | string | Valores: `"Transf30"` (QR interoperable), `"TTDD"` (Débito), `"TTCC"` (Crédito), `"Transfer"` (CVU) |
| `Payload.MensajePago.Moneda` | string | Valor fijo: `"ARS"` |
| `Payload.MensajePago.ImporteBruto` | decimal | Importe bruto total de la transacción original. |
| `Payload.MensajePago.EstadoTransaccion` | string | Valor fijo: `"DEVUELTA"` (Devolución exitosa — estado definitivo). |
| `Payload.MensajePago.Retenciones` | array | Por defecto es null. |
| `Payload.MensajePago.Mcc` | string | Código de rubro según VISA MCC del comercio. |
| `Payload.MensajePago.Cpa` | string | Código postal argentino del comercio. |
| `Payload.MensajePago.Cuit` | string | CUIT del comercio. |
| `Payload.MensajePago.CuentaVendedor` | string | CVU del comercio. |
| `Payload.MensajePago.IdentificadorVendedor` | string | Concatena CVU, CBU e ID Wallet (aplica para pagos con QR). |
| `Payload.MensajePago.IdentificadorPagador` | string | CUIT del cliente pagador. |
| `Payload.MensajePago.CuentaPagador` | string | CBU/CVU del cliente pagador. |
| `Payload.MensajePago.CodigoComercio` | string | Código identificador del comercio. |
| `Payload.MensajePago.CodigoSucursal` | string | Código identificador de la sucursal. |
| `Payload.MensajePago.CodigoCaja` | string | Código identificador de la caja. |
| `Payload.MensajePago.InformacionAdicionalPagador[]` | array | Tuplas llave-valor con información adicional del cliente pagador. |
| `Payload.MensajePago.Entidad` | string | Código unívoco de la Entidad en el sistema. |
| `Payload.MensajePago.Psp` | string | Código del PSP al que pertenece la Entidad. |
| `Payload.MensajePago.Procesador` | string | Id del pago enviado por el procesador. |
| `Payload.MensajePago.InformacionAdicionalMensaje[{}].Descripcion` | string | Valores posibles: `"motivoContracargo"`, `"importe"`, `"contracargoParcial"`, `"idContracargo"`, `"fechaContracargo"`, `"estadoContracargo"`, `"importeContracargo"`, `"tipoContracargo"`, `"idDebin"`, `"debinIdApiBank"`. Pueden agregarse nuevos objetos. |
| `Payload.MensajePago.InformacionAdicionalMensaje[{}].Valor` | string | motivoContracargo=Descripción del motivo; importe=Importe de la transacción; contracargoParcial=Si fue parcial o no; idContracargo=Id del contracargo; fechaContracargo=Fecha de creación; estadoContracargo=Estado; importeContracargo=Importe devuelto; tipoContracargo=Valores: "contracargo" o "desconocimiento"; idDebin=Id del procesador externo; debinIdApiBank=Id del débito sobre CBU del comercio. |
| `Type` | string | Valor fijo: `"CONTRACARGO"` |

## Ejemplo JSON

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

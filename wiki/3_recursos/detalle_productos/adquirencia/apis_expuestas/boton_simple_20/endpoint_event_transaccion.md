# Endpoint — Aviso de transacción botón simple 2.0 (EVENT)

> Fuente: https://psp.bind.com.ar/developers/apis/webhook-adboton20
> Producto: Adquirencia — Botón Simple 2.0

## Descripción

Se envía una notificación a través de un HTTP POST cada vez que una se crea una transacción de canal Botón simple 2.0 en estado "ACREDITADO" o "RECHAZADO"

Cada webhook debe responderse simplemente con un HTTP code 200, así se considerará que la Entidad recibió la notificación satisfactoriamente. De otra manera, el envío del webhook ingresará en un esquema de reintentos.

El webhook se enviará a la URL del destino que se haya configurado previamente en la Entidad.

Para recibir este evento la entidad debe tener parametrizada la URL destino para el producto.

## ⚠️ Notas y Advertencias del Portal

> No debe validarse la estructura del mensaje. Bind PSP puede agregar arbitrariamente nuevos atributos opcionales al request por nuevas funcionalidades o mejoras.

## Payload (Body del webhook)

| Campo | Tipo | Descripción |
|-------|------|-------------|
| `When` | datetime | Fecha y hora en que fue enviada la notificación (UTC +0). |
| `Payload` | object | Objeto con información del mensaje. |
| `Payload.TipoEvento` | string | Valor fijo: `"PAGO"` |
| `Payload.TipoOrigen` | string | Valor fijo: `"ENTIDAD"` |
| `Payload.IdentificadorOrigen` | string | Código unívoco de la Entidad a la que pertenece el comercio. |
| `Payload.TipoDestino` | string | Valor fijo: `"ENTIDAD"` |
| `Payload.IdentificadorDestino` | string | Código de la Entidad del comercio. |
| `Payload.DestinoPrincipal` | string | Es la URL del destino principal en donde se envía el webhook de notificación. |
| `Payload.DestinoSecundario` | string | Es la URL del destino secundario en donde se envía el webhook de notificación. |
| `Payload.FechaEmision` | datetime | Fecha y hora en que se envió la notificación (UTC +0). |
| `Payload.IdMensaje` | string | Id guid de la notificación. |
| `Payload.MensajePago.IdentificadorProcesador` | string | Id del pago enviado por el procesador del pago. Es el identificador que utilizamos para conciliar con nuestros procesadores. |
| `Payload.MensajePago.IdentificadorTransaccion` | string | Id de la transacción. |
| `Payload.MensajePago.IdentificadorOrdenVenta` | string | Para Botón simple 2.0: el guid asociado al link de pago. |
| `Payload.MensajePago.IdentificadorReferencia` | string | Es el codigoDeuda indicado por la entidad en la creación del link de pago. |
| `Payload.MensajePago.IdOrdenVentaQr` | string | Es el identificador de la deuda asociada al link de pago. |
| `Payload.MensajePago.TipoTransaccion` | string | Valor fijo: `"Boton20"` |
| `Payload.MensajePago.RubroMovimiento` | string | Subcanal por el cual se realizó el pago. Valores: `"BotonSimple"`, `"PagoQrTransferencia30"`, `"TransferenciaEntranteCvu"` |
| `Payload.MensajePago.FechaNegocio` | datetime | Fecha y hora en que el cliente realizó el pago (UTC -3). |
| `Payload.MensajePago.FechaProceso` | datetime | Fecha y hora en que se procesó el cobro (UTC -3). |
| `Payload.MensajePago.FormaPago` | string | Medio de pago. Valores: `"TTDD"` (Tarjeta de débito), `"TTCC"` (Tarjeta de crédito), `"TTPP"` (Tarjeta prepaga), `"Transf30"` (QR interoperable), `"TRANSFER"` (Transferencia en CVU) |
| `Payload.MensajePago.Moneda` | string | Valor fijo: `"ARS"` |
| `Payload.MensajePago.ImporteBruto` | decimal | Importe bruto total de la transacción. Es lo que pagó el cliente final. |
| `Payload.MensajePago.EstadoTransaccion` | string | Valores: `"ACREDITADO"` (Pago exitoso), `"RECHAZADA"` (Pago rechazado) |
| `Payload.MensajePago.Retenciones` | array | Array vacío por defecto en este evento. |
| `Payload.MensajePago.Mcc` | string | Código de rubro según VISA MCC del comercio. |
| `Payload.MensajePago.Cpa` | string | Código postal argentino del comercio. |
| `Payload.MensajePago.Cuit` | string | CUIT del comercio. |
| `Payload.MensajePago.CuentaVendedor` | string | CVU del comercio. |
| `Payload.MensajePago.IdentificadorVendedor` | string | Concatena el CVU, el CBU y el ID de la billetera con la que se pagó (lo último aplica para pagos con QR). |
| `Payload.MensajePago.IdentificadorPagador` | string | CUIT del cliente pagador. |
| `Payload.MensajePago.CuentaPagador` | string | CBU/CVU del cliente pagador o PAN de la tarjeta ofuscado. |
| `Payload.MensajePago.CodigoComercio` | string | Código identificador del comercio. |
| `Payload.MensajePago.CodigoSucursal` | string | Código identificador de la sucursal. |
| `Payload.MensajePago.CodigoCaja` | string | Código identificador de la caja. |
| `Payload.MensajePago.InformacionAdicionalPagador[{}].Descripcion` | string | Nombre del dato. Valores posibles: `"dni"`, `"marca"`, `"cuotas"`, `"idBilletera"`. Pueden agregarse nuevos objetos por necesidades de negocio u operativos. |
| `Payload.MensajePago.InformacionAdicionalPagador[{}].Valor` | string | Valor según Descripcion: dni=DNI del usuario, marca=Marca de la tarjeta, cuotas=Cantidad de cuotas, idBilletera=Id de la billetera virtual. |
| `Payload.MensajePago.Productos[{}]` | array | Array con información de cada producto item asociado a la deuda. |
| `Payload.MensajePago.Entidad` | string | Código de la Entidad. |
| `Payload.MensajePago.Psp` | string | Código del PSP al que pertenece la Entidad. |
| `Payload.MensajePago.Procesador` | string | Nombre del procesador externo. |
| `Payload.MensajePago.InformacionAdicionalMensaje[{}].Descripcion` | string | Valores posibles: `"idProvinciaSicore"`, `"IdComprobante"`, `"motivoRechazo"`, `"identificadorProcesadorTID"`, `"idDeuda"`, `"EstadoDeuda"`, `"IdentificadorReferencia"`, `"CodigoExterno"`. Pueden agregarse nuevos objetos. |
| `Payload.MensajePago.InformacionAdicionalMensaje[{}].Valor` | string | idProvinciaSicore=Código de provincia para impuestos; IdComprobante=Id del comprobante wallet; motivoRechazo=Motivo del rechazo; identificadorProcesadorTID=TID de DECIDIR; idDeuda=Id de la deuda; IdentificadorReferencia=Código para iniciar contracargo; CodigoExterno=codigoDeuda externo. |
| `Payload.MensajePago.FechaLiquidacion` | datetime | Fecha de liquidación. Por defecto null si no se liquida en línea. |
| `Payload.MensajePago.FechaPago` | datetime | Fecha de pago. Se utiliza cuando una transacción se inserta más tarde por conciliación. |
| `Payload.MensajePago.MotivoRechazo` | string | Descripción del motivo de rechazo. |
| `Type` | string | Valor fijo: `"PAGO"` |

## Ejemplo JSON

```json
{
  "When": "2026-06-09T18:31:13.1589544Z",
  "Payload": {
    "TipoEvento": "PAGO",
    "TipoOrigen": "ENTIDAD",
    "IdentificadorOrigen": "BS20",
    "TipoDestino": "ENTIDAD",
    "IdentificadorDestino": "BS20",
    "DestinoPrincipal": "https://amorenobind.pythonanywhere.com/webhook",
    "DestinoSecundario": "https://amorenobind.pythonanywhere.com/webhook",
    "FechaEmision": "2026-06-09T18:31:11.0058197+00:00",
    "IdMensaje": "3d589e30-2b3f-4fb9-982e-b5e8d350a64d",
    "MensajePago": {
      "IdentificadorProcesador": "153106",
      "IdentificadorTransaccion": "1396526",
      "IdentificadorOrdenVenta": "a4158f26-394a-41c0-b172-feaa5a38bf27",
      "IdentificadorReferencia": "NCQA-BS2.0-2520",
      "IdOrdenVentaQr": "14364613",
      "TipoTransaccion": "Boton20",
      "RubroMovimiento": "BotonSimple",
      "FechaNegocio": "2026-06-09T15:31:06.475983-03:00",
      "FechaProceso": "2026-06-09T15:31:06.95-03:00",
      "FormaPago": "TTDD",
      "Moneda": "ARS",
      "ImporteBruto": 2520,
      "EstadoTransaccion": "ACREDITADO",
      "Retenciones": [],
      "Mcc": "56482",
      "Cpa": "C1006ACT",
      "Cuit": "20322678275",
      "CuentaVendedor": "3220001823007351860012",
      "IdentificadorVendedor": "CVU:0000531908320067229030WAL:|CBU:3220001805007352560018",
      "IdentificadorPagador": "",
      "CuentaPagador": "451772****6075",
      "CodigoComercio": "C22903",
      "CodigoSucursal": "S18803",
      "CodigoCaja": "B00000623451",
      "InformacionAdicionalPagador": [
        { "Descripcion": "dni", "Valor": "41586509" },
        { "Descripcion": "marca", "Valor": "VISA" },
        { "Descripcion": "cuotas", "Valor": "1" }
      ],
      "Productos": [
        {
          "Descripcion": "Coca",
          "CodigoProducto": "ProductoQA",
          "Monto": 2520,
          "Cantidad": 1,
          "Adicional": "infoAdicionalProductoQA"
        }
      ],
      "Entidad": "BS20",
      "Psp": "531",
      "Procesador": "DECIDIR",
      "InformacionAdicionalMensaje": [
        { "Descripcion": "idProvinciaSicore", "Valor": "00" },
        { "Descripcion": "motivoRechazo", "Valor": "" },
        { "Descripcion": "identificadorProcesadorTID", "Valor": "" },
        { "Descripcion": "idDeuda", "Valor": "14364613" },
        { "Descripcion": "EstadoDeuda", "Valor": "PAGADA" },
        { "Descripcion": "IdentificadorReferencia", "Valor": "153106" },
        { "Descripcion": "CodigoExterno", "Valor": "{\"codigoDeuda\":\"NCQA-BS2.0-2520\"}" }
      ],
      "FechaLiquidacion": null,
      "FechaPago": null,
      "MotivoRechazo": null
    }
  },
  "Type": "PAGO"
}
```

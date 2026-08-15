# EVENT — Webhook: Aviso Transacción Recaudación por Transferencia (RxT)

> Extraído el: 2026-06-30
> Fuente: https://psp.bind.com.ar/developers/apis/webhook-adrxt
> Producto: Adquirencia > Recaudación por Transferencia (RxT)

## Descripción

"Se envía una notificación a través de un HTTP POST cada vez que una se crea una transacción de canal recaudación por transferencia en estado 'ACREDITADO'."

El sistema requiere respuesta HTTP 200 para confirmar recepción exitosa. En caso contrario, implementa reintentos automáticos. La URL destino debe configurarse previamente en la entidad.

## ⚠️ Notas y Advertencias del Portal

> "Para recibir este evento la entidad debe tener parametrizada la URL destino para el producto."

> "No debe validarse la estructura del mensaje. Bind PSP puede agregar arbitrariamente nuevos atributos opcionales al request."

> Manejo de Reintentos: Responder solo con HTTP 200; cualquier otro código activa mecanismo de reintento automático.

## Campos del Payload

| Campo | Tipo | Descripción |
|-------|------|-------------|
| `When` | datetime | Timestamp de envío (UTC +0) |
| `Type` | string | Valor fijo: "PAGO" |
| `Payload.TipoEvento` | string | Fijo: "PAGO" |
| `Payload.IdentificadorOrigen` | string | Código único de entidad |
| `Payload.IdMensaje` | string | GUID de la notificación |
| `Payload.MensajePago.IdentificadorTransaccion` | string | ID de la transacción |
| `Payload.MensajePago.IdentificadorOrdenVenta` | string | CVU receptor del pago |
| `Payload.MensajePago.IdentificadorReferencia` | string | Alias del CVU |
| `Payload.MensajePago.FormaPago` | string | Fijo: "TRANSFER" |
| `Payload.MensajePago.ImporteBruto` | decimal | Monto total pagado |
| `Payload.MensajePago.EstadoTransaccion` | string | Fijo: "ACREDITADO" |
| `Payload.MensajePago.FechaNegocio` | datetime | Momento del pago (UTC -3) |
| `Payload.MensajePago.IdentificadorPagador` | string | CUIT del pagador |
| `Payload.MensajePago.CuentaPagador` | string | CBU/CVU del pagador |
| `Payload.MensajePago.Moneda` | string | Fijo: "ARS" |

## Payload de Ejemplo

```json
{
    "When": "2026-06-10T00:23:41.3948806Z",
    "Payload": {
        "TipoEvento": "PAGO",
        "TipoOrigen": "ENTIDAD",
        "IdentificadorOrigen": "A032",
        "TipoDestino": "ENTIDAD",
        "IdentificadorDestino": "A032",
        "DestinoPrincipal": "https://urldestino.com/webhook",
        "DestinoSecundario": "https://urldestino.com/webhook",
        "FechaEmision": "2026-06-10T00:23:41.3502978+00:00",
        "IdMensaje": "7c4b3c92-deae-4a42-9755-4255bb0810b1",
        "MensajePago": {
            "IdentificadorProcesador": "67REZ8NPQV8ZJRMR94KVGO",
            "IdentificadorTransaccion": "27109026",
            "IdentificadorOrdenVenta": "0000184301020912179796",
            "IdentificadorReferencia": "regresionrxt9857",
            "IdOrdenVentaQr": "",
            "TipoTransaccion": "TransferenciaEntranteCvu",
            "RubroMovimiento": "TransferenciaEntranteCvu",
            "FechaNegocio": "2026-06-09T21:23:41.2203391-03:00",
            "FechaProceso": "2026-06-10T00:23:41.141+00:00",
            "FormaPago": "TRANSFER",
            "Moneda": "ARS",
            "ImporteBruto": 2,
            "EstadoTransaccion": "ACREDITADO",
            "Retenciones": [],
            "Mcc": "",
            "Cpa": "C1006ACT",
            "Cuit": "",
            "CuentaVendedor": "322-20-1-749049-1-5",
            "IdentificadorVendedor": "CVU:0000164505032067074006WAL:|CBU:3220001881007553170113",
            "IdentificadorPagador": "30717449076",
            "CuentaPagador": "3220001805007490490019",
            "CodigoComercio": "C07400",
            "CodigoSucursal": "S11369",
            "CodigoCaja": "B00001138098",
            "InformacionAdicionalPagador": [],
            "Entidad": "A032",
            "Psp": "164",
            "Procesador": "APIBANKBIND",
            "InformacionAdicionalMensaje": [
                {
                    "Descripcion": "idProvinciaSicore",
                    "Valor": "01"
                }
            ],
            "FechaLiquidacion": null,
            "FechaPago": null,
            "MotivoRechazo": null
        }
    },
    "Type": "PAGO"
}
```

### Respuesta esperada al Webhook

| Código | Descripción |
|--------|-------------|
| `200` | Evento recibido correctamente |

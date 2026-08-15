# EVENT — Webhook: Transacción Botón Simple 1.0

> Extraído el: 2026-06-30
> Fuente: https://psp.bind.com.ar/developers/apis/webhook-adboton10
> Producto: Adquirencia > Botón Simple

## Descripción

"Se envía una notificación a través de un HTTP POST cada vez que una se crea una transacción de canal Botón simple 1.0 en estado 'ACREDITADO' o 'RECHAZADO'."

La entidad debe responder con código HTTP 200 para confirmar recepción exitosa. Sin esta confirmación, el sistema reintenta el envío automáticamente. La URL de destino debe configurarse previamente en la entidad.

## ⚠️ Notas y Advertencias del Portal

> "No debe validarse la estructura del mensaje. Bind PSP puede agregar arbitrariamente nuevos atributos opcionales al request."

> Se requiere respuesta HTTP 200 para evitar reintentos automáticos del webhook.

> La URL de destino debe estar configurada previamente; sin configuración, no se recibirán notificaciones.

## Campos del Payload

| Campo | Tipo | Descripción |
|-------|------|-------------|
| `When` | datetime | Fecha/hora de envío notificación (UTC +0) |
| `Payload.TipoEvento` | string | Valor fijo: "PAGO" |
| `Payload.TipoOrigen` | string | Valor fijo: "ENTIDAD" |
| `Payload.IdentificadorDestino` | string | Código de la entidad del comercio |
| `Payload.IdMensaje` | string | ID guid de la notificación |
| `Payload.MensajePago.IdentificadorTransaccion` | string | ID de la transacción |
| `Payload.MensajePago.EstadoTransaccion` | string | "ACREDITADO" o "RECHAZADA" |
| `Payload.MensajePago.ImporteBruto` | decimal | Monto total pagado |
| `Payload.MensajePago.FormaPago` | string | TTDD, TTCC o TTPP |
| `Payload.MensajePago.Moneda` | string | Valor fijo: "ARS" |
| `Type` | string | Valor fijo: "PAGO" |

## Payload de Ejemplo

```json
{
    "When": "2026-06-10T00:23:41.6348564Z",
    "Payload": {
        "TipoEvento": "PAGO",
        "TipoOrigen": "ENTIDAD",
        "IdentificadorOrigen": "B",
        "TipoDestino": "COMERCIO",
        "IdentificadorDestino": "C02086",
        "DestinoPrincipal": "https://urldestino.com/webhook",
        "DestinoSecundario": "",
        "FechaEmision": "2026-06-10T00:23:39.5106685+00:00",
        "IdMensaje": "562e171a-9c70-45fc-94aa-656520a5df4f",
        "MensajePago": {
            "IdentificadorProcesador": "ERROR3422786",
            "IdentificadorTransaccion": "27109024",
            "IdentificadorOrdenVenta": "d5de60e9-72d5-425d-b3d3-1063c6bb4c33",
            "IdentificadorReferencia": "Reg-BS",
            "IdOrdenVentaQr": "",
            "TipoTransaccion": "BotonSimple",
            "RubroMovimiento": "BotonSimple",
            "FechaNegocio": "2026-06-09T21:23:39.0984647-03:00",
            "FechaProceso": "2026-06-09T21:23:39.196-03:00",
            "FormaPago": "TTCC",
            "Moneda": "ARS",
            "ImporteBruto": 120,
            "EstadoTransaccion": "RECHAZADA",
            "Retenciones": [],
            "Mcc": "56482",
            "Cpa": "C1006ACS",
            "Cuit": "30685029959",
            "CuentaVendedor": "0000000000000000000000",
            "IdentificadorVendedor": "CVU:0000164506600067020861WAL:|CBU:3220001881007553170113",
            "IdentificadorPagador": "",
            "CuentaPagador": "423985****4751",
            "CodigoComercio": "C02086",
            "CodigoSucursal": "S04399",
            "CodigoCaja": "B00000262146",
            "InformacionAdicionalPagador": [
                {"Descripcion": "dni", "Valor": "33929408"},
                {"Descripcion": "marca", "Valor": "VISA"},
                {"Descripcion": "cuotas", "Valor": "1"}
            ],
            "Entidad": "B",
            "Psp": "164",
            "Procesador": "DECIDIR",
            "InformacionAdicionalMensaje": [
                {"Descripcion": "idProvinciaSicore", "Valor": "00"},
                {"Descripcion": "motivoRechazo", "Valor": "Rechazada por Ardid (1001)"},
                {"Descripcion": "identificadorProcesadorTID", "Valor": ""}
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

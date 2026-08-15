# EVENT — Webhook: Aviso Transacción QR Dinámico (Deuda)

> Extraído el: 2026-06-30
> Fuente: https://psp.bind.com.ar/developers/apis/webhook-adqrdeuda
> Producto: Adquirencia > QR Dinámico

## Descripción

"Se envía una notificación a través de un HTTP POST cada vez que una se crea una transacción de canal QR en estado 'ACREDITADO' o 'RECHAZADO'."

Requiere respuesta con código HTTP 200; de lo contrario, entra en esquema de reintentos.

## ⚠️ Notas y Advertencias del Portal

> "No debe validarse la estructura del mensaje. Bind PSP puede agregar arbitrariamente nuevos atributos opcionales al request."

## Campos del Payload

| Campo | Tipo | Descripción |
|-------|------|-------------|
| `When` | datetime | Fecha/hora de envío (UTC +0) |
| `Payload.TipoEvento` | string | Valor fijo: "PAGO" |
| `Payload.TipoOrigen` | string | Valor fijo: "ENTIDAD" |
| `Payload.IdentificadorOrigen` | string | Código único de la Entidad |
| `Payload.DestinoPrincipal` | string | URL destino principal |
| `Payload.DestinoSecundario` | string | URL destino secundario |
| `Payload.FechaEmision` | datetime | Fecha/hora de envío (UTC +0) |
| `Payload.IdMensaje` | string | ID GUID de la notificación |
| `Payload.MensajePago.IdentificadorProcesador` | string | ID transacción en procesador externo |
| `Payload.MensajePago.IdentificadorTransaccion` | string | ID de la transacción |
| `Payload.MensajePago.ImporteBruto` | decimal | Monto total de transacción |
| `Payload.MensajePago.EstadoTransaccion` | string | "ACREDITADO" o "RECHAZADA" |
| `Payload.MensajePago.Moneda` | string | Valor fijo: "ARS" |
| `Payload.MensajePago.Cuit` | string | CUIT comercio |
| `Payload.MensajePago.IdentificadorPagador` | string | CUIT cliente |
| `Payload.MensajePago.MotivoRechazo` | string | Motivo de rechazo (si aplica) |
| `Type` | string | Valor fijo: "PAGO" |

## Payload de Ejemplo

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
            "ImporteBruto": 170000,
            "EstadoTransaccion": "ACREDITADO",
            "Moneda": "ARS",
            "Cuit": "30710345992",
            "IdentificadorPagador": "20213111931",
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

# Endpoint — Aviso de devolución de pago PIX (EVENT)

> Fuente: https://psp.bind.com.ar/developers/apis/webhook-devolucionpix
> Producto: Wallet — Pago QR PIX

## Descripción

Se envía una notificación a través de un HTTP POST cada vez que se registra una devolución por un pago PIX.

Cada webhook debe responderse simplemente con un HTTP code 200, así se considerará que la Entidad recibió la notificación satisfactoriamente. De otra manera, el envío del webhook ingresará en un esquema de reintentos.

El webhook se enviará a la URL del destino que se haya configurado previamente en la Entidad.

Para recibir este evento la organización debe tener parametrizada la URL destino para el tipo de evento `"DEVOLUCION_PAGO_PIX"`.

No debe validarse la estructura exacta del mensaje. Bind PSP puede agregar arbitrariamente nuevos atributos opcionales al request por nuevas funcionalidades o mejoras.

## Payload

| Campo | Tipo | Descripción |
|-------|------|-------------|
| `mensajeId` | string | Identificador del webhook. |
| `evento` | string | Tipo de evento. Valor fijo: `"DEVOLUCION_PAGO_PIX"` |
| `operacionId` | int | Identificador de la operación. |
| `operacionTipo` | string | Tipo de operación. Valor fijo: `"Devolucion Pago QR Pix"` |
| `operacionEstado` | string | Estado. Valores: `"Devuelta"`, `"Devuelta parcial"` |
| `cuentaId` | int | Identificador de la cuenta. |
| `importe` | double | Importe de la operación (en ARS). |
| `referencia` | string | Referencia de la operación. |
| `idExterno` | string | Identificador externo de la organización. |
| `idProcesador` | string | Identificador del procesador externo. |
| `montoBRL` | string | Monto en reales brasileños de la operación. |
| `idPix` | string | Identificador PIX de la operación. |
| `comprobanteId` | int | Comprobante del pago original. |
| `comprobanteDevolucionId` | int | Comprobante asociado a la devolución. |
| `fechaCreacion` | datetime | Fecha de creación de esta operación. |

## Ejemplo JSON

```json
{
  "mensajeId": "361c647b-fa1c-46cb-9ad2-16a234a989ab",
  "evento": "DEVOLUCION_PAGO_PIX",
  "operacionId": 1315670,
  "operacionTipo": "Devolucion Pago QR Pix",
  "operacionEstado": "Devuelta parcial",
  "cuentaId": 647859,
  "importe": 604.76,
  "referencia": "Pago QR Pix",
  "idExterno": "ABC794",
  "idProcesador": "3456cbb01a187ec0bb6c",
  "montoBRL": 11.50,
  "idPix": 4741,
  "comprobanteId": 12645386,
  "comprobanteDevolucionId": 12645388,
  "fechaCreacion": "2025-12-11T18:21:42.5591007+00:00"
}
```

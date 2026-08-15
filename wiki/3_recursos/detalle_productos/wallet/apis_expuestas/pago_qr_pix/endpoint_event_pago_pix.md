# Endpoint — Aviso de pago PIX (EVENT)

> Fuente: https://psp.bind.com.ar/developers/apis/webhook-pagopix
> Producto: Wallet — Pago QR PIX

## Descripción

Se envía una notificación a través de un HTTP POST cada vez que una operación de pago PIX obtiene un estado definitivo Aprobada o Rechazada.

Cada webhook debe responderse simplemente con un HTTP code 200, así se considerará que la Entidad recibió la notificación satisfactoriamente. De otra manera, el envío del webhook ingresará en un esquema de reintentos.

El webhook se enviará a la URL del destino que se haya configurado previamente en la Entidad.

Para recibir este evento la organización debe tener parametrizada la URL destino para el tipo de evento `"PAGO_PIX"`.

No debe validarse la estructura exacta del mensaje. Bind PSP puede agregar arbitrariamente nuevos atributos opcionales al request por nuevas funcionalidades o mejoras.

## Payload

| Campo | Tipo | Descripción |
|-------|------|-------------|
| `mensajeId` | string | Identificador del webhook. |
| `evento` | string | Tipo de evento. Valor fijo: `"PAGO_PIX"` |
| `operacionId` | int | Identificador de la operación. |
| `operacionTipo` | string | Nombre de tipo de operación. |
| `operacionEstado` | string | Estado. Valores: `"Aprobada"`, `"Rechazada"` |
| `cuentaId` | int | Identificador de la cuenta. |
| `importe` | double | Importe de la operación (en ARS). |
| `referencia` | string | Descripción de referencia de la operación. |
| `idExterno` | string | Identificador externo indicado por la organización. |
| `idProcesador` | string | Identificador del procesador externo. |
| `montoBRL` | string | Monto en reales brasileños pagado. |
| `idPix` | string | Identificador de la lectura PIX. |
| `comprobanteId` | int | Comprobante asociado a la operación. |
| `comprobanteDevolucionId` | int | Comprobante de reversa del saldo en caso de rechazo. |
| `fechaCreacion` | datetime | Fecha de creación de la operación. |
| `fechaActualizacion` | datetime | Fecha de última actualización. |

## Ejemplo JSON

```json
{
  "mensajeId": "523f6328-def7-4a93-8507-35cd65ac3b28",
  "evento": "PAGO_PIX",
  "operacionId": 1476542,
  "operacionTipo": "Pago QR Pix",
  "operacionEstado": "Aprobada",
  "cuentaId": 276363,
  "importe": 12.49,
  "referencia": "Pago QR Pix",
  "idExterno": "1779451462922550",
  "idProcesador": "732c21d93e2be632eff8",
  "montoBRL": 0.05,
  "idPix": 5649,
  "comprobanteId": 14015236,
  "comprobanteDevolucionId": null,
  "fechaCreacion": "2026-05-22T12:04:26.6257939+00:00",
  "fechaActualizacion": "2026-05-22T12:04:30.7727463+00:00"
}
```

# Endpoint — Aviso de pago de rendimiento (EVENT)

> Fuente: https://psp.bind.com.ar/developers/apis/webhook-rendimientofci
> Producto: Wallet — Cuenta remunerada

## Descripción

Se envía una notificación a través de un HTTP POST cada vez que se crea un comprobante de crédito para pagar el rendimiento diario de una cuenta por tener su saldo invertido en un fondo común de inversión por la funcionalidad de cuenta remunerada.

Cada webhook debe responderse simplemente con un HTTP code 200, así se considerará que la Entidad recibió la notificación satisfactoriamente. De otra manera, el envío del webhook ingresará en un esquema de reintentos.

El webhook se enviará a la URL del destino que se haya configurado previamente en la Entidad.

Para recibir este evento la organización debe tener parametrizada la URL destino para el tipo de evento `"RENDIMIENTOS_FCI"`.

No debe validarse la estructura del mensaje. Bind PSP puede agregar arbitrariamente nuevos atributos opcionales al request por nuevas funcionalidades o mejoras.

## Payload

| Campo | Tipo | Descripción |
|-------|------|-------------|
| `mensajeId` | string | Identificador único del webhook. |
| `evento` | string | Tipo de evento. Valor fijo: `"RENDIMIENTO_FCI"` |
| `cuentaId` | int | Identificador de la cuenta en la cual se creó el comprobante. |
| `importe` | double | Importe del comprobante. |
| `comprobanteId` | int | Identificador del comprobante creado. |
| `referencia` | string | Referencia del comprobante. |
| `tipoComprobanteId` | int | Identificador del tipo de comprobante. |

## Ejemplo JSON

```json
{
  "mensajeId": "537de36e-6d88-4218-a518-0435f384acb8",
  "evento": "RENDIMIENTO_FCI",
  "cuentaId": 274409,
  "importe": 6.78,
  "comprobanteId": 155555,
  "referencia": "",
  "tipoComprobanteId": 627
}
```

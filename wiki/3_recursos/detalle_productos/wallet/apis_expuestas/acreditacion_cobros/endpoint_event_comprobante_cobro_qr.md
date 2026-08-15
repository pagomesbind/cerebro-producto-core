# Endpoint — Aviso de cobro liquidado en cuenta (EVENT)

> Fuente: https://psp.bind.com.ar/developers/apis/webhook-walletcobro
> Producto: Wallet — Acreditación de cobros

## Descripción

Se envía una notificación a través de un HTTP POST cada vez que se crea un comprobante en una cuenta por un cobro con QR.

Este comprobante puede corresponder a un crédito por lo recaudado o a un débito por impuestos asociados a la transacción.

Cada webhook debe responderse simplemente con un HTTP code 200, así se considerará que la Entidad recibió la notificación satisfactoriamente. De otra manera, el envío del webhook ingresará en un esquema de reintentos.

El webhook se enviará a la URL del destino que se haya configurado previamente en la entidad.

La entidad también puede consultar estos tipos de comprobante creados con los endpoints de consultas de listados.

Para recibir este evento la organización debe tener parametrizada la URL destino para el tipo de evento `"COMPROBANTE_COBROQR"`.

No debe validarse la estructura exacta del mensaje. Bind PSP puede agregar arbitrariamente nuevos atributos opcionales al request por nuevas funcionalidades o mejoras.

## Payload

| Campo | Tipo | Descripción |
|-------|------|-------------|
| `mensajeId` | string | Identificador del webhook. |
| `evento` | string | Tipo de evento. Valor fijo: `"COMPROBANTE_COBROQR"` |
| `cuentaId` | int | Identificador de la cuenta. |
| `importe` | double | Importe de la operación. |
| `comprobanteId` | int | Identificador del comprobante. |
| `referencia` | string | Referencia del comprobante. |
| `tipoComprobanteId` | int | Identificador del tipo de comprobante. |
| `tipoComprobanteNombre` | string | Nombre del tipo de comprobante. |
| `tipoComprobanteSigno` | int | Signo del tipo de comprobante. |
| `fecha` | datetime | Fecha del comprobante. |

## Ejemplo JSON

```json
{
  "evento": "COMPROBANTE_COBROQR",
  "cuentaId": 648470,
  "importe": 0.02,
  "comprobanteId": 14147293,
  "referencia": "9OC114A473E15D3AB00000787849000000186840ET9LGW1TOC26943E1B1C",
  "tipoComprobanteId": 770,
  "tipoComprobanteNombre": "RET_IIBB_SIRTAC Impuesto por cobro",
  "tipoComprobanteSigno": -1,
  "fecha": "2026-05-28T15:23:33.9172797+00:00",
  "mensajeId": "a4a02c3c-04ba-423d-9f91-5bea5bbe9f7c"
}
```

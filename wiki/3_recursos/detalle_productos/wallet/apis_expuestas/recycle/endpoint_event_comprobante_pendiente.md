# Endpoint — Aviso de nuevo débito a reciclar (EVENT)

> Fuente: https://psp.bind.com.ar/developers/apis/webhook-comprobanteareciclar
> Producto: Wallet — Recycle

## Descripción

Se envía una notificación a través de un HTTP POST cada vez que un comprobante no se pudo debitar, entonces se registró como deuda pendiente de reciclar cuando la cuenta acredite saldo.

Cada webhook debe responderse simplemente con un HTTP code 200, así se considerará que la Entidad recibió la notificación satisfactoriamente. De otra manera, el envío del webhook ingresará en un esquema de reintentos.

El webhook se enviará a la URL del destino que se haya configurado previamente en la Entidad.

Para recibir este evento la organización debe tener parametrizada la URL destino para el tipo de evento `"COMPROBANTE_PENDIENTE_RECICLADO"`.

## Payload

| Campo | Tipo | Descripción |
|-------|------|-------------|
| `mensajeId` | string | Identificador único del webhook. |
| `evento` | string | Tipo de evento. Valor fijo: `"COMPROBANTE_PENDIENTE_RECICLADO"` |
| `cuentaId` | int | Identificador de la cuenta. |
| `importe` | double | Importe del comprobante. |
| `comprobanteId` | int | Identificador del comprobante. Es `null` porque aún no se creó el comprobante. |
| `comprobanteRelacionadoId` | int | Identificador del comprobante relacionado. |
| `referencia` | string | Referencia del comprobante. |
| `tipoComprobanteId` | int | Identificador del tipo de comprobante. |
| `tipoComprobanteCodigo` | string | Código del tipo de comprobante. |
| `tipoComprobanteNombre` | string | Nombre del tipo de comprobante. |
| `tipoComprobanteSigno` | int | Signo del tipo de comprobante. Valores: `1` = crédito, `-1` = débito |
| `fecha` | datetime | Fecha de creación del comprobante. Es `null` porque aún no se creó el comprobante. |
| `idRecycle` | int | Identificador del registro en el sistema de recycle. |
| `fechaInicioRecycle` | datetime | Fecha en que se intentó crear el comprobante y falló, registrándose como pendiente a reciclar. |

## Ejemplo JSON

```json
{
  "mensajeId": "325f20b8-ec33-468d-8114-6e3e72fd0b33",
  "evento": "COMPROBANTE_PENDIENTE_RECICLADO",
  "cuentaId": 278243,
  "importe": 222,
  "comprobanteId": null,
  "comprobanteRelacionadoId": 8570431,
  "referencia": "Contracargo operación debin 631617",
  "tipoComprobanteId": 1343,
  "tipoComprobanteCodigo": "DEBRECCRECON",
  "tipoComprobanteNombre": "Contracargo Debin Recurrente Crédito",
  "tipoComprobanteSigno": -1,
  "fecha": null,
  "recycleId": "1234451",
  "fechaHoraInicioRecycle": "2026-05-28T18:30:57.1861758+00:00"
}
```

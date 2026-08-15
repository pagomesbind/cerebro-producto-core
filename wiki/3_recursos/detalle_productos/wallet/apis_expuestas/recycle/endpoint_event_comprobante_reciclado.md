# Endpoint — Aviso de comprobante reciclado (EVENT)

> Fuente: https://psp.bind.com.ar/developers/apis/webhook-comprobantereciclado
> Producto: Wallet — Recycle

## Descripción

Se envía una notificación a través de un HTTP POST cada vez que se crea un comprobante a través del sistema de recycle.

Cada webhook debe responderse simplemente con un HTTP code 200, así se considerará que la Entidad recibió la notificación satisfactoriamente. De otra manera, el envío del webhook ingresará en un esquema de reintentos.

El webhook se enviará a la URL del destino que se haya configurado previamente en la Entidad.

Para recibir este evento la organización debe tener parametrizada la URL destino para el tipo de evento `"COMPROBANTE_RECICLADO"`.

No debe validarse la estructura exacta del mensaje. Bind PSP puede agregar arbitrariamente nuevos atributos opcionales al request por nuevas funcionalidades o mejoras.

## Payload

| Campo | Tipo | Descripción |
|-------|------|-------------|
| `mensajeId` | string | Identificador único del webhook. |
| `evento` | string | Tipo de evento. Valor fijo: `"COMPROBANTE_RECICLADO"` |
| `cuentaId` | int | Identificador de la cuenta en la cual se creó el comprobante. |
| `importe` | double | Importe del comprobante. |
| `comprobanteId` | int | Identificador del comprobante creado. |
| `comprobanteRelacionadoId` | int | Identificador del comprobante relacionado. |
| `referencia` | string | Referencia del comprobante. |
| `tipoComprobanteId` | int | Identificador del tipo de comprobante. |
| `codigoTipoComprobante` | string | Código del tipo de comprobante. |
| `tipoComprobanteNombre` | string | Nombre del tipo de comprobante. |
| `tipoComprobanteSigno` | int | Signo del tipo de comprobante. Valores: `1` = crédito, `-1` = débito |
| `fecha` | datetime | Fecha de creación del comprobante. |
| `idRecycle` | int | Identificador del registro en el sistema de recycle. |
| `fechaInicioRecycle` | datetime | Fecha en que se intentó crear el comprobante y falló, registrándose como pendiente a reciclar. |

## Ejemplo JSON

```json
{
  "idRecycle": "844c42b5-0356-4cc2-bd55-0c44eb8a5cd9",
  "fechaInicioRecycle": "2026-05-20T20:42:18.0550607+00:00",
  "comprobanteRelacionadoId": 14006792,
  "codigoTipoComprobante": "IMPD",
  "evento": "COMPROBANTE_RECICLADO",
  "cuentaId": 1506426,
  "importe": 41.75,
  "comprobanteId": 14014877,
  "referencia": "Impuesto por Comprobante 14006792",
  "tipoComprobanteId": 590,
  "tipoComprobanteNombre": "Retención Imp. al Débito",
  "tipoComprobanteSigno": -1,
  "fecha": "2026-05-22T03:02:32.4518351+00:00",
  "mensajeId": "466ee675-4666-4805-bb37-50bfac3989c6"
}
```

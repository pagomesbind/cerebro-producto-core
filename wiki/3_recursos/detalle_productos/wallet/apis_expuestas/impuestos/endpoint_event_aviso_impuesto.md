# Endpoint — Aviso de impuesto online (EVENT)

> Fuente: https://psp.bind.com.ar/developers/apis/webhook-impuestoonline
> Producto: Wallet — Impuestos

## Descripción

Se envía una notificación a través de un HTTP POST cada vez que se crea un comprobante de débito para retener un impuesto de una cuenta.

Cada webhook debe responderse simplemente con un HTTP code 200, así se considerará que la Entidad recibió la notificación satisfactoriamente. De otra manera, el envío del webhook ingresará en un esquema de reintentos.

El webhook se enviará a la URL del destino que se haya configurado previamente en la Entidad.

Para recibir este evento la organización debe tener parametrizada la URL destino para el tipo de evento `"COMPROBANTE_IMPUESTO_ONLINE"`.

## Payload

| Campo | Tipo | Descripción |
|-------|------|-------------|
| `mensajeId` | string | Identificador único del webhook. |
| `evento` | string | Tipo de evento. Valor fijo: `"COMPROBANTE_IMPUESTO_ONLINE"` |
| `cuentaId` | int | Identificador de la cuenta en la cual se creó el comprobante. |
| `importe` | double | Importe del comprobante. |
| `comprobanteId` | int | Identificador del comprobante creado. |
| `comprobanteRelacionadoId` | int | Comprobante original por el que se generó este impuesto. |
| `referencia` | string | Referencia del comprobante. |
| `tipoComprobanteId` | int | Identificador del tipo de comprobante. |
| `codigoTipoComprobante` | string | Código del tipo de comprobante. |
| `tipoComprobanteNombre` | string | Nombre del tipo de comprobante. |
| `tipoComprobanteSigno` | int | Signo. Valores: `1` = crédito, `-1` = débito |
| `fecha` | datetime | Fecha de creación del comprobante. |

## Ejemplo JSON

```json
{
  "comprobanteRelacionadoId": 14147439,
  "codigoTipoComprobante": "SIRCUPA",
  "evento": "COMPROBANTE_IMPUESTO_ONLINE",
  "cuentaId": 1506528,
  "importe": 5.6000,
  "comprobanteId": 14147441,
  "referencia": "Impuesto por Comprobante 14147439",
  "tipoComprobanteId": 592,
  "tipoComprobanteNombre": "Retención SIRCUPA",
  "tipoComprobanteSigno": -1,
  "fecha": "2026-05-28T18:16:50.587342+00:00",
  "mensajeId": "bfc711be-b4c7-46fb-911c-b97f6ea4a507"
}
```

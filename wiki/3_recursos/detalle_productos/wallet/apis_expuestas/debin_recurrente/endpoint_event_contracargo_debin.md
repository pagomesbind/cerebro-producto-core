# Endpoint — Aviso de contracargo DEBIN (EVENT)

> Fuente: https://psp.bind.com.ar/developers/apis/webhook-contracargodebin
> Producto: Wallet — Debin recurrente

## Descripción

Se envía una notificación a través de un HTTP POST cada vez que se registra una actualización en un contracargo por una operación de debin recurrente.

El contracargo se avisará por más que no se haya podido debitar el saldo.

Cada webhook debe responderse simplemente con un HTTP code 200, así se considerará que la Entidad recibió la notificación satisfactoriamente. De otra manera, el envío del webhook ingresará en un esquema de reintentos.

El webhook se enviará a la URL del destino que se haya configurado previamente en la Entidad.

Para recibir este evento la organización debe tener parametrizada la URL destino para el tipo de evento `"CONTRACARGO_DEBIN_ENTRANTE"`.

No debe validarse la estructura exacta del mensaje. Bind PSP puede agregar arbitrariamente nuevos atributos opcionales al request por nuevas funcionalidades o mejoras.

## Payload

| Campo | Tipo | Descripción |
|-------|------|-------------|
| `mensajeId` | string | Identificador del mensaje. |
| `evento` | string | Tipo de evento. Valor fijo: `"CONTRACARGO_DEBIN_ENTRANTE"` |
| `operacionId` | int | Identificador de la operación. |
| `operacionTipo` | string | Tipo de operación. Valor fijo: `"DebinRecurrenteCredito"` |
| `operacionEstado` | string | Estado. Valores: `"Devuelta"`, `"Devuelta parcial"`, `"Devolución pendiente"` |
| `cuentaId` | int | Identificador de la cuenta. |
| `importe` | double | Importe de la operación. |
| `nombreContraparte` | string | Nombre del titular de la cuenta contraparte. |
| `bancoContraparte` | string | Código del banco o entidad financiera de la cuenta contraparte. |
| `referencia` | string | Referencia indicada en la creación de la operación. |
| `cuitContraparte` | string | CUIT/CUIL del titular de la cuenta contraparte. |
| `cvuCbuContraparte` | string | CBU/CVU de la cuenta contraparte. |
| `aliasContraparte` | string | Alias de la cuenta contraparte. |
| `coelsaId` | string | Identificador de Coelsa del DEBIN original. |
| `idExterno` | string | Identificador externo indicado por la organización. |
| `motivoRechazo` | string | Motivo de rechazo (si aplica). |
| `comprobanteId` | int | Comprobante principal del ajuste de saldo. |
| `contracargo` | object | Información sobre el contracargo. |
| `contracargo.coelsaId` | string | Identificador de Coelsa del contracargo. |
| `contracargo.comprobantes` | array | Comprobantes de débito creados para recuperar el importe. Puede estar vacío si no se pudo debitar. |
| `contracargo.comprobantes[].importe` | decimal | Importe del comprobante. |
| `contracargo.comprobantes[].comprobanteId` | int | Identificador del comprobante. |
| `contracargo.comprobantes[].fechaCreacion` | datetime | Fecha de creación del comprobante. |
| `fechaCreacion` | datetime | Fecha de creación del DEBIN original. |
| `fechaActualizacion` | datetime | Fecha de última actualización. |

## Ejemplo JSON

```json
{
  "mensajeId": "2b1bfe8e-8860-4ce8-a7a2-831329b7c47d",
  "evento": "CONTRACARGO_DEBIN_ENTRANTE",
  "operacionId": 632174,
  "operacionTipo": "DebinRecurrenteCredito",
  "operacionEstado": "Devuelta",
  "cuentaId": 278301,
  "importe": 10.0,
  "nombreContraparte": "JOSE PEREZ",
  "bancoContraparte": "322",
  "referencia": "Debin",
  "cuitContraparte": null,
  "cvuCbuContraparte": "3220001823007351920015",
  "aliasContraparte": null,
  "coelsaId": "4XJ8G7V95PPQX4D9EMPYR0",
  "idExterno": "DebinPrueba22042568",
  "motivoRechazo": null,
  "comprobanteId": 8580777,
  "contracargo": {
    "coelsaId": "4XJ8G7V95PPQX4D9EMPYR0",
    "comprobantes": [
      {
        "importe": 0.05,
        "comprobanteId": 13905871,
        "fechaCreacion": "2026-04-28T13:44:36.7786281+00:00"
      },
      {
        "importe": 9.95,
        "comprobanteId": 13905879,
        "fechaCreacion": "2026-04-28T13:49:49.173214+00:00"
      }
    ]
  },
  "fechaCreacion": "2025-04-22T20:03:52.6593888+00:00",
  "fechaActualizacion": "2026-04-28T13:49:49.3253957+00:00"
}
```

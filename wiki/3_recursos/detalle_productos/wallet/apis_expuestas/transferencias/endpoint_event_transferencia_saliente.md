# Endpoint — Aviso de transferencia saliente (EVENT)

> Fuente: https://psp.bind.com.ar/developers/apis/webhook-transferenciasaliente
> Producto: Wallet — Transferencias

## Descripción

Se envía una notificación a través de un HTTP POST cada vez que una operación de tipo transferencia saliente pasa a un estado definitivo.

Cada webhook debe responderse simplemente con un HTTP code 200, así se considerará que la Entidad recibió la notificación satisfactoriamente. De otra manera, el envío del webhook ingresará en un esquema de reintentos.

El webhook se enviará a la URL del destino que se haya configurado previamente en la Entidad.

Para recibir este evento la organización debe tener parametrizada la URL destino para el tipo de evento `"TRANSFERENCIA_SALIENTE"` y `"TRANSFERENCIA_SALIENTE_INTERNA"`.

## Payload

| Campo | Tipo | Descripción |
|-------|------|-------------|
| `mensajeId` | string | Identificador del mensaje. |
| `evento` | string | Tipo de evento. Valores: `"TRANSFERENCIA_SALIENTE"`, `"TRANSFERENCIA_SALIENTE_INTERNA"` |
| `operacionId` | int | Identificador de la operación. |
| `operacionTipo` | string | Nombre de tipo de operación. Valores: `"TransferenciaSaliente"`, `"TransferenciaSalienteInterna"` |
| `operacionEstado` | string | Estado de la operación. Valores: `"Aprobada"`, `"Rechazada"` |
| `cuentaId` | int | Identificador de la cuenta. |
| `importe` | double | Valor del importe de la operación. |
| `nombreContraparte` | string | Nombre del titular de la cuenta contraparte. |
| `bancoContraparte` | string | Código del banco o entidad financiera contraparte. |
| `referencia` | string | Descripción de referencia indicada en la creación de la operación. |
| `cuitContraparte` | string | CUIT/CUIL del titular de la cuenta contraparte. |
| `cvuCbuContraparte` | string | CBU/CVU de la cuenta contraparte. |
| `aliasContraparte` | string | Alias de la cuenta contraparte. |
| `coelsaId` | string | Identificador de Coelsa de la operación. |
| `idExterno` | string | Identificador externo de la operación indicado por la organización. |
| `motivoRechazo` | string | Descripción del motivo en caso de rechazo. |
| `comprobanteId` | int | Identificador del comprobante principal del ajuste de saldo. |
| `comprobanteDevolucionId` | int | Identificador del comprobante de crédito por reversa (en caso de rechazo). |
| `fechaCreacion` | datetime | Fecha y hora en que se creó la operación. |
| `fechaActualizacion` | datetime | Fecha y hora de la última actualización. |

## Ejemplo JSON

```json
{
  "mensajeId": "3be24d8b-bd4b-49ff-840f-7006390abab2",
  "evento": "TRANSFERENCIA_SALIENTE",
  "operacionId": 1484252,
  "operacionTipo": "TransferenciaSaliente",
  "operacionEstado": "Rechazada",
  "cuentaId": 274409,
  "importe": 6403,
  "nombreContraparte": "BIND PAGO",
  "bancoContraparte": "322",
  "referencia": null,
  "cuitContraparte": "30717449076",
  "cvuCbuContraparte": "3220001812007351350612",
  "aliasContraparte": null,
  "coelsaId": null,
  "idExterno": null,
  "motivoRechazo": "Moneda del vendedor diferente a la requerida",
  "comprobanteId": 14147455,
  "comprobanteDevolucionId": 14147457,
  "fechaCreacion": "2026-05-28T18:19:53.727938+00:00",
  "fechaActualizacion": "2026-05-28T18:20:03.7507848+00:00"
}
```

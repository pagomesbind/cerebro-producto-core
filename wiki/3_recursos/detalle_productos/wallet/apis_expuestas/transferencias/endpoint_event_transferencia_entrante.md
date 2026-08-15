# Endpoint — Aviso de transferencia entrante (EVENT)

> Fuente: https://psp.bind.com.ar/developers/apis/webhook-transferenciaentrante
> Producto: Wallet — Transferencias

## Descripción

Se envía una notificación a través de un HTTP POST cada vez que una operación de tipo transferencia entrante pasa a un estado definitivo.

Cada webhook debe responderse simplemente con un HTTP code 200, así se considerará que la Entidad recibió la notificación satisfactoriamente. De otra manera, el envío del webhook ingresará en un esquema de reintentos.

El webhook se enviará a la URL del destino que se haya configurado previamente en la Entidad.

Para recibir este evento la organización debe tener parametrizada la URL destino para el tipo de evento `"TRANSFERENCIA_ENTRANTE"` y `"TRANSFERENCIA_INTERNA_ENTRANTE"`.

## Payload

| Campo | Tipo | Descripción |
|-------|------|-------------|
| `mensajeId` | string | Identificador del mensaje. |
| `evento` | string | Tipo de evento. Valores: `"TRANSFERENCIA_ENTRANTE"`, `"TRANSFERENCIA_ENTRANTE_INTERNA"` |
| `operacionId` | int | Identificador de la operación. |
| `operacionTipo` | string | Nombre de tipo de operación. Valores: `"TransferenciaEntrante"`, `"TransferenciaEntranteInterna"` |
| `operacionEstado` | string | Estado de la operación. Valores: `"Aprobada"` |
| `cuentaId` | int | Identificador de la cuenta. |
| `importe` | double | Valor del importe de la operación. |
| `nombreContraparte` | string | Nombre del titular de la cuenta contraparte. |
| `bancoContraparte` | string | Código del banco o entidad financiera contraparte. |
| `referencia` | string | Descripción de referencia de la operación. |
| `cuitContraparte` | string | CUIT/CUIL del titular de la cuenta contraparte. |
| `cvuCbuContraparte` | string | CBU/CVU de la cuenta contraparte. |
| `aliasContraparte` | string | Alias de la cuenta contraparte. |
| `coelsaId` | string | Identificador de Coelsa de la operación. |
| `idExterno` | string | Identificador externo de la operación indicado por la organización. |
| `motivoRechazo` | string | Descripción del motivo en caso de rechazo. |
| `comprobanteId` | int | Identificador del comprobante principal del ajuste de saldo. |
| `comprobanteDevolucionId` | int | Identificador del comprobante de crédito por reversa. Para transferencias entrantes, siempre será `null`. |
| `fechaCreacion` | datetime | Fecha y hora en que se creó la operación. |
| `fechaActualizacion` | datetime | Fecha y hora de la última actualización. |

## Ejemplo JSON

```json
{
  "mensajeId": "b334eb59-d6c3-4ec7-a924-4cedc6bf4963",
  "evento": "TRANSFERENCIA_ENTRANTE",
  "operacionId": 1484255,
  "operacionTipo": "TransferenciaEntrante",
  "operacionEstado": "Aprobada",
  "cuentaId": 274409,
  "importe": 200,
  "nombreContraparte": "BIND PAGOS SA",
  "bancoContraparte": "322",
  "referencia": null,
  "cuitContraparte": "30717449076",
  "cvuCbuContraparte": "3220001805007351350083",
  "aliasContraparte": null,
  "coelsaId": "76V4MR2Z181EJZYNDEZOL1",
  "idExterno": null,
  "motivoRechazo": null,
  "comprobanteId": 14147460,
  "comprobanteDevolucionId": null,
  "fechaCreacion": "2026-05-28T18:25:05.8260503+00:00",
  "fechaActualizacion": "2026-05-28T18:25:05.8260503+00:00"
}
```

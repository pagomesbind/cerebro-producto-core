# Endpoint — Aviso de pago QR (EVENT)

> Fuente: https://psp.bind.com.ar/developers/apis/webhook-pagoqr
> Producto: Wallet — Pago QR

## Descripción

Se envía una notificación a través de un HTTP POST cada vez que una operación de tipo pago QR es exitosa o rechazada.

Cada webhook debe responderse simplemente con un HTTP code 200, así se considerará que la Entidad recibió la notificación satisfactoriamente. De otra manera, el envío del webhook ingresará en un esquema de reintentos.

El webhook se enviará a la URL del destino que se haya configurado previamente en la Entidad.

Para recibir este evento la organización debe tener parametrizada la URL destino para el tipo de evento `"PAGO_QR"`.

## Payload

| Campo | Tipo | Descripción |
|-------|------|-------------|
| `mensajeId` | string | Identificador del mensaje. |
| `evento` | string | Tipo de evento. Valor fijo: `"PAGO_QR"` |
| `operacionId` | int | Identificador de la operación. |
| `operacionTipo` | string | Tipo de operación. Valor fijo: `"PagoConQR"` |
| `operacionEstado` | string | Estado. Valores: `"Aprobada"`, `"Rechazada"` |
| `cuentaId` | int | Identificador de la cuenta. |
| `importe` | double | Importe de la operación. |
| `nombreContraparte` | string | Nombre del comercio contraparte. |
| `bancoContraparte` | string | Código del banco contraparte. |
| `referencia` | string | Referencia de la operación. |
| `cuitContraparte` | string | CUIT del comercio contraparte. |
| `cvuCbuContraparte` | string | CBU/CVU del comercio contraparte. |
| `aliasContraparte` | string | Alias de la cuenta contraparte. |
| `coelsaId` | string | Identificador de Coelsa. |
| `idExterno` | string | Identificador externo de la organización. |
| `motivoRechazo` | string | Motivo en caso de rechazo. |
| `comprobanteId` | int | Comprobante principal del ajuste de saldo. |
| `comprobanteDevolucionId` | int | Comprobante de crédito por reversa (si fue rechazado). |
| `fechaCreacion` | datetime | Fecha y hora de creación. |
| `fechaActualizacion` | datetime | Fecha y hora de última actualización. |

## Ejemplo JSON

```json
{
  "mensajeId": "70ed5918-d8b1-486f-a7be-fb83cb35bd44",
  "evento": "PAGO_QR",
  "operacionId": 1484256,
  "operacionTipo": "PagoConQR",
  "operacionEstado": "Aprobada",
  "cuentaId": 650225,
  "importe": 4886,
  "nombreContraparte": "Boton Simple DosCero",
  "bancoContraparte": "0531",
  "referencia": "string",
  "cuitContraparte": "20322678275",
  "cvuCbuContraparte": "0000531908320067229030",
  "aliasContraparte": null,
  "coelsaId": "86VRPQ2GDXDR7KG2GLY0M1",
  "idExterno": null,
  "motivoRechazo": null,
  "comprobanteId": 14147461,
  "comprobanteDevolucionId": null,
  "fechaCreacion": "2026-05-28T18:30:49.7729164+00:00",
  "fechaActualizacion": "2026-05-28T18:30:49.7729164+00:00"
}
```

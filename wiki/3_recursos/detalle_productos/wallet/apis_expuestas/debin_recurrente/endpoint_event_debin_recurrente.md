# Endpoint — Aviso de DEBIN recurrente (EVENT)

> Fuente: https://psp.bind.com.ar/developers/apis/webhook-debinrecurrente
> Producto: Wallet — Debin recurrente

## Descripción

Se envía una notificación a través de un HTTP POST cada vez que una operación de tipo DEBIN recurrente pasa a un estado definitivo.

Cada webhook debe responderse simplemente con un HTTP code 200, así se considerará que la Entidad recibió la notificación satisfactoriamente. De otra manera, el envío del webhook ingresará en un esquema de reintentos.

El webhook se enviará a la URL del destino que se haya configurado previamente en la Entidad.

Para recibir este evento la organización debe tener parametrizada la URL destino para el tipo de evento `"DEBIN_RECURRENTE_CREDITO"`.

## Payload

| Campo | Tipo | Descripción |
|-------|------|-------------|
| `mensajeId` | string | Identificador del mensaje. |
| `evento` | string | Tipo de evento. Valor fijo: `"DEBIN_RECURRENTE_CREDITO"` |
| `operacionId` | int | Identificador de la operación. |
| `operacionTipo` | string | Tipo de operación. Valor fijo: `"DebinRecurrenteCredito"` |
| `operacionEstado` | string | Estado. Valores: `"Aprobada"`, `"Rechazada"` |
| `cuentaId` | int | Identificador de la cuenta. |
| `importe` | double | Importe de la operación. |
| `referencia` | string | Referencia indicada en la creación. |
| `idExterno` | string | Identificador externo de la organización. |

## Ejemplo JSON

```json
{
  "mensajeId": "c56c3b5b-1d6b-414f-80c7-b8667fc568b3",
  "evento": "DEBIN_RECURRENTE_CREDITO",
  "operacionId": 631776,
  "operacionTipo": "DebinRecurrenteCredito",
  "operacionEstado": "Rechazada",
  "cuentaId": 278259,
  "importe": 20000.00,
  "referencia": "DebinPruebaNueva2",
  "idExterno": "Prueba1"
}
```

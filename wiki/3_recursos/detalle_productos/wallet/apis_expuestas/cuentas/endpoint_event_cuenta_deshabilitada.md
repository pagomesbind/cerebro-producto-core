# Endpoint — Aviso de cuenta deshabilitada (EVENT)

> Fuente: https://psp.bind.com.ar/developers/apis/webhook-cuentadeshabilitada
> Producto: Wallet — Cuentas

## Descripción

Se envía una notificación a través de un HTTP POST cada vez que el sistema deshabilita una cuenta de manera automática.

Cada webhook debe responderse simplemente con un HTTP code 200, así se considerará que la Entidad recibió la notificación satisfactoriamente. De otra manera, el envío del webhook ingresará en un esquema de reintentos.

El webhook se enviará a la URL del destino que se haya configurado previamente en la Entidad.

Para recibir este evento la organización debe tener parametrizada la URL destino para el tipo de evento "DESHABILITAR_CUENTA".

## Payload

| Campo | Tipo | Descripción |
|-------|------|-------------|
| `mensajeId` | string | Identificador del mensaje. |
| `evento` | string | Tipo de evento. Valor fijo: `"DESHABILITAR_CUENTA"` |
| `motivo` | string | Código que identifica el motivo de la deshabilitación. Valores posibles: `"CONTRACARGO_DEBIN_PENDIENTE"`. Bind PSP puede agregar nuevos valores posibles según desarrolle nuevas casuísticas de deshabilitación automática. |
| `cuentaId` | int | Identificador de la cuenta. |
| `mensaje` | string | Mensaje descriptivo que explica con detalle el motivo de la deshabilitación. |

## Ejemplo JSON

```json
{
  "mensajeId": "09cc5f38-dfd5-47e3-b553-ac5dd6397332",
  "evento": "DESHABILITAR_CUENTA",
  "motivo": "CONTRACARGO_DEBIN_PENDIENTE",
  "cuentaId": 278243,
  "mensaje": "La cuenta con Id 278243 se ha deshabilitado debido a que recibió un contracargo de debin (operacion con id 631617) y no tiene saldo suficiente."
}
```

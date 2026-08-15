# GET — Consultar Devolución (QR Estático)

> Sincronizado el: 2026-06-30
> Fuente: https://psp.bind.com.ar/developers/apis/consultarcontracargo
> Producto: Adquirencia > QR Estático

## Descripción

Devuelve la información de un contracargo.

## Request

**Método HTTP:** `GET`
**Path:** `/bindentidad-transaccionquery-v2/v2/api/v1/contracargos/{Id}`
**Base URL Staging:** `https://gw-staging-qrbind.epays.services`
**URL Completa Staging:** `https://gw-staging-qrbind.epays.services/bindentidad-transaccionquery-v2/v2/api/v1/contracargos/{Id}`

### Headers

| Header | Valor |
|--------|-------|
| `Authorization` | `Bearer {{access_token}}` |
| `Cache-Control` | `no-cache` |

### Parámetros de Path

| Parámetro | Tipo | Requerido | Descripción |
|-----------|------|-----------|-------------|
| `Id` | int | REQUERIDO | Identificador del contracargo a consultar. |

## curl request

```bash
curl --location 'https://gw-staging-qrbind.epays.services/bindentidad-transaccionquery-v2/v2/api/v1/contracargos/3226' \
--header 'Cache-Control: no-cache' \
--header 'Authorization: Bearer {{access_token}}'
```

## Response

### Campos de respuesta exitosa (200)

| Campo | Tipo | Descripción |
|-------|------|-------------|
| `id` | int | Id del Contracargo. |
| `transaccionId` | int | Id de la Transacción contracargada relacionada. |
| `fechaNegocioOrigen` | string | Fecha y hora en que se realizó el Contracargo. |
| `importeContracargo` | decimal | Monto del Contracargo. |
| `motivoContracargo` | string | Razón por el cual se realizó el Contracargo. |
| `importeTransaccion` | decimal | Monto total original de la Transacción. |
| `parcial` | boolean | Indica si el Contracargo se hizo por el monto total o parcial con respecto a la Transacción original o su restante (más de un contracargo parcial). |
| `tipo` | string | Valor fijo: `"contracargo"` |
| `estado` | string | Indica el estado del Contracargo. Valores posibles: `"PENDIENTE"`, `"APROBADO"`, `"RECHAZADO"` |
| `motivoRechazo` | string | Se identifica la razón por la cual el Contracargo ha fallado, en caso de que el estado sea `"RECHAZADO"`. |
| `vendedorCuit` | string | CUIT del Comercio que ha recibido la Transacción. |
| `vendedorCbu` | string | CBU/CVU del Comercio que ha recibido la Transacción. |
| `idDebin` | string | Id Coelsa con el que se ha realizado la devolución final de cara al cliente pagador. |
| `debinIdApiBank` | string | Id Coelsa (Debin) con el cual se le debitan los fondos al Comercio y se acreditan en la cuenta recaudadora de BindPsp (exclusivo para QR Split). |
| `usuario` | string | Usuario que ha realizado la devolución. |

### Errores

| Descripción |
|-------------|
| Token de autenticación inválido |

# GET — Consultar Devolución (QR Dinámico)

> Extraído el: 2026-06-30
> Fuente: https://psp.bind.com.ar/developers/apis/consultarcontracargo-copy-copy
> Producto: Adquirencia > QR Dinámico

## Descripción

"Devuelve la información de un contracargo."

El endpoint permite consultar datos específicos asociados a una devolución mediante su identificador único.

## Request

**Método HTTP:** `GET`
**URL:** `https://gw-staging-qrbind.epays.services/bindentidad-transaccionquery-v2/v2/api/v1/contracargos/{Id}`

### curl request

```bash
curl --location 'https://gw-staging-qrbind.epays.services/bindentidad-transaccionquery-v2/v2/api/v1/contracargos/3226' \
--header 'Cache-Control: no-cache' \
--header 'Authorization: Bearer {{access_token}}'
```

### Headers

| Header | Valor |
|--------|-------|
| `Cache-Control` | `no-cache` |
| `Authorization` | `Bearer {{access_token}}` |

### Path Parameters

| Parámetro | Tipo | Requerido | Descripción |
|-----------|------|-----------|-------------|
| `Id` | int | SÍ | "Identificador del contracargo a consultar" |

## Response

### Respuesta exitosa (200)

Campos principales del response:

| Campo | Tipo | Descripción |
|-------|------|-------------|
| `id` | int | ID del contracargo |
| `transaccionId` | int | ID de la transacción original |
| `fechaNegocioOrigen` | datetime | Fecha de la transacción original |
| `importeContracargo` | decimal | Monto devuelto |
| `motivoContracargo` | string | Motivo de la devolución |
| `importeTransaccion` | decimal | Monto original de la transacción |
| `parcial` | boolean | Si es devolución parcial |
| `tipo` | string | Tipo de contracargo |
| `estado` | string | PENDIENTE, APROBADO o RECHAZADO |
| `motivoRechazo` | string | Motivo de rechazo (si aplica) |
| `vendedorCuit` | string | CUIT del comercio |
| `vendedorCbu` | string | CBU del comercio |
| `idDebin` | string | ID del DEBIN asociado |
| `debinIdApiBank` | string | ID ApiBank del DEBIN |
| `usuario` | string | Usuario que efectuó la devolución |

### Códigos de estado HTTP

| Código | Descripción |
|--------|-------------|
| `200` | Consulta exitosa |
| `401` | Token de autenticación inválido |

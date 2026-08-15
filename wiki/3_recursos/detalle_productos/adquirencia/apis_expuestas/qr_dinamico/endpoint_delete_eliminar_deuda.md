# DELETE — Eliminar Deuda (QR Dinámico)

> Extraído el: 2026-06-30
> Fuente: https://psp.bind.com.ar/developers/apis/deuda-eliminar
> Producto: Adquirencia > QR Dinámico

## Descripción

"Elimina una deuda. Una deuda eliminada no puede ser pagada."

## Request

**Método HTTP:** `DELETE`
**URL:** `https://gw-staging-qrbind.epays.services/bindentidad-deuda-v2/v2/api/v1.201/Deuda/{id}`

### curl request

```bash
curl -v -X DELETE "https://gw-staging-qrbind.epays.services/bindentidad-deuda-v2/v2/api/v1.201/Deuda/12356" -H "Authorization: Bearer {{access_token}}"
```

### Headers

| Header | Valor |
|--------|-------|
| `Authorization` | `Bearer {{access_token}}` |

### Path Parameters

| Parámetro | Tipo | Requerido | Descripción |
|-----------|------|-----------|-------------|
| `id` | int | SÍ | Identificador del registro de deuda |

## Response

### Respuesta exitosa (200)

| Campo | Tipo | Descripción |
|-------|------|-------------|
| `id` | int | Identificador del registro eliminado |

### Códigos de estado HTTP

| Código | Descripción |
|--------|-------------|
| `200` | Operación exitosa |
| `401` | Autenticación fallida |

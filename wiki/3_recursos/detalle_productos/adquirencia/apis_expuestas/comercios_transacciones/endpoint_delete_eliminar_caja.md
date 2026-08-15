# DELETE — Eliminar Caja (Comercios y Transacciones)

> Extraído el: 2026-06-30
> Fuente: https://psp.bind.com.ar/developers/apis/comercio-eliminarcaja
> Producto: Adquirencia > Comercios y Transacciones

## Descripción

"Elimina una caja existente."

## Request

**Método HTTP:** `DELETE`
**URL:** `https://gw-staging-qrbind.epays.services/bindentidad-comercio-v2/v2/api/v1.201/comercios/{id}/sucursales/{idSucursal}/cajas/{idCaja}`

### curl request

```bash
curl -v -X DELETE "https://gw-staging-qrbind.epays.services/bindentidad-comercio-v2/v2/api/v1.201/comercios/C07663/sucursales/S02825/cajas/B00000455197" -H "Authorization: Bearer {{access_token}}"
```

### Headers

| Header | Valor |
|--------|-------|
| `Authorization` | `Bearer {{access_token}}` |

### Path Parameters

| Parámetro | Tipo | Requerido | Descripción |
|-----------|------|-----------|-------------|
| `id` | string | SÍ | "código del comercio de la caja que se quiere eliminar" |
| `idSucursal` | string | SÍ | "código de la sucursal de la caja que se quiere eliminar" |
| `idCaja` | string | SÍ | "código de la caja que se quiere eliminar" |

## Response

Respuesta vacía (sin contenido en body).

### Códigos de estado HTTP

| Código | Descripción |
|--------|-------------|
| `204` | Eliminación exitosa |
| `404` | "Comercio o sucursal inválidos" |
| `401` | "Token de autenticación inválido" |

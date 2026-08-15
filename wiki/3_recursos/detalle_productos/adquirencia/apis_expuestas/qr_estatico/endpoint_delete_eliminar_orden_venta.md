# DELETE — Eliminar Orden de Venta (QR Estático)

> Sincronizado el: 2026-06-30
> Fuente: https://psp.bind.com.ar/developers/apis/qr-eliminarordendeventaenqr
> Producto: Adquirencia > QR Estático

## Descripción

Eliminar una orden de venta.

## Request

**Método HTTP:** `DELETE`
**Path:** `/bindentidad-transaction-v2/v2/api/v1.201/orden-venta/{IdOrdenVenta}`
**Base URL Staging:** `https://gw-staging-qrbind.epays.services`
**URL Completa Staging:** `https://gw-staging-qrbind.epays.services/bindentidad-transaction-v2/v2/api/v1.201/orden-venta/{IdOrdenVenta}`

### Headers

| Header | Valor |
|--------|-------|
| `Authorization` | `Bearer {{access_token}}` |

### Parámetros de Path

| Parámetro | Tipo | Requerido | Descripción |
|-----------|------|-----------|-------------|
| `IdOrdenVenta` | int | REQUIRED | Es el Id de la orden de venta. Es el id que devuelve el servicio al crear una orden de venta. |

## curl request

```bash
curl -v -X DELETE "https://gw-staging-qrbind.epays.services/bindentidad-transaction-v2/v2/api/v1.201/orden-venta/55026" -H "Authorization: Bearer {{access_token}}"
```

## Response

### Respuesta exitosa (200)

Respuesta vacía.

### Errores

| Descripción |
|-------------|
| La orden de venta ya se encuentra rechazada |
| Orden de venta inválida |
| Token de autenticación inválido |

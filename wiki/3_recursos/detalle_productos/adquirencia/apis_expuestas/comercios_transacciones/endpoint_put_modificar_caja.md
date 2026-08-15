# PUT — Modificar Caja (Comercios y Transacciones)

> Extraído el: 2026-06-30
> Fuente: https://psp.bind.com.ar/developers/apis/comercio-modificarcaja
> Producto: Adquirencia > Comercios y Transacciones

## Descripción

"Modifica atributos de una caja existente."

Nota: la documentación sugiere que esta funcionalidad puede no ser necesaria si se utilizan configuraciones fijas.

## Request

**Método HTTP:** `PUT`
**URL:** `https://gw-staging-qrbind.epays.services/bindentidad-comercio-v2/v2/api/v1.201/comercios/{id}/sucursales/{idSucursal}/cajas/{idCaja}`

### curl request

```bash
curl -v -X PUT "https://gw-staging-qrbind.epays.services/bindentidad-comercio-v2/v2/api/v1.201/comercios/C07663/sucursales/S02825/cajas/B00000455197" \
-H "Content-Type: application/json" \
-H "Cache-Control: no-cache" \
-H "Authorization: Bearer {{access_token}}" \
--data-raw "{\"soloOrden\": false, \"nombre\": \"Nombre de caja cambiado\", \"tipoCajaId\": 2}"
```

### Headers

| Header | Valor |
|--------|-------|
| `Content-Type` | `application/json` |
| `Cache-Control` | `no-cache` |
| `Authorization` | `Bearer {{access_token}}` |

### Path Parameters

| Parámetro | Tipo | Requerido | Descripción |
|-----------|------|-----------|-------------|
| `id` | string | SÍ | "Es el código del comercio de la caja que se quiere modificar" |
| `idSucursal` | string | SÍ | "Es el código de la sucursal de la caja que se quiere modificar" |
| `idCaja` | string | SÍ | "Es el código de la caja que se quiere modificar" |

### Body

| Parámetro | Tipo | Requerido | Descripción |
|-----------|------|-----------|-------------|
| `nombre` | string | NO | Denominación de la caja |
| `soloOrden` | boolean | SÍ | Acepta cobros sin órdenes: true/false |
| `tipoCajaId` | int | NO | 1 (físico) o 2 (e-commerce). Defecto: 1 |

### Request JSON

```json
{
    "soloOrden": false,
    "nombre": "Nombre de caja cambiado",
    "tipoCajaId": 2
}
```

## Response

Respuesta sin contenido.

### Códigos de estado HTTP

| Código | Descripción |
|--------|-------------|
| `204` | Modificación exitosa |
| `404` | Comercio o sucursal inválida |
| `401` | Token de autenticación inválido |

# POST — Crear Caja (Comercios y Transacciones)

> Extraído el: 2026-06-30
> Fuente: https://psp.bind.com.ar/developers/apis/comercio-crearcaja
> Producto: Adquirencia > Comercios y Transacciones

> ⚠️ **NOTA DE MAPEO**: Este archivo estaba nombrado como "habilitar_comercio" pero el endpoint real del portal en esta posición es "Crear Caja". Actualizado con el endpoint real.

## Descripción

"Da de alta una nueva caja en una sucursal." La caja representa un punto de venta que puede estar presente o no presente según su tipo de configuración.

## Request

**Método HTTP:** `POST`
**URL:** `https://gw-staging-qrbind.epays.services/bindentidad-comercio-v2/v2/api/v1.201/comercios/{id}/sucursales/{idSucursal}/cajas`

### curl request

```bash
curl -v -X POST "https://gw-staging-qrbind.epays.services/bindentidad-comercio-v2/v2/api/v1.201/comercios/C07663/sucursales/S02825/cajas" \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer {{access_token}}" \
  --data-raw '{"nombre": "Caja de prueba", "soloOrden": true, "tipoCajaId": 2, "requiereCvu": false}'
```

### Headers

| Header | Valor |
|--------|-------|
| `Content-Type` | `application/json` |
| `Authorization` | `Bearer {{access_token}}` |

### Path Parameters

| Parámetro | Tipo | Requerido | Descripción |
|-----------|------|-----------|-------------|
| `id` | string | SÍ | "código del comercio en donde se desea crear la caja" |
| `idSucursal` | string | SÍ | "código de la sucursal en donde se desea crear la caja" |

### Body

| Parámetro | Tipo | Requerido | Descripción |
|-----------|------|-----------|-------------|
| `nombre` | string | NO | Nombre o denominación de la caja |
| `soloOrden` | boolean | SÍ | "Indica si la caja acepta cobros sin ordenes de venta" (true/false) |
| `tipoCajaId` | int | NO | 1=presente; 2=no presente (por defecto: 1) |
| `requiereCvu` | boolean | NO | "se debe crear un CVU asociado a esta caja" (por defecto: false) |

### Request JSON

```json
{
  "nombre": "Caja de prueba",
  "soloOrden": true,
  "tipoCajaId": 2,
  "requiereCvu": false
}
```

## Response

### Respuesta exitosa (201)

```json
{
  "id": "[código_caja]",
  "cvu": "[cvu_generado]"
}
```

### Códigos de estado HTTP

| Código | Descripción |
|--------|-------------|
| `201` | Creación exitosa |
| `401` | Token de autenticación inválido |
| `404` | Comercio o sucursal inválidos |
| `422` | Error al intentar crear CVU |
| `500` | Tipo de caja inválido |

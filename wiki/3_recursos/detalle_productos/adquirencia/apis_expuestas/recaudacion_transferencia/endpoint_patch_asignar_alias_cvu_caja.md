# PATCH — Asignar Alias al CVU de una Caja (RxT)

> Extraído el: 2026-06-30
> Fuente: https://psp.bind.com.ar/developers/apis/asignar-alias-a-cvu-de-una-caja
> Producto: Adquirencia > Recaudación por Transferencia (RxT)

## Descripción

"Asigna un nuevo alias a un CVU asociado a una caja."

Solo puede renovarse la asignación cada 24 horas.

## Request

**Método HTTP:** `PATCH`
**URL:** `https://gw-staging-qrbind.epays.services/bindentidad-comercio-v2/v2/api/v1.201/comercios/{id}/sucursales/{idSucursal}/cajas/{idCaja}`

### curl request

```bash
curl -v -X PATCH "https://gw-staging-qrbind.epays.services/bindentidad-comercio-v2/v2/api/v1.201/comercios/C02086/sucursales/S08945/cajas/B00000455197" \
-H "Authorization: Bearer {{access_token}}" \
--data-raw '{"alias": "nuevo.alias1234"}'
```

### Headers

| Header | Valor |
|--------|-------|
| `Authorization` | `Bearer {{access_token}}` |

### Path Parameters

| Parámetro | Tipo | Requerido | Descripción |
|-----------|------|-----------|-------------|
| `id` | string | SÍ | "Código identificador del comercio al que pertenece el CVU" |
| `idSucursal` | string | SÍ | "Código identificador de la sucursal a la que pertenece el CVU" |
| `idCaja` | string | SÍ | "Código identificador de la caja a la que está asociado el CVU" |

### Body

| Parámetro | Tipo | Requerido | Descripción |
|-----------|------|-----------|-------------|
| `alias` | string | SÍ | Nuevo alias a asignar (ej: "nuevo.alias1234") |

### Request JSON

```json
{"alias": "nuevo.alias1234"}
```

## Response

Respuesta sin contenido.

### Códigos de estado HTTP

| Código | Descripción |
|--------|-------------|
| `204` | Asignación exitosa |
| `404` | No encontrado |
| `401` | Token de autenticación inválido |

## ⚠️ Notas y Advertencias del Portal

> Limitación temporal: la asignación de alias está disponible máximo una vez cada 24 horas.

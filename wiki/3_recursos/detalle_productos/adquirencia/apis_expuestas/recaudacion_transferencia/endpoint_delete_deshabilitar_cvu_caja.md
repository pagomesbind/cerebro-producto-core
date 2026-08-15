# DELETE — Deshabilitar el CVU de una Caja (RxT)

> Extraído el: 2026-06-30
> Fuente: https://psp.bind.com.ar/developers/apis/deshabilitar-el-cvu-de-una-caja
> Producto: Adquirencia > Recaudación por Transferencia (RxT)

## Descripción

"Elimina el CVU asociado a una caja. Al deshabilitar un CVU se elimina y ya no podrá operar. Puede crearse nuevamente el CVU para la caja para volver a utilizarlo."

## Request

**Método HTTP:** `DELETE`
**URL:** `https://gw-staging-qrbind.epays.services/bindentidad-comercio-v2/v2/api/v1.201/cajas/{idCaja}`

### curl request

```bash
curl -v -X DELETE "https://gw-staging-qrbind.epays.services/bindentidad-comercio-v2/v2/api/v1.201/cajas/B0123456" -H "Authorization: Bearer {{access_token}}"
```

### Headers

| Header | Valor |
|--------|-------|
| `Authorization` | `Bearer {{access_token}}` |

### Path Parameters

| Parámetro | Tipo | Requerido | Descripción |
|-----------|------|-----------|-------------|
| `idCaja` | string | SÍ | Código identificador de la caja |

## Response

Sin contenido.

### Códigos de estado HTTP

| Código | Descripción |
|--------|-------------|
| `204` | Eliminación exitosa |
| `404` | No encontrado |
| `401` | Token de autenticación inválido |

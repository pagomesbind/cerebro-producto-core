# DELETE — Eliminar CVU (Agente de Cobros)

> Fuente: https://psp.bind.com.ar/developers/apis/transfer-eliminarcvu
> Producto: Agente de Cobros — Transferencias entrantes en CVU

## Descripción

Elimina (inactiva) un CVU. Un CVU eliminado puede volver a activarse creándolo nuevamente con los datos originales (ver [Crear CVU](endpoint_post_crear_cvu.md)).

No se pueden realizar transferencias a un CVU eliminado.

## URL / Método

| Campo | Valor |
|-------|-------|
| Método | `DELETE` |
| URL (Staging) | `https://gw-staging-qrbind.epays.services/cvucollectentidad-financial/v1/v1.201/banks/322/view/owner/wallet/cvu/{cvu}/{cuit}` |

## Parámetros del Request

| Parámetro | Tipo | Requerido | Descripción |
|-----------|------|-----------|-------------|
| `cvu` | string (path) | REQUIRED | CVU a eliminar. |
| `cuit` | string (path) | REQUIRED | CUIT del titular del CVU a eliminar. |

## Bloque curl request

```bash
curl -v -X DELETE "https://gw-staging-qrbind.epays.services/cvucollectentidad-financial/v1/v1.201/banks/322/view/owner/wallet/cvu/0000532600001912202311/30717449076" \
-H "Authorization: Bearer {{access_token}}"
```

## Response

| Campo | Tipo | Descripción |
|-------|------|-------------|
| `cvu` | string | CVU eliminado. |

## Códigos HTTP

| Código | Descripción |
|--------|-------------|
| `200` | Eliminación exitosa |
| `401` | Token de autenticación inválido |

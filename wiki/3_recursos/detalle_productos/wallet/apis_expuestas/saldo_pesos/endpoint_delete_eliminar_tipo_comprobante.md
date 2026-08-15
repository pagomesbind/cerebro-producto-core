# DELETE — Eliminar Tipo de Comprobante

> Fuente: https://psp.bind.com.ar/developers/apis/eliminar-tipo-de-comprobante
> Producto: Wallet — Saldo en pesos

## Descripción

Elimina un tipo de comprobante de la entidad.

## URL / Método

| Campo | Valor |
|-------|-------|
| Método | `DELETE` |
| URL (Staging) | `https://gw-staging-qrbind.epays.services/walletentidad-comprobante/v1/api/v1.201/TipoComprobante/{id}` |

## Parámetros del Request

| Parámetro | Tipo | Requerido | Descripción |
|-----------|------|-----------|-------------|
| `id` | int | REQUIRED | Identificador del tipo de comprobante que se desea eliminar. |

## Bloque curl request

```bash
curl --location --request DELETE 'https://gw-staging-qrbind.epays.services/walletentidad-comprobante/v1/api/v1.201/TipoComprobante/357' \
--header 'Authorization: Bearer {{access_token}}' \
--header 'Content-Type: application/json'
```

## Response

Respuesta sin contenido.

## Códigos HTTP

| Código | Descripción |
|--------|-------------|
| `204` | Eliminado con éxito |
| `422` | Tipo de comprobante inválido |
| `422` | No se puede eliminar un tipo de comprobante reservado |
| `401` | Token de autenticación inválido |

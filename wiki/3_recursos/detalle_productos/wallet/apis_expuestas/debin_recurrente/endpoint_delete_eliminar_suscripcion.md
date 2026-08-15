# Endpoint — Eliminar suscripción

> Fuente: https://psp.bind.com.ar/developers/apis/eliminar-suscripcion
> Producto: Wallet — Debin recurrente

## Descripción

Elimina una suscripción de DEBIN recurrente.

## URL / Método

| Campo | Valor |
|-------|-------|
| Método | `DELETE` |
| URL (Staging) | `https://gw-staging-qrbind.epays.services/walletentidad-cuenta/v1/api/v1.201/Organizacion/DeleteSuscripcionDebin/{id}` |

## Parámetros del Request

| Parámetro | Tipo | Requerido | Descripción |
|-----------|------|-----------|-------------|
| `id` | int | REQUIRED | Identificador de la suscripción a eliminar (path param). |

## Bloque curl request

```bash
curl --location --request DELETE 'https://gw-staging-qrbind.epays.services/walletentidad-cuenta/v1/api/v1.201/Organizacion/DeleteSuscripcionDebin/2431' \
--header 'Authorization: Bearer {{access_token}}'
```

## Response

Sin contenido.

## Códigos HTTP

| Código | Descripción |
|--------|-------------|
| `204` | Eliminación exitosa |
| `422` | Suscripción no existente |
| `401` | Token de autenticación inválido |

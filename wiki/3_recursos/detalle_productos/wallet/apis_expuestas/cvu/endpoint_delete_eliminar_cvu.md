# Endpoint — Eliminar CVU

> Fuente: https://psp.bind.com.ar/developers/apis/eliminar-cvu
> Producto: Wallet — CVU

## Descripción

Elimina un CVU asignado a una cuenta.

Sólo elimina el CVU pero no la cuenta.

Puede volver a reactivarse un CVU eliminado volviendo a crearlo para la misma cuenta.

## URL / Método

| Campo | Valor |
|-------|-------|
| Método | `DELETE` |
| URL (Staging) | `https://gw-staging-qrbind.epays.services/walletentidad-cuenta/v1/api/v1.201/CVU/{id}` |

## Parámetros del Request

| Parámetro | Tipo | Requerido | Descripción |
|-----------|------|-----------|-------------|
| `id` | int | REQUIRED | Identificador del CVU que se desea eliminar (path param). |

## Bloque curl request

```bash
curl --location --request DELETE 'https://gw-staging-qrbind.epays.services/walletentidad-cuenta/v1/api/v1.201/CVU/154552' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer {{access_token}}'
```

## Response

Respuesta sin contenido.

## Códigos HTTP

| Código | Descripción |
|--------|-------------|
| `204` | Eliminación exitosa |
| `422` | El id de CVU es inválido |
| `400` | Algún dato de la solicitud tiene un formato inválido |
| `401` | Token de autenticación inválido |

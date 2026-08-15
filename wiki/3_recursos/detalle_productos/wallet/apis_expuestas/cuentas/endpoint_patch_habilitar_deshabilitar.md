# Endpoint — Habilitar/deshabilitar cuenta

> Fuente: https://psp.bind.com.ar/developers/apis/habilitar-deshabilitar-cuenta
> Producto: Wallet — Cuentas

## Descripción

Habilita o deshabilita una cuenta existente.

Deshabilitar una cuenta solo no permite que se realicen ajustes con comprobantes u operaciones salientes de dinero. Pero el CVU seguirá activo.

## URL / Método

| Campo | Valor |
|-------|-------|
| Método | `PATCH` |
| URL (Staging) | `https://gw-staging-qrbind.epays.services/walletentidad-cuenta/v1/api/v1.201/Habilitado/Cuenta/{id}` |
| Content-Type | `application/json` |

## Parámetros del Request

| Parámetro | Tipo | Requerido | Descripción |
|-----------|------|-----------|-------------|
| `id` | int | REQUIRED | Identificador de la cuenta (path param). |
| `habilitado` | boolean | REQUIRED | `true` para habilitar, `false` para deshabilitar. |

## Bloque curl request

```bash
curl --location --request PATCH 'https://gw-staging-qrbind.epays.services/walletentidad-cuenta/v1/api/v1.201/Habilitado/Cuenta/274926' \
--header 'Authorization: Bearer {{access_token}}' \
--header 'Content-Type: application/json' \
--data '{"habilitado": true}'
```

## Response

Respuesta vacía.

## Códigos HTTP

| Código | Descripción |
|--------|-------------|
| `204` | Solicitud exitosa |
| `400` | Algún dato de la solicitud tiene un formato inválido |
| `401` | Token de autenticación inválido |

# PATCH — Alta de Wallet

> Fuente: https://psp.bind.com.ar/developers/apis/alta-wallet-ob
> Producto: Onboarding — Validación por partes

## Descripción

Crea las cuentas de wallet con los datos de la solicitud.

Si no se completaron satisfactoriamente todos los pasos del flujo anteriores a este, es probable que el alta de las cuentas de wallet se realice con errores.

## URL / Método

| Campo | Valor |
|-------|-------|
| Método | `PATCH` |
| URL (Staging) | `https://gw-staging-qrbind.epays.services/orquestador/api/v1/solicitudes/{id}/alta-wallet` |

## Parámetros del Request

| Parámetro | Tipo | Requerido | Descripción |
|-----------|------|-----------|-------------|
| `id` | string (path) | REQUIRED | Identificador de la solicitud de onboarding creada. |

## Bloque curl request

```bash
curl --location --request PATCH 'https://gw-staging-qrbind.epays.services/orquestador/api/v1/solicitudes/da8a9839-2b00-4747-2760-08de218b4b26/alta-wallet' \
--header 'Cache-Control: no-cache' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer {{access_token}}'
```

## Response

Vacía.

## Códigos HTTP

| Código | Descripción |
|--------|-------------|
| `200` | Solicitud finalizada |
| `422` | Se inició el proceso de alta en wallet pero hubo un error. Deberá completarse desde el backoffice. |
| `401` | Token de autenticación inválido |

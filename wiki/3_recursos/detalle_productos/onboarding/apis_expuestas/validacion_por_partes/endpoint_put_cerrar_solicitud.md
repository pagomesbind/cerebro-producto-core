# PUT — Cerrar Solicitud de Onboarding

> Fuente: https://psp.bind.com.ar/developers/apis/cerrar-solicitud-ob
> Producto: Onboarding — Validación por partes

## Descripción

Cierra la solicitud de onboarding. Si no se completaron satisfactoriamente todos los pasos del flujo anteriores a este, es probable que este punto falle.

## URL / Método

| Campo | Valor |
|-------|-------|
| Método | `PUT` |
| URL (Staging) | `https://gw-staging-qrbind.epays.services/orquestador/api/v1/solicitudes/{id}/alta-wallet` |

> Nota: el portal muestra el mismo path que Alta de wallet. Confirmar con Bind si la URL correcta difiere.

## Parámetros del Request

| Parámetro | Tipo | Requerido | Descripción |
|-----------|------|-----------|-------------|
| `id` | string (path) | REQUIRED | Identificador de la solicitud de onboarding creada. |

## Bloque curl request

```bash
curl --location --request PUT 'https://gw-staging-qrbind.epays.services/orquestador/api/v1/solicitudes/da8a9839-2b00-4747-2760-08de218b4b26/alta-wallet' \
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
| `422` | Se inició el proceso pero hubo un error. Deberá completarse desde el backoffice. |
| `401` | Token de autenticación inválido |

# PATCH — Actualizar Teléfono

> Fuente: https://psp.bind.com.ar/developers/apis/actualizar-telefono-solicitud-ob
> Producto: Onboarding — Validación por partes

## Descripción

Actualiza el teléfono en la solicitud de onboarding.

## URL / Método

| Campo | Valor |
|-------|-------|
| Método | `PATCH` |
| URL (Staging) | `https://gw-staging-qrbind.epays.services/orquestador/api/v1/solicitudes/{id}/contacto/telefono` |

## Parámetros del Request

| Parámetro | Tipo | Requerido | Descripción |
|-----------|------|-----------|-------------|
| `id` | string (path) | REQUIRED | Identificador de la solicitud de onboarding creada. |
| `telefono` | string | REQUIRED | Número telefónico. |

## Bloque curl request

```bash
curl --location --request PATCH 'https://gw-staging-qrbind.epays.services/orquestador/api/v1/solicitudes/4fb30e39-9aeb-4d71-4f27-08dd72123456/contacto/telefono' \
--header 'Cache-Control: no-cache' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer {{access_token}}' \
--data-raw '{
  "telefono": "1199999999"
}'
```

## Response

Sin contenido.

## Códigos HTTP

| Código | Descripción |
|--------|-------------|
| `200` | Actualización exitosa |
| `401` | Token de autenticación inválido |

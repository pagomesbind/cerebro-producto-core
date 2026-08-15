# PATCH — Actualizar Email

> Fuente: https://psp.bind.com.ar/developers/apis/actualizar-email-solicitud-ob
> Producto: Onboarding — Validación por partes

## Descripción

Actualiza el email en la solicitud de onboarding.

## URL / Método

| Campo | Valor |
|-------|-------|
| Método | `PATCH` |
| URL (Staging) | `https://gw-staging-qrbind.epays.services/orquestador/api/v1/solicitudes/{id}/contacto/email` |

## Parámetros del Request

| Parámetro | Tipo | Requerido | Descripción |
|-----------|------|-----------|-------------|
| `id` | string (path) | REQUIRED | Identificador de la solicitud de onboarding creada. |
| `email` | string | REQUIRED | Correo electrónico. |

## Bloque curl request

```bash
curl --location --request PATCH 'https://gw-staging-qrbind.epays.services/orquestador/api/v1/solicitudes/4fb30e39-9aeb-4d71-4f27-08dd72123456/contacto/email' \
--header 'Cache-Control: no-cache' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer {{access_token}}' \
--data-raw '{
  "email": "hola@gmail.com"
}'
```

## Response

Sin contenido.

## Códigos HTTP

| Código | Descripción |
|--------|-------------|
| `200` | Actualización exitosa |
| `401` | Token de autenticación inválido |

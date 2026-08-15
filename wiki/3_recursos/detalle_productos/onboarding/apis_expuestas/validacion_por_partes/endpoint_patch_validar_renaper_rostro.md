# PATCH — Validar en Renaper Rostro

> Fuente: https://psp.bind.com.ar/developers/apis/validar-renaper-rostro
> Producto: Onboarding — Validación por partes

## Descripción

Consulta y valida en Renaper Rostro la foto selfie enviada comparándola con el DNI de la solicitud de onboarding.

## URL / Método

| Campo | Valor |
|-------|-------|
| Método | `PATCH` |
| URL (Staging) | `https://gw-staging-qrbind.epays.services/orquestador/api/v1/solicitudes/{id}/renaperRostro` |

## Parámetros del Request

| Parámetro | Tipo | Requerido | Descripción |
|-----------|------|-----------|-------------|
| `id` | string (path) | REQUIRED | Identificador de la solicitud de onboarding creada. |
| `selfie` | string | REQUIRED | Foto selfie en Base64. Máx 1 MB. |

## Bloque curl request

```bash
curl --location --request PATCH 'https://gw-staging-qrbind.epays.services/orquestador/api/v1/solicitudes/4fb30e39-9aeb-4d71-4f27-08dd72123456/renaperRostro' \
--header 'Cache-Control: no-cache' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer {{access_token}}' \
--data-raw '{
  "selfie": "fotoSelfieEnBase64_asdaksfhHIASDPASUFIUASDAD124235RWIKRFNMS"
}'
```

## Response

Sin contenido.

## Códigos HTTP

| Código | Descripción |
|--------|-------------|
| `200` | Validación exitosa |
| `401` | Token de autenticación inválido |

# PATCH — Validar en Padrón A5 ARCA

> Fuente: https://psp.bind.com.ar/developers/apis/validar-padrona5
> Producto: Onboarding — Validación por partes

## Descripción

Consulta y registra información del padrón A5 de ARCA para el CUIT de la solicitud de onboarding.

## URL / Método

| Campo | Valor |
|-------|-------|
| Método | `PATCH` |
| URL (Staging) | `https://gw-staging-qrbind.epays.services/orquestador/api/v1/solicitudes/{id}/afip/a5` |

## Parámetros del Request

| Parámetro | Tipo | Requerido | Descripción |
|-----------|------|-----------|-------------|
| `id` | string (path) | REQUIRED | Identificador de la solicitud de onboarding creada. |

## Bloque curl request

```bash
curl --location --request PATCH 'https://gw-staging-qrbind.epays.services/orquestador/api/v1/solicitudes/4fb30e39-9aeb-4d71-4f27-08dd72123456/afip/a5' \
--header 'Cache-Control: no-cache' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer {{access_token}}'
```

## Response

Sin contenido.

## Códigos HTTP

| Código | Descripción |
|--------|-------------|
| `200` | Validación exitosa |
| `401` | Token de autenticación inválido |

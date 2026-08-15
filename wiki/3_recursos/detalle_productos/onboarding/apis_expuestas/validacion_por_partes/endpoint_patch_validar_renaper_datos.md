# PATCH — Validar en Renaper Datos

> Fuente: https://psp.bind.com.ar/developers/apis/validar-renaper-datos
> Producto: Onboarding — Validación por partes

## Descripción

Consulta y valida en Renaper Datos el DNI asociado a la solicitud de onboarding.

## URL / Método

| Campo | Valor |
|-------|-------|
| Método | `PATCH` |
| URL (Staging) | `https://gw-staging-qrbind.epays.services/orquestador/api/v1/solicitudes/{id}/renaper` |

## Parámetros del Request

| Parámetro | Tipo | Requerido | Descripción |
|-----------|------|-----------|-------------|
| `id` | string (path) | REQUIRED | Identificador de la solicitud de onboarding creada. |

## Bloque curl request

```bash
curl --location --request PATCH 'https://gw-staging-qrbind.epays.services/orquestador/api/v1/solicitudes/4fb30e39-9aeb-4d71-4f27-08dd72123456/renaper' \
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
| `422` | Renaper no reconoce el DNI consultado |
| `422` | El DNI corresponde a una persona fallecida en Renaper |
| `422` | El ejemplar del DNI ingresado no está vigente en Renaper |
| `422` | El DNI corresponde a una persona de edad menor a la permitida |
| `401` | Token de autenticación inválido |

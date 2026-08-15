# PUT — Actualizar Datos Adicionales

> Fuente: https://psp.bind.com.ar/developers/apis/actualizar-datos-solicitud-ob
> Producto: Onboarding — Validación por partes

## Descripción

Actualiza datos generales de onboarding para completar los necesarios para finalizar una solicitud.

## URL / Método

| Campo | Valor |
|-------|-------|
| Método | `PUT` |
| URL (Staging) | `https://gw-staging-qrbind.epays.services/orquestador/api/v1/solicitudes/{id}` |

## Parámetros del Request

| Parámetro | Tipo | Requerido | Descripción |
|-----------|------|-----------|-------------|
| `id` | string (path) | REQUIRED | Identificador de la solicitud de onboarding creada. |
| `esPEP` | boolean | OPTIONAL | Indica si el usuario declaró que es PEP o no. |
| `esFatca` | boolean | OPTIONAL | Indica si el usuario declaró que es FATCA o no. |
| `esOcde` | boolean | OPTIONAL | Indica si el usuario declaró que es OCDE o no. |
| `esUIF` | boolean | OPTIONAL | Indica si el usuario declaró que es UIF o no. |
| `aceptaTyc` | boolean | OPTIONAL | Indica si el usuario aceptó los TyC. |
| `estadoCivil` | string | OPTIONAL | Estado civil: `"SOLTERO"` / `"CASADO"` / `"VIUDO"` / `"SEPARADO"` / `"DIVORCIADO"` |
| `ocupacion` | string | OPTIONAL | Ocupación: `"JUBILADO"` / `"ESTUDIANTE"` / `"TRABAJADOR EN RELACIÓN DE DEPENDENCIA"` / `"AMA DE CASA"` / `"DESOCUPADO"` |

## Bloque curl request

```bash
curl --location --request PUT 'https://gw-staging-qrbind.epays.services/orquestador/api/v1/solicitudes/2549d13d-1242-4c6b-275f-08de218b4b26' \
--header 'Cache-Control: no-cache' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer {{access_token}}' \
--data-raw '{
  "esPEP": false,
  "esFacta": false,
  "esOcde": false,
  "esUif": false,
  "aceptaTyc": true,
  "estadoCivil": "SOLTERO",
  "ocupacion": "TRABAJADOR EN RELACIÓN DE DEPENDENCIA"
}'
```

## Response

Sin contenido.

## Códigos HTTP

| Código | Descripción |
|--------|-------------|
| `200` | Actualización exitosa |
| `401` | Token de autenticación inválido |

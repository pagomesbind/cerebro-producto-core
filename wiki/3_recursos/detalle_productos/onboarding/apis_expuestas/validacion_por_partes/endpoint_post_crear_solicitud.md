# POST — Crear Solicitud OB (Validación por Partes)

> Fuente: https://psp.bind.com.ar/developers/apis/crear-solicitud-ob
> Producto: Onboarding — Validación por partes

## Descripción

Crea una solicitud de onboarding para luego poder invocar las validaciones sobre la misma.

## URL / Método

| Campo | Valor |
|-------|-------|
| Método | `POST` |
| URL (Staging) | `https://gw-staging-qrbind.epays.services/orquestador/api/v1/solicitudes` |

## Parámetros del Request

| Parámetro | Tipo | Requerido | Descripción |
|-----------|------|-----------|-------------|
| `frente` | string | REQUIRED | Foto del frente del DNI en Base64. Máx 1 MB. |
| `dorso` | string | REQUIRED | Foto del dorso del DNI en Base64. Máx 1 MB. |
| `documento` | string | OPTIONAL | Número de DNI. Usar si no puede extraerse del PDF417 (error `PDF417_NO_ENCONTRADO`). |
| `documentoTramite` | string | OPTIONAL | Número de trámite del documento. Usar si no puede extraerse del PDF417. |
| `genero` | string | OPTIONAL | Género: `"M"` / `"F"` / `"X"`. Usar si no puede extraerse del PDF417. |
| `externalrefid` | string | OPTIONAL | Identificador externo indicado por la propia Entidad. Máx 50 caracteres. |

## Bloque curl request

```bash
curl --location 'https://gw-staging-qrbind.epays.services/orquestador/api/v1/solicitudes' \
--header 'Cache-Control: no-cache' \
--header 'Content-Type: application/json' \
--header 'Authorization: {{access_token}}' \
--data-raw '{
  "frente": "fotoEnBase64DelFrenteDelDni_asdaksfhHIASDPASUFIUASDAD124235RWIKRFNMS",
  "dorso": "fotoEnBase64DelDorsoDelDni_asdaksfhHIASDPASUFIUASDAD124235RWIKRFNMS",
  "documento": null,
  "documentoTramite": null,
  "genero": null,
  "externalId": "789654ABCEDF"
}'
```

## Response

| Campo | Tipo | Descripción |
|-------|------|-------------|
| `id` | string | Identificador de la solicitud de onboarding creada. |

## Códigos HTTP

| Código | Descripción |
|--------|-------------|
| `201` | Solicitud creada exitosamente |
| `422` | Error en lectura del PDF417 |
| `422` | Ya existe una solicitud aprobada para la persona |
| `401` | Token de autenticación inválido |

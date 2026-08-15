# GET — Consultar Solicitud por ID Externo (Registro Único)

> Fuente: https://psp.bind.com.ar/developers/apis/consultar-solicitud-por-id-externo
> Producto: Onboarding — Registro único

## Descripción

Devuelve información asociada a la solicitud buscándola por el identificador externo de la entidad. Mismo response que [Consultar por ID](endpoint_get_consultar_solicitud_id.md).

## URL / Método

| Campo | Valor |
|-------|-------|
| Método | `GET` |
| URL (Staging) | `https://gw-staging-qrbind.epays.services/orquestador/api/v1/solicitudes/{externalrefid}/externalRefid` |

## Parámetros del Request

| Parámetro | Tipo | Requerido | Descripción |
|-----------|------|-----------|-------------|
| `externalrefid` | string | REQUIRED | Identificador externo indicado por la propia Entidad. |

## Bloque curl request

```bash
curl --location 'https://gw-staging-qrbind.epays.services/orquestador/api/v1/solicitudes/12345/externalRefid' \
--header 'Cache-Control: no-cache' \
--header 'Authorization: Bearer {{access_token}}' \
--header 'Content-Type: application/json'
```

## Response

Mismo response que [endpoint_get_consultar_solicitud_id.md](endpoint_get_consultar_solicitud_id.md).

## Códigos HTTP

| Código | Descripción |
|--------|-------------|
| `200` | Consulta exitosa |
| `422` | Algún campo del request no es válido |
| `401` | Token de autenticación inválido |

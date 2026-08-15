# GET — Descargar Archivo Cobro (Batch)

> Extraído el: 2026-06-30
> Fuente: https://psp.bind.com.ar/developers/apis/batch-descargararchivo
> Producto: Adquirencia > Conciliaciones

## Descripción

"Devuelve una lista de archivos disponibles para ser descargados según los filtros y condiciones de búsqueda indicados."

El parámetro `encrypted` se obtiene previamente desde el endpoint Consultar archivos Cobro.

## Request

**Método HTTP:** `GET`
**URL:** `https://gw-staging-qrbind.epays.services/bindentidad-filemanager-v2/v2/api/v1.201/Download`

### curl request

```bash
curl -v -X GET "https://gw-staging-qrbind.epays.services/bindentidad-filemanager-v2/v2/api/v1.201/Download?encrypted=qc04ZdXDepuxst7is1BOmxW0TX8rqz3BXoEhDsTl44Ss0gkV9d69uxRaP8ZE%2BNZo9WH1C5ax8P5IwjphoUFiUTpjlC5vbVkRp2uphZz9VFybWbRToqbpYlxlZTYOdM4WPX%2BVRUEoZ8H46fFLoYxQIa%2FA4d91C7lll1O9p7HGdwgxV6aOzCwu14GXRGpTqh2D" -H "Authorization: Bearer {{access_token}}"
```

### Headers

| Header | Valor |
|--------|-------|
| `Authorization` | `Bearer {{access_token}}` |

### Query Parameters

| Parámetro | Tipo | Requerido | Descripción |
|-----------|------|-----------|-------------|
| `encrypted` | string | SÍ | "Código encriptado único para el archivo. Se obtiene por el Consultar archivos" |

## Response

Descarga del archivo en formato binario.

### Códigos de estado HTTP

| Código | Descripción |
|--------|-------------|
| `200` | Descarga exitosa |
| `401` | Token de autenticación inválido |

# GET — Consultar Archivos Cobro (Batch)

> Extraído el: 2026-06-30
> Fuente: https://psp.bind.com.ar/developers/apis/batch-consultararchivos
> Producto: Adquirencia > Conciliaciones

## Descripción

"Devuelve una lista de archivos disponibles para ser descargados según los filtros y condiciones de búsqueda indicados."

El servicio genera archivos batch para conciliación todos los días hábiles, permitiendo acceso mediante API con código de descarga encriptado.

## Request

**Método HTTP:** `GET`
**URL:** `https://gw-staging-qrbind.epays.services/bindentidad-filemanager-v2/v2/api/v1.201/browser`

### curl request

```bash
curl -v -X GET "https://gw-staging-qrbind.epays.services/bindentidad-filemanager-v2/v2/api/v1.201/browser?PSP=164&Filter=000BBOTON011223.zip" -H "Authorization: Bearer {{access_token}}"
```

### Headers

| Header | Valor |
|--------|-------|
| `Authorization` | `Bearer {{access_token}}` |

### Query Parameters

| Parámetro | Tipo | Requerido | Descripción |
|-----------|------|-----------|-------------|
| `PSP` | string | SÍ | "Es el código del PSP que actúa de agente de retención del comercio." |
| `Filter` | string | NO | "Es el nombre exacto del archivo (incluyendo su extensión)." |

## Response

### Respuesta exitosa (200)

```json
{
  "id": "string",
  "folder": "string",
  "name": "string",
  "encrypted": "string"
}
```

| Campo | Tipo | Descripción |
|-------|------|-------------|
| `id` | string | Identificador interno del archivo |
| `folder` | string | Path de la carpeta donde se encuentra |
| `name` | string | Nombre del archivo |
| `encrypted` | string | Código encriptado para descargar (usar en endpoint Descargar) |

### Códigos de estado HTTP

| Código | Descripción |
|--------|-------------|
| `200` | Consulta exitosa |
| `401` | Token de autenticación inválido |

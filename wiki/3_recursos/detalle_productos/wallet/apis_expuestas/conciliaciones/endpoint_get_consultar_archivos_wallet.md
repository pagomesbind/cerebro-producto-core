# Endpoint — Consultar archivos Wallet

> Fuente: https://psp.bind.com.ar/developers/apis/consultar-archivos-wallet
> Producto: Wallet — Consultas y conciliaciones

## Descripción

Devuelve una lista de archivos disponibles para ser descargados según los filtros y condiciones de búsqueda indicados.

Se generan archivos batch para que la Entidad pueda realizar conciliaciones y controlar. Los archivos se generan todos los días hábiles.

Se pueden obtener los archivos vía API: Primero consultando para obtener el código de descarga encriptado, y luego descargándolo con este código.

Los archivos sólo tienen movimientos correspondientes a la Entidad que los está consultando.

Hay 2 tipos de archivos disponibles:
- Archivo de movimientos (ver [guia_archivo_batch_movimientos.md](guia_archivo_batch_movimientos.md))
- Archivo de saldos (ver [guia_archivo_batch_saldos.md](guia_archivo_batch_saldos.md))

## URL / Método

| Campo | Valor |
|-------|-------|
| Método | `GET` |
| URL (Staging) | `https://gw-staging-qrbind.epays.services/walletentidad-filemanager/v1/api/v1.201/browser` |

## Parámetros del Request

| Parámetro | Tipo | Requerido | Descripción |
|-----------|------|-----------|-------------|
| `PSP` | string | REQUIRED | Código del PSP. Staging: `"532"`, Producción: `"184"` |
| `Filter` | string | OPTIONAL | Nombre exacto del archivo (incluyendo extensión). |

## Bloque curl request

```bash
curl --location 'https://gw-staging-qrbind.epays.services/walletentidad-filemanager/v1/api/v1.201/browser?PSP=532' \
--header 'Authorization: Bearer {{access_token}}'
```

## Response

| Campo | Tipo | Descripción |
|-------|------|-------------|
| `id` | string | Identificador interno del archivo. |
| `folder` | string | Path de la carpeta donde se encuentra el archivo. |
| `name` | string | Nombre del archivo. |
| `encrypted` | string | Código encriptado único para descargar el archivo. |

## Códigos HTTP

| Código | Descripción |
|--------|-------------|
| `200` | Consulta exitosa |
| `401` | Token de autenticación inválido |

# Endpoint — Descargar archivo Wallet

> Fuente: https://psp.bind.com.ar/developers/apis/descargar-archivo-wallet
> Producto: Wallet — Consultas y conciliaciones

## Descripción

Descarga un archivo batch de conciliación usando el código encriptado obtenido del endpoint [Consultar archivos Wallet](endpoint_get_consultar_archivos_wallet.md).

## URL / Método

| Campo | Valor |
|-------|-------|
| Método | `GET` |
| URL (Staging) | `https://gw-staging-qrbind.epays.services/walletentidad-filemanager/v1/api/v1.201/Download` |

## Parámetros del Request

| Parámetro | Tipo | Requerido | Descripción |
|-----------|------|-----------|-------------|
| `encrypted` | string | REQUIRED | Código encriptado único del archivo. Se obtiene del endpoint Consultar archivos. |

## Bloque curl request

```bash
curl --location 'https://gw-staging-qrbind.epays.services/walletentidad-filemanager/v1/api/v1.201/Download?encrypted=123456DyTfS4tYtxf4gOwDULfcBqRwyucUj0fQyLMje%2BKgcRO2%2BuwAE5sqxpUwTsT3180y5SHvPJpv44byCDvWlxBSoJSXbEjHKtb6XsP5xk1UpLnOGFxARBM061BAyS6H0%2BtUjjqM46BPSjJMB8ja2H%2BKroURIg8DW2txBCU%2Bn71IBw%2BtDarKk4fEDREOiW' \
--header 'Authorization: Bearer {{access_token}}'
```

## Response

Descarga del archivo.

## Códigos HTTP

| Código | Descripción |
|--------|-------------|
| `200` | Descarga exitosa |
| `401` | Token de autenticación inválido |

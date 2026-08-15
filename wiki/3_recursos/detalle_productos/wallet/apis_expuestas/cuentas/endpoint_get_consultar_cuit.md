# Endpoint — Consultar cuentas por CUIT

> Fuente: https://psp.bind.com.ar/developers/apis/consultar-cuenta-por-cuit
> Producto: Wallet — Cuentas

## Descripción

Obtiene los datos de una cuenta.

La respuesta de este endpoint es un array debido a que podrían existir más de una cuenta para un mismo CUIT.

## URL / Método

| Campo | Valor |
|-------|-------|
| Método | `GET` |
| URL (Staging) | `https://gw-staging-qrbind.epays.services/walletentidad-cuenta/v1/api/v1.201/CuentaByCuit?cuit={cuit}` |

## Parámetros del Request

| Parámetro | Tipo | Requerido | Descripción |
|-----------|------|-----------|-------------|
| `cuit` | string | REQUIRED | CUIT/CUIL asociado a la cuenta a consultar. |

## Bloque curl request

```bash
curl --location 'https://gw-staging-qrbind.epays.services/walletentidad-cuenta/v1/api/v1.201/CuentaByCuit?cuit=20374312759' \
--header 'Authorization: Bearer {{access_token}}'
```

## Response

Array de objetos con los mismos campos que Consultar por ID (ver `endpoint_get_consultar_id.md`).

## Códigos HTTP

| Código | Descripción |
|--------|-------------|
| `200` | Consulta exitosa |
| `404` | No existe una cuenta con ese CUIT |
| `401` | Token de autenticación inválido |

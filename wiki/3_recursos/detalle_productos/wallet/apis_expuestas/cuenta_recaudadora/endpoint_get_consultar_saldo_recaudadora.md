# Endpoint — Consultar saldo de la cuenta recaudadora

> Fuente: https://psp.bind.com.ar/developers/apis/consultar-saldo-actual-de-la-cuenta-recaudadora
> Producto: Wallet — Cuenta recaudadora

## Descripción

Devuelve el valor de saldo que tiene la cuenta recaudadora de la entidad en el momento de la consulta.

## URL / Método

| Campo | Valor |
|-------|-------|
| Método | `GET` |
| URL (Staging) | `https://gw-staging-qrbind.epays.services/walletentidad-cuenta/v1/api/v1.201/SaldoCuentaRecaudadora` |

## Parámetros del Request

Sin contenido.

## Bloque curl request

```bash
curl --location 'https://gw-staging-qrbind.epays.services/walletentidad-cuenta/v1/api/v1.201/SaldoCuentaRecaudadora' \
--header 'Content-Type: application/json-patch+json' \
--header 'Cache-Control: no-cache' \
--header 'Authorization: Bearer {{access_token}}'
```

## Response

| Campo | Tipo | Descripción |
|-------|------|-------------|
| `saldo` | double | Valor del saldo actual de la cuenta recaudadora al momento de la consulta. |

## Códigos HTTP

| Código | Descripción |
|--------|-------------|
| `200` | Consulta exitosa |
| `401` | Token de autenticación inválido |

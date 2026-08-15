# GET — Consultar Saldo Actual por CVU

> Fuente: https://psp.bind.com.ar/developers/apis/consultar-saldo-actual-por-cvu
> Producto: Wallet — Saldo en pesos

## Descripción

Devuelve el valor de saldo que tiene la cuenta en el momento de la consulta.

## URL / Método

| Campo | Valor |
|-------|-------|
| Método | `GET` |
| URL (Staging) | `https://gw-staging-qrbind.epays.services/walletentidad-cuenta/v1/api/v1.201/SaldoActualByCVU/{cvu}` |

## Parámetros del Request

| Parámetro | Tipo | Requerido | Descripción |
|-----------|------|-----------|-------------|
| `cvu` | string | REQUIRED | CVU asociado a la cuenta a consultar. |

## Bloque curl request

```bash
curl --location 'https://gw-staging-qrbind.epays.services/walletentidad-cuenta/v1/api/v1.201/SaldoActualByCVU/0000532609100002749314' \
--header 'Authorization: Bearer {{access_token}}'
```

## Response

| Campo | Tipo | Descripción |
|-------|------|-------------|
| `saldo` | decimal | Valor del saldo actual de la cuenta al momento de la consulta. |

## Códigos HTTP

| Código | Descripción |
|--------|-------------|
| `200` | Consulta exitosa |
| `404` | El CVU consultado no existe |
| `401` | Token de autenticación inválido |

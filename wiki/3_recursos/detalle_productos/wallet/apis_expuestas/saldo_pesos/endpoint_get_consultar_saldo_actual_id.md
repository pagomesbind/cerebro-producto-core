# GET — Consultar Saldo Actual por ID de Cuenta

> Fuente: https://psp.bind.com.ar/developers/apis/consultar-saldo-actual-por-id
> Producto: Wallet — Saldo en pesos

## Descripción

Devuelve el valor de saldo que tiene la cuenta en el momento de la consulta.

## URL / Método

| Campo | Valor |
|-------|-------|
| Método | `GET` |
| URL (Staging) | `https://gw-staging-qrbind.epays.services/walletentidad-cuenta/v1/api/v1.201/SaldoActualByIdCuenta/{idCuenta}` |

## Parámetros del Request

| Parámetro | Tipo | Requerido | Descripción |
|-----------|------|-----------|-------------|
| `idCuenta` | int | REQUIRED | Identificador de la cuenta a consultar. |

## Bloque curl request

```bash
curl --location 'https://gw-staging-qrbind.epays.services/walletentidad-cuenta/v1/api/v1.201/SaldoActualByIdCuenta/10022' \
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
| `404` | La cuenta consultada es incorrecta |
| `401` | Token de autenticación inválido |

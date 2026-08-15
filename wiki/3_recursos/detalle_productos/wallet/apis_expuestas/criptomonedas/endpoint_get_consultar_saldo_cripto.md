# GET — Consultar Saldo Cripto

> Fuente: https://psp.bind.com.ar/developers/apis/consultar-saldo-cripto
> Producto: Wallet — Cripto

## Descripción

Devuelve el saldo actual de criptomonedas que tiene la cuenta. El monto es en unidades de cada criptomoneda.

## URL / Método

| Campo | Valor |
|-------|-------|
| Método | `GET` |
| URL (Staging) | `https://gw-staging-qrbind.epays.services/walletentidad-investment/v1/api/v1.201/Inversion/SaldoCripto/{idCuenta}` |

## Parámetros del Request

| Parámetro | Tipo | Requerido | Descripción |
|-----------|------|-----------|-------------|
| `idCuenta` | int | REQUIRED | Identificador de la cuenta. |

## Bloque curl request

```bash
curl --location 'https://gw-staging-qrbind.epays.services/walletentidad-investment/v1/api/v1.201/Inversion/SaldoCripto/276603' \
--header 'Authorization: Bearer {{access_token}}'
```

## Response

| Campo | Tipo | Descripción |
|-------|------|-------------|
| `saldosCriptomonedas[].moneda` | string | Criptomoneda siendo cotizada. |
| `saldosCriptomonedas[].saldo` | string | Cantidad de unidades de criptomoneda que posee actualmente la cuenta. |

## Códigos HTTP

| Código | Descripción |
|--------|-------------|
| `200` | Consulta exitosa |
| `422` | Cuenta inválida |
| `401` | Token de autenticación inválido |

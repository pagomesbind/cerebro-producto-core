# GET — Consultar Saldo Histórico por CVU

> Fuente: https://psp.bind.com.ar/developers/apis/consultar-saldo-hist%C3%B3rico-por-cvu
> Producto: Wallet — Saldo en pesos

## Descripción

Devuelve el valor de saldo histórico que tenía la cuenta en la fecha determinada.

## URL / Método

| Campo | Valor |
|-------|-------|
| Método | `GET` |
| URL (Staging) | `https://gw-staging-qrbind.epays.services/walletentidad-cuenta/v1/api/v1.201/SaldoHistoricoByCVU` |

## Parámetros del Request

| Parámetro | Tipo | Requerido | Descripción |
|-----------|------|-----------|-------------|
| `cvu` | string | REQUIRED | CVU asociado a la cuenta a consultar. |
| `fecha` | datetime | REQUIRED | Fecha para la cual se quiere consultar el saldo histórico. |

## Bloque curl request

```bash
curl --location 'https://gw-staging-qrbind.epays.services/walletentidad-cuenta/v1/api/v1.201/SaldoHistoricoByCVU?cvu=0000531909000067076630&fecha=2024-03-01' \
--header 'Authorization: Bearer {{access_token}}'
```

## Response

| Campo | Tipo | Descripción |
|-------|------|-------------|
| `saldo` | decimal | Valor del saldo histórico de la cuenta en la fecha indicada. |

## Códigos HTTP

| Código | Descripción |
|--------|-------------|
| `200` | Consulta exitosa |
| `400` | Falta un campo requerido |
| `404` | El CVU no existe |
| `422` | No existe saldo histórico de la cuenta en la fecha indicada |
| `422` | La fecha es inválida |
| `401` | Token de autenticación inválido |

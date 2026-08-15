# GET — Consultar Saldos Históricos (Listado)

> Fuente: https://psp.bind.com.ar/developers/apis/consultar-lista-de-saldos-hist%C3%B3ricos
> Producto: Wallet — Saldo en pesos

## Descripción

Devuelve el valor de saldo histórico que tenían todas las cuentas de la entidad en la fecha indicada en la consulta.

## URL / Método

| Campo | Valor |
|-------|-------|
| Método | `GET` |
| URL (Staging) | `https://gw-staging-qrbind.epays.services/walletentidad-cuenta/v1/api/v1.201/SaldosHistoricos` |

## Parámetros del Request

| Parámetro | Tipo | Requerido | Descripción |
|-----------|------|-----------|-------------|
| `fecha` | datetime | REQUIRED | Fecha para la cual se quiere consultar el saldo. |
| `pageNumber` | int | REQUIRED | Número de página a mostrar. |
| `pageSize` | int | REQUIRED | Cantidad de cuentas por página a mostrar. |

## Bloque curl request

```bash
curl --location 'https://gw-staging-qrbind.epays.services/walletentidad-cuenta/v1/api/v1.201/SaldosHistoricos?fecha=01-06-2024&pageNumber=1&pageSize=3' \
--header 'Authorization: Bearer {{access_token}}'
```

## Response

| Campo | Tipo | Descripción |
|-------|------|-------------|
| `totalPages` | int | Cantidad total de páginas disponibles para consultar. |
| `totalRecords` | int | Cantidad total de cuentas disponibles para consultar. |
| `saldos[].idCuenta` | int | Identificador de la cuenta consultada. |
| `saldos[].saldo` | decimal | Saldo de la cuenta en la fecha indicada. |

## Códigos HTTP

| Código | Descripción |
|--------|-------------|
| `200` | Consulta exitosa |
| `204` | No se encontró ningún saldo para los filtros indicados |
| `400` | Falta un campo requerido |
| `422` | La fecha ingresada es inválida |
| `422` | No hay registros de saldos históricos para los filtros indicados |
| `401` | Token de autenticación inválido |

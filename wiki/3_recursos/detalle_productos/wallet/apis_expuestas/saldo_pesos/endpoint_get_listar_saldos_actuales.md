# GET — Consultar Saldos Actuales (Listado)

> Fuente: https://psp.bind.com.ar/developers/apis/consultar-lista-de-saldos-actuales
> Producto: Wallet — Saldo en pesos

## Descripción

Devuelve el valor de saldo que tienen todas las cuentas de la entidad en el momento de la consulta.

## URL / Método

| Campo | Valor |
|-------|-------|
| Método | `GET` |
| URL (Staging) | `https://gw-staging-qrbind.epays.services/walletentidad-cuenta/v1/api/v1.201/SaldosActuales` |

## Parámetros del Request

| Parámetro | Tipo | Requerido | Descripción |
|-----------|------|-----------|-------------|
| `pageNumber` | int | REQUIRED | Número de página a mostrar. |
| `pageSize` | int | REQUIRED | Cantidad de cuentas por página a mostrar. |
| `cIds` | int[] | OPTIONAL | Array con identificadores de cuenta a consultar. |

## Bloque curl request

```bash
curl --location 'https://gw-staging-qrbind.epays.services/walletentidad-cuenta/v1/api/v1.201/SaldosActuales?pageNumber=20&pageSize=3' \
--header 'Authorization: Bearer {{access_token}}'
```

## Response

| Campo | Tipo | Descripción |
|-------|------|-------------|
| `totalPages` | int | Cantidad total de páginas disponibles para consultar. |
| `totalRecords` | int | Cantidad total de cuentas disponibles para consultar. |
| `saldos[].idCuenta` | int | Identificador de la cuenta consultada. |
| `saldos[].saldo` | decimal | Saldo actual de la cuenta al momento de la consulta. |

## Códigos HTTP

| Código | Descripción |
|--------|-------------|
| `200` | Consulta exitosa |
| `204` | No se encontró ningún saldo para los filtros indicados |
| `400` | Falta un campo requerido |
| `401` | Token de autenticación inválido |

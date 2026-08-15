# Endpoint — Consultar cuenta x CBU/CVU/alias

> Fuente: https://psp.bind.com.ar/developers/apis/consultar-cbu-cvu-por-cbu-cvu-o-alias
> Producto: Wallet — CVU

## Descripción

Obtiene los datos de una cuenta CBU/CVU.

Con este endpoint se pueden consultar datos de cuentas externas de otros bancos, billeteras y proveedores de cuentas.

## URL / Método

| Campo | Valor |
|-------|-------|
| Método | `GET` |
| URL (Staging) | `https://gw-staging-qrbind.epays.services/walletentidad-cuenta/v1/api/v1.201/CuentaCVUByCbuCvuOrAlias?cbuOrCvu=&alias=` |

## Parámetros del Request

| Parámetro | Tipo | Requerido | Descripción |
|-----------|------|-----------|-------------|
| `cbuOrCvu` | string | OPTIONAL | CBU o CVU de la cuenta que se quiere consultar. |
| `alias` | string | OPTIONAL | Alias de la cuenta que se quiere consultar. |

## Bloque curl request

```bash
curl --location 'https://gw-staging-qrbind.epays.services/walletentidad-cuenta/v1/api/v1.201/CuentaCVUByCbuCvuOrAlias?cbuOrCvu=0000532609100002749314&alias=null' \
--header 'Authorization: Bearer {{access_token}}'
```

## Response

| Campo | Tipo | Descripción |
|-------|------|-------------|
| `cuentaId` | int | Cuenta bancaria recaudadora asociada. |
| `cbucvu` | string | CBU o CVU de la cuenta consultada. |
| `alias` | string | Alias de la cuenta consultada. |
| `cuitCuil` | string | CUIT/CUIL del titular de la cuenta consultada. |
| `nombre` | string | Nombre del CBU o CVU. |
| `bancoNombre` | string | Nombre del banco sponsor de la cuenta. |
| `activo` | boolean | Indica si el CBU o CVU está activo. |
| `billeteraId` | int | Identificador de la billetera para Coelsa. |
| `nombreCvu` | string | Nombre con que se creó el CVU de la cuenta consultada. |
| `entidad` | string | Nombre de la entidad dueña del CBU o CVU. |
| `moneda` | string | Moneda de la cuenta. Valores posibles: `"ARS"`, `"USD"` |

## Códigos HTTP

| Código | Descripción |
|--------|-------------|
| `200` | Consulta exitosa |
| `404` | El CBU/CVU no es válido |
| `422` | El alias ingresado no existe |
| `422` | El alias ingresado tiene un formato inválido |
| `400` | Un campo requerido no fue enviado |
| `401` | Token de autenticación inválido |

# GET — Consultar Cotización de Dólar CCL

> Fuente: https://psp.bind.com.ar/developers/apis/inversiones-consultar-cotizacion-de-dolar
> Producto: Wallet — Dólar CCL

## Descripción

Devuelve la cotización de compra y venta del dólar CCL.

Si la Organización está configurada para operar con modelo **Combi**, también se devuelven los valores relativos al precio fijado (`hash`, `priceLimitTime`, `priceLimitTimeInSeconds`).

## URL / Método

| Campo | Valor |
|-------|-------|
| Método | `GET` |
| URL (Staging) | `https://gw-staging-qrbind.epays.services/walletentidad-investment/v1/api/v1.201/Inversion/CotizacionCCL/{idCuenta}` |

## Parámetros del Request

| Parámetro | Tipo | Requerido | Descripción |
|-----------|------|-----------|-------------|
| `idCuenta` | int | REQUIRED | Identificador de la cuenta. |

## Bloque curl request

```bash
curl --location 'https://gw-staging-qrbind.epays.services/walletentidad-investment/v1/api/v1.201/Inversion/CotizacionCCL/276058' \
--header 'Cache-Control: no-cache' \
--header 'Authorization: {{access_token}}'
```

## Response

| Campo | Tipo | Descripción |
|-------|------|-------------|
| `buyPrice` | double | Precio de compra en pesos argentinos. |
| `sellPrice` | int | Precio de venta en pesos argentinos. |
| `timestamp` | string | Fecha y horario de la cotización. |
| `horarioMercado` | boolean | Si al momento de la consulta se encontraba dentro del horario de mercado. |
| `hash` | string | Código único para fijar precio en intención de compra (modelo Combi). `null` en modelo Standard. |
| `priceLimitTime` | string | Fecha y hora de vencimiento del precio fijado (modelo Combi). `null` en modelo Standard. |
| `priceLimitTimeInSeconds` | string | Segundos hasta que expire el precio fijado (modelo Combi). `null` en modelo Standard. |

## Códigos HTTP

| Código | Descripción |
|--------|-------------|
| `200` | Consulta exitosa (Standard o Combi) |
| `422` | Cuenta inválida |
| `401` | Token de autenticación inválido |

# GET — Consultar Cotización de Cripto

> Fuente: https://psp.bind.com.ar/developers/apis/consultar-cotizacion-de-cripto
> Producto: Wallet — Cripto

## Descripción

Devuelve la cotización de compra y venta de las distintas criptos disponibles para operar en pesos argentinos.

## URL / Método

| Campo | Valor |
|-------|-------|
| Método | `GET` |
| URL (Staging) | `https://gw-staging-qrbind.epays.services/walletentidad-investment/v1/api/v1.201/Inversion/CotizacionCripto/{idCuenta}` |

## Parámetros del Request

| Parámetro | Tipo | Requerido | Descripción |
|-----------|------|-----------|-------------|
| `idCuenta` | int | REQUIRED | Identificador de la cuenta. |

## Bloque curl request

```bash
curl --location 'https://gw-staging-qrbind.epays.services/walletentidad-investment/v1/api/v1.201/Inversion/CotizacionCripto/123' \
--header 'Authorization: Bearer {{access_token}}'
```

## Response

| Campo | Tipo | Descripción |
|-------|------|-------------|
| `horarioMercado` | boolean | Si al momento de la consulta se encontraba dentro del horario de mercado. |
| `quoteCurrency` | string | Moneda FIAT en que se expresa la cotización. Siempre `"ARS"`. |
| `quotes[].currency` | string | Criptomoneda siendo cotizada. |
| `quotes[].ask` | decimal | Monto en ARS necesario para comprar una unidad entera de la criptomoneda. |
| `quotes[].bid` | decimal | Monto en ARS obtenido al vender una unidad entera de la criptomoneda. |

## Códigos HTTP

| Código | Descripción |
|--------|-------------|
| `200` | Consulta exitosa |
| `422` | Cuenta inválida |
| `401` | Token de autenticación inválido |

# Endpoint — Consultar cotización reales

> Fuente: https://psp.bind.com.ar/developers/apis/consultar-cotizacion-brl
> Producto: Wallet — Pago QR PIX

## Descripción

Devuelve el precio de compra y venta del real brasileño en pesos argentinos.

Esta cotización debe ser sólo usada como información de referencia ya que no es vinculante a una posible compra. La cotización final para una compra será obtenida al leer un QR PIX.

## URL / Método

| Campo | Valor |
|-------|-------|
| Método | `GET` |
| URL (Staging) | `https://gw-staging-qrbind.epays.services/walletentidad-investment/v1/api/v1.201/Inversion/CotizacionBRL` |

## Bloque curl request

```bash
curl --location 'https://gw-staging-qrbind.epays.services/walletentidad-investment/v1/api/v1.201/Inversion/CotizacionBRL' \
--header 'Authorization: Bearer {{access_token}}'
```

## Response

| Campo | Tipo | Descripción |
|-------|------|-------------|
| `precioCompraBRL` | double | Precio de compra de 1 real brasileño en pesos argentinos. |
| `precioVentaBRL` | double | Precio de venta de 1 real brasileño en pesos argentinos. |
| `precioCompraUSD` | double | Precio de compra de 1 dólar en pesos argentinos. Valor considerado para la operatoria cambiaria de pesos a reales. |
| `precioVentaUSD` | double | Precio de venta de 1 dólar en pesos argentinos. Valor considerado para la operatoria cambiaria de pesos a reales. |
| `tiempoLimiteCotizacion` | datetime | Fecha y hora en que expirará la presente cotización. |

## Códigos HTTP

| Código | Descripción |
|--------|-------------|
| `200` | Consulta exitosa |
| `401` | Token de autenticación inválido |

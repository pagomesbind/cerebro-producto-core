# Endpoint — Leer QR PIX

> Fuente: https://psp.bind.com.ar/developers/apis/leer-qr-pix
> Producto: Wallet — Pago QR PIX

## Descripción

Devuelve la información obtenida al leer un QR PIX necesaria para luego iniciar el pago.

## URL / Método

| Campo | Valor |
|-------|-------|
| Método | `POST` |
| URL (Staging) | `https://gw-staging-qrbind.epays.services/walletentidad-operaciones/v1/api/v1.201/QrCodeAmount` |
| Content-Type | `application/json` |

## Parámetros del Request

| Parámetro | Tipo | Requerido | Descripción |
|-----------|------|-----------|-------------|
| `qrCode` | string | REQUIRED | String que conforma la imagen QR PIX. Resulta de leer e interpretar el código QR PIX que se quiere pagar. |

## Bloque curl request

```bash
curl --location 'https://gw-staging-qrbind.epays.services/walletentidad-operaciones/v1/api/v1.201/QrCodeAmount' \
--header 'Authorization: Bearer {{access_token}}' \
--header 'Content-Type: application/json' \
--data '{
"qrCode": "00020101021226770014BR.GOV.BCB.PIX000000000000000000000000000000530398654041.005802BR0000000000000000000000000000000000000999999999V999m99999b63042AB3"
}'
```

## Response

| Campo | Tipo | Descripción |
|-------|------|-------------|
| `idPix` | int | Identificador único de la intención de pago de Pix. |
| `montoBRL` | double | Monto en reales que debe abonarse. |
| `montoARS` | double | Monto en pesos argentinos que se debitarán a la cuenta para completar la operación. |
| `precioBRL` | double | Precio de cotización de compra de 1 real brasileño. |
| `precioUSD` | double | Precio de cotización de compra de 1 dólar utilizado como referencia para la operación cambiaria crossborder. |
| `tiempoLimiteCotizacion` | datetime | Fecha y hora en que expirará la presente cotización. |

## Códigos HTTP

| Código | Descripción |
|--------|-------------|
| `200` | Lectura de QR PIX exitosa (monto abierto o cerrado) |
| `422` | El QR es inválido |
| `401` | Token de autenticación inválido |

# Endpoint — Crear un link de pago 2.0

> Fuente: https://psp.bind.com.ar/developers/apis/boton20-crearlinkdepago
> Producto: Adquirencia — Botón Simple 2.0

## Descripción

Crea un link de pago asociado a una deuda pendiente que podrá pagarse con tarjeta, con QR o con CVU.

## URL / Método

| Campo | Valor |
|-------|-------|
| Método | `POST` |
| URL (Staging) | `https://gw-staging-qrbind.epays.services/bindentidad-cardnotpresent-v2/v2/api/v1.201/deuda` |
| Content-Type | `application/json-patch+json` |

## Parámetros del Request

| Parámetro | Tipo | Requerido | Descripción |
|-----------|------|-----------|-------------|
| `codigoDeuda` | string | REQUERIDO | Identificador externo de la Entidad. No se permite más de un link con el mismo codigoDeuda. |
| `codigoCaja` | string | REQUERIDO | Identificador de la caja en la que se imputará el cobro. |
| `codigoSucursal` | string | REQUERIDO | Identificador de la sucursal en la que se imputará el cobro. |
| `codigoComercio` | string | REQUERIDO | Identificador del comercio en el que se imputará el cobro. |
| `moneda` | string | REQUERIDO | Moneda de la deuda. Valores posibles: `"1"` (Pesos argentinos) |
| `motivo` | string | REQUERIDO | Es la descripción de la deuda a pagar. Se muestra como título en el detalle del pago en el checkout del link de pago. |
| `tipoOrden` | string | REQUERIDO | Tipo de orden. Valor fijo: `"1"` (Monto cerrado) |
| `montoTotal` | string | REQUERIDO | Importe de la deuda a pagar. |
| `fechaVencimiento` | string | REQUERIDO | Fecha y hora de vencimiento de la deuda y del link de pago. |
| `habilitaQR` | boolean | REQUERIDO | Indica si el link debe poder pagarse con QR. |
| `habilitaTransferencia` | string | REQUERIDO | Indica si el link debe poder pagarse con Transferencia a CVU. |
| `habilitaTarjeta` | string | REQUERIDO | Indica si el link debe poder pagarse con tarjetas. |
| `requiereProductos` | string | OPCIONAL | Indica si se requiere que los productos detallados en el objeto items de este request se registren especialmente en el sistema para luego asociarlo a las transacciones. Valor por defecto: false |
| `configuracionCheckout` | object | OPCIONAL | Objeto con información necesaria para configurar el medio de pago tarjeta. |
| `configuracionCheckout.successUrl` | string | OPCIONAL | Url a la cual el checkout redirigirá al usuario en caso de que el pago haya sido exitoso. Es obligatorio incluir el "http://" o "https://". |
| `configuracionCheckout.errorUrl` | string | OPCIONAL | Url a la cual el checkout redirigirá al usuario en caso de que el pago haya sido fallido. Es obligatorio incluir el "http://" o "https://". |
| `configuracionCheckout.items[{}]` | object | OPCIONAL | Array de objetos con información de cada item del detalle del pago. Cada objeto representa a un item y estos se muestran en el detalle del pago en el checkout del link de pago. Puede enviarse vacío. |
| `configuracionCheckout.items[{}].description` | string | REQUERIDO | Descripción del item. |
| `configuracionCheckout.items[{}].amount` | string | REQUERIDO | Importe del item. |
| `configuracionCheckout.items[{}].quantity` | string | REQUERIDO | Cantidad del item. |
| `configuracionCheckout.items[{}].code` | string | OPCIONAL | Código del item. |
| `configuracionCheckout.items[{}].additional` | string | OPCIONAL | Información adicional del item. |

## Bloque curl request

```bash
curl --location 'https://gw-staging-qrbind.epays.services/bindentidad-cardnotpresent-v2/v2/api/v1.201/deuda' \
--header 'Content-Type: application/json-patch+json' \
--header 'Cache-Control: no-cache' \
--header 'Authorization: Bearer {{access_token}}' \
--data '{
"CodigoDeuda": "ABC1573",
"codigoCaja": "B00000623451",
"codigoSucursal": "S18803",
"codigoComercio": "C22903",
"moneda": "1",
"motivo": "Pago de servicios",
"tipoOrden": "1",
"montoTotal": 19895.63,
"fechaVencimiento": "2025-09-30T15:47:21.190Z",
"habilitaQR": true,
"habilitaTransferencia": true,
"habilitaTarjeta": true,
"configuracionCheckout": {
"successUrl": "https://www.google.com",
"errorUrl": "https://www.bind.com.ar",
"items": [
{
"description": "Factura N° ABC456",
"amount": 18864.63,
"quantity": 1,
"code": "asd123",
"additional": null
},
{
"description": "Factura N° DEF789",
"amount": 1031.00,
"quantity": 1,
"code": "asd456",
"additional": null
}
]
}
}'
```

## Response

| Campo | Tipo | Descripción |
|-------|------|-------------|
| `id` | int | Id de la deuda creada. |
| `url` | string | Url del link de pago creado. |

## Códigos HTTP

| Código | Descripción |
|--------|-------------|
| `201` | Creación exitosa |
| `401` | Token de autenticación inválido |

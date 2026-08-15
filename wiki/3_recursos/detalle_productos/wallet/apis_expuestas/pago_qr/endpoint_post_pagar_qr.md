# Endpoint — Pagar QR interoperable

> Fuente: https://psp.bind.com.ar/developers/apis/pagar-qr
> Producto: Wallet — Pago QR

## Descripción

Instruye un PCT en Coelsa. Requiere información obtenida luego de CONSULTAR INFORMACIÓN PARA PAGAR UN QR.

El resultado definitivo del pago puede darse en la respuesta de este endpoint, siempre y cuando Coelsa resuelva la transacción rápidamente.

El resultado definitivo del pago puede no ser inmediato, por lo tanto para conocerlo hay que esperar unos segundos. Se conoce vía el webhook del evento pago QR o consultando la información de la operación.

## URL / Método

| Campo | Valor |
|-------|-------|
| Método | `POST` |
| URL (Staging) | `https://gw-staging-qrbind.epays.services/walletentidad-operaciones/v1/api/v1.201/pagoQR` |
| Content-Type | `application/json` |

## Parámetros del Request

| Parámetro | Tipo | Requerido | Descripción |
|-----------|------|-----------|-------------|
| `cvuOrigen` | string | REQUIRED | CVU del comprador desde donde se debitará el saldo. |
| `cuitOrigen` | string | REQUIRED | CUIT del comprador. |
| `cbuCvuVendedor` | string | REQUIRED | CBU/CVU del comercio. Es `collector.account` que devuelve Leer QR. |
| `cuitVendedor` | string | REQUIRED | CUIT del comercio. Es `collector.identification_number` que devuelve Leer QR. |
| `transaccionId` | string | REQUIRED | Identificador de la orden. Es `order.id` que devuelve Leer QR. |
| `importe` | double | REQUIRED | Importe a pagar. Es `order.total_amount` de Leer QR. En QR monto abierto, el valor lo determina el comprador. |
| `descripcion` | string | OPTIONAL | Descripción de la venta. |
| `textoQR` | string | REQUIRED | String del QR (resultado de leer e interpretar el código QR). |
| `idExterno` | string | OPTIONAL | Identificador externo de la entidad. Longitud máxima: 50 caracteres. |

## Bloque curl request

```bash
curl --location 'https://gw-staging-qrbind.epays.services/walletentidad-operaciones/v1/api/v1.201/pagoQR' \
--header 'Authorization: Bearer {{access_token}}' \
--header 'Content-Type: application/json' \
--data '{
"cvuOrigen": "0000532609100002749314",
"cuitOrigen": "20374312759",
"cbuCvuVendedor": "0000532607300067079179",
"cuitVendedor": "30707101020",
"transaccionId": "9OA2264ED6A87C78B00000453831000000000000ET9000ITOA8986AACAD4",
"importe": 12.22,
"descripcion": "null",
"textoQR": "00020101021102080000000041370012com.testbind...",
"idExterno": "7894"
}'
```

## Response

| Campo | Tipo | Descripción |
|-------|------|-------------|
| `operacionId` | int | Identificador de la operación creada. |
| `operacionIdExterno` | string | Identificador de Coelsa. El más importante para reclamos y conciliaciones. |
| `estadoExterno` | string | Descripción del estado que devolvió Coelsa. |
| `estadoId` | int | Estado en el sistema. Valores: 1=A procesar, 2=Aprobada, 3=Rechazada, 4=A consultar, 5=Auditar, 6=Devuelta, 7=Devuelta parcialmente |
| `origenCuentaId` | int | Identificador de la cuenta de la que se debitaron los fondos. |
| `fechaNegocio` | datetime | Fecha y hora en que se instruyó la creación de la operación. |
| `puntaje` | int | No se utiliza en este momento. Valores posibles: `null` o `0`. |
| `vendedorCuit` | string | CUIT del comercio. |
| `vendedorCbuCvu` | string | CBU/CVU del comercio. |
| `vendedorNombre` | string | Nombre del comercio. |
| `fechaExpiracion` | datetime | Fecha y hora de expiración de la operación. |
| `comprobanteId` | int | Identificador del comprobante de débito del saldo. |
| `comprobanteDevolucionId` | int | Identificador del comprobante de crédito por reversa (si el pago falló). |
| `mensajeAdicional` | string | Descripción adicional del estado enviado por Coelsa. |
| `estaFinalizado` | boolean | Si la operación tiene estado definitivo. |
| `estaRechazado` | boolean | Si el pago fue rechazado definitivamente. |
| `estaAAuditar` | boolean | Si está pendiente de conciliación automática o revisión manual. |
| `estaPendiente` | boolean | Si aún no se ha intentado instruir en el procesador externo. |

## Códigos HTTP

| Código | Descripción |
|--------|-------------|
| `200` | Creación del pago exitoso (no necesariamente completado) |
| `500` | textoQR inválido |
| `422` | CVU y CUIT de origen no coinciden con datos de una cuenta |
| `422` | Cuenta origen inexistente |
| `400` | El formato de un dato es inválido |
| `401` | Token de autenticación inválido |

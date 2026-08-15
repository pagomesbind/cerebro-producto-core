# Endpoint — Pagar QR PIX

> Fuente: https://psp.bind.com.ar/developers/apis/pagar-qr-pix
> Producto: Wallet — Pago QR PIX

## Descripción

Inicia el procesamiento del pago en un QR PIX previamente leído.

## URL / Método

| Campo | Valor |
|-------|-------|
| Método | `POST` |
| URL (Staging) | `https://gw-staging-qrbind.epays.services/walletentidad-operaciones/v1/api/v1.201/ProcesarPagoQRPix` |
| Content-Type | `application/json` |

## Parámetros del Request

| Parámetro | Tipo | Requerido | Descripción |
|-----------|------|-----------|-------------|
| `idCuenta` | int | REQUIRED | Identificador de la cuenta desde la que se quiere realizar la operación. |
| `idPix` | int | REQUIRED | Identificador de la intención de pago PIX obtenido en la lectura. |
| `idExterno` | string | OPTIONAL | Identificador externo de la organización para asociar a esta operación. |
| `montoBRL` | double | REQUIRED | Monto en reales a pagar. |

## Bloque curl request

```bash
curl --location 'https://gw-staging-qrbind.epays.services/walletentidad-operaciones/v1/api/v1.201/ProcesarPagoQRPix' \
--header 'Authorization: Bearer {{access_token}}' \
--header 'Content-Type: application/json' \
--data '{
"idCuenta": 16988,
"idPix": 4503,
"idExterno": "ABC123",
"montoBRL": 143.76
}'
```

## Response

| Campo | Tipo | Descripción |
|-------|------|-------------|
| `operacionId` | int | Identificador de la operación creada. |
| `operacionIdExterno` | string | Identificador externo de la organización asociado a la operación. |
| `estadoId` | int | Estado en el sistema. Valores: 1=A procesar, 2=Aprobada, 3=Rechazada, 4=A consultar, 5=Auditar, 6=Devuelta, 7=Devuelta parcialmente |
| `origenCuentaId` | int | Identificador de la cuenta que realiza la operación. |
| `coelsaId` | string | Identificador de Coelsa. El más importante para reclamos y conciliaciones. |
| `fechaInicio` | datetime | Fecha y hora en que inició la transferencia en el banco. |
| `fechaFin` | datetime | Fecha y hora en que finalizó la transferencia en el banco. |
| `fechaNegocio` | datetime | Fecha y hora en que se instruyó la creación. |
| `importe` | double | Importe de la transferencia. |
| `cvuOrigen` | string | CVU desde el que se originó la operación. |
| `referencia` | string | Referencia de la operación. |
| `concepto` | string | Concepto de la operación. |
| `cvuCbuContraparte` | string | CBU/CVU de la cuenta destino. |
| `aliasContraparte` | string | Alias de la cuenta destino. |
| `nombreContraparte` | string | Nombre del titular de la cuenta destino. |
| `cuitCuilContraparte` | string | CUIT/CUIL del titular de la cuenta destino. |
| `comprobanteId` | int | Comprobante de débito del saldo. |
| `comprobanteDevolucionId` | int | Comprobante de crédito por reversa (si el pago falló). |
| `mensajeAdicional` | string | Descripción adicional del estado enviado por el banco. |
| `esTransferenciaInterna` | boolean | Si la transferencia fue entre cuentas de la misma entidad. |
| `estaFinalizada` | boolean | Si la operación tiene estado definitivo. |
| `estaRechazada` | boolean | Si fue rechazada definitivamente. |
| `estaAAuditar` | boolean | Si está pendiente de conciliación o revisión manual. |
| `estaPendiente` | boolean | Si aún no fue instruida en el procesador externo. |

## Códigos HTTP

| Código | Descripción |
|--------|-------------|
| `200` | Pago PIX exitoso |
| `200` | Pago PIX fallido |
| `200` | Pago PIX en proceso |
| `422` | El tiempo para pagar expiró |
| `401` | Token de autenticación inválido |

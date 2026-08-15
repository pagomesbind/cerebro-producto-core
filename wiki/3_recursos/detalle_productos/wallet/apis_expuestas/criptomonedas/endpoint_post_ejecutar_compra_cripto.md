# POST — Ejecutar Compra de Cripto

> Fuente: https://psp.bind.com.ar/developers/apis/ejecutar-compra-cripto
> Producto: Wallet — Cripto

## Descripción

Ejecuta una intención de compra de una criptomoneda previamente creada.

## URL / Método

| Campo | Valor |
|-------|-------|
| Método | `POST` |
| URL (Staging) | `https://gw-staging-qrbind.epays.services/walletentidad-investment/v1/api/v1.201/EjecutarCompraCripto` |

## Parámetros del Request

| Parámetro | Tipo | Requerido | Descripción |
|-----------|------|-----------|-------------|
| `intencionId` | int | OPTIONAL* | Identificador de la intención de compra. Obligatorio si no se envía `intencionEntidadId`. |
| `intencionEntidadId` | string | OPTIONAL* | Identificador externo de la intención. Obligatorio si no se envía `intencionId`. |
| `idCuenta` | int | REQUIRED | Identificador de la cuenta. |
| `codigoConfirmacion` | string | OPTIONAL | Código de confirmación enviado al crear la intención. Obligatorio sólo si la intención lo requiere. |

## Bloque curl request

```bash
curl --location 'https://gw-staging-qrbind.epays.services/walletentidad-investment/v1/api/v1.201/EjecutarCompraCripto' \
--header 'Authorization: {{access_token}}' \
--data '{
  "intencionId": 15894,
  "intencionEntidadId": null,
  "idCuenta": 276058,
  "codigoConfirmacion": null
}'
```

## Response

| Campo | Tipo | Descripción |
|-------|------|-------------|
| `intencionId` | int | Identificador de la intención. |
| `intencionEntidadId` | string | Identificador externo de la intención. |
| `monedaCripto` | string | Criptomoneda a comprar. |
| `montoCripto` | double | Cantidad de unidades de criptomoneda a comprar. |
| `monedaCambio` | string | Moneda a cambiar por criptomonedas. |
| `montoCambio` | double | Monto total a gastar, incluyendo gastos. |
| `totalGastos` | double | Monto de comisiones y gastos incluidos. |
| `cargo` | double | Comisión de Bind PSP. |
| `precioDolarReferencia` | double | Precio de compra del dólar, neto de gastos. |
| `fechaHoraCreacion` | datetime | Fecha y horario de creación de la intención. |
| `operacionTipoNombre` | string | Denominación del tipo de operación. |
| `cuentaId` | int | Identificador de la cuenta. |
| `estado` | string | `"EN_PROCESO"` = iniciada, en procesamiento (no definitivo). `"RECHAZADA"` = no se inició (definitivo). `"APROBADA"` = completada (definitivo). |
| `priceHash` | string | Código único del precio fijado. |
| `fechaHoraActualizacion` | datetime | Fecha y horario de última actualización. |
| `operacionId` | int | Identificador de la operación asociada. |
| `comprobanteId` | int | Comprobante del débito de moneda FIAT. |
| `reversaComprobanteId` | int | Comprobante del crédito por reversa. |
| `cargoComprobanteId` | int | Comprobante del débito de comisión. |
| `cargoReversaComprobanteId` | int | Comprobante del crédito por reversa de comisión. |

## Códigos HTTP

| Código | Descripción |
|--------|-------------|
| `200` | Ejecución exitosa |
| `422` | Cuenta inválida |
| `422` | Cuenta deshabilitada |
| `422` | Identificador externo no existente |
| `401` | Token de autenticación inválido |

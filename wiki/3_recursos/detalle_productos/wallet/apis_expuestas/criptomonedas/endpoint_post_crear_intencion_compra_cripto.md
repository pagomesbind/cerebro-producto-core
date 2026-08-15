# POST — Crear Intención de Compra Cripto

> Fuente: https://psp.bind.com.ar/developers/apis/crear-intencion-de-compra-cripto
> Producto: Wallet — Cripto

## Descripción

Crea una intención de compra de una criptomoneda.

## URL / Método

| Campo | Valor |
|-------|-------|
| Método | `POST` |
| URL (Staging) | `https://gw-staging-qrbind.epays.services/walletentidad-investment/v1/api/v1.201/IntencionCompraCripto` |

## Parámetros del Request

| Parámetro | Tipo | Requerido | Descripción |
|-----------|------|-----------|-------------|
| `idCuenta` | int | REQUIRED | Identificador de la cuenta. |
| `monedaCripto` | string | REQUIRED | Criptomoneda a comprar. |
| `montoCripto` | double | OPTIONAL* | Cantidad de unidades de criptomoneda a comprar. Requerido si no se envía `montoCambio`. |
| `monedaCambio` | string | REQUIRED | Moneda FIAT a cambiar por criptomonedas. |
| `montoCambio` | double | OPTIONAL* | Monto de moneda FIAT a utilizar, incluyendo gastos. Requerido si no se envía `montoCripto`. |
| `idExterno` | string | OPTIONAL | Identificador externo de la entidad. No puede repetirse entre intenciones. |
| `priceHash` | string | OPTIONAL | Código único que representa el precio fijado y su vencimiento. Se obtiene del endpoint Consultar cotización. |

> \* Se debe enviar `montoCripto` o `montoCambio`, no ambos ni ninguno.

## Bloque curl request

```bash
curl --location 'https://gw-staging-qrbind.epays.services/walletentidad-investment/v1/api/v1.201/IntencionCompraCripto' \
--header 'Authorization: {{access_token}}' \
--data '{
  "idCuenta": 276058,
  "monedaCripto": "BTC",
  "montoCripto": 0.25,
  "monedaCambio": "ARS",
  "montoCambio": null,
  "idExterno": null,
  "priceHash": "xwY250QG1haWxpbmF0b3IuY29tIiwib3Mi"
}'
```

## Response

| Campo | Tipo | Descripción |
|-------|------|-------------|
| `intencionId` | int | Identificador de la intención creada. |
| `intencionEntidadId` | string | Identificador externo indicado por la entidad. |
| `monedaCripto` | string | Criptomoneda a comprar. |
| `montoCripto` | double | Cantidad de unidades de criptomoneda a comprar. |
| `monedaCambio` | string | Moneda a cambiar por criptomonedas. |
| `montoCambio` | double | Monto total a gastar, incluyendo gastos. |
| `totalGastos` | double | Monto estimado de comisiones y gastos incluidos en la operación. |
| `cargo` | double | Comisión de Bind PSP (porcentaje del monto original). |
| `precioDolarReferencia` | double | Precio de compra del dólar, neto de gastos. |
| `fechaHoraCreacion` | datetime | Fecha y horario de creación de la intención. |
| `operacionTipoNombre` | string | Denominación del tipo de operación financiera a ejecutarse. |
| `cuentaId` | int | Identificador de la cuenta. |
| `estado` | string | `"PENDIENTE"` = La intención fue creada y está en espera de ser ejecutada. |
| `requiereCodigoConfirmacion` | boolean | Si la ejecución requiere un código de confirmación enviado por email al dueño de la cuenta. |

## Códigos HTTP

| Código | Descripción |
|--------|-------------|
| `200` | Creación de intención exitosa |
| `422` | Cuenta inválida |
| `422` | Cuenta deshabilitada |
| `422` | Identificador externo no existente |
| `401` | Token de autenticación inválido |

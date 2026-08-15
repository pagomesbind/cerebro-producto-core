# POST — Crear Intención de Venta Dólar CCL

> Fuente: https://psp.bind.com.ar/developers/apis/crear-intencion-de-venta-dolar-ccl
> Producto: Wallet — Dólar CCL

## Descripción

Crea una intención de venta de dólar CCL.

## URL / Método

| Campo | Valor |
|-------|-------|
| Método | `POST` |
| URL (Staging) | `https://gw-staging-qrbind.epays.services/walletentidad-investment/v1/api/v1.201/IntencionVentaCCL` |

## Parámetros del Request

| Parámetro | Tipo | Requerido | Descripción |
|-----------|------|-----------|-------------|
| `idCuenta` | int | REQUIRED | Identificador de la cuenta. |
| `monto` | double | REQUIRED | Monto en dólares que se desea vender. |
| `idExterno` | string | OPTIONAL | Identificador externo de la entidad. No puede repetirse entre intenciones. |
| `priceHash` | string | OPTIONAL | Código único del precio fijado. Solo aplica para modelo Combi. |

## Bloque curl request

```bash
curl --location 'https://gw-staging-qrbind.epays.services/walletentidad-investment/v1/api/v1.201/IntencionVentaCCL' \
--header 'Content-Type: application/json' \
--header 'Cache-Control: no-cache' \
--header 'Authorization: Bearer {{access_token}}' \
--data '{
  "idCuenta": 276058,
  "monto": 100,
  "idExterno": null,
  "priceHash": null
}'
```

## Response

| Campo | Tipo | Descripción |
|-------|------|-------------|
| `intencionId` | int | Identificador de la intención creada. |
| `intencionEntidadId` | string | Identificador externo indicado por la entidad. |
| `monto` | double | Monto en dólares que se solicitó vender. |
| `montoNeto` | double | Monto en USD estimado final incluyendo gastos y comisiones. |
| `montoBruto` | double | Monto en USD estimado a cursar en el sistema financiero (neto de gastos). |
| `vueltoEstimado` | double | Monto estimado en ARS de vuelto a devolver. |
| `totalGastos` | double | Monto de comisiones y gastos. |
| `gastosbroker` | double | Arancel del procesador. |
| `cargo` | double | Comisión de Bind PSP. |
| `precioDolar` | double | Precio de venta del dólar (incluye gastos y comisiones). |
| `precioDolarReferencia` | double | Precio del dólar informado por el procesador. |
| `montoEsperado` | double | Deprecado. Valor fijo: `null`. |
| `montoAObtener` | double | Monto estimado en ARS a obtener. En modelo Combi es el monto final. |
| `fechaHoraVencimiento` | datetime | Fecha y horario de expiración de la intención. |
| `fechaHoraCreacion` | datetime | Fecha y horario de creación. |
| `fechaHoraFinalizacionIntencion` | datetime | Fecha y horario de fin esperado de la operación. |
| `operacionTipoNombre` | string | Siempre `"VENTADOLARCCL"`. |
| `cuentaId` | int | Identificador de la cuenta. |
| `horarioMercado` | boolean | Si al crear la intención se encontraba dentro del horario de mercado. |
| `estado` | string | `"PENDIENTE"` = creada, en espera de ejecución. |
| `priceHash` | string | Código del precio fijado (solo modelo Combi). |

## Códigos HTTP

| Código | Descripción |
|--------|-------------|
| `200` | Creación de intención exitosa |
| `422` | Cuenta inválida |
| `422` | Cuenta deshabilitada |
| `422` | Identificador externo no existente |
| `401` | Token de autenticación inválido |

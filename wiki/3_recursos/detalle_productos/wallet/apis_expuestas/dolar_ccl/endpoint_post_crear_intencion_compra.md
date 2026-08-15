# POST — Crear Intención de Compra Dólar CCL

> Fuente: https://psp.bind.com.ar/developers/apis/inversiones-crear-intencion-de-compra-dolar-ccl
> Producto: Wallet — Dólar CCL

## Descripción

Crea una intención de compra de dólar CCL.

## URL / Método

| Campo | Valor |
|-------|-------|
| Método | `POST` |
| URL (Staging) | `https://gw-staging-qrbind.epays.services/walletentidad-investment/v1/api/v1.201/IntencionCompraCCL` |

## Parámetros del Request

| Parámetro | Tipo | Requerido | Descripción |
|-----------|------|-----------|-------------|
| `idCuenta` | int | REQUIRED | Identificador de la cuenta. |
| `monto` | double | REQUIRED | Monto en pesos argentinos que se desea comprar. |
| `idExterno` | string | OPTIONAL | Identificador externo de la entidad. No puede repetirse entre intenciones. |
| `priceHash` | string | OPTIONAL | Código único del precio fijado. Solo aplica para modelo Combi. |

## Bloque curl request

```bash
curl --location 'https://gw-staging-qrbind.epays.services/walletentidad-investment/v1/api/v1.201/IntencionCompraCCL' \
--header 'Content-Type: application/json' \
--header 'Cache-Control: no-cache' \
--header 'Authorization: {{access_token}}' \
--data '{
  "idCuenta": 276058,
  "monto": 70000,
  "idExterno": null,
  "priceHash": null
}'
```

## Response

| Campo | Tipo | Descripción |
|-------|------|-------------|
| `intencionId` | int | Identificador de la intención creada. |
| `intencionEntidadId` | string | Identificador externo indicado por la entidad. |
| `monto` | double | Monto en ARS que se solicitó comprar. |
| `montoNeto` | double | Monto en ARS estimado final incluyendo gastos. |
| `montoBruto` | double | Monto en ARS estimado a invertir. |
| `vueltoEstimado` | double | Monto estimado en ARS a devolver al saldo (vuelto). |
| `totalGastos` | double | Monto estimado de comisiones y gastos. |
| `gastosbroker` | double | Arancel del procesador. |
| `cargo` | double | Comisión de Bind PSP. |
| `precioDolar` | double | Precio de compra del dólar de referencia (incluye comisiones). |
| `precioDolarReferencia` | double | Precio del dólar informado por el procesador. |
| `montoEsperado` | double | Deprecado. Valor fijo: `null`. |
| `montoAObtener` | double | Monto estimado en dólares a obtener. En modelo Combi es el monto final. |
| `fechaHoraVencimiento` | datetime | Fecha y horario de expiración de la intención. |
| `fechaHoraCreacion` | datetime | Fecha y horario de creación. |
| `fechaHoraFinalizacionIntencion` | datetime | Fecha y horario de fin esperado de la operación. |
| `operacionTipoNombre` | string | Siempre `"COMPRADOLARCCL"`. |
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

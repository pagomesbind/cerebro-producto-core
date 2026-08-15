# POST — Ejecutar Compra de Dólar CCL

> Fuente: https://psp.bind.com.ar/developers/apis/inversiones-ejecutar-una-compra-de-dolar-ccl
> Producto: Wallet — Dólar CCL

## Descripción

Ejecuta una compra de dólar CCL a partir de una intención de compra previamente creada.

## URL / Método

| Campo | Valor |
|-------|-------|
| Método | `POST` |
| URL (Staging) | `https://gw-staging-qrbind.epays.services/walletentidad-investment/v1/api/v1.201/EjecutarCompraDolarCCL` |

## Parámetros del Request

| Parámetro | Tipo | Requerido | Descripción |
|-----------|------|-----------|-------------|
| `intencionId` | int | OPTIONAL* | Identificador de la intención de compra. Obligatorio si no se envía `intencionEntidadId`. |
| `intencionEntidadId` | string | OPTIONAL* | Identificador externo de la intención. Obligatorio si no se envía `intencionId`. |
| `cuentaId` | int | REQUIRED | Identificador de la cuenta. |
| `ddjjAceptada` | boolean | REQUIRED | Indica si el usuario aceptó la declaración jurada. |
| `ddjjAceptadaFechaHora` | datetime | REQUIRED | Fecha y hora en que el usuario aceptó la declaración jurada. |

## Bloque curl request

```bash
curl --location 'https://gw-staging-qrbind.epays.services/walletentidad-investment/v1/api/v1.201/EjecutarCompraDolarCCL' \
--header 'Authorization: {{access_token}}' \
--data '{
  "intencionId": 282,
  "intencionEntidadId": null,
  "cuentaId": 276058,
  "ddjjAceptada": true,
  "ddjjAceptadaFechaHora": "2024-12-19T18:03:47"
}'
```

## Response

| Campo | Tipo | Descripción |
|-------|------|-------------|
| `intencionId` | int | Identificador de la intención. |
| `intencionEntidadId` | string | Identificador externo indicado por la entidad. |
| `operacionId` | int | Identificador de la operación creada. |
| `operacionBrokerId` | string | Identificador del procesador. |
| `ddjjId` | string | Identificador de la declaración jurada aceptada. |
| `ddjjAceptadaFechaHora` | datetime | Fecha y hora en que se aceptó la DDJJ. |
| `monto` | double | Monto en ARS que se solicitó comprar. |
| `montoNeto` | double | Monto en ARS estimado final incluyendo gastos. En modelo Combi es el valor final. |
| `montoBruto` | double | Monto en ARS estimado a invertir. En modelo Combi es el valor final. |
| `vueltoEstimado` | double | Monto estimado en ARS de vuelto a devolver. En modelo Combi es `0`. |
| `totalGastos` | double | Monto de comisiones y gastos. |
| `gastosBroker` | double | Arancel del procesador. |
| `cargo` | double | Comisión de Bind PSP. |
| `precioDolar` | double | Precio de compra del dólar (incluye gastos y comisiones). |
| `precioDolarReferencia` | double | Precio del dólar informado por el procesador (neto de gastos). |
| `montoEsperado` | double | Deprecado. Valor fijo: `null`. |
| `montoAObtener` | double | Monto estimado en dólares a obtener. |
| `debitoComprobanteId` | int | Comprobante del débito de saldo del cliente. |
| `creditoComprobanteId` | int | Comprobante del crédito por reversa. |
| `fechaHoraCreacionEnBroker` | datetime | Fecha y horario de ingreso al broker. |
| `fechaHoraCreacion` | datetime | Fecha y horario de creación de la intención. |
| `operacionTipoNombre` | string | Denominación del tipo de operación. |
| `cuentaId` | int | Identificador de la cuenta. |
| `estado` | string | `"EN_PROCESO"` = en procesamiento, `"RECHAZADA"` = no se inició, `"COMPLETADA_PARCIAL"` = compra del bono en ARS completada (primera parte). |
| `motivoRechazo` | string | Motivo de rechazo (si aplica). |
| `montoOrdenado` | double | Monto enviado al procesador. |
| `cargoDebitoComprobanteId` | int | Comprobante del débito de comisión. |
| `cargoCreditoComprobanteId` | int | Comprobante del crédito de comisión por reversa. |
| `priceHash` | string | Código del precio fijado (solo modelo Combi). |

## Códigos HTTP

| Código | Descripción |
|--------|-------------|
| `200` | Ejecución exitosa, operación en proceso |
| `401` | Token de autenticación inválido |

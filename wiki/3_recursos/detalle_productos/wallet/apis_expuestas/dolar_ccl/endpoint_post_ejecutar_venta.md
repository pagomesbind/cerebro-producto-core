# POST — Ejecutar Venta de Dólar CCL

> Fuente: https://psp.bind.com.ar/developers/apis/ejecutar-una-venta-de-dolar-ccl
> Producto: Wallet — Dólar CCL

## Descripción

Ejecuta una venta de dólar CCL a partir de una intención de venta previamente creada.

## URL / Método

| Campo | Valor |
|-------|-------|
| Método | `POST` |
| URL (Staging) | `https://gw-staging-qrbind.epays.services/walletentidad-investment/v1/api/v1.201/EjecutarVentaDolarCCL` |

## Parámetros del Request

| Parámetro | Tipo | Requerido | Descripción |
|-----------|------|-----------|-------------|
| `intencionId` | int | OPTIONAL* | Identificador de la intención de venta. Obligatorio si no se envía `intencionEntidadId`. |
| `intencionEntidadId` | string | OPTIONAL* | Identificador externo de la intención. Obligatorio si no se envía `intencionId`. |
| `cuentaId` | int | REQUIRED | Identificador de la cuenta. |
| `ddjjAceptada` | boolean | REQUIRED | Indica si el usuario aceptó la declaración jurada. |
| `ddjjAceptadaFechaHora` | datetime | REQUIRED | Fecha y hora en que el usuario aceptó la declaración jurada. |

## Bloque curl request

```bash
curl --location 'https://gw-staging-qrbind.epays.services/walletentidad-investment/v1/api/v1.201/EjecutarVentaDolarCCL' \
--header 'Content-Type: application/json' \
--header 'Cache-Control: no-cache' \
--header 'Authorization: Bearer {{access_token}}' \
--data '{
  "intencionId": 388,
  "intencionEntidadId": null,
  "cuentaId": 276058,
  "ddjjAceptada": true,
  "ddjjAceptadaFechaHora": "2025-02-03T19:52:15"
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
| `monto` | double | Monto en dólares que se solicitó vender. |
| `montoNeto` | double | Monto en USD estimado final incluyendo gastos. |
| `montoBruto` | double | Monto en USD estimado a invertir. |
| `vueltoEstimado` | double | Monto estimado en USD de vuelto. En modelo Combi es `0`. |
| `totalGastos` | double | Monto de comisiones y gastos. |
| `gastosbroker` | double | Arancel del procesador (en ARS). |
| `cargo` | double | Comisión de Bind PSP (en ARS). |
| `precioDolar` | double | Precio de venta del dólar (incluye gastos y comisiones). |
| `precioDolarReferencia` | double | Precio del dólar informado por el procesador (neto de gastos). |
| `montoEsperado` | double | Monto esperado en ARS según cálculo con `precioDolar`. |
| `montoAObtener` | double | Monto estimado en ARS a obtener. |
| `fechaHoraCreacionEnBroker` | datetime | Fecha y horario de ingreso al broker. |
| `fechaHoraCreacion` | datetime | Fecha y horario de creación de la intención. |
| `fechaHoraFinalizacionIntencion` | datetime | Fecha y horario de fin esperado de la operación. |
| `fechaHoraFinalizacionVenta` | datetime | Fecha y horario de fin de la operación de venta. |
| `operacionTipoNombre` | string | Denominación del tipo de operación. |
| `cuentaId` | int | Identificador de la cuenta. |
| `estado` | string | `"EN_PROCESO"` = en procesamiento, `"RECHAZADA"` = no se inició. |
| `motivoRechazo` | string | Motivo de rechazo (si aplica). |
| `montoOrdenado` | double | Monto enviado al procesador. |
| `priceHash` | string | Código del precio fijado (solo modelo Combi). |

## Códigos HTTP

| Código | Descripción |
|--------|-------------|
| `200` | Ejecución exitosa, operación en proceso |
| `401` | Token de autenticación inválido |

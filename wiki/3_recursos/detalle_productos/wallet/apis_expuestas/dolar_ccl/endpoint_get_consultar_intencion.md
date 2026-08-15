# GET — Consultar Intención (Dólar CCL)

> Fuente: https://psp.bind.com.ar/developers/apis/inversiones-consultar-intencion
> Producto: Wallet — Dólar CCL

## Descripción

Obtiene la información de una intención de compra o venta de dólar CCL por ID o ID externo.

## URL / Método

| Campo | Valor |
|-------|-------|
| Método | `GET` |
| URL (Staging) | `https://gw-staging-qrbind.epays.services/walletentidad-investment/v1/api/v1.201/Intencion` |

## Parámetros del Request

| Parámetro | Tipo | Requerido | Descripción |
|-----------|------|-----------|-------------|
| `IntencionId` | int | OPTIONAL | Identificador de la intención. Opcional si se envía `IntencionEntidadId`. |
| `IntencionEntidadId` | string | OPTIONAL | Identificador externo de la intención. Opcional si se envía `IntencionId`. |

## Bloque curl request

```bash
curl --location 'https://gw-staging-qrbind.epays.services/walletentidad-investment/v1/api/v1.201/Intencion?IntencionId=282' \
--header 'Cache-Control: no-cache' \
--header 'Authorization: Bearer {{access_token}}'
```

## Response

| Campo | Tipo | Descripción |
|-------|------|-------------|
| `intencionId` | int | Identificador de la intención. |
| `intencionEntidadId` | string | Identificador externo indicado por la entidad. |
| `operacionId` | int | Identificador de la operación asociada. |
| `operacionBrokerId` | string | Identificador del procesador. |
| `ddjjId` | string | Identificador de la declaración jurada aceptada. |
| `ddjjAceptadaFechaHora` | datetime | Fecha y hora en que se aceptó la DDJJ. |
| `monto` | double | Monto que se solicitó operar. |
| `montoNeto` | double | Monto estimado final total incluyendo gastos. |
| `montoBruto` | double | Monto estimado a invertir en el mercado (sin gastos). |
| `totalGastos` | double | Monto de comisiones y gastos en ARS. |
| `vueltoEstimado` | double | Monto estimado de vuelto en ARS. |
| `montoOrdenado` | double | Monto enviado al procesador. |
| `gastosBroker` | double | Arancel del procesador (en ARS). |
| `cargo` | double | Comisión de Bind PSP. |
| `precioDolar` | double | Precio de compra/venta del dólar de referencia para esta operación. |
| `precioDolarReferencia` | double | Precio del dólar informado por el procesador. |
| `montoEsperado` | double | Monto esperado según cálculo con `precioDolar`. |
| `montoAObtener` | double | Monto estimado a obtener. |
| `debitoComprobanteId` | int | Comprobante del débito de ARS. |
| `creditoComprobanteId` | int | Comprobante del crédito de ARS. |
| `montoInvertido` | double | Monto final gastado. Se conoce al concretarse la compra del bono. |
| `montoObtenido` | double | Monto final obtenido. Se conoce al concretarse la venta del bono. |
| `vuelto` | double | Monto final del vuelto por la compra. |
| `vueltoComprobanteId` | int | Comprobante del crédito por vuelto. |
| `cargoDebitoComprobanteId` | int | Comprobante del débito de comisión. |
| `cargoCreditoComprobanteId` | int | Comprobante del crédito por reversa de comisión. |
| `operacionUltimoStatus` | string | Descripción del último status del procesador. |
| `fechaHoraVencimiento` | datetime | Fecha y horario de expiración. |
| `fechaHoraOperacionUltimoStatus` | datetime | Fecha y horario de última actualización. |
| `fechaHoraCreacionEnBroker` | datetime | Fecha y horario de ingreso al broker. |
| `fechaHoraFinalizacionIntencion` | datetime | Fecha y horario de fin de la intención. |
| `fechaHoraFinalizacion` | datetime | Fecha y horario de fin esperado en el mercado. |
| `fechaHoraCreacion` | datetime | Fecha y horario de creación. |
| `fechaHoraUltimaModificacion` | datetime | Fecha y horario de última modificación. |
| `vencida` | boolean | Si la intención se encuentra vencida. |
| `procesadorNombre` | string | Nombre del procesador externo. |
| `operacionTipo` | string | Denominación del tipo de operación. |
| `cuentaId` | int | Identificador de la cuenta. |
| `horarioMercado` | boolean | Si al crear la intención se encontraba dentro del horario de mercado. |
| `estado` | string | `"PENDIENTE"` / `"EN_PROCESO"` / `"RECHAZADA"` / `"COMPLETADA_PARCIAL"` (solo compra) / `"APROBADA"` / `"AUDITAR"` (resolución manual en 48hs hábiles) |
| `motivoRechazo` | string | Motivo de rechazo (si aplica). |
| `brokerInfo` | string | Información de auditoría del procesador. |
| `priceHash` | string | Código del precio fijado (solo modelo Combi). |

## Códigos HTTP

| Código | Descripción |
|--------|-------------|
| `200` | Consulta exitosa |
| `422` | Intención no encontrada / inexistente |
| `401` | Token de autenticación inválido |

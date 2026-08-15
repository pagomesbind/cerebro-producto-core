# GET — Consultar Intención (Cripto)

> Fuente: https://psp.bind.com.ar/developers/apis/consultar-intencion-cripto
> Producto: Wallet — Cripto

## Descripción

Devuelve la información actual de una intención de compra o de venta de cripto.

## URL / Método

| Campo | Valor |
|-------|-------|
| Método | `GET` |
| URL (Staging) | `https://gw-staging-qrbind.epays.services/walletentidad-investment/v1/api/v1.201/IntencionCripto` |

## Parámetros del Request

| Parámetro | Tipo | Requerido | Descripción |
|-----------|------|-----------|-------------|
| `intencionId` | int | OPTIONAL | Identificador de la intención de cripto. |
| `intencionEntidadId` | string | OPTIONAL | Identificador externo de la intención indicado por la entidad. |

## Bloque curl request

```bash
curl -v -X GET "https://gw-staging-qrbind.epays.services/walletentidad-investment/v1/api/v1.201/IntencionCripto?IntencionId=408&IntencionEntidadId=" \
-H "Authorization: Bearer {{access_token}}"
```

## Response

| Campo | Tipo | Descripción |
|-------|------|-------------|
| `intencionId` | int | Identificador de la intención. |
| `intencionEntidadId` | string | Identificador externo indicado por la entidad. |
| `cuentaId` | int | Identificador de la cuenta. |
| `estado` | string | `"PENDIENTE"` = creada, en espera. `"EN_PROCESO"` = iniciada, procesando (no definitivo). `"RECHAZADA"` = no se inició (definitivo). `"APROBADA"` = completada (definitivo). |
| `monedaCripto` | string | Criptomoneda operada. |
| `montoCripto` | double | Cantidad de unidades de criptomoneda operada. |
| `monedaCambio` | string | Moneda cambiada por criptomonedas. |
| `montoCambio` | double | Monto cambiado, incluyendo gastos. |
| `totalGastos` | double | Monto de comisiones y gastos incluidos. |
| `cargo` | double | Comisión de Bind PSP. |
| `precioDolarReferencia` | double | Precio del dólar, neto de gastos. |
| `fechaHoraCreacion` | datetime | Fecha y horario de creación de la intención. |
| `fechaHoraUltimaModificacion` | datetime | Fecha y horario de última actualización. |
| `fechaHoraVencimiento` | datetime | Fecha y horario de expiración de la intención. |
| `fechaHoraCreacionProcesador` | datetime | Fecha y horario de creación en el procesador. |
| `operacionId` | int | Identificador de la operación asociada. |
| `operacionTipoNombre` | string | `"COMPRACRIPTO"` / `"VENTACRIPTO"` |
| `debitoComprobanteId` | int | Comprobante del débito de ARS. |
| `creditoComprobanteId` | int | Comprobante del crédito de ARS. |
| `cargoDebitoComprobanteId` | int | Comprobante del débito de comisión. |
| `cargoCreditoComprobanteId` | int | Comprobante del crédito por devolución de comisión. |
| `motivoRechazo` | string | Descripción del motivo en caso de rechazo. |

## Códigos HTTP

| Código | Descripción |
|--------|-------------|
| `200` | Consulta exitosa |
| `401` | Token de autenticación inválido |

# EVENT — Webhook: Aviso de Cripto

> Fuente: https://psp.bind.com.ar/developers/apis/webhook-cripto
> Producto: Wallet — Cripto

## Descripción

Se envía una notificación vía HTTP POST cada vez que una operación de Cripto obtiene un estado definitivo: **Aprobada** o **Rechazada**.

Cada webhook debe responderse con HTTP 200. De lo contrario, el envío ingresará en un esquema de reintentos.

El webhook se envía a la URL configurada en la Entidad para los tipos de evento:
- `"COMPRA_CRYPTO"`
- `"VENTA_CRYPTO"`

## Campos del Payload

| Campo | Tipo | Descripción |
|-------|------|-------------|
| `mensajeId` | string | Identificador del webhook. |
| `evento` | string | `"COMPRA_CRIPTO"` / `"VENTA_CRIPTO"` |
| `operacionId` | int | Identificador de la operación. |
| `operacionTipo` | string | `"CompraCripto"` / `"VentaCripto"` |
| `operacionEstado` | string | `"Aprobada"` / `"Rechazada"` |
| `cuentaId` | int | Identificador de la cuenta. |
| `monedaCripto` | string | Criptomoneda operada. |
| `montoCripto` | double | Cantidad de unidades de criptomoneda operada. |
| `monedaCambio` | string | Moneda cambiada por criptomonedas. |
| `montoCambio` | double | Monto cambiado, incluyendo gastos. |
| `totalGastos` | double | Monto de comisiones y gastos incluidos. |
| `cargo` | double | Comisión de Bind PSP. |
| `comprobanteId` | int | Comprobante del débito de ARS. |
| `reversaComprobanteId` | int | Comprobante del crédito por reversa (si aplica). |
| `cargoComprobanteId` | int | Comprobante del débito de comisión. |
| `cargoReversaComprobanteId` | int | Comprobante del crédito por devolución de comisión. |
| `intencionId` | int | Identificador de la intención de cripto. |
| `intencionEntidadId` | string | Identificador externo de la intención. |
| `intencionEstado` | string | `"EN_PROCESO"` / `"RECHAZADA"` / `"APROBADA"` |
| `precioDolarReferencia` | double | Precio del dólar, neto de gastos. |
| `fechaCreacion` | datetime | Fecha y horario de creación de la operación. |
| `fechaActualizacion` | datetime | Fecha y horario de última actualización. |

## Ejemplo JSON real

```json
{
  "mensajeId": "4e24d599-5795-44fd-b5f1-4ac2a2ba993f",
  "evento": "COMPRA_CRIPTO",
  "operacionId": 1476543,
  "operacionTipo": "CompraCripto",
  "operacionEstado": "Aprobada",
  "cuentaId": 276603,
  "monedaCripto": "BTC",
  "montoCripto": 0.10000000,
  "monedaCambio": "ARS",
  "montoCambio": 9944147.60000000,
  "totalGastos": 0.00000000,
  "cargo": 0.00000000,
  "comprobanteId": 14015237,
  "reversaComprobanteId": null,
  "cargoComprobanteId": null,
  "cargoReversaComprobanteId": null,
  "intencionId": 1255,
  "intencionEntidadId": "1779451472812495",
  "intencionEstado": "APROBADA",
  "precioDolarReferencia": 1278.15000000,
  "fechaCreacion": "2026-05-22T12:04:37.8998815+00:00",
  "fechaActualizacion": "2026-05-22T12:04:37.8998815+00:00"
}
```

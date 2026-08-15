# EVENT — Webhook: Aviso de Dólar CCL

> Fuente: https://psp.bind.com.ar/developers/apis/webhook-dolarccl
> Producto: Wallet — Dólar CCL

## Descripción

Se envía una notificación vía HTTP POST cada vez que una intención de compra o venta de dólar CCL cambia de estado.

Cada webhook debe responderse con HTTP 200. De lo contrario, el envío ingresará en un esquema de reintentos.

El webhook se envía a la URL configurada en la Entidad para los tipos de evento:
- `"COMPRA_DOLAR_CCL"`
- `"VENTA_DOLAR_CCL"`

## Campos del Payload

| Campo | Tipo | Descripción |
|-------|------|-------------|
| `MensajeId` | string | Identificador del webhook. |
| `Evento` | string | `"COMPRA_DOLAR_CCL"` / `"VENTA_DOLAR_CCL"` |
| `OperacionId` | int | Identificador de la operación. |
| `OperacionTipo` | string | `"CompraDolarCCL"` / `"VentaDolarCCL"` |
| `OperacionEstado` | string | Estado de la operación. |
| `CuentaId` | int | Identificador de la cuenta. |
| `Monto` | double | Importe de la operación. |
| `DebitoComprobanteId` | int | Comprobante del débito asociado a la operación. |
| `CreditoComprobanteId` | int | Comprobante del crédito asociado a la operación. |
| `VueltoComprobanteId` | int | Comprobante del crédito por vuelto. |
| `CargoDebitoComprobanteId` | int | Comprobante del débito de comisión. |
| `CargoCreditoComprobanteId` | int | Comprobante del crédito de comisión por reversa. |
| `IntencionId` | int | Identificador de la intención. |
| `IntencionEntidadId` | int | Identificador externo de la intención. |
| `IntencionEstado` | string | `"COMPLETADA_PARCIAL"` / `"APROBADA"` / `"RECHAZADA"` |
| `Vuelto` | double | Monto no operado en el mercado devuelto al saldo. |
| `MontoInvertido` | double | Monto final gastado en la operación. |
| `MontoObtenido` | double | Monto final obtenido al concretarse la operación. |
| `GastosBroker` | double | Arancel del procesador. |
| `PrecioDolarReferencia` | double | Precio del dólar informado por el procesador (neto de gastos y comisiones). |

## Ejemplo JSON real

```json
{
  "MensajeId": "7e4351b5-961f-445d-b119-158699b0066b",
  "Evento": "COMPRA_DOLAR_CCL",
  "OperacionId": 612782,
  "OperacionTipo": "CompraDolarCCL",
  "OperacionEstado": "AConsultar",
  "CuentaId": 276058,
  "Monto": 150000,
  "DebitoComprobanteId": 8522109,
  "CreditoComprobanteId": null,
  "VueltoComprobanteId": 8522210,
  "CargoDebitoComprobanteId": 8522108,
  "CargoCreditoComprobanteId": null,
  "IntencionId": 321,
  "IntencionEntidadId": null,
  "IntencionEstado": "COMPLETADA_PARCIAL",
  "Vuelto": 1959.6,
  "MontoInvertido": 133040.4,
  "MontoObtenido": null,
  "GastosBroker": 979.67,
  "PrecioDolarReferencia": 1266.11
}
```

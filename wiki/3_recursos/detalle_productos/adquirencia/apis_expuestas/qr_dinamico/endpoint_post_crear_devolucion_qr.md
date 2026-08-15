# POST — Crear Devolución QR Dinámico

> Extraído el: 2026-06-30
> Fuente: https://psp.bind.com.ar/developers/apis/qr-devolucion-copy
> Producto: Adquirencia > QR Dinámico

## Descripción

"Instruye una devolución de un pago realizado con QR."

El endpoint procesa reembolsos parciales o totales. La transacción debe estar en estado ACREDITADO y el medio debe ser "Transferencia30" (QR interoperable). Las devoluciones solo inician desde el comercio.

## Request

**Método HTTP:** `POST`
**URL:** `https://gw-staging-qrbind.epays.services/bindentidad-workflow-v2/v2/api/v1.201/contracargo-qr-v31`

### curl request

```bash
curl -v -X POST "https://gw-staging-qrbind.epays.services/bindentidad-workflow-v2/v2/api/v1.201/contracargo-qr-v31" \
  -H "Content-Type: application/json-patch+json" \
  -H "Authorization: Bearer {{access_token}}" \
  --data-raw '{"qrIdTrx":"ZOC124E78E0F2097B000004550920000000545500000010000446C10E6A4","codigoComercio":"C07663","parcial":false,"importe":100,"motivo":"error en cobro"}'
```

### Headers

| Header | Valor |
|--------|-------|
| `Content-Type` | `application/json-patch+json` |
| `Authorization` | `Bearer {{access_token}}` |

### Body

| Parámetro | Tipo | Requerido | Descripción |
|-----------|------|-----------|-------------|
| `qrIdTrx` | string | SÍ | Identificador de transacción (identificadorOrdenVenta) |
| `codigoComercio` | string | SÍ | Código identificador del comercio |
| `parcial` | boolean | SÍ | true = parcial, false = total |
| `importe` | double | SÍ | Monto a devolver (bruto, sin descuentos) |
| `motivo` | string | SÍ | Razón de devolución (máx. 100 caracteres) |
| `usuario` | string | NO | Usuario que efectúa la devolución |

### Request JSON

```json
{
  "qrIdTrx": "ZOC124E78E0F2097B000004550920000000545500000010000446C10E6A4",
  "codigoComercio": "C07663",
  "parcial": false,
  "importe": 100,
  "motivo": "error en cobro"
}
```

## Response

### Respuesta exitosa (200)

```json
{
  "id": 12345,
  "estado": "PENDIENTE"
}
```

### Estados posibles de devolución

| Estado | Descripción |
|--------|-------------|
| `PENDIENTE` | Devolución iniciada |
| `PROCESADOENBIND` | En proceso |
| `ACEPTADO` | Devolución aprobada |
| `RECHAZADO` | Devolución rechazada |

### Códigos de estado HTTP

| Código | Descripción |
|--------|-------------|
| `200` | Creación exitosa |
| `202` | Identificador orden inválido |
| `400` | Falta algún campo requerido |
| `401` | Token de autenticación inválido |

## ⚠️ Notas y Advertencias del Portal

> "Pueden realizarse infinitas devoluciones de montos parciales hasta completar el monto total."

> Plazo máximo: 30 días desde ejecución de compra.

> Los clientes NO pueden iniciar contracargos desde billetera en este medio.

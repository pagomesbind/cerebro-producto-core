# POST — Crear Devolución QR Estático

> Sincronizado el: 2026-06-30
> Fuente: https://psp.bind.com.ar/developers/apis/qr-devolucion
> Producto: Adquirencia > QR Estático

## Descripción

Instruye una devolución de un pago realizado con QR.

Para utilizar este método, la transacción debe encontrarse en estado ACREDITADO y el medio de pago debe ser "Transferencia30" (QR interoperable).

Pueden realizarse dos tipos de devoluciones:

- **Devolución total:** Devolución del monto total de la compra.
- **Devolución parcial:** Pueden realizarse infinitas devoluciones de montos parciales hasta completar el monto total de la compra, siempre y cuando se realicen dentro del plazo de 30 días desde que se ejecutó la compra.

Considerar que en todos los casos las devoluciones sólo se inician en el comercio. Por lo tanto, un cliente desde su billetera NO puede iniciar un contracargo en este medio de pago.

## Request

**Método HTTP:** `POST`
**Path:** `/bindentidad-workflow-v2/v2/api/v1.201/contracargo-qr-v31`
**Base URL Staging:** `https://gw-staging-qrbind.epays.services`
**URL Completa Staging:** `https://gw-staging-qrbind.epays.services/bindentidad-workflow-v2/v2/api/v1.201/contracargo-qr-v31`

### Headers

| Header | Valor |
|--------|-------|
| `Authorization` | `Bearer {{access_token}}` |
| `Content-Type` | `application/json-patch+json` |

### Body — Parámetros

| Parámetro | Tipo | Requerido | Descripción |
|-----------|------|-----------|-------------|
| `qrIdTrx` | string | REQUIRED | Es el `identificadorOrdenVenta` de la transacción. Esta información se encuentra dentro de la notificación de pago (Ver Webhook: Notificación de pago o Consultar notificaciones de pago). |
| `codigoComercio` | string | REQUIRED | Es el código identificador del comercio. |
| `parcial` | boolean | REQUIRED | Indica si se trata de una devolución parcial o total. Valores permitidos: `true` (Devolución parcial), `false` (Devolución total) |
| `importe` | double | REQUIRED | Es el importe total a devolver. Debe ingresarse el importe bruto sin descuentos. |
| `motivo` | string | REQUIRED | Descripción del motivo de devolución. Longitud máxima = 100 caracteres. |
| `usuario` | string | OPTIONAL | Usuario que realizó la devolución. |

## curl request

```bash
curl -v -X POST "https://gw-staging-qrbind.epays.services/bindentidad-workflow-v2/v2/api/v1.201/contracargo-qr-v31" -H "Content-Type: application/json-patch+json" -H "Authorization: Bearer {{access_token}}" --data-raw "{
    \"qrIdTrx\": \"ZOC124E78E0F2097B000004550920000000545500000010000446C10E6A4\",
    \"codigoComercio\": \"C07663\",
    \"parcial\": false,
    \"importe\": 100,
    \"motivo\": \"error en cobro\",
}"
```

## Request JSON de Ejemplo

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

### Campos de respuesta exitosa (200)

| Campo | Tipo | Descripción |
|-------|------|-------------|
| `id` | int | Id de la orden de venta creada. |
| `estado` | string | Estado de la devolución. Valores permitidos: `"PENDIENTE"` (La devolución aún se encuentra en proceso. Estado no definitivo), `"PROCESADOENBIND"` (Se ha descontado el dinero al comercio pero aún no se ha completado la devolución al cliente pagador. Estado no definitivo), `"ACEPTADO"` (La devolución se completó con éxito. Estado definitivo), `"RECHAZADO"` (La devolución tuvo un error. Estado definitivo) |

### Errores

| Descripción |
|-------------|
| Identificador orden inválido |
| Falta algún campo requerido |
| Token de autenticación inválido |

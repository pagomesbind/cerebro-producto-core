# POST — Crear Orden de Venta (QR Estático)

> Sincronizado el: 2026-06-30
> Fuente: https://psp.bind.com.ar/developers/apis/qr-crearordendeventaenqr
> Producto: Adquirencia > QR Estático

## Descripción

Crea una orden de venta asociada a la caja indicada.

Una orden de venta indica información específica que la billetera que lee el QR deberá considerar para poder instruir el pago.

Sólo puede existir una orden de venta pendiente en una caja. Si existe una orden de venta pendiente y se crea una nueva, la billetera al leer el QR verá la última creada.

Sólo puede existir una orden de venta con código externo en estado APROBADA.

## Request

**Método HTTP:** `POST`
**Path:** `/bindentidad-transaction-v2/v2/api/v1.201/orden-venta-pendiente`
**Base URL Staging:** `https://gw-staging-qrbind.epays.services`
**URL Completa Staging:** `https://gw-staging-qrbind.epays.services/bindentidad-transaction-v2/v2/api/v1.201/orden-venta-pendiente`

### Headers

| Header | Valor |
|--------|-------|
| `Authorization` | `Bearer {{access_token}}` |
| `Content-Type` | `application/json` |

### Body — Parámetros

| Parámetro | Tipo | Requerido | Descripción |
|-----------|------|-----------|-------------|
| `codigoExterno` | string | OPCIONAL | Código externo de la entidad a asociar a la orden de venta. |
| `codigoCaja` | string | OPCIONAL | Es el código de la caja en la cual se quiere crear la orden de venta. |
| `codigoExternoCaja` | string | OPCIONAL | Es el código externo de la caja en la cual se quiere crear la orden de venta. |
| `fechaNegocio` | datetime | REQUERIDO | Fecha y hora en que se crea la orden de venta. |
| `montoTotal` | decimal | REQUERIDO | Es el importe total a cobrar en el QR con la orden de venta. |
| `moneda` | string | REQUERIDO | Es la moneda de la orden de venta. Valores posibles: `"ARS"` |
| `tiempoExpiracion` | int | OPTIONAL | Es el tiempo de expiración de la orden de venta en segundos. Una vez cumplido el tiempo de expiración, la orden de venta pasará a vencida y no podrá ser pagada. Valores posibles: 0 (valor mínimo), 10000000 (valor máximo). Valor por defecto: 600. |
| `productos` | array of objects | OPTIONAL | Array de objetos con información sobre los ítems que incluye la orden de venta. Este dato es sólo informativo. |
| `productos[{}].descripcion` | string | OPTIONAL | Es el nombre o denominación de un ítem de la orden de venta. |
| `productos[{}].monto` | decimal | OPTIONAL | Es el importe del ítem de la orden de venta. |
| `productos[{}].cantidad` | int | OPTIONAL | Cantidad del ítem. |
| `productos[{}].codigo` | string | OPTIONAL | Código del item. |
| `productos[{}].adicional` | string | OPTIONAL | Descripción o información adicional del item. |

## curl request

```bash
curl -v -X POST "https://gw-staging-qrbind.epays.services/bindentidad-transaction-v2/v2/api/v1.201/orden-venta-pendiente" -H "Content-Type: application/json" -H "Authorization: Bearer {{access_token}}" --data-raw "{
    \"codigoExterno\": \"ABC123456789\",
    \"codigoCaja\": \"B00000455196\",
    \"codigoExternoCaja\": null,
    \"fechaNegocio\": \"2023-11-21\",
    \"montoTotal\": 100.79,
    \"moneda\": \"ARS\",
    \"tiempoExpiracion\": 120,
    \"productos\": null
}
"
```

## Request JSON de Ejemplo

```json
{
    "codigoExterno": "ABC123456789",
    "codigoCaja": "B00000455196",
    "codigoExternoCaja": null,
    "fechaNegocio": "2023-11-21",
    "montoTotal": 100.79,
    "moneda": "ARS",
    "tiempoExpiracion": 120,
    "productos": null
}
```

## Response

### Campos de respuesta exitosa (200)

| Campo | Tipo | Descripción |
|-------|------|-------------|
| `idOrdenVenta` | int | Id de la orden de venta creada. |
| `fechaExpiracion` | datetime | Fecha y hora en que se expirará la orden de venta. Es decir que a partir de ella, la orden de venta estará vencida y no podrá pagarse. |
| `codigoExterno` | string | Código externo de la entidad. |

### Errores

| Descripción |
|-------------|
| Falta algún campo requerido |
| Token de autenticación inválido |

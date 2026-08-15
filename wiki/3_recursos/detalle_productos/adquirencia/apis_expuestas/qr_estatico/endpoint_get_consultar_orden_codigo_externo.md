# GET — Consultar Orden de Venta por Código Externo (QR Estático)

> Sincronizado el: 2026-06-30
> Fuente: https://psp.bind.com.ar/developers/apis/qr-consultarordendeventaporidext
> Producto: Adquirencia > QR Estático

## Descripción

Devuelve información de una orden de venta buscandola por su código externo.

Devuelve un array porque pueden haber más de una orden de venta con mismo codigo externo.

## Request

**Método HTTP:** `GET`
**Path:** `/bindentidad-transaccionquery-v2/v2/api/v1.201/orden-venta-por-codigoexterno/{CodigoExterno}`
**Base URL Staging:** `https://gw-staging-qrbind.epays.services`
**URL Completa Staging:** `https://gw-staging-qrbind.epays.services/bindentidad-transaccionquery-v2/v2/api/v1.201/orden-venta-por-codigoexterno/{CodigoExterno}`

### Headers

| Header | Valor |
|--------|-------|
| `Authorization` | `Bearer {{access_token}}` |
| `Cache-Control` | `no-cache` |

### Parámetros de Path

| Parámetro | Tipo | Requerido | Descripción |
|-----------|------|-----------|-------------|
| `CodigoExterno` | string | REQUERIDO | Código externo de la entidad asociado a la orden de venta. |

## curl request

```bash
curl --location 'https://gw-staging-qrbind.epays.services/bindentidad-transaccionquery-v2/v2/api/v1.201/orden-venta-por-codigoexterno/ABC123456789' \
--header 'Cache-Control: no-cache' \
--header 'Authorization: Bearer {{access_token}}'
```

## Response

### Campos de respuesta exitosa (200) — Array

| Campo | Tipo | Descripción |
|-------|------|-------------|
| `idOrdenVenta` | int | Identificador de la orden de venta. |
| `identificador` | string | Identificador de interoperabilidad de la orden de venta. |
| `idTransaccion` | int | Identificador de la transacción asociada a la orden de venta. |
| `fechaProceso` | string | Fecha de procesamiento de la orden de venta. |
| `fechaNegocio` | string | Fecha en que se creó la orden de venta. |
| `fechaBaja` | string | Fecha en la cual la orden de venta fue cancelada o eliminada inhabilitando la posibilidad de ser pagada. |
| `fechaExpiracion` | string | Fecha de expiración de la orden de venta a partir de la cual no se puede pagar. |
| `codigoExterno` | string | Código externo de la entidad de la orden de venta. |
| `codigoCaja` | string | Es el código de la caja. |
| `codigoExternoCaja` | string | Es el código externo de la caja. |
| `codigoComercio` | string | Código identificador único del comercio. |
| `entidad` | string | Código de la entidad. |
| `moneda` | string | Es la moneda de la orden de venta. Valores posibles: `"ARS"` |
| `estado` | string | Estado operativo en el que se encuentra la orden de venta en el flujo de cobro. Valores posibles: `"PENDIENTE"`, `"EN-PROCESO"`, `"INTENCION-PAGO"`, `"PRE-APROBADA"`, `"APROBADA"`, `"RECHAZADA"`, `"EXPIRADA"` |
| `tipoOrden` | string | Identificador del tipo de orden de cobro generada para la base de deudas. Valores posibles: `"OC"` (orden de venta), `"OD"` (deuda) |
| `montoTotal` | decimal | Es el importe total a cobrar en el QR con la orden de venta. |
| `formaPago` | int | Identificador de la forma de pago de la orden de venta. Valores posibles: `1` (QR) |
| `productos` | array of objects | Array de objetos con información sobre los ítems que incluye la orden de venta. Este dato es sólo informativo. |
| `productos[{}].descripcion` | string | Es el nombre o denominación de un ítem de la orden de venta. |
| `productos[{}].monto` | int | Es el importe del ítem de la orden de venta. |
| `productos[{}].cantidad` | int | Cantidad del ítem. |
| `productos[{}].codigo` | string | Código del item. |
| `productos[{}].adicional` | string | Descripción o información adicional del item. |

### Errores

| Descripción |
|-------------|
| Falta algún campo requerido |
| Token de autenticación inválido |

# Endpoint — Consultar movimientos cuenta corriente

> Fuente: https://psp.bind.com.ar/developers/apis/consultarmovimientoscuentacorriente
> Producto: Wallet — Consultas y conciliaciones

## Descripción

Devuelve información de una lista de movimientos de saldo indicando información de su operación asociada, si corresponde.

> **Nota:** Este endpoint no es recomendable para conciliar debido a que al traer mucha información no es performante. Por su información, este endpoint es útil para renderizar grillas de movimientos en aplicaciones.

## URL / Método

| Campo | Valor |
|-------|-------|
| Método | `GET` |
| URL (Staging) | `https://gw-staging-qrbind.epays.services/walletentidad-operaciones/v1/api/v1.201/CuentaCorriente` |

## Parámetros del Request

| Parámetro | Tipo | Requerido | Descripción |
|-----------|------|-----------|-------------|
| `fechaDesde` | datetime | REQUIRED | Fecha inicial del rango de consulta. |
| `fechaHasta` | datetime | REQUIRED | Fecha final del rango de consulta. |
| `pageNumber` | int | REQUIRED | Número de página. Valor mínimo: 1 |
| `pageSize` | int | REQUIRED | Cantidad de registros por página. Valor máximo: 100 |
| `idCuenta` | int | OPTIONAL | Filtrar por cuenta. |
| `idTipoComprobante` | int | OPTIONAL | Filtrar por tipo de comprobante. |
| `orderByDesc` | boolean | OPTIONAL | Si el resultado se ordena descendente. Valor por defecto: `true`. |
| `signo` | int | OPTIONAL | Filtrar por signo: `1` (Crédito), `-1` (Débito) |
| `idComprobante` | int | OPTIONAL | Filtrar por comprobante específico. |

## Bloque curl request

```bash
curl -v -X GET "https://gw-staging-qrbind.epays.services/walletentidad-operaciones/v1/api/v1.201/CuentaCorriente?fechaDesde=2026-06-23&fechaHasta=2026-06-24&pageNumber=1&pageSize=2&orderByDesc=true" \
-H "Cache-Control: no-cache" \
-H "Authorization: Bearer {{access_token}}"
```

## Response

| Campo | Tipo | Descripción |
|-------|------|-------------|
| `totalPages` | int | Cantidad total de páginas disponibles. |
| `totalRecords` | int | Cantidad total de registros. |
| `movimientos[].idComprobante` | int | Identificador del comprobante. |
| `movimientos[].idTipoComprobante` | int | Identificador del tipo de comprobante. |
| `movimientos[].descripcionTipoComprobante` | string | Descripción del tipo de comprobante. |
| `movimientos[].idCuenta` | int | Identificador de la cuenta. |
| `movimientos[].importe` | double | Importe del comprobante. |
| `movimientos[].saldo` | double | Saldo de la cuenta inmediatamente después. |
| `movimientos[].referencia` | string | Referencia del comprobante. |
| `movimientos[].fecha` | datetime | Fecha de creación del comprobante. |
| `movimientos[].signo` | int | `1` = Crédito, `-1` = Débito |
| `movimientos[].datosOperacion.idOperacion` | int | Identificador de la operación. |
| `movimientos[].datosOperacion.estadoOperacionId` | int | Estado de la operación. |
| `movimientos[].datosOperacion.estadoOperacionNombre` | string | Nombre del estado. |
| `movimientos[].datosOperacion.tipoOperacionId` | int | Tipo de operación. |
| `movimientos[].datosOperacion.tipoOperacionNombre` | string | Nombre del tipo de operación. |
| `movimientos[].datosOperacion.fechaCreacion` | datetime | Fecha de creación de la operación. |
| `movimientos[].datosOperacion.fechaActualización` | datetime | Fecha de última actualización. |
| `movimientos[].datosOperacion.comprobanteId` | int | Comprobante original. |
| `movimientos[].datosOperacion.comprobanteDevolucionId` | int | Comprobante de devolución (si aplica). |
| `movimientos[].datosOperacion.auditada` | boolean | Si la operación fue auditada manualmente. |
| `movimientos[].datosOperacion.detalles[].nombre` | string | Clave de información adicional. |
| `movimientos[].datosOperacion.detalles[].valor` | string | Valor de la información adicional. |

## Códigos HTTP

| Código | Descripción |
|--------|-------------|
| `200` | Consulta exitosa |
| `204` | No se encontró ninguna operación para los filtros indicados |
| `400` | Falta un campo requerido |
| `401` | Token de autenticación inválido |

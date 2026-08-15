# Endpoint — Consultar operaciones

> Fuente: https://psp.bind.com.ar/developers/apis/consultar-operaciones
> Producto: Wallet — Consultas y conciliaciones

## Descripción

Devuelve lista de operaciones con ciertos filtros determinados.

Solo incluye información de operaciones. No incluye algunos débitos y créditos de comprobantes que se creen sueltos.

## URL / Método

| Campo | Valor |
|-------|-------|
| Método | `GET` |
| URL (Staging) | `https://gw-staging-qrbind.epays.services/walletentidad-operaciones/v1/api/v1.201/MovimientosOperaciones` |

## Parámetros del Request

| Parámetro | Tipo | Requerido | Descripción |
|-----------|------|-----------|-------------|
| `fechaDesde` | datetime | REQUIRED | Fecha inicial del rango de consulta. |
| `fechaHasta` | datetime | REQUIRED | Fecha final del rango de consulta. |
| `pageNumber` | int | REQUIRED | Número de página a mostrar. |
| `pageSize` | int | REQUIRED | Cantidad de registros por página. |
| `idEstado` | int | OPTIONAL | Estado: 1=A procesar, 2=Aprobada, 3=Rechazada, 4=A consultar, 5=Auditar, 6=Devuelta, 7=Devuelta parcialmente |
| `idTipoOperacion` | int | OPTIONAL | Tipo: 1=Transferencia saliente, 2=Transferencia entrante, 3=Pago con QR, 4=Transferencia interna saliente, 5=Transferencia interna entrante, 6=Transferencia Pull Débito, 7=Compra Dolar CCL, 8=Venta Dolar CCL, 9=Debin Recurrente Crédito, 10=Pago QR PIX |
| `sortOrder` | string | OPTIONAL | Orden: `"asc"` o `"desc"` |

## Bloque curl request

```bash
curl --location 'https://gw-staging-qrbind.epays.services/walletentidad-operaciones/v1/api/v1.201/MovimientosOperaciones?fechaDesde=2025-09-08&fechaHasta=2025-09-10&pageNumber=0&pageSize=5&idEstado=2&idTipoOperacion=3&sortOrder=asc' \
--header 'Authorization: Bearer {{access_token}}'
```

## Response

| Campo | Tipo | Descripción |
|-------|------|-------------|
| `totalPages` | int | Cantidad total de páginas disponibles. |
| `totalRecords` | int | Cantidad total de registros. |
| `movimientosOperaciones[].idOperacion` | int | Identificador de la operación. |
| `movimientosOperaciones[].idExterno` | string | Identificador externo. |
| `movimientosOperaciones[].idTipoOperacion` | int | Tipo de operación (ver tabla de valores arriba). |
| `movimientosOperaciones[].cuenta` | string | Identificador de la cuenta. |
| `movimientosOperaciones[].coelsaId` | string | Identificador Coelsa de la transacción. |
| `movimientosOperaciones[].idTransaccion` | string | Identificador de la transacción en el banco. |
| `movimientosOperaciones[].cbuCvuContraparte` | string | CBU/CVU de la contraparte. |
| `movimientosOperaciones[].fechaHoraCreacion` | string | Fecha de creación de la operación. |
| `movimientosOperaciones[].fechaHoraActualizacion` | string | Fecha de último cambio de estado. |
| `movimientosOperaciones[].idEstado` | int | Estado de la operación (ver tabla de valores arriba). |
| `movimientosOperaciones[].importe` | double | Importe de la operación. |

## Códigos HTTP

| Código | Descripción |
|--------|-------------|
| `200` | Consulta exitosa |
| `204` | Sin registros |
| `401` | Token de autenticación inválido |

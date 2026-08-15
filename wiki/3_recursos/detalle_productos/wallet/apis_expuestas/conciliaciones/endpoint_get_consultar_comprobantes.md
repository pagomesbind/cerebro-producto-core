# Endpoint — Consultar comprobantes

> Fuente: https://psp.bind.com.ar/developers/apis/consultar-comprobantes
> Producto: Wallet — Consultas y conciliaciones

## Descripción

Devuelve información de los comprobantes consultados según filtros determinados.

Endpoint más óptimo para conciliar todos los movimientos de saldo (débito y crédito) de las cuentas corriente.

## URL / Método

| Campo | Valor |
|-------|-------|
| Método | `GET` |
| URL (Staging) | `https://gw-staging-qrbind.epays.services/walletentidad-comprobante/v1/api/v1.201/ComprobantesByFilters` |

## Parámetros del Request

| Parámetro | Tipo | Requerido | Descripción |
|-----------|------|-----------|-------------|
| `fechaDesde` | datetime | REQUIRED | Fecha inicial del filtro. |
| `fechaHasta` | datetime | REQUIRED | Fecha final del filtro. |
| `pageNumber` | int | REQUIRED | Número de página a mostrar. |
| `pageSize` | int | REQUIRED | Cantidad de comprobantes por página. |
| `idCuenta` | int | OPTIONAL | Filtrar por cuenta. |
| `idTipoComprobante` | int | OPTIONAL | Filtrar por tipo de comprobante. |
| `sinRelacionados` | boolean | OPTIONAL | Si solo se muestran comprobantes sin relacionados. |
| `fechaExterna` | datetime | OPTIONAL | Fecha externa indicada al crear el comprobante. |
| `orderByDesc` | boolean | OPTIONAL | Si el resultado se ordena por fecha descendente. |
| `signo` | int | OPTIONAL | Filtrar por signo. Valores: `1` (Crédito), `-1` (Débito) |

## Bloque curl request

```bash
curl --location 'https://gw-staging-qrbind.epays.services/walletentidad-comprobante/v1/api/v1.201/ComprobantesByFilters?fechaDesde=2024-09-01&fechaHasta=2024-09-04&pageNumber=1&pageSize=3' \
--header 'Authorization: Bearer {{access_token}}' \
--header 'Content-Type: application/json-patch+json' \
--header 'Cache-Control: no-cache'
```

## Response

| Campo | Tipo | Descripción |
|-------|------|-------------|
| `totalPages` | int | Cantidad total de páginas disponibles. |
| `totalRecords` | int | Cantidad total de comprobantes. |
| `comprobantes[].idComprobante` | int | Identificador del comprobante. |
| `comprobantes[].idTipoComprobante` | int | Identificador del tipo de comprobante. |
| `comprobantes[].descripcionTipoComprobante` | string | Descripción del tipo de comprobante. |
| `comprobantes[].idCuenta` | int | Identificador de la cuenta. |
| `comprobantes[].fecha` | datetime | Fecha de creación del comprobante. |
| `comprobantes[].importe` | double | Importe del comprobante. |
| `comprobantes[].signo` | int | `1` = Crédito, `-1` = Débito |
| `comprobantes[].saldo` | double | Saldo de la cuenta inmediatamente después de la creación. |
| `comprobantes[].referencia` | string | Referencia del comprobante. |
| `comprobantes[].idComprobanteRelacionado` | int | Identificador del comprobante relacionado (si aplica). |
| `comprobantes[].descripcionTipoComprobanteRelacionado` | string | Descripción del tipo del comprobante relacionado. |
| `comprobantes[].nombreApellidoComprobanteRelacionado` | string | Nombre y apellido del comprobante relacionado. |
| `comprobantes[].cuitComprobanteRelacionado` | string | CUIT/CUIL del comprobante relacionado. |
| `comprobantes[].cvuComprobanteRelacionado` | string | CBU/CVU del comprobante relacionado. |
| `comprobantes[].aliasComprobanteRelacionado` | string | Alias del comprobante relacionado. |
| `comprobantes[].idExterno` | string | Identificador externo indicado por la entidad. |
| `comprobantes[].fechaExterna` | datetime | Fecha externa indicada por la entidad. |

## Códigos HTTP

| Código | Descripción |
|--------|-------------|
| `200` | Consulta exitosa |
| `204` | No se encontraron registros para los filtros indicados |
| `401` | Token de autenticación inválido |

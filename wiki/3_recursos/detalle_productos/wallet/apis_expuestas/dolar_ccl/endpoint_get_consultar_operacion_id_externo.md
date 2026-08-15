# GET — Consultar Operación por ID Externo (Dólar CCL)

> Fuente: https://psp.bind.com.ar/developers/apis/consultaroperacionporidext-dolarccl
> Producto: Wallet — Dólar CCL

## Descripción

Devuelve información completa de una operación, buscándola por el código externo de la entidad.

## URL / Método

| Campo | Valor |
|-------|-------|
| Método | `GET` |
| URL (Staging) | `https://gw-staging-qrbind.epays.services/walletentidad-operaciones/v1/api/v1.201/OperacionByIdExterno/{IdExterno}` |

## Parámetros del Request

| Parámetro | Tipo | Requerido | Descripción |
|-----------|------|-----------|-------------|
| `IdExterno` | string | REQUIRED | Identificador externo de la entidad informado al crear la operación. |

## Bloque curl request

```bash
curl --location 'https://gw-staging-qrbind.epays.services/walletentidad-operaciones/v1/api/v1.201/OperacionByIdExterno/1234' \
--header 'Authorization: Bearer {{access_token}}'
```

## Response

| Campo | Tipo | Descripción |
|-------|------|-------------|
| `id` | int | Identificador de la operación. |
| `tipoOperacionId` | int | `9` = Compra Dolar CCL, `10` = Venta Dolar CCL |
| `tipoOperacionNombre` | string | `"Compra Dolar CCL"` / `"Venta Dolar CCL"` |
| `estadoOperacionId` | int | `1` = A procesar (no definitivo), `2` = Aprobada (definitivo), `3` = Rechazada (definitivo), `4` = A consultar (no definitivo), `5` = Auditar (no definitivo) |
| `estadoOperacionNombre` | string | `"A procesar"` / `"Aprobada"` / `"Rechazada"` / `"A consultar"` / `"Auditar"` |
| `cuentaId` | int | Identificador de la cuenta asociada. |
| `fechaCreacion` | datetime | Fecha y hora de creación. |
| `fechaActualización` | datetime | Fecha y hora de última actualización del estado. |
| `importe` | double | Importe de la operación. |
| `comprobanteId` | int | Identificador del comprobante original. |
| `comprobanteDevolucionId` | int | Identificador del comprobante de devolución (si la operación falló y se reversó). |
| `referencia` | string | Referencia de la operación. |
| `auditada` | boolean | Si la operación fue auditada manualmente. |
| `idExterno` | string | Identificador externo de la entidad. |
| `detalle[].nombre` | string | Clave del atributo adicional. |
| `detalle[].valor` | string | Valor del atributo adicional. |

## Códigos HTTP

| Código | Descripción |
|--------|-------------|
| `200` | Consulta exitosa |
| `404` | No existe la operación consultada |
| `401` | Token de autenticación inválido |

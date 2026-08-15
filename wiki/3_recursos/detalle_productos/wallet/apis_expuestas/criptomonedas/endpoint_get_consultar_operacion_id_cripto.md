# GET — Consultar Operación por ID (Cripto)

> Fuente: https://psp.bind.com.ar/developers/apis/consultaroperacionporid-cripto
> Producto: Wallet — Cripto

## Descripción

Devuelve información completa de una operación.

## URL / Método

| Campo | Valor |
|-------|-------|
| Método | `GET` |
| URL (Staging) | `https://gw-staging-qrbind.epays.services/walletentidad-operaciones/v1/api/v1.201/Operacion/{id}` |

## Parámetros del Request

| Parámetro | Tipo | Requerido | Descripción |
|-----------|------|-----------|-------------|
| `id` | int | REQUIRED | Identificador de la operación a consultar. |

## Bloque curl request

```bash
curl --location 'https://gw-staging-qrbind.epays.services/walletentidad-operaciones/v1/api/v1.201/Operacion/584869' \
--header 'Authorization: Bearer {{access_token}}'
```

## Response

| Campo | Tipo | Descripción |
|-------|------|-------------|
| `id` | int | Identificador de la operación consultada. |
| `tipoOperacionId` | int | `11` = Compra Cripto, `12` = Venta Cripto |
| `tipoOperacionNombre` | string | `"Compra Cripto"` / `"Venta Cripto"` |
| `estadoOperacionId` | int | `1` = A procesar (no definitivo), `2` = Aprobada (definitivo), `3` = Rechazada (definitivo), `4` = A consultar (no definitivo), `5` = Auditar (no definitivo) |
| `estadoOperacionNombre` | string | `"A procesar"` / `"Aprobada"` / `"Rechazada"` / `"A consultar"` / `"Auditar"` |
| `cuentaId` | int | Identificador de la cuenta asociada. |
| `fechaCreacion` | datetime | Fecha y hora de creación de la operación. |
| `fechaActualización` | datetime | Fecha y hora de última actualización del estado. |
| `importe` | double | Importe de la operación. |
| `comprobanteId` | int | Identificador del comprobante original asociado. |
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

# Endpoint — Consultar operación por ID

> Fuente: https://psp.bind.com.ar/developers/apis/consultaroperacionporid-debinrecurrente
> Producto: Wallet — Debin recurrente

## Descripción

Devuelve información completa de una operación de DEBIN recurrente.

## URL / Método

| Campo | Valor |
|-------|-------|
| Método | `GET` |
| URL (Staging) | `https://gw-staging-qrbind.epays.services/walletentidad-operaciones/v1/api/v1.201/Operacion/{id}` |

## Parámetros del Request

| Parámetro | Tipo | Requerido | Descripción |
|-----------|------|-----------|-------------|
| `id` | int | REQUIRED | Identificador de la operación (path param). |

## Bloque curl request

```bash
curl --location 'https://gw-staging-qrbind.epays.services/walletentidad-operaciones/v1/api/v1.201/Operacion/584869' \
--header 'Authorization: Bearer {{access_token}}'
```

## Response

| Campo | Tipo | Descripción |
|-------|------|-------------|
| `id` | int | Identificador de la operación. |
| `tipoOperacionId` | int | Tipo. Valores: `14` = Debin Recurrente Crédito |
| `tipoOperacionNombre` | string | Nombre del tipo. Valores: `"Debin Recurrente Crédito"` |
| `estadoOperacionId` | int | Estado en el sistema. Valores: 1=A procesar, 2=Aprobada, 3=Rechazada, 4=A consultar, 5=Auditar, 6=Devuelta, 7=Devuelta parcial, 8=Devolución pendiente |
| `estadoOperacionNombre` | string | Nombre del estado. |
| `cuentaId` | int | Identificador de la cuenta. |
| `fechaCreacion` | datetime | Fecha y hora de creación. |
| `fechaActualización` | datetime | Fecha y hora de última actualización. |
| `importe` | double | Importe de la operación. |
| `comprobanteId` | int | Comprobante original. |
| `comprobanteDevolucionId` | int | Comprobante de reversa (si aplica). |
| `referencia` | string | Referencia de la operación. |
| `auditada` | boolean | Si fue resuelto por conciliación manual. |
| `idExterno` | string | Identificador externo de la organización. |
| `detalle` | array | Array clave-valor con info adicional. |
| `detalle[].nombre` | string | Valores: `"CbuComprador"`, `"NombreComprador"`, `"CoelsaId"`, `"OriginId"`, `"EstadoExterno"`, `"MotivoRechazo"` |
| `detalle[].valor` | string | Valor del atributo. Ver tabla abajo. |

### Valores de `detalle[].valor` por nombre

| Nombre | Descripción del valor |
|--------|----------------------|
| `CbuComprador` | CBU externo del titular desde donde se debitó el dinero. |
| `NombreComprador` | Nombre del titular de la cuenta debitada. |
| `CoelsaId` | Identificador del procesador. El más importante en la red. |
| `OriginId` | Id de referencia utilizado para procesar en el banco. |
| `EstadoExterno` | Estado del DEBIN informado por el banco. Valores: `"AWAITING_CONFIRMATION"`, `"REJECTED_CLIENT"`, `"NO_BALANCE"`, `"DATA_ERROR"`, `"DEBIT_ERROR"`, `"EXPIRED"`, `"NO_WARRANTY"`, `"CREDIT_ERROR"`, `"COMPLETED"`, `"CANCELED"`, `"IN_PROGRESS"` |
| `MotivoRechazo` | Descripción del motivo del error (si corresponde). |

## Códigos HTTP

| Código | Descripción |
|--------|-------------|
| `200` | Consulta exitosa |
| `404` | No existe la operación consultada |
| `401` | Token de autenticación inválido |

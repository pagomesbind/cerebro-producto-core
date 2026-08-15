# Endpoint — Consultar operación por ID

> Fuente: https://psp.bind.com.ar/developers/apis/consultaroperacionporid-pagoqr
> Producto: Wallet — Pago QR

## Descripción

Devuelve información completa de una operación de pago QR.

## URL / Método

| Campo | Valor |
|-------|-------|
| Método | `GET` |
| URL (Staging) | `https://gw-staging-qrbind.epays.services/walletentidad-operaciones/v1/api/v1.201/Operacion/{id}` |

## Parámetros del Request

| Parámetro | Tipo | Requerido | Descripción |
|-----------|------|-----------|-------------|
| `id` | int | REQUIRED | Identificador de la operación a consultar (path param). |

## Bloque curl request

```bash
curl --location 'https://gw-staging-qrbind.epays.services/walletentidad-operaciones/v1/api/v1.201/Operacion/584869' \
--header 'Authorization: Bearer {{access_token}}'
```

## Response

| Campo | Tipo | Descripción |
|-------|------|-------------|
| `id` | int | Identificador de la operación. |
| `tipoOperacionId` | int | Tipo de operación. Valores: `3` = Pago con QR |
| `tipoOperacionNombre` | string | Nombre del tipo. Valores: `"Pago con QR"` |
| `estadoOperacionId` | int | Estado en el sistema. Valores: 1=A procesar (no definitivo), 2=Aprobada (definitivo), 3=Rechazada (definitivo), 4=A consultar (no definitivo), 5=Auditar (no definitivo), 6=Devuelta (definitivo), 7=Devuelta parcial (no definitivo) |
| `estadoOperacionNombre` | string | Nombre del estado. |
| `cuentaId` | int | Identificador de la cuenta. |
| `fechaCreacion` | datetime | Fecha y hora de creación. |
| `fechaActualización` | datetime | Fecha y hora de última actualización. |
| `importe` | double | Importe de la operación. |
| `comprobanteId` | int | Identificador del comprobante original. |
| `comprobanteDevolucionId` | int | Identificador del comprobante de reversa (si la operación falló). |
| `referencia` | string | Referencia de la operación. |
| `auditada` | boolean | Si el estado fue resuelto por conciliación manual. |
| `idExterno` | string | Identificador externo de la organización. |
| `detalle` | array | Array de objetos clave-valor con info adicional. |
| `detalle[].nombre` | string | Nombre del atributo. Valores: `"CoelsaId"`, `"EstadoCoelsa"`, `"VendedorCuit"`, `"VendedorCbuCvu"`, `"VendedorNombre"`, `"MotivoRechazo"`, `"Contracargos"` |
| `detalle[].valor` | string | Valor del atributo según nombre. |

### Valores de `detalle[].valor` por nombre

| Nombre | Descripción del valor |
|--------|----------------------|
| `CoelsaId` | Identificador único de Coelsa. Clave para reclamos y conciliaciones. |
| `EstadoCoelsa` | Estado externo del pago QR. Valores: `"ACREDITADO"`, `"ERROR DATOS"`, `"ERROR ACREDITACION"`, `"ERROR DEBITO"`, `"INICIADO"`, `"SIN SALDO"`, `"VENCIDO"`, `"SIN GARANTIA"`, `"RECHAZO DE CLIENTE"` |
| `VendedorCuit` | CUIT del comercio. |
| `VendedorCbuCvu` | CBU/CVU del comercio. |
| `VendedorNombre` | Nombre del titular del comercio. |
| `MotivoRechazo` | Motivo del error si corresponde. |
| `Contracargos` | Información de cada contracargo asociado a este pago QR. |

## Códigos HTTP

| Código | Descripción |
|--------|-------------|
| `200` | Consulta exitosa |
| `404` | No existe la operación consultada |
| `401` | Token de autenticación inválido |

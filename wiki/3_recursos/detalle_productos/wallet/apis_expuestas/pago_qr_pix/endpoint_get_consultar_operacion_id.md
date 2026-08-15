# Endpoint — Consultar operación por ID

> Fuente: https://psp.bind.com.ar/developers/apis/consultaroperacionporid-pagopix
> Producto: Wallet — Pago QR PIX

## Descripción

Devuelve información completa de una operación de pago QR PIX.

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
| `tipoOperacionId` | int | Tipo. Valores: `15` = Pago QR Pix |
| `tipoOperacionNombre` | string | Nombre del tipo. Valores: `"Pago QR Pix"` |
| `estadoOperacionId` | int | Estado en el sistema. Valores: 1=A procesar, 2=Aprobada, 3=Rechazada, 4=A consultar, 5=Auditar, 6=Devuelta, 7=Devuelta parcial |
| `estadoOperacionNombre` | string | Nombre del estado. |
| `cuentaId` | int | Identificador de la cuenta. |
| `fechaCreacion` | datetime | Fecha y hora de creación. |
| `fechaActualización` | datetime | Fecha y hora de última actualización. |
| `importe` | double | Importe de la operación. |
| `comprobanteId` | int | Comprobante original. |
| `comprobanteDevolucionId` | int | Comprobante de reversa (si la operación falló). |
| `referencia` | string | Referencia de la operación. |
| `auditada` | boolean | Si fue resuelto por conciliación manual. |
| `idExterno` | string | Identificador externo de la organización. |
| `detalle` | array | Array clave-valor con info adicional. |
| `detalle[].nombre` | string | Valores: `"LecturaPixId"`, `"EstadoExterno"`, `"MotivoRechazo"`, `"MontoReales"`, `"PaymentId"` |
| `detalle[].valor` | string | Valor del atributo. Ver tabla abajo. |

### Valores de `detalle[].valor` por nombre

| Nombre | Descripción del valor |
|--------|----------------------|
| `LecturaPixId` | Id de intención de pago Pix asociado. |
| `EstadoExterno` | Estado externo informado por el procesador. |
| `MotivoRechazo` | Causa técnica del fallo (si la transacción fue negativa). |
| `MontoReales` | Importe en reales brasileños que se pagó. |
| `PaymentId` | Identificador del procesador externo. |

## Códigos HTTP

| Código | Descripción |
|--------|-------------|
| `200` | Consulta exitosa |
| `404` | No existe la operación consultada |
| `401` | Token de autenticación inválido |

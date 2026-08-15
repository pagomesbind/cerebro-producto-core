# Endpoint — Consultar operación por ID

> Fuente: https://psp.bind.com.ar/developers/apis/consultaroperacionporid-transferencias
> Producto: Wallet — Transferencias

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
| `id` | int | REQUIRED | Identificador de la operación a consultar (path param). |

## Bloque curl request

```bash
curl --location 'https://gw-staging-qrbind.epays.services/walletentidad-operaciones/v1/api/v1.201/Operacion/584869' \
--header 'Authorization: Bearer {{access_token}}'
```

## Response

| Campo | Tipo | Descripción |
|-------|------|-------------|
| `id` | int | Identificador de la operación consultada. |
| `tipoOperacionId` | int | Tipo de operación. Valores: 1=Transferencia saliente, 2=Transferencia entrante, 4=Transferencia interna saliente, 5=Transferencia interna entrante |
| `tipoOperacionNombre` | string | Nombre del tipo de operación. |
| `estadoOperacionId` | int | Estado de la operación. Valores: 1=A procesar (no definitivo), 2=Aprobada (definitivo), 3=Rechazada (definitivo), 4=A consultar (no definitivo), 5=Auditar (no definitivo — se resuelve manualmente por conciliaciones) |
| `estadoOperacionNombre` | string | Nombre del estado de la operación. |
| `cuentaId` | int | Identificador de la cuenta asociada a la operación. |
| `fechaCreacion` | datetime | Fecha y hora en que se creó la operación. |
| `fechaActualización` | datetime | Fecha y hora de última actualización del estado. |
| `importe` | double | Valor del importe de la operación. |
| `comprobanteId` | int | Identificador del comprobante original asociado a la operación. |
| `comprobanteDevolucionId` | int | Identificador del comprobante de devolución (si la operación falló y se reversó). |
| `referencia` | string | Referencia de la operación. |
| `auditada` | boolean | Indica si la operación fue auditada — su estado pasó a definitivo por conciliación manual. |
| `idExterno` | string | Identificador externo de la entidad informado opcionalmente. |
| `detalle` | array | Array de objetos clave-valor con información adicional según el tipo de operación. Se pueden agregar nuevos atributos a futuro. |
| `detalle[].nombre` | string | Nombre del atributo. Valores posibles: `"CuitCuilContraparte"`, `"NombreContraparte"`, `"CvuCbuContraparte"`, `"CoelsaId"`, `"MotivoRechazo"`, `"EstadoExterno"`, `"Concepto"` |
| `detalle[].valor` | string | Valor del atributo. Ver tabla de valores posibles por nombre abajo. |

### Valores de `detalle[].valor` por nombre

| Nombre | Descripción del valor |
|--------|----------------------|
| `CuitCuilContraparte` | CUIT/CUIL de la contraparte (11 dígitos sin guiones). |
| `NombreContraparte` | Razón social o nombre completo del titular de la cuenta contraparte. |
| `CvuCbuContraparte` | CVU o CBU de 22 dígitos de la cuenta contraparte. |
| `CoelsaId` | Identificador único asignado por Coelsa. Clave para reclamos, conciliaciones y disputas interbancarias. |
| `MotivoRechazo` | Causa técnica del fallo (null si no fue rechazada). |
| `EstadoExterno` | Estado indicado por el procesador externo. Valores: `"COMPLETED"`, `"FAILED"`, `"IN_PROGRESS"`, `"UNKNOWN"` |
| `Concepto` | Concepto de la transferencia según BCRA. Valores: `"VAR"`, `"ALQ"`, `"CUO"`, `"EXP"`, `"FAC"`, `"PRE"`, `"SEG"`, `"HON"`, `"HAB"` |

## Códigos HTTP

| Código | Descripción |
|--------|-------------|
| `200` | Consulta exitosa |
| `404` | No existe la operación consultada |
| `401` | Token de autenticación inválido |

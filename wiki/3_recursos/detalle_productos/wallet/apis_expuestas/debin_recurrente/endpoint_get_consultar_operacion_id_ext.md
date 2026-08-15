# Endpoint — Consultar operación por ID externo

> Fuente: https://psp.bind.com.ar/developers/apis/consultaroperacionporidext-debinrecurrente
> Producto: Wallet — Debin recurrente

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
| `idExterno` | string | REQUIRED | Identificador externo informado al momento de la creación (path param). |

## Bloque curl request

```bash
curl --location 'https://gw-staging-qrbind.epays.services/walletentidad-operaciones/v1/api/v1.201/OperacionByIdExterno/1234' \
--header 'Authorization: Bearer {{access_token}}'
```

## Response

| Campo | Tipo | Descripción |
|-------|------|-------------|
| `id` | int | Identificador de la operación. |
| `tipoOperacionId` | int | Tipo. Valores: `14` = Debin Recurrente Crédito |
| `tipoOperacionNombre` | string | Nombre del tipo. Valores: `"Debin Recurrente Crédito"` |
| `estadoOperacionId` | int | Estado. Valores: 1=A procesar, 2=Aprobada, 3=Rechazada, 4=A consultar, 5=Auditar, 6=Devuelta, 7=Devuelta parcial, 8=Devolución pendiente |
| `estadoOperacionNombre` | string | Nombre del estado. |
| `cuentaId` | int | Identificador de la cuenta. |
| `fechaCreacion` | datetime | Fecha y hora de creación. |
| `fechaActualización` | datetime | Fecha y hora de última actualización. |
| `importe` | double | Importe de la operación. |
| `comprobanteId` | int | Comprobante original. |
| `comprobanteDevolucionId` | int | Comprobante de reversa (si aplica). |
| `referencia` | string | Referencia de la operación. |
| `auditada` | boolean | Si fue resuelto por conciliación manual. |
| `idExterno` | string | Identificador externo. |
| `detalle` | array | Array clave-valor con info adicional. |
| `detalle[].nombre` | string | Valores: `"CuitCuilContraparte"`, `"NombreContraparte"`, `"CvuCbuContraparte"`, `"CoelsaId"`, `"MotivoRechazo"`, `"EstadoExterno"`, `"Concepto"` |
| `detalle[].valor` | string | Valor del atributo. Ver tabla abajo. |

### Valores de `detalle[].valor` por nombre

| Nombre | Descripción del valor |
|--------|----------------------|
| `CuitCuilContraparte` | CUIT/CUIL de la contraparte, 11 dígitos sin guiones. |
| `NombreContraparte` | Razón social o nombre del titular de la cuenta contraparte. |
| `CvuCbuContraparte` | CVU o CBU de 22 dígitos de la cuenta contraparte. |
| `CoelsaId` | Identificador único asignado por Coelsa. Clave para reclamos y conciliaciones. |
| `MotivoRechazo` | Causa técnica del fallo (null si no fue rechazada). |
| `EstadoExterno` | Estado informado por el procesador. Valores: `"COMPLETED"`, `"FAILED"`, `"IN_PROGRESS"`, `"UNKNOWN"` |
| `Concepto` | Concepto BCRA. Valores: `"VAR"`, `"ALQ"`, `"CUO"`, `"EXP"`, `"FAC"`, `"PRE"`, `"SEG"`, `"HON"`, `"HAB"` |

## Códigos HTTP

| Código | Descripción |
|--------|-------------|
| `200` | Consulta exitosa |
| `404` | No existe la operación consultada |
| `401` | Token de autenticación inválido |

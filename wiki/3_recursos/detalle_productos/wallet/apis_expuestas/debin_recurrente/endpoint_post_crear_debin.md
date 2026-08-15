# Endpoint — Crear DEBIN recurrente

> Fuente: https://psp.bind.com.ar/developers/apis/crear-debin
> Producto: Wallet — Debin recurrente

## Descripción

Crea una instrucción de DEBIN recurrente.

## URL / Método

| Campo | Valor |
|-------|-------|
| Método | `POST` |
| URL (Staging) | `https://gw-staging-qrbind.epays.services/walletentidad-operaciones/v1/api/v1.201/DebinRecurrenteCredito` |
| Content-Type | `application/json-patch+json` |

## Parámetros del Request

| Parámetro | Tipo | Requerido | Descripción |
|-----------|------|-----------|-------------|
| `cuentaId` | int | REQUIRED | Identificador de la cuenta a acreditar. |
| `cbuOrigen` | string | REQUIRED | CBU/CVU de entidad externa de la cuál se debitarán los fondos. |
| `importe` | double | OPTIONAL | Importe a operar. |
| `referencia` | string | OPTIONAL | Descripción de referencia de la operación. |
| `idExterno` | string | OPTIONAL | Identificador externo de la Organización. No pueden existir dos operaciones con el mismo valor. |

## Bloque curl request

```bash
curl --location 'https://gw-staging-qrbind.epays.services/walletentidad-operaciones/v1/api/v1.201/DebinRecurrenteCredito' \
--header 'Content-Type: application/json-patch+json' \
--header 'Cache-Control: no-cache' \
--header 'Authorization: Bearer {{access_token}}' \
--data '{
"cuentaId": 278243,
"cbuOrigen": "3220001881007354720049",
"importe": 678,
"referencia": "texto 100420251",
"idExterno": "id100420251"
}'
```

## Response

| Campo | Tipo | Descripción |
|-------|------|-------------|
| `operacionId` | int | Identificador de la operación creada. |
| `estadoId` | int | Estado en el sistema. Valores: 1=A procesar, 2=Aprobada, 3=Rechazada, 4=A consultar, 5=Auditar |
| `estado` | string | Descripción del estado. |
| `cuentaId` | int | Identificador de la cuenta a acreditar. |
| `fechaCreacion` | datetime | Fecha y hora de creación. |
| `importe` | double | Importe de la operación. |
| `comprobanteId` | int | Comprobante de crédito del saldo. |
| `referencia` | string | Referencia de la operación. |
| `idExterno` | string | Identificador externo de la Organización. |
| `bancoTransaccionId` | string | Identificador de la operación para el banco. |
| `originId` | string | Identificador con el que se procesó en el banco. |
| `coelsaId` | string | Identificador de Coelsa. El más importante para reclamos y conciliaciones. |
| `estadoExterno` | string | Estado de la operación en el banco. |
| `cbuComprador` | string | CBU/CVU de la cuenta externa debitada. |
| `nombreComprador` | string | Nombre del titular de la cuenta externa. |
| `motivoRechazo` | string | Motivo de rechazo (si aplica). |
| `mensaje` | string | Descripción del motivo de rechazo (si aplica). |
| `estaPendiente` | boolean | Si aún no fue instruida en el procesador externo. |
| `estaAprobado` | boolean | Si adquirió estado aprobado definitivo. |
| `estaRechazado` | boolean | Si adquirió estado rechazado definitivo. |
| `estaAAuditar` | boolean | Si está pendiente de conciliación o revisión manual. |

## Códigos HTTP

| Código | Descripción |
|--------|-------------|
| `200` | Creación de DEBIN exitosa y aprobada |
| `200` | Creación de DEBIN exitosa pero rechazada |
| `200` | Creación de DEBIN en proceso |
| `422` | idExterno existente |
| `422` | Suscripción de recurrencia no existente |
| `400` | idExterno tiene un formato inválido |
| `422` | Cuenta inválida |
| `401` | Token de autenticación inválido |

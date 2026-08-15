# Endpoint — Consultar debin de fondeo de cuenta recaudadora

> Fuente: https://psp.bind.com.ar/developers/apis/consultar-un-debin
> Producto: Wallet — Cuenta recaudadora

## Descripción

Consulta la información de la solicitud de un DEBIN para fondeo de la cuenta recaudadora.

Para realizar un debin antes debe crearse una suscripción en la cuenta de origen. Esta configuración debe solicitarse a Bind PSP.

## URL / Método

| Campo | Valor |
|-------|-------|
| Método | `GET` |
| URL (Staging) | `https://gw-staging-qrbind.epays.services/walletentidad-cuenta/v1/api/v1.201/Organizacion/GetDebinPedidoById/{id}` |

## Parámetros del Request

| Parámetro | Tipo | Requerido | Descripción |
|-----------|------|-----------|-------------|
| `id` | int | REQUIRED | Identificador del debin (path param). Obtenido al momento de la creación. |

## Bloque curl request

```bash
curl --location 'https://gw-staging-qrbind.epays.services/walletentidad-cuenta/v1/api/v1.201/Organizacion/GetDebinPedidoById/10' \
--header 'Content-Type: application/json-patch+json' \
--header 'Cache-Control: no-cache' \
--header 'Authorization: Bearer {{access_token}}'
```

## Response

| Campo | Tipo | Descripción |
|-------|------|-------------|
| `id` | int | Identificador del debin. |
| `descripcion` | string | Descripción con la que se creó el debin. |
| `cbuOrigen` | string | CBU o CVU de la cuenta de origen. |
| `aliasOrigen` | string | Alias de la cuenta de origen. |
| `monto` | double | Importe del debin. |
| `originId` | string | Identificador con el que se creó el debin en el banco. |
| `coelsaId` | string | Id Coelsa del debin. |
| `bindId` | string | Identificador interno del banco. |
| `concepto` | string | Concepto del debin. Valor por defecto: `"VAR"` |
| `provision` | string | Descripción del uso del debin recurrente. |
| `contraparteCuit` | string | CUIT del titular de la cuenta origen. |
| `contraparteAlias` | string | Alias de la cuenta origen. |
| `contraparteCbu` | string | CBU o CVU de la cuenta origen. |
| `contraparteNombre` | string | Nombre del CVU de la cuenta origen. |
| `contraparteBancoId` | string | Identificador del banco de la cuenta origen. |
| `estado` | string | Estado del debin. Valores: `"COMPLETED"`, `"PENDING"`, `"IN_PROGRESS"`, `"UNKNOWN"`, `"UNKNOWN_FOREVER"` |
| `fechaInicio` | datetime | Fecha y hora en que inició la solicitud. |
| `fechaFin` | datetime | Fecha y hora en que finalizó el debin. |

## Códigos HTTP

| Código | Descripción |
|--------|-------------|
| `200` | Consulta exitosa |
| `404` | ID de debin inválido |
| `400` | Falta un campo requerido |
| `401` | Token de autenticación inválido |

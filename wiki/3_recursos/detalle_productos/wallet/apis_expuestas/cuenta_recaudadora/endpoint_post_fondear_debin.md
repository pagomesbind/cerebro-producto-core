# Endpoint — Fondear cuenta recaudadora con debin

> Fuente: https://psp.bind.com.ar/developers/apis/fondear-cuenta-recaudadora-con-debin
> Producto: Wallet — Cuenta recaudadora

## Descripción

Solicita la creación de un debin que se acreditará en la cuenta recaudadora. El estado del debin creado depende del banco que procesa la solicitud. Generalmente, inicia en estado PENDING y su estado deberá consultarse para validar que se haya actualizado.

Para realizar un debin antes debe crearse una suscripción en la cuenta de origen. Esta configuración debe solicitarse a Bind PSP.

## URL / Método

| Campo | Valor |
|-------|-------|
| Método | `POST` |
| URL (Staging) | `https://gw-staging-qrbind.epays.services/walletentidad-cuenta/v1/api/v1.201/Organizacion/CrearPedidoDebin` |

## Parámetros del Request

| Parámetro | Tipo | Requerido | Descripción |
|-----------|------|-----------|-------------|
| `descripcion` | string | REQUIRED | Descripción del debin a realizar para guardar como referencia. |
| `cbuOrigen` | string | REQUIRED | CBU o CVU desde donde se debitará el dinero. Puede ser null si se envía el alias. |
| `alias` | string | REQUIRED | Alias de la cuenta origen. Puede ser null si se envía el cbuOrigen. |
| `monto` | double | REQUIRED | Importe a debitar. |

## Bloque curl request

```bash
curl --location 'https://gw-staging-qrbind.epays.services/walletentidad-cuenta/v1/api/v1.201/Organizacion/CrearPedidoDebin' \
--header 'Content-Type: application/json-patch+json' \
--header 'Cache-Control: no-cache' \
--header 'Authorization: Bearer {{access_token}}' \
--data '{
  "descripcion": "Fondeo cuenta recaudadora",
  "cbuOrigen": "3220001823007351860012",
  "alias": null,
  "monto": 123.12
}'
```

## Response

| Campo | Tipo | Descripción |
|-------|------|-------------|
| `id` | int | Identificador del debin creado. Se utiliza para consultar su estado posteriormente. |
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
| `fechaInicio` | datetime | Fecha y hora en que inició la solicitud del debin. |
| `fechaFin` | datetime | Fecha y hora en que finalizó el debin. |

## Códigos HTTP

| Código | Descripción |
|--------|-------------|
| `200` | Creación de DEBIN exitosa |
| `404` | No existe una suscripción de debin recurrente activa sobre el CBU |
| `422` | Error en valor del monto |
| `401` | Token de autenticación inválido |

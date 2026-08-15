# POST — Realizar Transferencia desde CBU

> Fuente: https://psp.bind.com.ar/developers/apis/transfer-transferir
> Producto: Agente de Cobros — Operar CBU recaudadora

## Descripción

Realiza una transferencia saliente a un CBU, CVU o alias.

Si se crea una transferencia con un `origin_id` ya existente, no se crea una nueva y se devuelve la información de la original.

## URL / Método

| Campo | Valor |
|-------|-------|
| Método | `POST` |
| URL (Staging) | `https://gw-staging-qrbind.epays.services/cvucollectentidad-financial/v1/v1.201/banks/322/accounts/owner/transaction-request-types/TRANSFER/transaction-requests` |

## Parámetros del Request

| Parámetro | Tipo | Requerido | Descripción |
|-----------|------|-----------|-------------|
| `origin_id` | string | REQUIRED | Identificador unívoco de la transacción definido por el usuario. Máx 15 caracteres. Si ya existe, devuelve la transacción original. |
| `to.cbu` | string | OPTIONAL | CBU o CVU del destinatario. Requerido si no se envía `alias`. |
| `to.alias` | string | OPTIONAL | Alias del destinatario. Requerido si no se envía `cbu`. |
| `value.currency` | string | REQUIRED | Moneda: `"ARS"` / `"USD"`. |
| `value.amount` | double | REQUIRED | Importe de la transferencia. |
| `description` | string | OPTIONAL | Descripción (máx 100 caracteres). Default: `"Varios"`. |
| `concepto` | string | REQUIRED | `"ALQ"` / `"CUO"` / `"EXP"` / `"FAC"` / `"PRE"` / `"SEG"` / `"HON"` / `"HAB"` / `"VAR"`. Default: `"VAR"`. |
| `emails` | array | OPTIONAL | Lista de emails destinatarios para envío de comprobante (template fijo del Banco Industrial). |

## Bloque curl request

```bash
curl --location 'https://gw-staging-qrbind.epays.services/cvucollectentidad-financial/v1/v1.201/banks/322/accounts/owner/transaction-request-types/TRANSFER/transaction-requests' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer {{access_token}}' \
--data-raw '{
  "origin_id": "T0291220231",
  "to": {
    "cbu": "0000532608170000000011",
    "alias": null
  },
  "value": {
    "currency": "ARS",
    "amount": 29
  },
  "description": "primary",
  "concept": "VAR",
  "emails": ["email@gmail.com"]
}'
```

## Response

| Campo | Tipo | Descripción |
|-------|------|-------------|
| `id` | string | Identificador de la transacción. |
| `type` | string | Tipo de operación. Valor: `"TRANSFER"`. |
| `from.bank_id` | string | Código del banco. |
| `from.account_id` | string | Identificador de la cuenta en el banco. |
| `counterparty.id` | string | CUIT/CUIL del destinatario. |
| `counterparty.name` | string | Nombre del destinatario. |
| `counterparty.type` | string | `"CUIT_CUIL"` / `"UNAVAILABLE"`. |
| `counterparty.bank_routing.scheme` | string | `"NAME"` / `"UNAVAILABLE"`. |
| `counterparty.bank_routing.address` | string | Nombre del banco destino. |
| `counterparty.bank_routing.code` | string | Código del banco destino. |
| `counterparty.account_routing.scheme` | string | `"CBU"` / `"LABEL"` / `"UNAVAILABLE"`. |
| `counterparty.account_routing.address` | string | CBU, CVU o alias de la cuenta destino. |
| `details.origin_id` | string | Identificador definido por el usuario. |
| `transaction_ids` | array | IDs de procesamiento de la transferencia (banco + Coelsa). |
| `status` | string | Estado: `"PENDING"` / `"IN_PROGRESS"` / `"COMPLETED"` / `"FAILED"` / `"UNKNOWN"` / `"UNKNOWN_FOREVER"`. COMPLETED y FAILED son definitivos. UNKNOWN se intenta resolver durante el día. UNKNOWN_FOREVER ya no se reintenta. |
| `start_date` | datetime | Fecha y hora de inicio. |
| `end_date` | datetime | Fecha y hora de finalización. |
| `charge.summary` | string | Descripción de la transferencia. |
| `charge.value.currency` | string | Moneda: `"ARS"` / `"USD"`. |
| `charge.value.amount` | double | Importe. |

## Códigos HTTP

| Código | Descripción |
|--------|-------------|
| `200` | Creación exitosa |
| `422` | `origin_id` tiene más de 15 caracteres |
| `401` | Token de autenticación inválido |

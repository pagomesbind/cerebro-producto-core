# EVENT — Webhook: Aviso de Transferencia Saliente desde CBU

> Fuente: https://psp.bind.com.ar/developers/apis/transfer-webhooksaliente
> Producto: Agente de Cobros — Operar CBU recaudadora

## Descripción

Se envía una notificación HTTP POST cada vez que se actualiza el estado de una transferencia saliente a un estado definitivo.

Cada webhook debe responderse con HTTP 200. De lo contrario, el envío ingresará en un esquema de reintentos.

La URL destino debe estar parametrizada previamente para este producto.

## Campos del Payload

| Campo | Tipo | Descripción |
|-------|------|-------------|
| `id` | string | ID guid del mensaje. |
| `object` | string | Objeto del mensaje. |
| `created` | datetime | Fecha y hora de creación (UTC 0). |
| `type` | string | Tipo de evento. Valor fijo: `"TRANSFER"`. |
| `redeliveries` | int | Número de reintentos del banco. |
| `data.id` | string | ID Coelsa de la transferencia. |
| `data.type` | string | Valor fijo: `"TRANSFER"`. |
| `data.from.bank_id` | string | Código del banco. Valor fijo: `"322"`. |
| `data.from.account_id` | string | Identificador de la cuenta recaudadora. |
| `data.counterparty.id` | string | CUIT del titular de la cuenta destino. |
| `data.counterparty.name` | string | Nombre del titular de la cuenta destino. |
| `data.counterparty.id_type` | string | Valor fijo: `"CUIT_CUIL"`. |
| `data.counterparty.bank_routing.scheme` | string | `"NAME"` / `"UNAVAILABLE"`. |
| `data.counterparty.bank_routing.address` | string | Nombre del banco. |
| `data.counterparty.bank_routing.code` | string | Código del banco. |
| `data.counterparty.account_routing.scheme` | string | `"CBU"` / `"CVU"` / `"LABEL"` / `"UNAVAILABLE"`. |
| `data.counterparty.account_routing.address` | string | CBU, CVU o alias de la cuenta destino. |
| `data.details.origin_debit.cvu` | string | CBU/CVU de origen (puede no estar disponible). |
| `data.details.origin_debit.cuit` | string | CUIT de origen (puede no estar disponible). |
| `data.details.origin_credit.cvu` | string | CBU/CVU de destino (puede no estar disponible). |
| `data.details.origin_credit.cuit` | string | CUIT de destino (puede no estar disponible). |
| `data.transaction_ids` | array | IDs de procesamiento (banco + Coelsa). |
| `data.status` | string | `"PENDING"` / `"IN_PROGRESS"` / `"COMPLETED"` / `"FAILED"` / `"UNKNOWN"` / `"UNKNOWN_FOREVER"`. Solo se notifican estados definitivos. |
| `data.start_date` | datetime | Fecha de inicio. |
| `data.end_date` | datetime | Fecha de finalización. |
| `data.challenge` | string | Valor fijo: `""`. |
| `data.charge.summary` | string | Concepto: `"VAR"`, `"ALQ"`, `"CUO"`, `"EXP"`, `"FAC"`, `"PRE"`, `"SEG"`, `"HON"`, `"HAB"`. |
| `data.charge.value.currency` | string | `"ARS"`. |
| `data.charge.value.amount` | decimal | Monto. |

## Ejemplo JSON real

```json
{
  "id": "02defad8-c5dc-4cbc-ab54-367661d86f32",
  "object": "",
  "created": "2026-05-28T18:22:20.5530589Z",
  "data": {
    "id": "1-30717449076-000000092637177-1",
    "type": "TRANSFER",
    "from": {
      "bank_id": "322",
      "account_id": "20-1-735135-8-5"
    },
    "counterparty": {
      "id": "20322678275",
      "name": "Test1",
      "id_type": "CUIT_CUIL",
      "bank_routing": {
        "scheme": "UNAVAILABLE",
        "address": ""
      },
      "account_routing": {
        "scheme": "CVU",
        "address": "0000532608340370954151"
      }
    },
    "details": {
      "origin_debit": { "cvu": "", "cuit": "" },
      "origin_credit": { "cvu": "", "cuit": "" }
    },
    "transaction_ids": [
      "1-30717449076-000000092637177-1",
      "RD06ZO9WE4EOZD795GP7XY"
    ],
    "status": "COMPLETED",
    "start_date": "2026-05-28T18:22:21Z",
    "end_date": "2026-05-28T18:22:21Z",
    "challenge": "",
    "charge": {
      "summary": "VAR Devolución de Transferencia",
      "value": {
        "currency": "ARS",
        "amount": 200
      }
    }
  },
  "type": "TRANSFER",
  "redeliveries": 0
}
```

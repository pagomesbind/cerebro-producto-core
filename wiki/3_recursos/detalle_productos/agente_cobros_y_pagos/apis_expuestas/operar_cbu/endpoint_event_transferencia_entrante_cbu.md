# EVENT — Webhook: Aviso de Transferencia Entrante en CBU

> Fuente: https://psp.bind.com.ar/developers/apis/transfer-webhookentrantecbu
> Producto: Agente de Cobros — Operar CBU recaudadora

## Descripción

Se envía una notificación HTTP POST cada vez que llega una transferencia entrante directamente en el CBU de la cuenta recaudadora asociada a una entidad.

Cada webhook debe responderse con HTTP 200. De lo contrario, el envío ingresará en un esquema de reintentos.

La URL destino debe estar parametrizada previamente para este producto.

## Campos del Payload

| Campo | Tipo | Req | Descripción |
|-------|------|-----|-------------|
| `id` | string | REQ | ID guid del mensaje (prefijado con `"TRANSFERENCIA-"`). |
| `object` | string | OPT | Objeto del mensaje. |
| `created` | datetime | REQ | Fecha y hora de creación (UTC 0). |
| `type` | string | REQ | Tipo de evento. Valor: `"transfer.cbu.received"`. |
| `redeliveries` | int | REQ | Número de reintentos del banco. |
| `data.id` | string | REQ | ID del procesador de la transferencia (ID Coelsa). |
| `data.type` | string | REQ | Valor fijo: `"TRANSFER"`. |
| `data.from.bank_id` | string | REQ | Código del banco. Valor fijo: `"322"`. |
| `data.from.account_id` | string | REQ | Identificador de la cuenta recaudadora en el banco. |
| `data.counterparty.id` | string | REQ | CUIT del titular de la cuenta de origen. |
| `data.counterparty.name` | string | REQ | Nombre del titular de la cuenta de origen. |
| `data.counterparty.id_type` | string | REQ | Valor fijo: `"CUIT_CUIL"`. |
| `data.counterparty.bank_routing.scheme` | string | REQ | `"NAME"` / `"UNAVAILABLE"`. |
| `data.counterparty.bank_routing.address` | string | REQ | Nombre del banco. |
| `data.counterparty.account_routing.scheme` | string | REQ | `"CBU"` / `"CVU"` / `"LABEL"` / `"UNAVAILABLE"`. |
| `data.counterparty.account_routing.address` | string | REQ | CBU, CVU o alias de la cuenta. |
| `data.details.origin_debit.cvu` | string | REQ | CBU/CVU de origen. |
| `data.details.origin_debit.cuit` | string | REQ | CUIT de origen. |
| `data.details.origin_credit.cvu` | string | REQ | CBU de destino donde se acreditaron los fondos. |
| `data.details.origin_credit.cuit` | string | REQ | CUIT del titular de la cuenta de destino. |
| `data.transaction_ids` | array | REQ | IDs del procesador relacionados a la operación. |
| `data.status` | string | REQ | Solo se informan completadas: `"COMPLETED"`. |
| `data.start_date` | string | — | Fecha de inicio. |
| `data.end_date` | string | — | Fecha de finalización. |
| `data.charge.summary` | string | — | Concepto: `"VAR"`, `"ALQ"`, `"CUO"`, `"EXP"`, `"FAC"`, `"PRE"`, `"SEG"`, `"HON"`, `"HAB"`. |
| `data.charge.value.currency` | string | — | `"ARS"` / `"USD"`. |
| `data.charge.value.amount` | decimal | — | Monto. |

## Ejemplo JSON real

```json
{
  "id": "TRANSFERENCIA-46YGOW9MJGJ4ODP9EXD8J5",
  "object": "TransferEvent",
  "created": "2026-05-28T18:19:07.368",
  "data": {
    "id": "46YGOW9MJGJ4ODP9EXD8J5",
    "type": "TRANSFERENCIA",
    "from": {
      "bank_id": "322",
      "account_id": "20-1-735135-100-5"
    },
    "counterparty": {
      "id": "30717449076",
      "name": "BINDPAGOS SA",
      "id_type": "CUIT",
      "bank_routing": {
        "scheme": "cbu",
        "address": "3220001805007351351000"
      },
      "account_routing": {
        "scheme": "cbu",
        "address": "3220001805007351351000"
      }
    },
    "details": {
      "origin_debit": {
        "cvu": "0000532609240002744097",
        "cuit": "30717449076"
      },
      "origin_credit": {
        "cvu": "3220001805007351351000",
        "cuit": "30717449076"
      }
    },
    "transaction_ids": ["46YGOW9MJGJ4ODP9EXD8J5"],
    "status": "COMPLETED",
    "start_date": "2026-05-28T18:19:06Z",
    "end_date": "2026-05-28T18:19:07Z",
    "challenge": null,
    "charge": {
      "summary": "VAR ",
      "value": {
        "currency": "ARS",
        "amount": 6403
      }
    }
  },
  "type": "transfer.cbu.received",
  "redeliveries": 0
}
```

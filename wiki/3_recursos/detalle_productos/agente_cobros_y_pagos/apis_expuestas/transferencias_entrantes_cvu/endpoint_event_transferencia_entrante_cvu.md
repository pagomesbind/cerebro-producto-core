# EVENT — Webhook: Aviso de Transferencia Entrante en CVU

> Fuente: https://psp.bind.com.ar/developers/apis/transfer-webhookentrantecvu
> Producto: Agente de Cobros — Transferencias entrantes en CVU

## Descripción

Se envía una notificación HTTP POST cada vez que llega una transferencia entrante en un CVU de la Entidad.

Cada webhook debe responderse con HTTP 200. De lo contrario, el envío ingresará en un esquema de reintentos.

La URL destino debe estar parametrizada previamente para este producto.

## Campos del Payload

| Campo | Tipo | Req | Descripción |
|-------|------|-----|-------------|
| `id` | string | REQ | ID guid del mensaje (prefijado con `"CASHOUT-"`). |
| `object` | string | OPT | Objeto del mensaje. |
| `created` | datetime | REQ | Fecha y hora de creación del mensaje (UTC 0). |
| `type` | string | REQ | Tipo de evento. Valor: `"transfer.cvu.received"`. |
| `redeliveries` | int | REQ | Número de reintentos del banco para informar la transferencia. |
| `data.id` | string | REQ | ID del procesador de la transferencia (ID Coelsa). |
| `data.type` | string | REQ | Valor fijo: `"TRANSFER"`. |
| `data.from.bank_id` | string | REQ | Código de banco. Valor fijo: `"322"`. |
| `data.from.account_id` | string | REQ | Identificador de la cuenta recaudadora en el banco. |
| `data.counterparty.id` | string | REQ | CUIT del titular de la cuenta de origen. |
| `data.counterparty.name` | string | REQ | Nombre del titular de la cuenta de origen. |
| `data.counterparty.id_type` | string | REQ | Valor fijo: `"CUIT_CUIL"`. |
| `data.counterparty.bank_routing.scheme` | string | REQ | `"NAME"` / `"UNAVAILABLE"`. |
| `data.counterparty.bank_routing.address` | string | REQ | Nombre del banco. |
| `data.counterparty.account_routing.scheme` | string | REQ | `"CBU"` / `"CVU"` / `"LABEL"` / `"UNAVAILABLE"`. |
| `data.counterparty.account_routing.address` | string | REQ | Valor de identificación de la cuenta. |
| `data.details.origin_debit.cvu` | string | REQ | CVU de origen (débito). |
| `data.details.origin_debit.cuit` | string | REQ | CUIT del titular de la cuenta de origen. |
| `data.details.origin_credit.cvu` | string | REQ | CVU de destino (crédito). |
| `data.details.origin_credit.cuit` | string | REQ | CUIT del titular de la cuenta de destino. |
| `data.transaction_ids` | array | REQ | IDs del procesador relacionados a la operación. |
| `data.status` | string | REQ | Estado. Solo se informan completadas: `"COMPLETED"`. |
| `data.start_date` | string | REQ | Fecha de inicio de la transferencia. |
| `data.end_date` | string | REQ | Fecha de finalización de la transferencia. |
| `data.charge.summary` | string | REQ | Concepto: `"VAR"`, `"ALQ"`, `"CUO"`, `"EXP"`, `"FAC"`, `"PRE"`, `"SEG"`, `"HON"`, `"HAB"`. |
| `data.charge.value.currency` | string | REQ | Moneda. Valor: `"ARS"`. |
| `data.charge.value.amount` | decimal | REQ | Monto de la transferencia. |

## Ejemplo JSON real

```json
{
  "id": "CASHOUT-Z6OLMDN3VODEJKO62E7RQ5",
  "object": "ApiTransaction",
  "created": "2026-06-01T20:59:17.166Z",
  "data": {
    "id": "Z6OLMDN3VODEJKO62E7RQ5",
    "type": "TRANSFER",
    "from": {
      "bank_id": "322",
      "account_id": "20-1-749049-13-5"
    },
    "counterparty": {
      "id": "27265540703",
      "name": "Maria Nicolasa Acuna",
      "id_type": "CUIT_CUIL",
      "bank_routing": {
        "scheme": "UNAVAILABLE",
        "address": ""
      },
      "account_routing": {
        "scheme": "CVU",
        "address": "0000003100069103363490"
      }
    },
    "details": {
      "origin_debit": null,
      "origin_credit": {
        "cvu": "0000184302080000092603",
        "cuit": "33710449959"
      }
    },
    "transaction_ids": ["Z6OLMDN3VODEJKO62E7RQ5"],
    "status": "COMPLETED",
    "start_date": null,
    "end_date": null,
    "challenge": null,
    "charge": {
      "summary": "VAR",
      "value": {
        "currency": "ARS",
        "amount": 77070
      }
    }
  },
  "type": "transfer.cvu.received",
  "redeliveries": 0
}
```

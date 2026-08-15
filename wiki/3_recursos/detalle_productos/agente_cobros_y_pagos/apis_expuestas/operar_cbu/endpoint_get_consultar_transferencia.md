# GET — Consultar Transferencia (CBU)

> Fuente: https://psp.bind.com.ar/developers/apis/transfer-consultartransferencia
> Producto: Agente de Cobros — Operar CBU recaudadora

## Descripción

Devuelve información de una transferencia previamente realizada.

## URL / Método

| Campo | Valor |
|-------|-------|
| Método | `GET` |
| URL (Staging) | `https://gw-staging-qrbind.epays.services/cvucollectentidad-financial/v1/v1.201/banks/322/accounts/owner/transaction-request-types/TRANSFER/{transaction_id}` |

## Parámetros del Request

| Parámetro | Tipo | Requerido | Descripción |
|-----------|------|-----------|-------------|
| `transaction_id` | string (path) | REQUIRED | ID del procesador (ID Coelsa) u `origin_id` indicado al realizar la transferencia saliente. |

## Bloque curl request

```bash
curl -v -X GET "https://gw-staging-qrbind.epays.services/cvucollectentidad-financial/v1/v1.201/banks/322/accounts/owner/transaction-request-types/TRANSFER/202606021036" \
-H "Cache-Control: no-cache" \
-H "Authorization: Bearer {{access_token}}"
```

## Response

| Campo | Tipo | Descripción |
|-------|------|-------------|
| `id` | string | ID de la transferencia. En entrantes, corresponde al ID Coelsa. |
| `type` | string | Valor fijo: `"TRANSFER"`. |
| `from.bank_id` | string | Código del banco. Valor fijo: `"322"`. |
| `from.account_id` | string | Número de cuenta recaudadora. |
| `counterparty.id` | string | CUIT/CUIL del titular de origen. |
| `counterparty.name` | string | Nombre del titular de origen. |
| `counterparty.id_type` | string | Valor fijo: `"CUIT_CUIL"`. |
| `counterparty.bank_routing.scheme` | string | `"NAME"` / `"UNAVAILABLE"`. |
| `counterparty.bank_routing.address` | string | Nombre del banco de la contraparte. |
| `counterparty.account_routing.scheme` | string | `"CBU"` / `"CVU"` / `"LABEL"` / `"UNAVAILABLE"`. |
| `counterparty.account_routing.address` | string | CBU, CVU o alias de la cuenta contraparte. |
| `details.origin_id` | string | Identificador definido originalmente por el usuario. |
| `transaction_ids` | array | IDs de procesamiento (banco + Coelsa). |
| `status` | string | `"PENDING"` / `"IN_PROGRESS"` / `"COMPLETED"` / `"FAILED"` / `"UNKNOWN"` / `"UNKNOWN_FOREVER"`. |
| `start_date` | datetime | Fecha y hora de inicio. |
| `end_date` | datetime | Fecha y hora de finalización. |
| `charge.summary` | string | Concepto: `"VAR"`, `"ALQ"`, `"CUO"`, `"EXP"`, `"FAC"`, `"PRE"`, `"SEG"`, `"HON"`, `"HAB"`. |
| `charge.value.currency` | string | `"ARS"` / `"USD"`. |
| `charge.value.amount` | double | Monto. |

## Códigos HTTP

| Código | Descripción |
|--------|-------------|
| `200` | Consulta exitosa |
| `401` | Token de autenticación inválido |

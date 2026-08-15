# GET — Consultar Transferencias (Agente de Cobros CVU)

> Fuente: https://psp.bind.com.ar/developers/apis/transfer-consultartransferencias
> Producto: Agente de Cobros — Transferencias entrantes en CVU

## Descripción

Devuelve una lista de transferencias entrantes y salientes en CVUs o en la cuenta recaudadora de la entidad junto con toda su información.

## URL / Método

| Campo | Valor |
|-------|-------|
| Método | `GET` |
| URL (Staging) | `https://gw-staging-qrbind.epays.services/cvucollectentidad-financial/v1/v1.201/banks/322/accounts/transfers` |

## Parámetros del Request (headers)

| Parámetro | Tipo | Requerido | Descripción |
|-----------|------|-----------|-------------|
| `start` | string | OPTIONAL | Número de página. Default: `1`. |
| `length` | string | OPTIONAL | Registros por página. Default: `50`. |
| `type` | string | OPTIONAL | `"TRANSFERENCIAS_RECIBIDAS"` = entrantes / `"TRANSFER"` = salientes. |
| `fromDate` | string | OPTIONAL | Fecha/hora desde la que consultar (ej: `2023-12-20 00:00`). |
| `toDate` | string | OPTIONAL | Fecha/hora hasta la que consultar (ej: `2023-12-20 23:00`). |
| `cvu` | string | OPTIONAL | CVU donde se acreditó la transferencia. |
| `clientId` | string | OPTIONAL | `clientId` con el que se creó el CVU. |
| `transferenceId` | string | OPTIONAL | ID Coelsa de la transacción. |

## Bloque curl request

```bash
curl --location 'https://gw-staging-qrbind.epays.services/cvucollectentidad-financial/v1/v1.201/banks/322/accounts/transfers' \
--header 'start: 1' \
--header 'type: TRANSFERENCIAS_RECIBIDAS' \
--header 'fromDate: 2023-12-20 00:00' \
--header 'toDate: 2023-12-20 23:00' \
--header 'cvu: 0000532600001003222228' \
--header 'Authorization: Bearer {{access_token}}'
```

## Response

| Campo | Tipo | Descripción |
|-------|------|-------------|
| `id` | string | ID de Coelsa de la transferencia. |
| `type` | string | Valor fijo: `"TRANSFER"` |
| `from.bank_id` | string | Código de banco. Valor fijo: `"322"`. |
| `from.account_id` | string | Identificador de la cuenta recaudadora. |
| `counterparty.id` | string | CUIT del titular de la cuenta de origen. |
| `counterparty.name` | string | Nombre del titular de la cuenta de origen. |
| `counterparty.id_type` | string | Valor fijo: `"CUIT_CUIL"` |
| `counterparty.bank_routing.scheme` | string | Tipo de identificación del banco: `"NAME"` / `"UNAVAILABLE"`. |
| `counterparty.bank_routing.address` | string | Nombre del banco. |
| `counterparty.bank_routing.code` | string | Código del banco. |
| `counterparty.account_routing.scheme` | string | `"CBU"` / `"LABEL"` / `"UNAVAILABLE"`. |
| `counterparty.account_routing.address` | string | Valor de identificación de la cuenta. |
| `details.type` | string | Tipo de transferencia. Valor posible: `"TRANSFERENCIAS_RECIBIDAS"`. |
| `details.origin_id` | string | Identificador unívoco de la transacción. |
| `details.origin_debit.cvu` | string | CVU de origen desde donde se debitaron los fondos. |
| `details.origin_debit.cuit` | string | CUIT del titular de la cuenta de origen. |
| `details.origin_credit.cvu` | string | CVU de destino donde se acreditaron los fondos. |
| `details.origin_credit.cuit` | string | CUIT del titular de la cuenta de destino. |
| `details.transaction_ids` | object | Todos los IDs de Coelsa relacionados a la operación. |
| `status` | string | Estado de la transferencia. Entrantes: `"TRANSFERENCIAS_RECIBIDAS"`. |
| `start_date` | string | Fecha de inicio de la transferencia. |
| `end_date` | string | Fecha de finalización de la transferencia. |
| `charge.summary` | string | Concepto de la transferencia. |
| `charge.value.currency` | string | Moneda. Valor: `"ARS"`. |
| `charge.value.amount` | decimal | Monto de la transferencia. |
| `business_date` | datetime | Fecha de negocio (UTC 0). |

## Códigos HTTP

| Código | Descripción |
|--------|-------------|
| `200` | Consulta exitosa |
| `401` | Token de autenticación inválido |

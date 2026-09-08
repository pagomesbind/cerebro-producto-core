# API BANK — Eventos (payloads de webhooks)

> Grupo **Eventos**: no son endpoints que el cliente (Bind) invoque, sino la **documentación de los payloads** que el banco envía al webhook configurado por el cliente (ver grupo [Webhooks](webhooks.md), endpoint `AltaModificacionWebhook`). Cada uno de los 10 endpoints de este grupo documenta el `type` de evento y la forma de su `data`. Todos comparten el sobre (envelope) común:

| Campo del sobre | Tipo | Descripción |
|------------------|------|-------------|
| `id` | String | Identificador único del mensaje webhook. |
| `object` | String | Tipo de objeto — varía por evento (`ApiTransaction`, `Endpoint`, `ClientAccountUpdateEvent`, `TransferEvent`, `TransferEventMep`). |
| `created` | DateTime | Fecha de creación del mensaje. |
| `data` | Object | Contenido específico del evento — su forma depende de `object`/`type`. |
| `type` | String | Descripción concreta del evento (ej. `debin.acredited`, `transfer.cvu.received`). |
| `redeliveries` | Number | Número de reintento de este envío. |

Este contrato de sobre es el mismo que documenta `WebhookTestSendMessage` (grupo Webhooks) para simular estos eventos.

**Nota transversal importante:** en varios de estos eventos, el portal marca explícitamente varios campos como **deprecados** ("este campo será eliminado en futuras versiones") — puntualmente `details.origin_id`, `status` (a nivel raíz de `data`, distinto del `status` dentro de la propia estructura de transacción), `start_date` y `end_date` en los eventos basados en `object: ApiTransaction`. Cualquier integración nueva de Bind con estos webhooks debería evitar depender de esos campos.

## 1. Webhook creado — `WebhookCreated`

> Fuente: https://sandbox.bind.com.ar/apidoc/#api-Eventos-WebhookCreated

Se envía al dar de alta la URL de un webhook, **para confirmar que quedó correctamente configurado**. Si este envío falla, se rechaza la creación del webhook.

`object: "Endpoint"`, `type: "endpoint.created"`.

### `data`

`url`, `description`, `enabled` (Boolean), `events[]` (catálogo Referencias-EventsEnpoints).

### Ejemplo

```json
{
  "id": "23611c4d-3576-483e-aca4-2d19ca080d79",
  "object": "Endpoint",
  "created": "2018-09-27T19:41:44.667Z",
  "data": { "url": "https://unlugar.com/webhook/", "description": "una descripción", "enabled": true, "events": ["ALL"] },
  "type": "endpoint.created",
  "redeliveries": 0
}
```

## 2. Debin acreditado — `WebhookAcreditedDebin`

> Fuente: https://sandbox.bind.com.ar/apidoc/#api-Eventos-WebhookAcreditedDebin

`object: "ApiTransaction"`, `type: "debin.acredited"`.

### `data` — atributos principales

`id`, `type` (default `DEBIN`), `from.account_id`, `details.sellerCuit`/`.sellerAccountCBU`/`.buyerAcountCBU`/`.buyerAccountLabel`/`.buyerCuit`, `transaction_ids[]`, `status` (default `COMPLETED`, **deprecado**), `status_description`, `charge.summary`/`.value.currency`/`.value.amount`.

### Ejemplo (resumido)

```json
{
  "data": {
    "id": "JMRD06ZO9WX5Z125GP7XY3",
    "type": "DEBIN",
    "from": { "account_id": "21-1-99999-4-6" },
    "details": { "sellerCuit": "30714423033", "sellerAccountCBU": "3220001805000046360015", "buyerAccountCBU": "3220001823000055910025", "buyerCuit": "20263385072", "buyerAccountLabel": "aliasCbu" },
    "transaction_ids": ["JMRD06ZO9WX5Z125GP7XY3"],
    "status": "COMPLETED",
    "status_description": "ACREDITADO",
    "charge": { "summary": "FAC", "value": { "currency": "ARS", "amount": 0.16 } }
  },
  "type": "debin.acredited"
}
```

## 3. Debin rechazado — `WebhookRejectedDebin`

> Fuente: https://sandbox.bind.com.ar/apidoc/#api-Eventos-WebhookRejectedDebin

Mismo contrato que `WebhookAcreditedDebin`. `type: "debin.rejected"`, `status` default `REJECTED_CLIENT`.

### Ejemplo destacado

```json
{ "status": "REJECTED_CLIENT", "status_description": "RECHAZO DE CLIENTE" }
```

Este es el evento a escuchar cuando el comprador **rechaza explícitamente** un DEBIN.

## 4. Debin desconocido por comprador — `WebhookRefundedDebin`

> Fuente: https://sandbox.bind.com.ar/apidoc/#api-Eventos-WebhookRefundedDebin

Mismo contrato que los anteriores. `type: "debin.refunded"`, `status` default `REFUNDED` (según el ejemplo, aunque la descripción del parámetro dice default `ACCREDITED` — **posible inconsistencia en la fuente**, ver nota abajo).

### Nota — inconsistencia de la fuente

La descripción de `body.data.status` en este endpoint dice *"El estado default es ACCREDITED, aunque el monto del DEBIN fue devuelto al comprador. Valor por defecto: ACCREDITED"*, pero el ejemplo de payload muestra `"status": "REFUNDED"` y `"status_description": "DEVUELTO"`. Es decir, la documentación del campo y el ejemplo no coinciden. Semánticamente, este evento representa un DEBIN que **fue acreditado y luego devuelto** (el comprador lo desconoció después del hecho) — a diferencia de `WebhookRejectedDebin`, que es un rechazo antes de la acreditación.

### Ejemplo

```json
{ "status": "REFUNDED", "status_description": "DEVUELTO", "charge": { "summary": "VAR", "value": { "currency": "ARS", "amount": 0.03 } } }
```

## 5. Cuenta cliente — `WebhookPsiClientAccount`

> Fuente: https://sandbox.bind.com.ar/apidoc/#api-Eventos-WebhookPsiClientAccount

Informa una novedad en la cuenta de un cliente PSI/STI (ver grupo [Alta_De_Cuenta](alta_de_cuenta.md)): si fue creada o rechazada. `object: "ClientAccountUpdateEvent"`, `type: "client.account.updated"`.

### `data` — atributos

`workflow_id`, `workflow_status` (**solo puede ser `ACCOUNT_ACTIVE` o `REJECTED`** en este evento — más acotado que el catálogo completo de `PSIConsultarEstadoFlujoAlta`), `product_id`, `account_status`, `document`/`document_type`, `context_cuit` (CUIT del PSI/STI), `accounts[]` (mismo contrato que en `PSIConsultarEstadoFlujoAlta`: `account_id`, `currency`, `cbu`, `token`, `expiration_date`, `account_active`).

### Ejemplos

Cuenta creada: `workflow_status: "ACCOUNT_ACTIVE"`, con hasta 3 cuentas asociadas (ARS/USD) cada una con su propio `account_active`.
Cuenta rechazada: `workflow_status: "REJECTED"`, cuentas sin `token` ni `expiration_date` (no llegaron a activarse).

## 6. Transferencias recibidas en CBU — `WebhookTransferCbuReceived`

> Fuente: https://sandbox.bind.com.ar/apidoc/#api-Eventos-WebhookTransferCbuReceived

Informa que se ingresó dinero a un CBU. `object: "TransferEvent"`, `type: "transfer.cbu.received"`. Estructura distinta a los eventos basados en `ApiTransaction` — usa el par `credit`/`debit`.

### `data` — atributos

| Campo | Descripción |
|-------|-------------|
| `credit.bank_account.*` | Cuenta destino: `account_id`, `tax_id` (CUIT), `cbu`, `name`, `bank`, `branch`. |
| `debit.bank_account.*` | Cuenta origen (si es de otro banco/CBU): mismos sub-campos. |
| `debit.virtual_account.*` | Cliente de billetera virtual origen (si el origen fue un CVU): `tax_id`, `cvu`, `name`, `psp.id`/`psp.tax_id`. |
| `transfer_type` | `TRANSFERENCIA` o `CREDIN`. |
| `net_id` / `net_name` | Id y nombre de la red que generó el crédito (ej. `LINK`, `COELSA`). |
| `core_id` | Id del core bancario. |
| `origin_id` | Id de la transacción en el originante. |
| `amount` / `currency` | Importe. |
| `concept` / `reference` | Concepto y referencia. |
| `operation_date` / `business_date` | Fecha de generación del movimiento / fecha de conciliación. |

### Tres variantes de ejemplo documentadas

1. **CBU a CBU** (`net_name: "LINK"`) — sin `debit.virtual_account`.
2. **CVU a CBU, sin cuenta recaudadora informada** (`net_name: "COELSA"`) — solo `debit.virtual_account`, sin `debit.bank_account`.
3. **CVU a CBU, con cuenta recaudadora informada** — trae **ambos** `debit.bank_account` y `debit.virtual_account` simultáneamente (la cuenta recaudadora bancaria que sostiene el CVU, más los datos del cliente final de la billetera).

Esta tercera variante es clave para que Bind pueda mapear una transferencia entrante a la cuenta recaudadora física (banco) y, al mismo tiempo, al cliente final dueño del CVU dentro de su plataforma.

## 7. Transferencia MEP completada — `WebhookTransferMEP`

> Fuente: https://sandbox.bind.com.ar/apidoc/#api-Eventos-WebhookTransferMEP

`object: "TransferEventMep"`, `type: "transfer.mep.completed"`. Mismo patrón `credit`/`debit` que `WebhookTransferCbuReceived`, más los campos propios de MEP: `transfer_type: "TRANSFER-MEP"`, `net_id` (**id generado por el BCRA** — corresponde al `bcra_operation_number` que devuelven `ObtenerTransferenciaMEP`/`ObtenerTransferenciasMEP`), `net_name` (default `BCRA`), `status` (default `COMPLETED`), `status_description`, `mep_operation`, `observation`, `investment_type`, `origin_fund`, `creditor_entity`, `creditor_account`, `description`.

## 8. Transferencia MEP rechazada — `WebhookTransferMEPRejected`

> Fuente: https://sandbox.bind.com.ar/apidoc/#api-Eventos-WebhookTransferMEPRejected

Mismo contrato que `WebhookTransferMEP`, `type: "transfer.mep.rejected"`, `status` default `FAILED`.

## 9. Transferencias recibidas en CVU — `WebhookTransferCvuReceived`

> Fuente: https://sandbox.bind.com.ar/apidoc/#api-Eventos-WebhookTransferCvuReceived

Informa que se realizó una transferencia a un CVU de la cuenta recaudadora. `object: "ApiTransaction"`, `type: "transfer.cvu.received"`. Estructura equivalente al response de `ObtenerPedidoTransferenciaCvu` (grupo Billetera): `id`, `type` (default `TRANSFER`), `from.bank_id`/`.account_id`, `counterparty.*`, `details.origin_credit.cvu`/`.cuit` (o `details.origin_debit` según el sentido), `transaction_ids[]`, `status` (**deprecado**), `status_description`, `challenge`, `charge.*`.

### Ejemplo con `counterparty` no disponible (transferencia interna/CVU→CVU sin datos de tercero completos)

```json
{
  "id": "ESTE1ES2UN3ID4DE5DEBIN",
  "type": "TRANSFER",
  "from": { "bank_id": "322", "account_id": "21-1-99999-4-6" },
  "counterparty": { "id": "UNAVAILABLE", "name": "UNAVAILABLE", "id_type": "UNAVAILABLE", "bank_routing": { "scheme": "UNAVAILABLE", "address": null }, "account_routing": { "scheme": "UNAVAILABLE", "address": "UNAVAILABLE" } },
  "details": { "origin_credit": { "cvu": "0000031400000000000031", "cuit": "30615423323" } },
  "status": "COMPLETED"
}
```

## 10. Transferencia CVU reversada — `WebhookTransferCvuReversed`

> Fuente: https://sandbox.bind.com.ar/apidoc/#api-Eventos-WebhookTransferCvuReversed

Informa que se **reversó una transferencia emitida desde un CVU** (el crédito en destino tuvo un problema y la operación se revierte). `type: "transfer.cvu.reversed"` (nota: el default documentado en el parámetro `body.type` dice `transfer.cvu.received`, pero el ejemplo real usa `transfer.cvu.reversed` — inconsistencia menor de copia en la fuente, prevalece el ejemplo).

### Ejemplo destacado

```json
{
  "status": "FAILED",
  "statusDescription": "Problemas con el Crédito. REVERSAR",
  "business_date": "2018-04-12T03:00:00.000Z",
  "type": "transfer.cvu.reversed"
}
```

Este evento es importante operativamente: indica que una transferencia que salió de un CVU de Bind tuvo que revertirse por un problema del lado del crédito en destino — el sistema que consume este webhook debe reponer los fondos en el CVU de origen si corresponde (mismo criterio que la mecánica de `FAILED` documentada en `CrearTransferenciaCVU`, grupo Billetera).

## Nota de relevamiento

Grupo completo (10/10 endpoints relevados) desde `https://sandbox.bind.com.ar/apidoc/api_data.json`. Se detectaron dos inconsistencias menores en la documentación fuente del propio portal (no introducidas por este relevamiento, señaladas explícitamente arriba): el estado default documentado de `WebhookRefundedDebin` no coincide con su ejemplo, y el `type` default documentado de `WebhookTransferCvuReversed` (`transfer.cvu.received`) no coincide con el `type` real de su ejemplo (`transfer.cvu.reversed`). El catálogo completo de valores posibles para `events` (`Referencias-EventsEnpoints`, usado en `AltaModificacionWebhook`) pertenece al grupo `Referencias`, fuera de esta ronda.

> Capturado por Pablo Gomes, 2026-09-01.

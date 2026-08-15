# Webhook de Transferencia Entrante a CBU — Astropay

> Estado: en producción. Reubicado desde `detalle_productos/cobros/configuracion_y_operacion.md §3` en la reestructuración PARA en cascada (2026-08-12).

# Alcance
El alcance de este documento es informativo y apto para desarrollo.
# Objetivo
El objetivo de este documento es expandir la documentación de webhooks de aviso de transferencia entrante del producto Agente de cobros y pagos para considerar, también, transferencias al CBU en pesos y dolares.
# Objeto
El objeto de este documento está dirigido específicamente a una necesidad de Astropay.

# API
## Webhook de creación de comprobante por cobro
Se dispara un webhook a la organización cuando el banco nos notifica que ingresó en la cuenta recaudadora una transferencia entrante a un CVU o al CBU.
> Se envía el webhook a url configurada para webhooks del collector en el producto AGENTE DE COBROS Y PAGOS. Política de reintentos: ver [3_recursos/arquitectura_sistema/politica_de_reintentos_de_webhook.md §3](../../arquitectura_sistema/politica_de_reintentos_de_webhook.md) — este canal (CVUCollect) tiene una excepción sin confirmar respecto de la política general.

### Request
Atributos del request body:

| Atributo | Tipo | Descripción | Valores posibles |
|---|---|---|---|
| `id` | string | Identificador del mensaje | — |
| `object` | string | Componente que envía el mensaje | — |
| `created` | datetime | Fecha y hora en que se creó la transferencia | — |
| `data` | object | Objeto que contiene la información de la transferencia | — |
| `data.id` | string | Identificador principal de la transferencia | — |
| `data.type` | string | Descripción del tipo de transacción | Puede ser `null` |
| `data.from` | object | Objeto con información del origen de la transacción | — |
| `data.from.bank_id` | string | Código de banco de la cuenta origen. | `"322"` |
| `data.from.account_id` | string | Id de la cuenta recaudadora | Puede ser `null` |
| `data.counterparty` | object | Objeto con información de la contraparte | — |
| `data.counterparty.id` | string | Identificación de la contraparte (CUIT de la contraparte) | — |
| `data.counterparty.name` | string | Nombre del titular de la cuenta del contraparte | Puede ser `null` |
| `data.counterparty.id_type` | string | Describe el tipo de identificació de la contrañarte | `"TRANSFER"`, `"TRANSFERENCIA"`, Puede ser `null` |
| `data.counterparty.bank_routing` | string | Contiene información del banco de la contraparte. Generalmente, esta información no está disponible en línea en transferencias recibidas. | — |
| `data.counterparty.bank_routing.scheme` | string | Tipo de dato de identificación del banco | Puede ser `null` |
| `data.counterparty.bank_routing.address` | string | Nombre del banco | Puede ser `null` |
| `data.counterparty.account_routing` | object | Contiene información de la cuenta de la contraparte | — |
| `data.counterparty.account_routing.scheme` | string | Tipo de identificación de la cuenta | Puede ser `null` |
| `data.counterparty.account_routing.address` | string | Valor de identificación de la cuenta | Puede ser `null` |
| `data.details` | object | Contiene información de la transferencia | — |
| `data.details.origin_debit` | object | Contiene información del origen de la transferencia entrante | — |
| `data.details.origin_debit.cvu` | string | CVU/CBU de la cuenta de origen desde donde se debitaron los fondos de la transferencia | Puede ser `null` |
| `data.details.origin_debit.cuit` | string | CUIT del titular de la cuenta de origen desde donde se debitaron los fondos de la transferencia | — |
| `data.details.origin_credit` | object | Contiene información del destino de la transferencia entrante | — |
| `data.details.origin_credit.cvu` | — | CVU/CBU de la cuenta de destino donde se acreditaron los fondos de la transferencia | En transferencia recibida en CBU sería el CBU de la cuenta recaudadora. |
| `data.details.origin_credit.cuit` | — | CUIT del titular de la cuenta de destino donde se acreditaron los fondos de la transferencia | En transferencia recibida en CBU sería el CUIT del titular de la cuenta recaudadora. |
| `data.transaction_ids` | array | Contiene todos los ID de procesamiento relacionados a la operación | — |
| `data.status` | string | Estado de la transferencia | `"COMPLETED"` |
| `data.start_date` | datetime | Fecha de inicio de la transferencia. | Puede ser `null` |
| `data.end_date` | datetime | Fecha de finalización de la transferencia. | Puede ser `null` |
| `data.challenge` | string | Siempre vacío. | — |
| `data.charge` | object | Objeto con información de los cargos de la transacción | — |
| `data.charge.summary` | string | Concepto de la transferencia | `"ALQ"`, `"CUO"`, `"EXP"`, `"FAC"`, `"PRE"`, `"SEG"`, `"HON"`, `"HAB"`, `"VAR"` |
| `data.charge.value` | object | Objeto con información del importe de la transacción | — |
| `data.charge.value.currency` | string | Moneda de la transferencia | `"ARS"`, `"USD"` |
| `data.charge.value.amount` | string | Importe de la transferencia | — |
| `type` | string | Tipo de evento notificado | `"transfer.cvu.received"`, `"transfer.cbu.received"` |
| `redeliveries` | int | Número de reintentos que realizó el banco para informar la transferencia | — |

### Ejemplo de request body de webhook recibido a CBU:
```json
{
    "id": "ID-iasjdosd-23443-g",
    "object": "ApiTransaction",
    "created": "2026-01-08T19:32:24.359",
    "data": {
        "id": "QATEST709RGEDF5WEDWERF493",
        "type": null,
        "from": {
            "bank_id": "322",
            "account_id": ""
        },
        "counterparty": {
            "id": "20344364836",
            "name": null,
            "id_type": "CUIT",
            "bank_routing": {
                "scheme": null,
                "address": null
            },
            "account_routing": {
                "scheme": null,
                "address": null
            }
        },
        "details": {
            "origin_debit": {
                "cvu": null,
                "cuit": "20344364836"
            },
            "origin_credit": {
                "cvu": "3220001823007351770016",
                "cuit": "30718596277"
            }
        },
        "transaction_ids": [
            "QATEST709RGEDF5WEDWERF493"
        ],
        "status": "COMPLETED",
        "start_date": null,
        "end_date": "2026-01-08T19:32:24Z",
        "challenge": null,
        "charge": {
            "summary": "VAR",
            "value": {
                "currency": "USD",
                "amount": 12553.62
            }
        }
    },
    "type": "transfer.cbu.received",
    "redeliveries": 0
}
```
### Ejemplo de request body de webhook recibido a CVU:
```json
{
    "id": "CASHOUT-Z6OLMDN3VP1Z08LY2E7RQ5",
    "object": "ApiTransaction",
    "created": "2026-01-08T14:28:24.692Z",
    "data": {
        "id": "Z6OLMDN3VP1Z08LY2E7RQ5",
        "type": "TRANSFER",
        "from": {
            "bank_id": "322",
            "account_id": "20-1-749049-13-0"
        },
        "counterparty": {
            "id": "23258805364",
            "name": "CARINA ALMARAZ",
            "id_type": "CUIT_CUIL",
            "bank_routing": {
                "scheme": "UNAVAILABLE",
                "address": ""
            },
            "account_routing": {
                "scheme": "CBU",
                "address": "4530000800019917251467"
            }
        },
        "details": {
            "origin_debit": null,
            "origin_credit": {
                "cvu": "0000184302080098799237",
                "cuit": "33710449959"
            }
        },
        "transaction_ids": [
            "Z6OLMDN3VP1Z08LY2E7RQ5"
        ],
        "status": "COMPLETED",
        "start_date": null,
        "end_date": null,
        "challenge": null,
        "charge": {
            "summary": "VAR",
            "value": {
                "currency": "ARS",
                "amount": 45056
            }
        }
    },
    "type": "transfer.cvu.received",
    "redeliveries": 0
}
```

## Ver también
- [cuenta_recaudadora_usd.md §1](cuenta_recaudadora_usd.md) — diferenciación CBU vs CVU en este mismo webhook, para el caso multi-moneda.
- [crear_collector.md](crear_collector.md) — cómo se configura el collector que recibe este webhook.

---
*Última actualización: 2026-08-12 — Reubicado desde `detalle_productos/cobros/configuracion_y_operacion.md §3` (reestructuración PARA en cascada). Contenido sin cambios.*

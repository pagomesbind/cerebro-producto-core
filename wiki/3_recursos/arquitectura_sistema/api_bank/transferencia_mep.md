# API BANK — TransferenciaMEP

> Grupo **TransferenciaMEP**: transferencias MEP (Mercado Electrónico de Pagos) — operatoria bursátil/BCRA usada para suscripción/rescate de fondos comunes de inversión, cancelación de saldos deudores de mercado de capitales, y transferencias entre cuentas propias o de terceros (incluso en moneda extranjera). Grupo más especializado que [Transferencia](transferencia.md)/[Billetera](billetera.md) — no está directamente ligado a CVU/CBU de Wallet o Agente de Cobros y Pagos, pero se incluye por relevancia transversal al dominio de transferencias de API BANK. Header `Authorization: JWT :token` obligatorio en todos. `bank_id` siempre `322`, `view_id` siempre `"owner"`.

### Catálogo de operatorias (`mep_operation`)

| Código | Descripción |
|--------|-------------|
| `GC1` | Suscripción de Fondos Comunes de Inversión y de Fideicomisos. |
| `GC2` | Rescates de Fondos Comunes de Inversión y Fideicomisos. |
| `D20` | Cancelación de Saldos Deudores por Operaciones de Mercado de Capitales. |
| `DL0` | Transferencias entre Cuentas del Mismo Titular. |
| `DL1` | Transferencias entre Cuentas GRAVADAS en Origen. |
| `DL2` | Transferencias entre Cuentas NO GRAVADAS en Origen. |
| `DR0` | Transferencias entre Cuentas del Mismo Titular, en Moneda Extranjera. |
| `DR1` | Transferencias entre Cuentas GRAVADAS en Origen, en Moneda Extranjera. |
| `DR2` | Transferencias entre Cuentas NO GRAVADAS en Origen, en Moneda Extranjera. |

## 1. Realizar transferencia MEP — `CrearTransferenciaMEP`

> Fuente: https://sandbox.bind.com.ar/apidoc/#api-TransferenciaMEP-CrearTransferenciaMEP

### URL / Método

| Campo | Valor |
|-------|-------|
| Método | `POST` |
| URL | `/banks/:bank_id/accounts/:account_id/:view_id/transaction-request-types/TRANSFER-MEP/transaction-requests` |

### Parámetros del request

| Parámetro | Tipo | Obligatorio | Descripción |
|-----------|------|-------------|-------------|
| `bank_id`, `account_id` (cuenta origen), `view_id` | — | Sí | Estándar. |
| `body.origin_id` | String | Sí | Id único, máx. 15 caracteres, idempotente. |
| `body.mep_operation` | String | Sí | Código de operatoria (tabla arriba). |
| `body.to.cbu` | String | Condicional | Obligatorio para `GC1`, `DL0`, `DL1`, `DL2`, `DR0`, `DR1`, `DR2`. |
| `body.to.cuit` | String | Condicional | Obligatorio para `GC1`, `GC2`, `DL0`, `DL1`, `DL2`, `DR0`, `DR1`, `DR2`. |
| `body.to.beneficiary_name` | String | Condicional | Obligatorio para `DL1`, `DL2`, `DR1`, `DR2`. |
| `body.to.creditor_entity` | String | Condicional | Obligatorio para `GC2`, `D20`. |
| `body.to.creditor_account` | String | Condicional | Obligatorio para `GC2`, `D20`. |
| `body.value.currency` | String | Sí | `ARS` o `USD`. Para `DR0`/`DR1`/`DR2` **solo se acepta `USD`**. |
| `body.value.amount` | Number | Sí | Importe. |
| `body.description` | String | Condicional | Máximo 30 caracteres. Obligatorio para `GC2`, opcional para `GC1`/`D20`. |
| `body.observation` | String | Condicional | Obligatorio en `DL0`, `DL1`, `DL2`, `DR0`, `DR1`, `DR2`. |
| `body.concept` | String | Sí | Catálogo distinto según operatoria: Referencias-mepConceptTypeD (para DL0/DL1/DL2/DR0/DR1/DR2) o Referencias-mepConceptTypeD20 (para D20) — ambos pendientes de relevar. |
| `body.origin_fund` | String | Condicional | Obligatorio para `GC1`, `GC2`, `D20`. Catálogo Referencias-originFound (pendiente). |
| `body.investment_type` | String | Condicional | Obligatorio en `GC1`, `GC2`. Catálogo Referencias-investmentType (pendiente). |

### Response — atributos principales

Estructura similar a `CrearTransferencia`/`CrearTransferenciaCVU` (`id` con prefijo `MEP-<CUIT>-<origin_id>`, `type: TRANSFER-MEP`, `from`, `counterparty`, `transaction_ids[]`, `status`, `charge.*`), con detalles propios de MEP:

| Campo | Tipo | Descripción |
|-------|------|-------------|
| `details.mep_operation` | String | Código de operatoria ejecutada. |
| `details.operation_number` | String | Número de trámite de Bind. |
| `details.bcra_operation_number` | String | Número de trámite BCRA (cuando la operación fue recibida por el BCRA). |
| `details.observation` | String | Observaciones. |
| `details.investment_type` / `details.origin_fund` | String | Ecos del request (GC1/GC2/D20). |
| `details.creditor_entity` / `details.creditor_account` | String | Entidad y cuenta destino (GC2/D20). |
| `status` | String | Catálogo Referencias-EstadoTX. Estados observados en ejemplos: `COMPLETED`, `IN_PROGRESS`, `FAILED`. |
| `operation_date` | String (ISO) | No se informa si hubo problemas de comunicación junto con estado `UNKNOWN`. |

### Códigos de error

| HTTP | Código | Descripción |
|------|--------|-------------|
| 503 | `GE503` | Estado de las redes no permite ejecutar la transferencia. |
| 409 | `GE500` | Error general. |
| 409 | `TX003`/`TX004` | Monto / moneda no indicados. |
| 409 | `TX008` | CBU/CVU incorrecto. |
| 409 | `TX010` | Debe indicar el concepto. |
| 409 | `TX012` | Moneda inválida. |
| 409 | `TX086` | Debe indicar el código de operatoria MEP. |
| 409 | `PA004` | CUIT inválido. |

## 2. Obtener transferencia — `ObtenerTransferenciaMEP`

> Fuente: https://sandbox.bind.com.ar/apidoc/#api-TransferenciaMEP-ObtenerTransferenciaMEP

Proporciona el detalle de una transferencia MEP específica, incluyendo el estado actual — útil para verificar si se completó con éxito.

### URL / Método

| Campo | Valor |
|-------|-------|
| Método | `GET` |
| URL | `/banks/:bank_id/accounts/:account_id/:view_id/transaction-request-types/TRANSFER-MEP/:transaction_id` |

### Códigos de error (HTTP 409, salvo GE503 que es 503)

`GE503`, `GE500`, `PA001`, `PA002`, `TX019` (transferencia inexistente), `AC002` (cuenta inválida), `GE403`.

## 3. Obtener transferencias — `ObtenerTransferenciasMEP`

> Fuente: https://sandbox.bind.com.ar/apidoc/#api-TransferenciaMEP-ObtenerTransferenciasMEP

Devuelve un listado de transferencias MEP en un período/criterio determinado.

### URL / Método

| Campo | Valor |
|-------|-------|
| Método | `GET` |
| URL | `/banks/:bank_id/accounts/:account_id/:view_id/transaction-request-types/TRANSFER-MEP` |

### Headers de filtro (opcionales)

`obp_status` (catálogo EstadoTX), `obp_limit`, `obp_offset`, `obp_from_date`, `obp_to_date`.

### Response

Array del mismo contrato que un elemento individual, más el header `obp_total_items` (cantidad total, para paginación).

### Códigos de error

`GE503`, `GE500`, `PA001`, `PA002`, `GE403`, `AC002`, `FI003`–`FI007` (filtros de paginación/fechas inválidos).

## Nota de relevamiento

Grupo completo (3/3 endpoints relevados) desde `https://sandbox.bind.com.ar/apidoc/api_data.json`. Varios catálogos referenciados (`mepConceptTypeD`, `mepConceptTypeD20`, `originFound`, `investmentType`, `operationCode`, `EstadoTX`) pertenecen al grupo `Referencias`, fuera del alcance de esta ronda de relevamiento.

> Capturado por Pablo Gomes, 2026-09-01.

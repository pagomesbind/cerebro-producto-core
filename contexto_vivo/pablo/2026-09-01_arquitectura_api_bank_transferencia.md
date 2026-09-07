---
id: 2026-09-01_arquitectura_api_bank_transferencia
pm: pablo
fecha_captura: 2026-09-01
fuente: "Portal público de developers API BANK — https://sandbox.bind.com.ar/apidoc/#api-Transferencia"
producto: transversal
tema: API BANK (Banco Industrial) — Transferencia — referencia de endpoints
tipo: conocimiento
destino_propuesto: 3_recursos/arquitectura_sistema/api_bank/transferencia.md
tipo_destino: crear
contradice: "no"
confianza: alta
estado: en_cola
merge_commit:
---

## Contexto

Grupo **Transferencia** de API BANK: transferencias salientes desde una cuenta "normal" del banco (no específicamente desde un CVU de billetera virtual — para eso está el grupo `Billetera` / `TRANSFER-CVU`, ver item separado `2026-09-01_arquitectura_api_bank_billetera`). Header `Authorization: JWT :token` obligatorio en todos. `bank_id` siempre `322`, `view_id` siempre `"owner"`.

---

## 1. Realizar transferencia — `CrearTransferencia`

> Fuente: https://sandbox.bind.com.ar/apidoc/#api-Transferencia-CrearTransferencia

Realiza una transferencia por identificador de beneficiario, CBU, CVU o alias. Comparte casi todo el contrato con `CrearTransferenciaCVU` del grupo Billetera, salvo que **no** lleva `origin_debit` (no hay CVU de origen — se debita de la cuenta indicada por `account_id` directamente).

### URL / Método

| Campo | Valor |
|-------|-------|
| Método | `POST` |
| URL | `/banks/:bank_id/accounts/:account_id/:view_id/transaction-request-types/TRANSFER/transaction-requests` |

### Parámetros del request

| Parámetro | Tipo | Obligatorio | Descripción |
|-----------|------|-------------|-------------|
| `bank_id`, `account_id` (cuenta origen), `view_id` | — | Sí | Estándar. |
| `body.origin_id` | String | Sí | Id único de transacción, máx. 15 caracteres. Reenviarlo devuelve la info de la transacción existente (idempotencia). |
| `body.to.cbu` | String | No* | CBU o CVU del destinatario. |
| `body.to.label` | String | No* | Alias del destinatario. |
| `body.to.cuit` | String | No | CUIT del destinatario (recomendado). |
| `body.value.currency` | String | Sí | Catálogo Referencias-Currency (pendiente de relevar). |
| `body.value.amount` | Number | Sí | Importe. |
| `body.description` | String | No (default `Varios`) | Máximo 100 caracteres. |
| `body.concept` | String | Sí (default `VAR`) | Catálogo Referencias-ConceptoTX (pendiente de relevar). |
| `body.emails` | String[] | Sí | Emails para comprobante. |

*Debe completarse `to.cbu` o `to.label`.

### Response — atributos principales

Igual estructura que `CrearTransferenciaCVU` (id con prefijo `1`/`AT`/`WP`, `type: TRANSFER`, `from`, `counterparty`, `details.origin_id`, `details.warnings[]`, `transaction_ids[]`, `status`, `status_description`, `start_date`, `end_date`, `charge.summary`, `charge.value.currency`/`.amount`) — sin `origin_debit` ni `business_date` explícitos en todos los ejemplos.

Estados observados en los ejemplos del portal: `COMPLETED` (por LINK/RED INTERNA/desacoplada entre PSP de confianza) e `IN_PROGRESS` (transferencia CBU→CVU por Coelsa, "a confirmar").

### Códigos de error

| HTTP | Código | Descripción |
|------|--------|-------------|
| 503 | `GE503` | Estado de las redes no permite ejecutar la transferencia. |
| 409 | `GE500`/`GE013`/`GE403` | Generales / email inválido / permisos. |
| 409 | `PA001`/`PA002` | Banco / vista inválidos en URL. |
| 409 | `TX001`–`TX012` | Validaciones de datos de destino/monto/moneda/concepto (mismo set que `CrearTransferenciaCVU`). |
| 409 | `TX033`/`TX035` | Id > 15 caracteres / descripción > 100 caracteres. |
| 409 | `TX042` | El CBU/CVU o alias indicado se encuentra inhabilitado. |
| 409 | `TX046` | Monto excede el límite diario disponible para la cuenta origen. |
| 409 | `TX500` | Error genérico de transferencia (mensaje variable). |

---

## 2. Eliminar pedido de transferencia — `EliminarPedidoDeTransferencia`

> Fuente: https://sandbox.bind.com.ar/apidoc/#api-Transferencia-EliminarPedidoDeTransferencia

Permite eliminar un pedido de transferencia **en estado `PENDING`** (pendiente de firma/aprobación — no aplica a transferencias ya cursadas).

### URL / Método

| Campo | Valor |
|-------|-------|
| Método | `DELETE` |
| URL | `/banks/:bank_id/accounts/:account_id/:view_id/transaction-request-types/TRANSFER/:transaction_id` |

### Parámetros

| Parámetro | Tipo | Obligatorio | Descripción |
|-----------|------|-------------|-------------|
| `transaction_id` | String | Sí | Identificador de la transacción. |
| `bank_id`, `account_id`, `view_id` | — | Sí | Estándar. |

### Response

Solo devuelve el header `process` (identificador del proceso), sin body documentado con más detalle.

---

## 3. Obtener transferencias — `ObtenerPedidosTransferencias`

> Fuente: https://sandbox.bind.com.ar/apidoc/#api-Transferencia-ObtenerPedidosTransferencias

Obtiene un listado de transferencias realizadas desde o hacia las cuentas del cliente.

### URL / Método

| Campo | Valor |
|-------|-------|
| Método | `GET` |
| URL | `/banks/:bank_id/accounts/:account_id/:view_id/transaction-request-types/TRANSFER` |

### Headers de filtro (opcionales)

`obp_status` (catálogo Referencias-EstadoTX), `obp_limit`, `obp_offset`, `obp_from_date`, `obp_to_date`, `obp_origin` (catálogo Referencias-OriginTX) — mismo patrón que el resto de los listados de la API.

### Response

Array con el mismo contrato de item que `CrearTransferencia` (sin `origin_debit`), más `details.type` indicando `TRANSFERENCIAS_ENVIADAS` o `TRANSFERENCIAS_RECIBIDAS`.

### Ejemplo destacado — transferencia fallida por timeout

```json
{
  "status": "FAILED",
  "status_description": "La operación se rechazó porque se agotó el tiempo configurado para su resolución"
}
```

Este es un motivo de `FAILED` explícito documentado por el portal (timeout de resolución) — útil para troubleshooting de reclamos de clientes sobre transferencias fallidas.

---

## 4. Obtener transferencia — `ObtenerPedidoTransferencia`

> Fuente: https://sandbox.bind.com.ar/apidoc/#api-Transferencia-ObtenerPedidoTransferencia

Obtiene el detalle de una transferencia en particular, por `transaction_id` (el generado por el cliente o el devuelto al crear la transferencia).

### URL / Método

| Campo | Valor |
|-------|-------|
| Método | `GET` |
| URL | `/banks/:bank_id/accounts/:account_id/:view_id/transaction-request-types/TRANSFER/:transaction_id` |

### Response

Mismo contrato que un elemento del listado (punto 3), agregando `details.label` (alias del destinatario) y `details.cbu` (CBU del destinatario) cuando corresponde.

### Códigos de error

| Código | Descripción |
|--------|-------------|
| `PA002` | Vista inválida en URL. |
| `GE403` | Error de permisos. |
| `TX019` | Transferencia inexistente. |

---

## Nota de relevamiento

Grupo completo (4/4 endpoints relevados) desde `https://sandbox.bind.com.ar/apidoc/api_data.json`. Igual que en `Billetera`, varios campos referencian catálogos del grupo `Referencias` (pendiente de relevar, ver nota en el índice de `contexto_vivo/`).

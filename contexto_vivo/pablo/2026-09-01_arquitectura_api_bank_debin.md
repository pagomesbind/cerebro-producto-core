---
id: 2026-09-01_arquitectura_api_bank_debin
pm: pablo
fecha_captura: 2026-09-01
fuente: "Portal público de developers API BANK — https://sandbox.bind.com.ar/apidoc/#api-Debin"
producto: transversal
tema: API BANK (Banco Industrial) — DEBIN — referencia de endpoints
tipo: conocimiento
destino_propuesto: 3_recursos/arquitectura_sistema/api_bank/debin.md
tipo_destino: crear
contradice: "no"
confianza: alta
estado: ingestado
merge_commit:
---

## Contexto

Grupo **Debin** de API BANK: Débito Inmediato (DEBIN), mecanismo por el cual un vendedor solicita el cobro de un importe a un comprador, que debe confirmarlo (o tiene una recurrencia preautorizada). Relevante para el dominio de cobros de Agente de Cobros y Pagos de Bind. Header `Authorization: JWT :token` obligatorio en todos. `bank_id` siempre `322`, `view_id` siempre `"owner"`.

---

## 1. Alta/Baja de Cuenta Vendedor — `Alta_BajaCuentaVendedor`

> Fuente: https://sandbox.bind.com.ar/apidoc/#api-Debin-Alta_BajaCuentaVendedor

Adhiere o desadhiere una cuenta como vendedora de DEBIN — habilita/deshabilita la posibilidad de generar DEBINes desde esa cuenta.

### URL / Método

| Campo | Valor |
|-------|-------|
| Método | `PUT` |
| URL | `/banks/:bank_id/accounts/:account_id/:view_id/transaction-request-types/DEBIN` |

### Parámetros

| Parámetro | Tipo | Obligatorio | Descripción |
|-----------|------|-------------|-------------|
| `bank_id`, `account_id`, `view_id` | — | Sí | Estándar. |
| `body.enabled` | Boolean | Sí | Habilita o deshabilita la cuenta vendedora (los ejemplos del portal usan `adhered`, aparente inconsistencia de nombre entre la doc de parámetro y el ejemplo). |

### Response

| Campo | Tipo | Descripción |
|-------|------|-------------|
| `process` (header) | String | Identificador del proceso. |
| `adhered` | Boolean | Estado de la cuenta. |
| `accountId` | String | Identificador de la cuenta. |

### Ejemplo de response

```json
{ "adhered": true, "account_id": "20-1-4636-1-5" }
```

---

## 2. Consulta datos vendedor — `ConsultaVendedor`

> Fuente: https://sandbox.bind.com.ar/apidoc/#api-Debin-ConsultaVendedor

**Nota de relevamiento:** la descripción y el detalle de response de este endpoint vienen vacíos en el JSON fuente del portal (`api_data.json`) — solo se documentan headers, parámetros de URL y el header `process` en la respuesta.

### URL / Método

| Campo | Valor |
|-------|-------|
| Método | `GET` |
| URL | `/banks/:bank_id/accounts/:account_id/:view_id/transaction-request-types/DEBIN/info` |

### Parámetros

| Parámetro | Tipo | Obligatorio | Descripción |
|-----------|------|-------------|-------------|
| `bank_id` | Number | Sí | `322`. |
| `account_id` | String | Sí | Cuenta destino (crédito) de la operación. |
| `view_id` | String | Sí | `"owner"`. |

---

## 3. Crear pedido DEBIN — `CrearDEBIN`

> Fuente: https://sandbox.bind.com.ar/apidoc/#api-Debin-CrearDEBIN

### URL / Método

| Campo | Valor |
|-------|-------|
| Método | `POST` |
| URL | `/banks/:bank_id/accounts/:account_id/:view_id/transaction-request-types/DEBIN/transaction-requests` |

### Parámetros del request

| Parámetro | Tipo | Obligatorio | Descripción |
|-----------|------|-------------|-------------|
| `bank_id`, `account_id` (cuenta destino/crédito), `view_id` | — | Sí | Estándar. |
| `body.origin_id` | String | Sí | Id único, máx. 15 caracteres, idempotente. |
| `body.to.label` | String | Condicional | Alias del comprador — obligatorio si no se envía CBU/CVU. |
| `body.to.cbu` | String | Condicional | CBU o CVU del comprador — obligatorio si no se envía alias. |
| `body.value.currency` | String | Sí | Catálogo Referencias-Currency (pendiente). |
| `body.value.amount` | Number | Sí | Importe. |
| `body.concept` | String | Sí (default `VAR`) | Catálogo Referencias-ConceptoTX (pendiente). |
| `body.description` | String | No | Máximo 100 caracteres. |
| `body.provision` | String | No | Nombre de la prestación configurada en la adhesión de recurrencia — permite cobrar una prestación usando DEBIN cuando el comprador preaprobó la recurrencia. |
| `body.expiration` | Number | Sí | Minutos desde la creación hasta que expira el pedido; valor máximo `4320` (3 días). |

### Response — atributos principales

| Campo | Tipo | Descripción |
|-------|------|-------------|
| `id` | String | Identificador de la transacción. |
| `type` | String | Default `DEBIN`. |
| `from.bank_id` / `from.account_id` | String | Cuenta origen (del vendedor/cobrador). |
| `details.origin_id` | String | Eco del request. |
| `details.warnings[]` | String[] | Ej. `TRANSACTION_ALREADY_CREATED`. |
| `details.buyer.cuit` / `.alias` / `.cbu` / `.name` / `.bank_code` / `.bank_description` | — | Datos del comprador. |
| `transaction_ids[]` | String[] | IDs internos. |
| `status` | String | Catálogo Referencias-EstadoTX. |
| `status_description` | String | **Acá se devuelve el estado propio del DEBIN** — catálogo Referencias-EstadoDEBIN (distinto del `status` genérico de transacción). |
| `charge.summary` / `charge.value.currency` / `.amount` | — | Cargo. |

### Ejemplo de response

```json
{
  "id": "JMRD06ZO9WX5Z125GP7XY3",
  "type": "DEBIN",
  "from": { "bank_id": "322", "account_id": "21-1-99999-4-6" },
  "details": {
    "origin_id": "556677",
    "buyer": { "cuit": "20312528046", "alias": "alias", "cbu": null, "name": "Alejandro M.", "bank_code": "322", "bank_description": "BANCO INDUSTRIAL S.A." }
  },
  "transaction_ids": ["7-30714423033-000000000123667-1"],
  "status": "PENDING",
  "status_description": "AWAITING_CONFIRMATION",
  "start_date": "2018-04-12T18:53:29.269Z",
  "end_date": "2018-04-12T18:53:29.269Z",
  "challenge": null,
  "charge": { "summary": "VAR", "value": { "currency": "ARS", "amount": 10 } }
}
```

**Estado clave a resaltar:** `status_description: "AWAITING_CONFIRMATION"` con `status: "PENDING"` indica que el DEBIN quedó a la espera de que el comprador lo confirme (o rechace).

### Códigos de error (HTTP 409)

`GE403`, `GE500`, `PA001`, `PA002`, `TX002`–`TX004` (monto/moneda faltante), `TX008`/`TX009` (CBU/CVU o alias inválido), `TX010`/`TX011`/`TX012` (concepto/monto/moneda), `TX016` (falta CBU/CVU o alias destino), `TX017` (no pueden enviarse ambos), `TX022` (la cuenta destinataria no está habilitada para recibir DEBIN — ver endpoint `Alta_BajaCuentaVendedor`), `TX033`/`TX035` (id/descripción exceden longitud), `TX500` (error genérico).

---

## 4. Crear, actualizar o dar de baja pedido de recurrencia de DEBIN — `CrearSuscripcionDEBIN`

> Fuente: https://sandbox.bind.com.ar/apidoc/#api-Debin-CrearSuscripcionDEBIN

Permite crear, actualizar o dar de baja una recurrencia (preautorización) para un comprador. **Se debe solicitar al Banco el alta de los nombres de las prestaciones antes de poder adherirlas.**

### URL / Método

| Campo | Valor |
|-------|-------|
| Método | `POST` |
| URL | `/banks/:bank_id/:view_id/transaction-request-types/DEBIN-SUBSCRIPTION/transaction-requests` |

Nota: a diferencia del resto del grupo, esta URL **no lleva `account_id`** en el path.

### Parámetros del request

| Parámetro | Tipo | Obligatorio | Descripción |
|-----------|------|-------------|-------------|
| `bank_id`, `view_id` | — | Sí | Estándar. |
| `body.id` | String | No | Id de la recurrencia. `0`/`null` para crear una nueva; el id existente para actualizar o dar de baja. |
| `body.to.cuit` | String | Sí | CUIT del comprador. |
| `body.to.cbu` | String | Sí | CBU o CVU del comprador. |
| `body.value.currency` | String | Sí | Catálogo Referencias-Currency (pendiente). |
| `body.description` | String | No | Descripción enviada al comprador. |
| `body.concept` | String | Sí (default `VAR`) | Catálogo Referencias-ConceptoTX (pendiente). |
| `body.provision` | String | Sí | Nombre de la prestación provista por el Banco (debe existir previamente). |
| `body.provision_reference` | String | Sí | Valor de referencia asociado al servicio — típicamente identifica al comprador en particular. |
| `body.active` | Boolean | No (default `true`) | `true` = alta, `false` = baja de la preautorización existente. |

### Response — atributos principales

`id` (usar para actualizar la recurrencia), `type: DEBIN_SUBSCRIPTION`, `details.value`, `details.origin_id`, `details.warnings[]`, `details.description`, `details.concept`, `details.provision`, `details.provision_reference`, `details.buyer.alias`/`.cbu`/`.cuit`/`.name`, `transaction_ids[]`, `status`, `status_description` (ej. `"RECURRENCIA ADHERIDA"` / `"RECURRENCIA DESADHERIDA"`), `start_date`/`end_date`, `charge.summary`/`.currency`, `details.active`.

### Códigos de error (HTTP 409)

`GE500`, `PA001`, `PA002`, `PA004` (CUIT inválido), `GE403`, `TX004`/`TX008`/`TX009`/`TX010`/`TX012`/`TX013` (validaciones de datos), `TX016` (falta CBU/CVU o alias), `TX021` (origen inválido), `TX022` (cuenta no habilitada para DEBIN), `TX023`/`TX024`/`TX025` (falta prestación / referencia / descripción), `TX026` (la prestación indicada no existe — verificar el nombre con el Banco), `TX032` (suscripción de DEBIN no encontrada — al intentar actualizar/dar de baja una inexistente), `TX033` (id > 15 caracteres), `TX500` (genérico).

---

## 5. Eliminar pedido de DEBIN — `EliminarPedidoDeDebin`

> Fuente: https://sandbox.bind.com.ar/apidoc/#api-Debin-EliminarPedidoDeDebin

Permite eliminar un pedido de DEBIN **en estado `AWAITING_CONFIRMATION`** (aún no confirmado por el comprador).

### URL / Método

| Campo | Valor |
|-------|-------|
| Método | `DELETE` |
| URL | `/banks/:bank_id/accounts/:account_id/:view_id/transaction-request-types/DEBIN/:transaction_id` |

### Response

```json
{ "id": "FAWREWRDAESTOESUNAPRUEBASFAFAWREW" }
```

---

## 6. Obtener DEBIN — `ObtenerPedidoDebin`

> Fuente: https://sandbox.bind.com.ar/apidoc/#api-Debin-ObtenerPedidoDebin

Obtiene el detalle de un DEBIN por `transaction_id`.

### URL / Método

| Campo | Valor |
|-------|-------|
| Método | `GET` |
| URL | `/banks/:bank_id/accounts/:account_id/:view_id/transaction-request-types/DEBIN/:transaction_id` |

### Response — atributos adicionales relevantes

| Campo | Tipo | Descripción |
|-------|------|-------------|
| `details.preauthorized` | Boolean | Si el DEBIN es preautorizado (viene de una recurrencia) o no. |
| `details.sellerCuit` / `.sellerAccountLabel` / `.sellerAccountCBU` | — | Datos del vendedor. |
| `details.buyerAccountCBU` / `.buyerAccountLabel` / `.buyerCuit` | — | Datos del comprador. |
| `status` | String | Catálogo Referencias-EstadoDEBIN (nota: en este endpoint, a diferencia de `CrearDEBIN`, el catálogo de `status` referenciado es directamente `EstadoDEBIN`, no `EstadoTX`). |

### Códigos de error (HTTP 409)

`PA002`, `PA007` (tipo de transacción inválida), `GE403`, `TX018` (DEBIN no encontrado), `TX019` (transferencia inexistente).

---

## 7. Obtener DEBINES para cobrar — `ObtenerPedidosDebin`

> Fuente: https://sandbox.bind.com.ar/apidoc/#api-Debin-ObtenerPedidosDebin

Lista los DEBINes asociados a la cuenta.

### URL / Método

| Campo | Valor |
|-------|-------|
| Método | `GET` |
| URL | `/banks/:bank_id/accounts/:account_id/:view_id/transaction-request-types/DEBIN` |

### Headers de filtro (opcionales)

`obp_status` (catálogo Referencias-EstadoDEBIN), `obp_limit`, `obp_offset`, `obp_from_date`, `obp_to_date`.

### Response

Array con el mismo contrato de item que `ObtenerPedidoDebin`.

---

## Nota de relevamiento

Grupo completo (7/7 endpoints relevados) desde `https://sandbox.bind.com.ar/apidoc/api_data.json`. El endpoint `ConsultaVendedor` viene con descripción y detalle de response vacíos en la fuente — no es un límite de nuestro relevamiento, es así en el portal. Catálogos referenciados (`Currency`, `ConceptoTX`, `EstadoTX`, `EstadoDEBIN`, `OperationType`) pertenecen al grupo `Referencias`, fuera del alcance de esta ronda.

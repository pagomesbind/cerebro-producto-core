---
id: 2026-09-01_arquitectura_api_bank_cuenta
pm: pablo
fecha_captura: 2026-09-01
fuente: "Portal público de developers API BANK — https://sandbox.bind.com.ar/apidoc/#api-Cuenta"
producto: transversal
tema: API BANK (Banco Industrial) — Cuenta — referencia de endpoints
tipo: conocimiento
destino_propuesto: 3_recursos/arquitectura_sistema/api_bank/cuenta.md
tipo_destino: crear
contradice: "no"
confianza: alta
estado: en_cola
merge_commit:
---

## Qué es API BANK y por qué importa

API BANK es la API pública de Banco Industrial (documentada en `https://sandbox.bind.com.ar/apidoc/`, con formato apidoc.js) que Bind PSP consume internamente para operar cuentas y CVU — es la base técnica que sustenta tanto el producto **Wallet** como **Agente de Cobros y Pagos** de Bind (ambos usan Banco Industrial como banco sponsor/custodio de las cuentas CBU/CVU). Este documento releva el grupo **Cuenta**, que expone consulta y gestión de cuentas y sus alias CBU.

Toda la API requiere el header `Authorization: JWT :token` (ver grupo Autenticación, item separado `2026-09-01_arquitectura_api_bank_autenticacion`) salvo que se indique lo contrario. Las URLs de abajo son relativas a la base `@@REST_API_URL@@REST_API_VERSION` (placeholder del portal, resuelto por ambiente — sandbox vs. producción).

---

## 1. Consulta cuenta por CBU ó CVU — `ConsultaCuentaCBU`

> Fuente: https://sandbox.bind.com.ar/apidoc/#api-Cuenta-ConsultaCuentaCBU

Obtiene información de una cuenta mediante el CBU o CVU asociado a la misma. **Este es el endpoint que replica hacia afuera Bind Wallet en su propia API pública** (`consultar-cbu-cvu-por-cbu-cvu-o-alias`, ver `wiki/3_recursos/detalle_productos/wallet/apis_expuestas/cvu/endpoint_get_consultar_por_cbu_cvu_alias.md`), aunque con un contrato de datos distinto (Bind agrega campos propios como `cuentaId`, `billeteraId`, `bancoNombre`).

### URL / Método

| Campo | Valor |
|-------|-------|
| Método | `GET` |
| URL | `/accounts/cbu/:cbu_cvu` |

### Headers

| Header | Tipo | Obligatorio | Descripción |
|--------|------|-------------|-------------|
| `Authorization` | String | Sí | Formato `"JWT :token"` — reemplazar `:token` con el token de autenticación. |

### Parámetros del request

| Parámetro | Tipo | Obligatorio | Descripción |
|-----------|------|-------------|-------------|
| `cbu_cvu` | String | Sí | CBU ó CVU de la cuenta a consultar (path param). |

Ejemplos: CBU válido `3220001801000020816200`, CVU válido `0000033802019012400010`, CBU inválido (mal formado) `1234567890123456789012`.

### Response — atributos

| Campo | Tipo | Descripción |
|-------|------|-------------|
| `process` (header) | String | Identificador del proceso. |
| `owners` | Object[] | Integrantes de la cuenta. |
| `owners.id_type` | String | Tipo de identificador. |
| `owners.id` | String | Identificador de la persona. |
| `owners.display_name` | String | Nombre / Razón social. |
| `owners.is_physical_person` | Boolean | Es persona física. |
| `type` | String | Tipo de cuenta. |
| `is_active` | Boolean | Cuenta activa. |
| `currency` | String | Código de moneda — valores posibles en grupo Referencias-Currency (pendiente de relevar). |
| `label` | String | Alias de CBU ó CVU. |
| `account_routing` | Object | Información de la cuenta. |
| `account_routing.scheme` | String | Tipo de dato (ej. `CBU`). |
| `account_routing.address` | String | Valor (el CBU/CVU en sí). |
| `bank_routing` | Object | Información del banco. |
| `bank_routing.scheme` | String | Tipo de dato (ej. `NAME`). |
| `bank_routing.address` | String | Nombre del banco. |
| `bank_routing.code` | String | Código de banco. |

### Ejemplo de response — "Detalle de una cuenta"

```json
{
   "owners": [
       {
           "id": "20203385072",
           "display_name": "Parker, Peter",
           "id_type": "CUIT",
           "is_physical_person": true
       }
   ],
   "type": "CC",
   "is_active": true,
   "currency": "ARS",
   "label": "desdas",
   "account_routing": {
       "scheme": "CBU",
       "address": "3220001823001077580012"
   },
   "bank_routing": {
       "scheme": "NAME",
       "address": "BANCO INDUSTRIAL S.A.",
       "code": "322"
   }
}
```

### Códigos de error (HTTP 409, con `code` propio en el body)

| Código | Descripción |
|--------|-------------|
| `GE500` | Error general. |
| `GE403` | Error de permisos. |
| `PA005` | CBU inválido. |

---

## 2. Consulta cuenta por Alias — `ConsultaCuentaAlias`

> Fuente: https://sandbox.bind.com.ar/apidoc/#api-Cuenta-ConsultaCuentaAlias

Obtiene información de una cuenta mediante el alias asociado a la misma. Mismo contrato de response que `ConsultaCuentaCBU` (ver arriba).

### URL / Método

| Campo | Valor |
|-------|-------|
| Método | `GET` |
| URL | `/accounts/alias/:alias` |

### Headers

Mismo `Authorization: JWT :token` obligatorio.

### Parámetros del request

| Parámetro | Tipo | Obligatorio | Descripción |
|-----------|------|-------------|-------------|
| `alias` | String | Sí | Alias de la cuenta a consultar (path param). |

Ejemplos: alias válido `aliasDeCbuValido`, alias inválido `buquedaConAliasDeCbuInvalido`.

### Response — atributos

Idéntico contrato a `ConsultaCuentaCBU`: `process` (header), `owners[]` (`id_type`, `id`, `display_name`, `is_physical_person`), `type`, `is_active`, `currency`, `label`, `account_routing` (`scheme`, `address`), `bank_routing` (`scheme`, `address`, `code`).

### Códigos de error (HTTP 409)

| Código | Descripción |
|--------|-------------|
| `GE500` | Error general. |
| `GE403` | Error de permisos. |
| `PA006` | Alias de CBU/CVU inválido. |
| `PA011` | Alias de CBU/CVU inexistente. |

---

## 3. Asignar/Modificar Alias CBU — `AsignarAliasCBU`

> Fuente: https://sandbox.bind.com.ar/apidoc/#api-Cuenta-AsignarAliasCBU

Crea o modifica un alias para un CBU existente asociado a una cuenta y vista específica.

### URL / Método

| Campo | Valor |
|-------|-------|
| Método | `POST` |
| URL | `/banks/:bank_id/accounts/:accountId/:viewId/alias` |

### Parámetros del request

| Parámetro | Tipo | Obligatorio | Descripción |
|-----------|------|-------------|-------------|
| `bank_id` | Number | Sí | Código de identificación de la entidad. Valor permitido: `322` (Banco Industrial). |
| `accountId` | String | Sí | Identificador de la cuenta. |
| `viewId` | String | Sí | Identificador de la vista asociada a la cuenta. |
| `body.cuit` | String | Sí | CUIT del cliente de la billetera virtual (solo números, sin guiones). |
| `body.cbu` | String | Sí | CBU del cliente. |
| `body.label` | String | Sí | Alias que se asignará. |
| `body.old_label` | String | No | Alias actual del CBU (para reemplazo). |

### Ejemplo de body

```json
{
  "cuit": "27299069635",
  "cbu": "3220001805000016740012",
  "label": "VANESA.NOVO",
  "old_label": "PERRO.ANANA.CEDRO"
}
```

### Response

| Campo | Tipo | Descripción |
|-------|------|-------------|
| `status` | String | Resultado de la operación (`"OK"`). |

### Códigos de error (HTTP 409)

| Código | Descripción |
|--------|-------------|
| `GE500` | Error general. |
| `GE403` | Error de permisos. |
| `GE003` | Campo requerido con valor nulo. |
| `PA005` | CBU inválido. |
| `TX009` | El Alias de CBU/CVU no es correcto (formato). |
| `AC003` | El CBU ya tiene asignado ese Alias de CBU. |
| `AC005` | El Alias de CBU ya se encuentra en uso. |
| `AC006` | El Alias de CBU no puede modificarse más de una vez — debe esperar 24 horas para volver a hacerlo. |

**Regla de negocio a resaltar:** el alias de un CBU solo puede modificarse una vez cada 24 horas (`AC006`). Es un dato operativo importante si algún flujo interno de Bind necesita re-asignar alias en cadena.

---

## 4. Consulta de cuentas — `ConsultaCuentas`

> Fuente: https://sandbox.bind.com.ar/apidoc/#api-Cuenta-ConsultaCuentas

Retorna el listado de cuentas asociadas a la vista/banco indicados (típicamente, todas las cuentas que el cliente API tiene habilitadas para operar).

### URL / Método

| Campo | Valor |
|-------|-------|
| Método | `GET` |
| URL | `/banks/:bank_id/accounts/:view_id` |

### Parámetros del request

| Parámetro | Tipo | Obligatorio | Descripción |
|-----------|------|-------------|-------------|
| `bank_id` | Number | Sí | Código de identificación de la entidad. Valor permitido: `322`. |
| `view_id` | String | Sí | Código de identificación de la vista. Valor permitido: `"owner"`. |

### Response — atributos (listado)

| Campo | Tipo | Descripción |
|-------|------|-------------|
| `process` (header) | String | Identificador del proceso. |
| `id` | String | Identificador de la cuenta. |
| `label` | String | Alias de la cuenta. |
| `number` | String | Número de cuenta. |
| `type` | String | Tipo de cuenta. |
| `status` | String | Estado. |
| `owners[]` | Object | Integrantes de cuenta — `id`, `id_type` (`1`-CUIT / `2`-CUIL / `3`-CDI), `is_physical_person`, `display_name`. |
| `balance` | Object | Saldo disponible — `currency`, `amount`. |
| `bank_id` | String | Código de banco. |
| `account_routing` | Object | `scheme`, `address`. |

### Ejemplo de response

```json
[
   {
       "id": "21-1-99999-4-6",
       "label": "PruebaaliasBruno",
       "number": "99999",
       "type": "Caja de Ahorro",
       "status": "NORMAL",
       "owners": [
           {
               "id": "27876543212",
               "display_name": "COORPORACION CAPSULA",
               "id_type": "1",
               "is_physical_person": true
           }
       ],
       "balance": { "currency": "2", "amount": 197801 },
       "bank_id": "322",
       "account_routing": { "scheme": "CBU", "address": "3220001822000055910031" }
   }
]
```

### Códigos de error (HTTP 409)

| Código | Descripción |
|--------|-------------|
| `GE500` | Error general. |
| `PA001` | Código de banco enviado por parámetro en la url inválido. |
| `PA002` | Código de vista enviado por parámetro en la url inválido. |
| `GE403` | Error de permisos. |

---

## 5. Consulta de movimientos — `ConsultaDeMovimientos`

> Fuente: https://sandbox.bind.com.ar/apidoc/#api-Cuenta-ConsultaDeMovimientos

Retorna el listado de movimientos de una cuenta, con filtros por header (paginación, fechas, categorías).

### URL / Método

| Campo | Valor |
|-------|-------|
| Método | `GET` |
| URL | `/banks/:bank_id/accounts/:account_id/:view_id/transactions` |

### Parámetros del request

| Parámetro | Tipo | Obligatorio | Descripción |
|-----------|------|-------------|-------------|
| `bank_id` | Number | Sí | Código de la entidad. Valor permitido: `322`. |
| `account_id` | String | Sí | Código de cuenta, formato `XX-X-XXXX-X-X` (se obtiene de `ConsultaCuentas`). |
| `view_id` | String | Sí | Código de vista. Valor permitido: `"owner"`. |

### Headers de filtro (opcionales, salvo Authorization)

| Header | Tipo | Descripción |
|--------|------|-------------|
| `obp_sort_direction` | String | Valor permitido: `DESC`. |
| `obp_limit` | Number | Tamaño de página. |
| `obp_offset` | Number | Número de página (acepta `0` pero se comporta como `1`). |
| `obp_from_date` | String | Fecha desde, ISO (`2017-01-01`). |
| `obp_to_date` | String | Fecha hasta, ISO. |
| `obp_categories` | String | Categorías de movimiento, separadas por espacio o coma — catálogo en grupo Referencias-CategoryMov (pendiente de relevar). |

### Response — atributos principales

| Campo | Tipo | Descripción |
|-------|------|-------------|
| `process`, `obp_total_items` (headers) | String / Number | Proceso y cantidad total de movimientos (para paginación). |
| `id` | String | Identificador de movimiento. |
| `counterparty.*` | Object | Cuenta del tercero (`id`, `id_type`, `name`, `bank_routing.*`, `account_routing.*`) — cuando no está disponible, se envía `"UNAVAILABLE"`. |
| `details.type` | String | Tipo de operación (ej. `TRANSFERENCIAS_RECIBIDAS`, `TRANSFERENCIAS_ENVIADAS`, `OTROS_CREDITOS`). |
| `details.description` | String | Descripción textual del movimiento. |
| `details.posted` / `details.completed` | String | Fecha de ejecución / fecha de acreditación. |
| `details.value.currency` / `.amount` | String / — | Importe (moneda + monto; negativo si es débito). |
| `details.motive` | String | Concepto (3 caracteres) + referencia — catálogo en grupo Referencias-ConceptoTX (pendiente de relevar). |
| `details.reference_number` | String | Número de referencia. |
| `details.new_balance.*` | Object | Saldo posterior al movimiento. |
| `metadata.tags[]` | String[] | Etiquetas del movimiento. |
| `this_account.*` | Object | Cuenta propia (id, kind, bank_routing, account_routing). |

### Ejemplos de response relevantes

El portal documenta varios ejemplos de movimiento por tipo — entre ellos, movimientos de **Crédito CVU** y **Débito CVU** (transferencias entrantes/salientes vía CVU), con `counterparty.account_routing.scheme: "CVU"` y `details.description: "Transferencia Crédito"` / `"Transferencia Débito"`. Esto es directamente relevante para la conciliación de transferencias en Agente de Cobros y Pagos y Wallet.

### Códigos de error (HTTP 409)

| Código | Descripción |
|--------|-------------|
| `GE500` | Error general. |
| `PA001` | Código de banco inválido. |
| `PA002` | Código de vista inválido. |
| `GE403` | Error de permisos. |
| `AC002` | Cuenta inválida. |
| `FI002` – `FI007` | Valores de filtro inválidos (`sort_direction`, `limit`, `offset`, `from_date`, `to_date`, o `to_date` menor a `from_date`). |

---

## Nota de relevamiento

Grupo completo (5/5 endpoints relevados) desde `https://sandbox.bind.com.ar/apidoc/api_data.json` — fuente JSON embebida del portal apidoc.js, no HTML parseado a mano. Varios campos de `Response` referencian catálogos de otros grupos del mismo portal (`Referencias-Currency`, `Referencias-CategoryMov`, `Referencias-ConceptoTX`) — ese grupo (`Referencias`, 31 endpoints tipo catálogo) quedó fuera del alcance de esta ronda de relevamiento, ver nota de pendientes en el índice de `contexto_vivo/`.

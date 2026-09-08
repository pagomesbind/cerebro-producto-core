---
id: 2026-09-01_arquitectura_api_bank_billetera
pm: pablo
fecha_captura: 2026-09-01
fuente: "Portal público de developers API BANK — https://sandbox.bind.com.ar/apidoc/#api-Billetera"
producto: transversal
tema: API BANK (Banco Industrial) — Billetera (CVU) — referencia de endpoints
tipo: conocimiento
destino_propuesto: 3_recursos/arquitectura_sistema/api_bank/billetera.md
tipo_destino: crear
contradice: "no"
confianza: alta
estado: ingestado
merge_commit: d783db8
---

## Contexto

Grupo **Billetera** de API BANK (Banco Industrial): alta/baja/modificación de CVU, asignación de alias de CVU, y transferencias salientes desde un CVU. Es el grupo más directamente relevante para Wallet y Agente de Cobros y Pagos de Bind, ya que ambos productos operan CVU de sus clientes contra este banco sponsor. Header `Authorization: JWT :token` obligatorio en todos los endpoints. `bank_id` siempre `322` (Banco Industrial). `view_id` siempre `"owner"` en estos endpoints (no delegado).

---

## 1. Alta CVU cliente — `CrearCVU`

> Fuente: https://sandbox.bind.com.ar/apidoc/#api-Billetera-CrearCVU

Crea un CVU a partir del `client_id` enviado y el identificador del proveedor de billetera virtual (implícito en las credenciales del cliente API). Valida que la cuenta enviada (`account_id`) esté definida como cuenta recaudadora del proveedor y se la asigna como recaudadora del CVU.

**Comportamiento idempotente:** si el CVU ya existe para la billetera y `client_id`, devuelve `200 OK` como si se hubiera creado, con el CVU existente y `label` vacío (no se puede re-asignar alias automáticamente en ese caso). **Regla de negocio:** una vez dado de alta un CVU, el CUIT asociado no puede modificarse.

### URL / Método

| Campo | Valor |
|-------|-------|
| Método | `POST` |
| URL | `/banks/:bank_id/accounts/:account_id/:view_id/wallet/cvu` |

### Parámetros del request

| Parámetro | Tipo | Obligatorio | Descripción |
|-----------|------|-------------|-------------|
| `bank_id` | Number | Sí | `322`. |
| `account_id` | String | Sí | Cuenta recaudadora (formato `XX-X-XXXX-X-X`), dada de alta previamente para el proveedor de billetera virtual. |
| `view_id` | String | Sí | `"owner"`. |
| `body.client_id` | Number | Sí | Identificador numérico único del cliente de la billetera virtual, hasta 12 dígitos, entero sin decimales. |
| `body.cuit` | String | Sí | CUIT del cliente, solo números. |
| `body.name` | String | Sí | Nombre/denominación del cliente. Validado con regex `^[a-zA-Z0-9ñÑáéíóúÁÉÍÓÚ.\s]{5,41}$` (letras, números, ñ, vocales acentuadas, punto y espacio; 5–41 caracteres). |
| `body.currency` | String | No (default `ARS`) | Por ahora solo se acepta `ARS`. |

### Response — atributos

| Campo | Tipo | Descripción |
|-------|------|-------------|
| `process` (header) | String | Identificador del proceso. |
| `cvu` | String | Número de CVU generado. |
| `label` | String | Indica si se puede asignar alias automáticamente; si viene vacío hay que asignarlo manualmente con `AsignarAliasCVU`. |
| `reactivated` | Boolean | Indica si el CVU fue reactivado porque estaba inhabilitado. |

### Ejemplos de response

```json
{ "cvu": "0000032100000000000024", "label": "NO SE PUEDE ASIGNAR UN ALIAS AUTOMATICAMENTE, DEBERÁ HACERLO DE FORMA MANUAL", "reactivated": false }
```
CVU duplicado (idempotencia): `{ "cvu": "0000032100000000000024", "label": "", "reactivated": false }`
CVU reactivado: `{ "cvu": "0000032100000000000024", "label": "", "reactivated": true }`

### Códigos de error (HTTP 409)

| Código | Descripción |
|--------|-------------|
| `GE500` / `GE403` / `GE003` | Error general / de permisos / campo requerido nulo. |
| `PA015` | El campo titular no cumple con el formato requerido. |
| `TX012` / `TX040` | Moneda inválida / solo acepta ARS. |
| `VW001` | El id de cliente debe ser numérico y de hasta 12 dígitos. |
| `VW002` | No tiene un código de PSP asignado. |
| `VW003` | Cuenta recaudadora errónea para este proveedor PSP. |
| `VW004` | Ya existe un CVU creado para el id de cliente. |
| `VW012` | El id de cliente informado está asociado a otro CUIT. |
| `VW013` | No se pudo crear el CVU asociado al CUIT — comunicarse con el Banco. |
| `VW016` | No se pudo consultar los datos de la cuenta recaudadora. |

---

## 2. Asignar/Modificar Alias CVU — `AsignarAliasCVU`

> Fuente: https://sandbox.bind.com.ar/apidoc/#api-Billetera-AsignarAliasCVU

Crea o modifica un alias para un CVU existente. Valida que la cuenta enviada (`account_id`) sea la cuenta recaudadora del CVU.

### URL / Método

| Campo | Valor |
|-------|-------|
| Método | `POST` |
| URL | `/banks/:bank_id/accounts/:account_id/:view_id/wallet/alias` |

### Parámetros del request

| Parámetro | Tipo | Obligatorio | Descripción |
|-----------|------|-------------|-------------|
| `bank_id`, `account_id`, `view_id` | — | Sí | Igual que en `CrearCVU`. |
| `body.cuit` | String | Sí | CUIT del cliente. |
| `body.cvu` | String | Sí | CVU del cliente. |
| `body.label` | String | Sí | Alias a asignar. |

### Response

| Campo | Tipo | Descripción |
|-------|------|-------------|
| `status` | String | `"OK"`. |

### Códigos de error (HTTP 409)

| Código | Descripción |
|--------|-------------|
| `GE500` / `GE403` / `GE003` | Generales. |
| `PA012` | CVU inválido. |
| `TX009` | El alias de CBU/CVU no es correcto (formato). |
| `VW005` | El CVU enviado no es de la billetera virtual de la cuenta. |
| `VW006` | No existe CVU. |
| `VW007` | El alias ya se encuentra en uso. |
| `VW008` | No se pudo asignar alias de CVU. |
| `VW009` | CUIT erróneo para el CVU. |
| `VW010` | El CVU ya tiene asignado ese alias. |
| `VW011` | El alias no puede modificarse más de una vez — debe esperar 24 horas. |

**Misma regla que Alias CBU:** el alias de un CVU solo puede modificarse una vez cada 24 horas (`VW011`).

---

## 3. Modificar CVU cliente — `ModificarCVU`

> Fuente: https://sandbox.bind.com.ar/apidoc/#api-Billetera-ModificarCVU

Modifica un CVU existente (solo el nombre del titular; el CUIT no puede modificarse post-alta).

### URL / Método

| Campo | Valor |
|-------|-------|
| Método | `PUT` |
| URL | `/banks/:bank_id/accounts/:account_id/:view_id/wallet/cvu/:cvu` |

### Parámetros

| Parámetro | Tipo | Obligatorio | Descripción |
|-----------|------|-------------|-------------|
| `bank_id`, `account_id`, `view_id` | — | Sí | Igual que arriba. |
| `body.name` | String | No | Nuevo nombre/denominación del cliente. |

### Response

| Campo | Tipo | Descripción |
|-------|------|-------------|
| `process` (header) | String | Identificador del proceso. |
| `cvu` | String | Número de CVU. |

### Códigos de error (HTTP 409)

Comparte varios códigos con `CrearCVU`: `GE500`, `GE403`, `GE003`, `TX012`, `TX040`, `VW001`, `VW002`, `VW003`, `VW004`, `VW012`, `VW013`.

---

## 4. Baja de CVU — `EliminarCVU`

> Fuente: https://sandbox.bind.com.ar/apidoc/#api-Billetera-EliminarCVU

Elimina un CVU existente. Valida que pertenezca al CUIT informado y a la billetera. **La baja es lógica y ese CVU no puede volver a darse de alta para otro CUIT.**

### URL / Método

| Campo | Valor |
|-------|-------|
| Método | `DELETE` |
| URL | `/banks/:bank_id/accounts/:account_id/:view_id/wallet/cvu/:cvu/:cuit` |

### Parámetros

| Parámetro | Tipo | Obligatorio | Descripción |
|-----------|------|-------------|-------------|
| `cvu` | String | Sí | CVU a eliminar (path). |
| `cuit` | String | Sí | CUIT del cliente (path, solo números). |
| `bank_id`, `account_id`, `view_id` | — | Sí | Igual que arriba. |

### Response

| Campo | Tipo | Descripción |
|-------|------|-------------|
| `cvu` | String | CVU eliminado. |

### Códigos de error (HTTP 409)

| Código | Descripción |
|--------|-------------|
| `GE700` | Endpoint no habilitado. |
| `GE500` / `GE403` / `GE003` | Generales. |
| `PA004` | CUIT inválido. |
| `PA012` | CVU inválido. |
| `VW002` / `VW003` | PSP / cuenta recaudadora inválidos. |
| `VW005` | El CVU no es de la billetera de la cuenta. |
| `VW006` | No existe CVU. |
| `VW009` | CUIT erróneo para el CVU. |
| `VW014` | No se pudo eliminar el CVU — comunicarse con el Banco. |
| `VW015` | No se encontró la combinación CVU/CUIT/billetera. |

---

## 5. Realizar transferencia desde un CVU — `CrearTransferenciaCVU`

> Fuente: https://sandbox.bind.com.ar/apidoc/#api-Billetera-CrearTransferenciaCVU

Realiza una transferencia desde la cuenta de un cliente de billetera virtual hacia un CVU, CBU o Alias.

### Mecánica asincrónica — clave para entender el flujo

- Si la operación se cursa por **Coelsa** (protocolo asincrónico), una respuesta `IN_PROGRESS` significa que la solicitud fue recibida por la red, **no** que se acreditó en destino. Hay que consultar el estado con `ObtenerPedidoTransferenciaCvu` ~5 minutos después; si sigue `IN_PROGRESS`, esperar otros 5 minutos.
- Si se cursa por la **red interna del banco**, se recibe directamente el estado final (`COMPLETED` o `FAILED`).
- Respuesta `200` con `status: 'FAILED'`, o `HTTP 409`: la transferencia no se pudo cursar — el PSP debe reponer los fondos al CVU de origen si fueron retenidos.
- Respuesta `200` con `status: 'UNKNOWN'`, o `HTTP 50X`: no hubo confirmación de la red — consultar 5 minutos después (la transferencia pudo haberse cursado o no).

### URL / Método

| Campo | Valor |
|-------|-------|
| Método | `POST` |
| URL | `/banks/:bank_id/accounts/:account_id/:view_id/transaction-request-types/TRANSFER-CVU/transaction-requests` |

### Parámetros del request

| Parámetro | Tipo | Obligatorio | Descripción |
|-----------|------|-------------|-------------|
| `bank_id`, `account_id` (cuenta origen/débito), `view_id` | — | Sí | Estándar. |
| `body.origin_id` | String | Sí | Identificador unívoco de la transacción, definido por el cliente, máximo 15 caracteres. Reenviar un id existente devuelve la info de esa transacción (idempotencia). |
| `body.origin_debit.cvu` | String | Sí | CVU de origen. |
| `body.origin_debit.cuit` | String | No | CUIT de origen. |
| `body.to.cbu` | String | No* | CBU o CVU del destinatario. |
| `body.to.label` | String | No* | Alias del destinatario. |
| `body.to.cuit` | String | No | CUIT del destinatario (recomendado para validación). |
| `body.value.currency` | String | No (default `ARS`) | Solo se acepta `ARS`. |
| `body.value.amount` | Number | Sí | Importe. |
| `body.description` | String | No | Máximo 100 caracteres. |
| `body.concept` | String | Sí (default `VAR`) | Catálogo en Referencias-ConceptoTX (pendiente de relevar). |
| `body.emails` | String[] | Sí | Emails para comprobante — el remitente es la cuenta de mails de Banco Industrial. |

*Debe completarse `to.cbu` o `to.label`, uno de los dos.

### Response — atributos principales

| Campo | Tipo | Descripción |
|-------|------|-------------|
| `id` | String | Formato `<prefijo>-<CUIT>-<ID>-<X>`. Prefijo: `1` = redes interbancarias, `AT` = interna online, `WP` = interna desacoplada. `<X>`: `0` si el ID fue generado internamente, `1` si lo envió el cliente. |
| `type` | String | Default `TRANSFER-CVU`. |
| `from.bank_id` / `from.account_id` | String | Cuenta recaudadora origen (débito). |
| `counterparty.*` | Object | Datos del tercero (`id`, `id_type`, `name`, `bank_routing.*`, `account_routing.scheme` en `LABEL`/`CBU`/`CVU`, `account_routing.address`). |
| `details.origin_id` / `details.origin_debit.cvu` | String | Eco del request. |
| `details.warnings[]` | String[] | Ej. `TRANSACTION_ALREADY_CREATED` si el `origin_id` ya existía. |
| `transaction_ids[]` | String[] | IDs internos de los proveedores implicados (redes interbancarias incluidas). |
| `status` | String | Ver estados abajo. |
| `status_description` | String | Detalle del estado. |
| `start_date` / `end_date` / `business_date` | String (ISO) | Inicio, fin, fecha de conciliación. |
| `charge.summary` / `charge.value.currency` / `charge.value.amount` | — | Cargo aplicado a la operación. |

### Estados posibles (`status`)

- `IN_PROGRESS` — transferencia desde CVU queda así inicialmente; se resuelve al final del día cuando se concilian las operaciones.
- `UNKNOWN` — error de comunicación con un sistema externo; se intenta actualizar durante el día.
- `UNKNOWN_FOREVER` — no se pudo resolver el estado y no se reintentará automáticamente.
- `COMPLETED` / `FAILED` — estados finales.

### Códigos de error

| HTTP | Código | Descripción |
|------|--------|-------------|
| 503 | `GE503` | El estado de las redes no permite ejecutar la transferencia en este momento. |
| 409 | `GE500`/`GE403`/`GE013` | Generales / permisos / email inválido. |
| 409 | `PA001`/`PA002` | Banco / vista inválidos en URL. |
| 409 | `TX001`–`TX012` | Validaciones de datos de destino/monto/moneda/concepto (destino no indicado, monto/moneda faltante o inválido, beneficiario ambiguo o inexistente, CBU/CVU o alias inválido, concepto faltante). |
| 409 | `TX033` | El id debe ser menor a 15 caracteres. |
| 409 | `TX035` | Descripción supera 100 caracteres. |
| 409 | `TX036`–`TX039` | Validaciones de la cuenta origen (CVU/alias faltante, inválido, o ambos enviados). |
| 409 | `TX040` | Moneda distinta a ARS. |
| 409 | `TX046` | El monto excede el límite diario disponible para la cuenta origen. |
| 409 | `TX500` | Error genérico de transferencia (mensaje variable). |
| 409 | `VW002`/`VW005`/`VW016` | PSP sin código asignado / CVU no pertenece a la billetera / no se pudo consultar la cuenta recaudadora. |

---

## 6. Obtener listado de transferencias — `ObtenerPedidosTransferenciasCvu`

> Fuente: https://sandbox.bind.com.ar/apidoc/#api-Billetera-ObtenerPedidosTransferenciasCvu

Obtiene un listado de transferencias realizadas desde o hacia una billetera virtual. `account_id` debe ser la cuenta recaudadora.

### URL / Método

| Campo | Valor |
|-------|-------|
| Método | `GET` |
| URL | `/banks/:bank_id/accounts/:account_id/:view_id/transaction-request-types/TRANSFER-CVU` |

### Headers de filtro (opcionales)

| Header | Descripción |
|--------|-------------|
| `obp_status` | Estado de la transferencia — catálogo Referencias-EstadoTX (pendiente de relevar). |
| `obp_limit` / `obp_offset` | Paginación. |
| `obp_from_date` / `obp_to_date` | Rango de fechas ISO. |
| `obp_origin` | Origen de la transferencia — catálogo Referencias-OriginTX (pendiente de relevar). |

### Response

Mismo contrato por elemento que el response de `CrearTransferenciaCVU` (id, type, from, counterparty, details, transaction_ids, status, fechas, charge), en un array. Para transferencias recibidas, `details.origin_credit.cvu` reemplaza a `origin_debit.cvu`.

### Códigos de error

`GE500`, `GE403`, `GE003`.

---

## 7. Obtener una transferencia — `ObtenerPedidoTransferenciaCvu`

> Fuente: https://sandbox.bind.com.ar/apidoc/#api-Billetera-ObtenerPedidoTransferenciaCvu

Obtiene el detalle de una transferencia de/hacia CVU en particular, por `transaction_id` (el generado por el usuario, el devuelto al crear la transferencia, o el de la consulta de listado).

### Cómo interpretar la respuesta (guía operativa del propio portal)

- `200` + `status: COMPLETED` → acreditación en destino confirmada.
- `200` + `status: FAILED` → transferencia no cursada; el PSP debe reponer fondos al CVU originante.
- `200` + `status` en `IN_PROGRESS`/`UNKNOWN`/`UNKNOWN_FOREVER`, o `409` con `code: TX019` (transferencia no encontrada) u otro código → estado aún no determinable, reintentar consulta 5 minutos después. `UNKNOWN_FOREVER` requiere conciliar contra el archivo de conciliación. `TX019` puede darse por una carrera entre el registro de la solicitud y la consulta.

### URL / Método

| Campo | Valor |
|-------|-------|
| Método | `GET` |
| URL | `/banks/:bank_id/accounts/:account_id/:view_id/transaction-request-types/TRANSFER-CVU/:transaction_id` |

### Response

Mismo contrato que el listado (punto 6), para un único elemento — incluye además `status_description`.

### Códigos de error (HTTP 409)

| Código | Descripción |
|--------|-------------|
| `GE500` / `GE403` / `GE003` | Generales. |
| `PA002` | Vista inválida en URL. |
| `TX019` | Transferencia inexistente (ver interpretación arriba). |
| `TX044` | El CUIT de la cuenta origen no es válido. |

---

## Nota de relevamiento

Grupo completo (7/7 endpoints relevados) desde `https://sandbox.bind.com.ar/apidoc/api_data.json`. Varios campos referencian catálogos de otros grupos (`Referencias-ConceptoTX`, `Referencias-EstadoTX`, `Referencias-OriginTX`, `Referencias-Currency`, `Referencias-OperationType`) — grupo `Referencias` (31 endpoints tipo catálogo) quedó fuera del alcance de esta ronda, ver nota de pendientes en el índice de `contexto_vivo/`.

---
id: 2026-09-01_arquitectura_api_bank_alta_de_cuenta
pm: pablo
fecha_captura: 2026-09-01
fuente: "Portal público de developers API BANK — https://sandbox.bind.com.ar/apidoc/#api-Alta_De_Cuenta"
producto: transversal
tema: API BANK (Banco Industrial) — Alta de Cuenta (onboarding PSI/STI) — referencia de endpoints
tipo: conocimiento
destino_propuesto: 3_recursos/arquitectura_sistema/api_bank/alta_de_cuenta.md
tipo_destino: crear
contradice: "no"
confianza: alta
estado: en_cola
merge_commit:
---

## Contexto — qué son PSI y STI

Grupo **Alta_De_Cuenta**: onboarding de cuentas CBU/CVU vía API BANK, para dos modalidades de proveedor de billetera:

- **PSI** — el consumo de las APIs PSI habilita a una billetera a realizar altas, consultas y pagos de sus usuarios ordenantes sobre una cuenta bancaria (CBU) abierta en el banco a su nombre. La billetera PSI recopila los datos del usuario y llama a la API de alta; **el banco realiza la validación biométrica** y gestiona el alta a partir de la identificación positiva.
- **STI** — el mismo tipo de habilitación, pero la **billetera STI es responsable de garantizar la identificación positiva del cliente** mediante sus propias técnicas de biometría, y envía la información ya validada al banco.

Diferencia clave: en PSI la validación biométrica la hace el banco; en STI la hace la billetera antes de llamar a la API. Ambos flujos son relevantes como referencia de cómo Bind (o cualquier PSP que use API BANK) puede dar de alta cuentas de sus propios clientes contra Banco Industrial — comparar contra el onboarding real que usa Bind Wallet/Agente de Cobros y Pagos (documentado en `wiki/3_recursos/detalle_productos/onboarding/`).

Header `Authorization: JWT :token` obligatorio en todos. `bank_id` siempre `322`, `view_id` (donde aplica) siempre `"owner"`.

---

## 1. Alta Cuenta cliente PSI — `PSICrearCuenta`

> Fuente: https://sandbox.bind.com.ar/apidoc/#api-Alta_De_Cuenta-PSICrearCuenta

La API de alta de cuenta cliente permite a la billetera PSI generar el alta de paquetes de cuentas bancarias a nombre del usuario. El banco realiza la validación biométrica y, a partir de la identificación positiva, gestiona el alta del paquete de productos definido para el PSI.

### URL / Método

| Campo | Valor |
|-------|-------|
| Método | `POST` |
| URL | `/banks/:bank_id/:view_id/account-onboarding/psi` |

### Parámetros del request (principales)

| Parámetro | Tipo | Obligatorio | Descripción |
|-----------|------|-------------|-------------|
| `body.document` | String | Sí | CUIT del cliente, solo números. |
| `body.document_type` | String | Sí | `cuit`, `cuil` o `cdi`. |
| `body.tyc` | String | Sí | Aceptación de términos y condiciones. |
| `body.firstname` / `body.lastname` | String | Sí | 3–41 caracteres. |
| `body.date_of_birth` | String | Sí | Formato `YYYY-MM-DD`. |
| `body.civil_status` / `body.sex` / `body.occupation` / `body.occupation_description` / `body.laboral_activity` / `body.laboral_activity_description` / `body.nationality` | String | Sí | Códigos definidos en un "Archivo de Códigos-Descripciones" externo al portal (no accesible desde esta ronda de relevamiento). |
| `body.contacts[]` | Array | Sí | `contact_type` (`EMAIL`/`MOBILE`/`PHONE`), `value`, `is_verified`. **Debe incluir al menos un `EMAIL` y un `MOBILE`.** |
| `body.address.*` | Object | Sí | `street`, `number`, `city`, `province`, `province_code`, `floor`, `apartment`, `postal_code`, `cpa` (Código Postal Ampliado), `country` (Argentina = `80`). |
| `body.declaration.pep` / `.nif` / `.fatca` / `.ocde` / `.sujeto_obligado` | Boolean | Sí | Declaraciones normativas (persona políticamente expuesta, NIF extranjero, FATCA, OCDE, sujeto obligado). |
| `bank_id`, `view_id` | — | Sí | Estándar. |

### Response

| Campo | Tipo | Descripción |
|-------|------|-------------|
| `cuit` / `document_type` | String | Ecos del request. |
| `workflow_id` | String | Identificador del proceso de onboarding. |
| `workflow_status` | String | En la respuesta de creación, siempre `STARTED`. |
| `redirect_url` | String | URL a la que redirigir al usuario final para continuar el alta (validación biométrica). |

### Códigos de error (HTTP 409)

`GE500`, `GE403`, `GE003`, `GE009` (país inválido), `PA014` (tipo de documento incorrecto), `PA015` (formato de titular inválido), `TX012`/`TX040` (moneda inválida / solo ARS).

---

## 2. Alta Cuenta cliente STI — `STICrearCuenta`

> Fuente: https://sandbox.bind.com.ar/apidoc/#api-Alta_De_Cuenta-STICrearCuenta

Mismo contrato de parámetros que `PSICrearCuenta` (documento, datos personales, contactos, dirección, declaraciones) — la diferencia es de responsabilidad de negocio: la billetera STI ya validó biométricamente al cliente antes de llamar.

### URL / Método

| Campo | Valor |
|-------|-------|
| Método | `POST` |
| URL | `/banks/:bank_id/:view_id/account-onboarding/sti` |

### Response

Igual forma que PSI, pero `workflow_status` en la respuesta de creación es `IN_PROGRESS` (no `STARTED`), y no se documenta `redirect_url` en el ejemplo (consistente con que STI no necesita redirigir al usuario a un flujo biométrico externo, ya que la billetera lo validó antes).

### Códigos de error

Mismo set que `PSICrearCuenta`.

---

## 3. Alta Cuenta cliente STI (PJ) — `STICrearCuentaPJ`

> Fuente: https://sandbox.bind.com.ar/apidoc/#api-Alta_De_Cuenta-STICrearCuentaPJ

Permite a una billetera STI dar de alta cuentas bancarias a nombre de una **Persona Jurídica**. La billetera recopila los datos de la empresa y de su representante legal o apoderado.

### URL / Método

| Campo | Valor |
|-------|-------|
| Método | `POST` |
| URL | `/banks/:bank_id/:view_id/account-onboarding-pj/sti` |

### Parámetros del request (principales)

| Parámetro | Tipo | Obligatorio | Descripción |
|-----------|------|-------------|-------------|
| `body.document` | String | Sí | CUIT de la Persona Jurídica. |
| `body.company_name` | String | Sí | Razón social. |
| `body.incorporation_date` | String | Sí | Fecha de constitución, `YYYY-MM-DD`. |
| `body.address.*` | Object | Sí | Domicilio legal de la empresa (mismos sub-campos que en PSI/STI PF). |
| `body.contacts[]` | Array | Sí | Contactos de la empresa (`EMAIL`, `PHONE`). |
| `body.members[]` | Array | Sí | Representantes/apoderados: `document`, `country_code`, `document_type` (`DNI`/`CUIT`), `name`, `last_name`, `sex`, `civil_status`, `relationship` (`legal_representative`/`proxy`), `contacts[]`, `address`, y las mismas declaraciones normativas por persona (`pep`, `nif`, `fatca`, `ocde`, `sujeto_obligado`). |

### Response

| Campo | Tipo | Descripción |
|-------|------|-------------|
| `cuit` | String | CUIT de la Persona Jurídica. |
| `document_type` | String | Siempre `cuit` para PJ. |
| `workflow_id` | String | Identificador del proceso. |
| `workflow_status` | String | Siempre `IN_PROGRESS` en la respuesta de creación. |

### Códigos de error (HTTP 409)

`GE500`, `GE403`, `GE003`, `GE009`, `PA004` (CUIT inválido), `PA014`, `PA015`, `TX012`/`TX040`.

---

## 4. Obtener estado de un workflow — `PSIConsultarEstadoFlujoAlta`

> Fuente: https://sandbox.bind.com.ar/apidoc/#api-Alta_De_Cuenta-PSIConsultarEstadoFlujoAlta

Proporciona el detalle de un workflow de creación de cuenta (PSI o STI, PF o PJ) a partir del `workflow_id` generado en el alta. **La API de alta es idempotente**: si no se tiene el `workflow_id`, se puede reinvocar el alta para recuperarlo.

### URL / Método

| Campo | Valor |
|-------|-------|
| Método | `GET` |
| URL | `/banks/:bank_id/:view_id/account-onboarding/:workflow_id/:document_type/:document` |

### Parámetros

| Parámetro | Tipo | Obligatorio | Descripción |
|-----------|------|-------------|-------------|
| `workflow_id` | String | Sí | Identificador del workflow. |
| `document_type` | String | Sí | `cuit`, `cuil` o `cdi`. |
| `document` | String | Sí | CUIT del cliente, solo números. |
| `bank_id` | Number | Sí | `322`. |

### Response — atributos

| Campo | Tipo | Descripción |
|-------|------|-------------|
| `document` / `document_type` | — | Ecos del request. |
| `workflow_id` | String | Identificador del workflow. |
| `workflow_status` | String | Uno de: `STARTED`, `IN_PROGRESS`, `ACCOUNT_CREATED`, `ACCOUNT_ACTIVE`, `ACCOUNT_BLOCKED`, `FINISHED`, `FAILED`, `EXPIRED`, `REJECTED`. |
| `accounts[]` | Object[] | Detalle de cuentas creadas. |
| `accounts.account_id` | String | Identificador de cuenta (informado si se logró crear online). |
| `accounts.cbu` | String | CBU del cliente. |
| `accounts.currency` | String | Ej. `ARS`. |
| `accounts.token` | String | Token de autorización para operar la cuenta. |
| `accounts.expiration_date` | String (ISO) | Expiración del token. |
| `accounts.account_active` | Boolean | Si la cuenta está activa. |

### Ejemplo de response

```json
{
  "document": "20312528046",
  "document_type": "cuil",
  "workflow_id": "1234",
  "workflow_status": "IN_PROGRESS",
  "accounts": [
    { "account_id": "21-1-99999-4-6", "cbu": "3220001801000020816200", "currency": "ARS", "token": "wXyZ1aB2cD3eF4gH5iJ6kL7mN8", "expiration_date": "2026-03-05T15:10:25Z", "account_active": true },
    { "account_id": "21-1-99999-4-7", "cbu": "3220001818007706660027", "currency": "USD", "account_active": false }
  ]
}
```

Nota: un mismo workflow puede tener **múltiples cuentas asociadas** (por ejemplo, ARS y USD), cada una con su propio estado de activación.

### Códigos de error

| HTTP | Código | Descripción |
|------|--------|-------------|
| 503 | `GE503` | Estado de las redes no permite ejecutar la operación. |
| 409 | `GE500`/`GE403` | Generales / permisos. |
| 409 | `PA001`/`PA002`/`PA003` | Banco / vista inválidos, o vista inválida para el usuario logueado. |
| 409 | `PA014` | Tipo de documento incorrecto. |
| 409 | `PSI02` | Error interno al consultar el workflow de alta. |
| 409 | `PSI05` | Error interno al consultar el estado del workflow. |

---

## 5. Renovar el token de un PSI/STI — `PSIRenovarToken`

> Fuente: https://sandbox.bind.com.ar/apidoc/#api-Alta_De_Cuenta-PSIRenovarToken

Renueva el token de operación (`accounts.token` obtenido en el alta) de un cliente PSI/STI — necesario para seguir operando la vista `delegate` (ver grupo `Vista`, header `Delegate-authentication`).

### URL / Método

| Campo | Valor |
|-------|-------|
| Método | `POST` |
| URL | `/banks/{bankId}/{viewId}/renew-token` |

### Parámetros

| Parámetro | Tipo | Obligatorio | Descripción |
|-----------|------|-------------|-------------|
| `bankId` | String | Sí | Código de banco (`322`). |
| `viewId` | String | Sí | Valor permitido: `"owner"`. |
| `requestDTO` | — | Sí | Datos para renovar el token (`RenewTokenRequestDTO`, sin detalle adicional de sub-campos en la fuente). |

### Response

| Campo | Tipo | Descripción |
|-------|------|-------------|
| `account_number` | String | Número de cuenta. |
| `token` | String | Nuevo token generado (JWT). |
| `expires_in` | Number | Segundos de validez. |

### Códigos de error

| HTTP | Código | Descripción |
|------|--------|-------------|
| 503 | `GE503` | Redes no disponibles. |
| 409 | `GE500`/`GE403` | Generales / permisos. |
| 409 | `PA001`/`PA002`/`PA003` | Banco / vista inválidos. |
| 409 | `PA014` | Tipo de documento incorrecto. |
| 409 | `PSI02`/`PSI05` | Errores internos de consulta de workflow. |
| 401 | `TK001` | Token inválido o expirado. |

---

## Nota de relevamiento

Grupo completo (5/5 endpoints relevados) desde `https://sandbox.bind.com.ar/apidoc/api_data.json`. Los catálogos de códigos referenciados por `PSICrearCuenta`/`STICrearCuenta` (`civil_status`, `sex`, `occupation`, `laboral_activity`, `nationality`, `province_code`, `country`) están documentados en un "Archivo de Códigos-Descripciones" externo, enlazado desde el propio portal como `@@URL_PSI_CODE_DESC` (placeholder no resuelto en el JSON — no se pudo acceder al contenido real de ese archivo desde esta ronda de relevamiento). Ver item de tipo `gap` asociado.

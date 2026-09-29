# API Broker (Poincenot/IVSA) — Fundamentos: autenticación, cuenta comitente y errores

> Estado: en producción (superficie documentada tal como está publicada en el sandbox de test de Poincenot). Fuente: portal público de documentación de Poincenot (`apibroker.pcnt.io`, endpoint `https://api-investment-ar-test.pcntassets.com`), navegado en vivo durante el discovery de `inter_fondeo_usd/` (2026-09-28).

## Qué es este documento

El "API Broker" es la API REST de Poincenot, el proveedor tecnológico que opera la integración de Bind PSP con el broker IVSA (Bind Inversiones) para todo lo relacionado a dólar (CCL/D1C, FX/MULC, Combi), cuenta remunerada/FCI, y trading de instrumentos. Ya estaba documentado en el Cerebro de forma dispersa ([`dolar_ccl.md`](dolar_ccl.md), [`dolar_fx.md`](dolar_fx.md), [`cuenta_remunerada_fci.md`](cuenta_remunerada_fci.md) citan esta API sin documentar su superficie completa). Este archivo, y sus hermanos de la misma fecha, documentan **la superficie completa de la API pública de Poincenot** tal como está publicada hoy en su sandbox de test.

**Alcance de la API completa** (secciones del portal):
- Fundamentos (este archivo): Auth, Account/KYC, códigos de error y enums.
- Dólar 1 Click (D1C) — ver [`dolar_ccl.md`](dolar_ccl.md).
- Dólar FX (MULC) — ver [`dolar_fx.md`](dolar_fx.md).
- Dólar Combi — ver [`dolar_ccl.md §3.8`](dolar_ccl.md), pertenece a otro proyecto (COMBI/MOVE, foco de Luciana Rudaz).
- Cuenta remunerada (Interest Bearing Account) — ver [`cuenta_remunerada_fci.md`](cuenta_remunerada_fci.md).
- Tesorería, P2P y Portfolio (retiros a CBU/CVU externo, transferencias entre cuentas comitente, consulta de saldo) — ver [`api_broker_poincenot_tesoreria_p2p_portfolio.md`](api_broker_poincenot_tesoreria_p2p_portfolio.md), el más relevante para el proyecto `inter_fondeo_usd/`.
- Pagos, CAP y Trading general (tarjeta de crédito, cambio de perfil transaccional, compra/venta de títulos, FCI genérico) — ver [`api_broker_poincenot_pagos_cap_trading_fci.md`](api_broker_poincenot_pagos_cap_trading_fci.md), sin uso identificado hoy en ningún proyecto de Bind PSP.

## Autenticación

- **Login:** `POST /profile/v1/login/api`. Body: `{"username": "<access_key>", "password": "<secret>"}`. Header `organization: <acrónimo de la organización>`. Devuelve `{"token": "<JWT>"}`.
- El JWT **no expira mientras esté en uso**. Se pueden generar varios JWT simultáneos bajo el mismo `access_key`/`secret` (útil para múltiples microservicios). Si expira por inactividad, las APIs devuelven HTTP 401.
- **Headers estándar en toda la API:**
  - `organization`: acrónimo de la organización que invoca (provisto por Poincenot).
  - `account`: número de cuenta comitente que invoca — solo requerido en APIs que operan sobre una cuenta.
  - `Authorization: JWT <token>`.
- **ThirdPartyId:** ID generado por quien consume la API, único, con **idempotencia real**: el mismo `thirdPartyId` siempre devuelve la misma respuesta — cada `thirdPartyId` debe corresponder a una sola operación.

## Alta y consulta de cuenta comitente (KYC)

### Alta de cuenta — `POST /profile/v1/account`

Da de alta una persona física con todo el legajo KYC en un solo request. Campos principales del body (ejemplo real de la doc):

```json
{
  "thirdPartyId": "XU231A",
  "person": {
    "naturalPerson": true,
    "name": "Romina Paola",
    "lastname": "Pizzo",
    "nationality": "AR",
    "residenceCountry": "AR",
    "identificationType": "DNI",
    "identification": "28334194",
    "identificationCountry": "AR",
    "maritalState": "SINGLE",
    "birthDate": "1978-03-04",
    "birthPlace": "AR",
    "gender": "F",
    "taxInformation": {
      "type": "CUIT",
      "number": "27283341947",
      "businessActivity": "11341",
      "pep": { "isPep": true, "description": "Diputado Nacional" },
      "incomeInscription": { "type": "EXE", "date": "1998-10-04" },
      "ivaCondition": "RI",
      "countryTaxResidence": "AR",
      "fatca": { "isFatca": true, "ssn": "1491949991" },
      "ocde": {
        "isOcde": true,
        "countryTaxResidencePrincipal": "UY",
        "nitPrincipal": "12355550",
        "countryTaxResidenceOptional": "BR",
        "nitOptional": "12355554"
      },
      "subjectsBound": { "isSubjectsBound": true, "createdDate": "1998-10-04" }
    }
  },
  "address": { "type": "LEGAL", "street": "Helguera", "number": "2177", "floor": "3", "apartment": "A", "zipCode": "1752", "country": "AR", "state": "AR", "locality": "CABA" },
  "contact": { "email": "ejemplo@mail.com", "phone": "12341234", "areaCode": "011" },
  "documents": [
    { "type": "FRONT_DNI", "description": "Front DNI", "filename": "frente.png", "extension": ".png", "verified": true, "file": { "url": "http://contentcdn.com/imagenes/12345.png" } }
  ],
  "identityVerification": { "id": "21223213213" },
  "banks": { "identification": "0000347730000000049606", "type": "CVU" }
}
```

Respuesta: `{"account": "234234"}` (número de cuenta comitente asignado).

- **Tipos de documento en `documents`:** `FRONT_DNI`, `BACK_DNI`, `SELFIE`, `INCOME_PROOF`, `SERVICE`, `SIGNATURE`.
- **`banks.type`:** `CBU` o `CVU` — la cuenta bancaria/CVU a la que se asocia la cuenta comitente.
- **Errores relevantes (HTTP 409):** `THIRD_PARTY_ID_ALREADY_USE_FOR_ANOTHER_TAX_IDENTIFICATION`, `INVALID_TAX_INFORMATION_NUMBER`, `HIT_ON_BLACK_LIST_15/37/41` (listas negras numeradas), `IMPOSSIBLE_CREATE_ACCOUNT_IVSA_RESTRICTION`, `PERSON_IS_NOT_LEGAL_AGE`, entre otros de validación de campos.

### Alta multi-titular — `POST /profile/v1/account/multi/owners`

Mismo modelo, pero con `persons: [{person, address, contact, documents, identityVerification}, ...]` — para cuentas con más de un titular.

### Consulta de cuenta — `GET /profile/v1/customer`

Devuelve, entre otros, `bankIdentificationCvu` (CVU del titular), `bindBankAccountIdentification` (el **CBU creado en Bind**) y `bindBankAccountLabel` (su alias), con `bindBankAccountLabelState` (`CHECKING`/`DISABLED`/`INFORMED`) — confirma que la cuenta comitente de IVSA y el CBU/alias de Bind quedan vinculados y consultables desde esta misma API.

### Cuenta habilitada para operar — `GET /account-validator/v1/account/enabled`

**Importante — no confundir con validación de CBU/alias bancario.** Este endpoint es un chequeo de **compliance/AML sobre la cuenta comitente** (blacklist, PLD, restricciones operativas), no valida una cuenta bancaria de destino. Devuelve `{"enabled": true|false, "detail": [...]}`; el `detail` (si `enabled=false`) trae códigos como `BLACKLIST_HIT`, `ANTI_MONEY_LANDRYING`, `BLOQUEO_BC_PEP`, `BLOQUEO_BC_FATCA`, `BIND_DECISION_PLD`, `OP_COMEX_EXCH` (restricción por operaciones COMEX/FX), `OP_CEDEARS` (compró CEDEAR en los últimos 90 días), `OP_TRANSF_TIT_EXT` (transferencias de títulos al exterior en los últimos 90 días), entre ~20 códigos más. **Gap identificado en la sesión del 2026-09-23 (proyecto `inter_fondeo_usd`): la validación de CBU/alias de una cuenta de destino, para envíos salientes, no la resuelve este endpoint — Bind PSP ya la consume desde su propia API Bank (`ConsultaCuentaCBU`), confirmado por el PM el 2026-09-28.**

## Errores y formato

Todas las APIs transaccionales devuelven HTTP 409 en error, con el formato `{"code": "<CODIGO>", "process": "<id>"}` (o `errorDetail: {code, final}` en los webhooks asíncronos, donde `final` indica si el error es reintentable). Errores de autenticación devuelven HTTP 401.

## Enums de referencia (código de apéndice)

- **Income Tax Status:** `EXE` (Exento), `INS` (Inscripto), `NOINS` (No Inscripto).
- **VAT Status (`ivaCondition`):** `RI` (Responsable Inscripto), `RNI` (Responsable No Inscripto), `EX` (Exento), `RM` (Monotributista), `CF` (Consumidor Final).
- **Account States:** `ACTIVE`, `INACTIVE`.
- Provincias argentinas (código ISO `AR-XX`) y países (ISO de 2 letras) — catálogos completos, no se transcriben acá por ser estándar.

## Ver también
- [dolar_ccl.md](dolar_ccl.md), [dolar_fx.md](dolar_fx.md), [cuenta_remunerada_fci.md](cuenta_remunerada_fci.md) — flujos de negocio que consumen esta API.
- [api_broker_poincenot_tesoreria_p2p_portfolio.md](api_broker_poincenot_tesoreria_p2p_portfolio.md), [api_broker_poincenot_pagos_cap_trading_fci.md](api_broker_poincenot_pagos_cap_trading_fci.md) — resto de la superficie de la API.

---
*Última actualización: 2026-09-29 — `/context_merge`: archivo nuevo, relevamiento completo de la API pública de Poincenot durante el discovery de `inter_fondeo_usd/` (Pablo Gomes).*

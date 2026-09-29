---
id: 2026-09-28_wallet_api_broker_poincenot_tesoreria_p2p_portfolio
pm: pablo
fecha_captura: 2026-09-28
fuente: "portal público de documentación de Poincenot (apibroker.pcnt.io), navegado en vivo con el Chrome del PM durante /idea_start de inter_fondeo_usd"
producto: wallet
tema: "API Broker (Poincenot/IVSA) — Tesorería (retiro a CBU/CVU externo), P2P (transferencia entre cuentas comitente) y Portfolio (saldo disponible y tenencia)"
tipo: conocimiento
destino_propuesto: 3_recursos/detalle_productos/wallet/api_broker_poincenot_tesoreria_p2p_portfolio.md
tipo_destino: crear
contradice: "no"
confianza: alta
estado: ingestado
merge_commit: 9fbee64
---

## Por qué importa

Estas tres secciones de la API de Poincenot son las que más impactan el discovery de `inter_fondeo_usd/` (ingreso y envío de USD al exterior para Inter): confirman que **la consulta de saldo (S3) y el retiro a una cuenta externa (S6)** ya existen como endpoints publicados y en test — no hace falta pedírselos a IVSA como desarrollo nuevo. Lo que **no existe** es un endpoint de acreditación entrante/cash-in (ver más abajo).

## Tesorería — retiro a cuenta bancaria externa

### Retiro — `POST /cash-management/v1/transaction/OUT`

Envía dinero desde la cuenta comitente a una cuenta bancaria externa (CBU/CVU), en cualquier moneda soportada.

- **Headers:** además de los estándar, `account` (cuenta comitente) y `location` (URL a la que Poincenot manda el webhook de resultado).
- **Request:** `currency` (moneda), `amount`, `identificationBankAccount` (CBU/CVU de destino), `thirdPartyId`.
- **Response (200):**
```json
{
  "uniqueId": "1266122743860322304",
  "originBankAccount": {
    "identification": "3220001812000036580135",
    "account": "12000036580135",
    "taxIdentification": "30642023876",
    "name": "IVSA"
  }
}
```
- **Errores:** `NOT_MONEY_AVAILABLE`, `REQUIRED_FIELD_WITH_NULL_VALUE`, `INVALID_CURRENCY`, además de los genéricos.
- **Webhooks:** `PROCESS OK` (`{"id", "state": "CONCILIATION", "thirdPartyId"}`) y `PROCESS ERROR` (`{"id", "state": "ERROR", "thirdPartyId", "errorDetail": {"code", "final"}}`) — `final` indica si el error es reintentable.

### Consulta de estado — `GET /cash-management/v1/transaction`

Consulta el estado de un retiro ya iniciado, por `thirdPartyId` o `transactionId`. Devuelve `state`: `PENDING`, `ERROR`, `CONCILIATION`. Errores propios de la integración con el banco: `APIBANK_VALIDATION_ERROR`, `APIBANK_INVALID_DESTINATION_ACCOUNT`, `APIBANK_INVALID_CBU_CVU` (ambos reintentables) — confirma que este endpoint de Poincenot internamente valida contra **API Bank** del lado de ellos.

## P2P — transferencia entre cuentas comitente

### Transferir — `POST /cash-management/v1/p2p/transfer`

Mueve dinero entre dos cuentas comitente (no a una cuenta bancaria externa — `destinationAccount` es otra cuenta comitente, no un CBU). Request: `thirdPartyId`, `amount`, `currency`, `destinationAccount`. Respuesta: `{"uniqueId": "..."}`. Mismos webhooks de proceso OK/error que Tesorería. Errores: `NOT_MONEY_AVAILABLE`, `INVALID_CURRENCY`, `INVALID_BANK_TRANSACTION`.

### Preview — `POST /cash-management/v1/p2p/preview`

Antes de transferir, devuelve el detalle de impuestos aplicables (`destinationTaxDetail`), por ejemplo:
```json
{
  "destinationTaxDetail": [
    { "subtype": "DEFAULT", "amount": 0.03, "currency": "USD", "aliquotApplied": 0.006, "name": "IDC", "registerDate": "2026-01-27" },
    { "subtype": "M", "amount": 0.25, "currency": "USD", "aliquotApplied": 0.05, "name": "IIBB", "registerDate": "2025-12" }
  ]
}
```
Confirma que **el P2P soporta USD** (impuestos calculados en USD en el ejemplo real de la doc).

### Consulta — `GET /cash-management/v1/p2p/transfer` (detalle)

Devuelve el detalle de una transferencia P2P ya realizada.

## Portfolio — tenencia y saldo

### Consulta de saldo disponible — `GET /portfolio/v1/balances/available`

**Esta es la pieza que resuelve S3 del discovery de `inter_fondeo_usd/` sin desarrollo nuevo.** Devuelve el saldo disponible para operar, desglosado por **plazo de liquidación** (`T0`=Contado Inmediato/hoy, `T1`=24hs, `T2`=48hs) y por **moneda**, incluyendo USD explícitamente:

```json
{
  "T0": [
    { "currency": "ARS", "amount": 50000 },
    { "currency": "USD", "amount": 10000 }
  ],
  "T1": [
    { "currency": "ARS", "amount": 98000 },
    { "currency": "USD", "amount": 12000 }
  ],
  "T2": [
    { "currency": "ARS", "amount": 99000 },
    { "currency": "USD", "amount": 12000 }
  ]
}
```

### Consulta de activos — `GET /portfolio/v1/assets`

Devuelve la tenencia completa de la cuenta comitente (bonos, fondos, etc.), con disponibilidad por plazo y valorización. Ejemplo real de la doc, con un bono en dólares:
```json
{
  "instrumentTicker": "BONO REP ARG USD STEP UP 2030",
  "instrumentName": "BONO REP ARG USD STEP UP 2030",
  "currency": "ARS",
  "price": 57.3,
  "quantity": 4723,
  "available": 4723,
  "pendingSettlements": false,
  "availability": [
    { "term": "T1", "quantity": 4723, "monetaryValue": { "currency": "ARS", "amount": 270627.9 } }
  ]
}
```
(Nota: el ejemplo de la doc valoriza el bono en ARS pese a ser un instrumento denominado en USD — es la lógica de "instrumento vs. moneda de cotización" ya conocida del mecanismo AL30/AL30D de `dolar_ccl.md`.)

## Lo que NO está documentado: cash-in / acreditación entrante

Se revisó toda la documentación pública de Poincenot y **no existe ningún endpoint de acreditación entrante ("cash-in") ni webhook de "recibiste dinero"** — solo hay salida (Tesorería `OUT`) y transferencia entre cuentas comitente (P2P). Esto es evidencia a favor de que **S1 (cuenta recaudadora dedicada en USD) y S2 (webhook de cash-in)**, las dos piezas centrales del PRD que compartió Gastón Degiovanni para `inter_fondeo_usd/`, son **desarrollo nuevo real de parte de IVSA/Poincenot**, no algo ya expuesto y solo por consumir. Relevante para dimensionar el Carril 2 del discovery en `/idea_solution`.

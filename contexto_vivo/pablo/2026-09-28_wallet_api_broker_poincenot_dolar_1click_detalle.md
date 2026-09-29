---
id: 2026-09-28_wallet_api_broker_poincenot_dolar_1click_detalle
pm: pablo
fecha_captura: 2026-09-28
fuente: "portal público de documentación de Poincenot (apibroker.pcnt.io), navegado en vivo con el Chrome del PM durante /idea_start de inter_fondeo_usd"
producto: wallet
tema: "API Broker (Poincenot) — Dólar 1 Click (D1C/MEP): detalle completo de endpoints, request/response y webhooks (complementa dolar_ccl.md)"
tipo: conocimiento
destino_propuesto: 3_recursos/detalle_productos/wallet/dolar_ccl.md
tipo_destino: actualizar
contradice: "no"
confianza: alta
estado: ingestado
merge_commit: 9fbee64
---

## Contexto

`dolar_ccl.md` ya documenta el flujo de negocio de Dólar CCL/1Click (comisiones, modelo Combi, casos de uso Inter/Coinbase, bugs históricos). Este item agrega el **detalle técnico de la API pública de Poincenot** para ese mismo producto (en la doc de Poincenot se llama "Dollar 1 Click" / D1C / USDMEP), que no estaba consolidado: los endpoints reales con su request/response, y los dos webhooks por operación (patas 1 y 2).

## Cotización — `GET /marketdata/v1/price/usdmep`

```json
{ "buyPrice": 1481.82, "sellPrice": 1274.23, "timestamp": "2024-08-06T08:09:02Z" }
```

## Gastos de compra (preview) — `POST /investment-operation-flow/v1/exchange/usdmep/preview/BUY`

Request: `{"amount": 200700}` (en pesos). Response:
```json
{
  "amount": 200700, "gross": 198208, "net": 200224.72, "totalExpenses": 2016.72,
  "endOperationDate": "2024-08-07T12:00:00Z", "startOperationDate": "2024-08-06T12:00:00Z",
  "marketIsOpen": false, "totalExpensesCurrency": "ARS", "price": 1481.82,
  "taxes": [{ "name": "IDC", "subtype": "M", "aliquotApplied": 0.05, "amount": 100, "currency": "ARS", "registerDate": "2025-12-01" }]
}
```
Análogo simétrico para venta: `preview/SELL`.

## Ejecutar compra — `POST /investment-operation-flow/v1/exchange/usdmep/BUY`

Request:
```json
{
  "thirdPartyId": "joel-test-uat-20240628-0010",
  "amount": 600000,
  "price": "1330.66",
  "disclaimer": { "accepted": true, "timestamp": "32321321312" }
}
```
Response: `{"operationId": "412412411"}`. El header `location` define a dónde Poincenot manda los webhooks. Errores relevantes: `DISCLAIMER_NOT_ACCEPTED`, `ACCOUNT_DISABLED_TO_OPERATE`, `CLOSED_MARKET`, `CLOSED_OPERATION`, `MONTHLY_SUM_EXCEEDED`, `INVALID_MIN_USD`, `OUTDATED_REFERENCE_PRICE` (desfasaje entre el precio que mandó el cliente y el que devuelve el mercado al momento de ejecutar). Análogo para venta: `.../usdmep/SELL`, con error adicional `NOT_MONEY_AVAILABLE`.

## Webhooks — dos patas por operación (confirma el mecanismo AL30→AL30D de `dolar_ccl.md`)

**Leg 1** (compra del bono en pesos):
```json
{ "id":"00014fuk9x", "external_id":"1270022436872830976", "status":"APPROVED", "amount":599605.16,
  "taxes": [{ "name": "IDC", "subtype": "M", "aliquotApplied": 0.05, "amount": 100, "currency":"ARS", "registerDate": "2025-12-01" }] }
```

**Leg 2** (venta del bono en dólares — liquidación final):
```json
{ "id":"00014j8x7a", "external_id":"1270384740564017152", "status":"EXCHANGED", "amount":2.35, "exchange_amount":3119.66,
  "taxes": [{ "name": "IDC", "subtype": "M", "aliquotApplied": 0.05, "amount": 100, "currency":"ARS", "registerDate": "2025-12-01" }] }
```
`exchange_amount` es el monto final convertido. Los mismos dos webhooks (leg 1/leg 2) aplican también a la venta.

## Consultar una operación — `GET /investment-operation-flow/v1/exchange`

Por `thirdPartyId` u `operationId`. Devuelve `state` (`REGISTERED`/`APPROVED`/`EXCHANGED`/`ERROR`), `result: {totalInvested, totalObtained}`, y **`relatedOperations`**: el detalle de cada pata como operación de mercado independiente. Ejemplo real (compra):
```json
{
  "thirdPartyId": "0000tbx5oa", "amount": 1100000, "account": "1680043", "state": "EXCHANGED",
  "result": { "totalInvested": 1099048.91, "totalObtained": 979.24 },
  "id": "27293924800256", "operation": "BUY",
  "relatedOperations": [
    { "instrument": "BYMA.AL30", "term": "T0", "state": "FILLED", "amount": 1088396.1, "quantity": 1683,
      "expenses": { "byMarket": 108.81, "byOperation": 10880.6, "total": 10989.41 },
      "finalAmount": 1088059.5, "finalQuantity": 1683, "currency": "ARS", "operation": "BUY" },
    { "instrument": "BYMA.AL30D", "term": "T0", "state": "FILLED", "quantity": 1683,
      "expenses": { "byMarket": 0.1, "byOperation": 0, "total": 0.1 },
      "finalAmount": 979.34, "finalQuantity": 1683, "currency": "USD", "operation": "SELL" }
  ]
}
```
Confirma literalmente el mecanismo: comprar `BYMA.AL30` (pesos) y vender `BYMA.AL30D` (dólares) como dos operaciones de mercado relacionadas dentro de una única operación D1C.

## DDJJ (affidavit) — `GET /investment-operation-flow/v1/disclaimer/usdmep`

```json
{
  "disclaimer": "According to BCRA Communication A 7552, I declare that in the last 90 calendar days I have not accessed the exchange market for the purchase of foreign currency (including swaps or arbitrations) nor am I subject to any legal or regulatory restriction to carry out the operation.",
  "createdDate": "2023-11-16 11:43:43",
  "key": "D1C_OPERATION"
}
```
**Referencia normativa nueva para el Cerebro: BCRA Comunicación "A" 7552** — la restricción de no haber accedido al mercado de cambios en los últimos 90 días corridos, aplicada al D1C. No estaba citada en `dolar_ccl.md`.

## Flag de producto activo — `GET /investment-operation-flow/v1/operation/enabled`

`{"enabled": true}` — permite consultar si el producto D1C está habilitado para operar en general (no por cuenta), útil para feature-flag del lado de Bind.

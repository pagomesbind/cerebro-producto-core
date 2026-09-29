---
id: 2026-09-28_wallet_api_broker_poincenot_pagos_cap_trading_fci
pm: pablo
fecha_captura: 2026-09-28
fuente: "portal público de documentación de Poincenot (apibroker.pcnt.io), navegado en vivo con el Chrome del PM durante /idea_start de inter_fondeo_usd — resto de la superficie de la API, sin uso identificado hoy en ningún proyecto de Bind PSP"
producto: wallet
tema: "API Broker (Poincenot) — Pagos, CAP (perfil transaccional), Trading de títulos y FCI genérico: inventario de superficie no usada hoy"
tipo: conocimiento
destino_propuesto: 3_recursos/detalle_productos/wallet/api_broker_poincenot_pagos_cap_trading_fci.md
tipo_destino: crear
contradice: "no"
confianza: alta
estado: ingestado
merge_commit: 9fbee64
---

## Por qué se captura esto

A pedido del PM, se completó el relevamiento de **toda** la API de Poincenot durante el discovery de `inter_fondeo_usd/`, no solo lo relacionado a USD. Estas cuatro secciones no tienen uso identificado hoy en ningún proyecto documentado en el Cerebro — se registran como inventario de superficie disponible, sin profundizar en cada campo, para que quede consolidado que existen y qué resuelven.

## Payments

- **`POST /payments/v1/credit/card`** — descuenta saldo disponible y lo asocia a un pago con tarjeta de crédito. Ejemplo real: `{"currency": "USD", "amount": 10, "thirdPartyId": "...", "destinationBankAccountIdentification": "..."}`. Respuesta: `{"uniqueId": "...", "state": "APPROVED"}`.
- **`GET /payments/v1/.../credit/card`** — consulta el pago.
- **`POST /payments/v1/money/transfer/buyer`** — "Collections and Payments - Buyer": descuenta fondos disponibles para realizar un pago, con `destinationBankIdentification` (CBU), `grossAmount`, `totalTaxAmount`, `totalFeeAmount` — parece un mecanismo de cobros/pagos con desglose de impuestos y comisiones, para un flujo comprador/vendedor (hay un endpoint espejo "Seller").
- **`POST /payments/v1/.../seller`** — la contraparte del anterior, del lado del vendedor/cobrador.

## CAP (perfil transaccional)

- **`POST /investment-operation-flow/v1/cap/change`** — "Transactional Profile Change": permite cambiar el perfil transaccional de una cuenta, con `income_amount`, `upload_date` y `documents` (comprobantes de ingresos) — probablemente vinculado a límites operativos por perfil de riesgo/PLD.

## Trade (compra/venta de títulos, general)

Flujo estándar de trading de instrumentos (acciones, bonos — no específico de dólar), con el mismo patrón preview→ejecutar→consultar→cancelar que D1C/FX:
- `POST /trade/v1/trade/BUY/preview` — cotiza una orden antes de ejecutarla. Soporta `ticker` (ej. `ALUA`), `limitPrice`, `settlementTerm` (T0/T1/T2), `type` (`LIMIT`), y `actions` (ej. `STOP_LOSS` condicional con `requiredUserAuthorization`).
- `POST /trade/v1/trade/SELL/preview`, `POST .../BUY`, `POST .../SELL` (ejecutar), `GET .../order` (consultar), `DELETE .../order` (cancelar).

## Mutual Funds (FCI genérico, distinto de la Cuenta Remunerada)

A diferencia de la Cuenta Remunerada (que opera por lotes/`bundle-worker`, ver item hermano de este mismo día), este es un flujo de suscripción/rescate **individual, no por lotes**:
- `POST /trade/v1/fund/BUY` — "Place Subscription". Ejemplo real: `{"instrument": "ADAR-FCI.1195", "currency": "ARS", "amount": 50000, "thirdPartyId": "..."}`. Respuesta: `{"operationType": "FUND", "operationId": "..."}`.
- `POST /trade/v1/fund/SELL` — "Place Redemption" (rescate).
- `GET`/`DELETE` de la orden — consultar y cancelar, mismo patrón que Trade.

Es el mecanismo genérico de FCI de Poincenot — la Cuenta Remunerada de Bind PSP usa el flujo batch (`bundle-worker`) en su lugar, probablemente por volumen (muchos usuarios suscribiendo/rescatando el mismo fondo cada día).

# API Broker (Poincenot) — Pagos, CAP (perfil transaccional), Trading de títulos y FCI genérico

> Estado: superficie disponible del proveedor, **sin uso identificado hoy en ningún proyecto documentado en el Cerebro**. Fuente: portal público de documentación de Poincenot (`apibroker.pcnt.io`), navegado en vivo durante el discovery de `inter_fondeo_usd/` (2026-09-28) — a pedido del PM de completar el relevamiento de toda la API, no solo lo relacionado a USD. Ver [`api_broker_poincenot_fundamentos.md`](api_broker_poincenot_fundamentos.md) para autenticación y headers estándar.

## Por qué se captura esto

Estas cuatro secciones no tienen uso identificado hoy en ningún proyecto documentado en el Cerebro — se registran como inventario de superficie disponible, sin profundizar en cada campo, para que quede consolidado que existen y qué resuelven.

## Payments

- **`POST /payments/v1/credit/card`** — descuenta saldo disponible y lo asocia a un pago con tarjeta de crédito. Ejemplo real: `{"currency": "USD", "amount": 10, "thirdPartyId": "...", "destinationBankAccountIdentification": "..."}`. Respuesta: `{"uniqueId": "...", "state": "APPROVED"}`.
- **`GET /payments/v1/.../credit/card`** — consulta el pago.
- **`POST /payments/v1/money/transfer/buyer`** — "Collections and Payments - Buyer": descuenta fondos disponibles para realizar un pago, con `destinationBankIdentification` (CBU), `grossAmount`, `totalTaxAmount`, `totalFeeAmount` — mecanismo de cobros/pagos con desglose de impuestos y comisiones, para un flujo comprador/vendedor (hay un endpoint espejo "Seller").
- **`POST /payments/v1/.../seller`** — la contraparte del anterior, del lado del vendedor/cobrador.

## CAP (perfil transaccional)

- **`POST /investment-operation-flow/v1/cap/change`** — "Transactional Profile Change": permite cambiar el perfil transaccional de una cuenta, con `income_amount`, `upload_date` y `documents` (comprobantes de ingresos) — probablemente vinculado a límites operativos por perfil de riesgo/PLD.

## Trade (compra/venta de títulos, general)

Flujo estándar de trading de instrumentos (acciones, bonos — no específico de dólar), con el mismo patrón preview→ejecutar→consultar→cancelar que D1C/FX:
- `POST /trade/v1/trade/BUY/preview` — cotiza una orden antes de ejecutarla. Soporta `ticker` (ej. `ALUA`), `limitPrice`, `settlementTerm` (T0/T1/T2), `type` (`LIMIT`), y `actions` (ej. `STOP_LOSS` condicional con `requiredUserAuthorization`).
- `POST /trade/v1/trade/SELL/preview`, `POST .../BUY`, `POST .../SELL` (ejecutar), `GET .../order` (consultar), `DELETE .../order` (cancelar).

## Mutual Funds (FCI genérico, distinto de la Cuenta Remunerada)

A diferencia de la Cuenta Remunerada (que opera por lotes/`bundle-worker`, ver [`cuenta_remunerada_fci.md`](cuenta_remunerada_fci.md)), este es un flujo de suscripción/rescate **individual, no por lotes**:
- `POST /trade/v1/fund/BUY` — "Place Subscription". Ejemplo real: `{"instrument": "ADAR-FCI.1195", "currency": "ARS", "amount": 50000, "thirdPartyId": "..."}`. Respuesta: `{"operationType": "FUND", "operationId": "..."}`.
- `POST /trade/v1/fund/SELL` — "Place Redemption" (rescate).
- `GET`/`DELETE` de la orden — consultar y cancelar, mismo patrón que Trade.

Es el mecanismo genérico de FCI de Poincenot — la Cuenta Remunerada de Bind PSP usa el flujo batch (`bundle-worker`) en su lugar, probablemente por volumen (muchos usuarios suscribiendo/rescatando el mismo fondo cada día).

## Ver también
- [api_broker_poincenot_fundamentos.md](api_broker_poincenot_fundamentos.md) — autenticación, alta de cuenta comitente, errores.
- [api_broker_poincenot_tesoreria_p2p_portfolio.md](api_broker_poincenot_tesoreria_p2p_portfolio.md) — Tesorería, P2P y Portfolio.
- [cuenta_remunerada_fci.md](cuenta_remunerada_fci.md) — flujo de negocio de la Cuenta Remunerada (FCI batch), sí en producción.

---
*Última actualización: 2026-09-29 — `/context_merge`: archivo nuevo, inventario de la superficie de Pagos/CAP/Trading/FCI genérico de la API de Poincenot, sin uso identificado hoy (Pablo Gomes).*

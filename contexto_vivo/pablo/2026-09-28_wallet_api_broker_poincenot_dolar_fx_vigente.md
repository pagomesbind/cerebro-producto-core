---
id: 2026-09-28_wallet_api_broker_poincenot_dolar_fx_vigente
pm: pablo
fecha_captura: 2026-09-28
fuente: "portal público de documentación de Poincenot (apibroker.pcnt.io), navegado en vivo con el Chrome del PM durante /idea_start de inter_fondeo_usd"
producto: wallet
tema: "API Broker (Poincenot) — Dólar FX (MULC): confirmación de que el endpoint sigue documentado como activo, y su detalle técnico (complementa dolar_fx.md)"
tipo: conocimiento
destino_propuesto: 3_recursos/detalle_productos/wallet/dolar_fx.md
tipo_destino: actualizar
contradice: "dolar_fx.md dice \"Estado: en producción\" sin verificación reciente; en la sesión de /idea_start de inter_fondeo_usd (2026-09-23/28) el PM planteó la sospecha de que Dólar FX/MULC podría estar deprecado por normativa. Este item aporta evidencia (parcial, no concluyente) de que el endpoint sigue publicado del lado de Poincenot — no confirma si Bind PSP lo sigue consumiendo activamente."
confianza: media
estado: en_cola
merge_commit:
---

## Hallazgo principal

Se revisó el portal público de documentación de Poincenot (`apibroker.pcnt.io`) el 2026-09-28, en el marco del discovery de `inter_fondeo_usd/`, donde el PM había planteado la sospecha de que Dólar FX/MULC estuviera deprecado por normativa. **El endpoint de Dólar FX sigue documentado como parte activa de la API**, con flujo completo de cotización, compra, venta y DDJJ — no aparece marcado como deprecado ni con ninguna nota de discontinuación en la documentación de Poincenot.

**Esto no es concluyente del lado de Bind PSP:** que Poincenot lo siga ofreciendo no confirma que Bind PSP lo siga consumiendo activamente hoy — podría haberse dejado de usar del lado de Bind sin que Poincenot lo haya dado de baja. Queda como pregunta para Ingeniería (ver `gaps.md` de `inter_fondeo_usd/`).

## Detalle técnico — Cotización

`GET /marketdata/v1/price/fx`:
```json
{
  "buyPrice": 1481.82, "sellPrice": 1274.23, "timestamp": "2024-08-06T08:09:02Z",
  "market": "MULC", "hash": "xwY250QG1haWxpbmF0b3IuY29tIiwib3Mi",
  "priceLimitTime": "2024-08-06T08:19:02Z", "priceLimitTimeInSeconds": "600"
}
```

Diferencia clave con la cotización de D1C (`dolar_1click_detalle`, arriba): la de FX trae **`market: "MULC"`**, y un mecanismo de **`hash` + `priceLimitTime`** (10 minutos de vigencia, `priceLimitTimeInSeconds: 600`) — el precio cotizado se referencia por hash al ejecutar la operación, similar al mecanismo `priceHash` que `dolar_ccl.md` ya documenta para el modo Combi (organizaciones `combi=true`), pero acá aplicado nativamente al circuito FX/MULC completo, no solo a Combi.

## Gastos de venta (preview) — ejemplo real

`POST /investment-operation-flow/v1/exchange/fx/preview/SELL`. Request: `{"amount": <pesos>, "priceHash": "<hash de la cotización>"}`. Response (ejemplo real):
```json
{
  "endOperationDate": "2025-05-05T12:00:00Z", "startOperationDate": "2025-05-05T12:00:00Z",
  "marketIsOpen": true, "totalExpensesCurrency": "ARS", "price": 104.07
}
```
(Análogo a D1C: gross/net/totalExpenses/taxes, con el agregado del `priceHash` obligatorio en el request.)

## Resto del flujo

Comparte la misma forma que D1C: `enter Purchase`/`enter Sale` (ejecutar la orden con `priceHash`), `Get Operation` (consultar estado), y `Query an affidavit for FX` (DDJJ propia del circuito FX/MULC, separada de la de D1C).

## Implicancia para `inter_fondeo_usd/`

No cambia la decisión de dirección tomada el 2026-09-23 (aplicar sobre **Dólar 1Click**, no sobre Dólar FX/MULC, el patrón de saldo multimoneda) — el mecanismo de negocio elegido sigue siendo D1C por decisión explícita del PM (Dólar FX/MULC operaba distinto: compra de USD con pesos vía mercado oficial, no lo que Inter necesita, que es mover USD que el usuario ya tiene). Este hallazgo solo aporta evidencia sobre el estado de vigencia del endpoint, no cambia la alternativa técnica elegida.

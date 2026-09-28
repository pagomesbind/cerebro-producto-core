---
id: 2026-09-28_wallet_api_broker_poincenot_dolar_combi_detalle
pm: pablo
fecha_captura: 2026-09-28
fuente: "portal público de documentación de Poincenot (apibroker.pcnt.io), navegado en vivo con el Chrome del PM durante /idea_start de inter_fondeo_usd — sección revisada por completitud, no es del alcance de ese proyecto"
producto: wallet
tema: "API Broker (Poincenot) — Dólar Combi: detalle técnico (complementa dolar_ccl.md §3.8, modo Combi/MOVE)"
tipo: conocimiento
destino_propuesto: 3_recursos/detalle_productos/wallet/dolar_ccl.md
tipo_destino: actualizar
contradice: "no"
confianza: alta
estado: en_cola
merge_commit:
---

## Nota de alcance

Esta sección se revisó por pedido explícito del PM de completar la ingesta de toda la API de Poincenot, pero **Dólar Combi no es del alcance del proyecto `inter_fondeo_usd/`** — el PM aclaró que Combi pertenece a otros proyectos (el modo Combi/organización MOVE de Mastercard Cross-Border, ya documentado en `dolar_ccl.md` §3.8 y `dolar_fx.md` §2.8, foco de Luciana Rudaz).

## Detalle técnico

`GET /marketdata/v1/price/usdmep` — **mismo endpoint URL que Dólar 1Click**, pero la respuesta trae los campos adicionales `hash` y `priceLimitTime`/`priceLimitTimeInSeconds` (600 segundos de vigencia):
```json
{
  "buyPrice": 1481.82, "sellPrice": 1274.23, "timestamp": "2024-08-06T08:09:02Z",
  "hash": "xwY250QG1haWxpbmF0b3IuY29tIiwib3Mi",
  "priceLimitTime": "2024-08-06T08:19:02Z", "priceLimitTimeInSeconds": "600"
}
```

Esto confirma técnicamente lo que `dolar_ccl.md` §3.8 ya documentaba de forma indirecta: Combi usa el mismo endpoint de cotización que D1C, diferenciado por el flag `combi=true` de la organización en IVSA, y el `hash`/`priceHash` como mecanismo de fijación de precio con expiración — sin caché, cada consulta va en vivo. El resto del flujo (gastos de compra/venta, ejecutar compra/venta) sigue la misma estructura que D1C, con `priceHash` obligatorio en el request de ejecución.

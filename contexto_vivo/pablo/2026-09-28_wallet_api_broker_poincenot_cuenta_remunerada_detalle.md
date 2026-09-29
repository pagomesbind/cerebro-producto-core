---
id: 2026-09-28_wallet_api_broker_poincenot_cuenta_remunerada_detalle
pm: pablo
fecha_captura: 2026-09-28
fuente: "portal público de documentación de Poincenot (apibroker.pcnt.io), navegado en vivo con el Chrome del PM durante /idea_start de inter_fondeo_usd"
producto: wallet
tema: "API Broker (Poincenot) — Cuenta Remunerada / FCI (Interest Bearing Account): endpoints de precio, suscripción/rescate batch, liquidaciones e interés ganado (complementa cuenta_remunerada_fci.md)"
tipo: conocimiento
destino_propuesto: 3_recursos/detalle_productos/wallet/cuenta_remunerada_fci.md
tipo_destino: actualizar
contradice: "no"
confianza: alta
estado: ingestado
merge_commit:
---

## Contexto

`cuenta_remunerada_fci.md` ya documenta el proceso de negocio completo (Pasos 1-7, conciliación diaria, bugs históricos). Este item agrega el **detalle de los endpoints REST reales** del lado de Poincenot para ese mismo flujo batch, que hoy solo estaba descripto en prosa ("Paso 6: envía las suscripciones y rescates por API a API Broker, armando paquetes").

## Precio del fondo — `GET /marketdata/v1/price/fund/`

```json
{ "code": "1483", "price": 1.55, "date": "2024-10-01", "currency": "USD", "class": "A" }
```
**Dato relevante: el fondo puede estar denominado en USD** (`"currency": "USD"` en el ejemplo real de la documentación) — confirma que la infraestructura de Interest Bearing Account de Poincenot ya contempla fondos en moneda extranjera, no solo en pesos. `2_areas/clientes/` (contexto de Inter, weekly Bind↔Inter del 2026-09-23) registra que "el rendimiento en USD todavía no está disponible para Inter por un acuerdo de exclusividad con el cliente principal (solo FCI en pesos vía Bind Inversiones)" — la restricción es comercial/contractual, no técnica.

## Suscripción batch — `POST /bundle-worker/v1/investment/operate/fund/bulk/SUBSCRIPTION`

Envía un paquete (`bundle`) con una o más suscripciones. Ejemplo real:
```json
{
  "datetime": "2012-11-21T03:00:00Z",
  "total": { "data_size": 1, "total_amount": "30500.30" },
  "data": [
    { "fund": "2", "account": "4652", "value": { "amount": "30500.30" },
      "third_party_information": { "id": "123", "transaction_id": "trx-1342-232SAF", "detail": "free text" } }
  ],
  "third_party_information": { "packet_id": "ewqeq_312321_3123_edewqeq", "type": "A", "description": "..." }
}
```
La respuesta solo confirma la **recepción** del paquete (no el resultado de cada suscripción individual) — coincide con lo ya documentado en `cuenta_remunerada_fci.md` Paso 6 ("API Broker solo confirma recepción, sin indicar estado definitivo todavía").

## Rescate batch — `POST /bundle-worker/v1/investment/operate/fund/bulk/WITHDRAW`

Mismo mecanismo batch, con variantes "withdrawal by amount" y "total withdrawal" (rescate total de la posición).

## Aviso de fin de envío — Finished sending notice

Endpoint que le avisa a Poincenot que terminó el envío de paquetes del día (Paso 6 final del proceso ya documentado).

## Consulta de paquete/bundle — Bundle query / Package query

Permiten consultar el estado de un paquete ya enviado por su `packet_id`.

## Webhook de fin de procesamiento — Processing finished webhook

```json
{
  "datetime": "2023-10-09T10:00:00Z",
  "funds": [{ "price": 1091.0594, "id": "2", "rejected": [...] }]
}
```
Es el webhook del Paso 7 ya documentado ("API Broker avisa por webhook que procesó cada paquete"), con el detalle de rechazos por fondo.

## Interés ganado e liquidaciones por usuario

- **`GET .../get-interest-earned-per-user`**: consulta cuánto interés ganó un usuario — endpoint distinto del `investment/settlement/info` que `cuenta_remunerada_fci.md` §… ya documenta (WS-730) para reportes normativos; puede ser el mismo concepto expuesto por dos vías, o un endpoint complementario — a confirmar si hace falta en un futuro trabajo sobre este producto.
- **`GET .../get-settlements-per-user`**: consulta las liquidaciones (suscripciones/rescates ya liquidados) de un usuario.

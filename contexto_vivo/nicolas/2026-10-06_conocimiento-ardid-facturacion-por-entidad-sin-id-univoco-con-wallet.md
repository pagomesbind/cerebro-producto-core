---
id: 2026-10-06_conocimiento-ardid-facturacion-por-entidad-sin-id-univoco-con-wallet
pm: nicolas
fecha_captura: 2026-10-06
fuente: "Mail 'Dolor en facturación de ARDID - COTO' — Gonzalo Rivera, 2026-10-05"
producto: ardid
tema: Facturación de Ardid por entidad (caso COTO) — no hay un ID único que persista entre Ardid y Wallet, y el cruce depende del tipo de operación
tipo: conocimiento
destino_propuesto: 3_recursos/detalle_productos/ardid/integracion_con_productos_bind.md
tipo_destino: actualizar
contradice: "no"
confianza: alta
estado: en_cola
---

**Cómo se factura hoy Ardid a una entidad.** Cada mes Rocío Revelli le manda a la entidad (caso COTO, entidad **4845**) el listado de transacciones que pasaron por Ardid y que se le facturan. El archivo de agosto 2026 lo adjunta Gonzalo Rivera (`Facturación Agosto COTO.xlsx`, pestañas "Agosto 4845" y "Wallet Agosto Coto"; no descargado).

**El problema.** Es difícil cruzar con certeza las transacciones que se le cobran por Ardid con lo que efectivamente registran las bases transaccionales de Wallet, porque **no hay un ID ni un valor único que persista en todas las bases**. Hoy la única forma es cruzar la columna F del listado de Ardid con un campo distinto de Wallet según el tipo de operación:

| Tipo de operación | Campo de Wallet con el que se cruza |
|---|---|
| Transferencia saliente externa | Id de operación de Wallet |
| Transferencia entrante externa | `ArdidTransactionId` de Wallet |
| QR entrante | **No se puede cruzar** |
| Rechazada por Ardid | **No se puede cruzar**: no se genera operación en Wallet |

**Alcance.** Gonzalo Rivera lo plantea como un punto que había quedado pendiente y que va a afectar también a las próximas entidades que se facturen igual. El mail va a los 3 PM, con copia a Rocío Revelli, Mariana Nadalin y Emma Vignoles.

**Relación con otros temas.** Ardid guarda 45 días de datos (ver `2026-10-06_conocimiento-ardid-consumo-de-datos-vistas-ventana-45-dias-e-historico`). Las rechazadas por Ardid no dejan rastro en Wallet, que es justo la población que también quiere ver el equipo de fraude de Credicuotas.

> Fuente: Mail "Dolor en facturación de ARDID - COTO" — Gonzalo Rivera (2026-10-05).

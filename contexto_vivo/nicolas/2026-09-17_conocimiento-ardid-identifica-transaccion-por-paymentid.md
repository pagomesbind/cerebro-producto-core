---
id: 2026-09-17_conocimiento-ardid-identifica-transaccion-por-paymentid
pm: nicolas
fecha_captura: 2026-09-17
fuente: "Sesión /idea_solution sobre ardid_desconocimientos, aporte directo del PM (2026-09-17)"
producto: ardid
tema: Para informar un contracargo, Ardid identifica la transacción por el PaymentId de Botón Simple, no por el ID interno de Cobro
tipo: conocimiento
destino_propuesto: 3_recursos/detalle_productos/ardid/integracion_con_productos_bind.md
tipo_destino: actualizar
contradice: "no"
confianza: alta
estado: ingestado
merge_commit: f460705
---

Al diseñar cómo informarle a Ardid que una transacción de Botón Simple tuvo un contracargo tipo "desconocimiento" (`POST /api/FilProcess/Process`, campo `transactionId`), surgió una precisión importante que no estaba explícita en el resto de la integración ya documentada: **el identificador que Ardid espera no es el `transaccionId` interno del sistema de Cobro** (el que aparece, por ejemplo, en el request del endpoint de refund/contracargo) — **es el identificador con el que Ardid ya conoce esa transacción desde que se la analizó por primera vez** (llamada original a `/Transaction`/`Analyze`).

Para el canal Botón Simple, ese identificador es el `PaymentId` (el id del link de pago) — consistente con lo ya documentado en el catálogo de webhooks de contracargo, donde `IdentificadorOrdenVenta` "para Botón simple es el PaymentId (id del link de pago)".

**Implicación práctica para cualquier integración futura que necesite referenciar ante Ardid una transacción ya analizada:** no alcanza con el ID interno de Cobro/liquidación — hay que resolver primero el `PaymentId` (u otro identificador equivalente según el canal, ver la misma tabla de `IdentificadorOrdenVenta`/`IdOrdenVentaQR` ya documentada) antes de armar el llamado a Ardid. El mecanismo exacto para resolver ese identificador a partir de los datos que circulan en el flujo de contracargos (`deudaId`/`transaccionId`) quedó delegado al equipo de desarrollo tercerizado como detalle de implementación — no se relevó en esta sesión.

---
id: 2026-08-15_wallet_ccl_bugs_w71
pm: pablo
fecha_captura: 2026-08-15
fuente: "/sync_releases — Jira bindpsp.atlassian.net, versión W 71 (publicada 2026-07-15), tickets WS-1217, WS-1427, WS-1285 (W 71.4 FIX, publicada 2026-07-30)"
producto: wallet
tema: Dólar CCL — correcciones al flujo de venta y almacenamiento de comprobantes
tipo: conocimiento
destino_propuesto: 3_recursos/detalle_productos/wallet/dolar_ccl.md
tipo_destino: actualizar
contradice: "no"
confianza: alta
estado: ingestado
merge_commit:
---

Ampliar §3.6 "Bugs y aprendizajes reales (llegaron a producción)" con 3 correcciones nuevas sobre el flujo de Dólar CCL, dos de ellas específicas a **venta** (hasta ahora la sección documenta sobre todo bugs de compra):

- **Interpretación de webhooks Poincenot con estado `ERROR` (WS-1217, W 71):** Poincenot (proveedor) tiene un bug recurrente — operaciones rechazadas de su lado a veces devuelven `GENERAL_ERROR` genérico al consultarlas en vez de la info real de rechazo. Poincenot confirmó que el estado que viaja en los webhooks "Pata 1"/"Pata 2" es el fehaciente. Nueva lógica: si el WH Pata 1 de **compra** viene `ERROR` y la consulta posterior da `GENERAL_ERROR` → rechazar, devolver fondos, avisar por webhook a la organización. Si es el WH Pata 2 de compra → mantener el flujo actual (queda en "Auditar", intervención operativa, porque si ocurrió Pata 2 ya se compró el bono). Si es el WH Pata 1 de **venta** (no existe Pata 2 en ventas) → rechazar y avisar por webhook.
- **Orden de comprobantes en venta corregido (WS-1217):** antes se debitaba primero el cargo de comisión (exigiendo saldo disponible del cliente) y recién después se acreditaba el monto obtenido — invertido: ahora primero se acredita `montoObtenido`, después se debita el cargo.
- **Fórmula de comisión de venta corregida (WS-1217):** pasa de `monto × precioDolar × porcentajeCargo` a `totalObtained × porcentajeCargo` (bug introducido entre el 2026-02-02 y el 2026-02-10, sin ticket propio). También se corrige `montoObtenido` para que sea `totalObtained − ComisionInterna` (lo que el cliente ve acreditado), no el bruto.
- **`MontoObtenido` no se actualizaba si la compra se resolvía el mismo día (WS-1427, W 71.4 FIX):** cuando una compra de dólar CCL pasaba PENDING → APPROVED → EXCHANGED en el día, el campo `MontoObtenido` (tabla `dbo.Intenciones`) no se pisaba con el `totalObtained` real — el cliente no podía saber cuánto obtuvo. Fix: pisar siempre que el estado obtenido en Poincenot sea `EXCHANGED`, sin importar cuándo ocurra ni por qué mecanismo (webhook o reintento automático); nunca pisar en estado `APPROVED` intermedio.
- **Reubicación de IDs de comprobante de cargo (WS-1285, W 71.4 FIX):** los IDs de comprobantes de cargo se guardaban en campos con nombres contraintuitivos. Ahora: cargos debitados (compra o venta) → campo `CargoDebitoComprobanteId`, expuesto como `cargoDebitoComprobanteId` en `GET Intencion` y en `POST EjecutarCompraCCL`. Cargos acreditados por devolución de error en compra → campo `CargoCreditoComprobanteId`, expuesto como `cargoCreditoComprobanteId` en los mismos endpoints.

---
id: 2026-09-24_agente_cobros_y_pagos_conocimiento_reversas_liquidacion_y_bug_doble_descuento
pm: pablo
fecha_captura: 2026-09-24
fuente: "/sync_meetings — reunión 'Análisis COBRO' (2026-09-24, 12:01, minuta Gemini, docId 1yHLVGw5y2gBGS9pfRN5_Qjv9WPNA9nCJEHArKNs1LyY)"
producto: agente_cobros_y_pagos
tema: mecánica de reversas/aranceles en liquidaciones, y bug de doble descuento por devolución previa a liquidación
tipo: conocimiento
destino_propuesto: 3_recursos/detalle_productos/agente_cobros_y_pagos/liquidaciones_reversas_y_comprobantes.md
tipo_destino: crear
contradice: "no"
confianza: alta
estado: ingestado
merge_commit: 2bc1252
---

**Regeneración de comprobantes de liquidación (Swagger):** Daniela Collia (Fintexa) confirma que hoy se puede regenerar una liquidación ya emitida usando Swagger — la operación **sobrescribe el registro y el comprobante PDF sin dejar versión anterior ni constancia de autoría** (quién la regeneró, cuándo, por qué). Nicolás Colón y Daniela Collia coinciden en que un control de versiones sería complejo de implementar; queda a evaluar la viabilidad técnica.

**Decisión operativa — Opción A para reversas fuera de plazo (ticket 3400/1791):** cuando una liquidación se re-ejecuta con transacciones revertidas después de su fecha de plazo, el comprobante actual descuenta el bruto y la comisión del total, pero **la reversa no aparece en ese comprobante sino en un ciclo posterior** — rompiendo la trazabilidad para quien lo lee. De las 3 opciones evaluadas (A/B/C), se **acordó la Opción A**: reflejar la venta como acreditada en su comprobante original, y la reversa en el ciclo siguiente (mantiene el estado histórico de cada comprobante fiel al momento de la transacción original, en vez de "corregir" retroactivamente comprobantes ya emitidos).

**Aranceles en devoluciones parciales — confirmado por Pablo Gomes, pendiente de validar con recaudaciones (ticket 1835):** ante una devolución parcial de una transacción, el arancel completo se muestra repetido en cada línea de devolución. Pablo Gomes afirma que **el arancel no debe devolverse ni prorratearse**, porque el proceso de cobro de la transacción ya se ejecutó por completo — el comportamiento actual (mostrar el arancel completo, no prorratearlo) sería correcto en el fondo, pero Nicolás Colón señala que el cálculo actual parece **restar la comisión del total a liquidar de forma incorrecta** en devoluciones parciales. Se acordó verificar el comportamiento real con el equipo de recaudaciones antes de tocar nada (evitar modificar un comportamiento no deseado sin evidencia).

**Bug — doble descuento en venta devuelta antes de liquidarse (ticket 1822):** cuando una venta se devuelve **antes** de haber sido liquidada, la venta en sí no llega a sumarse a la liquidación (correcto, nunca se liquidó), pero **su devolución sí se descuenta igual** — generando un doble descuento neto sobre el total a liquidar. Nicolás Colón y Daniela Collia lo dejan pendiente de análisis técnico.

**Ausencia de columna para "desconocimientos" (chargebacks) en el registro de liquidación:** a diferencia de las devoluciones de comercio, hoy el registro de cada liquidación **no guarda en ningún campo específico** el total ni la cantidad de transacciones desconocidas (chargebacks). Nicolás Colón evalúa agregar columnas separadas para total y cantidad de desconocimientos, mediante consulta previa a "Euge" sobre si afecta procesos existentes — sin resolver todavía, aplazado.

> Fuente: reunión "Análisis COBRO" (2026-09-24, 12:01 GMT-03:00), con Daniela Collia, Melisa Belpassi, Flavia Salmerón y equipo Fintexa; Nicolás Colón y Pablo Gomes por Bind PSP.

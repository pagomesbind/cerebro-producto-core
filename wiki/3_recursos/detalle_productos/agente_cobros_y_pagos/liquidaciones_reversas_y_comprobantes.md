# Liquidaciones — Reversas, Aranceles y Comprobantes

> Estado: en producción, con varios puntos en discusión/pendientes de resolución técnica (ver cada sección). Fuente: reunión "Análisis COBRO" (2026-09-24, 12:01, minuta Gemini), con Daniela Collia, Melisa Belpassi, Flavia Salmerón (Fintexa) y Nicolás Colón/Pablo Gomes (Bind PSP).

## 1. Regeneración de comprobantes de liquidación (Swagger)

Daniela Collia (Fintexa) confirma que hoy se puede regenerar una liquidación ya emitida usando Swagger — la operación **sobrescribe el registro y el comprobante PDF sin dejar versión anterior ni constancia de autoría** (quién la regeneró, cuándo, por qué). Nicolás Colón y Daniela Collia coinciden en que un control de versiones sería complejo de implementar; queda a evaluar la viabilidad técnica.

## 2. Reversas fuera de plazo — Opción A adoptada (ticket 3400/1791)

Cuando una liquidación se re-ejecuta con transacciones revertidas después de su fecha de plazo, el comprobante actual descuenta el bruto y la comisión del total, pero **la reversa no aparece en ese comprobante sino en un ciclo posterior** — rompiendo la trazabilidad para quien lo lee. De 3 opciones evaluadas (A/B/C), se **acordó la Opción A**: reflejar la venta como acreditada en su comprobante original, y la reversa en el ciclo siguiente (mantiene el estado histórico de cada comprobante fiel al momento de la transacción original, en vez de "corregir" retroactivamente comprobantes ya emitidos).

## 3. Aranceles en devoluciones parciales (ticket 1835, pendiente de validar con recaudaciones)

Ante una devolución parcial de una transacción, el arancel completo se muestra repetido en cada línea de devolución. Pablo Gomes afirma que **el arancel no debe devolverse ni prorratearse**, porque el proceso de cobro de la transacción ya se ejecutó por completo — el comportamiento actual (mostrar el arancel completo, no prorratearlo) sería correcto en el fondo, pero Nicolás Colón señala que el cálculo actual parece **restar la comisión del total a liquidar de forma incorrecta** en devoluciones parciales. Se acordó verificar el comportamiento real con el equipo de recaudaciones antes de tocar nada (evitar modificar un comportamiento no deseado sin evidencia).

## 4. Bug — doble descuento en venta devuelta antes de liquidarse (ticket 1822)

Cuando una venta se devuelve **antes** de haber sido liquidada, la venta en sí no llega a sumarse a la liquidación (correcto, nunca se liquidó), pero **su devolución sí se descuenta igual** — generando un doble descuento neto sobre el total a liquidar. Nicolás Colón y Daniela Collia lo dejan pendiente de análisis técnico.

## 5. Ausencia de columna para "desconocimientos" (chargebacks) en el registro de liquidación

A diferencia de las devoluciones de comercio, hoy el registro de cada liquidación **no guarda en ningún campo específico** el total ni la cantidad de transacciones desconocidas (chargebacks). Nicolás Colón evalúa agregar columnas separadas para total y cantidad de desconocimientos, mediante consulta previa a "Euge" sobre si afecta procesos existentes — sin resolver todavía, aplazado.

## Ver también
- [devoluciones_y_contracargos.md](devoluciones_y_contracargos.md) — bug de contracargos de colectores (Pago Fácil) rechazados por validación incorrecta de ID de caja vs. ID de colector — mecanismo distinto al de este archivo.
- [pedidos_de_clientes_y_hallazgos_operativos.md](pedidos_de_clientes_y_hallazgos_operativos.md) — otros hallazgos operativos del producto.

---
*Última actualización: 2026-09-25 — `/context_merge`: archivo nuevo, a partir de la reunión "Análisis COBRO" (2026-09-24) — mecánica de reversas/aranceles en liquidaciones y 2 bugs abiertos (doble descuento, ausencia de columna de desconocimientos).*

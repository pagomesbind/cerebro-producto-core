# Liquidaciones — Reversas, Aranceles y Comprobantes

> Estado: en producción. Fuente: reunión "Análisis COBRO" (2026-09-24, minuta Gemini) y, para el cierre de definiciones, mail "Liquidaciones AD 73 – Estado de observaciones, propuesta de registro y confirmaciones pendientes" (Melisa Belpassi/Fintexa ↔ Pablo Gomes, 2026-09-25). **Estas definiciones son las mismas que resuelven las observaciones equivalentes de Botón/Cobro para AD V73** — ver [`adquirencia/desconocimientos_de_tarjeta.md`](../adquirencia/desconocimientos_de_tarjeta.md) y [`adquirencia/devoluciones_y_contracargos.md`](../adquirencia/devoluciones_y_contracargos.md), mismo motor de liquidaciones compartido entre ambos productos.

## 1. Regeneración de comprobantes de liquidación (Swagger)

Daniela Collia (Fintexa) confirma que hoy se puede regenerar una liquidación ya emitida usando Swagger — la operación **sobrescribe el registro y el comprobante PDF sin dejar versión anterior ni constancia de autoría** (quién la regeneró, cuándo, por qué). Nicolás Colón y Daniela Collia coinciden en que un control de versiones sería complejo de implementar; queda a evaluar la viabilidad técnica.

## 2. Reversas fuera de plazo — reglas confirmadas (AD-1791/DAD-3400, caso real liq. 31128)

> Fuente: mail "Liquidaciones AD 73" — Melisa Belpassi (Fintexa, 2026-09-25) y respuesta de Pablo Gomes el mismo día.

**Causa raíz:** al regenerar una liquidación ya emitida 3 días después (caso real: liq. 31128), dos ventas ya tenían reversas posteriores a su fecha de plazo. El sistema toma el estado actual de las ventas (descuenta su importe del total) pero no informaba la reversa en ningún apartado — el comportamiento de regenerar una liquidación emitida nunca había estado definido.

**Reglas confirmadas (reemplazan la "Opción A" descripta antes — mismo espíritu, ahora con las 3 reglas completas):**
- **a) Clasificación por fecha:** el comprobante clasifica cada venta según la fecha de su reversa respecto de su fecha de plazo, no según el estado actual de la venta. Una venta revertida después del plazo sigue figurando como acreditada en esa liquidación, y su reversa se informa en el ciclo siguiente — así, **regenerar una liquidación siempre da el mismo resultado**.
- **b) Cierre del total:** el total a liquidar siempre coincide con ventas − devoluciones − desconocimientos (criterio de verificación de QA).
- **c) Registro de la liquidación:** el campo de devoluciones del registro vuelve a guardar la **suma de devoluciones + desconocimientos** en un único campo, como antes de la separación — reemplaza la "Opción B" de campos separados (se había elegido antes, pero requería scripts de base de datos y más tiempo). **En el PDF se mantiene la separación en dos columnas.** Efecto colateral: la columna "Devoluciones" del Admin vuelve a incluir los desconocimientos, así que "Liq. Total − Devoluciones" vuelve a coincidir con el "Total a Liquidar" mientras el Admin no tenga columna propia de Desconocimientos.
- Se mantiene: la venta pasa a `DEVUELTA` cuando se acepta la reversa, y regenerar una liquidación sigue permitido. Estas reglas no cambian aranceles ni impuestos.

**No bloqueante para el pase de V73 (martes 29/09).**

## 3. Regla de deducciones (arancel, IVA, impuestos) en reversas — CONFIRMADA, corrige la nota anterior

> Fuente: mail "Liquidaciones AD 73", pregunta 3.2 de Melisa Belpassi y respuesta de Pablo Gomes, 2026-09-25.

**Corrección respecto de la nota anterior (2026-09-24):** acá se había registrado que Pablo Gomes opinaba, sin validar todavía, que "el arancel no debe devolverse ni prorratearse" en ninguna devolución parcial. Fintexa preguntó explícitamente cuál era la regla vigente "validada con Impuestos", porque circulaban dos versiones: (1) "los aranceles no se devuelven nunca" y (2) la regla de abajo. La regla nunca había estado definida en los tickets de liquidaciones (AD-1361/AD-1398) — la respuesta de Pablo Gomes del 25/09 es más específica que la nota anterior:

**Regla confirmada: los aranceles e impuestos se devuelven solo si la reversa es TOTAL y ocurre el MISMO DÍA del cobro.** En cualquier reversa parcial, o en una reversa total de otro día, **no se devuelve nada** (ni arancel ni impuestos).

**Estado actual no respeta la regla:** hoy el comprobante de liquidación devuelve arancel e IVA en **cada** reversa (no solo en la total del mismo día) — Fintexa propuso corregirlo en un ticket aparte, que tiene que crear Bind. Esta misma regla es el criterio que resuelve la observación de "arancel completo repetido en cada línea de devoluciones parciales" (ticket AD-1835/DAD-3418, antes anotado acá como "pendiente de validar con recaudaciones").

**Riesgo aceptado explícitamente:** en las devoluciones parciales del mismo día del cobro, el usuario no recibe de vuelta el arancel/impuesto proporcional a esa porción. Se acepta "como hacemos desde siempre" por dos motivos: el bajo volumen de estos casos, y que devolverlos obligaría a eliminar todo el impuesto en SISCRI y mandar a recalcularlo por el importe parcial acumulado — complejo de gestionar en el sistema.

**Confianza media en la validación formal:** Pablo Gomes respondió "Aceptable" sin mencionar una validación formal con Impuestos/Recaudaciones, que era lo que pedía Fintexa (ver `1_proyectos/tareas.md` T-072 de Nicolás Colón, validación pendiente).

## 4. Bug — doble descuento en venta devuelta antes de liquidarse (AD-1822/DAD-3419) — CONFIRMADO, bloqueante para V73

Confirmado como **defecto puro** sobre un comportamiento ya definido en AD-1361/DAD-2209 (el PDF y el registro deben mostrar la transacción y su reversa, igual que el BOTONLIQ del mismo día) — no requiere nueva definición de negocio, se corrige directo. **Pablo Gomes lo definió como bloqueante para el pase de V73 (martes 29/09)** — según Fintexa, para verificarlo tiene que correr el ciclo diario de liquidación, dejando poco margen entre el fix y el pase.

## 5. Ausencia de columna para "desconocimientos" (chargebacks) en el registro de liquidación (AD-1837/DAD-3425) — resuelto dentro de AD-1791

El registro se resuelve dentro de la regla c) de la §2 de arriba — Pablo Gomes confirmó cerrar esta parte ahí. La pantalla **Admin → Liquidaciones** (columna Desconocimientos, nunca pedida en ningún ticket de liquidaciones original) se convierte en una **historia de usuario nueva**, no bloqueante — mientras tanto, con la regla c), la columna Devoluciones del Admin vuelve a incluir los desconocimientos.

## Ver también
- [devoluciones_y_contracargos.md](devoluciones_y_contracargos.md) — bug de contracargos de colectores (Pago Fácil) rechazados por validación incorrecta de ID de caja vs. ID de colector — mecanismo distinto al de este archivo.
- [pedidos_de_clientes_y_hallazgos_operativos.md](pedidos_de_clientes_y_hallazgos_operativos.md) — otros hallazgos operativos del producto.
- [`adquirencia/desconocimientos_de_tarjeta.md`](../adquirencia/desconocimientos_de_tarjeta.md) y [`adquirencia/devoluciones_y_contracargos.md`](../adquirencia/devoluciones_y_contracargos.md) — mismas definiciones de AD V73, versión Botón/Cobro (Adquirencia).

---
*Última actualización: 2026-09-29 — `/context_merge`: §2-5 — reglas confirmadas por Fintexa/Pablo Gomes (mail "Liquidaciones AD 73", 2026-09-25): clasificación por fecha al regenerar, regla de deducciones de arancel/impuestos (corrige la nota anterior, ya no es solo opinión de Pablo Gomes sin validar), AD-1822 confirmado bloqueante para V73, registro de desconocimientos resuelto dentro de AD-1791.*
*Última actualización anterior: 2026-09-25 — `/context_merge`: archivo nuevo, a partir de la reunión "Análisis COBRO" (2026-09-24) — mecánica de reversas/aranceles en liquidaciones y 2 bugs abiertos (doble descuento, ausencia de columna de desconocimientos).*

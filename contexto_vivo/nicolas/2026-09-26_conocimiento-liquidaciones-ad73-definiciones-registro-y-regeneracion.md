---
id: 2026-09-26_conocimiento-liquidaciones-ad73-definiciones-registro-y-regeneracion
pm: nicolas
fecha_captura: 2026-09-26
fuente: "Mail 'Liquidaciones AD 73 – Estado de observaciones, propuesta de registro y confirmaciones pendientes' — melisa.belpassi@fintexa.tech (2026-09-25 14:39) + respuesta de pagomes@bind.com.ar (Pablo Gomes, 2026-09-25 15:13) + OK de Fintexa (15:17)"
producto: adquirencia
tema: Liquidaciones de Botón/Cobro en AD V73 — observaciones de QA de AD-1361/AD-1398, reglas nuevas de clasificación por fecha al regenerar, registro de liquidación con devoluciones+desconocimientos sumados, qué bloquea el pase
tipo: conocimiento
destino_propuesto: 3_recursos/detalle_productos/adquirencia/desconocimientos_de_tarjeta.md
tipo_destino: actualizar
contradice: "no — extiende la sección 'Separación de desconocimientos y devoluciones en PDF y liquidación — confirmada para AD V73'. Matiz para el merge: la separación se mantiene en el PDF, pero el REGISTRO de liquidación (base de datos/Admin) vuelve a guardar devoluciones + desconocimientos sumados en un solo campo (se descartó la 'opción B' de campos separados)."
confianza: alta
estado: en_cola
---

En las pruebas de QA de **AD-1361 / DAD-2209** ("[Cobro] Corregir archivos y registros de liquidaciones") y **AD-1398 / DAD-2257** ("[Cobro] Separar desconocimientos de devoluciones en el PDF de liquidación") se levantaron observaciones. Son las historias que implementan en AD V73 la separación entre desconocimiento y devolución. El 25/09, Fintexa (Melisa Belpassi, PM) consolidó el estado, incluido lo conversado en el refinamiento del 24/09. Pablo Gomes respondió por Bind ese mismo día, porque Nicolás estaba de licencia, y Fintexa confirmó que avanza con esas definiciones.

**Observaciones y su resolución:**

| Ticket (Bind / Fintexa) | Problema | Diagnóstico | Resolución |
|---|---|---|---|
| AD-1822 / DAD-3419 | Una venta devuelta **antes** de liquidarse no suma en la liquidación, pero su devolución sí se descuenta | Es un defecto: el comportamiento esperado ya estaba definido en AD-1361 (el PDF y el registro deben mostrar la transacción y su reversa, igual que el BOTONLIQ del mismo día) | Se corrige como defecto. Pablo Gomes la definió como **bloqueante para el pase de AD V73** |
| AD-1791 / DAD-3400 | El total a liquidar no descuenta bien cuando hay devoluciones y desconocimientos en la misma liquidación (caso liq. 31128) | La liquidación se **regeneró** 3 días después de emitida, cuando dos ventas ya tenían reversas posteriores a su fecha de plazo. Al regenerar, el sistema toma el estado actual de las ventas: descuenta su importe, pero no informa las reversas en ningún apartado. Nunca se había definido qué hacer al regenerar | Reglas nuevas (ver abajo). **No bloqueante** |
| AD-1835 / DAD-3418 | En devoluciones parciales de una misma transacción, cada línea muestra el arancel completo | El criterio para repartir el arancel entre reversas nunca se definió | Lo resuelve la regla de deducciones en reversas (ver item `2026-09-26_conocimiento-regla-deducciones-arancel-impuestos-en-reversas`) |
| AD-1837 / DAD-3425 | Los desconocimientos no quedan registrados ni se muestran por separado en la liquidación | El registro se resuelve dentro de AD-1791. Para la pantalla Admin → Liquidaciones (columna Desconocimientos), Fintexa dice que no estaba en ningún ticket. Pablo Gomes aclara que **sí se había pedido** en la US original (columnas por desconocimientos en la tabla Liquidaciones), así que esa parte es en rigor un bug | Pablo la **convirtió a tipo US**, que agrupa todo, incluida la parte del Admin. **No bloqueante** |
| DAD-3383 | DEVBOTON vuelve a informar contracargos ya informados cuando llega uno nuevo sobre la misma transacción | — | Ya corregida, en QA |

**Reglas nuevas que definen el alcance del fix de AD-1791 (aprobadas):**
- **a) Clasificación por fecha (opción A, indicada por Nicolás Colón):** el comprobante clasifica cada venta según la **fecha de su reversa comparada con su fecha de plazo**, no según el estado actual de la venta. Una venta revertida después del plazo **sigue figurando como acreditada** en esa liquidación, y su reversa se informa en el **ciclo siguiente**. Así, **regenerar una liquidación siempre da el mismo resultado**.
- **b) Cierre del total:** el total a liquidar siempre coincide con el resumen: **ventas − devoluciones − desconocimientos**. QA lo usa como criterio de verificación.
- **c) Registro de liquidación:** el campo de devoluciones del registro **vuelve a guardar la suma de devoluciones + desconocimientos**, como antes de la separación. Esto reemplaza la "opción B" que se había elegido (campos separados para desconocimientos), que se descartó porque requería scripts de base de datos y más tiempo. **En el PDF se mantiene la separación en dos columnas** de AD-1398. Efecto colateral: la columna "Devoluciones" del Admin vuelve a incluir los desconocimientos, así que "Liq. Total − Devoluciones" vuelve a coincidir con el "Total a Liquidar" mientras el Admin no tenga la columna Desconocimientos.
- **Se mantiene:** la venta pasa a `DEVUELTA` cuando se acepta la reversa, y regenerar una liquidación sigue permitido. Estas reglas no cambian aranceles ni impuestos.

**Otros compromisos del hilo:** Fintexa va a escribir **documentación funcional del flujo de desconocimientos**, que hasta ahora no existía. Bind tiene que crear el ticket de la regla de deducciones.

**Riesgo para el pase (martes 29/09):** AD-1822 es bloqueante y, según Fintexa, **para verificarla tiene que correr el ciclo diario de liquidación**, así que queda poco margen entre el fix y el pase. El mail de Fintexa habla del "pasaje previsto para el martes". Eso refuerza la fecha del martes 29/09 frente al lunes 28/09 que aparecía en el borrador de aviso a clientes (ver item en cola `2026-09-25_conocimiento-v73-adquirencia-y-wallet-reprogramadas`).

> Fuente: Mail "Liquidaciones AD 73 – Estado de observaciones, propuesta de registro y confirmaciones pendientes" — Melisa Belpassi (Fintexa, 2026-09-25) y respuesta de Pablo Gomes (Bind, 2026-09-25).

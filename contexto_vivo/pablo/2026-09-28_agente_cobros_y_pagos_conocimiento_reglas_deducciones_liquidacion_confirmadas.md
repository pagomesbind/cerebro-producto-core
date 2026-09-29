---
id: 2026-09-28_agente_cobros_y_pagos_conocimiento_reglas_deducciones_liquidacion_confirmadas
pm: pablo
fecha_captura: 2026-09-28
fuente: "/sync_mails — mail 'Liquidaciones AD 73 – Estado de observaciones, propuesta de registro y confirmaciones pendientes', Melisa Belpassi (Fintexa) ↔ Pablo Gomes, 2026-09-25 (threadId 1a0d9a65ba0ad0b1)"
producto: agente_cobros_y_pagos
tema: reglas de negocio confirmadas para el fix de liquidaciones de la V73 (AD-1791/AD-1822/AD-1835/AD-1837) — corrige y completa lo capturado el 2026-09-24 sobre la misma mecánica
tipo: conocimiento
destino_propuesto: 3_recursos/detalle_productos/agente_cobros_y_pagos/liquidaciones_reversas_y_comprobantes.md
tipo_destino: actualizar
contradice: "sí — corrige la regla de aranceles del item ya mergeado el 2026-09-24 (`2026-09-24_agente_cobros_y_pagos_conocimiento_reversas_liquidacion_y_bug_doble_descuento`, hoy en `liquidaciones_reversas_y_comprobantes.md`): allí Pablo Gomes opinaba, sin validar todavía, que el arancel 'no debe devolverse ni prorratearse' en ninguna devolución parcial. La regla formalmente confirmada el 2026-09-25 (misma persona, Pablo Gomes, respondiendo a Fintexa) es más específica: los aranceles e impuestos SÍ se devuelven, pero solo cuando la reversa es TOTAL y ocurre el MISMO DÍA del cobro; en cualquier reversa parcial, o en una reversa total de otro día, no se devuelve nada."
confianza: alta
estado: ingestado
---

Fintexa (Melisa Belpassi) resumió el estado de 4 observaciones de liquidaciones abiertas desde las pruebas de AD-1361/AD-1398, y Pablo Gomes confirmó las 3 definiciones pendientes el mismo día (25/09), destrabando el fix para el pasaje de V73 (martes 29/09).

## Por observación

**AD-1822 / DAD-3419 — venta devuelta antes de liquidarse (doble descuento):** confirmado como **defecto puro** sobre un comportamiento ya definido en AD-1361/DAD-2209 (el PDF y el registro deben mostrar la transacción y su reversa, igual que el BOTONLIQ del mismo día) — no requiere nueva definición de negocio, se corrige directo. **Es bloqueante para el pase de V73.**

**AD-1791 / DAD-3400 — el total a liquidar no descuenta correctamente cuando hay devoluciones y desconocimiento en la misma liquidación (caso real: liq. 31128):** causa raíz — al regenerar una liquidación ya emitida, el sistema toma el estado actual de las ventas (descuenta su importe del total) pero no informa la reversa en ningún apartado, porque el comportamiento de regenerar una liquidación emitida nunca estuvo definido. **Propuesta confirmada (reemplaza la Opción B de campos separados que se había tomado antes):**
- a) Clasificación por fecha: el comprobante clasifica cada venta según la fecha de su reversa respecto de su fecha de plazo, no según el estado actual — una venta revertida después del plazo sigue figurando como acreditada en su comprobante original, y su reversa se informa en el ciclo siguiente (regenerar una liquidación da siempre el mismo resultado).
- b) El total a liquidar siempre coincide con ventas − devoluciones − desconocimientos (criterio de verificación de QA).
- c) **Registro de la liquidación:** el campo de devoluciones vuelve a guardar la suma de las dos columnas de reversas (devoluciones + desconocimientos) en un único campo, como antes de la separación — es el fix más rápido, sin scripts de base de datos. En el **PDF** se mantiene la separación en dos columnas (de AD-1398).
No es bloqueante para V73, queda para la próxima versión.

**AD-1835 / DAD-3418 — devoluciones parciales de una misma transacción muestran el arancel completo en cada línea:** depende de la regla de deducciones (ver abajo). No es bloqueante, queda para la próxima versión.

**AD-1837 / DAD-3425 — los desconocimientos no quedan registrados ni se muestran por separado en la liquidación:** el registro se resuelve dentro de AD-1791 (punto c) — Pablo Gomes confirmó cerrar esta parte ahí. La parte de pantalla **Admin → Liquidaciones** (columna Desconocimientos, nunca pedida en ningún ticket de liquidaciones original) se convierte en una **historia de usuario nueva**, no bloqueante — mientras tanto, con la propuesta del punto c), la columna Devoluciones del Admin vuelve a incluir los desconocimientos.

## Regla de deducciones en reversas (arancel, IVA, impuestos) — CONFIRMADA

Pablo Gomes confirmó la regla vigente (validada él mismo, sin escalar a Impuestos por bajo volumen de la casuística): **los aranceles e impuestos se devuelven solo si la reversa es TOTAL y ocurre el MISMO DÍA del cobro.** En cualquier reversa parcial, o en una reversa total de otro día, **no se devuelve nada.**

Riesgo aceptado explícitamente: en una devolución parcial del mismo día de cobro, el usuario no recibe de vuelta el arancel/impuesto proporcional a esa porción — evitar esto implicaría eliminar todo el impuesto en SISCRI y recalcularlo de nuevo por el importe acumulado parcial, gestión que el equipo considera demasiado compleja para el volumen de casos que representa.

## Carácter bloqueante para el pase de V73 (martes 29/09)

Confirmado por Pablo Gomes: **AD-1822 sí es bloqueante; AD-1791 no es bloqueante.** (AD-1835/AD-1837 tampoco, por transitividad — dependen de AD-1791/de la regla de deducciones, ambas ya resueltas para la próxima versión).

> Fuente: mail "Liquidaciones AD 73 – Estado de observaciones, propuesta de registro y confirmaciones pendientes", Melisa Belpassi (Fintexa) → Pablo Gomes et al., 2026-09-25 17:39, con respuesta de Pablo Gomes el mismo día 18:13 (threadId `1a0d9a65ba0ad0b1`); consistente con el informe semanal de Adquirencia del mismo día (mail "RE: Informe Semanal Adquirencia", 2026-09-25).

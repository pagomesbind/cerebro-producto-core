---
id: 2026-10-05_agente_cobros_y_pagos_regla_arancel_iva_cero_sin_devolucion
pm: pablo
fecha_captura: 2026-10-05
fuente: "/sync_meetings — reunión 'Análisis COBRO', 2026-10-05 12:01, minuta Gemini (propia)"
producto: agente_cobros_y_pagos
tema: regla de arancel/IVA en cero en el archivo de liquidación cuando no hay devolución
tipo: conocimiento
destino_propuesto: 3_recursos/detalle_productos/agente_cobros_y_pagos/liquidaciones_reversas_y_comprobantes.md
tipo_destino: actualizar
contradice: "no"
confianza: alta
estado: en_cola
merge_commit:
---

**Regla de negocio acordada (reunión "Análisis COBRO", 2026-10-05, con Fintexa):** en el archivo de liquidación, cuando una transacción **no tiene ninguna devolución ni desconocimiento asociado**, las columnas de arancel e IVA deben informarse en **cero** (en vez de con el valor real del cobro). Nicolás Colón explicó que esto es necesario para que el cálculo de "importe de la transacción menos arancel/IVA" dé el resultado correcto en esos casos — si se informara el arancel/IVA real sin que haya devolución que lo justifique, el cálculo quedaría inconsistente.

**Ticket técnico — AD 1932:** Daniela Collia (Fintexa) y Nicolás Colón revisaron este ticket y determinaron que, para mantener la congruencia, el cambio debe aplicarse simultáneamente en **tres elementos**: (1) el PDF de liquidación, (2) el registro de liquidación propiamente dicho, y (3) el archivo del "botón" (export). Daniela Collia manifestó preocupación por si Euge (verificar si es Eugenia/Emma Vignoles u otra persona del equipo de Fintexa) está al tanto de este cambio estructural — Nicolás Colón se ofreció a notificarle.

**Alcance relacionado — AD 1837 / AD 3425:** Daniela Collia copió el nuevo alcance del ticket AD 1837 (archivo CSV en el administrador) dentro de la descripción de AD 3425, para que quede registrado correctamente. Nicolás Colón acordó revisar y dar el visto bueno para finalizar ese análisis — sin cierre confirmado todavía al momento de esta reunión.

**Nota:** esta regla convive con la ya documentada en `agente_cobros_y_pagos/liquidaciones_reversas_y_comprobantes.md` / `adquirencia/devoluciones_y_contracargos.md §7` sobre deducciones de arancel/impuestos en reversas (solo se devuelven en reversa total del mismo día del cobro, confirmada para AD V73) — son reglas complementarias, no la misma: aquella cubre cuándo se devuelve el arancel al comercio en una reversa, esta cubre qué valor se informa en el archivo de liquidación cuando no hay reversa/devolución en absoluto.

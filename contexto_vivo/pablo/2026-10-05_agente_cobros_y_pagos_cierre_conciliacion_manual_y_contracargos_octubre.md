---
id: 2026-10-05_agente_cobros_y_pagos_cierre_conciliacion_manual_y_contracargos_octubre
pm: pablo
fecha_captura: 2026-10-05
fuente: "/sync_meetings — reunión 'Weekly - Producto / Operaciones', 2026-10-05 15:01, minuta Gemini (compartida, mnadalin)"
producto: agente_cobros_y_pagos
tema: cierre de la conciliación manual diaria de liquidaciones + extensión del tratamiento de contracargos a octubre
tipo: conocimiento
destino_propuesto: 3_recursos/detalle_productos/agente_cobros_y_pagos/liquidaciones_reversas_y_comprobantes.md
tipo_destino: actualizar
contradice: "no"
confianza: alta
estado: en_cola
merge_commit:
---

**Logro confirmado (Nicolás Colón, reunión "Weekly - Producto / Operaciones", 2026-10-05):** se eliminó la necesidad de liquidar mediante **conciliación manual diaria** — el proceso que exigía sumar a mano todas las transacciones y restar devoluciones/desconocimientos en las liquidaciones. Esto era lo que específicamente pedía resolver Emma Vignoles (Euge). Confirmado que ya está sucediendo en producción al momento de esta reunión.

**Contracargos de tarjeta — extensión a octubre:** el tratamiento de contracargos de tarjeta debería haber cerrado este mes (septiembre), pero surgieron tickets no frenantes (no bloqueantes) que lo extienden a octubre. Nicolás Colón no detalló cuáles tickets específicamente en esta reunión.

**Pendiente, no resuelto en esta reunión:** qué le resta mostrarse a los clientes sobre este cambio (Pablo Gomes lo señaló como lo que falta cerrar, sin resolución en la misma sesión).

**Contexto relacionado ya documentado:** las reglas de deducción de arancel/IVA en reversas totales del mismo día (AD V73, confirmadas 2026-09-29) y la regla nueva de arancel/IVA en cero sin devolución (ver ítem separado `2026-10-05_agente_cobros_y_pagos_regla_arancel_iva_cero_sin_devolucion`, misma fecha de captura) son parte del mismo motor de liquidaciones que este ítem actualiza.

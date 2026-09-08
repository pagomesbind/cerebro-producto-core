---
id: 2026-09-07_conocimiento-contracargo-rechazado-por-validacion-caja-id-colectores
pm: nicolas
fecha_captura: 2026-09-07
fuente: "Reunión \"Weekly - Producto / Operaciones\" (2026-09-07)"
producto: agente_cobros_y_pagos
tema: Bug de contracargos rechazados en colectores (ej. Pago Fácil) por validación incorrecta de ID de caja vs. ID de colector — decisión de eliminar la validación
tipo: conocimiento
destino_propuesto: 3_recursos/detalle_productos/agente_cobros_y_pagos/devoluciones_y_contracargos.md
tipo_destino: crear
contradice: "no"
confianza: alta
estado: en_cola
---

Nicolás Colón explicó en la reunión "Weekly - Producto / Operaciones" (2026-09-07) un bug de mecánica de contracargos en el Agente de Cobros y Pagos: para colectores como **Pago Fácil**, las **devoluciones** se procesan correctamente, pero los **contracargos** quedan guardados con estado de rechazo por una validación interna que compara el **ID de caja de la transacción** contra el **ID de caja del colector** — campos que difieren en el ~99% de los casos reales (no tiene por qué coincidir la caja puntual donde se originó la transacción con la caja general configurada del colector).

**Decisión del grupo:** eliminar esa validación mediante una corrección técnica, ya que no aporta control real y bloquea contracargos legítimos.

Este bug es distinto del proyecto de "tratamiento de contracargos" (PRD-146, prioridad alta, tickets DAD-2209/DAD-2257 — ver `contexto_vivo/2026-09-08_conocimiento-tratamiento-contracargos-prioridad-alta-tickets.md`, capturado vía mail el mismo día): aquél es sobre Adquirencia/tarjetas, este es específicamente sobre contracargos de **colectores RxT/CVUCollect** en Agente de Cobros y Pagos — dos frentes de contracargos en paralelo, en productos distintos.

> Fuente: Reunión "Weekly - Producto / Operaciones" (2026-09-07, minuta Gemini).

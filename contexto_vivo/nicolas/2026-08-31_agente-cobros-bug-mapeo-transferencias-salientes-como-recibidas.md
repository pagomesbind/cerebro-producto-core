---
id: 2026-08-31_agente-cobros-bug-mapeo-transferencias-salientes-como-recibidas
pm: nicolas
fecha_captura: 2026-08-31
fuente: "Reunión \"Weekly - Producto / Operaciones\" (2026-08-31)"
producto: agente_cobros_y_pagos
tema: Bug real — transferencias salientes mapeadas erróneamente como transferencias recibidas
tipo: conocimiento
destino_propuesto: 3_recursos/detalle_productos/agente_cobros_y_pagos/transferencia_saliente_mecanica.md
tipo_destino: actualizar
contradice: "no"
confianza: media
estado: ingestado
---

En la reunión "Weekly - Producto / Operaciones" (2026-08-31), Nicolás Colón identificó una inconsistencia técnica: **las transferencias salientes del Agente de Cobros y Pagos se están mapeando erróneamente como transferencias recibidas**. La minuta no da más detalle técnico (en qué endpoint/reporte se ve el mapeo incorrecto, desde cuándo, ni el cliente afectado) — se registró como hallazgo a corregir, sin desarrollo asociado todavía. Ver tarea T-018 en `tareas.md` para el seguimiento de reporte/corrección.

Este hallazgo es distinto del grupo de tickets ya en curso para "arreglar transferencias salientes de agente de cobros y pagos" (mencionado en la misma reunión, con foco en reconsultas de monitoreo) — no quedó claro en la minuta si este bug de mapeo es parte de ese mismo grupo de tickets o un hallazgo nuevo y separado; a confirmar cuando se cargue el ticket.

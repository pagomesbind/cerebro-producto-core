---
id: 2026-09-28_agente_cobros_y_pagos_conocimiento_optimizacion_liquidacion_lotes_padrones
pm: pablo
fecha_captura: 2026-09-28
fuente: "/sync_meetings — reunión \"Producto\" (2026-09-28 14:12, compartida por evignoles), minuta Gemini"
producto: agente_cobros_y_pagos
tema: "Optimización de tiempos de liquidación de cobros online mediante procesamiento por lotes y tabla intermedia de padrones fiscales — objetivo versión 74/octubre"
tipo: conocimiento
destino_propuesto: 3_recursos/detalle_productos/agente_cobros_y_pagos/liquidaciones_reversas_y_comprobantes.md
tipo_destino: actualizar
contradice: "no"
confianza: alta
estado: ingestado
merge_commit: 3492d04
---

Nicolás Colón y Pablo Gomes repasaron en la reunión "Producto" las mejoras en los tiempos de liquidación de cobros online: **procesamiento por lotes** (referido también en la reunión "Weekly - Producto / Operaciones" del mismo día como ticket **PR205**), la creación de nuevas vistas de acumulados mensuales y nuevas tablas de liquidación.

**Mecánica técnica nueva:** para evitar consultar individualmente los más de **160 padrones fiscales** en el momento del cálculo de liquidación, se va a construir una **tabla temporal intermedia** que precalcule y almacene los resultados de los padrones, actualizándose mensualmente. Entrega programada para la **versión 74 de octubre**.

> Fuente: reunión "Producto", 2026-09-28 (`/sync_meetings`).

---
id: 2026-10-01_agente_cobros_y_pagos_optimizacion_qr_hipodromo
pm: pablo
fecha_captura: 2026-10-01
fuente: "/sync_meetings — reunión 'Análisis COBRO' (docId 1N7n2QoyUVrD94Z4QhLdBiBSS3FLlwuJ1LMi0dYMjQWk), 2026-10-01 12:01, propia"
producto: agente_cobros_y_pagos
tema: Optimización de tiempos de respuesta en pagos QR del Hipódromo de Palermo — reducción de pasos y bug de cola en escaneo rápido
tipo: conocimiento
destino_propuesto: 3_recursos/detalle_productos/agente_cobros_y_pagos/pedidos_de_clientes_y_hallazgos_operativos.md
tipo_destino: actualizar
contradice: "no"
confianza: media
estado: en_cola
merge_commit:
---

En la reunión semanal "Análisis COBRO" con Fintexa (2026-10-01), se analizó un pedido de optimización de tiempos de respuesta en los pagos QR del **Hipódromo de Palermo**, cliente de Agente de Cobros y Pagos.

**Hallazgo:** el proceso de registro de un pago QR constaba de **16 pasos**, que el análisis técnico determinó que pueden reducirse a **11** (y en una segunda vuelta, a **8**) sin perder funcionalidad, con el objetivo de acortar el tiempo de respuesta percibido por el usuario.

**Problema operativo identificado:** cuando un usuario escanea el QR muy rápido, la transacción no alcanza a insertarse en la base de datos a tiempo — se envía a una cola de procesamiento que genera demoras considerables (por encima del objetivo). La solución propuesta es eliminar ese camino de cola para los casos de escaneo rápido, reduciendo el tiempo de respuesta de los ~7 segundos actuales a un objetivo estimado de **~4 segundos**.

**Nota adicional (sin confirmar como decisión):** en la misma reunión se mencionó un ticket relacionado con un cambio de "Barchart Max" (BMX) para optimizar el rendimiento general de la base de datos — mencionado de forma tangencial, sin detalle técnico adicional en la minuta.

**Estado:** análisis técnico ya realizado por el equipo de Fintexa; sin ticket de Jira identificado en la minuta, sin fecha de implementación confirmada — queda dentro del backlog general de la versión 74/75 (ver también la discusión de estrategia de despliegues quincenales de la misma reunión, sin resolver todavía).

> Fuente: reunión "Análisis COBRO", 2026-10-01, minuta Gemini.

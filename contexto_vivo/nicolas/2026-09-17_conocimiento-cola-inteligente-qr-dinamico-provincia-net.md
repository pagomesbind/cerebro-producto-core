---
id: 2026-09-17_conocimiento-cola-inteligente-qr-dinamico-provincia-net
pm: nicolas
fecha_captura: 2026-09-17
fuente: "Reunión 'Análisis de riesgo: AD V 73' (2026-09-17), minuta Gemini"
producto: agente_cobros_y_pagos
tema: Gestión inteligente de colas para QR dinámico — despriorización de ráfagas que superen 200 peticiones/minuto, implementada en AD V73; resuelve el debate abierto de "colas diferenciadas por cliente" (Provincia Net vs. clientes urgentes)
tipo: conocimiento
destino_propuesto: 3_recursos/detalle_productos/agente_cobros_y_pagos/masividad_generacion_qr.md
tipo_destino: actualizar
contradice: "no"
confianza: alta
estado: en_cola
---

En "Análisis de riesgo: AD V 73" se discutió una incidencia de demora superior a 35 segundos en la disponibilidad de datos de códigos QR dinámicos, atribuida a Provincia Net (mismo frente ya documentado en `masividad_generacion_qr.md`, ticket AD-935). Daniel Zalazar explicó que **se implementó una gestión inteligente de cola**: los clientes que superen las **200 solicitudes por minuto** se despriorizan temporalmente y pasan a una **cola secundaria**, en vez de competir por los mismos recursos que el resto del tráfico.

Esto resuelve, con una solución concreta, el debate que había quedado abierto en la reunión "Análisis COBRO" del 2026-09-10 (Melisa Belpassi proponía separar colas de procesamiento para clientes urgentes como DPay de la de Provincia Net, "sin resolución todavía" a esa fecha) — la solución final no separó por cliente nombrado sino por **umbral de tasa de peticiones** (200 req/min), que en la práctica despriorizaría a cualquier cliente que genere ráfagas de ese volumen, no solo a Provincia Net.

**Seguimiento operativo acordado:** el equipo de infraestructura debe monitorear el consumo de bases de datos y las colas de RabbitMQ durante el manejo de ráfagas (asignado color amarillo, no verde). Hernan Clarich queda a cargo de avisar preventivamente a Provincia Net sobre el envío de ráfagas en horarios específicos, para minimizar riesgos durante el despliegue.

> Fuente: Reunión "Análisis de riesgo: AD V 73" (2026-09-17), minuta Gemini — sección Decisiones ("Gestión inteligente de colas para QR dinámico") y Detalles.

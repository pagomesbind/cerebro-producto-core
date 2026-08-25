---
id: 2026-08-21_agcyp-integracion-procesadores-prisma-gp
pm: nicolas
fecha_captura: 2026-08-21
fuente: "Reunión \"Análisis COBRO\" (2026-08-20), minuta Gemini"
producto: agente_cobros_y_pagos
tema: Integración de procesadores de pago (Prisma/GP) — deuda técnica de reglas, parámetro "pago único" y regla de liquidación
tipo: conocimiento
destino_propuesto: 3_recursos/detalle_productos/agente_cobros_y_pagos/integracion_procesadores_pago.md
tipo_destino: crear
contradice: "no"
confianza: alta
estado: en_cola
---

En la reunión recurrente "Análisis COBRO" (2026-08-20, con Daniela Collia y equipo de Fintexa) se destiló la siguiente mecánica/estado de la integración de procesadores de pago del Agente de Cobros y Pagos:

- **Deuda técnica de grupos de reglas**: el sistema mantiene dos procesadores en paralelo (Prisma y GP) con grupos de reglas mal estructurados para su coexistencia, lo que genera fricción operativa en las pruebas (pagos y devoluciones no pueden ejecutarse completamente en el entorno actual). Se acordó migrar el enfoque hacia parámetros de canal dinámicos en lugar de grupos de reglas rígidos, para evitar ciclos repetitivos de modificación manual. No es bloqueante para el despliegue en curso.
- **Parámetro "pago único"**: se definió para diferenciar productos — valor `1` = botón de pago, valor `0` = RXT.
- **Regla de liquidación de transacciones en línea**: las transacciones en línea deben liquidarse el mismo día; si no pueden procesarse, se descartan (antes quedaban en una cola de espera incorrecta por un error de lógica de negocio, detectado junto con el problema de saturación de la base de impuestos — ver riesgo asociado en `2_areas/riesgos.md`).
- **Limitación del panel administrativo con Prisma**: el backend ya soporta Prisma como procesador único, pero el panel de administración no permite seleccionarlo así porque el sistema habilita GP por defecto. Se decidió aprobar igual el despliegue del ticket de Prisma sin esta funcionalidad de configuración en el admin (no cumple 100% la Definition of Done), gestionando la limitación de la interfaz por separado.
- **Hotfix de localidades/códigos postales**: se corrigen inconsistencias de validación en alta/edición manteniendo el alcance acotado; la reestructuración de la API para devolver una lista de localidades (en vez de una sola) queda postergada a un ticket futuro de menor prioridad, fuera de alcance del hotfix del ticket 789.
- **Cronograma**: versión 72 programada para el jueves siguiente (2026-08-27) a las 21:00hs, con transferencias salientes y guardado de respuesta de Rebank encaminados.

> Fuente: Reunión "Análisis COBRO" (2026-08-20), minuta Gemini.

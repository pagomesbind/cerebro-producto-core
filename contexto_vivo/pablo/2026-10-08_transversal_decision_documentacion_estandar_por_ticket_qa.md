---
id: 2026-10-08_transversal_decision_documentacion_estandar_por_ticket_qa
pm: pablo
fecha_captura: 2026-10-16
fuente: "/sync_meetings — reunión 'Pruebas QA Fintexa - Bind Psp' (2026-10-08, 17:01)"
producto: transversal
tema: Desde la v74, cada ticket debe llevar documentación técnica/funcional estándar adjunta para que QA pueda probar sin depender de definiciones sueltas por mail
tipo: decision
destino_propuesto: 2_areas/procesos/ciclo_de_vida_desarrollo.md
tipo_destino: actualizar
contradice: "no"
confianza: alta
estado: en_cola
merge_commit:
---

## Problema que origina la decisión

Ana María Moreno (QA, Fintexa) reportó que casos de prueba no cerraban porque las definiciones cambiaban por mail (de Mariano) sin reflejarse en los tickets de Jira, obligando a buscar información externa imprevista. Además, el equipo de QA de Fintexa carece de cierto conocimiento de negocio, lo que hizo que se omitieran pruebas asociadas a impuestos y PMC. Se señaló también que correcciones recibidas a pocos días del pase a producción no dejan margen para probar módulos complejos (PMC, impuestos, FCI).

## Decisión

1. **Documentación estándar por ticket desde la v74**: adjuntar una primera versión de la documentación de desarrollo y cambios (plantilla a definir por Mariela Marin/Andrea Orsini/Melisa Belpassi en base a informes previos de Saulo y Mariano) con cambios, tablas, endpoints y datos funcionales — al momento del pase a control de calidad.
2. **Reuniones de planificación integrales**: con participación de todos los equipos, para dar visibilidad anticipada del alcance de cada versión y anticipar riesgos/optimizar márgenes de tiempo (mencionado explícitamente de cara a la v74, programada para el jueves 29 — nota: la fecha real terminó siendo el 22/10, ver `rechazos_bines_payway/proyecto.md`).

## Contexto adicional

Se usa un criterio de "semáforo" para priorizar qué prueba QA (excluye tareas puramente técnicas como librerías de cero downtime o migración de colas). Se mencionó la auditoría de 5 semanas del BCRA desde el 26/10 como presión adicional sobre la velocidad/calidad de entregas. Conecta con la tensión ya capturada el 2026-10-15 sobre la suspensión del soporte diario de Fintexa a QA interno (`2026-10-15_transversal_riesgo_decision_soporte_qa_sin_stakeholders_presentes`, ya `capturado`) — mismo problema de fondo (comunicación Producto↔QA↔Desarrollo) visto en dos momentos distintos.

> Fuente: reunión "Pruebas QA Fintexa - Bind Psp", 2026-10-08 17:01hs (Bethania Tornari, Pablo Gomes, Matías Alzogaray, Andrea Orsini, Ana María Moreno, Hernán Clarich, Mariana Nadalin, equipo Fintexa).

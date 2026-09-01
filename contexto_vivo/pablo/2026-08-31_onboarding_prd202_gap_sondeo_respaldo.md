---
id: 2026-08-31_onboarding_prd202_gap_sondeo_respaldo
pm: pablo
fecha_captura: 2026-08-31
fuente: "sesión de trabajo directa con el PM, revisión de los tickets de PRD-202 recién creados en Jira"
producto: onboarding
tema: gap cerrado — endpoint liviano dedicado para el sondeo de respaldo del webhook de PRD-202
tipo: iniciativa
proyecto: PRD-202
pm_destino:
destino_propuesto: wiki/2_areas/direccion/iniciativas.md
tipo_destino: actualizar
contradice: "no"
confianza: alta
estado: ingestado
merge_commit:
---

El PM revisó los 8 tickets recién creados de PRD-202 (Fase 1) y notó que Onboarding no exponía ningún endpoint liviano para que Wallet monitoree el estado de una solicitud — todo lo que Onboarding devolvía en lectura era el endpoint de detalle completo (pesado, prioridad Should-have).

Investigando el análisis técnico-funcional de la solución y las historias de usuario ya escritas, se confirmó que esto era un gap real, no solo una impresión: el "sondeo periódico de respaldo" que el KYC-wrapper de Wallet debía correr contra Onboarding — mencionado como mecanismo de resiliencia del webhook hacia la organización integradora (esa historia sí es Must-have) — nunca tuvo definido, en ninguna fuente del proyecto, contra qué endpoint corría. El único endpoint de lectura ya existente en Onboarding era el pesado, de prioridad menor, lo que dejaba un mecanismo crítico de resiliencia apoyado en algo que podía no estar construido para el lanzamiento.

El PM confirmó agregar un endpoint dedicado y liviano en Onboarding (mismo sobre ya usado en las respuestas de creación/continuación de solicitud — estado, motivo, último paso, acción, timestamps — sin el detalle pesado de pasos/domicilio/contacto), en vez de reusar el endpoint completo existente. Se creó como historia nueva (novena de PRD-202 en Jira, ticket OB-238, prioridad Must-have) bajo la Epic de Onboarding, y se actualizó la descripción del ticket del webhook de Wallet para que su criterio de aceptación sobre el sondeo de respaldo referencie el endpoint real en vez de quedar genérico.

Deja un aprendizaje reutilizable: al diseñar un contrato de integración con un mecanismo de resiliencia (reintentos, sondeo de respaldo, reconciliación), vale la pena verificar explícitamente que ese mecanismo tenga un endpoint/transporte concreto definido — es fácil que quede mencionado en prosa ("hay un sondeo de respaldo") sin que nadie lo baje a un contrato accionable, y ese vacío puede pasar inadvertido hasta que se arma el ticket de desarrollo.

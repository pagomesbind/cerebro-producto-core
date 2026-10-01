---
id: 2026-09-29_arquitectura_conocimiento_migracion_cero_downtime_y_escalado_bd
pm: pablo
fecha_captura: 2026-09-29
fuente: "/sync_meetings — reunión \"Repaso Semanal líderes\" (2026-09-29 11:00, compartida por evignoles), minuta Gemini"
producto: transversal
tema: "Migración a cero tiempo de inactividad en microservicios (3 etapas, prioriza Webhook Sender) + escalado automático de bases de datos + ventanas de mantenimiento para depuración"
tipo: conocimiento
destino_propuesto: 3_recursos/arquitectura_sistema/evolucion_de_la_plataforma.md
tipo_destino: actualizar
contradice: "no"
confianza: alta
estado: ingestado
merge_commit: 9bf60c5
---

En "Repaso Semanal líderes" (2026-09-29), con Fintexa (Alejandro Sfrede, Melisa Belpassi, Daniel Zalazar, Hernán Clarich):

**Migración a cero tiempo de inactividad (zero downtime), en 3 etapas:** priorizando primero los microservicios más críticos — **Webhook Sender** es el primero — para evitar pérdida de mensajes durante despliegues continuos. Esquema ya comunicado a los líderes técnicos.

**Escalado automático de bases de datos:** Daniel Zalazar asume revisar y configurar el escalado/desescalado automático de BD, en conjunto con el equipo de infraestructura y desarrollo — pruebas iniciales sobre microservicios específicos antes de extenderlo al resto del ecosistema, para medir impacto en costos. Queda pendiente ("requiere más debate") la prueba de escalamiento en sí, a cargo de Daniel Zalazar, en conjunto con el despliegue de cero downtime.

**Ventanas de mantenimiento para depuración de tablas grandes:** las tablas de comprobantes y operaciones están depuradas solo hasta **febrero de 2026** — se necesitan ventanas adicionales. Emma Vignoles objetó que los tiempos actuales (4 horas por cada 2 meses de datos) generan bloqueos con pérdida de transacciones; Gonzalo Rivera sugirió programar las ventanas según los horarios de menor operatoria de **BSF** (decisión acordada: buscar ventana basada en esos horarios). Daniel Zalazar se compromete a revisar optimizaciones con el DBA.

**Hallazgos operativos menores relacionados (Ardid):** un proceso automático que cambia el estado de transacciones pendientes de validación quedó con registros trabados desde el 28/09 — se ejecuta manualmente hasta resolverse en la próxima versión; también hay una incidencia de tiempo de espera excesivo que afecta la visualización de la pestaña de transferencias, en resolución.

> Fuente: reunión "Repaso Semanal líderes", 2026-09-29 (`/sync_meetings`), minuta de Gemini (docId `1yvPrMP0eehP2qw4fUey7i8eISz5rKtZtlWaXpB_LLCI`).

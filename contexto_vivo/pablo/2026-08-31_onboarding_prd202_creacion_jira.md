---
id: 2026-08-31_onboarding_prd202_creacion_jira
pm: pablo
fecha_captura: 2026-08-31
fuente: "/idea_jira sobre PRD-202 (Fase 1) — sesión de trabajo directa con el PM"
producto: onboarding
tema: creación en Jira de PRD-202 (Fase 1) completada — IDEA, 2 Epics, 8 Historias
tipo: iniciativa
proyecto: PRD-202
pm_destino:
destino_propuesto: wiki/2_areas/direccion/iniciativas.md
tipo_destino: actualizar
contradice: "no"
confianza: alta
estado: ingestado
merge_commit: c4148e7
---

`/idea_jira` completó la creación en Jira de PRD-202 (Fase 1, Onboarding — validación de identidad KYC en el alta de wallet PF mayor de edad) el 2026-08-31.

La IDEA [PRD-202](https://bindpsp.atlassian.net/browse/PRD-202) (ya existía en Jira, en estado Discovery) quedó transicionada a **EN APROBACION**, con SP estimado 54 y prioridad High.

Por primera vez en este Cerebro, una IDEA de `/idea_jira` se dividió en **2 Epics** en vez de una sola: las 8 historias de desarrollo se reparten entre 2 equipos técnicos (Wallet y Onboarding), y Jira no permite que una Epic tenga historias hijas en un proyecto distinto al suyo. Se crearon [WS-1559](https://bindpsp.atlassian.net/browse/WS-1559) (Wallet, 5 historias) y [OB-234](https://bindpsp.atlassian.net/browse/OB-234) (Onboarding, 3 historias), ambas linkeadas a la misma IDEA y con la misma descripción técnica completa (12 secciones del análisis de solución), porque ambos equipos necesitan el contrato entero para construir su mitad sin romper lo compartido. El PM también pidió, por primera vez, que los títulos de las Historias en Jira no lleven el prefijo "US-N:" que usa el artefacto interno de historias de usuario.

De las 10 historias documentadas, 2 (migración de organizaciones legacy al nuevo patrón, y traza de datos para que Administración facture) no se ticketearon como desarrollo — el PM las identificó como tareas de su propio seguimiento post go-live, no trabajo de ingeniería, y quedaron en el backlog personal del PM en vez de en Jira.

La ejecución tuvo un blocker intermedio: el conector de Jira devolvió `403 "The app is not installed on this instance"` en toda escritura durante buena parte de la sesión (mismo síntoma ya visto el 2026-08-27 en PRD-216) — se resolvió cuando el PM desconectó y reconectó el conector manualmente.

Esta sesión deja 2 precedentes de convención reutilizables para futuras corridas de `/idea_jira`: (1) cuando una IDEA reparte historias entre más de un equipo técnico, corresponde crear una Epic por equipo (no una sola), todas linkeadas a la misma IDEA; (2) antes de crear los tickets, vale la pena que el PM revise si alguna "historia" documentada es en realidad una tarea de coordinación/negocio del propio PM, no un ticket de desarrollo.

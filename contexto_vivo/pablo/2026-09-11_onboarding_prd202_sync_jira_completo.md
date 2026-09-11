---
id: 2026-09-11_onboarding_prd202_sync_jira_completo
pm: pablo
fecha_captura: 2026-09-11
fuente: "/idea_jira — sesión de sincronización de Jira con el estado vigente de la wiki de PRD-202"
producto: onboarding
tema: PRD-202 — sincronización completa de Jira (IDEA, 2 Epics, 9 Historias) tras backlog drift desde 2026-09-09
tipo: iniciativa
proyecto: PRD-202
destino_propuesto: 2_areas/direccion/iniciativas.md
tipo_destino: actualizar
contradice: "no"
confianza: alta
estado: en_cola
merge_commit:
---

**PRD-202 (API wallet orquestando OB — Fase 1: cuenta PF mayor edad) quedó con Jira sincronizado al estado vigente de la wiki, tras un desfasaje de más de una semana.**

La IDEA y las 2 Epics (WS-1559 Wallet, OB-234 Onboarding) no se tocaban desde el 2026-08-31/2026-09-02 y seguían describiendo el contrato viejo ("4 endpoints + 2 mecanismos de notificación", controles de cumplimiento normativo fuera de alcance) — desalineadas con el PRD desde su reescritura a v7.0 (2026-09-09, que revirtió esa exclusión de alcance) y con toda la maduración posterior del análisis técnico (`solution` v2.0→v3.0) y de las historias de usuario (`us` v6.3→v7.9): expansión del catálogo de errores por proveedor externo, mecanismo de degradación por timeout trasladado de Wallet a Onboarding, y el agregado más reciente del campo `datosCuenta` (mapeo completo al contrato legacy de creación de cuenta de Wallet, confirmado contra su OpenAPI real).

Se regeneraron las 12 descripciones (IDEA, 2 Epics con contenido técnico idéntico y autocontenido, 9 Historias con contrato de API + AC completos), sin tocar estado/prioridad/assignee en ningún ticket (ya estaban correctos).

**Hallazgo técnico de la plataforma, no específico de este proyecto:** el campo `description` de Jira rechaza contenido ADF por encima de ~28-30KB (`CONTENT_LIMIT_EXCEEDED`). Aplica a cualquier IDEA futura con un análisis técnico-funcional extenso — la mitigación (tablas markdown → listas de bullets, prosa comprimida; si aun así no entra, dividir en descripción + comentario del ticket) debería incorporarse como criterio general de la skill `/idea_jira`, no quedar como un ajuste ad hoc de esta corrida.

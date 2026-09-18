---
id: 2026-09-18_transversal_iniciativa_revision_pj_cumplimiento
pm: pablo
fecha_captura: 2026-09-18
fuente: "/idea_start — discovery propio del PM (mockup 'Centro de Revisión' + reconstrucción de problema Modo C)"
producto: onboarding
tema: nueva IDEA — backoffice de revisión de PJ por Cumplimiento
tipo: iniciativa
proyecto: PRD-256
pm_destino:
destino_propuesto: 2_areas/direccion/iniciativas.md
tipo_destino: actualizar
contradice: "no"
confianza: alta
estado: ingestado
merge_commit:
---

Nueva IDEA abierta por Pablo Gomes vía `/idea_start`: **PRD-256 — "Backoffice de revisión de PJ por Cumplimiento — UX no está lista para uso obligatorio y masivo"** (`wiki/1_proyectos/revision_pj_cumplimiento/`).

**Origen:** el PM probó personalmente la pantalla de revisión de Cumplimiento (Nivel 2) de Onboarding Jurídico y la encontró muy pobre en UX. Reconstruido hacia atrás (Modo C), el problema es anticipatorio: ese nivel de revisión hoy no está activo en el flujo real de La Virginia (único cliente con Onboarding Jurídico en producción), pero un comité de auditoría estableció que ninguna persona jurídica de Bind puede darse de alta sin pasar por Cumplimiento — la pantalla va a volverse de uso obligatorio y masivo para el 100% de las PJ de Bind, bajo SLA regulatorio de 72hs, con un deadline de directorio 2026-10-01.

**Por qué es proyecto nuevo y no un slice de `proyecto-la-virginia-ob-pj`:** la pantalla deja de ser exclusiva de La Virginia — la generalización a todos los clientes/flujos futuros de PJ cambió el veredicto del Gate 2 (vale la pena ahora, como iniciativa propia).

**Alcance acordado (Gate 3):** solo la UX de revisión/aprobación del oficial de Cumplimiento (Nivel 2) — la carga del Oficial de Negocio (Nivel 1) queda expresamente fuera, ya resuelta y aprobada por el cliente en `proyecto-la-virginia-ob-pj`. Se parte de un mockup ya prototipado con el PM ("Centro de Revisión"), incorporando ideas de una consola de Cumplimiento más madura de la misma plataforma (Fintexa, demo a Banco Industrial/Octagon) solo en lo que aplica a la vista de una solicitud individual (screening, aprobación por documento) — quedan fuera matriz de riesgo configurable, cola de casos y políticas parametrizables (son negocio/validación nueva, no UI).

**Gap Alta que condiciona la Entrega, todavía sin resolver:** no está confirmado si este rediseño lo construye Fintexa (como el resto de la plataforma) o si Bind tiene alguna capacidad propia sobre ese frontend — define el formato del artefacto de salida (PRD para Fintexa vs. ticket de ingeniería interna).

IDEA creada en Jira (PRD-256, proyecto "PRD"/Producto, tipo Idea, asignada a Pablo Gomes) desde el arranque del discovery, per regla de proceso del PM.

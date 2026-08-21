---
id: 2026-08-20_onboarding_prd214_discovery_gate1-2_y_arquitectura_sharedkyc
pm: pablo
fecha_captura: 2026-08-20
fuente: "/idea_start — primera sesión de discovery formal de PRD-214, retomando una carpeta creada 2026-07-17 sin discovery corrido"
producto: onboarding
tema: PRD-214 (legajo de stock) — Gate 1/2 cerrados, dimensionamiento del stock y alternativa de arquitectura SharedKYC
tipo: iniciativa
proyecto: PRD-214
pm_destino:
destino_propuesto: 2_areas/direccion/iniciativas.md
tipo_destino: actualizar
contradice: "no"
confianza: alta
estado: ingestado
merge_commit: 5f0974a
---

PRD-214 ("Carga masiva de legajos de cuentas de wallet existentes", vehículo de KR2 del foco Onboarding) corrió su primer discovery formal el 2026-08-20 (`/idea_start`, Modo D — la carpeta ya existía desde 2026-07-17 con contexto acumulado pero sin gates corridos).

**Gate 1 (problema) y Gate 2 (vale la pena) cerrados.** Dimensionamiento del stock actualizado: ~4M cuentas totales, ~2M dadas de baja por Astropay, ~2M activas sin legajo — cierra un gap de medición abierto desde 2026-07-17 en `2_areas/direccion/estrategia/foco_onboarding.md` (corrige además la estimación previa de PRD-147, que había anotado ~1,5M). Veredicto ✅ vale la pena ahora, consistente con la decisión de dirección ya tomada (KR2 en paralelo a KR1, prioridad 2).

**Gate 3 (solución) parcial — surgió una bifurcación de arquitectura.** Al desestacionar la solución, el PM planteó una alternativa: en vez de que Onboarding integre directo con Worldsys/ComplianceOne (diseño ya cerrado en PRD-147), extraer esa integración a un servicio compartido nuevo — **SharedKYC** — dejando a Onboarding como validador puro de identidad. Esto:
- Afecta también a **PRD-147**, que ya tiene diseño técnico completo (2026-08-19) bajo el supuesto de integración directa, sin tickets todavía en Jira.
- Reabre la **decisión heredada #11** del proyecto general `proyecto-onboarding-estrategico` ("Onboarding es la fuente de archivos... migrar a otro repositorio queda diferido, solo si resulta necesario") — el PM plantea que ese momento podría haber llegado.

Se armó una comparación completa (pros/contras, tabla, y 4 diagramas de secuencia con el detalle real de endpoints de Worldsys — alta nueva y backfill, para cada alternativa) en `1_proyectos/proyecto-onboarding-estrategico/artefactos/2026-08-20_alternativas_shared_kyc_vs_onboarding.md`. La decisión queda **en revisión**, a resolver en una mesa técnica con Arquitectura/Fintexa (tarea T-023 en `1_proyectos/tareas.md`) y una futura sesión de `/idea_solution` sobre PRD-214. Recomendación no vinculante de la sesión: pilotear SharedKYC en PRD-214 (sin nada construido todavía) mientras PRD-147 avanza con su diseño actual.

Sin cambios de horizonte de roadmap (PRD-214 sigue en Siguiente/Next) ni de Estado Jira (PENDIENTE).

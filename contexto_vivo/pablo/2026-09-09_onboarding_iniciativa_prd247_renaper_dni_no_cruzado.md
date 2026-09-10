---
id: 2026-09-09_onboarding_iniciativa_prd247_renaper_dni_no_cruzado
pm: pablo
fecha_captura: 2026-09-09
fuente: "/idea_start — sesión de discovery, escalada desde `1_proyectos/proyecto-onboarding-estrategico/prd-202_onboarding_consolidado/decisiones.md` [2026-09-09] (3)"
producto: onboarding
tema: "Alta de nueva IDEA PRD-247 (vulnerabilidad Renaper Datos) dentro de proyecto-onboarding-estrategico"
tipo: iniciativa
proyecto: PRD-247
destino_propuesto: 2_areas/direccion/iniciativas.md
tipo_destino: actualizar
contradice: "no"
confianza: alta
estado: ingestado
merge_commit: 0de2694
---

Nace **PRD-247** — "Vulnerabilidad Renaper Datos: no cruza imágenes de DNI frente/dorso contra el dato declarado", nueva IDEA miembro de `proyecto-onboarding-estrategico/` (carpeta `prd-247_renaper_dni_no_cruzado/`), PM Pablo Gomes.

Origen: escalada el 2026-09-09 desde el discovery de PRD-202 — durante la regeneración de `onboarding_consolidado-solution.md` se identificó una vulnerabilidad ya confirmada en producción (auditoría externa LLYASOC, contratada por Banco Industrial, 2026-08-25, ya documentada como canon en `3_recursos/detalle_productos/onboarding/arquitectura_solicitud_y_flujos.md §1ter`): Renaper Datos valida identidad solo por CUIL+género+número de trámite (texto), sin cruzar contra las imágenes de DNI frente/dorso — permite en teoría combinar el frente y el dorso de DNIs de dos personas distintas. El PM decidió no tratarlo como gap suelto de PRD-202 y escalarlo como iniciativa propia del proyecto general.

Estado: IDEA creada en Jira en DISCOVERY el mismo día (2026-09-09), asignada a Pablo Gomes, categoría BAU / Cliente COMPLIANCE / Producto Onboarding. Discovery de `/idea_start` en curso — barrido de contexto (Paso 1) completo, Ronda 1 del Gate 1 (problema) presentada al PM, pendiente confirmación literal. Sin mandato normativo explícito identificado que lo obligue (a diferencia de otros proyectos ⚠️ Obligatorios del Cerebro) — la presión viene de la auditoría externa de un banco sponsor. Posible relación de journey (no de alcance) con PRD-238 (`gestion_riesgo_fraude/`), a definir en Ronda 1.

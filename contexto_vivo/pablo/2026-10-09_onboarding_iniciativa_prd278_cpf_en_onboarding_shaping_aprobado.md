---
id: 2026-10-09_onboarding_iniciativa_prd278_cpf_en_onboarding_shaping_aprobado
pm: pablo
fecha_captura: 2026-10-09
fuente: "/idea_start — discovery de PRD-278 \"CPF en onboarding\" (shaping aprobado por el PM el 2026-10-09)"
producto: onboarding
tema: Nueva iniciativa PRD-278 "CPF en onboarding" — consulta a la Central de Prevención de Fraude de Coelsa en el alta, obligatoria por Com. B 13117; shaping aprobado
tipo: iniciativa
proyecto: PRD-278
pm_destino:
destino_propuesto: wiki/2_areas/direccion/iniciativas.md
tipo_destino: actualizar
contradice: "no"
confianza: alta
estado: en_cola
merge_commit:
---

**Novedad puntual (2026-10-09):** nace la IDEA **PRD-278 "CPF en onboarding"** (Pablo Gomes, Categoría BAU, Producto Onboarding, estado DISCOVERY), slice del foco Onboarding (KR1) y relacionada con PRD-238 (gestión del riesgo de fraude, Com. "A" 8471/8473). Es un proyecto **⚠️ Obligatorio**: la Com. "B" 13117 del BCRA (10/02/2026) exige a los PSPCP consultar y usar la CPF de Coelsa para prevenir fraude, incluido el onboarding, y hoy Bind no la consulta en ningún punto del alta (sanciones de los arts. 41/42 de la Ley de Entidades Financieras si lo constata la SEFYC).

**Shaping aprobado por el PM:** alternativa **A3′** — un paso nuevo de consulta a la CPF en el Onboarding (PF y PJ, por defecto en todas las altas, independiente del canal) con conector propio, cuyo resultado entra como regla con puntaje en la matriz de riesgo existente, con umbrales por entidad. **Tamaño preliminar de shaping 10–35 SP** (🔶; SP 22,5 cargado en Jira). Queda fuera, por decisión del PM: el screening del stock y el monitoreo transaccional (integración de Ardid a la CPF, otro proyecto), el reporte de eventos de fraude a la CPF y la suscripción a novedades. Pendiente: política de bloqueo de Compliance (T-200) y análisis funcional-técnico (`/idea_solution`).

> Fuente: Pablo Gomes, sesión `/idea_start`, 2026-10-09; `1_proyectos/fraude_en_altas/artefactos/fraude_en_altas-start.md`.

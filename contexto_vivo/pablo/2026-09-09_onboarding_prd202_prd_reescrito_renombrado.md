---
id: 2026-09-09_onboarding_prd202_prd_reescrito_renombrado
pm: pablo
fecha_captura: 2026-09-09
fuente: "Sesión `/idea_prd` sobre PRD-202 (Fase 1) — reescritura y renombre del PRD formal a onboarding_consolidado-prd.md v7.0"
producto: onboarding
tema: PRD formal de PRD-202 reescrito para incorporar los controles de cumplimiento normativo dentro de su alcance, y renombrado a la convención estándar de artefactos
tipo: iniciativa
proyecto: PRD-202
destino_propuesto: 2_areas/direccion/iniciativas.md
tipo_destino: actualizar
contradice: "no — es una reversión deliberada y documentada de una decisión anterior (2026-07-21), no una contradicción sin resolver"
confianza: alta
estado: ingestado
merge_commit: 4b0d3d1e684ff33256a33a29f86746dfd5c7cc9a
---

El PRD formal de PRD-202 (Fase 1 — alta de wallet PF mayor de edad) se reescribió de punta a punta y se renombró: pasa de `prd_alta_wallet_pf_mayor_fase1.md` a `onboarding_consolidado-prd.md` (v7.0), alineado a la convención de nombres (`onboarding_consolidado-*`) que ya usan el resto de los artefactos técnicos del proyecto (historias de usuario, análisis de solución, descripción de Epic de Jira).

**Cambio de fondo, no solo de forma:** el documento ahora describe, dentro de su propio alcance (Must-have), los controles de cumplimiento normativo que antes quedaban excluidos — validación contra la lista de personas inhabilitadas del banco patrocinador, listas internacionales de terrorismo y personas políticamente expuestas, condición de sujeto obligado ante el organismo de prevención de lavado de activos, situación fiscal ante el organismo recaudador, y el motor de puntaje de riesgo que combina todos esos resultados para decidir aprobación automática, rechazo automático o revisión manual. Esto refleja el contrato técnico vigente del proyecto (las historias de usuario ya modelan estos controles como parte del mismo motor de validación, conectando servicios que ya existen en producción para otros procesos de Bind PSP, no construyéndolos desde cero).

**Esto revierte, para este documento puntual, una decisión tomada el 2026-07-21** que había sacado explícitamente estas 3 validaciones (lista 15, totalizadores, Worldsys) del alcance del PRD porque cada una ya tenía una IDEA propia trackeada en el roadmap (lista 15 → PRD-116, contribuyentes no confiables de ARCA → PRD-117, totalizadores CBU/CVU → PRD-118) — para no duplicar scope entre items del roadmap. Al reescribir el PRD se detectó que el contrato técnico actual de PRD-202 ya corre estas validaciones como parte de su propio motor, y que el hallazgo técnico de PRD-116 (2026-09-02: "la lista 15 no requiere integración nueva, solo incluir el paso ya existente en los flujos de alta de CVU") describe exactamente lo que construye PRD-202. En vez de decidir unilateralmente si esto absorbe/cierra el scope de PRD-116, se dejó **anotado como gap abierto en el roadmap general** (`proyecto-onboarding-estrategico/gaps.md`, 2026-09-09) para que el PM lo resuelva: si PRD-116 debería cerrarse como absorbido por PRD-202, o si tiene una pieza propia que sigue siendo trabajo separado. Nota aparte capturada en el mismo gap: PRD-147 (legajo Worldsys) es sobre guardar documentación en el ZIP/legajo, una pieza distinta de la consulta de listas PEP/terrorismo que ya corre en la Etapa 2 de PRD-202 — la decisión de 2026-07-21 podría haber conflacionado ambas bajo el nombre genérico "Worldsys".

**ARCA no confiables (PRD-117) y totalizadores CBU/CVU (PRD-118) siguen confirmados fuera de alcance** de PRD-202 — son las únicas 2 validaciones de cumplimiento que efectivamente no tienen motor construido todavía, a diferencia de lista 15/condición fiscal ARCA/UIF/Worldsys-screening que ya corren en producción.

Sin cambios de prioridad, estimación de SP, ni en el Problema/Contexto/cifras del caso de negocio del PRD — el cambio es de alcance descrito y de completitud (se agregaron las 2 filas que faltaban en el checklist operativo por área, Fraude e IT, que antes cubría solo 5 de las 7 áreas obligatorias).

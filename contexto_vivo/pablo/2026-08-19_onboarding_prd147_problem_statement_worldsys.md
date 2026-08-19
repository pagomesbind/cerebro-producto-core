---
id: 2026-08-19_onboarding_prd147_problem_statement_worldsys
pm: pablo
fecha_captura: 2026-08-19
fuente: "/idea_problem — actualización in place del problem statement de PRD-147"
producto: onboarding
tema: PRD-147 (legajo Worldsys) — problem statement actualizado a v2.0
tipo: iniciativa
proyecto: PRD-147
destino_propuesto: 2_areas/direccion/iniciativas.md
tipo_destino: actualizar
contradice: "no"
confianza: alta
estado: ingestado
merge_commit: PENDIENTE
---

PRD-147 (Guardar documentación en el producto legajo de Worldsys, proyecto Onboarding Estratégico, KR2) actualizó su problem statement a v2.0 el 2026-08-19. El cambio de fondo: el riesgo crítico que bloqueaba el diseño (Legajo Digital de Fintexa vs. Worldsys como repositorio) ya estaba resuelto desde el 2026-08-18 a favor de Worldsys como único repositorio activo — esta sesión consolidó esa resolución en el documento de problem statement, que había quedado desactualizado desde su v1.0 (2026-07-21), previa a que se cerrara esa pregunta.

El documento actualizado también incorpora el alcance ampliado definido el 2026-08-18: Onboarding pasa a crear/consultar la persona en Worldsys online (no solo depender del batch diario `LAVADOCLIENTES` existente), y maneja el caso de una persona ya existente en Worldsys por otra unidad de negocio de Bind PSP (Worldsys no es multi-entidad) vía un patrón get-or-create con actualización de perfil.

Sin decisiones ni gaps nuevos — trabajo de síntesis y actualización de documento, no de discovery. Las preguntas abiertas vigentes (convivencia entre el batch diario y la integración online; documentación técnica pendiente de los endpoints de descarga de Worldsys; confirmación formal de costo/capacidad para el volumen de traslado retroactivo de ~1,5M cuentas) ya estaban trackeadas en el `gaps.md` propio de PRD-147, sin cambios.

---
id: 2026-09-18_onboarding_oportunidad_reutilizar_ob_aprobado_cuit
pm: pablo
fecha_captura: 2026-09-18
fuente: "/idea_problem sobre revision_pj_cumplimiento (PRD-256) — surgió al analizar el volumen real de altas de PJ"
producto: onboarding
tema: permitir cuentas nuevas sobre un CUIT ya aprobado sin repetir la revisión completa
tipo: oportunidad
destino_propuesto: 2_areas/direccion/oportunidades.md
tipo_destino: actualizar
contradice: "no"
confianza: media
estado: en_cola
merge_commit:
---

Durante `/idea_problem` sobre `revision_pj_cumplimiento` (PRD-256), al procesar el volumen real de altas de personas jurídicas (export de cuentas Wallet con CUIT de PJ, 2026-09-18), apareció un caso concreto: dentro de una misma organización, un solo CUIT (persona jurídica) puede generar una enorme cantidad de cuentas/sub-cuentas — se detectaron 2 CUIT que por sí solos explican 2.485 filas del export, bajo el mismo `OrganizacionId`.

Esto llevó al PM (Pablo Gomes) a una idea de mejora que **no es parte del proyecto de revisión de Cumplimiento** (ese proyecto es exclusivamente UX de la pantalla de revisión, no reglas de negocio) pero sí es una oportunidad real para el proyecto estratégico de Onboarding: **permitir que una organización cree cuentas nuevas para un CUIT que ya tiene un Onboarding de persona jurídica aprobado, sin tener que repetir la revisión completa de Cumplimiento**. El mecanismo propuesto por el PM: que la organización le pase a Bind el ID de la solicitud de Onboarding ya aprobada para ese CUIT, Bind valide que efectivamente está aprobada, y a partir de ahí permita crear cuentas nuevas asociadas sin re-disparar el flujo completo de carga + revisión de Cumplimiento.

**Por qué importa:** con el mandato de Cumplimiento de exigir que toda alta de persona jurídica pase por el producto de Onboarding PJ (ver `revision_pj_cumplimiento/proyecto.md` y su problem statement en `artefactos/`), organizaciones con alta rotación de sub-cuentas bajo el mismo CUIT podrían generar carga repetida e innecesaria sobre Cumplimiento (que hoy tiene una sola persona cubriendo la revisión) si cada alta de cuenta —incluso de un CUIT ya aprobado— se tratara como un caso nuevo a revisar. Sin este mecanismo, el volumen real que le llega a Cumplimiento podría ser un orden de magnitud mayor al de personas jurídicas genuinamente nuevas.

**Decisión del PM (2026-09-18):** explícitamente estacionada para retomar cuando se hable de personas jurídicas dentro de `proyecto-onboarding-estrategico` — no abre un discovery propio todavía. Ver `revision_pj_cumplimiento/decisiones.md` (2026-09-18) para el registro de por qué queda fuera del alcance de ese proyecto puntual.

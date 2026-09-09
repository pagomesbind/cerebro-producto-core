---
id: 2026-09-09_onboarding_prd202_solution_regenerado
pm: pablo
fecha_captura: 2026-09-09
fuente: "Sesión `/idea_solution` sobre PRD-202 (Fase 1) — regeneración completa del análisis técnico-funcional de la solución"
producto: onboarding
tema: Análisis técnico-funcional de PRD-202 regenerado a v2.0 para reflejar el contrato v6.3 y las 11 historias de usuario ya contractualizadas; hallazgo nuevo sobre la prioridad de PATCH vs. el Must-have del PRD
tipo: iniciativa
proyecto: PRD-202
destino_propuesto: 2_areas/direccion/iniciativas.md
tipo_destino: actualizar
contradice: "no"
confianza: alta
estado: ingestado
merge_commit:
---

El análisis técnico-funcional de la solución de PRD-202 (`onboarding_consolidado-solution.md`) se regeneró de punta a punta, de v1.3 (2026-09-04, sincronizado contra el contrato v6.0) a **v2.0**. En el tiempo transcurrido, el contrato de datos avanzó a v6.3 (agregando `paisNacimiento`, `declaracion.ocde`, `declaracion.detalleUif`, `declaracion.detalleFatca` — todos exigidos por la norma cruzada BCRA/OCDE/FATCA) y las historias de usuario pasaron de un contrato implícito de ~7 endpoints a **11 interfaces plenamente contractualizadas**, agrupadas por frontera de equipo (Wallet↔Organización, Wallet↔Onboarding vía el KYC-wrapper, y 2 historias de configuración/datos sin superficie de API nueva).

**Cambios de fondo del documento:**
- El **KYC-wrapper** deja de figurar como "actor todavía no contractualizado" — ya tiene 4 interfaces propias con contrato cerrado (crear/continuar, detalle completo, aviso de cambio de estado, sondeo de respaldo), y los diagramas de secuencia ya lo muestran como salto explícito en vez de una caja negra.
- El modelo de palancas de validación se simplificó de 3 modos a 2 valores `true`/`false` (2026-09-04), reduciendo el espacio de configuración por organización/flujo.
- Se precisa que el motor de Etapa 2 (cumplimiento normativo — ARCA condición fiscal, UIF, Worldsys, Lista 15) **ya existe y corre en producción** para otros flujos de Onboarding — este proyecto lo adapta al nuevo modelo de palancas, no lo construye desde cero.
- El catálogo de errores se reescribió con los códigos literales reales del contrato (`PAYLOAD_INVALIDO`, `CODIGO_YA_EXISTE`, `SOLICITUD_NO_EDITABLE`, `SOLICITUD_NO_ENCONTRADA`, etc.), reemplazando placeholders de versiones anteriores.
- La clasificación MoSCoW de la consulta completa de una solicitud se alinea a Could-have, siguiendo el feedback que el PM ya había dado sobre el PRD formal en esta misma sesión de trabajo.

**Hallazgo nuevo, no reflejado antes en ningún documento del proyecto (severidad Alta):** al cruzar la clasificación MoSCoW del PRD contra la prioridad real de las historias de usuario, se detectó que `PATCH /cuenta/kyc/{codigo}` (US-8) — el único mecanismo por el cual una organización puede resolver una solicitud que quedó `EN_ESPERA` (dato faltante, documento ilegible, envío fraccionado) — está clasificado P1/Should-have desde el 2026-08-26, pese a que el PRD marca como 🔴 Must-have que las solicitudes puedan quedar a la espera de una acción de la organización. Sin `PATCH` construido, esa espera no tiene forma de resolverse en la práctica hasta que el endpoint exista. Capturado como gap nuevo en `proyecto-onboarding-estrategico/prd-202_onboarding_consolidado/gaps.md` (2026-09-09) — pendiente de decisión del PM/Ingeniería sobre si se lanza el camino genérico sin `PATCH`, o se prioriza junto con la creación pese a su clasificación P1 ya acordada en el roadmap de sprints.

El documento queda todavía en Paso 4 de la skill `/idea_solution` (revisión completa con el PM) — pendiente su OK explícito antes de considerarse cerrado. Sin cambios de alcance, prioridad ni estimación de SP fuera de lo ya descripto.

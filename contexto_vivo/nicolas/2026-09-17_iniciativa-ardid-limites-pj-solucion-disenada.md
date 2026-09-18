---
id: 2026-09-17_iniciativa-ardid-limites-pj-solucion-disenada
pm: nicolas
fecha_captura: 2026-09-17
fuente: "Análisis técnico-funcional /idea_solution (2026-09-17)"
producto: ardid
tema: Segmentación de personas jurídicas en Ardid — análisis técnico-funcional cerrado con OK del PM
tipo: iniciativa
destino_propuesto: 2_areas/direccion/iniciativas.md
tipo_destino: actualizar
contradice: "no"
confianza: alta
estado: en_cola
proyecto: ardid_limites_pj
---

El proyecto `ardid_limites_pj` (segmentación de persona jurídica en Ardid, discovery cerrado el 2026-09-15) avanzó con su análisis técnico-funcional (`/idea_solution`), cerrado con OK explícito del PM tras 3 rondas de corrección.

**Diseño confirmado:**
- **Alta de Organización:** se agrega la creación de un `BankType` de persona jurídica nuevo — **uno por Organización/Entidad, nunca compartido ni reutilizado** — seguido de un `ClientBankType` que lo referencia. Mismo patrón ampliado del precedente de menores (PRD-17), que en su momento solo documentaba el `ClientBankType`, no si hacía falta un `BankType` propio.
- **Alta de Cuenta:** se reutiliza la validación de tipo de persona por CUIT **ya existente en producción** (identificación por primer dígito, "2"=física/"3"=jurídica) para elegir el segmento — no se construye una clasificación nueva. Si la Organización todavía no tiene el segmento PJ (fail-open), la cuenta se crea igual que hoy, sin bloquear el alta.
- **Fuera de alcance:** migración de las 3.740 cuentas/Organizaciones PJ ya existentes — queda como tarea manual de backfill, pendiente de planificar (quién y cuándo).

**Gaps técnicos que quedaron abiertos (no bloqueantes para `/idea_prd`, sí para escribir historias de desarrollo):** valor de `PersonTypeId`/`ClientTypeId` en el catálogo de Ardid (Alta), código real del punto de integración a extender (Alta), mecanismo de reintento ante falla de Ardid (Media), comportamiento ante un CUIT que no empiece ni con "2" ni con "3" (Media, definición del PM), rate limit para el backfill masivo (Baja).

**Próximo paso:** aprobación de Emma Vignoles, luego confirmación técnica de los gaps con Ingeniería/Fintexa, y `/idea_prd`. Sigue compitiendo por capacidad con `ardid_desconocimientos`, `titularidad_tarjeta` y PRD-191 dentro del foco Ardid del mismo PM.

> Fuente: `wiki/1_proyectos/ardid_limites_pj/artefactos/ardid_limites_pj-solution.md`, `wiki/1_proyectos/ardid_limites_pj/decisiones.md`, `wiki/1_proyectos/ardid_limites_pj/gaps.md`.

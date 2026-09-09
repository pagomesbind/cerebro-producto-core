---
id: 2026-09-09_transversal_oportunidad_proceso_formal_desarrollo_productos
pm: pablo
fecha_captura: 2026-09-09
fuente: "Assessment de auditoría del banco tras el fraude de Transferencias Pull (raw/BIND PSP- Assessment 14052026.xlsx, hoja 'Aspectos Identificados', fila área 'Productos' — Ref. sin código Jira, PLAZO-COSTO 90 días, Golive propuesto 2026-06-01). Remediación liderada por Hernán Clarich y Mariana Nadalin."
producto: transversal
tema: Falta de un proceso formal y estandarizado de desarrollo de productos que involucre obligatoriamente a legales, cumplimiento (PLD), riesgos y soporte antes de cada lanzamiento
tipo: oportunidad
destino_propuesto: 2_areas/direccion/oportunidades.md
tipo_destino: actualizar
contradice: "no"
confianza: alta
estado: ingestado
merge_commit:
---

## Qué encontró el banco

El assessment señala que Bind PSP no tiene "un proceso formal y estandarizado para la creación de nuevos productos y funcionalidades" — la validación de un lanzamiento no involucra de manera obligatoria a áreas clave (legales, PLD, riesgos, soporte), lo que "genera vulnerabilidades operativas". El comentario de Producto en el propio assessment (columna COMENTARIOS) ya adelanta una respuesta parcial: "Formalización del plan de Producto, con validaciones de los distintos sectores (producto, Admin, Impuestos, Riesgos, Comercial, IT, Infra, Soporte, Recaudaciones, PLAFT). Este ejercicio se realizó con otros productos como MC Move. Podríamos validar la definición del Proceso con Bind, y luego la aprobación del Producto por CCU."

## Por qué es una oportunidad, no solo un gap de otro

No hay ninguna IDEA en Jira ni proyecto vivo en este Cerebro que ataque este punto de punta a punta. Es, en esencia, formalizar el propio proceso de discovery/PRD de Producto (`/idea_start` → `/idea_prd` → aprobación) agregándole un gate explícito y documentado de sign-off multi-área antes de cualquier lanzamiento — algo que hoy pasa de forma ad hoc (ej. reuniones puntuales, el precedente de MC Move) en vez de estar estandarizado. Complementa, sin superponerse, al Comité de Cambios ya operativo desde v69 (que valida el *pase a producción* técnico) — este proceso ataca la etapa anterior, la *aprobación del producto* como tal.

## Qué haría falta para avanzar

- Confirmar con Emma Vignoles (o quien lidere hoy la validación de nuevos productos) si existe ya un criterio no documentado (más allá del precedente MC Move) que sirva de base.
- Definir el checklist mínimo de sign-off por área (Legales, PLD, Riesgos, Soporte, y las demás mencionadas en el comentario del propio assessment) y en qué instancia del ciclo de vida de un PRD se aplica.
- Evaluar si la instancia final de aprobación es el CCU (Comité de Cambios y Usuarios, mencionado en el comentario) u otra mesa a definir con el banco.

Ver tarea relacionada `T-077` en `tareas.md`.

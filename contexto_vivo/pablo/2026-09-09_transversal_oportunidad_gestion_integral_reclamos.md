---
id: 2026-09-09_transversal_oportunidad_gestion_integral_reclamos
pm: pablo
fecha_captura: 2026-09-09
fuente: "Assessment de auditoría del banco tras el fraude de Transferencias Pull (raw/BIND PSP- Assessment 14052026.xlsx, hoja 'Aspectos Identificados', área 'Riesgos', PRIORIDAD Alta, PLAZO-COSTO 15 días / 45 días). Remediación liderada por Hernán Clarich y Mariana Nadalin."
producto: transversal
tema: Ausencia de un marco de gestión de reclamos — qué empresas/entidades se consideran, qué canales de recepción están habilitados, cómo se registran
tipo: oportunidad
destino_propuesto: 2_areas/direccion/oportunidades.md
tipo_destino: actualizar
contradice: "no"
confianza: alta
estado: en_cola
merge_commit:
---

## Qué encontró el banco

El assessment pide, de forma explícita y asociada al propio incidente de fraude: "evaluar una estrategia de atención para este tipo de reclamos, con el objetivo de minimizar los reclamos de BCRA y Defensa del Consumidor" y "definir un marco de gestión de reclamos, donde se indique cuáles son las empresas a considerar, los canales habilitados de recepción, [y la] registración de los mismos". El comentario del propio assessment lo asocia también al Plan de Adecuación BCRA 2026, aunque sin el mismo nivel de desarrollo que el punto de análisis de riesgo de productos.

## Qué ya existe vs. qué falta

El único antecedente en Jira es **PRD-207** ("Reclamos de transferencias que se registran tarde en BS2.0", PENDIENTE) — un bug puntual sobre un síntoma concreto, no el framework completo que pide el banco. No hay ningún proyecto vivo en este Cerebro que ataque la pregunta de fondo: qué canales de reclamo existen hoy (Soporte, comercial, directo del banco, redes), cómo se registra cada uno, y si hay trazabilidad end-to-end desde que un cliente reclama hasta que se resuelve. Es plausible que el dueño natural del framework sea Soporte, no Producto — pero Producto tiene un rol de cooperación claro: los canales de reclamo dependen de cada producto (Wallet, Cobro, Onboarding) y su registración probablemente requiera cambios de producto (ej. un endpoint o pantalla de reclamo dentro del flujo).

## Qué haría falta para avanzar

- Confirmar con Soporte si ya hay un dueño informal de este tema o si sigue completamente sin asignar.
- Relevar los canales de reclamo hoy activos por producto (Wallet, Cobro/Adquirencia, Onboarding) antes de proponer un marco único.
- Evaluar si PRD-207 debería quedar absorbido como un caso puntual del framework más amplio, una vez que exista.

Ver tarea relacionada `T-077` en `tareas.md`.

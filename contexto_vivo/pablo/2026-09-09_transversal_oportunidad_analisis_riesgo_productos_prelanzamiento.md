---
id: 2026-09-09_transversal_oportunidad_analisis_riesgo_productos_prelanzamiento
pm: pablo
fecha_captura: 2026-09-09
fuente: "Assessment de auditoría del banco tras el fraude de Transferencias Pull (raw/BIND PSP- Assessment 14052026.xlsx, hoja 'Aspectos Identificados', área 'Riesgos', PRIORIDAD Media, PLAZO-COSTO 30 días). Remediación liderada por Hernán Clarich y Mariana Nadalin."
producto: transversal
tema: Ausencia de una evaluación de riesgos formal, previa al lanzamiento de un nuevo producto o al cambio técnico de uno existente
tipo: oportunidad
destino_propuesto: 2_areas/direccion/oportunidades.md
tipo_destino: actualizar
contradice: "no"
confianza: alta
estado: ingestado
merge_commit:
---

## Qué encontró el banco

El punto es puntual: "Ausencia de evaluación de riesgos previa al lanzamiento de un nuevo producto y técnica." La mitigante propuesta es "Definir una estrategia de evaluación de riesgos para los productos vigentes y por salir" y "Robustecer el proceso de autorización ante la salida de nuevo producto". El propio comentario del assessment lo ubica hoy dentro del **"Plan Adecuación BCRA 2026-V1-2"** (Anexo-Adecuación BCRA 2026, ligado a la Com. "A" 8398), con la incorporación propuesta de un Líder de Riesgo Integral (posición nueva, ver Hoja 3 del assessment) para aplicarlo.

## Por qué Producto debería tener un rol activo, no solo receptor

Hoy este framework vive enteramente del lado de Infra/Riesgos (el Plan de Adecuación BCRA), sin que el Cerebro documente ninguna instancia donde Producto aporte la dimensión de riesgo específica de cada producto (volumen, tipo de cliente, superficie de fraude nueva que abre una funcionalidad) antes del lanzamiento. Es exactamente el mismo vacío que expuso el incidente de marzo 2026 (Transferencias Pull activadas sin evaluación de riesgo ni integración a Ardid) — sin un framework de este tipo, cada lanzamiento nuevo repite la apuesta.

Conecta directo con la oportunidad hermana [`2026-09-09_transversal_oportunidad_proceso_formal_desarrollo_productos`] — probablemente ambas terminen siendo la misma mesa/gate, con esta como su componente de análisis de riesgo específico.

## Qué haría falta para avanzar

- Confirmar con Infra/Riesgos el estado real del Plan de Adecuación BCRA 2026 en este punto puntual (dueño, fecha).
- Si se define un Líder de Riesgo Integral, acordar con esa posición el rol de Producto en el análisis (quién aporta qué insumo, en qué momento del ciclo de vida del PRD).
- Evaluar si conviene un framework separado o fusionarlo con el proceso formal de desarrollo de productos.

Ver tarea relacionada `T-077` en `tareas.md`.

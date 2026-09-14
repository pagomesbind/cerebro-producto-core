---
id: 2026-09-14_adquirencia_iniciativa_prd216_golive_pendientes
pm: pablo
fecha_captura: 2026-09-14
fuente: "/idea_golive sobre PRD-216 — auditoría de cierre de proyecto, verificación directa en Jira (issue AD-1434 y comentarios de QA)"
producto: adquirencia
tema: cierre de PRD-216 (Arcos Dorados, mapeo de productos en /resolve) — desarrollo en producción, cierre formal de Producto pendiente
tipo: iniciativa
proyecto: PRD-216
destino_propuesto: 2_areas/direccion/iniciativas.md
tipo_destino: actualizar
contradice: "no"
confianza: alta
estado: ingestado
merge_commit: 122ad74
---

Novedad puntual sobre PRD-216 (Arcos Dorados: mapear productos de la orden de venta en items del `/resolve`, QR eco cerrado) para la fila de la cartera de iniciativas.

El desarrollo (ticket AD-1434) está confirmado **Finalizado/Listo, en producción desde el 31/08/2026** (versión de release "AD 72", liberada). Sin embargo, al auditar el cierre del proyecto contra el estado real en Jira (no solo contra lo ya escrito en la wiki, desactualizada desde el 2026-08-31), la IDEA madre PRD-216 sigue en estado **"Shipping"**, no en un estado de cierre — y aparecieron 4 pendientes no visibles hasta ahora:

1. La aprobación formal de Producto a nivel dirección (Emma Vignoles, COO) nunca quedó confirmada como cerrada — el desarrollo avanzó en paralelo por decisión del PM (bajo riesgo/tamaño), pero el circuito de aprobación formal no se cerró después.
2. El cliente que disparó el caso (Arcos Dorados) solo tiene confirmada por mail la fecha original de pase a producción (27/08), que se reprogramó a último momento al 31/08 por errores de QA en otros componentes del mismo lote de despliegue — no hay evidencia de que se le haya reavisado la fecha final.
3. La corrección introdujo, sin documentarlo en el alcance original, una validación nueva que **rechaza** (antes descartaba en silencio) órdenes de venta cuya suma de precio×cantidad no coincide con el total — riesgo de afectar sin aviso a otros comercios con datos ya "sucios" cargados, sin que se haya comunicado a Soporte.
4. 2 defectos colaterales del webhook de pago, detectados en QA (no informa el código del producto; omite el array completo de productos si el código es muy largo), catalogados como no bloqueantes para este pase puntual pero siguen abiertos sin fecha.

El checklist completo de auditoría, con el detalle de cada punto, quedó persistido en `1_proyectos/prd-216_arcos_dorados_productos_resolve/artefactos/arcos_dorados_productos_resolve-golive.md` (fuera del alcance de este item — referencia solo para quien mergee, no es contenido a copiar al canon).

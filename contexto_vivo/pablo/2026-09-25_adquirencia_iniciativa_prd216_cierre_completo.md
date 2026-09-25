---
id: 2026-09-25_adquirencia_iniciativa_prd216_cierre_completo
pm: pablo
fecha_captura: 2026-09-25
fuente: "/idea_golive sobre PRD-216 — resolución de los 4 pendientes que había dejado abiertos la auditoría de go-live del 2026-09-14"
producto: adquirencia
tema: PRD-216 (Arcos Dorados, mapeo de productos en /resolve) — los 4 pendientes de la auditoría de go-live quedaron resueltos
tipo: iniciativa
proyecto: PRD-216
destino_propuesto: 2_areas/direccion/iniciativas.md
tipo_destino: actualizar
contradice: "2_areas/direccion/iniciativas.md, fila PRD-216 (entrada 2026-09-14) — describe los 4 pendientes como abiertos; esta entrada los reporta todos resueltos/migrados el 2026-09-25"
confianza: alta
estado: ingestado
merge_commit:
---

Novedad puntual sobre PRD-216 para anteponer a la fila existente en la cartera de iniciativas (la entrada del 2026-09-14 describe 4 pendientes que ya se resolvieron).

Los 4 puntos que había dejado abiertos la auditoría de go-live (`/idea_golive`, 2026-09-14) se resolvieron el 2026-09-25, todos por decisión directa del PM:

1. **Aprobación formal de Producto a nivel dirección:** se ratifica avanzar sin ella — el cliente necesitaba el fix rápido y era un bug preexistente del propio sistema de Bind PSP, no una funcionalidad nueva a criterio de negocio.
2. **Reaviso de fecha a Arcos Dorados:** se avisó de forma informal en su momento. Dato nuevo y más relevante: **Arcos Dorados se está bajando del proyecto por problemas internos de su lado** (sin más detalle todavía) — le quita efecto práctico a este punto, pero es una señal aparte que se capturó por separado para Comercial (ver item de tipo `riesgo` del mismo día, `2026-09-25_clientes_arcos_dorados_posible_salida_proyecto`).
3. **Cambio de comportamiento no documentado (rechazo HTTP 422 de órdenes con total inconsistente):** el PM confirmó que no hubo problemas detectados en clientes. Al ser el resultado esperado de la corrección (el comportamiento anterior era el bug), se decide explícitamente no comunicarlo a Soporte ni a los comercios.
4. **2 defectos colaterales de QA (AD-1633/AD-1634, webhook de pago):** migrados por el PM al proyecto Ministerio de Justicia (PRD-134, "Asociar productos en BS 2.0 y POS") por ser el mismo mecanismo de productos en transacciones — verificado en Jira, ambos tickets ya cuelgan del Epic AD-374 de ese proyecto.

Con esto, PRD-216 queda sin pendientes abiertos desde Producto (aunque la IDEA sigue en estado "Shipping" en Jira, sin que el PM haya priorizado forzar un estado de cierre formal). Detalle completo en `1_proyectos/prd-216_arcos_dorados_productos_resolve/decisiones.md` (2026-09-25) y `artefactos/arcos_dorados_productos_resolve-golive.md`.

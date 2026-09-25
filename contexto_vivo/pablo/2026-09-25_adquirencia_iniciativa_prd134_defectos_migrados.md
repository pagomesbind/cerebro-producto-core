---
id: 2026-09-25_adquirencia_iniciativa_prd134_defectos_migrados
pm: pablo
fecha_captura: 2026-09-25
fuente: "/idea_golive sobre PRD-216 — el PM migró 2 defectos de QA a este proyecto al cerrar la auditoría de go-live de PRD-216"
producto: adquirencia
tema: PRD-134 (Ministerio, asociar productos) recibe 2 defectos de QA migrados desde PRD-216
tipo: iniciativa
proyecto: PRD-134
destino_propuesto: 2_areas/direccion/iniciativas.md
tipo_destino: crear
contradice: "no"
confianza: alta
estado: en_cola
merge_commit:
---

Novedad puntual sobre PRD-134 (MINISTERIO: Asociar productos en BS 2.0 y POS) para la cartera de iniciativas — no tenía fila propia hasta ahora.

Al cerrar la auditoría de go-live de PRD-216 (Arcos Dorados, mapeo de productos en `/resolve`), el PM decidió migrar 2 defectos de QA detectados ahí al Epic de este proyecto (AD-374, "Ministerio de Justicia - Asociar productos a transacción"), por tratarse del mismo mecanismo de productos en transacciones y no ser específicos de Arcos Dorados:

- [AD-1633](https://bindpsp.atlassian.net/browse/AD-1633) — el webhook de pago no informa el código del producto aunque esté cargado en la orden de venta.
- [AD-1634](https://bindpsp.atlassian.net/browse/AD-1634) — el webhook de pago omite el array completo de productos cuando el código/descripción es muy largo.

Verificado en Jira: ambos tickets ya cuelgan del Epic AD-374. Estado "En curso", prioridad Medium, sin fecha de resolución comprometida. Detalle en `1_proyectos/proyecto-ministerio/prd-134_ministerio_productos_bs20_pos/proyecto.md` §4/§9 (2026-09-25).

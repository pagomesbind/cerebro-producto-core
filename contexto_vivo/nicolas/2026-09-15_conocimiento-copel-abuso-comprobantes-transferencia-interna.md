---
id: 2026-09-15_conocimiento-copel-abuso-comprobantes-transferencia-interna
pm: nicolas
fecha_captura: 2026-09-15
fuente: "Reunión 'W 72.3 (Pagos FX) y Modificaciones en los Proxys de PRD - Análisis de riesgos' (2026-09-11)"
producto: wallet
tema: Entidad "Copel" usa hace dos meses comprobantes de transferencia interna reservados para el sistema, en vez de generar la operación real
tipo: conocimiento
destino_propuesto: 3_recursos/detalle_productos/wallet/transferencias_red_interna.md
tipo_destino: actualizar
contradice: "no"
confianza: media
estado: ingestado
merge_commit: 0b463d974f85a1b19919f0b7ae5d338c8da68ec8
---

**Fuente:** reunión "W 72.3 (Pagos FX) y Modificaciones en los Proxys de PRD - Análisis de riesgos" (2026-09-11), Gonzalo Damian Rivera.

Gonzalo Damian Rivera reportó que la entidad **Copel** lleva **dos meses** haciendo sus operaciones internas resolviéndolas por comprobante de transferencia interna —un tipo de comprobante reservado para uso del sistema— en lugar de generar la operación real. Consecuencia: quedan comprobantes creados pero sin la operación asociada. Bind ya les avisó hace dos meses que debían dejar de hacerlo; Gonzalo propuso bloquearles directamente el uso de ese tipo de comprobante para forzar el corte ("se quedarán sin operar"). No quedó registrada como decisión formal en la minuta (no aparece en la sección "Decisiones" de la reunión) — es una propuesta verbal de Gonzalo Rivera, a confirmar si se ejecutó.

**Nota:** "Copel" no tiene ficha propia en `2_areas/clientes/log_clientes.md` — ya apareció antes en el Cerebro como mención relacionada a "La Virginia" (endpoint de alta de cuenta comitente compartido, reunión "Weekly" 2026-09-07/14), sin quedar claro si es un cliente propio o una entidad relacionada/interna a otro cliente.

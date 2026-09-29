---
id: 2026-09-25_adquirencia_esfuerzo_real_prd216
pm: pablo
fecha_captura: 2026-09-25
fuente: "Proyecto PRD-216 (Arcos Dorados: mapear productos de la orden de venta en items del Resolve), finalizado 2026-09-25 — cierre vía /idea_finish. SP real = customfield_10041 de AD-1434, verificado directo en Jira"
producto: adquirencia
tema: historial de esfuerzo real de PRD-216 para referencia de estimaciones futuras
tipo: conocimiento
destino_propuesto: 2_areas/procesos/referencia_estimaciones.md, sección "## Jira (`bindpsp.atlassian.net`) — IDEAs de Producto" — nueva entrada al final
tipo_destino: actualizar
contradice: "no"
confianza: alta
estado: ingestado
merge_commit: 9fbee64
---

Nueva entrada para la sección de IDEAs de Jira, mismo formato que las ya existentes (PRD-115, PRD-87, PRD-81):

### Arcos Dorados: mapear productos de la orden de venta en items del Resolve — IDEA PRD-216 (Finalizada, Go Live 2026-08-31)

**Qué se construyó:** corrección del mapeo de productos de la orden de venta en el endpoint de lectura de QR (`/resolve`, `PaymentAcceptor.Iep`) — de un ítem sintético hardcodeado a un ítem real por producto (1:1), con nueva validación de cuadratura de montos (rechazo HTTP 422 si no cuadra). Detalle: [adquirencia/botones_de_pago_y_qr.md, sección Arcos Dorados](../../3_recursos/detalle_productos/adquirencia/botones_de_pago_y_qr.md).

**Esfuerzo:** 3 Story Points estimados = 3 Story Points reales (único ticket de desarrollo, AD-1434) — estimación exacta, caso poco común. Epic AD-1433 con 8 tickets: 1 Historia de desarrollo + 7 subtareas de test explícitas por escenario (mapeo con uno/varios productos, fallback de título, estados no cerrados, independencia del flag `RequiereProductos`, validación de cuadratura 422, truncado de 50 caracteres), todas Finalizadas sin regresiones. **Lectura para estimaciones futuras:** diseñar los casos de test como subtareas explícitas desde el arranque (no solo un checklist de QA informal) sostuvo la estimación original sin desvío — pero de todos modos surgieron 2 defectos colaterales en el webhook de pago (endpoint vecino, no el corregido), consistente con el patrón ya visto en PRD-87/PRD-81: un dato compartido entre varios endpoints (acá, productos de la orden de venta reflejados tanto en `/resolve` como en el webhook) tiende a destapar bugs en el endpoint vecino que nadie estaba mirando, incluso cuando el ticket principal sale sin sorpresas.

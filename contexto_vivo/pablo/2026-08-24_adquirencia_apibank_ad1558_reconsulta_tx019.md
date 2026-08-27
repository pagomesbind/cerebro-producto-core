---
id: 2026-08-24_adquirencia_apibank_ad1558_reconsulta_tx019
pm: pablo
fecha_captura: 2026-08-24
fuente: "/sync_meetings — reunión 'Análisis COBRO' (docId 11mHIK-2tgdcnOuz_crGedaBDbWHp0IgnWHJupNmkPyU), 2026-08-24"
producto: adquirencia
tema: "Ticket AD-1558 (Apibank) — reconsulta indebida guardando TX019 tras rechazo por TX021, baja prioridad"
tipo: conocimiento
destino_propuesto: 3_recursos/detalle_productos/adquirencia/pedidos_de_clientes_y_hallazgos_operativos.md
tipo_destino: actualizar
contradice: "no"
confianza: media
estado: en_cola
merge_commit:
---

## Ticket AD-1558 — comportamiento de reconsulta de Apibank ante transferencia rechazada

**Descripción:** reportado originalmente por Ana. Al guardar las consultas de Apibank, se dispara una reconsulta que guarda un `TX019` incluso cuando la creación de la transferencia fue **rechazada por validación** mediante un `TX021`. Es decir, el sistema registra el código de éxito de reconsulta (`TX019`) aunque la operación de origen haya sido rechazada (`TX021`).

**Estado y decisión de priorización (2026-08-24):** Nicolás Colón (Bind) verificó que no se registraron casos de `TX021` en producción en los últimos 30 días — dado la baja frecuencia observada, el equipo decidió **bajar la prioridad del ticket, dejarlo pendiente sin desarrollo inmediato**, y mantenerse atentos ante cualquier eventualidad futura en producción. No se prioriza para la versión de septiembre (ver [`2026-08-24_adquirencia_decision_prioridades_producto_septiembre`](2026-08-24_adquirencia_decision_prioridades_producto_septiembre.md)).

**Nota de ubicación:** este hallazgo puede pertenecer más a `arquitectura_sistema/` que a `adquirencia/` si Apibank se documenta ahí como integración de core bancario — `/context_merge` puede reubicarlo si corresponde; se propone `adquirencia/` porque el ticket nace en el espacio Jira `AD`.

> Fuente: Reunión "Análisis COBRO" (2026-08-24), minuta Gemini — comentario de Daniela Collia (Fintexa), verificación de Nicolás Colón (Bind).

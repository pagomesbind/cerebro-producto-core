---
id: 2026-08-21_adquirencia_bug_contracargo_tipo_devolucion_anulacion_pos
pm: pablo
fecha_captura: 2026-08-24
fuente: "/sync_mails — mail 'Análisis de riesgos AD V 72: Vie, 21 de ago de 2026' (threadId `1a025f5dceef64ef`), mensaje de Nicolás Colón, 2026-08-21"
producto: adquirencia
tema: Bug de tipo de operación en contracargos de devolución/anulación POS GP (AD-1020/AD-1579) detectado en el análisis de riesgo de AD V72
tipo: conocimiento
destino_propuesto: 3_recursos/detalle_productos/adquirencia/devoluciones_y_contracargos.md
tipo_destino: actualizar
contradice: "no"
confianza: alta
estado: ingestado
merge_commit:
---

Durante la reunión de análisis de riesgos de la versión AD V72 (pase a producción programado 27/08/2026, 21:00hs, ventana de 3hs), Nicolás Colón detectó un bug asociado al ticket **AD-1020/DAD-1673** ("Lógica de devolución/anulación POS GP — Guardar detalle en contracargo"), que forma parte de esa misma versión:

**El problema:** la tabla de Contracargos debe guardar siempre el tipo de operación como `Tipo="contracargo"` cuando se registra una devolución o anulación hecha desde POS con Global Processing — hoy ese campo queda con el valor genérico "Devolucion" en vez de distinguir explícitamente el tipo real de operación (anulación same-day vs. devolución de días previos).

**La corrección:** un ticket adicional, **AD-1579**, resuelve este comportamiento. Nico recomendó sumar AD-1579 a la misma versión AD V72, "mitigando así el riesgo que presenta el ticket original [AD-1020] por sí solo" — es decir, sin AD-1579, el ticket AD-1020 se desplegaría con este bug de tipo mal guardado.

Contexto de la versión (para ubicar el hallazgo): AD V72 modifica el esquema de devolución/anulación en POS distinguiendo transacciones del mismo día (anulación) de días anteriores (devolución), afecta ~20 microservicios (PaymentAcceptor.Deuda, Bff.CardPresent, PaymentAcceptor.CardOrchestrator, etc.) y aplica cambios estructurales a CVU Collect. El ticket AD-1020 fue marcado en la minuta de riesgo con semáforo 🔴🔴🔴 (riesgo alto) y acción "PRE-IMPLEMENTACIÓN: Avisar a clientes" — la tabla de contracargos que consumen los clientes en sus archivos podría verse afectada por el cambio de estructura.

> Fuente: Mail "Análisis de riesgos AD V 72: Vie, 21 de ago de 2026 a las 2:00pm – 3:30pm (GMT-03)" — Nicolás Colón (respuesta dentro del hilo iniciado por Matías Alzogaray), 2026-08-21.

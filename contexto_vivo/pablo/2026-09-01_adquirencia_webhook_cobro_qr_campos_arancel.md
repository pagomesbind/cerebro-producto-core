---
id: 2026-09-01_adquirencia_webhook_cobro_qr_campos_arancel
pm: pablo
fecha_captura: 2026-09-01
fuente: "/sync_meetings — reunión 'Análisis COBRO' (2026-08-31 12:01, minuta Gemini)"
producto: adquirencia
tema: Webhook de transacción exitosa de Cobro QR suma campos de arancel aceptador e importe neto
tipo: conocimiento
destino_propuesto: 3_recursos/detalle_productos/adquirencia/webhooks_y_notificaciones.md
tipo_destino: actualizar
contradice: "no"
confianza: alta
estado: ingestado
merge_commit:
---

Se acordó agregar al webhook de transacción exitosa de **Cobro con QR** tres campos nuevos: **arancel aceptador (porcentaje)**, **arancel aceptador (importe)** e **importe neto** (tras aplicar el arancel). El objetivo explícito es que el consumidor del webhook no tenga que hacer una llamada adicional de consulta de la transacción para obtener estos datos — hoy solo vienen en el detalle vía API, no en el evento. Sin ticket específico identificado en la minuta más allá del compromiso genérico ("el grupo" lo lleva adelante).

También en la misma reunión: se retoma la **segunda parte de las mejoras de performance para la generación de archivos** (liquidación/rendiciones), tras haber cerrado la primera parte en una corrida anterior — Nicolás Colón consulta con "Euge" si las demoras/errores detectados están relacionados con el rendimiento de la API antes de avanzar. Sin detalle técnico adicional en la minuta sobre qué archivo/proceso puntual.

> Fuente: Reunión "Análisis COBRO" (2026-08-31), minuta Gemini — sección Decisiones/Próximos pasos.

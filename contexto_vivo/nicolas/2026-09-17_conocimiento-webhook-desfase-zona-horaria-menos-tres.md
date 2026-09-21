---
id: 2026-09-17_conocimiento-webhook-desfase-zona-horaria-menos-tres
pm: nicolas
fecha_captura: 2026-09-17
fuente: "Reunión 'Análisis COBRO' (2026-09-17), minuta Gemini"
producto: adquirencia
tema: Bug de implementación en webhooks — hora de pago enviada con el desfase -3 omitido, generando confusión horaria a los clientes; decisión pendiente (revertir vs. exigir integración correcta)
tipo: conocimiento
destino_propuesto: 3_recursos/detalle_productos/adquirencia/webhooks_y_notificaciones.md
tipo_destino: actualizar
contradice: "no"
confianza: alta
estado: ingestado
merge_commit: 70dcf2a
---

> **Nota de merge (2026-09-21):** duplicado del mismo hallazgo capturado independientemente por Pablo Gomes (`pablo/2026-09-18...adquirencia_webhook_qr_desfase_horario_gmt3`, ya ingerido el 2026-09-18 en `webhooks_y_notificaciones.md §"Bug de zona horaria en el webhook de pagos QR"`) — mismo ticket 1448/494, misma fecha de implementación (31/08), mismo estado "decisión pendiente". No se reescribe contenido, la sección ya vigente en el canon cubre este item sin pérdida de información.

Melisa Belpassi (Fintexa) reportó una incidencia detectada vía ticket de soporte: los webhooks de pago están enviando la hora de la transacción **con el desfase horario `-3` omitido**, generando confusión en los clientes al recibir, por ejemplo, `21:58 -3` en vez de la hora real `18:58` (la resta ya no se aplica sobre el valor mostrado). Melisa asumió la responsabilidad por el error de implementación, ocurrido en el ticket `1448` (identificado internamente como `494`) el pasado 31 de agosto de 2026 — señaló que el análisis de riesgo original y las respuestas del PDR de esa fecha no generaron una alerta suficientemente enfática sobre el impacto.

**Estado: sin decisión, escalado.** El caso fue derivado a "Maru" para discutirlo con "Gono" (Gonzalo Rivera), evaluando dos alternativas: (1) revertir el cambio, aunque eso implica volver al estado incorrecto anterior, o (2) exigir a los clientes que integren correctamente considerando el `-3`. Clasificado en la minuta como "Requiere más debate" (no acordado).

> Fuente: Reunión "Análisis COBRO" (2026-09-17), minuta Gemini — sección Decisiones ("Requiere más debate") y Detalles.

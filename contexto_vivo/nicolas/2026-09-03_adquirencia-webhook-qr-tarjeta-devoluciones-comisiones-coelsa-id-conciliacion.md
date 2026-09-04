---
id: 2026-09-03_adquirencia-webhook-qr-tarjeta-devoluciones-comisiones-coelsa-id-conciliacion
pm: nicolas
fecha_captura: 2026-09-03
fuente: "Reunión \"Análisis COBRO\" (2026-09-03)"
producto: adquirencia
tema: Tres decisiones acordadas sobre el webhook de QR Tarjeta — endpoint separado para devoluciones, comisiones de Coelsa incluidas con sus decimales originales, e ID Coelsa en el comprobante de acreditación en wallet para conciliación
tipo: conocimiento
destino_propuesto: 3_recursos/detalle_productos/adquirencia/webhooks_y_notificaciones.md
tipo_destino: actualizar
contradice: "no"
confianza: alta
estado: en_cola
---

En la reunión recurrente "Análisis COBRO" (2026-09-03) se acordaron tres definiciones sobre el circuito de **QR Tarjeta**:

1. **Alcance del webhook y endpoint de devoluciones:** Daniela Collia (Fintexa) planteó que el ticket de herramientas administrativas ("admin y dos") necesita gestionar reembolsos, pero el webhook actual de QR Tarjeta solo notifica pagos aprobados/rechazados — no se puede reutilizar esa lógica para devoluciones. Se acordó **limitar el webhook existente a pagos aprobados/rechazados** y **crear un nuevo endpoint específico para devoluciones de QR tarjeta**.
2. **Comisiones de Coelsa en el webhook:** hoy el webhook solo envía el importe neto y las entidades deben consultar la comisión por otra vía. Se acordó **incluir las comisiones de Coelsa en el webhook**, manteniendo la cantidad de decimales tal como las provee Coelsa (duda abierta de Daniela Collia entre truncar a 2 decimales o mantener los 7 que existen en la base — Pablo Antonio Gomes resolvió que se debe enviar tal cual la provee Coelsa; Daniela Collia queda en confirmar el formato exacto contra la documentación de Coelsa).
3. **ID Coelsa en comprobantes de wallet:** Nicolás Colón propuso insertar el **ID Coelsa en el campo "ID externo"** de los comprobantes de acreditación en wallet, para que el equipo de administración pueda conciliar sin el proceso manual/duplicado actual (hoy el campo de referencia trae el ID de transacción propio, no el de Coelsa).

Quedó pendiente de más debate (no acordado) si el ticket 361/2209 —corrección del PDF de liquidaciones para Coto, diferenciando "desconocimiento" de "devolución"— entra en la versión 73 o 74; depende de la prioridad que confirme Euge.

> Fuente: Reunión "Análisis COBRO" (2026-09-03), minuta Gemini.

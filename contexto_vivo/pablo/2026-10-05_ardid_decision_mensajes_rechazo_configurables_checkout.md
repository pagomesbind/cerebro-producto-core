---
id: 2026-10-05_ardid_decision_mensajes_rechazo_configurables_checkout
pm: pablo
fecha_captura: 2026-10-05
fuente: "/sync_meetings — reunión 'Weekly - Producto / Operaciones', 2026-10-05 15:01, minuta Gemini + transcripción (compartida, mnadalin)"
producto: ardid
tema: decisión de implementar mensajes de rechazo configurables en el checkout del botón de pago, según el motivo específico de Ardid
tipo: decision
destino_propuesto: 3_recursos/detalle_productos/ardid/integracion_con_productos_bind.md
tipo_destino: actualizar
contradice: "no"
confianza: alta
estado: en_cola
merge_commit:
---

**Problema planteado (Gonzalo Rivera, Pablo Gomes, reunión "Weekly - Producto / Operaciones", 2026-10-05):** hoy el mensaje de rechazo en el checkout del botón de pago es genérico ("Intente nuevamente"), independientemente del motivo real del rechazo. Esto provoca que el cliente final reintente múltiples veces con la misma tarjeta, sin saber que el motivo (p. ej. bloqueo antifraude de Ardid) hace que el reintento nunca vaya a funcionar.

**Decisión:** implementar mensajes configurables en el checkout, basados en el **motivo específico de rechazo recibido desde Ardid** (no el mensaje genérico actual).

**Hallazgo relacionado en la misma conversación — bloqueo por hash de tarjeta:** Mariana Nadalin reportó que una parte importante de los rechazos de Ardid (**52% entre el 1 y el 4 de octubre**) se debe al bloqueo por hash de tarjeta — Ardid genera un hash a partir de los datos de la tarjeta (incluida la fecha de vencimiento) y bloquea reintentos cuando detecta errores de tipeo en esos datos, impidiendo reintentos legítimos del mismo usuario con los datos correctos. Pablo Gomes y Gonzalo Rivera debatieron si eliminar esa validación o establecer un límite de intentos — sin decisión cerrada; Luciana Rudaz tomó el ticket en su tablero para analizar una solución con el equipo.

**Nota de precedente:** la mecánica de bloqueo permanente de tarjeta por hash (ligado al primer vencimiento cargado) ya está documentada en `ardid/modulo_pagos.md §14` (reunión "ARDID" 2026-08-24) — este hallazgo aporta el dato cuantitativo nuevo (52% de los rechazos en un rango de 4 días) y reabre la discusión de si la regla debe eliminarse o acotarse con un límite de intentos.

---
id: 2026-10-06_conocimiento-ardid-rechazos-hash-alertas-configurables-identificador-regla
pm: nicolas
fecha_captura: 2026-10-06
fuente: "Reunión \"Weekly - Producto / Operaciones\" (2026-10-05), solo resumen del mail de Gemini (Drive invalidado, sin minuta completa)"
producto: ardid
tema: Pedidos operativos sobre Ardid — desbloqueo de tarjetas por hash, frecuencia configurable de alertas de fraude por mail, identificador de regla y código de error en los reportes de rechazos, mensajes de rechazo configurables
tipo: conocimiento
destino_propuesto: 3_recursos/detalle_productos/ardid/reporteria_alertas.md
tipo_destino: actualizar
contradice: "no"
confianza: media
estado: en_cola
---

**Pedidos de Operaciones y Producto sobre Ardid (Weekly del 2026-10-05):**

1. **Bloqueos por hash.** Hay tarjetas bloqueadas por rechazos asociados al hash de la tarjeta, y hoy cuesta identificarlas y desbloquearlas. Mariana Nadalin carga un ticket para identificar y desbloquear esas tarjetas, y para evitar bloqueos innecesarios. Contexto en el canon: `ardid/modulo_pagos.md` documenta la identificación de tarjetas por hash y el bloqueo permanente por hash de vencimiento.
2. **Frecuencia de alertas de fraude por mail.** Se pide que la recepción de alertas de fraude por mail se pueda configurar como diaria, semanal o mensual. Mariana Nadalin gestiona el pedido con Ardid.
3. **Análisis de rechazos.** Luciana Rudaz investiga los rechazos de transacciones por Ardid, con el motivo y el código de error de cada caso. Para eso, Nicolás Colón incluye el **identificador de la regla** que disparó el rechazo en los reportes de rechazos de Ardid.
4. **Mensajes de rechazo configurables.** El resumen menciona "implementar mensajes de rechazo configurables" junto al análisis de rechazos y contracargos. No dice de qué producto ni de qué lado (Ardid o el producto que muestra el mensaje). Se relaciona con el mapeo de motivos de rechazo de Ardid en Onboarding (T-006).

> Fuente: Reunión "Weekly - Producto / Operaciones" (2026-10-05), resumen del mail de Gemini.

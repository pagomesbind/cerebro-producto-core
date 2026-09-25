---
id: 2026-09-23_conocimiento-boton-simple-motivo-rechazo-ardid
pm: nicolas
fecha_captura: 2026-09-23
fuente: "Charla directa con el PM (Nicolás Colón) durante /idea_us de titularidad_tarjeta (PRD-25), 2026-09-23"
producto: Adquirencia (Botón Simple)
tema: Cómo queda registrada hoy una transacción de Botón Simple que rechaza Ardid
tipo: conocimiento
destino_propuesto: 3_recursos/detalle_productos/adquirencia/herramientas_operativas_boton_simple.md
tipo_destino: actualizar
contradice: "no"
confianza: alta
estado: ingestado
merge_commit: 2bc1252
---

Cuando el motor antifraude (Ardid) rechaza por reglas propias un pago con tarjeta de Botón Simple, el flujo no se corta sin dejar rastro. Sigue adelante y registra la transacción con estado **RECHAZADA** y motivo de rechazo **"Rechazada por Ardid"**. Es el comportamiento vigente en producción, confirmado por el PM el 2026-09-23 al corregir una historia de usuario que decía "el flujo termina ahí".

Sirve a Soporte para diagnosticar un reclamo por pago rechazado: ese motivo identifica que el rechazo vino del antifraude y no del procesador.

**Contexto a futuro, todavía no es canon:** el proyecto de validación de titularidad de tarjeta (PRD-25, historias AD-1815 a AD-1817) va a sumar un motivo nuevo, "Rechazo por MODO", para las transacciones que el servicio externo de validación de titularidad rechace. Solo se debería incorporar como comportamiento vigente cuando ese desarrollo esté en producción.

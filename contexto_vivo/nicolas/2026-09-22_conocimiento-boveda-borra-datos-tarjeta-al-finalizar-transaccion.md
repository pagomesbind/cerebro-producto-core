---
id: 2026-09-22_conocimiento-boveda-borra-datos-tarjeta-al-finalizar-transaccion
pm: nicolas
fecha_captura: 2026-09-22
fuente: "Confirmación directa del PM durante /idea_solution sobre titularidad_tarjeta (2026-09-22)"
producto: Adquirencia (Botón Simple)
tema: Bóveda (guardado de tarjeta para pagos recurrentes) solo retiene los datos de la tarjeta durante la transacción en curso, no entre transacciones
tipo: conocimiento
destino_propuesto: 3_recursos/detalle_productos/adquirencia/boton_simple_2_0.md
tipo_destino: actualizar
contradice: "no"
confianza: alta
estado: ingestado
---

Durante el análisis técnico-funcional de `titularidad_tarjeta` se evaluó apoyar un mecanismo nuevo (caché de validaciones de titularidad para pagos recurrentes) en Bóveda — el guardado de tarjeta de Botón Simple para pagos recurrentes. El PM confirmó que **Bóveda solo retiene los datos de la tarjeta hasta que finaliza la transacción en curso; se borran al terminar, no persisten entre transacciones**.

Esto descarta a Bóveda como fuente de cualquier mecanismo que necesite "recordar" datos de una tarjeta entre distintos cobros (ej. evitar re-consultar un servicio externo en cada cobro recurrente de la misma tarjeta) — cualquier proyecto futuro con esa necesidad tiene que construir su propio mecanismo de persistencia, no puede asumir que Bóveda ya lo resuelve.

---
id: 2026-09-11_conocimiento-ardid-fix-estados-tarjetas-solucion-temporal-mongodb-sql-server
pm: nicolas
fecha_captura: 2026-09-11
fuente: "Mail 'RE: Análisis de Riesgo - Fix de cambios de estados de las tarjetas' — Osmel Mata (Fintexa), 2026-09-10"
producto: ardid
tema: Fix de estados de pagos/Corrección BIN (01/09) — solución temporal en Mongo, SQL Server sin resolver, posible upgrade a v1.19.x
tipo: conocimiento
destino_propuesto: 3_recursos/detalle_productos/ardid/despliegues_y_operacion.md
tipo_destino: actualizar
contradice: "no"
confianza: alta
estado: en_cola
---

Osmel Mata (Fintexa, SRE Sr) respondió en el hilo del fix "Análisis de Riesgos Fix actualización estado pagos | Corrección BIN" (publicado en PROD el 01/09) con el estado real del despliegue, a pedido de Matías Alzogaray:

- El despliegue del 01/09 se aplicó **sin inconvenientes**. La vista de Pagos en la consola web quedó corregida y se regularizaron los **250.000 registros** que estaban trabados en estado `PENDING`.
- Esa regularización fue una **solución temporal**: implica seguir corriendo **manualmente un script sobre la base de datos MongoDB de Ardid** para ir moviendo esos registros de `PENDING` a `Realized`, hasta que el equipo de desarrollo de Pentass encuentre una solución permanente de fondo.
- Del lado de **SQL Server**, el fix implementado **no parece haber funcionado** como se esperaba; Fintexa sigue trabajando en conjunto con el equipo de soporte de Pentass para normalizarlo.
- Hay indicios (sin confirmación oficial ni documentación todavía) de que se está evaluando pasar Ardid/Akurtech de la versión actual **v1.18.2** a la **v1.19.x**, con la expectativa de que sea más estable.

> Fuente: Mail "RE: Análisis de Riesgo - Fix de cambios de estados de las tarjetas: Vie, 28 de ago de 2026..." — Osmel Mata (osmel.mata@fintexa.tech), 2026-09-10.

Nota: este mismo hilo tiene la pregunta específica de Matías a Nicolás Colón (si el bypass del fix interrumpe la creación de cuentas, cruzando Ardid vs. Wallet) todavía sin responder — trackeada como **T-040** en `tareas.md`, no incluida en este item por ser tarea personal pendiente, no conocimiento confirmado.

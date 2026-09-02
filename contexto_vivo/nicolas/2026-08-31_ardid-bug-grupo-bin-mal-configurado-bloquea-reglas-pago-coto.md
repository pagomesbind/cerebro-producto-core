---
id: 2026-08-31_ardid-bug-grupo-bin-mal-configurado-bloquea-reglas-pago-coto
pm: nicolas
fecha_captura: 2026-08-31
fuente: "Reunión \"FIX - Pagos\" (2026-08-26)"
producto: ardid
tema: Bug real — el filtro de grupo BIN en Ardid quedó configurado en "todos" sin ningún grupo asignado, por lo que las reglas de pago nunca llegaban a impactar
tipo: conocimiento
destino_propuesto: 3_recursos/detalle_productos/ardid/integracion_con_productos_bind.md
tipo_destino: actualizar
contradice: "no"
confianza: alta
estado: ingestado
---

En la reunión "FIX - Pagos" (2026-08-26, con Hernan Clarich, Rocio Revelli, Matias Alzogaray, Nicolás Colón, Andrea Orsini y Osmel Mata) surgió, al analizar un fix de Pentas para corregir estados de transacciones, un segundo problema más grave: dentro de Ardid, uno de los filtros de reglas de pago es por grupo BIN, y en la entidad afectada ese filtro estaba configurado únicamente con la opción "todos" sin ningún grupo BIN específico asignado. Como consecuencia, **las reglas de monitoreo de pago nunca estaban impactando** — si una transacción se rechazaba, era por otro motivo, nunca por estas reglas. El equipo (Rocio Revelli y Lorena Macedo, Fintexa) detectó que el mismo fix de Pentas que corrige el estado de la primera transacción (ver ítem de conocimiento separado si se documenta) también resuelve este problema de grupo BIN.

Contexto del fix relacionado: la gente de Pentas envía un patch para corregir el estado que muestra el front en la primera transacción de una tarjeta cuando Ardid no encuentra el hash de 16 dígitos asociado — hoy esas operaciones quedan mostradas como "pendiente" sin reflejar el estado real (aprobada o rechazada). El paquete no requiere compilación (imágenes Docker de API de transacciones + servicio de transacciones, actualizador de base de datos SQL Server/MongoDB, manual). Decisión del equipo: desplegar primero en Staging para pruebas de regresión de QA antes de producción (excepción solo si hay algo crítico ardiendo). Se pospuso la implementación para no interferir con el pase de AD V72 (compromiso de cliente, 38-40 historias de usuario esa misma noche); Osmel Mata estimó que la migración de base de datos podría requerir una ventana de mantenimiento de ~1 hora en producción (en el entorno de prueba de Fintexa tardó <5 min, pero con menor volumen de datos que el de Bind PSP) — a coordinar con el cliente Coto, que no tiene forma de ser "bypaseado" en la ventana nocturna.

Esta misma falla de grupo BIN de Coto reaparece mencionada en la reunión "Priorización de despliegues" (2026-08-28): Mariana Nadalin señaló que "no estaban haciendo validaciones de las reglas" desde la semana anterior, generando alto rechazo en Payway, y que el fix inicial introducido el 26 de agosto estaba mal y requirió correcciones adicionales vinculadas al ID de comercio.

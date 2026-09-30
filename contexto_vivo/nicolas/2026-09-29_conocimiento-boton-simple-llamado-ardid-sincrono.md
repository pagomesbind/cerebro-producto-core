---
id: 2026-09-29_conocimiento-boton-simple-llamado-ardid-sincrono
pm: nicolas
fecha_captura: 2026-09-29
fuente: "Confirmación directa del PM (Nicolás Colón) durante el seguimiento de titularidad_tarjeta (PRD-25), 2026-09-29; ya lo había adelantado en general el 2026-09-15"
producto: Ardid / Adquirencia (Botón Simple)
tema: El llamado de Botón Simple a Ardid es síncrono en las versiones 1.0 y 2.0
tipo: conocimiento
destino_propuesto: 3_recursos/detalle_productos/ardid/integracion_con_productos_bind.md
tipo_destino: actualizar
contradice: "no"
confianza: alta
estado: ingestado
merge_commit: 3492d04
---

En el pago con tarjeta de Botón Simple, el llamado a Ardid es **síncrono** tanto en la versión 1.0 como en la 2.0. El servicio de pagos llama a Ardid, espera su respuesta dentro del mismo procesamiento del pago y recién ahí decide si sigue hacia el procesador o registra la transacción como RECHAZADA con motivo "Rechazada por Ardid". Lo confirmó el PM el 2026-09-29 para las dos versiones; el 2026-09-15 ya lo había confirmado en general.

Por qué importa: cualquier control que se quiera sumar entre Ardid y el procesador puede apoyarse en datos que existen solo en ese momento del pago, sin tener que guardarlos. El proyecto de validación de titularidad de tarjeta (PRD-25) usa esto para retener en memoria el BIN, los últimos 4 y el vencimiento hasta consultar a MODO. Si en algún momento el llamado a Ardid pasara a ser asíncrono, ese diseño habría que revisarlo.

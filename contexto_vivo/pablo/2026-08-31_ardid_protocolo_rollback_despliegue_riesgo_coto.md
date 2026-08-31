---
id: 2026-08-31_ardid_protocolo_rollback_despliegue_riesgo_coto
pm: pablo
fecha_captura: 2026-08-31
fuente: "/sync_meetings — reunión \"Análisis de Riesgo - Fix de cambios de estados de las tarjetas\" (docId 1QLWJd6WyUAVTdul2c8tkZbue7eL84ddDZlZs-pJDEOo), 2026-08-28"
producto: ardid
tema: Protocolo estándar de rollback en despliegues de Ardid (imagen Docker + restore de base de datos) y riesgo de rechazos al activar reglas antifraude no aplicadas
tipo: conocimiento
destino_propuesto: 3_recursos/detalle_productos/ardid/
tipo_destino: crear
contradice: "no"
confianza: alta
estado: en_cola
merge_commit:
---

## Protocolo de rollback estándar de un despliegue de Ardid

Ticket AD-1374 (fix "actualización estado de pagos, corrección BIN" sobre la versión 1182 de Ardid, afecta los microservicios `transaction API` y `Transaction Service`) — el equipo (Matías Alzogaray, Osmel Mata/Fintexa, Mateo Capitanich/Fintexa) confirmó el patrón de rollback que usa Ardid ante una falla post-despliegue: **no alcanza con restaurar la imagen Docker anterior** (`docker-compose up -d --force-recreate --no-deps <servicio>` a partir del backup `.tar`) — si el despliegue ya modificó la base de datos (en este caso, un script de corrección sobre Mongo que regulariza registros trabados en estado `pending`), el rollback también requiere **restaurar el backup de base de datos (SQL Server + Mongo) tomado inmediatamente antes del despliegue** (ventana de ~30 min previa reservada para ese backup). Es la primera vez que este protocolo de dos pasos (imagen + DB) queda documentado explícitamente para Ardid — antes solo se hablaba de restaurar la imagen.

## Riesgo de rechazos al activar reglas antifraude que no se estaban aplicando — caso Coto

El fix de AD-1374 activa reglas antifraude que, por un bug previo, no se estaban aplicando (afecta especialmente a Coto, que consume las APIs de Ardid sin bypass — a diferencia de botón simple/wallet, que sí pueden operar en modo bypass durante la ventana de mantenimiento). El equipo clasificó el riesgo como **amarillo** (cambio funcional, no solo técnico) porque activar las reglas correctamente puede generar un salto de rechazos de transacciones y reclamos de clientes que antes pasaban sin control. Mitigación acordada: habilitar las reglas de forma gradual en vez de todas de una vez, y monitorear post-implementación la relación entre respuestas 200 y rechazos contra el volumen histórico. Deploy: staging lunes 31/08 9hs, producción martes 01/09 en ventana 6:30-8:00 (media hora previa reservada para el backup de bases). Sin action item de Producto — el seguimiento queda en el equipo técnico (Hernan Clarich monitorea rechazos, Rocío Revelli hace la revisión post-implementación en Ardid).

> Fuente: reunión "Análisis de Riesgo - Fix de cambios de estados de las tarjetas" (2026-08-28, 17:01), minuta Gemini.

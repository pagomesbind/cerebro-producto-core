---
id: 2026-09-22_gap_actualizacion_dim_collectors_pipeline_quinta_vez
pm: pablo
fecha_captura: 2026-09-22
fuente: "/sync_metrics — ingesta semana 202638"
producto: transversal
tema: dim_collectors sin orden posicional de columnas definido en pipeline.py — quinta corrida consecutiva con el mismo reclamo
tipo: gap
destino_propuesto: 2_areas/gaps_y_preguntas.md
tipo_destino: actualizar
contradice: "no"
confianza: alta
estado: en_cola
merge_commit:
---

**Actualiza el gap `[2026-08-18] — dim_collectors sin orden posicional de columnas definido para exports sin encabezado` en `2_areas/gaps_y_preguntas.md`.**

**Actualización (2026-09-22, semana 202638):** quinta corrida consecutiva (2026-08-18, 08-26, 08-31, 09-14,
09-22) en la que `collectors.csv` llega sin fila de encabezado y hay que reaplicar el workaround local. El
mapeo posicional sigue siendo exactamente el mismo, sin cambios, desde la primera confirmación:
`Id;CollectAccountId;Name;Cuit;Psp;Cbu;Webhook;FechaAlta;(sin identificar);Codigo;BankId;(sin identificar)`.

**Nota de esta corrida — casi se introduce una regresión:** al procesar `collectors.csv` en esta sesión, se
le preguntó al usuario el mapeo sin revisar primero el historial de gaps/`contexto_ingestado/` — se le
propuso (y aprobó) un orden **distinto e incorrecto** (`Codigo` en la columna 12 en vez de la 10). El error
se detectó recién al comparar contra `dim_collectors.csv` ya ingerido en el store real, antes de escribir
nada — se corrigió sin llegar a aplicar el mapeo equivocado. Si esta sesión hubiera revisado
`gaps_y_preguntas.md` antes de preguntar, el error (y la pregunta redundante al usuario) se evitaban.

**Pregunta para el usuario (repetida, quinta vez):** ¿se puede priorizar aplicar este mapeo en
`pipeline.py` (rama compartida en `CEREBRO_CORE`, archivo
`.claude/skills/sync_metrics/scripts/pipeline.py`, diccionario `COLUMN_ORDER_HEADERLESS`)? El mapeo está
confirmado sin cambios desde hace cuatro corridas — solo falta el cambio de código, que ninguna sesión de
este install puede aplicar porque el archivo está protegido (espejo read-only de `CEREBRO_CORE`).

**Estado:** Pendiente — mapeo confirmado y reconfirmado sin cambios por quinta vez, sigue faltando aplicar
el cambio en `pipeline.py`.

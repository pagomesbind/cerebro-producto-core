---
id: 2026-08-26_gap_dim_collectors_mapeo_confirmado
pm: pablo
fecha_captura: 2026-08-26
fuente: "/sync_metrics — ingesta semanal, semana 202634"
producto: transversal
tema: dim_collectors sin orden posicional de columnas definido para exports sin encabezado
tipo: gap
destino_propuesto: 2_areas/gaps_y_preguntas.md
tipo_destino: actualizar
contradice: "no"
confianza: alta
estado: ingestado
---

Actualización al gap abierto **"[2026-08-18] — dim_collectors sin orden posicional de columnas definido
para exports sin encabezado"** en `2_areas/gaps_y_preguntas.md`.

**Mapeo confirmado por el usuario (2026-08-26).** Cruzando los valores del export
`SELECT * FROM [dbo].[Collectors]` de esta corrida contra el store ya ingerido (`Id;Name;Cuit;Codigo;
BankId`, verificado exacto en 3 filas) y con la confirmación del usuario sobre las dos columnas ambiguas
por contenido solo, el orden real de las 12 columnas del export es:

| Posición | Columna | Confianza |
|---|---|---|
| 1 | Id | Alta — verificado contra store |
| 2 | CollectAccountId | Alta — confirmado por el usuario |
| 3 | Name | Alta — verificado contra store |
| 4 | Cuit | Alta — verificado contra store |
| 5 | Psp | Alta — confirmado por el usuario |
| 6 | Cbu | Media — formato CBU de 22 dígitos, no cruzable contra store |
| 7 | Webhook (URL) | Media — obvio por formato, sin uso en el store |
| 8 | FechaAlta (creación) | Media — sin uso en el store |
| 9 | sin identificar (`NULL` en todas las filas de muestra) | Baja — sin uso en el store |
| 10 | Codigo | Alta — verificado contra store |
| 11 | BankId | Alta — verificado contra store |
| 12 | sin identificar (código compuesto tipo `7$$C17105$$B00009548213`) | Baja — sin uso en el store |

Esta corrida se destrabó como workaround local (agregando la fila de encabezado directo al CSV en `raw/`,
sin tocar `pipeline.py`) — ver el item `tipo: dato` del store de esta misma corrida. El workaround no
persiste semana a semana.

**Pregunta para el usuario (actualizada, ahora con mapeo confirmado en mano):** ¿corresponde agregar esta
entrada a `COLUMN_ORDER_HEADERLESS["dim_collectors"]` en `pipeline.py` (vía el repo `CEREBRO_CORE`, ya que
el script está espejado y esta sesión no puede tocarlo directo)? Con esto el pipeline resuelve el archivo
por forma/posición como ya hace con `dim_entidades`/`dim_organizaciones`, sin depender de que el export
traiga (o no) fila de encabezado cada semana.

**Estado:** Pendiente — mapeo ya confirmado, falta aplicar el cambio en `pipeline.py`.

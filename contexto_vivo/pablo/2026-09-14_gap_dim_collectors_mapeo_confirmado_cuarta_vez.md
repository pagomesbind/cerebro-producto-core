---
id: 2026-09-14_gap_dim_collectors_mapeo_confirmado_cuarta_vez
pm: pablo
fecha_captura: 2026-09-14
fuente: "/sync_metrics — ingesta semanal, semana 202637"
producto: transversal
tema: dim_collectors sin orden posicional de columnas definido para exports sin encabezado — cuarta vez que se reconfirma el mismo mapeo, sigue sin aplicarse el cambio de código
tipo: gap
destino_propuesto: 2_areas/gaps_y_preguntas.md
tipo_destino: actualizar
contradice: "no"
confianza: alta
estado: ingestado
merge_commit: 122ad74
---

Actualización al gap abierto **"[2026-08-18] — dim_collectors sin orden posicional de columnas definido
para exports sin encabezado"** en `2_areas/gaps_y_preguntas.md`, con mapeo confirmado el 2026-08-26,
reconfirmado el 2026-08-31 (ver `[[2026-08-26_gap_dim_collectors_mapeo_confirmado]]` y
`[[2026-08-31_gap_dim_collectors_mapeo_reconfirmado_tercera_vez]]`), y ahora repetido **por cuarta vez** en
esta corrida (2026-09-14, semana 202637).

**El mismo problema volvió a repetirse, sin ningún cambio en el mapeo.** `collectors.csv` llegó otra vez
sin fila de encabezado, 12 columnas. Se contrastó contra el store ya ingerido y coincide exactamente con
el mapeo ya documentado dos veces:

| Posición | Columna |
|---|---|
| 1 | Id |
| 2 | CollectAccountId |
| 3 | Name |
| 4 | Cuit |
| 5 | Psp |
| 6 | Cbu |
| 7 | Webhook (URL) |
| 8 | FechaAlta (creación) |
| 9 | sin identificar (`NULL` en todas las filas de muestra) |
| 10 | Codigo |
| 11 | BankId |
| 12 | sin identificar (código compuesto tipo `7$$C17105$$B00009548213`) |

Se aplicó otra vez como workaround local (fila de encabezado agregada directo al CSV en `raw/`, sin tocar
`pipeline.py`, que sigue espejado desde `CEREBRO_CORE` y bloqueado para edición en esta sesión) — esta vez
como una corrida separada de `ingest` con solo `collectors.csv` en `raw/`, ya que las otras 7 fuentes ya
se habían ingerido antes de detectar el problema.

**Por qué importa ahora más que antes:** es la **cuarta** semana (202633→202634→202635→202637, con un
salto en 202636 donde aparentemente no se reprocesó o no hizo falta) que se repite exactamente la misma
pregunta con exactamente la misma respuesta, ya confirmada dos veces explícitamente por el usuario
("guardate esto para no volver a preguntarme"). El mapeo no tiene ninguna ambigüedad pendiente — está
verificado contra el store en múltiples filas y en múltiples corridas. El único motivo de que se siga
repitiendo es que el cambio en `COLUMN_ORDER_HEADERLESS["dim_collectors"]` de `pipeline.py` (vía
`CEREBRO_CORE`) todavía no se aplicó.

**Pregunta para el usuario (repetida, cuarta vez):** ¿se puede priorizar aplicar este mapeo en
`pipeline.py` (rama compartida en `CEREBRO_CORE`) para que deje de repetirse cada semana? El mapeo está
confirmado sin cambios desde hace tres corridas — solo falta el cambio de código.

**Estado:** Pendiente — mapeo confirmado y reconfirmado sin cambios por cuarta vez, sigue faltando aplicar
el cambio en `pipeline.py`.

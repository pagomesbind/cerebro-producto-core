---
id: 2026-08-31_gap_dim_collectors_mapeo_reconfirmado_tercera_vez
pm: pablo
fecha_captura: 2026-08-31
fuente: "/sync_metrics — ingesta semanal, semana 202635"
producto: transversal
tema: dim_collectors sin orden posicional de columnas definido para exports sin encabezado — tercera vez que se reconfirma el mismo mapeo
tipo: gap
destino_propuesto: 2_areas/gaps_y_preguntas.md
tipo_destino: actualizar
contradice: "no"
confianza: alta
estado: ingestado
---

Actualización al gap abierto **"[2026-08-18] — dim_collectors sin orden posicional de columnas definido
para exports sin encabezado"** en `2_areas/gaps_y_preguntas.md`, con mapeo ya confirmado por el usuario el
2026-08-26 (ver `[[2026-08-26_gap_dim_collectors_mapeo_confirmado]]`) y ahora **reconfirmado por segunda
vez** en esta corrida (2026-08-31, semana 202635).

**El mismo problema volvió a repetirse.** `collectors.csv` llegó otra vez sin fila de encabezado. Se
recruzaron los valores del export contra el store ya ingerido (`Id;Name;Cuit;Codigo;BankId`, verificado
exacto en 5 filas: Id 1, 2, 4, 5) y contra el mapeo ya documentado el 2026-08-26 — coincide exactamente,
sin cambios:

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

El usuario confirmó explícitamente: *"Si es correcto. Por favor guardate esto para no volver a
preguntarme."* Se aplicó otra vez como workaround local (fila de encabezado agregada directo al CSV en
`raw/`, sin tocar `pipeline.py`, que sigue espejado desde `CEREBRO_CORE` y bloqueado para edición en esta
sesión).

**Por qué importa ahora más que antes:** es la **tercera** semana consecutiva (202633→202634→202635, según
el gap original del 2026-08-18) que se repite exactamente la misma pregunta con exactamente la misma
respuesta. El mapeo no tiene ninguna ambigüedad pendiente — está verificado contra el store en múltiples
filas y confirmado dos veces por el usuario. El único motivo de que se siga repitiendo es que el cambio en
`COLUMN_ORDER_HEADERLESS["dim_collectors"]` de `pipeline.py` (vía `CEREBRO_CORE`) todavía no se aplicó.

**Pregunta para el usuario (repetida, ahora con más urgencia):** ¿se puede priorizar aplicar este mapeo en
`pipeline.py` en la próxima sincronización con `CEREBRO_CORE`? Con el mapeo ya confirmado dos veces sin
cambios, no hace falta volver a preguntarlo — solo falta el cambio de código.

**Estado:** Pendiente — mapeo reconfirmado por segunda vez, sigue faltando aplicar el cambio en
`pipeline.py`.

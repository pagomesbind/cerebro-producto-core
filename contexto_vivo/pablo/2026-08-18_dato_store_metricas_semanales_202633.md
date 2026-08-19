---
id: 2026-08-18_dato_store_metricas_semanales_202633
pm: pablo
fecha_captura: 2026-08-18
fuente: "/sync_metrics — ingesta semanal, semana 202633 (10 al 17 de agosto de 2026)"
producto: transversal
tema: Store acumulado de métricas semanales (NSM) — semana 202633
tipo: dato
destino_propuesto: 3_recursos/datos/datos_metricas_semanales/
tipo_destino: reemplazar
contradice: "no"
confianza: alta
estado: ingestado
merge_commit:
---

Payload ya generado por `pipeline.py ingest` (corrida 2026-08-18) en
`wiki/1_proyectos/contexto_vivo/_staging_sync_metrics/datos_metricas_semanales/` — mismo mecanismo de
siempre (`seed_staging_from_mirror()` sembró la carpeta desde el espejo de `3_recursos/datos/
datos_metricas_semanales/` y el `ingest` mergeó ahí el lote nuevo). `/context_merge` copia esa carpeta
completa, byte a byte, sobre `3_recursos/datos/datos_metricas_semanales/` — no hay contenido que redactar
acá, el store ya está actualizado en la carpeta de staging.

**Archivos tocados por esta corrida** (el resto de la carpeta queda igual, se copia entera de todos modos
por ser la mecánica estándar de este tipo de item):

- `fact_operaciones.csv` — +145 filas
- `fact_cuentas.csv` — +19 filas
- `fact_transacciones.csv` — +290 filas
- `fact_comercios.csv` — +6 filas
- `fact_transferencias_agente_cobro.csv` — +177 filas
- `dim_entidades.csv` — 210 filas, pisadas (refresh completo, sin cambios de contenido esta corrida)
- `dim_organizaciones.csv` — 66 filas, pisadas (refresh completo, sin cambios de contenido esta corrida)
- `semanas.csv` — semana 202633 nueva, marcada completa. 50 semanas cerradas en total (202536 → 202633).

**Pendiente — `dim_collectors.csv` NO se ingirió esta corrida.** El usuario subió `collectors.csv` a `raw/`
(export `SELECT * FROM [dbo].[Collectors]`), pero llegó sin fila de encabezado y el pipeline nunca tuvo
definido el orden posicional de columnas para esa tabla (a diferencia de operaciones/transacciones/cuentas/
comercios/transferencias, resueltas por forma+contenido desde el 2026-08-11). Como `dim_collectors` no
bloquea el `ingest` de los demás recursos, se lo dejó afuera del lote y se movió el archivo a
`scratchpad/collectors.csv` de esta sesión, pendiente de mapeo confirmado por el usuario — ver el item de
gap asociado (`2026-08-18_gap_dim_collectors_sin_orden_columnas`) y `2_areas/gaps_y_preguntas.md` tras el
merge. Los nombres de collectors nuevos que hayan aparecido esta semana no se reflejan en `dim_collectors`
del store todavía; el desglose por collector del reporte de esta semana usa los nombres ya conocidos del
store anterior.

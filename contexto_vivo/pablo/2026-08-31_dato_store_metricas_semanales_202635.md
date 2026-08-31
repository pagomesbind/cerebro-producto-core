---
id: 2026-08-31_dato_store_metricas_semanales_202635
pm: pablo
fecha_captura: 2026-08-31
fuente: "/sync_metrics — ingesta semanal, semana 202635 (24 al 31 de agosto de 2026)"
producto: transversal
tema: Store acumulado de métricas semanales (NSM) — semana 202635
tipo: dato
destino_propuesto: 3_recursos/datos/datos_metricas_semanales/
tipo_destino: reemplazar
contradice: "no"
confianza: alta
estado: en_cola
merge_commit:
---

Payload ya generado por `pipeline.py ingest` (corrida 2026-08-31) en
`wiki/1_proyectos/contexto_vivo/_staging_sync_metrics/datos_metricas_semanales/` — mismo mecanismo de
siempre (`seed_staging_from_mirror()` sembró la carpeta desde el espejo de
`3_recursos/datos/datos_metricas_semanales/` y el `ingest` mergeó ahí el lote nuevo). `/context_merge`
copia esa carpeta completa, byte a byte, sobre `3_recursos/datos/datos_metricas_semanales/` — no hay
contenido que redactar acá, el store ya está actualizado en la carpeta de staging.

**Archivos tocados por esta corrida** (el resto de la carpeta queda igual, se copia entera de todos modos
por ser la mecánica estándar de este tipo de item):

- `fact_operaciones.csv` — +157 filas
- `fact_cuentas.csv` — +21 filas
- `fact_transacciones.csv` — +293 filas
- `fact_comercios.csv` — +8 filas
- `fact_transferencias_agente_cobro.csv` — +161 filas
- `dim_entidades.csv` — 211 filas, pisadas (refresh completo, sin cambios de contenido esta corrida)
- `dim_organizaciones.csv` — 66 filas, pisadas (refresh completo, sin cambios de contenido esta corrida)
- `dim_collectors.csv` — 159 filas, pisadas (refresh completo, +1 fila nueva)
- `semanas.csv` — semana 202635 nueva, marcada completa. 52 semanas cerradas en total (202536 → 202635).

**`dim_collectors.csv` volvió a llegar sin fila de encabezado** (`SELECT * FROM [dbo].[Collectors]`, 12
columnas) — mismo patrón que las corridas del 2026-08-18 y 2026-08-26. Se reconfirmó el mapeo posicional
ya documentado (ver `[[2026-08-31_gap_dim_collectors_mapeo_reconfirmado_tercera_vez]]`) y se aplicó como
workaround local en `raw/collectors.csv` (fila de encabezado agregada al CSV de origen, sin tocar
`pipeline.py`).

---
id: 2026-08-26_dato_store_metricas_semanales_202634
pm: pablo
fecha_captura: 2026-08-26
fuente: "/sync_metrics — ingesta semanal, semana 202634 (17 al 24 de agosto de 2026)"
producto: transversal
tema: Store acumulado de métricas semanales (NSM) — semana 202634
tipo: dato
destino_propuesto: 3_recursos/datos/datos_metricas_semanales/
tipo_destino: reemplazar
contradice: "no"
confianza: alta
estado: ingestado
merge_commit: c4148e7
---

Payload ya generado por `pipeline.py ingest` (corrida 2026-08-26) en
`wiki/1_proyectos/contexto_vivo/_staging_sync_metrics/datos_metricas_semanales/` — mismo mecanismo de
siempre (`seed_staging_from_mirror()` sembró la carpeta desde el espejo de `3_recursos/datos/
datos_metricas_semanales/` y el `ingest` mergeó ahí el lote nuevo). `/context_merge` copia esa carpeta
completa, byte a byte, sobre `3_recursos/datos/datos_metricas_semanales/` — no hay contenido que redactar
acá, el store ya está actualizado en la carpeta de staging.

**Archivos tocados por esta corrida** (el resto de la carpeta queda igual, se copia entera de todos modos
por ser la mecánica estándar de este tipo de item):

- `fact_operaciones.csv` — +152 filas
- `fact_cuentas.csv` — +22 filas
- `fact_transacciones.csv` — +278 filas
- `fact_comercios.csv` — +7 filas
- `fact_transferencias_agente_cobro.csv` — +161 filas
- `dim_entidades.csv` — 211 filas, pisadas (refresh completo, +1 fila nueva)
- `dim_organizaciones.csv` — 66 filas, pisadas (refresh completo, sin cambios de contenido esta corrida)
- `dim_collectors.csv` — 158 filas, pisadas (refresh completo, +1 fila nueva) — **primera corrida en la que
  se ingiere esta dimensión** desde que se abrió el gap el 2026-08-18 (ver item de gap asociado).
- `semanas.csv` — semana 202634 nueva, marcada completa. 51 semanas cerradas en total (202536 → 202634).

**Resuelto — `dim_collectors.csv` se ingirió por primera vez esta corrida.** El export llegó de nuevo sin
fila de encabezado (`SELECT * FROM [dbo].[Collectors]`, 12 columnas) y el pipeline sigue sin tener un orden
posicional definido para esta tabla en `COLUMN_ORDER_HEADERLESS` de `pipeline.py` (no se tocó el script —
está espejado desde `CEREBRO_CORE`, fuera del alcance de esta sesión). Se resolvió como workaround local:
se identificaron y el usuario confirmó las 5 columnas necesarias para el merge (`Id`, `Name`, `Cuit`,
`Codigo`, `BankId`, más `CollectAccountId` para la firma) cruzando los valores contra el store ya ingerido,
y se agregó una fila de encabezado directamente al CSV en `raw/` con esos nombres — el pipeline lo
reconoció por firma de header sin necesidad de tocar el código. **Este workaround no persiste**: la próxima
corrida va a volver a llegar sin encabezado y va a necesitar el mismo tratamiento (o la fila de encabezado
agregada en origen por quien exporta) hasta que `COLUMN_ORDER_HEADERLESS` se actualice en `CEREBRO_CORE` —
ver el item de gap actualizado con el mapeo confirmado para que ese cambio se pueda aplicar sin volver a
adivinar nada.

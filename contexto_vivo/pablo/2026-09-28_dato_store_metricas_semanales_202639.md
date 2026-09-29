---
id: 2026-09-28_dato_store_metricas_semanales_202639
pm: pablo
fecha_captura: 2026-09-28
fuente: "/sync_metrics — ingesta semanal de exports de SQL (8 queries del SKILL.md), semana 202639"
producto: transversal
tema: Datos acumulados de NSM semanales (202639 — 2026-09-21 a 2026-09-28)
tipo: dato
destino_propuesto: 3_recursos/datos/datos_metricas_semanales
tipo_destino: reemplazar
contradice: "no"
confianza: alta
estado: en_cola
merge_commit:
---

**Fuente:** copia de trabajo en `wiki/1_proyectos/contexto_vivo/_staging_sync_metrics/datos_metricas_semanales/`
(ingerida con `pipeline.py ingest` desde `raw/`, una sola pasada, sin `[WARN]`). `/context_merge` copia esa
carpeta byte a byte sobre `3_recursos/datos/datos_metricas_semanales/`, junto con
`_staging_sync_metrics/log_metricas_semanales.md` → `3_recursos/datos/log_metricas_semanales.md`.

**Contenido:**
- `fact_operaciones.csv` — 7.333 filas (+139 nuevas en 202639).
- `fact_cuentas.csv` — 991 filas (+18 nuevas).
- `fact_transacciones.csv` — 13.019 filas (+284 nuevas).
- `fact_comercios.csv` — 398 filas (+9 nuevas).
- `fact_transferencias_agente_cobro.csv` — 5.406 filas (+143 nuevas).
- `dim_organizaciones.csv` — 67 filas (sin altas, 67 pisadas).
- `dim_entidades.csv` — 215 filas (sin altas, 215 pisadas).
- `dim_collectors.csv` — 164 filas (sin altas, 163 pisadas).
- `semanas.csv` — 56 semanas completas, 0 parciales; 202639 es la última cerrada.

**Nota sobre `dim_collectors`:** `collectors.csv` volvió a llegar sin fila de encabezado (12 columnas), pero
por primera vez **no hizo falta workaround**: el pipeline lo detectó solo por forma
(`COLUMN_ORDER_HEADERLESS['dim_collectors']`, aplicado el 2026-09-25) con el mapeo ya confirmado. Todos los
demás archivos también llegaron sin encabezado y se detectaron por forma/contenido (`[ASUMIDO]`, verificado
contra los conteos esperados).

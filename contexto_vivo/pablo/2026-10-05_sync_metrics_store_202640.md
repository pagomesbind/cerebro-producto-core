---
id: 2026-10-05_sync_metrics_store_202640
pm: pablo
fecha_captura: 2026-10-05
fuente: "/sync_metrics — ingesta semanal de exportes de SQL (queries en SKILL.md)"
producto: transversal
tema: Datos acumulados de NSM semanales (202640 — 2026-09-28 a 2026-10-05)
tipo: dato
destino_propuesto: 3_recursos/datos/datos_metricas_semanales
tipo_destino: reemplazar
contradice: "no"
confianza: alta
estado: en_cola
merge_commit:
---

**Fuente:** Copia de trabajo en `wiki/1_proyectos/contexto_vivo/_staging_sync_metrics/datos_metricas_semanales/`
(ingerida mediante `pipeline.py ingest` desde `raw/`) y `wiki/1_proyectos/contexto_vivo/_staging_sync_metrics/log_metricas_semanales.md`.

**Contenido:**
- `fact_operaciones.csv` — 7.478 filas históricas, +145 nuevas en 202640.
- `fact_cuentas.csv` — 1.011 filas históricas, +20 nuevas en 202640.
- `fact_transacciones.csv` — 13.326 filas históricas, +307 nuevas en 202640.
- `fact_comercios.csv` — 404 filas históricas, +6 nuevas en 202640.
- `fact_transferencias_agente_cobro.csv` — 5.555 filas históricas, +149 nuevas en 202640.
- `dim_organizaciones.csv` (67), `dim_entidades.csv` (215), `dim_collectors.csv` (164) — dimensiones
  refrescadas, sin altas nuevas esta semana (0 filas nuevas en las tres).
- `semanas.csv` — 57 semanas en el store, las 57 completas, ninguna parcial; 202640 es la última cerrada.
- `log_metricas_semanales.md` — log de ingesta actualizado con la corrida del 2026-10-05.

**Semana 202640 (2026-09-28 → 2026-10-05):**
- NSM#1: $299.554 M (+79,8% WoW, +13,8% vs. baseline 13s, −28,6% vs. máximo histórico)
- NSM#2: $11.701 M (+47,3% WoW, +19,7% vs. baseline 13s, −20,3% vs. máximo histórico)
- Tendencia 4 semanas móviles: NSM#1 −7,0%, NSM#2 +1,6% (no es cierre mensual calendario, ver nota de
  metodología en el reporte)

**`[WARN]` de la corrida:** `Estado = REALIZADA` reapareció en transacciones (1 fila) — caso ya conocido y
marginal desde el backfill original, no mueve ninguna NSM, no requiere nueva pregunta al usuario.

**Decisiones confirmadas esta semana:** ninguna sobre la definición de NSM o métricas.

**Próxima ingesta:** se pedirá el mismo lote de 8 queries la semana que viene (viernes/sábado de la semana
202641).

---
id: 2026-09-07_sync_metrics_store_202636
pm: pablo
fecha_captura: 2026-09-07
fuente: "/sync_metrics — ingesta semanal de exportes de SQL (queries en SKILL.md)"
producto: transversal
tema: Datos acumulados de NSM semanales (202636 — 2026-08-31 a 2026-09-07)
tipo: dato
destino_propuesto: 3_recursos/datos/datos_metricas_semanales
tipo_destino: reemplazar
contradice: no
confianza: alta
estado: ingestado
merge_commit: d783db8
---

**Fuente:** Copia de trabajo en `wiki/1_proyectos/contexto_vivo/_staging_sync_metrics/datos_metricas_semanales/` (ingerida mediante `pipeline.py ingest` desde raw/).

**Contenido:** 
- `fact_operaciones.csv` — operaciones aprobadas de Wallet (tipos 1, 2, 3, 6, 8, 14; estado Aprobada), agregadas por semana, organización, tipo de operación, estado. 6.905 filas históricas, +149 nuevas en 202636.
- `fact_cuentas.csv` — altas de cuentas de Wallet por semana y organización (leading indicator de NSM#1). 936 filas históricas, +21 nuevas en 202636.
- `fact_transacciones.csv` — transacciones de Adquirencia (tipos 6, 7; formas 10, 60, 80, 90; estado ACREDITADO), agregadas por semana, entidad, tipo, forma, estado. 12.153 filas históricas, +310 nuevas en 202636.
- `fact_comercios.csv` — altas de comercios de Adquirencia por semana y entidad (leading indicator de NSM#2). 375 filas históricas, +6 nuevas en 202636.
- `fact_transferencias_agente_cobro.csv` — transferencias del Agente de Cobros y Pagos (COMPLETED), agregadas por semana, tipo, collector, status. Palanca directa que suma a NSM#1. 4.966 filas históricas, +167 nuevas en 202636.
- `dim_organizaciones.csv`, `dim_entidades.csv`, `dim_collectors.csv` — dimensiones de referencia (refresh semanal; contienen clientes/cuentas/collectors nuevos si aplica).
- `semanas.csv` — índice de semanas en el store (53 completas, ninguna parcial; 202636 es la última cerrada).

**Semana 202636 (2026-08-31 → 2026-09-07):**
- NSM#1: $387.389 M (+86.6% WoW, +55.8% vs. baseline 13s, -7.7% vs. máximo histórico)
- NSM#2: $12.197 M (+50.7% WoW, +48.1% vs. baseline 13s, -17.0% vs. máximo histórico)
- Tendencia 4 semanas móviles: NSM#1 -1.6%, NSM#2 -3.2% (no es cierre mensual calendario, ver nota de metodología en el reporte)

**Decisiones confirmadas esta semana:** ninguna sobre la definición de NSM o métricas.

**Próxima ingesta:** se pedirá el mismo lote de 8 queries la siguiente semana (viernes/sábado de la semana que termina).

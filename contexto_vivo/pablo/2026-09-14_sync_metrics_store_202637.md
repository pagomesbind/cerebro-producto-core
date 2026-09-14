---
id: 2026-09-14_sync_metrics_store_202637
pm: pablo
fecha_captura: 2026-09-14
fuente: "/sync_metrics — ingesta semanal de exportes de SQL (queries en SKILL.md)"
producto: transversal
tema: Datos acumulados de NSM semanales (202637 — 2026-09-07 a 2026-09-14)
tipo: dato
destino_propuesto: 3_recursos/datos/datos_metricas_semanales
tipo_destino: reemplazar
contradice: "no"
confianza: alta
estado: en_cola
---

**Fuente:** Copia de trabajo en `wiki/1_proyectos/contexto_vivo/_staging_sync_metrics/datos_metricas_semanales/` (ingerida mediante `pipeline.py ingest` desde raw/, en dos pasadas — ver nota de `dim_collectors` abajo).

**Contenido:**
- `fact_operaciones.csv` — 7.052 filas históricas, +147 nuevas en 202637.
- `fact_cuentas.csv` — 954 filas históricas, +18 nuevas en 202637.
- `fact_transacciones.csv` — 12.445 filas históricas, +292 nuevas en 202637.
- `fact_comercios.csv` — 383 filas históricas, +8 nuevas en 202637.
- `fact_transferencias_agente_cobro.csv` — 5.118 filas históricas, +152 nuevas en 202637.
- `dim_organizaciones.csv` — 67 filas (+1 nueva, 66 pisadas).
- `dim_entidades.csv` — 215 filas (+4 nuevas, 211 pisadas).
- `dim_collectors.csv` — 164 filas (+3 nuevas, 160 pisadas).
- `semanas.csv` — 54 semanas completas, 0 parciales; 202637 es la última cerrada.

**Nota sobre `dim_collectors` — mismo problema recurrente, mismo mapeo ya confirmado, ahora aplicado también acá:**
`collectors.csv` volvió a llegar sin fila de encabezado (12 columnas). Es la **cuarta vez** que se repite
(gaps del 2026-08-18, 2026-08-26 y 2026-08-31, ver `wiki/4_archivos/contexto_ingestado/`) con exactamente
el mismo mapeo ya confirmado dos veces por el usuario ("guardate esto para no volver a preguntarme"):
Id/CollectAccountId/Name/Cuit/Psp/Cbu/Webhook/FechaAlta/(sin identificar)/Codigo/BankId/(sin identificar).
Se aplicó otra vez como workaround local (fila de encabezado agregada al CSV en `raw/`, sin tocar
`pipeline.py`, que sigue espejado desde `CEREBRO_CORE` y bloqueado para edición en esta sesión) — ver el
item `tipo: gap` de esta misma corrida pidiendo que se priorice el cambio de código.

**Semana 202637 (2026-09-07 → 2026-09-14):**
- NSM#1 (oficial, Wallet + Agente de Cobros): $322.438 M (-16.8% WoW, +26.3% vs. baseline 13s, -23.2% vs. máximo histórico)
- NSM#2: $12.525 M (+2.7% WoW, +44.1% vs. baseline 13s, -14.7% vs. máximo histórico)
- Tendencia 4 semanas móviles: NSM#1 +3.1%, NSM#2 -4.2% (no es cierre mensual calendario, ver nota de metodología en el reporte)

**Decisiones confirmadas esta semana:** ninguna sobre la definición de NSM o métricas.

**Próxima ingesta:** se pedirá el mismo lote de 8 queries la semana que viene (202638).

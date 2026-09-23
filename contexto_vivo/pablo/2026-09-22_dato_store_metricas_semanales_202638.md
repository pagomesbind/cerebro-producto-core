---
id: 2026-09-22_dato_store_metricas_semanales_202638
pm: pablo
fecha_captura: 2026-09-22
fuente: "/sync_metrics — ingesta semanal de exportes de SQL (queries en SKILL.md)"
producto: transversal
tema: Datos acumulados de NSM semanales (202638 — 2026-09-14 a 2026-09-21)
tipo: dato
destino_propuesto: 3_recursos/datos/datos_metricas_semanales
tipo_destino: reemplazar
contradice: "no"
confianza: alta
estado: ingestado
merge_commit: 72d6140
---

**Fuente:** Copia de trabajo en `wiki/1_proyectos/contexto_vivo/_staging_sync_metrics/datos_metricas_semanales/` (ingerida mediante `pipeline.py ingest` desde raw/, en dos pasadas — ver nota de `dim_collectors` abajo).

**Contenido:**
- `fact_operaciones.csv` — 7.194 filas históricas (+142 nuevas en 202638).
- `fact_cuentas.csv` — 973 filas históricas (+19 nuevas en 202638).
- `fact_transacciones.csv` — 12.735 filas históricas (+290 nuevas en 202638).
- `fact_comercios.csv` — 389 filas históricas (+6 nuevas en 202638).
- `fact_transferencias_agente_cobro.csv` — 5.263 filas históricas (+145 nuevas en 202638).
- `dim_organizaciones.csv` — 67 filas (sin altas nuevas, 67 pisadas).
- `dim_entidades.csv` — 215 filas (sin altas nuevas, 215 pisadas).
- `dim_collectors.csv` — 164 filas (sin altas nuevas, 163 pisadas).
- `semanas.csv` — 55 semanas completas, 0 parciales; 202638 es la última cerrada.

**Nota sobre `dim_collectors` — mismo problema recurrente, mismo mapeo ya confirmado, ahora aplicado también acá (quinta vez):**
`collectors.csv` volvió a llegar sin fila de encabezado (12 columnas). Es la **quinta vez** que se repite
(gaps del 2026-08-18, 2026-08-26, 2026-08-31 y 2026-09-14, ver `wiki/4_archivos/contexto_ingestado/`) con
exactamente el mismo mapeo ya confirmado cuatro veces por el usuario:
`Id;CollectAccountId;Name;Cuit;Psp;Cbu;Webhook;FechaAlta;(sin identificar);Codigo;BankId;(sin identificar)`.
**Nota de esta corrida:** al preguntarle al usuario en esta sesión (sin haber revisado antes el historial de
gaps), se le propuso por error un mapeo distinto (`Codigo` en la columna 12 en vez de la 10) — el usuario lo
aprobó sin poder saber que contradecía el ya confirmado, y recién se detectó el error al cruzar contra
`dim_collectors.csv` ya ingerido en el store. Se corrigió antes de ingerir, usando el mapeo históricamente
correcto (verificado contra el store real). Se aplicó otra vez el mismo workaround local (fila de
encabezado agregada al CSV en `raw/`, sin tocar `pipeline.py`, que sigue espejado desde `CEREBRO_CORE` y
bloqueado para edición en esta sesión) — ver el gap actualizado de esta misma corrida pidiendo, por quinta
vez, que se priorice el cambio de código.

**Semana 202638 (2026-09-14 → 2026-09-21):**
- NSM#1 (oficial, Wallet + Agente de Cobros): $197.263 M (-38.8% WoW, -24.3% vs. baseline 13s, -53.0% vs. máximo histórico)
- NSM#2: $8.198 M (-34.5% WoW, -11.1% vs. baseline 13s, -44.2% vs. máximo histórico)
- Tendencia 4 semanas móviles: NSM#1 +4.2%, NSM#2 -3.1% (no es cierre mensual calendario, ver nota de metodología en el reporte)

**Decisiones confirmadas esta semana:** ninguna sobre la definición de NSM o métricas.

**Próxima ingesta:** se pedirá el mismo lote de 8 queries la semana que viene (202639).

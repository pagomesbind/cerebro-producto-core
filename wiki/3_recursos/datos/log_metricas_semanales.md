# Log de control — /sync_metrics

> Ledger de máquina. Una fila por corrida de la skill: qué archivos entraron,
> qué semanas cubrieron y cuántas filas quedaron en el store acumulado
> (`datos_metricas_semanales/`). Se consulta para auditar qué hizo la skill,
> no para razonar sobre el negocio — eso vive en
> [`metricas_semanales.md`](metricas_semanales.md).

| Fecha corrida | Semanas del lote | Semanas cerradas | Recurso | Archivos | Filas lote | Filas store | Nuevas | Pisadas |
|---|---|---|---|---|---|---|---|---|
| 2026-07-21 | 202536–202630 | 46 | comercios | 1 | 319 | 319 | 319 | 0 |
| 2026-07-21 | 202536–202630 | 46 | cuentas | 1 | 798 | 798 | 798 | 0 |
| 2026-07-21 | 202536–202630 | 46 | dim_entidades | 1 | 202 | 202 | 202 | 0 |
| 2026-07-21 | 202536–202630 | 46 | dim_estados_operacion | 1 | 8 | 8 | 8 | 0 |
| 2026-07-21 | 202536–202630 | 46 | dim_organizaciones | 1 | 63 | 63 | 63 | 0 |
| 2026-07-21 | 202536–202630 | 46 | dim_tipos_operacion | 1 | 16 | 16 | 16 | 0 |
| 2026-07-21 | 202536–202630 | 46 | operaciones | 3 | 6097 | 5944 | 5944 | 0 |
| 2026-07-21 | 202536–202630 | 46 | transacciones | 3 | 10268 | 10188 | 10188 | 0 |
| 2026-07-23 | 202601–202630 | 0 | dim_collectors | 1 | 151 | 151 | 151 | 0 |
| 2026-07-23 | 202601–202630 | 0 | transferencias_agente_cobro | 2 | 3882 | 3882 | 3882 | 0 |
| 2026-07-23 | 202601–202630 | 0 | dim_collectors | 1 | 151 | 151 | 0 | 151 |
| 2026-07-23 | 202601–202630 | 0 | transferencias_agente_cobro | 2 | 3882 | 3882 | 0 | 3882 |
| 2026-07-27 | 202630–202630 | 1 | comercios | 1 | 8 | 327 | 8 | 0 |
| 2026-07-27 | 202630–202630 | 1 | cuentas | 1 | 22 | 807 | 9 | 13 |
| 2026-07-27 | 202630–202630 | 1 | operaciones | 1 | 144 | 5996 | 52 | 92 |
| 2026-07-27 | 202630–202630 | 1 | transacciones | 1 | 278 | 10411 | 223 | 55 |
| 2026-07-27 | 202630–202630 | 1 | transferencias_agente_cobro | 1 | 155 | 3989 | 107 | 48 |
| 2026-07-27 | — | 0 | dim_collectors | 1 | 153 | 153 | 2 | 151 |
| 2026-07-27 | — | 0 | dim_entidades | 1 | 203 | 203 | 1 | 202 |
| 2026-08-04 | 202631–202631 | 1 | comercios | 1 | 8 | 335 | 8 | 0 |
| 2026-08-04 | 202631–202631 | 1 | cuentas | 1 | 23 | 830 | 23 | 0 |
| 2026-08-04 | 202631–202631 | 1 | dim_collectors | 1 | 155 | 155 | 2 | 153 |
| 2026-08-04 | 202631–202631 | 1 | dim_entidades | 1 | 207 | 207 | 4 | 203 |
| 2026-08-04 | 202631–202631 | 1 | dim_organizaciones | 1 | 65 | 65 | 2 | 63 |
| 2026-08-04 | 202631–202631 | 1 | operaciones | 1 | 156 | 6152 | 156 | 0 |
| 2026-08-04 | 202631–202631 | 1 | transacciones | 1 | 278 | 10689 | 278 | 0 |
| 2026-08-04 | 202631–202631 | 1 | transferencias_agente_cobro | 1 | 143 | 4132 | 143 | 0 |
| 2026-08-11 | 202632–202632 | 1 | comercios | 1 | 13 | 348 | 13 | 0 |
| 2026-08-11 | 202632–202632 | 1 | cuentas | 1 | 23 | 853 | 23 | 0 |
| 2026-08-11 | 202632–202632 | 1 | dim_collectors | 1 | 157 | 157 | 2 | 155 |
| 2026-08-11 | 202632–202632 | 1 | dim_entidades | 1 | 210 | 210 | 3 | 207 |
| 2026-08-11 | 202632–202632 | 1 | dim_organizaciones | 1 | 66 | 66 | 1 | 65 |
| 2026-08-11 | 202632–202632 | 1 | operaciones | 1 | 150 | 6302 | 150 | 0 |
| 2026-08-11 | 202632–202632 | 1 | transacciones | 1 | 293 | 10982 | 293 | 0 |
| 2026-08-11 | 202632–202632 | 1 | transferencias_agente_cobro | 1 | 168 | 4300 | 168 | 0 |

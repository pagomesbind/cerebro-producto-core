# Datos de Métricas Semanales — Store CSV

> Store de datos crudo (CSV) que alimenta `/sync_metrics` para calcular las 2 North Star Metrics semana a semana. No es contenido de lectura directa para razonar sobre el negocio — ver [2_areas/datasets/metricas_semanales.md](../metricas_semanales.md) para los resultados ya calculados y narrados.

## Archivos

| Archivo | Contenido |
|---|---|
| `semanas.csv` | Calendario de semanas ya procesadas (control de idempotencia de `/sync_metrics`). |
| `dim_entidades.csv` | Dimensión: entidades de Adquirencia/Agente de Cobros. |
| `dim_organizaciones.csv` | Dimensión: organizaciones de Wallet. |
| `dim_collectors.csv` | Dimensión: collectors del Agente de Cobros y Pagos. |
| `dim_estados_operacion.csv` | Dimensión: estados posibles de una operación. |
| `dim_tipos_operacion.csv` | Dimensión: tipos de operación. |
| `fact_comercios.csv` | Hechos: comercios de Adquirencia por semana. |
| `fact_cuentas.csv` | Hechos: cuentas de Wallet por semana. |
| `fact_operaciones.csv` | Hechos: operaciones de Wallet por semana. |
| `fact_transacciones.csv` | Hechos: transacciones de Adquirencia por semana. |
| `fact_transferencias_agente_cobro.csv` | Hechos: transferencias del Agente de Cobros y Pagos por semana. |

## Ver también
- [2_areas/datasets/metricas_semanales.md](../metricas_semanales.md) — métricas ya calculadas y con hallazgos narrados.
- [2_areas/control/log_metricas_semanales.md](../log_metricas_semanales.md) — control de qué semanas ya se procesaron.

---
*Última actualización: 2026-08-12 — Reubicado desde `wiki/5_control/datos_metricas_semanales/` en la reestructuración PARA en cascada; creado el índice (no existía).*

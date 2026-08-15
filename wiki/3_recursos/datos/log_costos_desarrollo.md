# Log de Costos de Desarrollo — Base de datos de la métrica USD/SP

> **Última ingesta:** 2026-07-27 — `Stock_JUN_2026__final_.xlsx` (Junio 2026, AD + OB + SER + WS, 5700 hs / $276240).
>
> Este archivo es la **base de datos acumulada** de costo de desarrollo, mantenida por la skill [`/dashboard_delivery`](../../.claude/skills/dashboard_delivery/SKILL.md) a partir del **stock de horas mensual que factura Fintexa** (Excel `Stock de Horas - <Mes><Año>` depositado en `raw/`). Junto con [`log_performance_desarrollo.md`](log_performance_desarrollo.md) (SP publicados) alimenta la pestaña **USD por SP** del dashboard [`outputs/dashboard_performance_desarrollo.html`](../../outputs/dashboard_performance_desarrollo.html): cuánto cuesta un punto de historia y cómo evoluciona ese costo mes a mes.

## Metodología / criterios de agregación

- **Horas de desarrollo:** todas las secciones del stock salvo `SOPORTE` e `IT` (no son desarrollo de producto). Incluye `OPERATIVO`, `DEVOPS`, `COE`, `GESTION`, `KITS`/`DEUDA`, `ONBOARDING`/`S.A.`.
- **Cálculo del costo — fila por fila, nunca promediado:** `USD = Horas Mes × Valor Hora del perfil de esa fila`. El costo total de un espacio es la suma de ese producto en todas sus filas; el "USD/hora promedio" que resulta de dividir el total es un efecto de la mezcla de perfiles asignados ese mes, no un insumo del cálculo.
- **Imputación por Componente / Proyecto:** Wallet / Wallet Services / Wallet APK → **WS**; Cobro y Admin / BP / BO → **AD**; Onboarding / Onboarding PJ / OB-93 Legajos → **OB**; Deuda → **SER**; Todos y Comité de Arquitectura → **50% WS / 50% AD** (esfuerzo transversal). Componente no reconocido → fila descartada y advertida, nunca imputada por adivinanza.
- **Tarifas faltantes (carry-forward):** cuando el Excel de un mes no trae su propia tabla de precios, se hereda la tarifa del mes conocido más cercano (si hay empate entre uno anterior y uno posterior, gana el anterior). Cada fila del registro de tarifas abajo indica si es `propia` o `heredada de <Mes Año>`.
- **Ventana de ingesta:** Ene'25 y Jun'25 no se ingieren (fuera del rango de SP publicados, que arranca en Jul'25; Ene'25 además usa un layout distinto).
- **Relación con SP:** la métrica USD/SP se calcula en el dashboard cruzando este log con `log_performance_desarrollo.md` por año × mes × espacio. Si un espacio no tiene SP publicados ese mes (hoy: OB y SER), USD/SP da **0** — no se oculta ni se propaga a otros espacios.

## Registro de lotes ingeridos

| Fecha ingesta | Archivo fuente | Cobertura | Horas | USD | Destino histórico |
|---|---|---|---|---|---|
| 2026-07-21 | `Stock JUL_2025 (1).xlsm` | Julio 2025, AD + OB + WS | 6024 | 292160 | `4_archivos/historial_raw/2026-07_backfill_stock_horas_fintexa/` |
| 2026-07-21 | `Control hs ago.25.xlsm` | Agosto 2025, AD + OB + WS | 6232 | 301020 | `4_archivos/historial_raw/2026-07_backfill_stock_horas_fintexa/` |
| 2026-07-21 | `Stock SEP_2025.xlsm` | Septiembre 2025, AD + OB + SER + WS | 6556 | 316520 | `4_archivos/historial_raw/2026-07_backfill_stock_horas_fintexa/` |
| 2026-07-21 | `Stock OCT_2025.xlsm` | Octubre 2025, AD + OB + SER + WS | 6702 | 326624 | `4_archivos/historial_raw/2026-07_backfill_stock_horas_fintexa/` |
| 2026-07-21 | `Stock NOV_2025 (1).xlsm` | Noviembre 2025, AD + OB + SER + WS | 6960 | 343840 | `4_archivos/historial_raw/2026-07_backfill_stock_horas_fintexa/` |
| 2026-07-21 | `Stock DIC_2025.xlsm` | Diciembre 2025, AD + OB + SER + WS | 7120 | 351520 | `4_archivos/historial_raw/2026-07_backfill_stock_horas_fintexa/` |
| 2026-07-21 | `Stock ENE_2026.xlsm` | Enero 2026, AD + OB + SER + WS | 7040 | 341920 | `4_archivos/historial_raw/2026-07_backfill_stock_horas_fintexa/` |
| 2026-07-21 | `Stock FEB_2026.xlsm` | Febrero 2026, AD + OB + SER + WS | 6672 | 322080 | `4_archivos/historial_raw/2026-07_backfill_stock_horas_fintexa/` |
| 2026-07-21 | `Stock MAR_2026.xlsm` | Marzo 2026, AD + OB + SER + WS | 6126 | 295232 | `4_archivos/historial_raw/2026-07_backfill_stock_horas_fintexa/` |
| 2026-07-21 | `Stock_ABR_2026 (2).xlsx` | Abril 2026, AD + OB + SER + WS | 5533 | 268744 | `4_archivos/historial_raw/2026-07_backfill_stock_horas_fintexa/` |
| 2026-07-21 | `Stock_MAY_2026 (final).xlsx` | Mayo 2026, AD + OB + SER + WS | 5832 | 282576 | `4_archivos/historial_raw/2026-07_backfill_stock_horas_fintexa/` |
| 2026-07-21 | `Stock_JUN_2026__final_.xlsx` | Junio 2026, AD + OB + SER + WS | 5700 | 276240 | `4_archivos/historial_raw/2026-07_backfill_stock_horas_fintexa/` |

## Registro de tarifas por perfil

| Año | Mes | Perfil | USD/h | Origen |
|---|---|---|---|---|
| 2025 | Julio | analista | 48 | heredada de Noviembre 2025 |
| 2025 | Julio | arq | 60 | heredada de Noviembre 2025 |
| 2025 | Julio | dev | 48 | heredada de Noviembre 2025 |
| 2025 | Julio | devops | 55 | heredada de Noviembre 2025 |
| 2025 | Julio | lider | 60 | heredada de Noviembre 2025 |
| 2025 | Julio | qa | 35 | heredada de Noviembre 2025 |
| 2025 | Agosto | analista | 48 | heredada de Noviembre 2025 |
| 2025 | Agosto | arq | 60 | heredada de Noviembre 2025 |
| 2025 | Agosto | dev | 48 | heredada de Noviembre 2025 |
| 2025 | Agosto | devops | 55 | heredada de Noviembre 2025 |
| 2025 | Agosto | lider | 60 | heredada de Noviembre 2025 |
| 2025 | Agosto | qa | 35 | heredada de Noviembre 2025 |
| 2025 | Septiembre | analista | 48 | heredada de Noviembre 2025 |
| 2025 | Septiembre | arq | 60 | heredada de Noviembre 2025 |
| 2025 | Septiembre | dev | 48 | heredada de Noviembre 2025 |
| 2025 | Septiembre | devops | 55 | heredada de Noviembre 2025 |
| 2025 | Septiembre | lider | 60 | heredada de Noviembre 2025 |
| 2025 | Septiembre | qa | 35 | heredada de Noviembre 2025 |
| 2025 | Octubre | analista | 48 | heredada de Noviembre 2025 |
| 2025 | Octubre | arq | 60 | heredada de Noviembre 2025 |
| 2025 | Octubre | dev | 48 | heredada de Noviembre 2025 |
| 2025 | Octubre | devops | 55 | heredada de Noviembre 2025 |
| 2025 | Octubre | lider | 60 | heredada de Noviembre 2025 |
| 2025 | Octubre | qa | 35 | heredada de Noviembre 2025 |
| 2025 | Noviembre | analista | 48 | propia |
| 2025 | Noviembre | arq | 60 | propia |
| 2025 | Noviembre | dev | 48 | propia |
| 2025 | Noviembre | devops | 55 | propia |
| 2025 | Noviembre | lider | 60 | propia |
| 2025 | Noviembre | qa | 35 | propia |
| 2025 | Diciembre | analista | 48 | heredada de Noviembre 2025 |
| 2025 | Diciembre | arq | 60 | heredada de Noviembre 2025 |
| 2025 | Diciembre | dev | 48 | heredada de Noviembre 2025 |
| 2025 | Diciembre | devops | 55 | heredada de Noviembre 2025 |
| 2025 | Diciembre | lider | 60 | heredada de Noviembre 2025 |
| 2025 | Diciembre | qa | 35 | heredada de Noviembre 2025 |
| 2026 | Enero | analista | 48 | propia |
| 2026 | Enero | arq | 60 | propia |
| 2026 | Enero | dev | 48 | propia |
| 2026 | Enero | devops | 40 | propia |
| 2026 | Enero | lider | 60 | propia |
| 2026 | Enero | qa | 35 | propia |
| 2026 | Febrero | analista | 48 | propia |
| 2026 | Febrero | arq | 60 | propia |
| 2026 | Febrero | dev | 48 | propia |
| 2026 | Febrero | devops | 40 | propia |
| 2026 | Febrero | lider | 60 | propia |
| 2026 | Febrero | qa | 35 | propia |
| 2026 | Marzo | analista | 48 | heredada de Febrero 2026 |
| 2026 | Marzo | arq | 60 | heredada de Febrero 2026 |
| 2026 | Marzo | dev | 48 | heredada de Febrero 2026 |
| 2026 | Marzo | devops | 40 | heredada de Febrero 2026 |
| 2026 | Marzo | lider | 60 | heredada de Febrero 2026 |
| 2026 | Marzo | qa | 35 | heredada de Febrero 2026 |
| 2026 | Abril | analista | 48 | propia |
| 2026 | Abril | arq | 60 | propia |
| 2026 | Abril | dev | 48 | propia |
| 2026 | Abril | devops | 40 | propia |
| 2026 | Abril | lider | 60 | propia |
| 2026 | Abril | qa | 35 | propia |
| 2026 | Mayo | analista | 48 | propia |
| 2026 | Mayo | arq | 60 | propia |
| 2026 | Mayo | dev | 48 | propia |
| 2026 | Mayo | devops | 40 | propia |
| 2026 | Mayo | lider | 60 | propia |
| 2026 | Mayo | qa | 35 | propia |
| 2026 | Junio | analista | 48 | propia |
| 2026 | Junio | arq | 60 | propia |
| 2026 | Junio | dev | 48 | propia |
| 2026 | Junio | devops | 40 | propia |
| 2026 | Junio | lider | 60 | propia |
| 2026 | Junio | qa | 35 | propia |

## Resumen mensual (horas / USD de desarrollo)

| Año | Mes | AD | OB | SER | WS | Total |
|---|---|---|---|---|---|---|
| 2025 | Julio | 3248 hs / $159360 | 160 hs / $6640 | — | 2616 hs / $126160 | **6024 hs / $292160** |
| 2025 | Agosto | 3328 hs / $163340 | 160 hs / $6640 | — | 2744 hs / $131040 | **6232 hs / $301020** |
| 2025 | Septiembre | 3328 hs / $163340 | 240 hs / $10480 | 336 hs / $16128 | 2652 hs / $126572 | **6556 hs / $316520** |
| 2025 | Octubre | 3409 hs / $168296 | 240 hs / $10480 | 336 hs / $16128 | 2717 hs / $131720 | **6702 hs / $326624** |
| 2025 | Noviembre | 3400 hs / $170040 | 240 hs / $10480 | 336 hs / $17280 | 2984 hs / $146040 | **6960 hs / $343840** |
| 2025 | Diciembre | 3480 hs / $173880 | 240 hs / $10480 | 336 hs / $17280 | 3064 hs / $149880 | **7120 hs / $351520** |
| 2026 | Enero | 3504 hs / $170920 | 160 hs / $7680 | 336 hs / $17280 | 3040 hs / $146040 | **7040 hs / $341920** |
| 2026 | Febrero | 3592 hs / $173560 | 160 hs / $7680 | 336 hs / $16704 | 2584 hs / $124136 | **6672 hs / $322080** |
| 2026 | Marzo | 3000 hs / $145320 | 174 hs / $8352 | 336 hs / $16704 | 2616 hs / $124856 | **6126 hs / $295232** |
| 2026 | Abril | 2760 hs / $133800 | 253 hs / $12144 | 80 hs / $3840 | 2440 hs / $118960 | **5533 hs / $268744** |
| 2026 | Mayo | 2840 hs / $136160 | 432 hs / $20736 | 80 hs / $3840 | 2480 hs / $121840 | **5832 hs / $282576** |
| 2026 | Junio | 2840 hs / $136160 | 300 hs / $14400 | 80 hs / $3840 | 2480 hs / $121840 | **5700 hs / $276240** |
| **Total** | **histórico** | **38729 hs / $1894176** | **2759 hs / $126192** | **2592 hs / $129024** | **32417 hs / $1569084** | **76497 hs / $3718476** |

## Datos — detalle año × mes × espacio

| Año | Mes | Espacio | Horas | USD |
|---|---|---|---|---|
| 2025 | Julio | AD | 3248 | 159360 |
| 2025 | Julio | OB | 160 | 6640 |
| 2025 | Julio | WS | 2616 | 126160 |
| 2025 | Agosto | AD | 3328 | 163340 |
| 2025 | Agosto | OB | 160 | 6640 |
| 2025 | Agosto | WS | 2744 | 131040 |
| 2025 | Septiembre | AD | 3328 | 163340 |
| 2025 | Septiembre | OB | 240 | 10480 |
| 2025 | Septiembre | SER | 336 | 16128 |
| 2025 | Septiembre | WS | 2652 | 126572 |
| 2025 | Octubre | AD | 3409 | 168296 |
| 2025 | Octubre | OB | 240 | 10480 |
| 2025 | Octubre | SER | 336 | 16128 |
| 2025 | Octubre | WS | 2717 | 131720 |
| 2025 | Noviembre | AD | 3400 | 170040 |
| 2025 | Noviembre | OB | 240 | 10480 |
| 2025 | Noviembre | SER | 336 | 17280 |
| 2025 | Noviembre | WS | 2984 | 146040 |
| 2025 | Diciembre | AD | 3480 | 173880 |
| 2025 | Diciembre | OB | 240 | 10480 |
| 2025 | Diciembre | SER | 336 | 17280 |
| 2025 | Diciembre | WS | 3064 | 149880 |
| 2026 | Enero | AD | 3504 | 170920 |
| 2026 | Enero | OB | 160 | 7680 |
| 2026 | Enero | SER | 336 | 17280 |
| 2026 | Enero | WS | 3040 | 146040 |
| 2026 | Febrero | AD | 3592 | 173560 |
| 2026 | Febrero | OB | 160 | 7680 |
| 2026 | Febrero | SER | 336 | 16704 |
| 2026 | Febrero | WS | 2584 | 124136 |
| 2026 | Marzo | AD | 3000 | 145320 |
| 2026 | Marzo | OB | 174 | 8352 |
| 2026 | Marzo | SER | 336 | 16704 |
| 2026 | Marzo | WS | 2616 | 124856 |
| 2026 | Abril | AD | 2760 | 133800 |
| 2026 | Abril | OB | 253 | 12144 |
| 2026 | Abril | SER | 80 | 3840 |
| 2026 | Abril | WS | 2440 | 118960 |
| 2026 | Mayo | AD | 2840 | 136160 |
| 2026 | Mayo | OB | 432 | 20736 |
| 2026 | Mayo | SER | 80 | 3840 |
| 2026 | Mayo | WS | 2480 | 121840 |
| 2026 | Junio | AD | 2840 | 136160 |
| 2026 | Junio | OB | 300 | 14400 |
| 2026 | Junio | SER | 80 | 3840 |
| 2026 | Junio | WS | 2480 | 121840 |

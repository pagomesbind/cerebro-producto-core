# Log de Performance de QA — Base de datos del dashboard "Performance de QA"

> **Última ingesta:** 2026-07-27 — `2026-07-27 11-08-Tiempo QA.csv` (2025-10 – 2026-07, ADQUIRENCIA + ARDID + EMISIÓN + ONBOARDING + SERVICIOS, 853 tickets).
>
> Este archivo es la **base de datos acumulada**, por ticket, del dashboard [`outputs/dashboard_performance_qa.html`](../../outputs/dashboard_performance_qa.html), mantenida por la skill [`/dashboard_qa`](../../.claude/skills/dashboard_qa/SKILL.md). El usuario deja en `raw/` un export de Jira "Tiempo QA" (una fila por ticket, tiempo acumulado por estado). Cada ingesta hace **upsert por `Clave`**: el ticket que reaparece se actualiza con el dato fresco (su tiempo en QA puede haber cambiado si seguía abierto), el que no aparece en el export nuevo se conserva tal cual. Los agregados del dashboard se recalculan enteros desde este detalle en cada corrida — **no hace falta releer los CSV históricos**.

## Metodología / criterios de agregación

- **Equipo de QA** (`wiki/0_direccion/equipo.md`): Andrea Orsini, Bethania Tornari, Ana Moreno. Todo lo demás (Producto, PM de desarrollo, Unassigned) se agrupa como "Otros" — tanto para "Persona asignada" (quién testeó) como para "Creador" (quién reportó una observación).
- **Tiempo en QA** = suma de todas las variantes de columna "EN QA*" del export (el proveedor las parte por variante de workflow). Es **tiempo calendario** (24h/día, 7d/semana), no horas hábiles — el export no trae las fechas de transición necesarias para descontar fines de semana.
- **Universo de las métricas de tiempo (tiempo en QA / tiempo por SP):** tickets con tiempo en QA > 0 y estado ≠ `EN QA` (su reloj ya paró, sea `Finalizada` o `Bloqueado`). Los tickets hoy en `EN QA` (20) se excluyen de esas métricas — su tiempo sigue corriendo, promediarlo no mide nada — y se reportan aparte como "aún en QA". Los tickets que nunca pasaron por QA (75) se reportan como "sin paso por QA".
- **Observación** = ticket con prefijo `[OBS]`/`[DEF]`/`[REQ]` en el Resumen (`gestion_jira.md` §1.3), no todo ticket tipo Error. Total histórico: 325.
- **Story Points nulos:** el ticket queda fuera de la métrica "tiempo por SP" (no computa 0 — sesgaría el ratio a la baja).
- **Eje X — 3 anclas posibles, "por asignación a QA" es la default (decisión del usuario, 2026-07-27):**
  - **Por asignación a QA (default):** ubica el ticket en el mes en que **entró por primera vez a `EN QA`** = `Creada` + Σ de todas las columnas de tiempo previas a `EN QA` (`Backlog`/`Asignado`/`Listo para desarrollo`/`En curso`, todas sus variantes). Es la ancla más representativa de "qué estaba testeando el equipo ese mes": el desfasaje entre creación y entrada a QA (mediana 16.92 días) es mucho mayor que el desfasaje entre entrada a QA y cierre — agrupar por creación arrastra ese desfasaje largo al gráfico, agrupar por asignación a QA casi no. Validado empíricamente antes de construir: Σ(todas las columnas de tiempo del export) ≈ (fecha de export − `Creada`) en 839/853 tickets (error > 1 día en solo 14) — confirma que cada columna es una duración real y aditiva, y que el estado terminal (`Finalizada`) sigue corriendo hasta el export, no se congela en `Resuelta`. Solo definido para tickets que alguna vez llegaron a `EN QA` (778 de 853) — a diferencia de "por creación", acá **no hay** censura por tickets que todavía no llegaron a QA (simplemente no aparecen en el eje bajo este modo).
    - **⚠️ Caveat sin resolver — rebote a "Con defecto":** el export no trae la secuencia de transiciones, solo totales acumulados por estado. Para los 124 tickets que alguna vez pasaron por `Con defecto` (columna `Rebote = Sí` en el detalle), no se puede distinguir si el tiempo en `En curso`/`Asignado`/etc. ocurrió TODO antes de la primera llegada a `EN QA`, o si una parte es retrabajo posterior al rebote — de ser así, esos tickets podrían quedar ubicados en un mes posterior al real. Evidencia indirecta de que puede haber mezcla: los tickets con rebote tienen más del doble de tiempo mediano en "En curso" que los que nunca rebotaron (9,1d vs 3,9d). El dashboard expone un KPI aparte ("Con rebote"), no oculta los tickets.
  - **Por creación:** ubica el ticket en su mes de `Creada`. Como el tiempo en QA se mide solo sobre tickets ya cerrados, los meses recientes muestran únicamente los tickets que cerraron rápido — los lentos siguen abiertos. Esto hace que los últimos 2-3 meses del gráfico se vean sistemáticamente más veloces de lo que realmente son (censura estadística fuerte, porque el desfasaje pre-QA es largo), no por mejora real. Se mantiene como toggle secundario, útil para ver "cuándo entró el trabajo" en vez de "cuándo se testeó".
  - **Por resolución:** ubica el ticket en su mes de `Resuelta` (si el export la trae). Mezcla tickets creados en distintos meses que cerraron el mismo mes — útil como segundo cruce independiente para detectar si el sesgo de otro modo es real.
  - En los 3 modos, los meses con cohorte incompleta se marcan en itálica en el eje X (criterio según la pestaña: tickets aún en `EN QA` para Tiempo en QA/Tiempo por SP; no aplica a Observaciones).
- **Recorte de consistencia:** si el tiempo en QA de un ticket supera el lag total `Resuelta − Creada` (posible por el redondeo de "M" a 30,44 días), se recorta a ese lag y se advierte en la ingesta.

## Registro de lotes ingeridos

| Fecha ingesta | Archivo fuente | Cobertura | Tickets tocados | Destino histórico |
|---|---|---|---|---|
| 2026-07-27 | `2026-07-27 10-56-Tiempo QA.csv` | 2025-10 – 2026-07, ADQUIRENCIA + ARDID + EMISIÓN + ONBOARDING + SERVICIOS | 853 tickets | `4_archivos/historial_raw/2026-07_reporte_tiempo_qa/` |
| 2026-07-27 | `2026-07-27 11-08-Tiempo QA.csv` | 2025-10 – 2026-07, ADQUIRENCIA + ARDID + EMISIÓN + ONBOARDING + SERVICIOS | 853 tickets | `4_archivos/historial_raw/2026-07_reporte_tiempo_qa/` |

## Resumen mensual (sanity check — el dashboard recalcula todo del detalle)

| Mes (creación) | Tickets creados | Con QA cerrado | Mediana días en QA (equipo) | Mediana días hasta EN QA | Observaciones | Aún en QA | Sin paso por QA |
|---|---|---|---|---|---|---|---|
| 2025-10 | 63 | 51 | 7.14 | 36.24 | 13 | 0 | 12 |
| 2025-11 | 114 | 98 | 4.99 | 29.66 | 50 | 0 | 16 |
| 2025-12 | 145 | 133 | 5.98 | 19.81 | 47 | 1 | 11 |
| 2026-01 | 126 | 118 | 2.98 | 11.06 | 53 | 0 | 8 |
| 2026-02 | 115 | 106 | 3.73 | 19.67 | 40 | 1 | 8 |
| 2026-03 | 81 | 73 | 2.72 | 19.1 | 37 | 2 | 6 |
| 2026-04 | 71 | 62 | 1.91 | 15.02 | 30 | 3 | 6 |
| 2026-05 | 65 | 58 | 1.06 | 6.49 | 20 | 4 | 3 |
| 2026-06 | 55 | 43 | 1.04 | 10.96 | 30 | 8 | 4 |
| 2026-07 | 18 | 16 | 0.12 | 0.96 | 5 | 1 | 1 |

## Datos — detalle por ticket

| Clave | Proyecto | Tipo | Estado | Creada | Resuelta | Asignado | Creador | SP | Horas QA | Horas Defecto | Horas pre-QA | Rebote | Obs |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| WS-29 | EMISIÓN | Historia | Finalizada | 2025-10-01 | 2025-10-31 | Unassigned | malzogaray | 15 | 46.48 | 0 | 675.4 | No | — |
| AD-11 | ADQUIRENCIA | Historia | Finalizada | 2025-10-07 | 2026-02-26 | Andrea ORSINI | malzogaray | — | 39 | 2479.58 | 869.68 | Sí | — |
| WS-40 | EMISIÓN | Historia | Finalizada | 2025-10-07 | 2025-11-26 | Andrea ORSINI | Pablo Antonio GOMES | 7 | 241.12 | 0 | 965.55 | No | — |
| WS-41 | EMISIÓN | Historia | Finalizada | 2025-10-07 | 2025-11-26 | Andrea ORSINI | Pablo Antonio GOMES | 7 | 241.12 | 0 | 965.53 | No | — |
| WS-11 | EMISIÓN | Historia | Finalizada | 2025-10-08 | 2025-10-29 | Unassigned | malzogaray | 3 | 46.45 | 0 | 452.83 | No | — |
| WS-13 | EMISIÓN | Historia | Finalizada | 2025-10-08 | 2025-11-05 | Unassigned | malzogaray | 15 | 46.45 | 0 | 622.27 | No | — |
| WS-27 | EMISIÓN | Historia | Finalizada | 2025-10-08 | 2025-11-14 | Unassigned | malzogaray | 7 | 431.38 | 0 | 452.65 | No | — |
| WS-33 | EMISIÓN | Historia | Finalizada | 2025-10-08 | 2025-11-07 | Unassigned | malzogaray | 7 | 262.8 | 0 | 452.55 | No | — |
| WS-34 | EMISIÓN | Historia | Finalizada | 2025-10-08 | 2025-11-07 | Unassigned | malzogaray | 1 | 263.18 | 0 | 452.6 | No | — |
| AD-23 | ADQUIRENCIA | Historia | Finalizada | 2025-10-09 | 2025-11-03 | Unassigned | malzogaray | — | 71.55 | 0 | 522.88 | No | OBS |
| AD-30 | ADQUIRENCIA | Historia | Finalizada | 2025-10-09 | 2025-11-14 | Nicolás Colón | malzogaray | — | 270.82 | 0 | 594.25 | No | — |
| WS-26 | EMISIÓN | Historia | Finalizada | 2025-10-09 | 2025-11-07 | Unassigned | malzogaray | 3 | 281.42 | 0 | 410.52 | No | — |
| AD-13 | ADQUIRENCIA | Historia | Finalizada | 2025-10-13 | 2025-11-14 | Unassigned | Pablo Antonio GOMES | — | 270.78 | 0 | 503.87 | No | — |
| AD-31 | ADQUIRENCIA | Error | Finalizada | 2025-10-14 | 2025-11-06 | Unassigned | malzogaray | — | 74.45 | 0 | 479.08 | No | OBS |
| AD-32 | ADQUIRENCIA | Error | Finalizada | 2025-10-14 | 2025-11-06 | Unassigned | malzogaray | — | 74.47 | 0 | 479.08 | No | OBS |
| AD-33 | ADQUIRENCIA | Error | Finalizada | 2025-10-14 | 2025-11-06 | Unassigned | malzogaray | — | 74.47 | 0 | 479.1 | No | OBS |
| AD-12 | ADQUIRENCIA | Historia | Finalizada | 2025-10-21 | 2025-11-03 | Unassigned | malzogaray | — | 291.55 | 0 | 17.17 | No | — |
| AD-15 | ADQUIRENCIA | Historia | Finalizada | 2025-10-22 | 2025-11-06 | Unassigned | malzogaray | — | 0 | 0 | 361.57 | No | OBS |
| AD-16 | ADQUIRENCIA | Error | Finalizada | 2025-10-22 | 2026-03-12 | Andrea ORSINI | malzogaray | 3 | 217.97 | 0 | 3169.1 | No | OBS |
| AD-17 | ADQUIRENCIA | Error | Finalizada | 2025-10-22 | 2025-11-06 | Unassigned | malzogaray | — | 52.55 | 0 | 309.02 | No | OBS |
| AD-18 | ADQUIRENCIA | Error | Finalizada | 2025-10-22 | 2026-02-26 | Andrea ORSINI | malzogaray | 1 | 1042.33 | 0 | 1498.04 | No | OBS |
| WS-12 | EMISIÓN | Historia | Finalizada | 2025-10-22 | 2025-10-31 | Unassigned | malzogaray | 15 | 46.48 | 0 | 170.48 | No | — |
| AD-25 | ADQUIRENCIA | Historia | Finalizada | 2025-10-23 | 2026-01-27 | Nicolás Colón | malzogaray | 3 | 88.08 | 266.03 | 1940.99 | Sí | — |
| AD-10 | ADQUIRENCIA | Historia | Finalizada | 2025-10-24 | 2025-11-14 | Unassigned | malzogaray | — | 437.92 | 0 | 71.72 | No | OBS |
| AD-14 | ADQUIRENCIA | Error | Finalizada | 2025-10-24 | 2025-11-06 | Unassigned | malzogaray | — | 52.72 | 0 | 263.1 | No | OBS |
| AD-24 | ADQUIRENCIA | Historia | Finalizada | 2025-10-24 | 2025-11-03 | Unassigned | malzogaray | — | 0 | 0 | 238.95 | No | — |
| AD-26 | ADQUIRENCIA | Historia | Finalizada | 2025-10-24 | 2025-11-14 | Unassigned | malzogaray | — | 270.83 | 0 | 238.37 | No | — |
| AD-27 | ADQUIRENCIA | Historia | Finalizada | 2025-10-24 | 2025-11-03 | Unassigned | malzogaray | — | 0 | 0 | 238.37 | No | — |
| AD-28 | ADQUIRENCIA | Historia | Finalizada | 2025-10-24 | 2025-11-03 | Unassigned | malzogaray | — | 0.68 | 0 | 238.37 | No | — |
| AD-29 | ADQUIRENCIA | Historia | Finalizada | 2025-10-24 | 2025-11-03 | Unassigned | malzogaray | — | 167.07 | 0 | 71.5 | No | OBS |
| SER-2 | SERVICIOS | Historia | Finalizada | 2025-10-27 | 2026-02-23 | Nicolás Colón | Pablo Antonio GOMES | — | 1579.99 | 0 | 1281.76 | No | — |
| SER-3 | SERVICIOS | Historia | Finalizada | 2025-10-27 | 2026-02-23 | Nicolás Colón | Pablo Antonio GOMES | — | 1579.99 | 0 | 1281.78 | No | — |
| SER-4 | SERVICIOS | Historia | Finalizada | 2025-10-27 | 2026-02-20 | Nicolás Colón | Pablo Antonio GOMES | — | 1460.79 | 47.53 | 1281.74 | Sí | — |
| SER-5 | SERVICIOS | Historia | Finalizada | 2025-10-27 | 2026-02-18 | Nicolás Colón | Pablo Antonio GOMES | — | 1460.55 | 0 | 1281.74 | No | — |
| SER-6 | SERVICIOS | Historia | Finalizada | 2025-10-27 | 2026-02-18 | Nicolás Colón | Pablo Antonio GOMES | — | 1460.39 | 0 | 1281.74 | No | — |
| SER-7 | SERVICIOS | Historia | Finalizada | 2025-10-27 | 2026-07-17 | Nicolás Colón | Pablo Antonio GOMES | — | 1.08 | 694.57 | 5631.04 | Sí | — |
| WS-20 | EMISIÓN | Historia | Finalizada | 2025-10-30 | 2026-01-12 | Bethania | Pablo Antonio GOMES | 3 | 171.32 | 0 | 1617.14 | No | — |
| WS-21 | EMISIÓN | Historia | Finalizada | 2025-10-30 | 2026-01-20 | Bethania | Pablo Antonio GOMES | 3 | 89.65 | 0 | 1882.54 | No | — |
| WS-23 | EMISIÓN | Historia | Finalizada | 2025-10-30 | 2026-01-12 | Bethania | Pablo Antonio GOMES | 3 | 170.48 | 0 | 1617.14 | No | — |
| WS-24 | EMISIÓN | Historia | Finalizada | 2025-10-30 | 2026-01-12 | Bethania | Pablo Antonio GOMES | 7 | 170.38 | 0 | 1617.19 | No | — |
| WS-25 | EMISIÓN | Historia | Finalizada | 2025-10-30 | 2026-01-12 | Bethania | Pablo Antonio GOMES | 7 | 164.85 | 0 | 1617.19 | No | — |
| AD-19 | ADQUIRENCIA | Historia | Finalizada | 2025-10-31 | 2025-11-03 | Unassigned | malzogaray | — | 0 | 0 | 63.67 | No | — |
| AD-20 | ADQUIRENCIA | Historia | Finalizada | 2025-10-31 | 2025-11-03 | Unassigned | malzogaray | — | 0 | 0 | 63.67 | No | — |
| AD-21 | ADQUIRENCIA | Historia | Finalizada | 2025-10-31 | 2025-11-03 | Unassigned | malzogaray | — | 0 | 0 | 63.67 | No | — |
| AD-22 | ADQUIRENCIA | Historia | Finalizada | 2025-10-31 | 2025-11-03 | Unassigned | malzogaray | — | 0 | 0 | 63.48 | No | — |
| WS-14 | EMISIÓN | Historia | Finalizada | 2025-10-31 | 2025-11-14 | Unassigned | Pablo Antonio GOMES | 3 | 0 | 334.53 | 0 | Sí | — |
| WS-15 | EMISIÓN | Historia | Finalizada | 2025-10-31 | 2025-11-26 | Nicolás Colón | Pablo Antonio GOMES | 7 | 194.87 | 0 | 434.53 | No | — |
| WS-16 | EMISIÓN | Historia | Finalizada | 2025-10-31 | 2026-01-14 | Nicolás Colón | Pablo Antonio GOMES | 1 | 23.8 | 0 | 1796.19 | No | — |
| WS-17 | EMISIÓN | Historia | Finalizada | 2025-10-31 | 2025-11-26 | Nicolás Colón | Pablo Antonio GOMES | 7 | 194.88 | 0 | 434.53 | No | — |
| WS-18 | EMISIÓN | Historia | Finalizada | 2025-10-31 | 2025-11-26 | Nicolás Colón | Pablo Antonio GOMES | 15 | 194.87 | 0 | 434.53 | No | — |
| WS-19 | EMISIÓN | Historia | Finalizada | 2025-10-31 | 2026-02-04 | Nicolás Colón | Pablo Antonio GOMES | 7 | 379.4 | 0 | 1919.89 | No | — |
| WS-30 | EMISIÓN | Historia | Finalizada | 2025-10-31 | 2025-12-11 | Andrea ORSINI | Pablo Antonio GOMES | 7 | 137.63 | 0 | 974.34 | No | — |
| WS-31 | EMISIÓN | Historia | Finalizada | 2025-10-31 | 2025-12-16 | Ana | Pablo Antonio GOMES | 7 | 141.75 | 0 | 974.38 | No | OBS |
| WS-32 | EMISIÓN | Historia | Finalizada | 2025-10-31 | 2025-12-12 | Nicolas Pomponio | Pablo Antonio GOMES | 3 | 0 | 0 | 1017.19 | No | — |
| WS-36 | EMISIÓN | Historia | Finalizada | 2025-10-31 | 2026-01-16 | Ana | Pablo Antonio GOMES | — | 895.68 | 0 | 974.48 | No | — |
| WS-37 | EMISIÓN | Historia | Finalizada | 2025-10-31 | 2025-11-26 | Ana | Pablo Antonio GOMES | 7 | 189.9 | 0 | 434.42 | No | — |
| WS-38 | EMISIÓN | Historia | Finalizada | 2025-10-31 | 2025-11-13 | Unassigned | Pablo Antonio GOMES | 3 | 0 | 0 | 315.33 | No | — |
| WS-39 | EMISIÓN | Historia | Finalizada | 2025-10-31 | 2025-11-13 | Unassigned | Pablo Antonio GOMES | 3 | 0 | 0 | 315.33 | No | — |
| WS-44 | EMISIÓN | Error | Finalizada | 2025-10-31 | 2025-12-10 | Nicolás Colón | Pablo Antonio GOMES | 1 | 49.12 | 0 | 914.92 | No | OBS |
| WS-46 | EMISIÓN | Historia | Finalizada | 2025-10-31 | 2025-12-12 | Bethania | Pablo Antonio GOMES | 15 | 65.17 | 0 | 934.58 | No | — |
| WS-49 | EMISIÓN | Historia | Finalizada | 2025-10-31 | 2026-03-04 | malzogaray | Pablo Antonio GOMES | 15 | 0 | 0 | 2834.93 | No | — |
| WS-52 | EMISIÓN | Historia | Finalizada | 2025-10-31 | 2025-12-11 | Andrea ORSINI | Pablo Antonio GOMES | 1 | 23.1 | 0 | 970.34 | No | — |
| WS-53 | EMISIÓN | Historia | Finalizada | 2025-10-31 | 2026-01-12 | Andrea ORSINI | Pablo Antonio GOMES | 15 | 802.06 | 0 | 959.72 | No | — |
| AD-37 | ADQUIRENCIA | Error | Finalizada | 2025-11-03 | 2025-12-18 | Nicolás Colón | malzogaray | — | 143.5 | 0 | 949.16 | No | OBS |
| AD-38 | ADQUIRENCIA | Error | Finalizada | 2025-11-03 | 2026-01-06 | Nicolás Colón | malzogaray | 1 | 93.35 | 0 | 1455.01 | No | OBS |
| AD-39 | ADQUIRENCIA | Error | Finalizada | 2025-11-03 | 2025-12-01 | Andrea ORSINI | malzogaray | 3 | 121.67 | 0 | 552.6 | No | OBS |
| AD-40 | ADQUIRENCIA | Historia | Finalizada | 2025-11-03 | 2026-03-04 | Bethania | malzogaray | 3 | 1396.23 | 0 | 1516.85 | No | — |
| AD-41 | ADQUIRENCIA | Historia | Finalizada | 2025-11-03 | 2026-02-19 | Bethania | malzogaray | 7 | 591.12 | 646.55 | 1365.19 | Sí | — |
| AD-42 | ADQUIRENCIA | Historia | Finalizada | 2025-11-03 | 2026-03-02 | Bethania | malzogaray | 3 | 149.02 | 0 | 2710.3 | No | — |
| AD-43 | ADQUIRENCIA | Historia | Finalizada | 2025-11-03 | 2026-03-09 | malzogaray | malzogaray | 3 | 554.75 | 310.72 | 2159.59 | Sí | — |
| AD-44 | ADQUIRENCIA | Historia | Finalizada | 2025-11-03 | 2025-12-12 | Bethania | malzogaray | 15 | 47.68 | 0 | 905.36 | No | — |
| AD-45 | ADQUIRENCIA | Error | Finalizada | 2025-11-03 | 2026-01-13 | Bethania | malzogaray | 1 | 96.78 | 0 | 1618.31 | No | OBS |
| AD-46 | ADQUIRENCIA | Historia | Finalizada | 2025-11-03 | 2026-02-12 | Bethania | malzogaray | 3 | 258.15 | 1281.61 | 905.38 | Sí | — |
| AD-50 | ADQUIRENCIA | Error | Bloqueado | 2025-11-03 | — | malzogaray | malzogaray | 1 | 358.98 | 118.03 | 3103.57 | Sí | OBS |
| AD-52 | ADQUIRENCIA | Error | Finalizada | 2025-11-03 | 2025-11-03 | Nicolás Colón | malzogaray | — | 0 | 0 | 0.07 | No | OBS |
| AD-53 | ADQUIRENCIA | Error | Finalizada | 2025-11-03 | 2025-12-16 | Nicolás Colón | malzogaray | — | 24.45 | 0 | 1016.46 | No | OBS |
| AD-54 | ADQUIRENCIA | Error | Finalizada | 2025-11-03 | 2025-12-16 | Nicolás Colón | malzogaray | — | 23.8 | 0 | 1016.98 | No | OBS |
| AD-55 | ADQUIRENCIA | Historia | Finalizada | 2025-11-03 | 2025-12-10 | Andrea ORSINI | malzogaray | — | 1.27 | 0 | 901.74 | No | — |
| AD-56 | ADQUIRENCIA | Historia | Finalizada | 2025-11-03 | 2025-12-01 | Andrea ORSINI | malzogaray | — | 264.25 | 0 | 412.98 | No | — |
| AD-62 | ADQUIRENCIA | Historia | Finalizada | 2025-11-03 | 2025-12-18 | Nicolás Colón | Pablo Antonio GOMES | 3 | 137.12 | 53.95 | 892.32 | Sí | — |
| AD-63 | ADQUIRENCIA | Historia | Finalizada | 2025-11-03 | 2025-12-12 | Nicolás Colón | Pablo Antonio GOMES | 3 | 41.92 | 0 | 892.43 | No | — |
| AD-64 | ADQUIRENCIA | Historia | Finalizada | 2025-11-03 | 2025-12-11 | Nicolás Colón | Pablo Antonio GOMES | 7 | 44.45 | 0 | 866.5 | No | — |
| OB-31 | ONBOARDING | Historia | Finalizada | 2025-11-03 | 2025-12-09 | Ana | malzogaray | — | 44.83 | 0 | 870.93 | No | OBS |
| AD-66 | ADQUIRENCIA | Historia | Finalizada | 2025-11-04 | 2025-11-06 | Unassigned | malzogaray | — | 0 | 52.75 | 0 | Sí | — |
| AD-67 | ADQUIRENCIA | Historia | Finalizada | 2025-11-04 | 2025-11-04 | Unassigned | malzogaray | 7 | 0 | 0 | 0.05 | No | — |
| AD-68 | ADQUIRENCIA | Error | Finalizada | 2025-11-04 | 2025-11-28 | Andrea ORSINI | malzogaray | — | 42.9 | 0 | 534.83 | No | OBS |
| AD-70 | ADQUIRENCIA | Historia | Finalizada | 2025-11-04 | 2026-02-18 | Ana | Pablo Antonio GOMES | 1 | 1065.14 | 0 | 1487.63 | No | — |
| AD-71 | ADQUIRENCIA | Historia | Bloqueado | 2025-11-04 | — | malzogaray | Pablo Antonio GOMES | 3 | 453.98 | 723.18 | 3732 | Sí | — |
| AD-535 | ADQUIRENCIA | Historia | Finalizada | 2025-11-05 | 2026-01-20 | Nicolás Colón | Pablo Antonio GOMES | 7 | 359.47 | 0 | 1461.39 | No | — |
| WS-56 | EMISIÓN | Historia | Finalizada | 2025-11-05 | 2025-12-02 | Nicolás Colón | Pablo Antonio GOMES | 1 | 137.12 | 0 | 508.83 | No | OBS |
| WS-58 | EMISIÓN | Historia | Finalizada | 2025-11-05 | 2026-02-20 | malzogaray | Luciana Rudaz | 7 | 163.6 | 0 | 2179.99 | No | — |
| AD-78 | ADQUIRENCIA | Historia | Finalizada | 2025-11-06 | 2025-12-17 | Nicolas Pico | malzogaray | — | 166.75 | 0 | 827.71 | No | — |
| AD-79 | ADQUIRENCIA | Historia | Finalizada | 2025-11-06 | 2025-12-01 | Bethania | malzogaray | — | 123.98 | 0 | 477.72 | No | — |
| AD-80 | ADQUIRENCIA | Historia | Finalizada | 2025-11-06 | 2025-12-04 | Bethania | malzogaray | 3 | 195.8 | 0 | 479.33 | No | — |
| AD-83 | ADQUIRENCIA | Historia | Finalizada | 2025-11-06 | 2025-11-06 | Unassigned | malzogaray | 15 | 0 | 0 | 0.05 | No | — |
| AD-85 | ADQUIRENCIA | Error | Finalizada | 2025-11-06 | 2025-12-09 | Bethania | malzogaray | — | 1.58 | 0 | 797.31 | No | OBS |
| AD-86 | ADQUIRENCIA | Error | Finalizada | 2025-11-06 | 2025-12-09 | Bethania | malzogaray | — | 90.42 | 0 | 697.57 | No | OBS |
| SER-13 | SERVICIOS | Historia | Finalizada | 2025-11-06 | 2026-02-12 | malzogaray | Pablo Antonio GOMES | — | 0 | 0 | 2372.85 | No | — |
| WS-59 | EMISIÓN | Historia | Finalizada | 2025-11-06 | 2026-02-13 | Nicolás Colón | Pablo Antonio GOMES | 7 | 0 | 0 | 1318.06 | No | — |
| WS-63 | EMISIÓN | Historia | Finalizada | 2025-11-06 | 2026-02-09 | Bethania | Luciana Rudaz | 3 | 74.3 | 0 | 2197.57 | No | — |
| WS-64 | EMISIÓN | Historia | Finalizada | 2025-11-06 | 2026-02-18 | Bethania | Luciana Rudaz | 3 | 119.97 | 0 | 2221.35 | No | — |
| WS-65 | EMISIÓN | Historia | Finalizada | 2025-11-06 | 2026-02-18 | Bethania | Luciana Rudaz | 3 | 120.1 | 0 | 2221.29 | No | — |
| WS-66 | EMISIÓN | Historia | Finalizada | 2025-11-07 | 2025-11-07 | Unassigned | malzogaray | 15 | 0 | 0 | 0 | No | — |
| WS-68 | EMISIÓN | Historia | Finalizada | 2025-11-07 | 2026-02-09 | Bethania | Luciana Rudaz | 3 | 78.18 | 0 | 2205.87 | No | — |
| AD-87 | ADQUIRENCIA | Error | Finalizada | 2025-11-10 | 2026-02-24 | Ana | malzogaray | 1 | 497.43 | 0 | 2059.26 | No | OBS |
| AD-89 | ADQUIRENCIA | Error | Finalizada | 2025-11-10 | 2026-06-11 | Ana | malzogaray | 3 | 2085.84 | 0 | 3037.11 | No | OBS |
| AD-93 | ADQUIRENCIA | Error | Finalizada | 2025-11-10 | 2025-12-04 | Bethania | malzogaray | — | 1.93 | 0 | 576.17 | No | OBS |
| AD-98 | ADQUIRENCIA | Historia | Finalizada | 2025-11-10 | 2025-12-18 | Ana | Pablo Antonio GOMES | 7 | 166.08 | 23.95 | 720.7 | Sí | — |
| AD-99 | ADQUIRENCIA | Historia | Finalizada | 2025-11-10 | 2026-01-26 | Ana | Pablo Antonio GOMES | 3 | 289.13 | 0 | 1554.63 | No | — |
| WS-70 | EMISIÓN | Error | Finalizada | 2025-11-10 | 2025-12-16 | Nicolás Colón | malzogaray | — | 267.25 | 0 | 605.03 | No | OBS |
| WS-71 | EMISIÓN | Historia | Finalizada | 2025-11-10 | 2026-02-09 | Bethania | Luciana Rudaz | 3 | 77.3 | 0 | 2133.39 | No | — |
| WS-72 | EMISIÓN | Historia | Finalizada | 2025-11-10 | 2026-02-09 | Bethania | Luciana Rudaz | 3 | 76.75 | 0 | 2109.29 | No | — |
| WS-73 | EMISIÓN | Historia | Finalizada | 2025-11-10 | 2026-02-09 | Bethania | Luciana Rudaz | 3 | 75.93 | 0 | 2133.37 | No | — |
| WS-74 | EMISIÓN | Historia | Finalizada | 2025-11-10 | 2026-02-09 | Bethania | Luciana Rudaz | 3 | 74.52 | 0 | 2108.57 | No | — |
| WS-75 | EMISIÓN | Error | Finalizada | 2025-11-10 | 2025-12-10 | Bethania | malzogaray | 3 | 19.02 | 0 | 696.95 | No | OBS |
| AD-106 | ADQUIRENCIA | Error | Finalizada | 2025-11-11 | 2025-11-11 | Nicolás Colón | Andrea ORSINI | — | 0 | 0 | 2.07 | No | OBS |
| WS-80 | EMISIÓN | Historia | Finalizada | 2025-11-11 | 2026-06-02 | Ana | Pablo Antonio GOMES | 7 | 261.12 | 0 | 4618.68 | No | — |
| WS-81 | EMISIÓN | Historia | Finalizada | 2025-11-11 | 2025-12-12 | Nicolas Pomponio | Pablo Antonio GOMES | 1 | 0 | 0 | 744.68 | No | — |
| WS-82 | EMISIÓN | Historia | Finalizada | 2025-11-11 | 2025-12-12 | Nicolas Pomponio | Pablo Antonio GOMES | 3 | 0 | 0 | 744.58 | No | — |
| WS-83 | EMISIÓN | Error | Finalizada | 2025-11-11 | 2025-11-11 | Nicolás Colón | Andrea ORSINI | — | 1.37 | 0 | 0.02 | No | — |
| AD-113 | ADQUIRENCIA | Error | Finalizada | 2025-11-12 | 2026-05-13 | Andrea ORSINI | Andrea ORSINI | 0.25 | 3.32 | 0 | 47.2 | No | OBS |
| AD-114 | ADQUIRENCIA | Error | Finalizada | 2025-11-12 | 2025-11-28 | Nicolás Colón | Andrea ORSINI | — | 40.42 | 0 | 343.07 | No | OBS |
| AD-115 | ADQUIRENCIA | Error | Finalizada | 2025-11-12 | 2026-01-23 | Ana | Andrea ORSINI | 1 | 489.38 | 0 | 1239.03 | No | OBS |
| AD-116 | ADQUIRENCIA | Error | Finalizada | 2025-11-12 | 2025-12-02 | Nicolás Colón | Andrea ORSINI | 3 | 141.18 | 0 | 337.87 | No | OBS |
| AD-118 | ADQUIRENCIA | Error | Finalizada | 2025-11-12 | 2025-12-17 | Nicolás Colón | Nicolás Colón | — | 247.67 | 0 | 596.33 | No | OBS |
| AD-119 | ADQUIRENCIA | Error | Finalizada | 2025-11-12 | 2025-12-16 | Nicolás Colón | Andrea ORSINI | 3 | 91.62 | 0 | 724.62 | No | OBS |
| AD-121 | ADQUIRENCIA | Error | Finalizada | 2025-11-12 | 2025-12-17 | Nicolás Colón | Andrea ORSINI | 7 | 364.17 | 0 | 479.37 | No | OBS |
| AD-123 | ADQUIRENCIA | Error | Finalizada | 2025-11-12 | 2025-12-10 | Andrea ORSINI | Andrea ORSINI | 3 | 1.2 | 0 | 675.02 | No | OBS |
| AD-124 | ADQUIRENCIA | Error | Finalizada | 2025-11-12 | 2026-01-21 | Bethania | Andrea ORSINI | 3 | 61.48 | 0 | 1598.29 | No | OBS |
| AD-125 | ADQUIRENCIA | Error | Finalizada | 2025-11-12 | 2025-12-16 | Andrea ORSINI | Andrea ORSINI | 3 | 140 | 0 | 677.17 | No | OBS |
| AD-126 | ADQUIRENCIA | Error | Finalizada | 2025-11-12 | 2025-12-11 | Ana | Andrea ORSINI | 3 | 116.02 | 0 | 579.12 | No | OBS |
| AD-127 | ADQUIRENCIA | Error | Finalizada | 2025-11-12 | 2025-12-18 | Nicolás Colón | Nicolás Colón | 3 | 250.53 | 0 | 617.17 | No | OBS |
| AD-136 | ADQUIRENCIA | Error | Finalizada | 2025-11-12 | 2025-12-01 | Bethania | Andrea ORSINI | — | 119.75 | 0 | 332.62 | No | OBS |
| WS-88 | EMISIÓN | Historia | Finalizada | 2025-11-12 | 2025-12-10 | Bethania | Bethania | 3 | 15.22 | 0 | 653.5 | No | OBS |
| WS-90 | EMISIÓN | Error | Finalizada | 2025-11-12 | 2025-11-28 | Ana | Andrea ORSINI | 3 | 306.65 | 27.98 | 37 | Sí | OBS |
| WS-91 | EMISIÓN | Error | Finalizada | 2025-11-12 | 2025-11-28 | Ana | Andrea ORSINI | 3 | 24.23 | 0 | 354.53 | No | OBS |
| AD-140 | ADQUIRENCIA | Error | Finalizada | 2025-11-13 | 2025-12-17 | Nicolás Colón | Nicolás Colón | 3 | 116.9 | 0 | 702.95 | No | OBS |
| AD-142 | ADQUIRENCIA | Error | Finalizada | 2025-11-13 | 2026-03-12 | Andrea ORSINI | Andrea ORSINI | 3 | 575.57 | 0 | 100.48 | No | OBS |
| AD-144 | ADQUIRENCIA | Error | Finalizada | 2025-11-13 | 2025-11-14 | Nicolas Pico | Andrea ORSINI | — | 18.88 | 0 | 1.85 | No | — |
| WS-94 | EMISIÓN | Error | Finalizada | 2025-11-14 | 2025-11-14 | Nicolás Colón | Andrea ORSINI | — | 2.72 | 0 | 0 | No | — |
| AD-151 | ADQUIRENCIA | Error | Finalizada | 2025-11-17 | 2025-11-28 | Andrea ORSINI | Andrea ORSINI | 1 | 171.78 | 0 | 94.53 | No | — |
| OB-1 | ONBOARDING | Error | Finalizada | 2025-11-17 | 2026-02-04 | malzogaray | Andrea ORSINI | — | 50.42 | 0 | 1848.22 | No | — |
| OB-4 | ONBOARDING | Error | Finalizada | 2025-11-17 | 2026-02-04 | malzogaray | Andrea ORSINI | — | 0.03 | 0 | 1898.37 | No | — |
| AD-153 | ADQUIRENCIA | Historia | Finalizada | 2025-11-18 | 2026-03-09 | malzogaray | Andrea ORSINI | 7 | 126.07 | 621.67 | 1916.02 | Sí | — |
| AD-155 | ADQUIRENCIA | Historia | Finalizada | 2025-11-18 | 2026-01-27 | Nicolás Colón | Andrea ORSINI | 3 | 147.12 | 0 | 5.03 | No | — |
| AD-159 | ADQUIRENCIA | Historia | Finalizada | 2025-11-18 | 2026-02-27 | Bethania | Andrea ORSINI | — | 310.47 | 1447.74 | 670.38 | Sí | — |
| WS-104 | EMISIÓN | Historia | Finalizada | 2025-11-18 | 2026-07-14 | malzogaray | malzogaray | 3 | 195.72 | 0 | 1798.57 | No | — |
| AD-166 | ADQUIRENCIA | Error | Finalizada | 2025-11-19 | 2025-11-21 | Nicolás Colón | Nicolás Colón | 3 | 0.53 | 0 | 47.85 | No | OBS |
| AD-169 | ADQUIRENCIA | Error | Finalizada | 2025-11-19 | 2025-11-21 | Bethania | Bethania | 1 | 0.82 | 0 | 49.07 | No | OBS |
| AD-170 | ADQUIRENCIA | Error | Finalizada | 2025-11-19 | 2025-11-26 | Nicolás Colón | Nicolás Colón | 1 | 0.18 | 0 | 169.1 | No | OBS |
| OB-7 | ONBOARDING | Error | Finalizada | 2025-11-19 | 2025-11-19 | Andrea ORSINI | Andrea ORSINI | — | 0.12 | 0 | 4.67 | No | — |
| OB-8 | ONBOARDING | Error | Finalizada | 2025-11-19 | 2025-12-01 | Bethania | Andrea ORSINI | — | 97.1 | 0 | 190.32 | No | — |
| OB-9 | ONBOARDING | Historia | Finalizada | 2025-11-19 | 2025-11-19 | Andrea ORSINI | Andrea ORSINI | — | 2.92 | 0 | 0.02 | No | — |
| WS-106 | EMISIÓN | Error | Finalizada | 2025-11-19 | 2025-11-27 | Ana | Ana | — | 166.85 | 0 | 23.08 | No | — |
| WS-107 | EMISIÓN | Error | Finalizada | 2025-11-19 | 2026-06-18 | Ana | Andrea ORSINI | 1 | 980.84 | 0 | 88.42 | No | — |
| OB-12 | ONBOARDING | Historia | Finalizada | 2025-11-20 | 2025-11-20 | Andrea ORSINI | Andrea ORSINI | — | 2.48 | 0 | 0 | No | — |
| WS-122 | EMISIÓN | Error | Finalizada | 2025-11-21 | 2025-11-25 | Ana | Ana | — | 1.45 | 0 | 96.9 | No | OBS |
| AD-182 | ADQUIRENCIA | Error | Finalizada | 2025-11-25 | 2025-12-03 | Andrea ORSINI | Andrea ORSINI | 7 | 197.82 | 0 | 0.02 | No | — |
| AD-183 | ADQUIRENCIA | Error | Finalizada | 2025-11-25 | 2026-01-13 | Bethania | Bethania | 1 | 261.25 | 0 | 914.33 | No | OBS |
| AD-184 | ADQUIRENCIA | Historia | Finalizada | 2025-11-25 | 2026-01-22 | Ana | Pablo Antonio GOMES | 7 | 45.13 | 0 | 1349.53 | No | — |
| AD-186 | ADQUIRENCIA | Error | Finalizada | 2025-11-25 | 2025-12-29 | Bethania | Bethania | 3 | 118.22 | 0 | 700.78 | No | OBS |
| AD-193 | ADQUIRENCIA | Error | Finalizada | 2025-11-25 | 2026-01-09 | Nicolás Colón | Nicolás Colón | 3 | 333.87 | 0 | 738.85 | No | OBS |
| AD-194 | ADQUIRENCIA | Error | Finalizada | 2025-11-25 | 2025-12-18 | Nicolás Colón | Nicolás Colón | 1 | 205.45 | 0 | 342.25 | No | OBS |
| OB-30 | ONBOARDING | Error | Finalizada | 2025-11-25 | 2025-12-02 | Andrea ORSINI | Andrea ORSINI | — | 168.2 | 0 | 0.05 | No | — |
| WS-129 | EMISIÓN | Historia | Finalizada | 2025-11-25 | 2026-01-09 | Bethania | malzogaray | 0.25 | 49.58 | 0 | 1049.26 | No | — |
| AD-195 | ADQUIRENCIA | Error | Finalizada | 2025-11-26 | 2026-01-06 | Nicolas Pico | Nicolás Colón | 3 | 92.25 | 0 | 902.28 | No | OBS |
| WS-135 | EMISIÓN | Error | Finalizada | 2025-11-26 | 2025-12-22 | Ana | Ana | — | 0 | 0 | 629.1 | No | — |
| WS-136 | EMISIÓN | Error | Finalizada | 2025-11-26 | 2026-01-26 | Ana | Ana | — | 929.41 | 0 | 543.5 | No | — |
| WS-137 | EMISIÓN | Error | Finalizada | 2025-11-26 | 2026-01-02 | Ana | Ana | — | 0 | 0 | 886.7 | No | — |
| WS-139 | EMISIÓN | Error | Finalizada | 2025-11-26 | 2025-12-01 | Andrea ORSINI | Andrea ORSINI | — | 0 | 0 | 121.13 | No | OBS |
| WS-141 | EMISIÓN | Error | Finalizada | 2025-11-26 | 2026-01-12 | Andrea ORSINI | Andrea ORSINI | — | 0 | 0 | 1140.68 | No | OBS |
| WS-145 | EMISIÓN | Error | Finalizada | 2025-11-26 | 2026-03-12 | Andrea ORSINI | Andrea ORSINI | — | 169.35 | 0 | 2377.55 | No | OBS |
| WS-147 | EMISIÓN | Error | Finalizada | 2025-11-26 | 2025-12-22 | Ana | Ana | — | 161.17 | 0 | 456.85 | No | — |
| AD-202 | ADQUIRENCIA | Error | Finalizada | 2025-11-27 | 2025-12-02 | Ana | Andrea ORSINI | — | 117.53 | 0 | 0.02 | No | — |
| AD-210 | ADQUIRENCIA | Error | Finalizada | 2025-11-27 | 2025-12-01 | Andrea ORSINI | Andrea ORSINI | 3 | 0.53 | 0 | 89.6 | No | OBS |
| AD-211 | ADQUIRENCIA | Historia | Finalizada | 2025-11-28 | 2025-11-28 | Nicolas Pico | Pablo Antonio GOMES | 3 | 0 | 0 | 0.02 | No | — |
| WS-154 | EMISIÓN | Error | Finalizada | 2025-11-28 | 2025-12-01 | Ana | Ana | 1 | 0 | 0 | 83.87 | No | — |
| AD-213 | ADQUIRENCIA | Historia | Finalizada | 2025-12-01 | 2026-01-28 | Ana | Pablo Antonio GOMES | 3 | 169.98 | 157.53 | 1064.03 | Sí | — |
| AD-219 | ADQUIRENCIA | Historia | Finalizada | 2025-12-01 | 2026-05-13 | Andrea ORSINI | Pablo Antonio GOMES | 7 | 1818.7 | 0 | 1605.94 | No | — |
| AD-220 | ADQUIRENCIA | Historia | Finalizada | 2025-12-01 | 2026-03-03 | Bethania | Pablo Antonio GOMES | 7 | 780.04 | 431.72 | 1020.34 | Sí | — |
| AD-225 | ADQUIRENCIA | Historia | Finalizada | 2025-12-01 | 2026-01-16 | Andrea ORSINI | Pablo Antonio GOMES | 3 | 264.27 | 0 | 838.78 | No | — |
| AD-226 | ADQUIRENCIA | Historia | Finalizada | 2025-12-01 | 2026-04-01 | Andrea ORSINI | Pablo Antonio GOMES | 3 | 455.6 | 0 | 2467.42 | No | — |
| AD-229 | ADQUIRENCIA | Historia | Finalizada | 2025-12-01 | 2026-03-19 | Andrea ORSINI | Pablo Antonio GOMES | 3 | 222.3 | 1204.39 | 1177.85 | Sí | — |
| AD-233 | ADQUIRENCIA | Historia | Finalizada | 2025-12-01 | 2026-01-19 | Nicolás Colón | Pablo Antonio GOMES | 7 | 198.2 | 146.25 | 838.87 | Sí | — |
| AD-236 | ADQUIRENCIA | Error | Finalizada | 2025-12-01 | 2026-01-21 | Bethania | Bethania | 3 | 123.77 | 0 | 761.57 | No | OBS |
| WS-159 | EMISIÓN | Historia | Finalizada | 2025-12-01 | 2026-03-17 | Bethania | Luciana Rudaz | 15 | 438.62 | 0 | 2108.68 | No | — |
| AD-240 | ADQUIRENCIA | Error | Finalizada | 2025-12-02 | 2025-12-04 | Nicolás Colón | Nicolás Colón | 3 | 0.1 | 0 | 50.67 | No | OBS |
| AD-242 | ADQUIRENCIA | Error | Finalizada | 2025-12-02 | 2025-12-23 | Nicolás Colón | Andrea ORSINI | — | 451.02 | 0 | 50.95 | No | — |
| AD-243 | ADQUIRENCIA | Error | Finalizada | 2025-12-02 | 2025-12-04 | Nicolás Colón | Nicolás Colón | 3 | 19.45 | 0 | 26.05 | No | OBS |
| AD-244 | ADQUIRENCIA | Error | Finalizada | 2025-12-02 | 2025-12-10 | Nicolás Colón | Andrea ORSINI | 3 | 115.53 | 0 | 71.42 | No | — |
| AD-245 | ADQUIRENCIA | Error | Finalizada | 2025-12-02 | 2026-01-28 | Nicolás Colón | Nicolás Colón | 3 | 323.22 | 0 | 1049.46 | No | OBS |
| WS-160 | EMISIÓN | Error | Finalizada | 2025-12-02 | 2025-12-04 | Nicolás Colón | Nicolás Colón | 1 | 0 | 0 | 46.4 | No | OBS |
| WS-164 | EMISIÓN | Error | Finalizada | 2025-12-02 | 2026-01-07 | Bethania | Bethania | 3 | 41.58 | 0 | 819.08 | No | OBS |
| AD-248 | ADQUIRENCIA | Error | Finalizada | 2025-12-03 | 2025-12-16 | Ana | Ana | 3 | 217.3 | 0 | 92.48 | No | — |
| AD-250 | ADQUIRENCIA | Error | Finalizada | 2025-12-03 | 2025-12-03 | Nicolás Colón | Andrea ORSINI | — | 0.35 | 0 | 0 | No | — |
| AD-253 | ADQUIRENCIA | Error | Finalizada | 2025-12-03 | 2025-12-03 | Andrea ORSINI | Andrea ORSINI | 3 | 0 | 0 | 0.13 | No | — |
| WS-167 | EMISIÓN | Error | Finalizada | 2025-12-03 | 2025-12-17 | Ana | Ana | — | 39.22 | 0 | 294.37 | No | — |
| WS-168 | EMISIÓN | Error | Finalizada | 2025-12-03 | 2025-12-09 | Nicolás Colón | Nicolás Colón | — | 0 | 0 | 146.27 | No | OBS |
| WS-169 | EMISIÓN | Error | Finalizada | 2025-12-03 | 2025-12-11 | Ana | malzogaray | — | 183.73 | 0 | 0 | No | — |
| AD-257 | ADQUIRENCIA | Error | Finalizada | 2025-12-04 | 2025-12-15 | Nicolás Colón | Nicolás Colón | — | 0.02 | 0 | 262.43 | No | OBS |
| SER-15 | SERVICIOS | Historia | Finalizada | 2025-12-04 | 2026-02-23 | Nicolás Colón | Pablo Antonio GOMES | — | 1579.99 | 0 | 354.68 | No | — |
| SER-16 | SERVICIOS | Historia | Finalizada | 2025-12-04 | 2026-02-23 | Nicolás Colón | Pablo Antonio GOMES | — | 1579.99 | 0 | 354.67 | No | — |
| SER-17 | SERVICIOS | Historia | Finalizada | 2025-12-04 | 2026-02-18 | Nicolás Colón | Pablo Antonio GOMES | — | 1460.79 | 0 | 354.67 | No | — |
| WS-172 | EMISIÓN | Historia | Finalizada | 2025-12-04 | 2026-02-04 | Andrea ORSINI | Pablo Antonio GOMES | 3 | 363.32 | 0 | 1143.91 | No | — |
| AD-259 | ADQUIRENCIA | Error | Finalizada | 2025-12-05 | 2025-12-16 | Nicolás Colón | Nicolás Colón | 1 | 24.8 | 0 | 234.58 | No | OBS |
| WS-181 | EMISIÓN | Historia | EN QA | 2025-12-05 | — | Ana | Nicolás Colón | 7 | 1805.74 | 668.28 | 3102.03 | Sí | OBS |
| WS-186 | EMISIÓN | Error | Finalizada | 2025-12-05 | 2025-12-11 | Nicolás Colón | Nicolás Colón | — | 0.18 | 0 | 145.35 | No | OBS |
| AD-261 | ADQUIRENCIA | Historia | Finalizada | 2025-12-09 | 2026-01-14 | Andrea ORSINI | Pablo Antonio GOMES | 3 | 294.23 | 0 | 576.92 | No | — |
| AD-262 | ADQUIRENCIA | Historia | Finalizada | 2025-12-09 | 2026-01-16 | Nicolás Colón | Pablo Antonio GOMES | 3 | 99.42 | 0 | 818.15 | No | — |
| AD-263 | ADQUIRENCIA | Historia | Finalizada | 2025-12-09 | 2026-03-27 | Ana | Pablo Antonio GOMES | 3 | 695.37 | 174.53 | 1728.68 | Sí | — |
| AD-264 | ADQUIRENCIA | Error | Finalizada | 2025-12-09 | 2026-01-19 | Nicolás Colón | Pablo Antonio GOMES | 7 | 337.65 | 20.92 | 632.05 | Sí | OBS |
| AD-265 | ADQUIRENCIA | Historia | Finalizada | 2025-12-09 | 2025-12-16 | Bethania | malzogaray | 3 | 140.77 | 1.5 | 25.55 | Sí | — |
| AD-266 | ADQUIRENCIA | Historia | Finalizada | 2025-12-09 | 2025-12-16 | Ana | malzogaray | — | 143.6 | 0 | 25.55 | No | OBS |
| AD-268 | ADQUIRENCIA | Historia | Finalizada | 2025-12-09 | 2025-12-16 | Bethania | malzogaray | 3 | 41.7 | 96.62 | 25.57 | Sí | — |
| AD-269 | ADQUIRENCIA | Historia | Finalizada | 2025-12-09 | 2025-12-17 | Andrea ORSINI | malzogaray | 3 | 95.67 | 48.68 | 47.72 | Sí | OBS |
| AD-270 | ADQUIRENCIA | Error | Finalizada | 2025-12-09 | 2025-12-18 | Nicolás Colón | malzogaray | 3 | 165.08 | 0 | 45.57 | No | — |
| OB-39 | ONBOARDING | Error | Finalizada | 2025-12-09 | 2025-12-11 | Andrea ORSINI | Andrea ORSINI | — | 45.25 | 0 | 0 | No | — |
| WS-194 | EMISIÓN | Error | Finalizada | 2025-12-09 | 2025-12-22 | Ana | Ana | 3 | 242.83 | 0 | 72.57 | No | — |
| WS-195 | EMISIÓN | Historia | Finalizada | 2025-12-09 | 2025-12-15 | Nicolás Colón | Pablo Antonio GOMES | 1 | 0 | 0 | 148.82 | No | — |
| WS-196 | EMISIÓN | Historia | Finalizada | 2025-12-09 | 2025-12-12 | Nicolás Colón | Pablo Antonio GOMES | — | 40.92 | 0 | 30.1 | No | — |
| AD-271 | ADQUIRENCIA | Error | Finalizada | 2025-12-10 | 2025-12-15 | Andrea ORSINI | Andrea ORSINI | — | 65.18 | 0 | 54.88 | No | OBS |
| AD-272 | ADQUIRENCIA | Error | Finalizada | 2025-12-10 | 2025-12-16 | Andrea ORSINI | Andrea ORSINI | 3 | 0.03 | 0 | 143.73 | No | OBS |
| AD-275 | ADQUIRENCIA | Error | Finalizada | 2025-12-10 | 2026-01-14 | Nicolás Colón | Nicolás Colón | 1 | 0.33 | 0 | 846.06 | No | OBS |
| AD-276 | ADQUIRENCIA | Error | Finalizada | 2025-12-10 | 2026-02-06 | Nicolás Colón | Nicolás Colón | 3 | 89.3 | 0 | 1301.27 | No | OBS |
| WS-204 | EMISIÓN | Historia | Finalizada | 2025-12-10 | 2026-01-23 | Ana | Pablo Antonio GOMES | 3 | 768.69 | 0 | 288 | No | — |
| WS-207 | EMISIÓN | Error | Finalizada | 2025-12-10 | 2026-01-12 | Andrea ORSINI | Andrea ORSINI | — | 0 | 0 | 808.54 | No | OBS |
| WS-208 | EMISIÓN | Error | Finalizada | 2025-12-10 | 2025-12-11 | Nicolás Colón | Nicolás Colón | 1 | 0.33 | 0 | 24.85 | No | OBS |
| AD-287 | ADQUIRENCIA | Error | Finalizada | 2025-12-11 | 2025-12-12 | Nicolás Colón | Nicolás Colón | — | 0.23 | 0 | 21.85 | No | OBS |
| AD-288 | ADQUIRENCIA | Error | Finalizada | 2025-12-11 | 2025-12-12 | Nicolás Colón | Nicolás Colón | — | 1.08 | 0 | 20.67 | No | OBS |
| AD-290 | ADQUIRENCIA | Historia | Finalizada | 2025-12-11 | 2026-01-21 | Ana | Pablo Antonio GOMES | 3 | 9.88 | 0 | 978.23 | No | — |
| AD-291 | ADQUIRENCIA | Historia | Finalizada | 2025-12-11 | 2026-01-23 | Andrea ORSINI | Pablo Antonio GOMES | 1 | 25.38 | 68.47 | 934.57 | Sí | — |
| SER-18 | SERVICIOS | Historia | Finalizada | 2025-12-11 | 2026-02-23 | Nicolás Colón | Pablo Antonio GOMES | — | 1579.99 | 0 | 188.48 | No | — |
| WS-211 | EMISIÓN | Historia | Finalizada | 2025-12-11 | 2026-03-12 | Andrea ORSINI | Pablo Antonio GOMES | 7 | 1254.69 | 0 | 942.32 | No | — |
| WS-212 | EMISIÓN | Historia | Finalizada | 2025-12-11 | 2026-01-26 | Andrea ORSINI | Pablo Antonio GOMES | 3 | 162.55 | 0.02 | 942.27 | Sí | — |
| WS-216 | EMISIÓN | Historia | Finalizada | 2025-12-11 | 2026-02-23 | Andrea ORSINI | Pablo Antonio GOMES | 1 | 847.88 | 0 | 949.08 | No | — |
| WS-219 | EMISIÓN | Historia | Finalizada | 2025-12-11 | 2026-03-06 | Bethania | Luciana Rudaz | 3 | 216.42 | 0 | 1826.59 | No | — |
| AD-293 | ADQUIRENCIA | Error | Finalizada | 2025-12-12 | 2025-12-16 | Ana | Andrea ORSINI | 3 | 0.02 | 0 | 96.12 | No | OBS |
| AD-298 | ADQUIRENCIA | Historia | Finalizada | 2025-12-12 | 2026-01-06 | Nicolás Colón | Nicolás Colón | 1 | 22.62 | 0 | 576.97 | No | OBS |
| AD-316 | ADQUIRENCIA | Error | Finalizada | 2025-12-12 | 2025-12-18 | Nicolás Colón | Nicolás Colón | 1 | 39.32 | 0 | 100.53 | No | OBS |
| AD-319 | ADQUIRENCIA | Error | Finalizada | 2025-12-12 | 2025-12-15 | Nicolás Colón | Nicolás Colón | 3 | 0.15 | 0 | 69.52 | No | OBS |
| WS-223 | EMISIÓN | Error | Finalizada | 2025-12-12 | 2026-01-22 | Ana | Ana | — | 0 | 0 | 346.53 | No | — |
| WS-232 | EMISIÓN | Historia | Finalizada | 2025-12-12 | 2026-03-03 | malzogaray | Pablo Antonio GOMES | 1 | 1045.73 | 0 | 430.57 | No | — |
| WS-233 | EMISIÓN | Historia | Finalizada | 2025-12-12 | 2026-03-10 | Ana | Pablo Antonio GOMES | 1 | 1218.91 | 0 | 430.47 | No | — |
| WS-238 | EMISIÓN | Error | Finalizada | 2025-12-14 | 2026-02-18 | Ana | Ana | 0.5 | 196.85 | 0 | 933.05 | No | — |
| WS-241 | EMISIÓN | Error | Finalizada | 2025-12-14 | 2026-01-21 | Bethania | Ana | 1 | 5.77 | 0 | 898.55 | No | — |
| WS-242 | EMISIÓN | Error | Finalizada | 2025-12-14 | 2026-01-22 | Bethania | Ana | 0.5 | 7.57 | 0 | 898.08 | No | — |
| WS-243 | EMISIÓN | Error | Finalizada | 2025-12-14 | 2026-01-22 | Bethania | Ana | 0.5 | 8.58 | 0 | 897.92 | No | — |
| WS-244 | EMISIÓN | Error | Finalizada | 2025-12-14 | 2026-01-22 | Bethania | Ana | 0.5 | 8.12 | 0 | 897.77 | No | — |
| WS-245 | EMISIÓN | Error | Finalizada | 2025-12-14 | 2026-01-23 | Bethania | Ana | 0.5 | 51.1 | 0 | 897.62 | No | — |
| AD-333 | ADQUIRENCIA | Error | Finalizada | 2025-12-15 | 2026-03-12 | Andrea ORSINI | Andrea ORSINI | 1 | 168.15 | 0 | 1917.08 | No | — |
| AD-340 | ADQUIRENCIA | Historia | Finalizada | 2025-12-15 | 2026-03-12 | Ana | Pablo Antonio GOMES | 3 | 0.7 | 0 | 2096.06 | No | — |
| WS-247 | EMISIÓN | Error | Finalizada | 2025-12-15 | 2026-02-18 | Ana | Ana | 1 | 196.8 | 0 | 1382.54 | No | — |
| WS-248 | EMISIÓN | Error | Finalizada | 2025-12-15 | 2026-01-22 | Ana | Ana | — | 0 | 0 | 559.7 | No | — |
| WS-251 | EMISIÓN | Error | Finalizada | 2025-12-15 | 2026-01-22 | Ana | Ana | 1 | 0 | 0 | 553.13 | No | — |
| AD-345 | ADQUIRENCIA | Error | Finalizada | 2025-12-16 | 2026-01-06 | Nicolás Colón | Nicolás Colón | 1 | 167.37 | 0 | 340.03 | No | OBS |
| AD-346 | ADQUIRENCIA | Error | Finalizada | 2025-12-16 | 2026-01-06 | Nicolás Colón | Nicolás Colón | 1 | 165.37 | 0 | 339.53 | No | OBS |
| AD-350 | ADQUIRENCIA | Error | Finalizada | 2025-12-16 | 2026-01-07 | Bethania | Bethania | 3 | 4.02 | 0 | 525.47 | No | OBS |
| WS-252 | EMISIÓN | Historia | Finalizada | 2025-12-16 | 2026-02-18 | Ana | Pablo Antonio GOMES | 1 | 383.6 | 0 | 1170.04 | No | — |
| WS-257 | EMISIÓN | Historia | Finalizada | 2025-12-16 | 2025-12-16 | Andrea ORSINI | Andrea ORSINI | — | 0 | 0 | 1.8 | No | — |
| WS-259 | EMISIÓN | Error | Finalizada | 2025-12-16 | 2026-02-24 | Bethania | Nicolás Colón | 1 | 216.58 | 92.75 | 1375.09 | Sí | OBS |
| AD-357 | ADQUIRENCIA | Error | Finalizada | 2025-12-17 | 2025-12-18 | Nicolás Colón | Nicolás Colón | 1 | 3.4 | 0 | 24.88 | No | OBS |
| AD-358 | ADQUIRENCIA | Error | Finalizada | 2025-12-17 | 2025-12-18 | Ana | Ana | 3 | 20.93 | 0 | 2.78 | No | — |
| AD-361 | ADQUIRENCIA | Error | Finalizada | 2025-12-17 | 2025-12-18 | Ana | Ana | 3 | 1.4 | 0 | 22.02 | No | — |
| AD-362 | ADQUIRENCIA | Error | Finalizada | 2025-12-17 | 2025-12-18 | Ana | Ana | — | 4.75 | 0 | 18.73 | No | — |
| WS-263 | EMISIÓN | Error | Finalizada | 2025-12-17 | 2025-12-17 | Nicolás Colón | Andrea ORSINI | 1 | 0 | 0 | 0.83 | No | — |
| WS-264 | EMISIÓN | Historia | Finalizada | 2025-12-17 | 2026-01-26 | Andrea ORSINI | malzogaray | 3 | 173.78 | 0 | 786.68 | No | — |
| AD-372 | ADQUIRENCIA | Historia | Finalizada | 2025-12-18 | 2026-01-09 | Andrea ORSINI | Pablo Antonio GOMES | 3 | 220.52 | 0 | 310.95 | No | — |
| AD-375 | ADQUIRENCIA | Historia | Finalizada | 2025-12-18 | 2026-01-16 | Nicolas Pico | Pablo Antonio GOMES | 3 | 0 | 0 | 696.5 | No | — |
| AD-378 | ADQUIRENCIA | Historia | Finalizada | 2025-12-18 | 2026-03-20 | Andrea ORSINI | Pablo Antonio GOMES | 3 | 24.02 | 0 | 2198.86 | No | — |
| AD-379 | ADQUIRENCIA | Error | Finalizada | 2025-12-18 | 2026-02-27 | Andrea ORSINI | Andrea ORSINI | 1 | 286.55 | 334.57 | 1091.78 | Sí | DEF/OBS |
| AD-381 | ADQUIRENCIA | Historia | Finalizada | 2025-12-18 | 2026-03-30 | Andrea ORSINI | Pablo Antonio GOMES | 3 | 100.38 | 24.03 | 2333.53 | Sí | — |
| AD-388 | ADQUIRENCIA | Error | Finalizada | 2025-12-18 | 2026-01-06 | Nicolás Colón | Nicolás Colón | — | 165.07 | 0 | 1.55 | No | OBS |
| AD-389 | ADQUIRENCIA | Error | Finalizada | 2025-12-18 | 2026-01-06 | Nicolás Colón | Nicolás Colón | 3 | 18.03 | 0 | 429.9 | No | OBS |
| WS-268 | EMISIÓN | Error | Finalizada | 2025-12-18 | 2026-01-16 | Ana | Ana | 1 | 22.53 | 0 | 675.43 | No | — |
| WS-269 | EMISIÓN | Error | Finalizada | 2025-12-18 | 2025-12-22 | Ana | Ana | 1 | 1.02 | 0 | 100.1 | No | — |
| WS-270 | EMISIÓN | Historia | Finalizada | 2025-12-18 | 2025-12-30 | Ana | Pablo Antonio GOMES | 3 | 74.08 | 0 | 280.53 | No | — |
| WS-272 | EMISIÓN | Historia | Finalizada | 2025-12-18 | 2025-12-29 | Nicolás Colón | Pablo Antonio GOMES | 3 | 120.83 | 3.6 | 134.23 | Sí | — |
| WS-273 | EMISIÓN | Historia | Finalizada | 2025-12-18 | 2026-01-26 | Nicolás Colón | Pablo Antonio GOMES | 7 | 165.5 | 0 | 765.17 | No | — |
| AD-392 | ADQUIRENCIA | Error | Finalizada | 2025-12-19 | 2026-01-20 | Bethania | Bethania | 3 | 469.13 | 0.2 | 297.52 | Sí | OBS |
| AD-393 | ADQUIRENCIA | Historia | Finalizada | 2025-12-19 | 2026-03-19 | Andrea ORSINI | Pablo Antonio GOMES | 7 | 50.68 | 0 | 2123.34 | No | — |
| AD-394 | ADQUIRENCIA | Error | Finalizada | 2025-12-19 | 2026-01-14 | Bethania | Bethania | 3 | 164.07 | 0 | 267.77 | No | OBS |
| WS-274 | EMISIÓN | Historia | Finalizada | 2025-12-19 | 2026-03-17 | Andrea ORSINI | Pablo Antonio GOMES | 3 | 431.53 | 0 | 1704.8 | No | — |
| AD-395 | ADQUIRENCIA | Historia | Finalizada | 2025-12-22 | 2026-02-11 | Bethania | Andrea ORSINI | 7 | 211.42 | 877.89 | 147.1 | Sí | — |
| AD-403 | ADQUIRENCIA | Error | Finalizada | 2025-12-22 | 2026-01-07 | Nicolás Colón | Nicolás Colón | 3 | 141.63 | 0 | 217.38 | No | OBS |
| AD-404 | ADQUIRENCIA | Historia | Finalizada | 2025-12-22 | 2026-01-28 | Ana | malzogaray | 3 | 22.03 | 0 | 879.56 | No | — |
| AD-409 | ADQUIRENCIA | Error | Finalizada | 2025-12-22 | 2026-01-16 | Ana | Ana | 1 | 409.65 | 0 | 188.6 | No | — |
| SER-19 | SERVICIOS | Error | Finalizada | 2025-12-22 | 2026-01-06 | Nicolás Colón | Nicolás Colón | — | 19.72 | 0 | 333.38 | No | OBS |
| WS-275 | EMISIÓN | Historia | Finalizada | 2025-12-22 | 2026-02-13 | malzogaray | malzogaray | 3 | 184.5 | 0 | 1073.14 | No | — |
| WS-276 | EMISIÓN | Historia | Finalizada | 2025-12-22 | 2026-02-04 | Bethania | malzogaray | 3 | 168.17 | 0 | 898.84 | No | — |
| WS-277 | EMISIÓN | Historia | Finalizada | 2025-12-22 | 2026-02-04 | Bethania | malzogaray | 3 | 168.15 | 0 | 898.78 | No | — |
| WS-278 | EMISIÓN | Historia | Finalizada | 2025-12-22 | 2026-02-04 | Bethania | malzogaray | 1 | 502 | 0 | 554.35 | No | — |
| WS-279 | EMISIÓN | Historia | Finalizada | 2025-12-22 | 2026-01-15 | Andrea ORSINI | malzogaray | 7 | 579.55 | 0 | 0 | No | — |
| WS-280 | EMISIÓN | Historia | Finalizada | 2025-12-22 | 2026-01-21 | Andrea ORSINI | malzogaray | 7 | 379.4 | 0 | 339.5 | No | — |
| WS-281 | EMISIÓN | Historia | Finalizada | 2025-12-22 | 2026-02-06 | Andrea ORSINI | malzogaray | 1 | 264.58 | 0 | 844.4 | No | — |
| WS-284 | EMISIÓN | Historia | Finalizada | 2025-12-22 | 2026-02-24 | Andrea ORSINI | Pablo Antonio GOMES | 3 | 332.65 | 0 | 1210.46 | No | — |
| AD-414 | ADQUIRENCIA | Historia | Finalizada | 2025-12-23 | 2026-03-12 | Andrea ORSINI | malzogaray | 3 | 355.13 | 0 | 1224.05 | No | — |
| AD-417 | ADQUIRENCIA | Error | Finalizada | 2025-12-23 | 2026-02-19 | Bethania | malzogaray | 7 | 651.2 | 0 | 749.44 | No | — |
| AD-421 | ADQUIRENCIA | Historia | Finalizada | 2025-12-23 | 2026-05-27 | Bethania | malzogaray | 1 | 185.63 | 0 | 3546.42 | No | — |
| AD-422 | ADQUIRENCIA | Historia | Finalizada | 2025-12-23 | 2026-03-09 | Andrea ORSINI | malzogaray | 3 | 624.32 | 0 | 1205.19 | No | — |
| AD-424 | ADQUIRENCIA | Error | Finalizada | 2025-12-23 | 2026-01-06 | Nicolás Colón | Nicolás Colón | 1 | 91.48 | 0 | 238.28 | No | OBS |
| SER-20 | SERVICIOS | Error | Finalizada | 2025-12-23 | 2026-01-13 | Nicolás Colón | Nicolás Colón | — | 38.6 | 0 | 466.68 | No | OBS |
| SER-21 | SERVICIOS | Historia | Finalizada | 2025-12-23 | 2026-01-06 | Unassigned | Nicolás Colón | — | 18.3 | 0 | 317.03 | No | — |
| SER-22 | SERVICIOS | Historia | Finalizada | 2025-12-23 | 2026-01-13 | Juan Pablo Carubelli | Nicolás Colón | — | 17.23 | 0 | 484.18 | No | — |
| SER-23 | SERVICIOS | Historia | Finalizada | 2025-12-23 | 2026-01-13 | Nicolás Colón | Nicolás Colón | — | 37.15 | 0 | 462.42 | No | OBS |
| SER-25 | SERVICIOS | Error | Finalizada | 2025-12-23 | 2026-01-06 | Nicolás Colón | Nicolás Colón | — | 17.37 | 0 | 311.95 | No | OBS |
| SER-27 | SERVICIOS | Error | Finalizada | 2025-12-23 | 2026-01-06 | Nicolás Colón | Nicolás Colón | — | 17.45 | 0 | 310.97 | No | OBS |
| WS-292 | EMISIÓN | Historia | Finalizada | 2025-12-23 | 2026-03-17 | Bethania | Luciana Rudaz | 15 | 438.4 | 0 | 1581.85 | No | — |
| AD-425 | ADQUIRENCIA | Historia | Finalizada | 2025-12-24 | 2026-04-29 | Andrea ORSINI | malzogaray | 3 | 207.82 | 0 | 2821.35 | No | — |
| WS-295 | EMISIÓN | Error | Finalizada | 2025-12-24 | 2026-01-16 | Ana | Ana | 1 | 23.6 | 0 | 531.85 | No | — |
| WS-296 | EMISIÓN | Error | Finalizada | 2025-12-24 | 2026-01-26 | Ana | Andrea ORSINI | 1 | 153.67 | 0 | 644.4 | No | — |
| WS-297 | EMISIÓN | Error | Finalizada | 2025-12-26 | 2026-01-14 | Ana | Pablo Antonio GOMES | 0.5 | 73.3 | 288.08 | 93.78 | Sí | — |
| WS-300 | EMISIÓN | Error | Finalizada | 2025-12-26 | 2025-12-29 | Nicolás Colón | Nicolás Colón | 0.5 | 69.37 | 0 | 69.35 | No | OBS |
| AD-426 | ADQUIRENCIA | Error | Finalizada | 2025-12-29 | 2026-01-09 | Andrea ORSINI | Andrea ORSINI | 3 | 156.7 | 0 | 109.18 | No | OBS |
| AD-427 | ADQUIRENCIA | Historia | Finalizada | 2025-12-29 | 2026-01-27 | Ana | Pablo Antonio GOMES | 1 | 502.15 | 0 | 198.48 | No | — |
| AD-428 | ADQUIRENCIA | Error | Finalizada | 2025-12-29 | 2026-01-07 | Nicolás Colón | Nicolás Colón | 1 | 20.27 | 0 | 171.05 | No | OBS |
| AD-429 | ADQUIRENCIA | Historia | Finalizada | 2025-12-29 | 2026-05-27 | Andrea ORSINI | malzogaray | 7 | 260.87 | 1450.34 | 1882.16 | Sí | — |
| AD-431 | ADQUIRENCIA | Historia | Bloqueado | 2025-12-29 | — | Bethania | Pablo Antonio GOMES | 7 | 48.37 | 0 | 4207.38 | No | — |
| AD-432 | ADQUIRENCIA | Historia | Bloqueado | 2025-12-29 | — | Bethania | Pablo Antonio GOMES | 7 | 5.43 | 0 | 4146.21 | No | — |
| WS-301 | EMISIÓN | Error | Finalizada | 2025-12-29 | 2026-01-26 | Ana | Ana | 1 | 67.6 | 229.9 | 372.82 | Sí | — |
| WS-303 | EMISIÓN | Historia | Finalizada | 2025-12-29 | 2026-01-26 | Nicolás Colón | malzogaray | 3 | 168.5 | 0 | 504.93 | No | — |
| WS-306 | EMISIÓN | Error | Finalizada | 2025-12-29 | 2026-01-23 | Nicolás Colón | Nicolás Colón | 3 | 5.87 | 0 | 586.12 | No | OBS |
| WS-307 | EMISIÓN | Error | Finalizada | 2025-12-30 | 2026-01-16 | Ana | Ana | 0.5 | 258.83 | 0 | 146.5 | No | — |
| AD-437 | ADQUIRENCIA | Error | Finalizada | 2026-01-02 | 2026-01-09 | Andrea ORSINI | Andrea ORSINI | 1 | 0 | 0 | 171.37 | No | DEF/OBS |
| WS-313 | EMISIÓN | Historia | Finalizada | 2026-01-02 | 2026-02-20 | Bethania | malzogaray | 3 | 22.37 | 0 | 1165.68 | No | — |
| WS-316 | EMISIÓN | Historia | Finalizada | 2026-01-02 | 2026-01-27 | Bethania | malzogaray | 2 | 186.63 | 0 | 410.8 | No | — |
| OB-46 | ONBOARDING | Historia | Finalizada | 2026-01-04 | 2026-02-24 | Luciana Rudaz | Luciana Rudaz | — | 0 | 0 | 1231.21 | No | — |
| OB-48 | ONBOARDING | Error | Finalizada | 2026-01-05 | 2026-01-07 | Andrea ORSINI | Andrea ORSINI | — | 0.02 | 0 | 47.65 | No | — |
| SER-28 | SERVICIOS | Error | Finalizada | 2026-01-05 | 2026-01-13 | Nicolás Colón | Nicolás Colón | — | 17.02 | 0 | 169.73 | No | OBS |
| SER-30 | SERVICIOS | Historia | Finalizada | 2026-01-05 | 2026-02-13 | Nicolás Colón | Nicolás Colón | — | 779.01 | 0 | 166.72 | No | — |
| SER-31 | SERVICIOS | Historia | Finalizada | 2026-01-05 | 2026-01-15 | Nicolás Colón | Nicolás Colón | — | 71.23 | 0 | 166.25 | No | — |
| WS-318 | EMISIÓN | Historia | Finalizada | 2026-01-05 | 2026-05-18 | Bethania | Luciana Rudaz | 15 | 129.05 | 0 | 3076.13 | No | — |
| WS-320 | EMISIÓN | Historia | Finalizada | 2026-01-05 | 2026-03-19 | Bethania | Luciana Rudaz | 3 | 481.42 | 0 | 1267.93 | No | — |
| WS-321 | EMISIÓN | Historia | Finalizada | 2026-01-05 | 2026-03-19 | Bethania | Luciana Rudaz | 3 | 479.97 | 0 | 1267.7 | No | — |
| WS-326 | EMISIÓN | Historia | Finalizada | 2026-01-05 | 2026-05-13 | Bethania | Luciana Rudaz | 7 | 320.62 | 0 | 1264.45 | No | — |
| AD-442 | ADQUIRENCIA | Historia | Finalizada | 2026-01-06 | 2026-03-12 | Andrea ORSINI | malzogaray | 3 | 353.47 | 0 | 892.5 | No | — |
| AD-444 | ADQUIRENCIA | Error | Finalizada | 2026-01-06 | 2026-01-27 | Nicolás Colón | Nicolás Colón | 1 | 120.22 | 91.78 | 297.48 | Sí | DEF/OBS |
| AD-445 | ADQUIRENCIA | Error | Finalizada | 2026-01-06 | 2026-01-28 | Nicolás Colón | Nicolás Colón | 1 | 0.9 | 0 | 526.65 | No | OBS |
| AD-446 | ADQUIRENCIA | Historia | Finalizada | 2026-01-06 | 2026-02-18 | Bethania | Pablo Antonio GOMES | 1 | 295.02 | 0 | 739.88 | No | — |
| WS-331 | EMISIÓN | Historia | Finalizada | 2026-01-06 | 2026-01-16 | Ana | Pablo Antonio GOMES | 1 | 164.57 | 0 | 73.05 | No | — |
| AD-448 | ADQUIRENCIA | Error | Finalizada | 2026-01-07 | 2026-01-19 | Nicolás Colón | Nicolás Colón | 1 | 11.25 | 0 | 281.53 | No | DEF/OBS |
| AD-449 | ADQUIRENCIA | Error | Finalizada | 2026-01-08 | 2026-01-27 | Andrea ORSINI | Andrea ORSINI | 3 | 361.5 | 0 | 2.48 | No | — |
| AD-453 | ADQUIRENCIA | Historia | Finalizada | 2026-01-08 | 2026-03-12 | Andrea ORSINI | malzogaray | 1 | 533.08 | 0 | 787.45 | No | — |
| WS-351 | EMISIÓN | Error | Finalizada | 2026-01-08 | 2026-01-08 | Nicolás Colón | Andrea ORSINI | 3 | 2.38 | 0 | 0.23 | No | — |
| WS-353 | EMISIÓN | Error | Finalizada | 2026-01-08 | 2026-01-16 | Ana | Ana | 3 | 66.4 | 0 | 124.72 | No | — |
| WS-354 | EMISIÓN | Historia | Finalizada | 2026-01-08 | 2026-01-22 | Ana | Pablo Antonio GOMES | 3 | 66.88 | 0 | 264.63 | No | — |
| WS-357 | EMISIÓN | Historia | Finalizada | 2026-01-08 | 2026-01-20 | Bethania | malzogaray | 1 | 5.33 | 0 | 283.77 | No | — |
| WS-358 | EMISIÓN | Historia | Finalizada | 2026-01-08 | 2026-03-10 | Andrea ORSINI | malzogaray | 3 | 669.5 | 0 | 788.72 | No | — |
| WS-359 | EMISIÓN | Error | Finalizada | 2026-01-08 | 2026-01-09 | Ana | Andrea ORSINI | — | 17.3 | 0 | 2.48 | No | — |
| AD-457 | ADQUIRENCIA | Error | Finalizada | 2026-01-09 | 2026-01-14 | Nicolás Colón | Nicolás Colón | 1 | 16.92 | 0 | 3.35 | No | OBS |
| AD-458 | ADQUIRENCIA | Historia | Finalizada | 2026-01-09 | 2026-02-24 | Bethania | malzogaray | 3 | 757.69 | 0 | 115.8 | No | — |
| AD-463 | ADQUIRENCIA | Error | Finalizada | 2026-01-09 | 2026-01-16 | Ana | Ana | 1 | 71.67 | 0 | 89.75 | No | OBS |
| WS-363 | EMISIÓN | Error | Finalizada | 2026-01-09 | 2026-01-16 | Bethania | Bethania | — | 69.68 | 0 | 96.33 | No | DEF/OBS |
| AD-459 | ADQUIRENCIA | Error | Finalizada | 2026-01-12 | 2026-01-14 | Nicolás Colón | Pablo Antonio GOMES | 1 | 16.95 | 0 | 29.18 | No | OBS |
| AD-460 | ADQUIRENCIA | Historia | Finalizada | 2026-01-12 | 2026-01-14 | Ana | Pablo Antonio GOMES | 3 | 48.68 | 0 | 2.6 | No | — |
| AD-614 | ADQUIRENCIA | Error | Finalizada | 2026-01-12 | 2026-03-03 | Ana | malzogaray | 1 | 200.83 | 70.87 | 940.18 | Sí | OBS |
| ARD-1 | ARDID | Historia | Finalizada | 2026-01-12 | 2026-02-04 | Andrea ORSINI | Andrea ORSINI | — | 72.88 | 482.35 | 0.02 | Sí | — |
| ARD-3 | ARDID | Error | Finalizada | 2026-01-12 | 2026-01-23 | Nicolás Colón | Nicolás Colón | — | 0.13 | 0 | 266.1 | No | OBS |
| OB-49 | ONBOARDING | Error | Finalizada | 2026-01-12 | 2026-01-16 | Andrea ORSINI | malzogaray | — | 0.32 | 0 | 93.17 | No | OBS |
| AD-465 | ADQUIRENCIA | Error | Finalizada | 2026-01-13 | 2026-01-13 | Ana | Ana | 1 | 0.55 | 0 | 7.12 | No | OBS |
| AD-466 | ADQUIRENCIA | Error | Finalizada | 2026-01-13 | 2026-01-13 | Ana | Ana | — | 0 | 0 | 6.83 | No | — |
| AD-467 | ADQUIRENCIA | Error | Finalizada | 2026-01-13 | 2026-01-27 | Andrea ORSINI | Nicolás Colón | 3 | 116.07 | 0 | 271.8 | No | OBS |
| AD-470 | ADQUIRENCIA | Error | Finalizada | 2026-01-13 | 2026-01-19 | Nicolás Colón | Nicolás Colón | 0.5 | 73.63 | 0 | 76.7 | No | OBS |
| AD-471 | ADQUIRENCIA | Error | Finalizada | 2026-01-13 | 2026-01-16 | Nicolás Colón | Nicolás Colón | 1 | 0.82 | 0 | 69.7 | No | OBS/REQ |
| AD-474 | ADQUIRENCIA | Error | Finalizada | 2026-01-13 | 2026-01-19 | Nicolás Colón | Nicolás Colón | 0.5 | 73.63 | 0 | 75.55 | No | OBS |
| AD-475 | ADQUIRENCIA | Error | Finalizada | 2026-01-13 | 2026-01-19 | Nicolás Colón | Nicolás Colón | 0.5 | 73.62 | 0 | 75.4 | No | OBS/REQ |
| AD-476 | ADQUIRENCIA | Error | Finalizada | 2026-01-13 | 2026-01-19 | Nicolás Colón | Nicolás Colón | 3 | 7.05 | 0 | 50.5 | No | OBS |
| AD-482 | ADQUIRENCIA | Error | Finalizada | 2026-01-13 | 2026-01-19 | Nicolás Colón | Nicolás Colón | 3 | 3.75 | 0 | 142.52 | No | OBS |
| AD-483 | ADQUIRENCIA | Error | Finalizada | 2026-01-13 | 2026-01-21 | Nicolás Colón | Nicolás Colón | 1 | 0.77 | 0 | 72.13 | No | DEF/OBS |
| OB-50 | ONBOARDING | Historia | Finalizada | 2026-01-13 | 2026-01-15 | Andrea ORSINI | Andrea ORSINI | — | 53.55 | 0 | 1.33 | No | — |
| SER-36 | SERVICIOS | Error | Finalizada | 2026-01-13 | 2026-02-18 | Nicolás Colón | Nicolás Colón | — | 531.38 | 0 | 331.32 | No | OBS |
| WS-371 | EMISIÓN | Historia | Finalizada | 2026-01-13 | 2026-04-29 | Bethania | Luciana Rudaz | 3 | 551.3 | 0 | 1827.84 | No | — |
| WS-373 | EMISIÓN | Historia | Finalizada | 2026-01-13 | 2026-04-01 | Bethania | Luciana Rudaz | 3 | 53.52 | 0 | 1818 | No | — |
| WS-374 | EMISIÓN | Historia | Finalizada | 2026-01-13 | 2026-01-19 | Nicolás Colón | malzogaray | 1 | 71.97 | 0 | 71.73 | No | — |
| AD-486 | ADQUIRENCIA | Error | Finalizada | 2026-01-14 | 2026-01-16 | Bethania | Bethania | 1 | 1.75 | 0 | 53.73 | No | OBS |
| AD-487 | ADQUIRENCIA | Error | Finalizada | 2026-01-14 | 2026-01-21 | Nicolás Colón | Nicolás Colón | 1 | 0.98 | 0 | 168.78 | No | DEF/OBS |
| AD-488 | ADQUIRENCIA | Error | Finalizada | 2026-01-14 | 2026-05-27 | Andrea ORSINI | Nicolás Colón | 1 | 1113.49 | 342.67 | 1754.63 | Sí | DEF/OBS |
| AD-489 | ADQUIRENCIA | Error | Finalizada | 2026-01-14 | 2026-01-19 | Nicolás Colón | Nicolás Colón | 1 | 3.97 | 0 | 124.3 | No | DEF/OBS |
| AD-493 | ADQUIRENCIA | Error | Finalizada | 2026-01-14 | 2026-01-15 | Andrea ORSINI | Andrea ORSINI | 1 | 25.05 | 0 | 0.02 | No | — |
| OB-51 | ONBOARDING | Error | Finalizada | 2026-01-14 | 2026-03-02 | Bethania | Andrea ORSINI | — | 159.22 | 337.42 | 629.08 | Sí | — |
| WS-375 | EMISIÓN | Historia | Finalizada | 2026-01-14 | 2026-01-16 | Nicolás Colón | malzogaray | 1 | 3.48 | 0 | 49.93 | No | — |
| WS-376 | EMISIÓN | Historia | Finalizada | 2026-01-14 | 2026-01-21 | Bethania | malzogaray | 0.5 | 44.23 | 0 | 120.87 | No | — |
| WS-377 | EMISIÓN | Historia | Finalizada | 2026-01-14 | 2026-01-22 | Nicolás Colón | malzogaray | 3 | 70.7 | 0 | 120.73 | No | — |
| WS-381 | EMISIÓN | Historia | Finalizada | 2026-01-14 | 2026-01-20 | Bethania | malzogaray | 1 | 25 | 0 | 119.53 | No | — |
| AD-496 | ADQUIRENCIA | Historia | Finalizada | 2026-01-15 | 2026-02-23 | malzogaray | Pablo Antonio GOMES | 15 | 0 | 0 | 935.38 | No | — |
| AD-498 | ADQUIRENCIA | Historia | Finalizada | 2026-01-15 | 2026-03-27 | Ana | malzogaray | 3 | 9.58 | 0 | 1708.48 | No | — |
| AD-502 | ADQUIRENCIA | Error | Finalizada | 2026-01-15 | 2026-01-23 | Nicolás Colón | Nicolás Colón | 3 | 16.08 | 0 | 170.83 | No | DEF/OBS |
| OB-54 | ONBOARDING | Error | Finalizada | 2026-01-15 | 2026-01-26 | Andrea ORSINI | Andrea ORSINI | — | 264.93 | 0 | 0 | No | — |
| WS-385 | EMISIÓN | Historia | Finalizada | 2026-01-15 | 2026-03-09 | malzogaray | Automation for Jira | 15 | 0 | 0 | 1281.86 | No | — |
| AD-507 | ADQUIRENCIA | Error | Finalizada | 2026-01-16 | 2026-01-23 | Nicolás Colón | Nicolás Colón | 1 | 0.18 | 0 | 167.68 | No | DEF/OBS |
| AD-509 | ADQUIRENCIA | Historia | Finalizada | 2026-01-16 | 2026-03-30 | Andrea ORSINI | Pablo Antonio GOMES | 7 | 261.43 | 0 | 1502.89 | No | — |
| AD-518 | ADQUIRENCIA | Historia | Finalizada | 2026-01-16 | 2026-03-25 | Andrea ORSINI | Pablo Antonio GOMES | 7 | 196.05 | 53.25 | 1395.99 | Sí | — |
| WS-386 | EMISIÓN | Error | Finalizada | 2026-01-16 | 2026-06-02 | Ana | Pablo Antonio GOMES | 3 | 123.38 | 20.73 | 1979.34 | Sí | OBS |
| WS-387 | EMISIÓN | Historia | Finalizada | 2026-01-16 | 2026-02-18 | Ana | Pablo Antonio GOMES | 3 | 313.52 | 0 | 485.78 | No | — |
| WS-393 | EMISIÓN | Error | Finalizada | 2026-01-16 | 2026-02-11 | Ana | Ana | 0.25 | 186.58 | 0 | 435.3 | No | — |
| AD-522 | ADQUIRENCIA | Error | Finalizada | 2026-01-19 | 2026-01-21 | Ana | Pablo Antonio GOMES | 1 | 25.38 | 0 | 29.73 | No | REQ |
| AD-525 | ADQUIRENCIA | Error | Finalizada | 2026-01-19 | 2026-01-21 | Nicolás Colón | Nicolás Colón | 3 | 0.28 | 0 | 39.27 | No | OBS |
| AD-577 | ADQUIRENCIA | Error | Finalizada | 2026-01-19 | 2026-01-27 | Ana | Ana | 3 | 5.42 | 0 | 189.22 | No | OBS |
| WS-391 | EMISIÓN | Historia | Finalizada | 2026-01-19 | 2026-01-19 | Ana | malzogaray | 3 | 0 | 0 | 0.2 | No | — |
| WS-396 | EMISIÓN | Historia | Finalizada | 2026-01-19 | 2026-03-12 | Andrea ORSINI | Automation for Jira | 1 | 75.72 | 0 | 1180.84 | No | — |
| AD-532 | ADQUIRENCIA | Error | Finalizada | 2026-01-20 | 2026-04-23 | Andrea ORSINI | Nicolás Colón | 1 | 262.6 | 116 | 1852.14 | Sí | DEF/OBS |
| AD-538 | ADQUIRENCIA | Error | Finalizada | 2026-01-20 | 2026-01-23 | Andrea ORSINI | Andrea ORSINI | 1 | 43.52 | 0 | 24.98 | No | OBS |
| AD-539 | ADQUIRENCIA | Error | Finalizada | 2026-01-20 | 2026-01-21 | Nicolás Colón | malzogaray | — | 16.15 | 0 | 0.25 | No | — |
| OB-55 | ONBOARDING | Historia | Finalizada | 2026-01-20 | 2026-04-08 | Andrea ORSINI | Andrea ORSINI | — | 862.23 | 512.98 | 508.58 | Sí | — |
| WS-397 | EMISIÓN | Error | Finalizada | 2026-01-20 | 2026-03-02 | Andrea ORSINI | Andrea ORSINI | 1 | 67.8 | 0 | 917.83 | No | — |
| WS-402 | EMISIÓN | Historia | Finalizada | 2026-01-20 | 2026-03-10 | Andrea ORSINI | Automation for Jira | 0.5 | 189.53 | 0 | 980.18 | No | — |
| WS-403 | EMISIÓN | Historia | Finalizada | 2026-01-20 | 2026-02-26 | malzogaray | Automation for Jira | 1 | 0 | 0 | 882.83 | No | — |
| AD-547 | ADQUIRENCIA | Error | Finalizada | 2026-01-21 | 2026-03-19 | Ana | Ana | 1 | 310.43 | 0 | 1054.55 | No | REQ |
| AD-560 | ADQUIRENCIA | Error | Finalizada | 2026-01-21 | 2026-01-22 | Nicolás Colón | Nicolás Colón | — | 0 | 0 | 22.47 | No | DEF/OBS |
| WS-408 | EMISIÓN | Historia | Finalizada | 2026-01-21 | 2026-06-11 | Bethania | Luciana Rudaz | 15 | 222.75 | 0.08 | 3174.21 | Sí | — |
| WS-409 | EMISIÓN | Historia | Finalizada | 2026-01-21 | 2026-02-12 | Ana | Automation for Jira | 7 | 238.05 | 0 | 295.12 | No | — |
| WS-411 | EMISIÓN | Error | Finalizada | 2026-01-21 | 2026-01-21 | Ana | Ana | 0.5 | 3.43 | 0 | 5.5 | No | — |
| WS-412 | EMISIÓN | Error | Finalizada | 2026-01-21 | 2026-01-21 | Nicolás Colón | Nicolás Colón | 0.25 | 0.13 | 0 | 4.9 | No | OBS |
| WS-413 | EMISIÓN | Error | Finalizada | 2026-01-21 | 2026-01-23 | Nicolás Colón | Nicolás Colón | 0.25 | 0.18 | 0 | 47.6 | No | OBS |
| WS-415 | EMISIÓN | Error | Finalizada | 2026-01-21 | 2026-01-21 | Ana | Andrea ORSINI | — | 0.58 | 0 | 0.52 | No | — |
| AD-572 | ADQUIRENCIA | Historia | Finalizada | 2026-01-22 | 2026-02-06 | Nicolás Colón | malzogaray | 3 | 70.68 | 0 | 281.88 | No | — |
| AD-574 | ADQUIRENCIA | Error | Finalizada | 2026-01-22 | 2026-02-04 | Andrea ORSINI | Andrea ORSINI | — | 16.38 | 0 | 282.88 | No | DEF/OBS |
| AD-591 | ADQUIRENCIA | Error | Finalizada | 2026-01-22 | 2026-03-03 | Andrea ORSINI | malzogaray | 3 | 168.05 | 0 | 799.37 | No | OBS |
| AD-575 | ADQUIRENCIA | Error | Finalizada | 2026-01-23 | 2026-01-23 | Andrea ORSINI | Andrea ORSINI | 1 | 0.92 | 0 | 14.77 | No | DEF/OBS |
| AD-576 | ADQUIRENCIA | Error | Finalizada | 2026-01-23 | 2026-02-03 | Andrea ORSINI | Andrea ORSINI | — | 0.03 | 0 | 272.22 | No | DEF/OBS |
| OB-57 | ONBOARDING | Historia | Bloqueado | 2026-01-23 | — | Bethania | Pablo Antonio GOMES | — | 698.73 | 0 | 3493.02 | No | — |
| OB-58 | ONBOARDING | Historia | Bloqueado | 2026-01-23 | — | Bethania | Pablo Antonio GOMES | — | 698.73 | 0 | 3493.01 | No | — |
| SER-38 | SERVICIOS | Historia | Finalizada | 2026-01-23 | 2026-02-26 | Nicolás Colón | Nicolás Colón | — | 330.9 | 0 | 484.15 | No | — |
| WS-434 | EMISIÓN | Historia | Finalizada | 2026-01-23 | 2026-02-20 | Bethania | Automation for Jira | 7 | 22.57 | 0 | 653.13 | No | — |
| WS-440 | EMISIÓN | Error | Finalizada | 2026-01-23 | 2026-02-18 | Ana | Pablo Antonio GOMES | 0.5 | 456.38 | 0 | 170.75 | No | — |
| WS-445 | EMISIÓN | Error | Finalizada | 2026-01-23 | 2026-04-13 | Bethania | Bethania | 1 | 145.92 | 0 | 1785.53 | No | DEF/OBS |
| WS-448 | EMISIÓN | Error | Finalizada | 2026-01-23 | 2026-01-26 | Nicolás Colón | Nicolás Colón | 0.25 | 1.02 | 0 | 67.12 | No | OBS |
| WS-462 | EMISIÓN | Error | Finalizada | 2026-01-26 | 2026-03-02 | Ana | Ana | 7 | 267.43 | 0 | 576.53 | No | — |
| AD-584 | ADQUIRENCIA | Error | Finalizada | 2026-01-27 | 2026-03-19 | Andrea ORSINI | Andrea ORSINI | 1 | 314.3 | 0 | 911.13 | No | OBS |
| AD-585 | ADQUIRENCIA | Error | Finalizada | 2026-01-27 | 2026-02-27 | Andrea ORSINI | Andrea ORSINI | 1 | 74.28 | 0 | 672.95 | No | OBS |
| AD-586 | ADQUIRENCIA | Error | Finalizada | 2026-01-27 | 2026-05-20 | Nicolás Colón | Nicolás Colón | 3 | 0.2 | 28.22 | 2682.5 | Sí | OBS |
| AD-587 | ADQUIRENCIA | Error | Finalizada | 2026-01-27 | 2026-02-23 | Andrea ORSINI | Nicolás Colón | 3 | 123.1 | 0 | 528 | No | OBS |
| AD-594 | ADQUIRENCIA | Historia | Finalizada | 2026-01-27 | 2026-02-26 | Andrea ORSINI | malzogaray | 1 | 74.65 | 0 | 639.92 | No | — |
| AD-595 | ADQUIRENCIA | Error | Finalizada | 2026-01-27 | 2026-03-12 | Andrea ORSINI | malzogaray | 1 | 331.5 | 0 | 234.77 | No | — |
| AD-596 | ADQUIRENCIA | Historia | Finalizada | 2026-01-27 | 2026-02-10 | malzogaray | malzogaray | 1 | 91.75 | 0 | 236.62 | No | — |
| AD-597 | ADQUIRENCIA | Historia | Finalizada | 2026-01-27 | 2026-02-10 | Andrea ORSINI | malzogaray | 3 | 91.4 | 0 | 236.88 | No | — |
| AD-598 | ADQUIRENCIA | Error | Bloqueado | 2026-01-27 | — | malzogaray | malzogaray | 1 | 2153.25 | 0 | 1196.77 | No | OBS |
| AD-599 | ADQUIRENCIA | Error | Finalizada | 2026-01-27 | 2026-02-23 | malzogaray | malzogaray | 3 | 48.73 | 266.15 | 330.75 | Sí | OBS |
| WS-472 | EMISIÓN | Error | Finalizada | 2026-01-27 | 2026-01-28 | Bethania | Andrea ORSINI | 1 | 0.98 | 0 | 26.08 | No | — |
| WS-474 | EMISIÓN | Historia | Finalizada | 2026-01-27 | 2026-02-24 | Ana | malzogaray | 1 | 282.32 | 0 | 383.93 | No | — |
| AD-604 | ADQUIRENCIA | Error | Finalizada | 2026-01-28 | 2026-03-19 | Ana | Ana | 3 | 193.45 | 0 | 1008.45 | No | OBS |
| OB-62 | ONBOARDING | Error | Finalizada | 2026-01-28 | 2026-01-28 | Andrea ORSINI | Andrea ORSINI | — | 2.27 | 0 | 0.12 | No | — |
| SER-39 | SERVICIOS | Historia | Finalizada | 2026-01-28 | 2026-02-26 | Nicolás Colón | Nicolás Colón | — | 331.1 | 0 | 362.52 | No | — |
| WS-478 | EMISIÓN | Error | Finalizada | 2026-01-28 | 2026-02-11 | Bethania | Nicolás Colón | 1 | 21.47 | 0 | 173.4 | No | OBS |
| WS-479 | EMISIÓN | Historia | Finalizada | 2026-01-28 | 2026-02-05 | Andrea ORSINI | Automation for Jira | 7 | 18.3 | 0 | 172.72 | No | — |
| WS-480 | EMISIÓN | Historia | Finalizada | 2026-01-28 | 2026-03-12 | Ana | Automation for Jira | 3 | 508.6 | 0.28 | 527.5 | Sí | — |
| WS-486 | EMISIÓN | Error | Finalizada | 2026-01-29 | 2026-01-29 | malzogaray | Andrea ORSINI | 0.5 | 1.22 | 0 | 0.2 | No | — |
| AD-615 | ADQUIRENCIA | Error | Finalizada | 2026-01-30 | 2026-02-12 | Andrea ORSINI | Nicolás Colón | 1 | 24.55 | 0 | 289.5 | No | OBS |
| WS-490 | EMISIÓN | Error | Finalizada | 2026-01-30 | 2026-02-24 | Andrea ORSINI | Pablo Antonio GOMES | 7 | 90.95 | 0 | 509.9 | No | — |
| AD-618 | ADQUIRENCIA | Error | Finalizada | 2026-02-02 | 2026-02-03 | Ana | Ana | 1 | 0.28 | 0 | 27.02 | No | OBS |
| AD-620 | ADQUIRENCIA | Historia | Finalizada | 2026-02-02 | 2026-03-30 | Andrea ORSINI | Pablo Antonio GOMES | 3 | 462.33 | 20.55 | 863.5 | Sí | — |
| AD-621 | ADQUIRENCIA | Historia | Finalizada | 2026-02-02 | 2026-03-18 | Andrea ORSINI | Pablo Antonio GOMES | 3 | 170.05 | 0 | 857.23 | No | — |
| AD-622 | ADQUIRENCIA | Historia | Finalizada | 2026-02-02 | 2026-03-16 | Andrea ORSINI | Pablo Antonio GOMES | 1 | 149.08 | 0 | 856.62 | No | — |
| ARD-6 | ARDID | Historia | Finalizada | 2026-02-02 | 2026-05-08 | Andrea ORSINI | Andrea ORSINI | — | 25.05 | 1707.34 | 549.33 | Sí | — |
| AD-624 | ADQUIRENCIA | Historia | Finalizada | 2026-02-03 | 2026-02-19 | Nicolás Colón | Pablo Antonio GOMES | 1 | 139.73 | 0 | 246.15 | No | — |
| AD-629 | ADQUIRENCIA | Error | Finalizada | 2026-02-03 | 2026-02-18 | Nicolás Colón | Nicolás Colón | 1 | 110.08 | 0 | 248.2 | No | DEF/OBS |
| AD-630 | ADQUIRENCIA | Error | Finalizada | 2026-02-03 | 2026-02-18 | Nicolás Colón | Nicolás Colón | 1 | 110.07 | 0 | 248.22 | No | DEF/OBS |
| SER-40 | SERVICIOS | Historia | Finalizada | 2026-02-03 | 2026-02-13 | Nicolás Colón | Nicolás Colón | — | 18.88 | 0 | 219.85 | No | — |
| WS-494 | EMISIÓN | Historia | Finalizada | 2026-02-03 | 2026-04-27 | malzogaray | Alan Martinez | 3 | 1379.53 | 76.27 | 555.23 | Sí | — |
| WS-495 | EMISIÓN | Historia | Finalizada | 2026-02-03 | 2026-03-09 | Nicolás Colón | Automation for Jira | 1 | 431.12 | 0 | 388.4 | No | — |
| AD-636 | ADQUIRENCIA | Historia | Finalizada | 2026-02-04 | 2026-04-20 | Ana | Automation for Jira | 3 | 945.74 | 0 | 856.82 | No | — |
| AD-637 | ADQUIRENCIA | Historia | Finalizada | 2026-02-04 | 2026-04-29 | Bethania | Automation for Jira | 3 | 306.9 | 720.28 | 993.11 | Sí | — |
| AD-638 | ADQUIRENCIA | Historia | Finalizada | 2026-02-04 | 2026-04-10 | Ana | Automation for Jira | 1 | 669.97 | 0 | 881.73 | No | — |
| WS-500 | EMISIÓN | Historia | Finalizada | 2026-02-04 | 2026-04-20 | Ana | Automation for Jira | 7 | 1325.48 | 0 | 484.98 | No | — |
| WS-501 | EMISIÓN | Historia | Finalizada | 2026-02-04 | 2026-03-10 | Ana | malzogaray | 3 | 191.4 | 0 | 626.43 | No | OBS/REQ |
| WS-502 | EMISIÓN | Historia | Finalizada | 2026-02-04 | 2026-02-27 | malzogaray | Automation for Jira | 1 | 24.67 | 15.82 | 510.92 | Sí | — |
| WS-506 | EMISIÓN | Error | Finalizada | 2026-02-04 | 2026-03-04 | Andrea ORSINI | Andrea ORSINI | 0.5 | 264.58 | 66.52 | 334.08 | Sí | OBS |
| AD-641 | ADQUIRENCIA | Error | Finalizada | 2026-02-05 | 2026-04-23 | Andrea ORSINI | Alan Martinez | 3 | 645.93 | 0 | 1214.78 | No | — |
| AD-646 | ADQUIRENCIA | Error | Finalizada | 2026-02-05 | 2026-03-02 | Bethania | Bethania | 3 | 92.02 | 191.95 | 316.02 | Sí | OBS |
| AD-647 | ADQUIRENCIA | Historia | Finalizada | 2026-02-05 | 2026-06-03 | Andrea ORSINI | Pablo Antonio GOMES | 3 | 101.3 | 0 | 2742.65 | No | — |
| AD-649 | ADQUIRENCIA | Error | Finalizada | 2026-02-05 | 2026-02-18 | malzogaray | Bethania | 1 | 168.83 | 0 | 147.8 | No | OBS |
| AD-651 | ADQUIRENCIA | Error | Finalizada | 2026-02-05 | 2026-04-23 | Andrea ORSINI | Nicolás Colón | 3 | 68.48 | 0 | 1800.74 | No | DEF/OBS |
| AD-652 | ADQUIRENCIA | Error | Bloqueado | 2026-02-05 | — | malzogaray | Andrea ORSINI | 1 | 649.27 | 0 | 981.22 | No | DEF/OBS |
| WS-509 | EMISIÓN | Error | Finalizada | 2026-02-05 | 2026-02-11 | Andrea ORSINI | Pablo Antonio GOMES | 1 | 47.6 | 0 | 91.92 | No | REQ |
| AD-656 | ADQUIRENCIA | Historia | Finalizada | 2026-02-06 | 2026-03-30 | Bethania | Automation for Jira | 1 | 121.43 | 0 | 1127.03 | No | — |
| WS-510 | EMISIÓN | Error | Finalizada | 2026-02-06 | 2026-02-11 | Ana | Ana | 1 | 114.77 | 0 | 6.17 | No | — |
| WS-514 | EMISIÓN | Historia | Finalizada | 2026-02-06 | 2026-02-18 | Bethania | Automation for Jira | 1 | 195.02 | 0 | 88.82 | No | — |
| AD-660 | ADQUIRENCIA | Historia | Finalizada | 2026-02-09 | 2026-04-27 | Andrea ORSINI | Pablo Antonio GOMES | 3 | 0.37 | 0 | 1838.99 | No | — |
| AD-663 | ADQUIRENCIA | Historia | Finalizada | 2026-02-10 | 2026-05-06 | Andrea ORSINI | Automation for Jira | 3 | 64.75 | 0 | 2021.04 | No | — |
| AD-670 | ADQUIRENCIA | Error | Finalizada | 2026-02-10 | 2026-03-17 | Andrea ORSINI | Andrea ORSINI | 1 | 268.62 | 0 | 570.77 | No | DEF/OBS |
| WS-543 | EMISIÓN | Historia | Finalizada | 2026-02-10 | 2026-04-17 | Bethania | malzogaray | 7 | 48.53 | 0 | 1544.36 | No | — |
| WS-549 | EMISIÓN | Historia | Finalizada | 2026-02-10 | 2026-04-27 | Bethania | Pablo Antonio GOMES | 7 | 94.72 | 0 | 1739.13 | No | — |
| WS-550 | EMISIÓN | Historia | Finalizada | 2026-02-10 | 2026-04-27 | Bethania | Pablo Antonio GOMES | 3 | 95.97 | 17.9 | 1738.41 | Sí | — |
| WS-551 | EMISIÓN | Historia | Finalizada | 2026-02-10 | 2026-04-27 | Bethania | Pablo Antonio GOMES | 3 | 99.47 | 0 | 1738.28 | No | — |
| AD-672 | ADQUIRENCIA | Error | Finalizada | 2026-02-11 | 2026-03-20 | Andrea ORSINI | Nicolás Colón | 1 | 126.1 | 16.82 | 793.72 | Sí | OBS |
| AD-674 | ADQUIRENCIA | Historia | Finalizada | 2026-02-11 | 2026-02-18 | malzogaray | malzogaray | 1 | 1.12 | 0 | 170.6 | No | — |
| AD-677 | ADQUIRENCIA | Historia | Finalizada | 2026-02-11 | 2026-03-23 | Andrea ORSINI | Pablo Antonio GOMES | 3 | 290.17 | 0 | 670.28 | No | — |
| OB-66 | ONBOARDING | Error | Finalizada | 2026-02-11 | 2026-03-13 | Andrea ORSINI | Andrea ORSINI | — | 205.28 | 522.73 | 0.82 | Sí | — |
| OB-67 | ONBOARDING | Error | Finalizada | 2026-02-11 | 2026-02-23 | Andrea ORSINI | Andrea ORSINI | — | 286.43 | 0 | 0.68 | No | — |
| OB-69 | ONBOARDING | Historia | Finalizada | 2026-02-11 | 2026-02-12 | Andrea ORSINI | Andrea ORSINI | — | 30.35 | 1.58 | 0.5 | Sí | — |
| OB-70 | ONBOARDING | Historia | Finalizada | 2026-02-11 | 2026-02-12 | Andrea ORSINI | Andrea ORSINI | — | 29.45 | 0 | 0.4 | No | — |
| OB-71 | ONBOARDING | Error | Finalizada | 2026-02-11 | 2026-04-10 | Andrea ORSINI | Andrea ORSINI | — | 31.62 | 1370.09 | 0.25 | Sí | — |
| OB-72 | ONBOARDING | Historia | Finalizada | 2026-02-11 | 2026-02-18 | Bethania | Andrea ORSINI | — | 169.03 | 0 | 0.17 | No | — |
| OB-78 | ONBOARDING | Error | Finalizada | 2026-02-11 | 2026-02-12 | Andrea ORSINI | Andrea ORSINI | — | 0 | 0 | 25.68 | No | OBS |
| WS-555 | EMISIÓN | Historia | Finalizada | 2026-02-11 | 2026-04-13 | Andrea ORSINI | Nicolas Pomponio | 7 | 3.43 | 0 | 1471.94 | No | — |
| WS-556 | EMISIÓN | Historia | Finalizada | 2026-02-11 | 2026-03-09 | malzogaray | Nicolas Pomponio | 1 | 0 | 0 | 623.07 | No | — |
| AD-681 | ADQUIRENCIA | Error | Finalizada | 2026-02-12 | 2026-03-25 | malzogaray | Ana | — | 1.12 | 5.95 | 986.26 | Sí | OBS |
| AD-683 | ADQUIRENCIA | Error | Finalizada | 2026-02-12 | 2026-03-16 | Ana | malzogaray | 1 | 457.73 | 0 | 308.2 | No | OBS |
| AD-684 | ADQUIRENCIA | Error | Finalizada | 2026-02-12 | 2026-03-26 | Ana | malzogaray | 3 | 296.63 | 183.85 | 525.43 | Sí | OBS/REQ |
| AD-685 | ADQUIRENCIA | Historia | Finalizada | 2026-02-12 | 2026-03-17 | Andrea ORSINI | malzogaray | 1 | 22.75 | 0 | 779.38 | No | — |
| AD-688 | ADQUIRENCIA | Historia | Finalizada | 2026-02-12 | 2026-06-04 | Andrea ORSINI | malzogaray | 15 | 51.55 | 0 | 2643.38 | No | — |
| ARD-10 | ARDID | Error | Finalizada | 2026-02-12 | 2026-02-12 | Andrea ORSINI | Andrea ORSINI | — | 0 | 0 | 0.38 | No | OBS |
| ARD-9 | ARDID | Error | Finalizada | 2026-02-12 | 2026-02-12 | Andrea ORSINI | Andrea ORSINI | — | 0 | 0 | 0.45 | No | OBS |
| OB-81 | ONBOARDING | Error | Finalizada | 2026-02-12 | 2026-02-13 | Andrea ORSINI | Andrea ORSINI | — | 5.3 | 0 | 27.78 | No | OBS |
| OB-82 | ONBOARDING | Error | Finalizada | 2026-02-12 | 2026-02-19 | Andrea ORSINI | Andrea ORSINI | — | 3.63 | 0 | 164.52 | No | OBS |
| OB-83 | ONBOARDING | Error | Finalizada | 2026-02-12 | 2026-05-05 | Andrea ORSINI | Andrea ORSINI | — | 7 | 1790.6 | 24.12 | Sí | DEF/OBS |
| OB-85 | ONBOARDING | Error | Finalizada | 2026-02-12 | 2026-02-13 | Andrea ORSINI | Andrea ORSINI | — | 4.57 | 1793.52 | 23.38 | Sí | OBS |
| SER-41 | SERVICIOS | Historia | Finalizada | 2026-02-12 | 2026-04-30 | Nicolás Colón | Pablo Antonio GOMES | — | 50.92 | 357.63 | 1444.79 | Sí | — |
| SER-42 | SERVICIOS | Historia | Finalizada | 2026-02-12 | 2026-04-20 | Nicolás Colón | Pablo Antonio GOMES | — | 53.57 | 121 | 1444.33 | Sí | — |
| WS-558 | EMISIÓN | Historia | Finalizada | 2026-02-12 | 2026-02-12 | malzogaray | malzogaray | — | 0 | 0 | 0.07 | No | — |
| WS-559 | EMISIÓN | Historia | Finalizada | 2026-02-12 | 2026-04-13 | Andrea ORSINI | Nicolas Pomponio | 3 | 3.45 | 0 | 1445.11 | No | — |
| WS-560 | EMISIÓN | Historia | Finalizada | 2026-02-12 | 2026-04-13 | Andrea ORSINI | malzogaray | 15 | 3.37 | 0 | 1445.06 | No | — |
| WS-561 | EMISIÓN | Historia | Finalizada | 2026-02-12 | 2026-03-02 | Andrea ORSINI | malzogaray | 7 | 19.02 | 0 | 428.2 | No | — |
| AD-693 | ADQUIRENCIA | Error | Finalizada | 2026-02-13 | 2026-02-23 | Andrea ORSINI | malzogaray | 1 | 71.38 | 71.85 | 168.25 | Sí | — |
| AD-694 | ADQUIRENCIA | Error | Finalizada | 2026-02-13 | 2026-03-27 | Ana | malzogaray | 1 | 434.65 | 46.73 | 534.63 | Sí | — |
| AD-696 | ADQUIRENCIA | Error | Finalizada | 2026-02-13 | 2026-03-25 | Bethania | malzogaray | 3 | 219.42 | 26.4 | 711.35 | Sí | OBS |
| AD-700 | ADQUIRENCIA | Error | Finalizada | 2026-02-13 | 2026-03-27 | Bethania | malzogaray | 1 | 264.32 | 47.37 | 690.63 | Sí | OBS |
| WS-565 | EMISIÓN | Error | Finalizada | 2026-02-13 | 2026-02-23 | Andrea ORSINI | malzogaray | 15 | 70.02 | 0 | 165.95 | No | — |
| AD-703 | ADQUIRENCIA | Historia | Finalizada | 2026-02-18 | 2026-06-11 | malzogaray | Luciana Rudaz | 15 | 408.77 | 70.22 | 2228.55 | Sí | — |
| AD-707 | ADQUIRENCIA | Error | Finalizada | 2026-02-18 | 2026-03-02 | Bethania | Bethania | 1 | 123.37 | 0 | 161.8 | No | OBS |
| SER-43 | SERVICIOS | Historia | Finalizada | 2026-02-18 | 2026-02-25 | Nicolás Colón | Nicolás Colón | 3 | 4.87 | 0 | 170.45 | No | — |
| SER-44 | SERVICIOS | Error | Finalizada | 2026-02-18 | 2026-02-20 | Nicolás Colón | Nicolás Colón | 1 | 24.98 | 0 | 22.47 | No | OBS |
| WS-575 | EMISIÓN | Historia | Finalizada | 2026-02-18 | 2026-03-03 | Ana | Nicolas Pomponio | 1 | 97.28 | 0 | 218.37 | No | — |
| AD-710 | ADQUIRENCIA | Error | Finalizada | 2026-02-19 | 2026-02-20 | Bethania | Bethania | 1 | 20.55 | 0 | 3.23 | No | DEF/OBS |
| AD-714 | ADQUIRENCIA | Error | Finalizada | 2026-02-19 | 2026-03-26 | Nicolás Colón | malzogaray | 3 | 290.03 | 81.88 | 471.98 | Sí | — |
| ARD-12 | ARDID | Error | Finalizada | 2026-02-19 | 2026-02-20 | Andrea ORSINI | Andrea ORSINI | — | 0.08 | 0 | 26.38 | No | DEF/OBS |
| OB-88 | ONBOARDING | Historia | Finalizada | 2026-02-19 | 2026-02-23 | Andrea ORSINI | Andrea ORSINI | — | 95.88 | 2.65 | 0 | Sí | — |
| OB-89 | ONBOARDING | Historia | Finalizada | 2026-02-19 | 2026-02-19 | Andrea ORSINI | Andrea ORSINI | — | 2.97 | 0 | 0.03 | No | — |
| WS-584 | EMISIÓN | Historia | Finalizada | 2026-02-19 | 2026-04-23 | malzogaray | Pablo Antonio GOMES | 3 | 50.02 | 144.27 | 1326.63 | Sí | — |
| WS-585 | EMISIÓN | Historia | Finalizada | 2026-02-19 | 2026-04-07 | Bethania | Luciana Rudaz | 3 | 261.78 | 0 | 875.21 | No | — |
| AD-718 | ADQUIRENCIA | Error | Finalizada | 2026-02-20 | 2026-03-02 | Bethania | Bethania | 3 | 218.2 | 0 | 166.77 | No | OBS |
| ARD-11 | ARDID | Historia | Finalizada | 2026-02-20 | 2026-02-24 | Nicolás Colón | Andrea ORSINI | — | 88.2 | 0 | 0.02 | No | — |
| OB-97 | ONBOARDING | Error | Finalizada | 2026-02-20 | 2026-02-23 | Andrea ORSINI | Andrea ORSINI | — | 0 | 0 | 71.42 | No | OBS |
| WS-588 | EMISIÓN | Historia | Finalizada | 2026-02-20 | 2026-04-27 | Ana | Nicolás Colón | 3 | 128 | 0 | 1472.48 | No | — |
| WS-590 | EMISIÓN | Error | Finalizada | 2026-02-20 | 2026-02-23 | Ana | Nicolás Colón | 0.25 | 51.12 | 0 | 16.57 | No | DEF/OBS |
| WS-591 | EMISIÓN | Error | Finalizada | 2026-02-20 | 2026-03-16 | Ana | Pablo Antonio GOMES | 3 | 289.25 | 0 | 280.4 | No | — |
| AD-728 | ADQUIRENCIA | Error | Finalizada | 2026-02-23 | 2026-02-26 | Andrea ORSINI | Andrea ORSINI | 3 | 19.9 | 0 | 52.28 | No | DEF/OBS |
| WS-594 | EMISIÓN | Historia | Finalizada | 2026-02-23 | 2026-02-27 | Andrea ORSINI | Juan Pablo Carubelli | 3 | 92.77 | 0 | 73.48 | No | — |
| AD-748 | ADQUIRENCIA | Error | Finalizada | 2026-02-24 | 2026-05-08 | Bethania | Bethania | 3 | 115.17 | 630.45 | 1017.39 | Sí | OBS |
| WS-596 | EMISIÓN | Historia | Finalizada | 2026-02-24 | 2026-03-03 | Ana | Juan Pablo Carubelli | 3 | 91.02 | 0 | 77.87 | No | — |
| WS-597 | EMISIÓN | Historia | Finalizada | 2026-02-24 | 2026-02-26 | Andrea ORSINI | Juan Pablo Carubelli | 1 | 0.22 | 0 | 50.35 | No | — |
| WS-598 | EMISIÓN | Error | Finalizada | 2026-02-24 | 2026-02-27 | Ana | Ana | 0.5 | 23.38 | 0 | 49.58 | No | OBS |
| AD-754 | ADQUIRENCIA | Historia | Finalizada | 2026-02-25 | 2026-03-12 | malzogaray | Andrea ORSINI | — | 354.02 | 1.38 | 1.17 | Sí | — |
| AD-756 | ADQUIRENCIA | Historia | Finalizada | 2026-02-25 | 2026-03-20 | Bethania | Nicolás Colón | — | 18.18 | 0 | 527.37 | No | OBS/REQ |
| ARD-16 | ARDID | Error | Finalizada | 2026-02-25 | 2026-05-08 | Andrea ORSINI | Andrea ORSINI | — | 0.05 | 0 | 1730.79 | No | OBS |
| WS-603 | EMISIÓN | Error | Finalizada | 2026-02-25 | 2026-03-04 | malzogaray | Pablo Antonio GOMES | 1 | 0 | 0 | 169.5 | No | — |
| AD-767 | ADQUIRENCIA | Historia | Finalizada | 2026-02-26 | 2026-03-30 | malzogaray | Pablo Antonio GOMES | 3 | 152.03 | 85.55 | 529.02 | Sí | — |
| AD-769 | ADQUIRENCIA | Historia | Finalizada | 2026-02-26 | 2026-04-21 | Nicolás Colón | Nicolás Colón | 3 | 20.8 | 145.15 | 1129.12 | Sí | — |
| AD-771 | ADQUIRENCIA | Historia | Finalizada | 2026-02-26 | 2026-07-02 | Andrea ORSINI | Pablo Antonio GOMES | 3 | 367.72 | 63.77 | 2519.27 | Sí | — |
| AD-775 | ADQUIRENCIA | Error | EN QA | 2026-02-26 | — | Andrea ORSINI | Andrea ORSINI | 15 | 624.02 | 0 | 2988.11 | No | — |
| ARD-17 | ARDID | Historia | Finalizada | 2026-02-26 | 2026-02-26 | Nicolás Colón | Andrea ORSINI | — | 0.05 | 0 | 0 | No | — |
| OB-98 | ONBOARDING | Error | Finalizada | 2026-02-26 | 2026-02-27 | Andrea ORSINI | Andrea ORSINI | — | 23.15 | 0 | 0 | No | — |
| SER-52 | SERVICIOS | Historia | Finalizada | 2026-02-26 | 2026-04-10 | Nicolás Colón | Pablo Antonio GOMES | — | 698.18 | 0 | 335.75 | No | — |
| WS-605 | EMISIÓN | Historia | Finalizada | 2026-02-26 | 2026-03-11 | Ana | malzogaray | 7 | 14.88 | 0 | 292.7 | No | — |
| WS-606 | EMISIÓN | Historia | Finalizada | 2026-02-26 | 2026-03-10 | Ana | malzogaray | 7 | 4.33 | 0 | 292.65 | No | — |
| WS-607 | EMISIÓN | Historia | Finalizada | 2026-02-26 | 2026-04-01 | Andrea ORSINI | malzogaray | 3 | 17.95 | 0 | 790.73 | No | — |
| AD-783 | ADQUIRENCIA | Error | Finalizada | 2026-02-27 | 2026-03-31 | Bethania | Nicolás Colón | 3 | 72.53 | 0.78 | 692.45 | Sí | OBS |
| AD-784 | ADQUIRENCIA | Error | Finalizada | 2026-02-27 | 2026-04-08 | Bethania | Bethania | 1 | 22.5 | 0 | 67.83 | No | OBS |
| AD-786 | ADQUIRENCIA | Error | Finalizada | 2026-02-27 | 2026-04-08 | Bethania | Bethania | 3 | 21.85 | 0 | 932.38 | No | OBS |
| OB-100 | ONBOARDING | Error | Finalizada | 2026-02-27 | 2026-02-27 | Andrea ORSINI | Andrea ORSINI | — | 1.35 | 0 | 0 | No | OBS |
| OB-102 | ONBOARDING | Error | Finalizada | 2026-02-27 | 2026-05-06 | Andrea ORSINI | Andrea ORSINI | — | 4.73 | 0 | 1626.67 | No | — |
| WS-610 | EMISIÓN | Historia | Finalizada | 2026-02-27 | 2026-05-26 | Ana | Pablo Antonio GOMES | 3 | 475.18 | 0 | 1636.34 | No | — |
| WS-612 | EMISIÓN | Historia | Finalizada | 2026-02-27 | 2026-03-06 | Bethania | malzogaray | 1 | 46.25 | 0 | 124.95 | No | — |
| WS-613 | EMISIÓN | Historia | Finalizada | 2026-02-27 | 2026-07-17 | malzogaray | Nicolás Colón | 15 | 0 | 0 | 3354.61 | No | — |
| WS-614 | EMISIÓN | Historia | Finalizada | 2026-03-02 | 2026-06-01 | Ana | Automation for Jira | 0.5 | 1021.84 | 0 | 667.2 | No | — |
| WS-616 | EMISIÓN | Historia | Finalizada | 2026-03-03 | 2026-05-26 | malzogaray | Automation for Jira | 3 | 19.58 | 0 | 2013.08 | No | — |
| WS-618 | EMISIÓN | Error | Finalizada | 2026-03-03 | 2026-04-07 | Bethania | Bethania | — | 2.9 | 0 | 847.16 | No | DEF/OBS |
| AD-804 | ADQUIRENCIA | Historia | Finalizada | 2026-03-04 | 2026-03-05 | malzogaray | Automation for Jira | 1 | 0 | 0 | 21.93 | No | — |
| WS-620 | EMISIÓN | Error | Finalizada | 2026-03-04 | 2026-03-04 | Andrea ORSINI | Andrea ORSINI | — | 0.03 | 0 | 6.3 | No | DEF/OBS |
| WS-623 | EMISIÓN | Error | Finalizada | 2026-03-05 | 2026-03-05 | Nicolás Colón | Ana | — | 0 | 0 | 0.35 | No | — |
| WS-625 | EMISIÓN | Historia | Finalizada | 2026-03-05 | 2026-03-09 | Andrea ORSINI | Nicolas Pomponio | 1 | 6.02 | 0 | 89.98 | No | — |
| AD-807 | ADQUIRENCIA | Error | Finalizada | 2026-03-06 | 2026-03-11 | Nicolás Colón | malzogaray | 1 | 3.02 | 0 | 121.08 | No | — |
| AD-808 | ADQUIRENCIA | Historia | Finalizada | 2026-03-06 | 2026-03-26 | Andrea ORSINI | Nicolas Pico | 1 | 0 | 0 | 486.28 | No | — |
| AD-809 | ADQUIRENCIA | Error | Finalizada | 2026-03-06 | 2026-03-11 | Bethania | Bethania | 1 | 51.27 | 0 | 72.9 | No | DEF/OBS |
| AD-810 | ADQUIRENCIA | Error | Finalizada | 2026-03-06 | 2026-04-07 | Nicolás Colón | Pablo Antonio GOMES | — | 0 | 0 | 777.03 | No | — |
| WS-627 | EMISIÓN | Historia | Finalizada | 2026-03-06 | 2026-05-04 | Bethania | Luciana Rudaz | 3 | 453.97 | 0 | 972.53 | No | — |
| AD-814 | ADQUIRENCIA | Error | Finalizada | 2026-03-09 | 2026-03-26 | Andrea ORSINI | Andrea ORSINI | 1 | 186.32 | 0 | 216.15 | No | DEF/OBS |
| WS-674 | EMISIÓN | Error | Finalizada | 2026-03-09 | 2026-03-10 | Andrea ORSINI | malzogaray | 0.5 | 24.78 | 2.8 | 0 | Sí | OBS |
| AD-818 | ADQUIRENCIA | Error | Finalizada | 2026-03-10 | 2026-03-18 | Andrea ORSINI | Pablo Antonio GOMES | 1 | 178.17 | 0 | 20.08 | No | OBS |
| AD-819 | ADQUIRENCIA | Error | Finalizada | 2026-03-10 | 2026-03-18 | Andrea ORSINI | Pablo Antonio GOMES | 1 | 178.23 | 0 | 20.07 | No | OBS |
| AD-820 | ADQUIRENCIA | Error | Finalizada | 2026-03-10 | 2026-03-16 | Bethania | malzogaray | 1 | 115.93 | 0 | 23.17 | No | — |
| WS-692 | EMISIÓN | Historia | Finalizada | 2026-03-10 | 2026-04-10 | Ana | Pablo Antonio GOMES | 3 | 334.2 | 0 | 403.95 | No | — |
| WS-698 | EMISIÓN | Error | Finalizada | 2026-03-10 | 2026-03-10 | Ana | malzogaray | — | 3.87 | 0 | 0.27 | No | — |
| WS-702 | EMISIÓN | Error | Finalizada | 2026-03-10 | 2026-03-16 | Ana | Ana | 3 | 3.75 | 0 | 133.73 | No | — |
| AD-823 | ADQUIRENCIA | Error | Finalizada | 2026-03-11 | 2026-03-11 | malzogaray | Alan Martinez | 1 | 0.53 | 0 | 4.58 | No | — |
| WS-703 | EMISIÓN | Historia | Finalizada | 2026-03-11 | 2026-04-23 | Andrea ORSINI | Juan Pablo Carubelli | 7 | 141.25 | 0 | 891.03 | No | — |
| WS-704 | EMISIÓN | Historia | Finalizada | 2026-03-11 | 2026-05-05 | Bethania | Luciana Rudaz | 3 | 318.18 | 0 | 1008.37 | No | — |
| WS-707 | EMISIÓN | Historia | Finalizada | 2026-03-11 | 2026-04-29 | Bethania | Luciana Rudaz | 3 | 317.35 | 0 | 872.21 | No | — |
| WS-708 | EMISIÓN | Historia | Finalizada | 2026-03-11 | 2026-04-13 | Bethania | Automation for Jira | 1 | 115.37 | 0 | 676.17 | No | — |
| WS-717 | EMISIÓN | Historia | Finalizada | 2026-03-11 | 2026-04-07 | Bethania | Luciana Rudaz | 1 | 186.6 | 0 | 458.42 | No | — |
| WS-720 | EMISIÓN | Historia | Finalizada | 2026-03-11 | 2026-05-19 | Bethania | Luciana Rudaz | 7 | 855.76 | 0 | 811.65 | No | — |
| WS-721 | EMISIÓN | Historia | Finalizada | 2026-03-11 | 2026-05-13 | Bethania | Luciana Rudaz | 15 | 799.03 | 0 | 719.93 | No | — |
| WS-722 | EMISIÓN | Historia | Finalizada | 2026-03-11 | 2026-05-29 | Andrea ORSINI | Nicolas Pomponio | 3 | 21.25 | 0 | 1884.39 | No | — |
| AD-832 | ADQUIRENCIA | Historia | Finalizada | 2026-03-12 | 2026-05-27 | Andrea ORSINI | Pablo Antonio GOMES | 1 | 189.93 | 0 | 1642.48 | No | — |
| WS-726 | EMISIÓN | Historia | Finalizada | 2026-03-12 | 2026-04-10 | Ana | Juan Pablo Carubelli | 7 | 65.37 | 0 | 628.77 | No | — |
| WS-727 | EMISIÓN | Historia | Finalizada | 2026-03-12 | 2026-03-16 | Ana | malzogaray | 0.5 | 0.28 | 0 | 100.32 | No | — |
| AD-837 | ADQUIRENCIA | Error | Finalizada | 2026-03-13 | 2026-04-23 | Bethania | Bethania | 0.5 | 170.15 | 3.35 | 289.05 | Sí | OBS |
| AD-838 | ADQUIRENCIA | Error | Finalizada | 2026-03-13 | 2026-03-26 | Bethania | Bethania | 0.5 | 21.92 | 0 | 288.08 | No | OBS |
| AD-839 | ADQUIRENCIA | Error | Finalizada | 2026-03-13 | 2026-04-10 | Bethania | Bethania | 0.25 | 71.25 | 103.32 | 497.1 | Sí | OBS |
| AD-841 | ADQUIRENCIA | Error | Finalizada | 2026-03-13 | 2026-05-07 | Bethania | Bethania | 0.5 | 717.15 | 0 | 597.23 | No | OBS |
| AD-842 | ADQUIRENCIA | Error | Finalizada | 2026-03-13 | 2026-04-10 | Bethania | Bethania | 0.5 | 24.9 | 3.53 | 286.17 | Sí | OBS |
| AD-843 | ADQUIRENCIA | Error | Finalizada | 2026-03-13 | 2026-04-24 | Ana | Ana | 3 | 22.67 | 72.9 | 905.38 | Sí | — |
| WS-730 | EMISIÓN | Historia | EN QA | 2026-03-13 | — | Ana | Luciana Rudaz | 7 | 759.74 | 164 | 2370.05 | Sí | — |
| WS-731 | EMISIÓN | Error | Finalizada | 2026-03-13 | 2026-04-27 | Andrea ORSINI | Andrea ORSINI | 0.5 | 334.37 | 99.5 | 639.05 | Sí | OBS/REQ |
| AD-845 | ADQUIRENCIA | Error | Finalizada | 2026-03-15 | 2026-05-13 | Bethania | Bethania | 1 | 86.82 | 151.35 | 555.67 | Sí | OBS |
| AD-851 | ADQUIRENCIA | Historia | Finalizada | 2026-03-16 | 2026-05-27 | Andrea ORSINI | Automation for Jira | 3 | 28.88 | 0 | 1698.25 | No | — |
| AD-855 | ADQUIRENCIA | Error | Finalizada | 2026-03-16 | 2026-07-21 | Ana | malzogaray | 1 | 424.13 | 2199.6 | 17.67 | Sí | — |
| AD-857 | ADQUIRENCIA | Error | Finalizada | 2026-03-16 | 2026-03-26 | Ana | Ana | 1 | 22.27 | 0 | 213.6 | No | — |
| AD-858 | ADQUIRENCIA | Error | Finalizada | 2026-03-16 | 2026-03-26 | Ana | Ana | 1 | 21.93 | 0.62 | 211.68 | Sí | — |
| WS-736 | EMISIÓN | Error | Finalizada | 2026-03-16 | 2026-04-07 | Nicolás Colón | Nicolás Colón | 0.5 | 18.2 | 0 | 509.33 | No | OBS |
| WS-738 | EMISIÓN | Error | Finalizada | 2026-03-16 | 2026-04-22 | Nicolás Colón | Nicolás Colón | 1 | 138.87 | 0 | 749.62 | No | OBS |
| WS-739 | EMISIÓN | Error | Finalizada | 2026-03-16 | 2026-03-31 | malzogaray | Nicolás Colón | 1 | 0.4 | 0 | 359.18 | No | OBS |
| AD-862 | ADQUIRENCIA | Error | Finalizada | 2026-03-17 | 2026-03-27 | Ana | Ana | 1 | 0.38 | 0 | 238.33 | No | — |
| WS-756 | EMISIÓN | Error | Finalizada | 2026-03-17 | 2026-03-27 | Nicolás Colón | malzogaray | 1 | 2.87 | 0 | 241.73 | No | OBS |
| WS-757 | EMISIÓN | Historia | Finalizada | 2026-03-17 | 2026-04-08 | Ana | malzogaray | 3 | 46.8 | 0 | 479.65 | No | OBS |
| WS-758 | EMISIÓN | Error | Finalizada | 2026-03-17 | 2026-04-13 | Nicolás Colón | Nicolás Colón | 0.5 | 29.87 | 311.22 | 310.6 | Sí | OBS |
| AD-870 | ADQUIRENCIA | Error | Finalizada | 2026-03-18 | 2026-03-25 | Andrea ORSINI | Andrea ORSINI | 1 | 0.52 | 0 | 161.4 | No | OBS |
| AD-871 | ADQUIRENCIA | Error | Finalizada | 2026-03-18 | 2026-03-25 | Andrea ORSINI | Andrea ORSINI | 1 | 1.27 | 0 | 165.75 | No | REQ |
| WS-771 | EMISIÓN | Historia | Finalizada | 2026-03-18 | 2026-04-10 | Bethania | malzogaray | 3 | 66.43 | 0 | 484.98 | No | — |
| WS-772 | EMISIÓN | Historia | Finalizada | 2026-03-18 | 2026-03-27 | Bethania | malzogaray | 0.5 | 5.53 | 0 | 212.77 | No | — |
| WS-777 | EMISIÓN | Error | Finalizada | 2026-03-18 | 2026-04-15 | Andrea ORSINI | malzogaray | 3 | 388.08 | 0 | 282.68 | No | — |
| AD-882 | ADQUIRENCIA | Error | Finalizada | 2026-03-19 | 2026-04-10 | Andrea ORSINI | Nicolás Colón | 3 | 216.67 | 0 | 310.98 | No | OBS |
| SER-54 | SERVICIOS | Historia | Finalizada | 2026-03-19 | 2026-03-27 | Nicolás Colón | Nicolás Colón | 2 | 5.47 | 0 | 189.17 | No | — |
| AD-898 | ADQUIRENCIA | Error | Finalizada | 2026-03-20 | 2026-03-25 | Andrea ORSINI | Andrea ORSINI | 1 | 0.02 | 0 | 114.9 | No | OBS |
| AD-899 | ADQUIRENCIA | Historia | Finalizada | 2026-03-20 | 2026-04-28 | Bethania | Nicolás Colón | 1 | 161.75 | 49.02 | 718.47 | Sí | — |
| WS-807 | EMISIÓN | Error | Finalizada | 2026-03-20 | 2026-03-27 | Nicolás Colón | Nicolás Colón | 1 | 6.73 | 0 | 166.35 | No | OBS |
| AD-913 | ADQUIRENCIA | Error | Finalizada | 2026-03-23 | 2026-05-27 | Andrea ORSINI | Andrea ORSINI | 1 | 191.17 | 0 | 1372.11 | No | OBS |
| AD-914 | ADQUIRENCIA | Error | Finalizada | 2026-03-23 | 2026-05-27 | Andrea ORSINI | Andrea ORSINI | 1 | 966.61 | 0 | 596.03 | No | OBS |
| WS-811 | EMISIÓN | Historia | Finalizada | 2026-03-23 | 2026-04-28 | Andrea ORSINI | Pablo Antonio GOMES | 14 | 278.38 | 116.82 | 590.75 | Sí | — |
| WS-815 | EMISIÓN | Historia | Finalizada | 2026-03-23 | 2026-05-26 | Bethania | Pablo Antonio GOMES | 7 | 290.73 | 0 | 1247.02 | No | — |
| WS-816 | EMISIÓN | Historia | EN QA | 2026-03-23 | — | Nicolás Colón | Pablo Antonio GOMES | 3 | 289.2 | 0 | 2688.84 | No | — |
| WS-817 | EMISIÓN | Historia | Finalizada | 2026-03-23 | 2026-05-19 | Bethania | Luciana Rudaz | 3 | 784.79 | 0 | 599.05 | No | — |
| WS-818 | EMISIÓN | Historia | Finalizada | 2026-03-23 | 2026-05-19 | Bethania | Luciana Rudaz | 7 | 823.98 | 0 | 554.9 | No | — |
| WS-819 | EMISIÓN | Historia | Finalizada | 2026-03-23 | 2026-05-19 | Bethania | Luciana Rudaz | 7 | 722.9 | 0 | 698.82 | No | — |
| AD-917 | ADQUIRENCIA | Error | Finalizada | 2026-03-25 | 2026-03-27 | Andrea ORSINI | Nicolás Colón | 1 | 4.08 | 0 | 46.22 | No | OBS |
| AD-919 | ADQUIRENCIA | Error | Finalizada | 2026-03-25 | 2026-03-25 | Nicolás Colón | Andrea ORSINI | — | 0 | 0 | 0.72 | No | DEF/OBS |
| AD-920 | ADQUIRENCIA | Error | Finalizada | 2026-03-25 | 2026-03-25 | Andrea ORSINI | Andrea ORSINI | — | 0 | 0 | 0.13 | No | DEF/OBS |
| AD-925 | ADQUIRENCIA | Error | Finalizada | 2026-03-25 | 2026-06-12 | Bethania | Nicolás Colón | 1 | 191.1 | 0 | 1710.98 | No | OBS/REQ |
| AD-939 | ADQUIRENCIA | Error | Finalizada | 2026-03-26 | 2026-03-27 | malzogaray | Andrea ORSINI | 0.25 | 0.37 | 0 | 21.45 | No | OBS |
| AD-941 | ADQUIRENCIA | Error | Finalizada | 2026-03-26 | 2026-03-27 | Andrea ORSINI | Andrea ORSINI | 1 | 0.8 | 0 | 20.68 | No | OBS |
| AD-942 | ADQUIRENCIA | Error | Finalizada | 2026-03-26 | 2026-03-30 | malzogaray | Andrea ORSINI | 1 | 6.73 | 65.08 | 16.28 | Sí | DEF/OBS |
| AD-943 | ADQUIRENCIA | Error | Finalizada | 2026-03-27 | 2026-03-27 | malzogaray | Andrea ORSINI | 1 | 1.73 | 0 | 5.3 | No | DEF/OBS |
| AD-945 | ADQUIRENCIA | Error | Finalizada | 2026-03-27 | 2026-04-17 | Bethania | Bethania | 3 | 4.4 | 0 | 502.3 | No | DEF/OBS |
| WS-840 | EMISIÓN | Error | Finalizada | 2026-03-27 | 2026-06-02 | Andrea ORSINI | Nicolás Colón | 0.5 | 334.77 | 0 | 1272.48 | No | OBS/REQ |
| AD-957 | ADQUIRENCIA | Historia | Finalizada | 2026-03-30 | 2026-06-29 | Andrea ORSINI | Nicolás Colón | 1 | 676.53 | 0 | 1520.71 | No | — |
| OB-108 | ONBOARDING | Historia | Finalizada | 2026-04-01 | 2026-05-19 | Andrea ORSINI | Andrea ORSINI | — | 1096.51 | 0 | 0 | No | — |
| OB-109 | ONBOARDING | Historia | Finalizada | 2026-04-01 | 2026-04-07 | Andrea ORSINI | Andrea ORSINI | — | 112.08 | 28.97 | 0.02 | Sí | — |
| WS-857 | EMISIÓN | Error | Finalizada | 2026-04-01 | 2026-05-20 | Ana | Ana | 0.25 | 25.23 | 0 | 1145.5 | No | OBS |
| AD-964 | ADQUIRENCIA | Historia | Finalizada | 2026-04-05 | 2026-07-03 | Bethania | Luciana Rudaz | 7 | 433.33 | 573.73 | 1133.81 | Sí | — |
| AD-965 | ADQUIRENCIA | Historia | Finalizada | 2026-04-05 | 2026-06-11 | Bethania | Luciana Rudaz | 7 | 137.17 | 0 | 1461.03 | No | — |
| AD-966 | ADQUIRENCIA | Historia | Finalizada | 2026-04-05 | 2026-06-11 | Bethania | Luciana Rudaz | 15 | 119.58 | 21.62 | 1471.58 | Sí | — |
| AD-968 | ADQUIRENCIA | Error | Finalizada | 2026-04-06 | 2026-04-06 | Andrea ORSINI | Andrea ORSINI | 3 | 5.18 | 0 | 1.18 | No | — |
| OB-111 | ONBOARDING | Error | Finalizada | 2026-04-06 | 2026-04-06 | Andrea ORSINI | Andrea ORSINI | — | 0.5 | 0 | 0.07 | No | — |
| WS-858 | EMISIÓN | Historia | Finalizada | 2026-04-06 | 2026-05-19 | Andrea ORSINI | Juan Pablo Carubelli | 7 | 0.18 | 0 | 1049.26 | No | — |
| WS-861 | EMISIÓN | Historia | Finalizada | 2026-04-06 | 2026-04-21 | Bethania | Luciana Rudaz | 1 | 91.13 | 0 | 265.42 | No | — |
| AD-971 | ADQUIRENCIA | Historia | Finalizada | 2026-04-07 | 2026-04-29 | Bethania | Nicolás Colón | 3 | 164.17 | 0 | 360.38 | No | — |
| WS-880 | EMISIÓN | Historia | Finalizada | 2026-04-07 | 2026-06-01 | Ana | Nicolás Colón | 3 | 129.45 | 139.85 | 1053.42 | Sí | — |
| WS-885 | EMISIÓN | Historia | Finalizada | 2026-04-08 | 2026-04-08 | Pablo Antonio GOMES | Andrea ORSINI | — | 1.93 | 0 | 0 | No | — |
| AD-976 | ADQUIRENCIA | Error | Finalizada | 2026-04-09 | 2026-04-10 | Andrea ORSINI | Andrea ORSINI | 3 | 19.72 | 0 | 5.62 | No | — |
| AD-977 | ADQUIRENCIA | Error | Finalizada | 2026-04-09 | 2026-04-17 | Andrea ORSINI | malzogaray | 3 | 3.3 | 91.43 | 93.82 | Sí | — |
| AD-978 | ADQUIRENCIA | Error | Finalizada | 2026-04-09 | 2026-04-14 | Andrea ORSINI | malzogaray | 1 | 8.37 | 0 | 94.58 | No | — |
| AD-981 | ADQUIRENCIA | Historia | EN QA | 2026-04-09 | — | Ana | Nicolás Colón | 3 | 1552.02 | 0 | 1054.82 | No | — |
| ARD-19 | ARDID | Error | Finalizada | 2026-04-09 | 2026-05-08 | Andrea ORSINI | Andrea ORSINI | — | 0.05 | 0 | 695.62 | No | — |
| AD-985 | ADQUIRENCIA | Historia | Finalizada | 2026-04-10 | 2026-04-20 | Andrea ORSINI | malzogaray | 3 | 169.63 | 0 | 75.87 | No | — |
| AD-988 | ADQUIRENCIA | Error | Finalizada | 2026-04-10 | 2026-05-12 | Bethania | Bethania | 1 | 2.75 | 0 | 768.23 | No | OBS |
| WS-900 | EMISIÓN | Error | Finalizada | 2026-04-10 | 2026-06-18 | malzogaray | Nicolás Colón | 3 | 699.12 | 19.47 | 946.69 | Sí | OBS |
| AD-989 | ADQUIRENCIA | Error | Finalizada | 2026-04-13 | 2026-05-28 | Bethania | Nicolás Colón | 3 | 336.75 | 18.3 | 727.25 | Sí | OBS |
| AD-991 | ADQUIRENCIA | Historia | Finalizada | 2026-04-13 | 2026-04-23 | Bethania | Automation for Jira | 3 | 47.53 | 0 | 192.58 | No | — |
| AD-996 | ADQUIRENCIA | Error | Finalizada | 2026-04-13 | 2026-04-17 | Andrea ORSINI | Andrea ORSINI | — | 0.72 | 0 | 90.62 | No | DEF/OBS |
| WS-908 | EMISIÓN | Error | Finalizada | 2026-04-13 | 2026-05-13 | Andrea ORSINI | Nicolás Colón | 3 | 24.1 | 0 | 691.65 | No | OBS |
| WS-911 | EMISIÓN | Historia | Finalizada | 2026-04-13 | 2026-04-14 | malzogaray | malzogaray | — | 0 | 0 | 23.52 | No | — |
| WS-912 | EMISIÓN | Historia | Finalizada | 2026-04-13 | 2026-04-14 | malzogaray | malzogaray | — | 0 | 0 | 23.42 | No | — |
| WS-913 | EMISIÓN | Historia | Finalizada | 2026-04-13 | 2026-04-14 | malzogaray | malzogaray | — | 0 | 0 | 23.35 | No | — |
| AD-998 | ADQUIRENCIA | Error | Finalizada | 2026-04-14 | 2026-05-20 | Ana | Ana | 1 | 381.68 | 0 | 484.95 | No | — |
| AD-999 | ADQUIRENCIA | Error | Finalizada | 2026-04-14 | 2026-04-17 | Andrea ORSINI | Nicolás Colón | 1 | 28.7 | 0 | 42.6 | No | DEF/OBS |
| AD-1005 | ADQUIRENCIA | Historia | Finalizada | 2026-04-15 | 2026-04-29 | Andrea ORSINI | Nicolás Colón | 1 | 122.13 | 0 | 221.23 | No | — |
| AD-1006 | ADQUIRENCIA | Error | Finalizada | 2026-04-15 | 2026-04-23 | Bethania | Nicolás Colón | — | 69.52 | 0 | 122.45 | No | OBS |
| AD-1010 | ADQUIRENCIA | Error | Finalizada | 2026-04-15 | 2026-07-02 | Bethania | Nicolás Colón | 3 | 27.98 | 0 | 1838.3 | No | OBS |
| SER-55 | SERVICIOS | Error | Finalizada | 2026-04-15 | 2026-04-30 | Nicolás Colón | Nicolás Colón | — | 0.13 | 0 | 357.78 | No | OBS |
| SER-56 | SERVICIOS | Error | Finalizada | 2026-04-15 | 2026-04-30 | Nicolás Colón | Nicolás Colón | — | 0.15 | 0 | 357.6 | No | OBS |
| WS-918 | EMISIÓN | Error | Finalizada | 2026-04-15 | 2026-04-24 | Ana | Nicolás Colón | 3 | 77.43 | 0 | 136.9 | No | OBS |
| AD-1019 | ADQUIRENCIA | Error | Finalizada | 2026-04-17 | 2026-04-23 | Andrea ORSINI | Nicolás Colón | 3 | 6.97 | 0 | 136.12 | No | OBS |
| WS-947 | EMISIÓN | Error | Finalizada | 2026-04-17 | 2026-04-23 | Bethania | Bethania | — | 0 | 0 | 144.43 | No | OBS |
| WS-948 | EMISIÓN | Error | Finalizada | 2026-04-17 | 2026-04-23 | Bethania | Bethania | 0.25 | 21.28 | 0 | 123 | No | OBS |
| OB-120 | ONBOARDING | Error | EN QA | 2026-04-20 | — | Andrea ORSINI | Andrea ORSINI | — | 666.23 | 0 | 1682.3 | No | DEF/OBS |
| WS-950 | EMISIÓN | Historia | EN QA | 2026-04-20 | — | Ana | malzogaray | 1 | 1577.34 | 0 | 768.75 | No | — |
| AD-1027 | ADQUIRENCIA | Error | Finalizada | 2026-04-21 | 2026-04-29 | Andrea ORSINI | Andrea ORSINI | 1 | 0.07 | 0 | 184.02 | No | DEF/OBS |
| OB-121 | ONBOARDING | Error | Finalizada | 2026-04-21 | 2026-06-25 | Andrea ORSINI | Andrea ORSINI | — | 1551.72 | 0 | 2.17 | No | — |
| SER-57 | SERVICIOS | Error | Finalizada | 2026-04-21 | 2026-04-21 | Nicolás Colón | Nicolás Colón | — | 0 | 0 | 2.97 | No | OBS/REQ |
| SER-58 | SERVICIOS | Historia | Finalizada | 2026-04-21 | 2026-07-23 | Nicolás Colón | Nicolás Colón | 3 | 2018.4 | 0 | 211.52 | No | — |
| SER-59 | SERVICIOS | Error | Finalizada | 2026-04-21 | 2026-04-21 | Nicolás Colón | Nicolás Colón | — | 0.15 | 0 | 4.5 | No | OBS |
| WS-953 | EMISIÓN | Historia | Finalizada | 2026-04-21 | 2026-06-01 | Andrea ORSINI | Automation for Jira | 3 | 147.77 | 0.33 | 853.46 | Sí | — |
| WS-972 | EMISIÓN | Historia | Finalizada | 2026-04-21 | 2026-06-01 | malzogaray | Pablo Antonio GOMES | 3 | 138.18 | 0 | 696.82 | No | — |
| AD-1029 | ADQUIRENCIA | Error | Finalizada | 2026-04-22 | 2026-07-21 | malzogaray | malzogaray | 7 | 0 | 0 | 2159.67 | No | OBS |
| AD-1038 | ADQUIRENCIA | Error | Finalizada | 2026-04-22 | 2026-05-19 | Ana | Nicolás Colón | 3 | 166.48 | 7.63 | 479.55 | Sí | OBS |
| AD-1039 | ADQUIRENCIA | Error | Finalizada | 2026-04-22 | 2026-07-27 | Bethania | Nicolás Colón | — | 65.53 | 0 | 172.82 | No | OBS |
| WS-978 | EMISIÓN | Historia | Finalizada | 2026-04-22 | 2026-06-01 | Bethania | Automation for Jira | 3 | 403.32 | 0 | 558.67 | No | — |
| WS-982 | EMISIÓN | Error | Finalizada | 2026-04-22 | 2026-05-20 | Bethania | Bethania | 0.25 | 54.82 | 0 | 624.25 | No | OBS |
| WS-984 | EMISIÓN | Error | Finalizada | 2026-04-22 | 2026-05-19 | Ana | Automation for Jira | 0.25 | 270.77 | 0 | 380.05 | No | OBS |
| WS-985 | EMISIÓN | Historia | Finalizada | 2026-04-22 | 2026-05-22 | Ana | Automation for Jira | 1 | 44.12 | 0 | 671.37 | No | — |
| AD-1059 | ADQUIRENCIA | Error | Finalizada | 2026-04-24 | 2026-05-27 | Bethania | malzogaray | 3 | 188.67 | 18.83 | 583.07 | Sí | — |
| AD-1060 | ADQUIRENCIA | Error | Finalizada | 2026-04-24 | 2026-04-24 | Andrea ORSINI | Nicolás Colón | — | 3.17 | 0.87 | 2.8 | Sí | — |
| WS-1003 | EMISIÓN | Error | Finalizada | 2026-04-24 | 2026-04-27 | Ana | Ana | 0.25 | 7.3 | 0 | 68.95 | No | OBS |
| WS-987 | EMISIÓN | Error | Finalizada | 2026-04-24 | 2026-04-27 | Ana | Nicolás Colón | 0.25 | 4.88 | 0 | 70.98 | No | OBS |
| WS-990 | EMISIÓN | Error | Finalizada | 2026-04-24 | 2026-06-01 | Andrea ORSINI | Nicolás Colón | 3 | 319.05 | 0 | 599.75 | No | OBS |
| WS-1023 | EMISIÓN | Historia | Finalizada | 2026-04-28 | 2026-05-05 | Andrea ORSINI | malzogaray | 0.5 | 0.02 | 0 | 168 | No | — |
| WS-1024 | EMISIÓN | Historia | Finalizada | 2026-04-28 | 2026-05-15 | Bethania | Luciana Rudaz | 3 | 26.03 | 0 | 383.6 | No | — |
| AD-1096 | ADQUIRENCIA | Error | Finalizada | 2026-04-29 | 2026-05-27 | Bethania | Nicolás Colón | 3 | 27.77 | 0 | 643.1 | No | OBS |
| WS-1027 | EMISIÓN | Historia | Finalizada | 2026-04-29 | 2026-05-26 | Ana | Automation for Jira | 3 | 168.45 | 140.85 | 512.78 | Sí | — |
| WS-1037 | EMISIÓN | Historia | Finalizada | 2026-04-29 | 2026-07-14 | Bethania | Pablo Antonio GOMES | 7 | 800.19 | 0 | 1043.88 | No | — |
| WS-1041 | EMISIÓN | Error | Finalizada | 2026-04-29 | 2026-05-04 | Andrea ORSINI | Nicolás Colón | 0.5 | 1.27 | 0 | 117.3 | No | OBS |
| WS-1042 | EMISIÓN | Error | Finalizada | 2026-04-29 | 2026-05-04 | Andrea ORSINI | Nicolás Colón | 0.5 | 0.57 | 0 | 117.17 | No | OBS |
| WS-1043 | EMISIÓN | Historia | Finalizada | 2026-04-30 | 2026-05-20 | Bethania | Nicolás Colón | 1 | 26.13 | 0.43 | 459.27 | Sí | — |
| WS-1044 | EMISIÓN | Historia | Finalizada | 2026-04-30 | 2026-07-06 | Bethania | Nicolás Colón | 3 | 118.73 | 0 | 1506.44 | No | — |
| WS-1045 | EMISIÓN | Historia | Finalizada | 2026-04-30 | 2026-05-15 | Bethania | Luciana Rudaz | 3 | 7 | 0 | 355.07 | No | — |
| WS-1048 | EMISIÓN | Historia | Finalizada | 2026-04-30 | 2026-05-19 | Bethania | Luciana Rudaz | 3 | 96.57 | 0 | 361.33 | No | — |
| AD-1103 | ADQUIRENCIA | Error | EN QA | 2026-05-04 | — | Andrea ORSINI | Nicolás Colón | 1 | 723.88 | 522.75 | 762.68 | Sí | — |
| WS-1050 | EMISIÓN | Historia | Finalizada | 2026-05-04 | 2026-07-13 | Bethania | Automation for Jira | 3 | 147.98 | 0 | 1547.79 | No | — |
| WS-1052 | EMISIÓN | Historia | Finalizada | 2026-05-04 | 2026-05-22 | Andrea ORSINI | malzogaray | 3 | 29.47 | 0 | 408.97 | No | — |
| AD-1104 | ADQUIRENCIA | Error | Finalizada | 2026-05-05 | 2026-05-06 | Andrea ORSINI | Andrea ORSINI | 1 | 24.2 | 0 | 0 | No | — |
| AD-1105 | ADQUIRENCIA | Error | Finalizada | 2026-05-05 | 2026-07-14 | Bethania | Nicolás Colón | 0.5 | 4.17 | 0 | 1672.72 | No | — |
| AD-1107 | ADQUIRENCIA | Error | Finalizada | 2026-05-05 | 2026-05-28 | Ana | Nicolás Colón | 1 | 52.75 | 18.57 | 329.12 | Sí | — |
| OB-122 | ONBOARDING | Error | Finalizada | 2026-05-05 | 2026-05-07 | Andrea ORSINI | Andrea ORSINI | — | 54.7 | 0 | 0 | No | — |
| OB-123 | ONBOARDING | Error | Finalizada | 2026-05-05 | 2026-05-06 | Andrea ORSINI | Andrea ORSINI | — | 24.52 | 0 | 0 | No | — |
| OB-126 | ONBOARDING | Error | Finalizada | 2026-05-06 | 2026-05-07 | Andrea ORSINI | Andrea ORSINI | — | 0.4 | 0 | 24.92 | No | — |
| OB-127 | ONBOARDING | Error | Finalizada | 2026-05-06 | 2026-05-20 | Andrea ORSINI | Andrea ORSINI | — | 0.95 | 24.08 | 309.67 | Sí | — |
| AD-1110 | ADQUIRENCIA | Error | Finalizada | 2026-05-07 | 2026-06-30 | Andrea ORSINI | Nicolás Colón | 3 | 19.72 | 0 | 1289.94 | No | REQ |
| AD-1114 | ADQUIRENCIA | Error | Finalizada | 2026-05-07 | 2026-05-14 | Bethania | Bethania | 1 | 22.8 | 0 | 143.73 | No | OBS |
| AD-1117 | ADQUIRENCIA | Error | Finalizada | 2026-05-07 | 2026-05-15 | Bethania | Bethania | 0.5 | 16.92 | 55.57 | 116.05 | Sí | OBS |
| AD-1118 | ADQUIRENCIA | Error | Finalizada | 2026-05-07 | 2026-05-12 | Bethania | Bethania | 0.5 | 0.42 | 0 | 115.33 | No | OBS |
| AD-1119 | ADQUIRENCIA | Error | Finalizada | 2026-05-07 | 2026-05-12 | Bethania | Bethania | 0.25 | 0.52 | 0 | 114.53 | No | OBS |
| AD-1120 | ADQUIRENCIA | Error | Finalizada | 2026-05-07 | 2026-05-12 | Bethania | Bethania | 0.25 | 0.73 | 0 | 111.88 | No | OBS |
| AD-1121 | ADQUIRENCIA | Error | Finalizada | 2026-05-07 | 2026-05-12 | Bethania | Bethania | 0.25 | 0.77 | 0 | 111.78 | No | OBS |
| ARD-20 | ARDID | Historia | Finalizada | 2026-05-07 | 2026-05-07 | Andrea ORSINI | Andrea ORSINI | — | 1.35 | 0 | 1.28 | No | — |
| WS-1074 | EMISIÓN | Historia | Finalizada | 2026-05-07 | 2026-05-12 | Ana | Automation for Jira | 1 | 26.22 | 0 | 96.45 | No | — |
| ARD-23 | ARDID | Historia | Finalizada | 2026-05-08 | 2026-06-05 | Andrea ORSINI | Andrea ORSINI | — | 606.17 | 0 | 66.3 | No | — |
| WS-1077 | EMISIÓN | Error | Finalizada | 2026-05-08 | 2026-06-29 | Bethania | Nicolás Colón | 0.5 | 71.45 | 0 | 1191.59 | No | OBS/REQ |
| WS-1078 | EMISIÓN | Error | Finalizada | 2026-05-08 | 2026-07-13 | Ana | Nicolás Colón | 1 | 578.32 | 45.12 | 975.86 | Sí | OBS/REQ |
| AD-1123 | ADQUIRENCIA | Error | Finalizada | 2026-05-11 | 2026-07-02 | malzogaray | Nicolás Colón | 3 | 28.35 | 455.05 | 1234.09 | Sí | — |
| AD-1124 | ADQUIRENCIA | Historia | Con defecto | 2026-05-11 | — | Bethania | Andrea ORSINI | — | 1841.39 | 0.02 | 0 | Sí | — |
| AD-1125 | ADQUIRENCIA | Error | Finalizada | 2026-05-11 | 2026-05-11 | Andrea ORSINI | Andrea ORSINI | — | 0.08 | 0 | 2.52 | No | DEF/OBS |
| OB-130 | ONBOARDING | Error | Finalizada | 2026-05-11 | 2026-05-13 | Andrea ORSINI | Andrea ORSINI | — | 50.98 | 0 | 0 | No | — |
| OB-131 | ONBOARDING | Error | Finalizada | 2026-05-11 | 2026-05-15 | malzogaray | Andrea ORSINI | — | 0 | 0 | 98.1 | No | OBS |
| AD-1128 | ADQUIRENCIA | Error | Finalizada | 2026-05-12 | 2026-05-20 | Bethania | Nicolás Colón | 3 | 23.8 | 0 | 168.07 | No | — |
| AD-1129 | ADQUIRENCIA | Error | Finalizada | 2026-05-12 | 2026-05-14 | Bethania | Bethania | 3 | 23.33 | 0 | 24 | No | OBS |
| AD-1130 | ADQUIRENCIA | Error | Finalizada | 2026-05-12 | 2026-05-14 | Bethania | Bethania | 0.5 | 22.82 | 0 | 23.67 | No | OBS |
| OB-132 | ONBOARDING | Error | Finalizada | 2026-05-12 | 2026-05-12 | Andrea ORSINI | Andrea ORSINI | — | 0.13 | 0 | 0 | No | — |
| WS-1082 | EMISIÓN | Historia | Finalizada | 2026-05-12 | 2026-05-26 | Ana | Automation for Jira | 3 | 35.55 | 0 | 334.37 | No | — |
| AD-1131 | ADQUIRENCIA | Error | Finalizada | 2026-05-13 | 2026-05-15 | Bethania | Bethania | 0.25 | 24.33 | 0 | 18.57 | No | DEF/OBS |
| AD-1132 | ADQUIRENCIA | Error | Finalizada | 2026-05-14 | 2026-05-18 | Bethania | Bethania | 0.5 | 74.33 | 0 | 25.88 | No | DEF/OBS |
| AD-1133 | ADQUIRENCIA | Error | Finalizada | 2026-05-14 | 2026-05-15 | Bethania | Bethania | 0.5 | 6.67 | 0 | 24.73 | No | DEF/OBS |
| AD-1138 | ADQUIRENCIA | Historia | Finalizada | 2026-05-15 | 2026-05-26 | Andrea ORSINI | Nicolás Colón | 3 | 142.47 | 0 | 127.4 | No | — |
| AD-1139 | ADQUIRENCIA | Historia | EN QA | 2026-05-15 | — | Andrea ORSINI | Nicolás Colón | 3 | 309.72 | 0 | 1453.78 | No | — |
| AD-1140 | ADQUIRENCIA | Historia | Finalizada | 2026-05-15 | 2026-07-14 | Nicolás Colón | Nicolás Colón | 3 | 189.75 | 0 | 1258.79 | No | — |
| OB-136 | ONBOARDING | Error | Finalizada | 2026-05-15 | 2026-06-08 | Andrea ORSINI | Andrea ORSINI | — | 72.98 | 0 | 503.03 | No | — |
| OB-137 | ONBOARDING | Error | Finalizada | 2026-05-15 | 2026-06-08 | Andrea ORSINI | Andrea ORSINI | — | 73.38 | 0 | 500.82 | No | — |
| OB-138 | ONBOARDING | Error | Finalizada | 2026-05-15 | 2026-06-09 | Andrea ORSINI | Andrea ORSINI | — | 78.8 | 25.3 | 500.88 | Sí | — |
| OB-139 | ONBOARDING | Error | Finalizada | 2026-05-15 | 2026-06-08 | Andrea ORSINI | Andrea ORSINI | — | 73.53 | 0 | 500.67 | No | — |
| OB-140 | ONBOARDING | Error | Finalizada | 2026-05-15 | 2026-05-15 | Andrea ORSINI | Andrea ORSINI | — | 0.47 | 0 | 0 | No | — |
| AD-1145 | ADQUIRENCIA | Error | Finalizada | 2026-05-18 | 2026-05-21 | Andrea ORSINI | Andrea ORSINI | — | 1.62 | 0 | 68.62 | No | DEF/OBS |
| ARD-27 | ARDID | Historia | Finalizada | 2026-05-19 | 2026-05-19 | Andrea ORSINI | Andrea ORSINI | — | 2.3 | 0 | 0.05 | No | — |
| OB-142 | ONBOARDING | Error | Finalizada | 2026-05-19 | 2026-05-19 | Andrea ORSINI | Andrea ORSINI | — | 1.15 | 0 | 0.02 | No | DEF |
| OB-144 | ONBOARDING | Error | Finalizada | 2026-05-19 | 2026-06-08 | Andrea ORSINI | Andrea ORSINI | — | 73.55 | 0 | 403.8 | No | — |
| OB-145 | ONBOARDING | Error | Finalizada | 2026-05-19 | 2026-06-08 | Andrea ORSINI | Andrea ORSINI | — | 26.8 | 450.17 | 0 | Sí | — |
| WS-1139 | EMISIÓN | Error | Finalizada | 2026-05-19 | 2026-06-10 | Andrea ORSINI | Nicolás Colón | 1 | 50.55 | 0 | 484.97 | No | OBS |
| WS-1159 | EMISIÓN | Historia | Finalizada | 2026-05-20 | 2026-05-20 | Andrea ORSINI | Andrea ORSINI | — | 0 | 0 | 0.03 | No | — |
| WS-1177 | EMISIÓN | Historia | Finalizada | 2026-05-20 | 2026-06-10 | Ana | Nicolás Colón | 3 | 127 | 16.68 | 352.33 | Sí | — |
| OB-149 | ONBOARDING | Historia | EN QA | 2026-05-22 | — | Unassigned | Automation for Jira | — | 306.6 | 0 | 920.94 | No | — |
| OB-150 | ONBOARDING | Historia | Finalizada | 2026-05-22 | 2026-06-09 | Andrea ORSINI | Automation for Jira | — | 27.8 | 0 | 408.12 | No | — |
| WS-1195 | EMISIÓN | Historia | Finalizada | 2026-05-22 | 2026-06-04 | Andrea ORSINI | Automation for Jira | 3 | 137.98 | 0 | 167.82 | No | — |
| WS-1202 | EMISIÓN | Error | Finalizada | 2026-05-26 | 2026-06-01 | Ana | Ana | 0.5 | 5.93 | 0 | 139.7 | No | — |
| WS-1206 | EMISIÓN | Error | Finalizada | 2026-05-26 | 2026-07-14 | Andrea ORSINI | Nicolás Colón | 3 | 1.92 | 0 | 1149.43 | No | — |
| AD-1197 | ADQUIRENCIA | Error | Finalizada | 2026-05-27 | 2026-05-28 | Andrea ORSINI | Andrea ORSINI | — | 15.22 | 0 | 12.42 | No | — |
| AD-1204 | ADQUIRENCIA | Error | Finalizada | 2026-05-27 | 2026-05-27 | malzogaray | Ana | — | 0 | 0 | 0.93 | No | — |
| OB-152 | ONBOARDING | Historia | Finalizada | 2026-05-27 | 2026-06-08 | Andrea ORSINI | Automation for Jira | — | 1.28 | 0 | 288.42 | No | — |
| OB-153 | ONBOARDING | Historia | Finalizada | 2026-05-28 | 2026-06-08 | Andrea ORSINI | Automation for Jira | — | 1.38 | 0 | 261.98 | No | — |
| OB-154 | ONBOARDING | Historia | Finalizada | 2026-05-28 | 2026-06-09 | Andrea ORSINI | Automation for Jira | — | 146.53 | 0 | 142.27 | No | — |
| OB-155 | ONBOARDING | Historia | EN QA | 2026-05-28 | — | Unassigned | Automation for Jira | — | 306.6 | 0 | 760.6 | No | — |
| AD-1217 | ADQUIRENCIA | Error | Finalizada | 2026-05-29 | 2026-06-17 | Ana | Nicolás Colón | 1 | 52.03 | 115.2 | 284.32 | Sí | OBS |
| AD-1219 | ADQUIRENCIA | Historia | Finalizada | 2026-05-29 | 2026-06-12 | Andrea ORSINI | Nicolás Colón | 1 | 27.32 | 0 | 310.45 | No | — |
| WS-1217 | EMISIÓN | Historia | Finalizada | 2026-05-29 | 2026-07-13 | Nicolás Colón | Nicolás Colón | 3 | 169.18 | 0 | 913.35 | No | — |
| OB-156 | ONBOARDING | Historia | Finalizada | 2026-06-01 | 2026-06-08 | Andrea ORSINI | Automation for Jira | — | 72.7 | 0 | 31.17 | No | — |
| WS-1242 | EMISIÓN | Error | Finalizada | 2026-06-02 | 2026-06-09 | Andrea ORSINI | Nicolás Colón | 1 | 22.67 | 0 | 147.33 | No | OBS |
| WS-1243 | EMISIÓN | Error | Finalizada | 2026-06-02 | 2026-06-09 | Ana | Ana | 1 | 94.85 | 0 | 70.67 | No | — |
| AD-1229 | ADQUIRENCIA | Error | EN QA | 2026-06-03 | — | Ana | Nicolás Colón | 1 | 307.35 | 0 | 999.86 | No | — |
| WS-1246 | EMISIÓN | Error | Finalizada | 2026-06-03 | 2026-06-10 | Bethania | Nicolás Colón | 0.5 | 48.57 | 0 | 118.02 | No | OBS |
| AD-1234 | ADQUIRENCIA | Error | Finalizada | 2026-06-04 | 2026-07-24 | Bethania | Bethania | 3 | 2.87 | 0 | 1213.16 | No | DEF/OBS |
| AD-1237 | ADQUIRENCIA | Error | Finalizada | 2026-06-04 | 2026-07-14 | Bethania | Bethania | 0.5 | 4.43 | 0 | 970.78 | No | DEF/OBS |
| AD-1239 | ADQUIRENCIA | Error | Finalizada | 2026-06-05 | 2026-06-09 | Bethania | Bethania | 1 | 68.8 | 27 | 6.08 | Sí | OBS |
| AD-1240 | ADQUIRENCIA | Error | Finalizada | 2026-06-05 | 2026-07-23 | Bethania | Nicolás Colón | 3 | 51.6 | 0 | 1114.38 | No | — |
| WS-1249 | EMISIÓN | Historia | Finalizada | 2026-06-05 | 2026-07-08 | Nicolás Colón | Nicolás Colón | 3 | 0 | 0 | 789.85 | No | — |
| WS-1250 | EMISIÓN | Historia | Finalizada | 2026-06-05 | 2026-06-10 | Ana | Automation for Jira | 3 | 51.6 | 0 | 71.55 | No | — |
| AD-1251 | ADQUIRENCIA | Error | Finalizada | 2026-06-08 | 2026-06-11 | Bethania | Bethania | 0.5 | 21.82 | 0 | 43.28 | No | OBS |
| WS-1252 | EMISIÓN | Historia | Finalizada | 2026-06-08 | 2026-07-06 | Bethania | Nicolás Colón | 3 | 241.32 | 0 | 435.28 | No | OBS |
| WS-1254 | EMISIÓN | Error | Finalizada | 2026-06-08 | 2026-06-10 | Bethania | Nicolás Colón | 3 | 25.08 | 4.37 | 17.33 | Sí | — |
| AD-1262 | ADQUIRENCIA | Error | Finalizada | 2026-06-09 | 2026-06-16 | Bethania | Bethania | 3 | 0.9 | 0.33 | 163.43 | Sí | OBS |
| SER-62 | SERVICIOS | Historia | Finalizada | 2026-06-11 | 2026-07-23 | Juan Pablo Carubelli | Nicolás Colón | — | 388.58 | 0 | 623.23 | No | — |
| WS-1267 | EMISIÓN | Historia | Finalizada | 2026-06-11 | 2026-06-11 | Ana | Automation for Jira | 0.5 | 1.95 | 0 | 0.55 | No | — |
| AD-1314 | ADQUIRENCIA | Error | Finalizada | 2026-06-12 | 2026-06-17 | Ana | Ana | 1 | 18.98 | 0 | 97.72 | No | OBS |
| AD-1316 | ADQUIRENCIA | Error | Finalizada | 2026-06-12 | 2026-06-24 | Bethania | Luciana Rudaz | 1 | 168.98 | 0 | 117.12 | No | OBS |
| OB-175 | ONBOARDING | Error | Finalizada | 2026-06-12 | 2026-07-16 | Bethania | Andrea ORSINI | — | 68.73 | 0 | 746.72 | No | DEF/OBS |
| WS-1277 | EMISIÓN | Historia | Finalizada | 2026-06-12 | 2026-07-03 | Andrea ORSINI | Pablo Antonio GOMES | 1 | 55.78 | 0 | 459.03 | No | — |
| AD-1320 | ADQUIRENCIA | Error | Finalizada | 2026-06-16 | 2026-06-18 | Andrea ORSINI | Nicolás Colón | 1 | 5.18 | 0 | 47.1 | No | — |
| WS-1280 | EMISIÓN | Historia | Finalizada | 2026-06-16 | 2026-06-30 | Andrea ORSINI | Automation for Jira | 3 | 3.87 | 0 | 339.98 | No | — |
| AD-1328 | ADQUIRENCIA | Historia | EN QA | 2026-06-17 | — | Andrea ORSINI | Andrea ORSINI | — | 968.08 | 0 | 0.27 | No | — |
| AD-1329 | ADQUIRENCIA | Error | Finalizada | 2026-06-17 | 2026-07-01 | Andrea ORSINI | Andrea ORSINI | 1 | 24.25 | 0.03 | 24.78 | Sí | OBS |
| AD-1331 | ADQUIRENCIA | Error | EN QA | 2026-06-17 | — | Andrea ORSINI | Andrea ORSINI | 1 | 941.31 | 0 | 24.25 | No | DEF/OBS |
| AD-1332 | ADQUIRENCIA | Error | Finalizada | 2026-06-17 | 2026-06-19 | Andrea ORSINI | Andrea ORSINI | 1 | 24.77 | 0 | 23 | No | DEF/OBS |
| WS-1284 | EMISIÓN | Historia | EN QA | 2026-06-17 | — | Ana | Automation for Jira | 3 | 643.48 | 0 | 317.27 | No | — |
| WS-1285 | EMISIÓN | Error | EN QA | 2026-06-17 | — | Andrea ORSINI | Nicolás Colón | 1 | 160.3 | 0 | 806.59 | No | REQ |
| SER-63 | SERVICIOS | Error | Finalizada | 2026-06-18 | 2026-07-06 | Nicolás Colón | Nicolás Colón | — | 2.28 | 0 | 427.73 | No | OBS |
| WS-1289 | EMISIÓN | Historia | Finalizada | 2026-06-18 | 2026-06-18 | Andrea ORSINI | Automation for Jira | 0.25 | 0.5 | 0 | 1.87 | No | — |
| WS-1292 | EMISIÓN | Historia | Finalizada | 2026-06-19 | 2026-07-13 | Bethania | Automation for Jira | 3 | 270.33 | 0 | 312.4 | No | — |
| WS-1296 | EMISIÓN | Historia | Finalizada | 2026-06-19 | 2026-07-07 | Bethania | Nicolás Colón | 1 | 120.53 | 0 | 314.65 | No | — |
| WS-1298 | EMISIÓN | Historia | Finalizada | 2026-06-23 | 2026-07-20 | Andrea ORSINI | Automation for Jira | 0.25 | 1.05 | 0 | 648.78 | No | — |
| WS-1300 | EMISIÓN | Historia | Finalizada | 2026-06-24 | 2026-07-07 | Bethania | Luciana Rudaz | 3 | 25.28 | 0 | 293.43 | No | — |
| WS-1303 | EMISIÓN | Error | Finalizada | 2026-06-25 | 2026-07-07 | Ana | Ana | 0.5 | 25.4 | 0 | 260.83 | No | OBS |
| WS-1304 | EMISIÓN | Error | Finalizada | 2026-06-25 | 2026-07-07 | Ana | Ana | 0.5 | 25.78 | 0 | 259.97 | No | OBS |
| WS-1305 | EMISIÓN | Error | Finalizada | 2026-06-25 | 2026-07-07 | Ana | Ana | 0.5 | 25.03 | 0 | 259.75 | No | — |
| WS-1306 | EMISIÓN | Error | Finalizada | 2026-06-25 | 2026-07-07 | Ana | Ana | 0.5 | 25.05 | 0 | 258.97 | No | — |
| AD-1348 | ADQUIRENCIA | Error | Finalizada | 2026-06-26 | 2026-07-01 | Ana | Pablo Antonio GOMES | — | 50.95 | 0 | 95.77 | No | — |
| WS-1309 | EMISIÓN | Historia | Finalizada | 2026-06-26 | 2026-07-13 | Andrea ORSINI | Automation for Jira | 1 | 0.03 | 0 | 409.4 | No | — |
| WS-1311 | EMISIÓN | Historia | Finalizada | 2026-06-26 | 2026-07-14 | malzogaray | Pablo Antonio GOMES | — | 0 | 0 | 429.6 | No | — |
| OB-181 | ONBOARDING | Error | Bloqueado | 2026-06-29 | — | malzogaray | Pablo Antonio GOMES | — | 1.83 | 0 | 262.1 | No | OBS |
| OB-182 | ONBOARDING | Error | Bloqueado | 2026-06-29 | — | Andrea ORSINI | Pablo Antonio GOMES | — | 44.67 | 0 | 384.57 | No | OBS |
| OB-183 | ONBOARDING | Historia | Bloqueado | 2026-06-29 | — | Andrea ORSINI | Pablo Antonio GOMES | — | 44.55 | 0 | 384.67 | No | REQ |
| OB-184 | ONBOARDING | Error | Bloqueado | 2026-06-29 | — | malzogaray | Pablo Antonio GOMES | — | 1.43 | 0 | 262.52 | No | OBS |
| OB-185 | ONBOARDING | Historia | Bloqueado | 2026-06-29 | — | Andrea ORSINI | Pablo Antonio GOMES | — | 44.37 | 0 | 384.85 | No | REQ |
| OB-186 | ONBOARDING | Error | Finalizada | 2026-06-29 | 2026-07-08 | malzogaray | Pablo Antonio GOMES | — | 0 | 0 | 214.37 | No | OBS |
| OB-187 | ONBOARDING | Error | Bloqueado | 2026-06-29 | — | malzogaray | Pablo Antonio GOMES | — | 0.83 | 0 | 263.13 | No | OBS |
| OB-188 | ONBOARDING | Error | Bloqueado | 2026-06-29 | — | malzogaray | Pablo Antonio GOMES | — | 0.77 | 0 | 263.18 | No | OBS |
| OB-189 | ONBOARDING | Error | Bloqueado | 2026-06-29 | — | malzogaray | Pablo Antonio GOMES | — | 0.48 | 0 | 263.48 | No | OBS |
| OB-191 | ONBOARDING | Error | Finalizada | 2026-06-29 | 2026-07-08 | malzogaray | Pablo Antonio GOMES | — | 0 | 0 | 214.37 | No | OBS |
| WS-1315 | EMISIÓN | Error | EN QA | 2026-06-29 | — | Ana | Ana | 0.5 | 117.95 | 0 | 552.53 | No | OBS |
| WS-1317 | EMISIÓN | Error | EN QA | 2026-06-29 | — | Ana | Ana | 1 | 117.95 | 0 | 547.97 | No | — |
| AD-1352 | ADQUIRENCIA | Error | EN QA | 2026-06-30 | — | Ana | Nicolás Colón | 3 | 140.43 | 0 | 507.13 | No | OBS |
| SER-64 | SERVICIOS | Historia | Finalizada | 2026-07-01 | 2026-07-01 | Juan Pablo Carubelli | Juan Pablo Carubelli | — | 2.87 | 0 | 0.13 | No | OBS |
| WS-1324 | EMISIÓN | Error | Finalizada | 2026-07-01 | 2026-07-08 | Ana | Ana | 1 | 43.4 | 0 | 122.12 | No | — |
| AD-1366 | ADQUIRENCIA | Error | Finalizada | 2026-07-02 | 2026-07-02 | Bethania | Andrea ORSINI | — | 0.72 | 0 | 1.47 | No | — |
| AD-1368 | ADQUIRENCIA | Error | EN QA | 2026-07-02 | — | Ana | Ana | 1 | 72.03 | 0 | 524.62 | No | — |
| AD-1373 | ADQUIRENCIA | Error | Finalizada | 2026-07-03 | 2026-07-06 | Andrea ORSINI | Andrea ORSINI | — | 0 | 0 | 5.52 | No | DEF |
| ARD-32 | ARDID | Error | Finalizada | 2026-07-03 | 2026-07-03 | Andrea ORSINI | malzogaray | — | 1.1 | 0 | 0.05 | No | — |
| WS-1364 | EMISIÓN | Historia | Finalizada | 2026-07-08 | 2026-07-21 | Ana | Automation for Jira | — | 89.3 | 0 | 221.35 | No | — |
| AD-1397 | ADQUIRENCIA | Error | Finalizada | 2026-07-15 | 2026-07-20 | Andrea ORSINI | Andrea ORSINI | — | 0.12 | 0 | 116.15 | No | DEF/OBS |
| WS-1387 | EMISIÓN | Historia | Finalizada | 2026-07-15 | 2026-07-15 | Andrea ORSINI | Automation for Jira | — | 0.5 | 0 | 2.85 | No | — |
| WS-1388 | EMISIÓN | Historia | Finalizada | 2026-07-15 | 2026-07-15 | Andrea ORSINI | Automation for Jira | — | 0.27 | 0 | 2.78 | No | — |
| WS-1389 | EMISIÓN | Error | Finalizada | 2026-07-15 | 2026-07-20 | Bethania | Nicolás Colón | 1 | 65.75 | 0 | 53.75 | No | — |
| WS-1394 | EMISIÓN | Historia | Finalizada | 2026-07-16 | 2026-07-21 | Bethania | malzogaray | 0.5 | 21.43 | 0 | 98.9 | No | — |
| WS-1395 | EMISIÓN | Error | Finalizada | 2026-07-17 | 2026-07-17 | Bethania | malzogaray | 0.5 | 1.53 | 0 | 5.93 | No | — |
| AD-1420 | ADQUIRENCIA | Error | Finalizada | 2026-07-20 | 2026-07-22 | Andrea ORSINI | malzogaray | — | 16.3 | 0 | 23.12 | No | — |
| AD-1418 | ADQUIRENCIA | Error | Finalizada | 2026-07-21 | 2026-07-23 | Andrea ORSINI | Andrea ORSINI | — | 2.22 | 0 | 50.63 | No | OBS |
| WS-1413 | EMISIÓN | Historia | Finalizada | 2026-07-21 | 2026-07-22 | Andrea ORSINI | Automation for Jira | 0.25 | 23.22 | 0 | 4.98 | No | — |
| AD-1426 | ADQUIRENCIA | Error | Finalizada | 2026-07-22 | 2026-07-23 | Andrea ORSINI | Andrea ORSINI | — | 2.95 | 0 | 23.75 | No | OBS |
| WS-1417 | EMISIÓN | Error | Finalizada | 2026-07-22 | 2026-07-22 | Andrea ORSINI | malzogaray | — | 5.02 | 0 | 0.12 | No | — |

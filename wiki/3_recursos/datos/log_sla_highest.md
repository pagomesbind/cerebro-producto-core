# Log de SLA de tickets Highest — Base de datos de la métrica "tiempo de resolución de urgencias"

> **Última ingesta:** 2026-07-27 — `2026-07-27 18-17-Highest.csv` (2025-10 – 2026-07, AD + ARD + SER + WS, 197 tickets).
>
> Este archivo es la **base de datos acumulada**, por ticket, de la métrica de SLA de tickets Prioridad=Highest (reclamos de clientes, bugs, incendios) del dashboard [`outputs/dashboard_performance_desarrollo.html`](../../outputs/dashboard_performance_desarrollo.html), mantenida por la skill [`/dashboard_delivery`](../../.claude/skills/dashboard_delivery/SKILL.md). El usuario deja en `raw/` un export de Jira "tiempo por estado" filtrado a Prioridad=Highest (una fila por ticket, tiempo acumulado por estado — mismo formato que usa `/dashboard_qa`). Cada ingesta hace **upsert por `Clave`**: el ticket que reaparece se actualiza con el dato fresco, el que no aparece en el export nuevo se conserva tal cual. Los agregados se recalculan enteros desde este detalle en cada corrida.
>
> ⚠️ **Requiere un paso manual de Claude antes de ingerir:** este export no trae fecha de release de versión, así que antes de correr `pipeline.py ingest` hay que consultar Jira por MCP (`fixVersions`/`releaseDate`) para cada ticket Finalizada del CSV y volcarlo a `<mismo nombre>.versions.json` en `raw/` (mapa Clave -> lista de fechas ISO de versiones released). Sin ese archivo, "días hasta Publicación" degrada entero a la fecha proxy de "días hasta Finalizada" — ver metodología abajo.

## Metodología / criterios de agregación

- **Universo:** tickets Prioridad=Highest del export (reclamos, bugs urgentes, incendios) — no todos los tickets del backlog.
- **Días hasta Finalizada** = `Creada` + Σ(tiempo en Backlog* + Asignado + Bloqueado + Con defecto + En curso + EN QA + Listo/Seleccionado para desarrollo), es decir, todo el tiempo del export EXCEPTO el que corre dentro de "Finalizada"/"No aplica" (estados terminales cuyo reloj sigue corriendo hasta el export, no se congela). Solo tiene valor para tickets con Estado = Finalizada — el reloj de los demás no paró.
- **Días hasta Publicación** = `Creada` hasta la fecha REAL de release de la versión que resolvió el ticket (`fixVersions`/`releaseDate` de Jira, vía el JSON compañero). Si el ticket no tiene ninguna versión released con fecha en ese JSON, degrada a la misma fecha proxy que "Días hasta Finalizada" (`fuente_publicacion = proxy_finalizada`) — hoy 21 de 166 finalizados están en ese caso.
- **Días abierto (a la ingesta):** para tickets que NO llegaron a Finalizada, días corridos entre `Creada` y el momento de esta ingesta — el reloj **sigue corriendo**: estos tickets NO se excluyen de la vista de riesgo (aparecen igual, con su conteo de días creciendo), solo se excluyen de las medianas/promedios de "tiempo hasta resolución" (no tiene sentido promediar una medición que no terminó). Valor congelado a la fecha de esta ingesta — no se recalcula solo, hace falta una ingesta nueva para actualizarlo.
- **Mediana global (Días hasta Finalizada), 166 tickets resueltos:** 14.54 días.
- **Peor caso abierto ahora mismo:** AD-775 — 151.07 días corridos desde 2026-02-26 (Estado: EN QA).
- **Eje X del dashboard = mes de `Creada`** (decisión del usuario, 2026-07-27): mide "las urgencias creadas en el mes X tardaron Y días en resolverse", no "cuánto se resolvió ese mes" — los meses recientes con tickets aún abiertos quedan marcados como cohorte incompleta (en itálica en el eje) porque su mediana todavía no incluye a los lentos que siguen corriendo.

## Registro de lotes ingeridos

| Fecha ingesta | Archivo fuente | Cobertura | Tickets tocados | Destino histórico |
|---|---|---|---|---|
| 2026-07-27 | `2026-07-27 18-17-Highest.csv` | 2025-10 – 2026-07, AD + ARD + SER + WS | 197 tickets | `4_archivos/historial_raw/2026-07_sla_highest_jira/` |

## Resumen mensual (sanity check — el dashboard recalcula todo del detalle)

| Mes (creación) | Creados | Finalizados | Abiertos | Mediana días hasta Finalizada | Mediana días hasta Publicación | Máx días abierto |
|---|---|---|---|---|---|---|
| 2025-10 | 7 | 7 | 0 | 26.2 | 25.5 | — |
| 2025-11 | 13 | 13 | 0 | 38.0 | 33.6 | — |
| 2025-12 | 24 | 24 | 0 | 22.6 | 32.5 | — |
| 2026-01 | 19 | 19 | 0 | 13.1 | 24.6 | — |
| 2026-02 | 24 | 23 | 1 | 14.9 | 33.3 | 151.1 |
| 2026-03 | 13 | 13 | 0 | 9.1 | 23.6 | — |
| 2026-04 | 25 | 23 | 2 | 10.0 | 19.3 | 117.4 |
| 2026-05 | 25 | 22 | 3 | 13.4 | 23.4 | 84.0 |
| 2026-06 | 25 | 14 | 11 | 6.5 | 6.9 | 56.3 |
| 2026-07 | 22 | 8 | 14 | 1.4 | 1.7 | 26.1 |

## Datos — detalle por ticket

| Clave | Espacio | Tipo | Estado | Creada | Días hasta Finalizada | Días hasta Publicación | Fuente publicación | Días abierto (a la ingesta) |
|---|---|---|---|---|---|---|---|---|
| SER-2 | SER | Historia | Finalizada | 2025-10-27 | 119.24 | 219.52 | jira_release | — |
| SER-3 | SER | Historia | Finalizada | 2025-10-27 | 119.24 | 219.52 | jira_release | — |
| WS-15 | WS | Historia | Finalizada | 2025-10-31 | 26.23 | 25.47 | jira_release | — |
| WS-17 | WS | Historia | Finalizada | 2025-10-31 | 26.23 | 25.47 | jira_release | — |
| WS-18 | WS | Historia | Finalizada | 2025-10-31 | 26.23 | 25.47 | jira_release | — |
| WS-32 | WS | Historia | Finalizada | 2025-10-31 | 42.38 | 16.46 | jira_release | — |
| WS-37 | WS | Historia | Finalizada | 2025-10-31 | 26.01 | 25.46 | jira_release | — |
| AD-62 | AD | Historia | Finalizada | 2025-11-03 | 45.14 | 42.46 | jira_release | — |
| AD-63 | AD | Historia | Finalizada | 2025-11-03 | 38.93 | 42.46 | jira_release | — |
| AD-64 | AD | Historia | Finalizada | 2025-11-03 | 37.96 | 42.46 | jira_release | — |
| AD-66 | AD | Historia | Finalizada | 2025-11-04 | 2.2 | 12.6 | jira_release | — |
| WS-59 | WS | Historia | Finalizada | 2025-11-06 | 54.92 | 104.45 | jira_release | — |
| AD-98 | AD | Historia | Finalizada | 2025-11-10 | 37.95 | 35.31 | jira_release | — |
| AD-99 | AD | Historia | Finalizada | 2025-11-10 | 76.82 | 91.31 | jira_release | — |
| WS-81 | WS | Historia | Finalizada | 2025-11-11 | 31.03 | 5.55 | jira_release | — |
| WS-82 | WS | Historia | Finalizada | 2025-11-11 | 31.02 | 5.54 | jira_release | — |
| AD-114 | AD | Error | Finalizada | 2025-11-12 | 15.98 | 33.58 | jira_release | — |
| AD-144 | AD | Error | Finalizada | 2025-11-13 | 0.86 | 20.34 | jira_release | — |
| WS-104 | WS | Historia | Finalizada | 2025-11-18 | 83.1 | 7.35 | jira_release | — |
| WS-154 | WS | Error | Finalizada | 2025-11-28 | 3.49 | 6.59 | jira_release | — |
| AD-229 | AD | Historia | Finalizada | 2025-12-01 | 108.52 | 70.46 | jira_release | — |
| WS-167 | WS | Error | Finalizada | 2025-12-03 | 13.9 | 54.55 | jira_release | — |
| AD-261 | AD | Historia | Finalizada | 2025-12-09 | 36.3 | 62.62 | jira_release | — |
| AD-264 | AD | Error | Finalizada | 2025-12-09 | 41.28 | 62.44 | jira_release | — |
| WS-195 | WS | Historia | Finalizada | 2025-12-09 | 6.2 | 5.56 | jira_release | — |
| WS-204 | WS | Historia | Finalizada | 2025-12-10 | 44.03 | 47.57 | jira_release | — |
| AD-291 | AD | Historia | Finalizada | 2025-12-11 | 42.85 | 60.32 | jira_release | — |
| AD-319 | AD | Error | Finalizada | 2025-12-12 | 2.9 | 3.29 | jira_release | — |
| WS-233 | WS | Historia | Finalizada | 2025-12-12 | 88.68 | 5.51 | jira_release | — |
| AD-358 | AD | Error | Finalizada | 2025-12-17 | 0.99 | -1.57 | jira_release | — |
| AD-361 | AD | Error | Finalizada | 2025-12-17 | 0.98 | -1.59 | jira_release | — |
| WS-263 | WS | Error | Finalizada | 2025-12-17 | 0.03 | 0.28 | jira_release | — |
| AD-372 | AD | Historia | Finalizada | 2025-12-18 | 22.14 | 53.49 | jira_release | — |
| WS-268 | WS | Error | Finalizada | 2025-12-18 | 29.08 | 39.53 | jira_release | — |
| WS-270 | WS | Historia | Finalizada | 2025-12-18 | 14.78 | -0.73 | jira_release | — |
| WS-272 | WS | Historia | Finalizada | 2025-12-18 | 10.78 | -0.75 | jira_release | — |
| WS-273 | WS | Historia | Finalizada | 2025-12-18 | 38.78 | 39.25 | jira_release | — |
| WS-295 | WS | Error | Finalizada | 2025-12-24 | 23.14 | 33.56 | jira_release | — |
| WS-296 | WS | Error | Finalizada | 2025-12-24 | 33.25 | 33.46 | jira_release | — |
| WS-297 | WS | Error | Finalizada | 2025-12-26 | 18.97 | 31.48 | jira_release | — |
| AD-426 | AD | Error | Finalizada | 2025-12-29 | 11.08 | 42.59 | jira_release | — |
| AD-427 | AD | Historia | Finalizada | 2025-12-29 | 29.19 | 31.55 | jira_release | — |
| WS-306 | WS | Error | Finalizada | 2025-12-29 | 24.67 | 28.25 | jira_release | — |
| WS-307 | WS | Error | Finalizada | 2025-12-30 | 16.89 | 27.36 | jira_release | — |
| AD-437 | AD | Error | Finalizada | 2026-01-02 | 7.14 | 38.43 | jira_release | — |
| WS-331 | WS | Historia | Finalizada | 2026-01-06 | 9.9 | 20.39 | jira_release | — |
| AD-449 | AD | Error | Finalizada | 2026-01-08 | 15.17 | 21.61 | jira_release | — |
| WS-351 | WS | Error | Finalizada | 2026-01-08 | 0.11 | 6.53 | jira_release | — |
| WS-354 | WS | Historia | Finalizada | 2026-01-08 | 13.81 | 18.4 | jira_release | — |
| WS-359 | WS | Error | Finalizada | 2026-01-08 | 0.82 | -0.66 | jira_release | — |
| AD-463 | AD | Error | Finalizada | 2026-01-09 | 6.73 | 31.26 | jira_release | — |
| AD-460 | AD | Historia | Finalizada | 2026-01-12 | 2.14 | 0.43 | jira_release | — |
| AD-614 | AD | Error | Finalizada | 2026-01-12 | 50.49 | 49.29 | jira_release | — |
| AD-465 | AD | Error | Finalizada | 2026-01-13 | 0.32 | -0.43 | jira_release | — |
| AD-466 | AD | Error | Finalizada | 2026-01-13 | 0.28 | -0.44 | jira_release | — |
| AD-496 | AD | Historia | Finalizada | 2026-01-15 | 38.97 | 24.58 | jira_release | — |
| AD-518 | AD | Historia | Finalizada | 2026-01-16 | 68.55 | 72.38 | jira_release | — |
| WS-415 | WS | Error | Finalizada | 2026-01-21 | 1.29 | -0.67 | jira_release | — |
| AD-591 | AD | Error | Finalizada | 2026-01-22 | 40.31 | 39.54 | jira_release | — |
| WS-440 | WS | Error | Finalizada | 2026-01-23 | 26.13 | 26.54 | jira_release | — |
| WS-462 | WS | Error | Finalizada | 2026-01-26 | 35.17 | 43.57 | jira_release | — |
| AD-615 | AD | Error | Finalizada | 2026-01-30 | 13.09 | 58.31 | jira_release | — |
| WS-490 | WS | Error | Finalizada | 2026-01-30 | 25.04 | 39.51 | jira_release | — |
| AD-624 | AD | Historia | Finalizada | 2026-02-03 | 16.08 | 15.58 | jira_release | — |
| AD-629 | AD | Error | Finalizada | 2026-02-03 | 14.93 | 15.47 | jira_release | — |
| AD-630 | AD | Error | Finalizada | 2026-02-03 | 14.93 | 15.47 | jira_release | — |
| WS-509 | WS | Error | Finalizada | 2026-02-05 | 5.81 | 33.32 | jira_release | — |
| AD-674 | AD | Historia | Finalizada | 2026-02-11 | 7.15 | 7.45 | jira_release | — |
| AD-677 | AD | Historia | Finalizada | 2026-02-11 | 40.02 | 46.29 | jira_release | — |
| WS-556 | WS | Historia | Finalizada | 2026-02-11 | 25.96 | 27.33 | jira_release | — |
| AD-683 | AD | Error | Finalizada | 2026-02-12 | 31.91 | 45.38 | jira_release | — |
| AD-693 | AD | Error | Finalizada | 2026-02-13 | 12.98 | 74.57 | jira_release | — |
| AD-696 | AD | Error | Finalizada | 2026-02-13 | 39.88 | 44.39 | jira_release | — |
| SER-43 | SER | Historia | Finalizada | 2026-02-18 | 7.3 | 105.61 | jira_release | — |
| SER-44 | SER | Error | Finalizada | 2026-02-18 | 1.98 | 105.57 | jira_release | — |
| AD-714 | AD | Error | Finalizada | 2026-02-19 | 35.16 | 38.39 | jira_release | — |
| ARD-12 | ARD | Error | Finalizada | 2026-02-19 | 1.1 | 1.1 | proxy_finalizada | — |
| WS-590 | WS | Error | Finalizada | 2026-02-20 | 2.82 | 18.39 | jira_release | — |
| WS-597 | WS | Historia | Finalizada | 2026-02-24 | 2.11 | 14.48 | jira_release | — |
| WS-603 | WS | Error | Finalizada | 2026-02-25 | 7.06 | 7.06 | proxy_finalizada | — |
| AD-767 | AD | Historia | Finalizada | 2026-02-26 | 31.94 | 31.52 | jira_release | — |
| AD-769 | AD | Historia | Finalizada | 2026-02-26 | 53.96 | 61.51 | jira_release | — |
| AD-775 | AD | Error | EN QA | 2026-02-26 | — | — | — | 151.07 |
| AD-783 | AD | Error | Finalizada | 2026-02-27 | 31.91 | 60.44 | jira_release | — |
| AD-784 | AD | Error | Finalizada | 2026-02-27 | 3.76 | 72.36 | jira_release | — |
| WS-612 | WS | Historia | Finalizada | 2026-02-27 | 7.13 | 11.54 | jira_release | — |
| WS-613 | WS | Historia | Finalizada | 2026-02-27 | 139.78 | 139.78 | proxy_finalizada | — |
| AD-807 | AD | Error | Finalizada | 2026-03-06 | 5.17 | 23.57 | jira_release | — |
| AD-808 | AD | Historia | Finalizada | 2026-03-06 | 20.26 | 23.57 | jira_release | — |
| AD-809 | AD | Error | Finalizada | 2026-03-06 | 5.17 | 23.54 | jira_release | — |
| AD-818 | AD | Error | Finalizada | 2026-03-10 | 8.26 | 19.45 | jira_release | — |
| AD-819 | AD | Error | Finalizada | 2026-03-10 | 8.26 | 19.45 | jira_release | — |
| AD-823 | AD | Error | Finalizada | 2026-03-11 | 0.21 | 18.5 | jira_release | — |
| AD-843 | AD | Error | Finalizada | 2026-03-13 | 41.71 | 46.12 | jira_release | — |
| AD-855 | AD | Error | Finalizada | 2026-03-16 | 127.12 | 127.12 | proxy_finalizada | — |
| WS-772 | WS | Historia | Finalizada | 2026-03-18 | 9.1 | 41.33 | jira_release | — |
| WS-777 | WS | Error | Finalizada | 2026-03-18 | 27.95 | 41.27 | jira_release | — |
| AD-882 | AD | Error | Finalizada | 2026-03-19 | 21.99 | 40.38 | jira_release | — |
| AD-899 | AD | Historia | Finalizada | 2026-03-20 | 38.72 | 39.29 | jira_release | — |
| AD-942 | AD | Error | Finalizada | 2026-03-26 | 3.67 | 3.26 | jira_release | — |
| AD-961 | AD | Error | LISTO PARA DESARROLLO | 2026-04-01 | — | — | — | 117.36 |
| AD-971 | AD | Historia | Finalizada | 2026-04-07 | 21.86 | 21.4 | jira_release | — |
| WS-885 | WS | Historia | Finalizada | 2026-04-08 | 0.08 | 0.08 | proxy_finalizada | — |
| AD-977 | AD | Error | Finalizada | 2026-04-09 | 7.86 | 19.29 | jira_release | — |
| AD-978 | AD | Error | Finalizada | 2026-04-09 | 4.29 | 19.29 | jira_release | — |
| AD-989 | AD | Error | Finalizada | 2026-04-13 | 45.1 | 71.61 | jira_release | — |
| AD-991 | AD | Historia | Finalizada | 2026-04-13 | 10 | 15.49 | jira_release | — |
| AD-1000 | AD | Historia | En curso | 2026-04-14 | — | — | — | 104.11 |
| AD-998 | AD | Error | Finalizada | 2026-04-14 | 36.11 | 70.62 | jira_release | — |
| AD-999 | AD | Error | Finalizada | 2026-04-14 | 2.97 | 14.33 | jira_release | — |
| AD-1005 | AD | Historia | Finalizada | 2026-04-15 | 14.31 | 13.48 | jira_release | — |
| AD-1010 | AD | Error | Finalizada | 2026-04-15 | 77.76 | 77.76 | proxy_finalizada | — |
| WS-918 | WS | Error | Finalizada | 2026-04-15 | 8.93 | 13.23 | jira_release | — |
| AD-1027 | AD | Error | Finalizada | 2026-04-21 | 7.67 | 7.67 | proxy_finalizada | — |
| AD-1029 | AD | Error | Finalizada | 2026-04-22 | 89.99 | 89.99 | proxy_finalizada | — |
| AD-1038 | AD | Error | Finalizada | 2026-04-22 | 27.24 | 42.52 | jira_release | — |
| AD-1059 | AD | Error | Finalizada | 2026-04-24 | 32.94 | 60.51 | jira_release | — |
| AD-1060 | AD | Error | Finalizada | 2026-04-24 | 0.28 | -0.51 | jira_release | — |
| WS-1003 | WS | Error | Finalizada | 2026-04-24 | 3.18 | 4.41 | jira_release | — |
| WS-987 | WS | Error | Finalizada | 2026-04-24 | 3.16 | 4.53 | jira_release | — |
| WS-990 | WS | Error | Finalizada | 2026-04-24 | 38.28 | 39.52 | jira_release | — |
| AD-1096 | AD | Error | Finalizada | 2026-04-29 | 27.95 | 55.3 | jira_release | — |
| WS-1027 | WS | Historia | Finalizada | 2026-04-29 | 34.25 | 34.59 | jira_release | — |
| WS-1041 | WS | Error | Finalizada | 2026-04-29 | 4.94 | 5.24 | jira_release | — |
| WS-1042 | WS | Error | Finalizada | 2026-04-29 | 4.91 | 5.23 | jira_release | — |
| AD-1103 | AD | Error | EN QA | 2026-05-04 | — | — | — | 84.05 |
| WS-1050 | WS | Historia | Finalizada | 2026-05-04 | 70.66 | 71.55 | jira_release | — |
| AD-1107 | AD | Error | Finalizada | 2026-05-05 | 22.7 | 49.28 | jira_release | — |
| AD-1110 | AD | Error | Finalizada | 2026-05-07 | 54.57 | 55.59 | jira_release | — |
| WS-1077 | WS | Error | Finalizada | 2026-05-08 | 52.63 | 67.58 | jira_release | — |
| AD-1123 | AD | Error | Finalizada | 2026-05-11 | 71.56 | 71.56 | proxy_finalizada | — |
| AD-1125 | AD | Error | Finalizada | 2026-05-11 | 0.11 | 0.11 | proxy_finalizada | — |
| AD-1128 | AD | Error | Finalizada | 2026-05-12 | 7.99 | 42.58 | jira_release | — |
| AD-1132 | AD | Error | Finalizada | 2026-05-14 | 4.18 | 4.18 | proxy_finalizada | — |
| AD-1133 | AD | Error | Finalizada | 2026-05-14 | 1.31 | 1.31 | proxy_finalizada | — |
| AD-1134 | AD | Error | En curso | 2026-05-14 | — | — | — | 74.27 |
| AD-1138 | AD | Historia | Finalizada | 2026-05-15 | 11.24 | 39.58 | jira_release | — |
| AD-1140 | AD | Historia | Finalizada | 2026-05-15 | 60.36 | 60.36 | proxy_finalizada | — |
| AD-1142 | AD | Error | Backlog | 2026-05-15 | — | — | — | 73.06 |
| AD-1145 | AD | Error | Finalizada | 2026-05-18 | 2.93 | 2.93 | proxy_finalizada | — |
| WS-1139 | WS | Error | Finalizada | 2026-05-19 | 22.31 | 21.58 | jira_release | — |
| WS-1159 | WS | Historia | Finalizada | 2026-05-20 | 0 | -0.42 | jira_release | — |
| WS-1177 | WS | Historia | Finalizada | 2026-05-20 | 20.67 | 20.26 | jira_release | — |
| WS-1195 | WS | Historia | Finalizada | 2026-05-22 | 12.74 | 11.34 | jira_release | — |
| WS-1202 | WS | Error | Finalizada | 2026-05-26 | 6.07 | 7.34 | jira_release | — |
| AD-1197 | AD | Error | Finalizada | 2026-05-27 | 1.15 | -0.54 | jira_release | — |
| AD-1204 | AD | Error | Finalizada | 2026-05-27 | 0.04 | 0.04 | proxy_finalizada | — |
| AD-1217 | AD | Error | Finalizada | 2026-05-29 | 18.81 | 25.33 | jira_release | — |
| AD-1219 | AD | Historia | Finalizada | 2026-05-29 | 14.07 | 25.31 | jira_release | — |
| WS-1217 | WS | Historia | Finalizada | 2026-05-29 | 45.11 | 46.39 | jira_release | — |
| AD-1220 | AD | Historia | En curso | 2026-06-01 | — | — | — | 56.29 |
| AD-1222 | AD | Historia | En curso | 2026-06-01 | — | — | — | 56.28 |
| WS-1242 | WS | Error | Finalizada | 2026-06-02 | 7.08 | 7.51 | jira_release | — |
| WS-1243 | WS | Error | Finalizada | 2026-06-02 | 6.9 | 7.36 | jira_release | — |
| WS-1244 | WS | Historia | Backlog | 2026-06-02 | — | — | — | 55.15 |
| AD-1229 | AD | Error | EN QA | 2026-06-03 | — | — | — | 54.35 |
| WS-1245 | WS | Error | Asignado | 2026-06-03 | — | — | — | 54.39 |
| WS-1246 | WS | Error | Finalizada | 2026-06-03 | 6.94 | 6.29 | jira_release | — |
| AD-1239 | AD | Error | Finalizada | 2026-06-05 | 4.25 | 18.53 | jira_release | — |
| AD-1240 | AD | Error | Finalizada | 2026-06-05 | 48.58 | 48.58 | proxy_finalizada | — |
| AD-1241 | AD | Historia | En curso | 2026-06-08 | — | — | — | 49.31 |
| AD-1242 | AD | Historia | En curso | 2026-06-08 | — | — | — | 49.28 |
| AD-1243 | AD | Historia | En curso | 2026-06-08 | — | — | — | 49.26 |
| WS-1252 | WS | Historia | Finalizada | 2026-06-08 | 28.19 | 36.51 | jira_release | — |
| WS-1254 | WS | Error | Finalizada | 2026-06-08 | 1.95 | 1.32 | jira_release | — |
| SER-62 | SER | Historia | Finalizada | 2026-06-11 | 42.16 | -7.47 | jira_release | — |
| AD-1314 | AD | Error | Finalizada | 2026-06-12 | 4.86 | 11.4 | jira_release | — |
| AD-1320 | AD | Error | Finalizada | 2026-06-16 | 2.18 | 6.46 | jira_release | — |
| AD-1329 | AD | Error | Finalizada | 2026-06-17 | 2.04 | 2.04 | proxy_finalizada | — |
| AD-1331 | AD | Error | EN QA | 2026-06-17 | — | — | — | 40.12 |
| AD-1332 | AD | Error | Finalizada | 2026-06-17 | 1.99 | 1.99 | proxy_finalizada | — |
| AD-1348 | AD | Error | Finalizada | 2026-06-26 | 6.11 | 5.57 | jira_release | — |
| WS-1311 | WS | Historia | Finalizada | 2026-06-26 | 17.9 | 18.36 | jira_release | — |
| WS-1313 | WS | Historia | En curso | 2026-06-26 | — | — | — | 31.1 |
| AD-1352 | AD | Error | EN QA | 2026-06-30 | — | — | — | 27.31 |
| AD-1362 | AD | Historia | Con defecto | 2026-07-01 | — | — | — | 26.12 |
| AD-1372 | AD | Error | En curso | 2026-07-02 | — | — | — | 25.06 |
| AD-1373 | AD | Error | Finalizada | 2026-07-03 | 0.23 | -1.41 | jira_release | — |
| AD-1377 | AD | Historia | En curso | 2026-07-03 | — | — | — | 24.06 |
| AD-1383 | AD | Historia | En curso | 2026-07-07 | — | — | — | 20.12 |
| AD-1384 | AD | Historia | En curso | 2026-07-07 | — | — | — | 20.06 |
| AD-1385 | AD | Historia | En curso | 2026-07-08 | — | — | — | 19.38 |
| AD-1397 | AD | Error | Finalizada | 2026-07-15 | 4.84 | 4.84 | proxy_finalizada | — |
| WS-1386 | WS | Historia | Backlog | 2026-07-15 | — | — | — | 12.47 |
| WS-1387 | WS | Historia | Finalizada | 2026-07-15 | 0.14 | 0.61 | jira_release | — |
| WS-1389 | WS | Error | Finalizada | 2026-07-15 | 4.98 | 7.52 | jira_release | — |
| WS-1390 | WS | Historia | Backlog | 2026-07-15 | — | — | — | 12.29 |
| WS-1395 | WS | Error | Finalizada | 2026-07-17 | 0.31 | 5.6 | jira_release | — |
| WS-1397 | WS | Error | Backlog | 2026-07-17 | — | — | — | 10.29 |
| AD-1420 | AD | Error | Finalizada | 2026-07-20 | 1.64 | 1.27 | jira_release | — |
| AD-1418 | AD | Error | Finalizada | 2026-07-21 | 2.2 | 2.2 | proxy_finalizada | — |
| AD-1426 | AD | Error | Finalizada | 2026-07-22 | 1.11 | 1.11 | proxy_finalizada | — |
| AD-1430 | AD | Error | LISTO PARA DESARROLLO | 2026-07-22 | — | — | — | 5.05 |
| WS-1419 | WS | Historia | Backlog | 2026-07-22 | — | — | — | 5.02 |
| AD-1434 | AD | Historia | En curso | 2026-07-23 | — | — | — | 4 |
| WS-1427 | WS | Error | Asignado | 2026-07-23 | — | — | — | 4.02 |
| WS-1428 | WS | Historia | Backlog | 2026-07-24 | — | — | — | 3.34 |

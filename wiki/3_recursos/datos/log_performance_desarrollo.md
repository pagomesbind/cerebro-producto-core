# Log de Performance de Desarrollo — Base de datos del dashboard "Performance de desarrollo"

> **Última ingesta:** 2026-07-27 — `PUBLICACIONES (1).xlsx` (Julio 2025 – Diciembre 2025, AD + WS, 345 tickets).
>
> Este archivo es la **base de datos acumulada** del dashboard [`outputs/dashboard_performance_desarrollo.html`](../../outputs/dashboard_performance_desarrollo.html), mantenida por la skill [`/dashboard_delivery`](../../.claude/skills/dashboard_delivery/SKILL.md). El PM deja todos los principios de mes un Excel en `raw/` con lo **publicado en producción** (tickets Historia/Error con versión corregida); ocasionalmente se suman backfills históricos puntuales de otras fuentes. Cada ingesta: (1) el pipeline mergea acá las filas nuevas con granularidad año × mes × espacio × tipo × epic — el Excel nuevo PISA los combos año×mes×espacio que trae —, (2) se regenera el dashboard embebiendo esta tabla como JSON, (3) el Excel rota a `4_archivos/historial_raw/`. **No hace falta releer los Excel históricos: este log es la fuente.**
>
> ⚠️ **Este reporte NO alimenta el conocimiento de producto de la wiki** (indicación del usuario 2026-07-13): es una métrica de management para medir al equipo de desarrollo por lo ENTREGADO en producción. El conocimiento de producto de las publicaciones lo maneja `/sync_releases`. El costo de ese desarrollo (USD/SP) se mide aparte, en [`log_costos_desarrollo.md`](log_costos_desarrollo.md).

## Metodología / criterios de agregación

- **Fuente:** reporte mensual del PM (export de Jira, formato ticket-level) y, puntualmente, backfills históricos de otras fuentes (formato agregado por versión). Se cuenta todo ticket/versión listado, incluidos los tickets en estado "No aplica" (decisión del usuario 2026-07-13: si está en el reporte de publicaciones, cuenta como entregado).
- **Espacio:** prefijo de la clave del ticket (WS-123 → WS) en el formato ticket-level; columna PRODUCTO (WALLET→WS, COBRO→AD) en el formato agregado por versión.
- **Epic:** columna "Parent summary" de Jira (formato ticket-level), con trim de espacios. El formato agregado por versión **no trae Epic** — esos registros quedan con Epic vacío (`—`) y **no aparecen en las vistas "por Epic" del dashboard** (no se agrupan en un bucket "sin epic": esos meses simplemente no muestran datos en esa métrica, por pedido explícito del usuario 2026-07-14).
- **SP nulos → 0**; tickets sin clave se descartan; valores de "Mes"/"Año" no reconocidos se excluyen y se reportan.
- **Año:** el formato ticket-level mensual del PM no trae columna de año — se asume `ANIO_DEFAULT` (ver `pipeline.py`, hoy 2026; hay que bumpearlo a mano cuando lleguen reportes de 2027). El formato agregado por versión sí trae "AÑO PUBLICACIÓN" explícito.
- **Epics BAU fijas** (colores constantes en el dashboard): SOPORTE (rojo), REGRESIONES WS, REGRESIONES AD, REGRESIONES OB, REGRESIONES SER, COE, INICIATIVAS TECNICAS. El resto de epics se pinta en escala de grises.

## Registro de lotes ingeridos

| Fecha ingesta | Archivo fuente | Cobertura | Tickets | SP | Destino histórico |
|---|---|---|---|---|---|
| 2026-07-13 | `METRICAS JULIO 26 (Jira) 1 (1).xlsx` | Enero–Junio 2026, WS + AD | 415 | 1099.5 | `4_archivos/historial_raw/2026-07_reporte_pm_metricas_publicadas_ws_ad_ene-jun/` |
| 2026-07-14 | `PUBLICACIONES (1).xlsx` | Julio 2025 – Diciembre 2025, AD + WS | 345 | 1655 | `4_archivos/historial_raw/2026-07_backfill_historico/` |

## Resumen mensual (tickets / SP publicados)

| Año | Mes | AD | WS | Total |
|---|---|---|---|---|
| 2025 | Julio | 20 tk / 84 SP | 30 tk / 146 SP | **50 tk / 230 SP** |
| 2025 | Agosto | 14 tk / 98 SP | 15 tk / 105 SP | **29 tk / 203 SP** |
| 2025 | Septiembre | 60 tk / 253 SP | 35 tk / 273 SP | **95 tk / 526 SP** |
| 2025 | Octubre | 27 tk / 101 SP | 15 tk / 79 SP | **42 tk / 180 SP** |
| 2025 | Noviembre | 20 tk / 82 SP | 27 tk / 167 SP | **47 tk / 249 SP** |
| 2025 | Diciembre | 62 tk / 199 SP | 20 tk / 68 SP | **82 tk / 267 SP** |
| 2026 | Enero | 10 tk / 14 SP | 55 tk / 111.25 SP | **65 tk / 125.25 SP** |
| 2026 | Febrero | 50 tk / 118.5 SP | 1 tk / 0 SP | **51 tk / 118.5 SP** |
| 2026 | Marzo | 76 tk / 196 SP | 64 tk / 202.25 SP | **140 tk / 398.25 SP** |
| 2026 | Abril | 31 tk / 67 SP | 47 tk / 171.25 SP | **78 tk / 238.25 SP** |
| 2026 | Mayo | 5 tk / 10 SP | 9 tk / 17 SP | **14 tk / 27 SP** |
| 2026 | Junio | 33 tk / 108.5 SP | 34 tk / 83.75 SP | **67 tk / 192.25 SP** |
| **Total** | **histórico** | **408 tk / 1331 SP** | **352 tk / 1423.5 SP** | **760 tk / 2754.5 SP** |

## Datos — detalle año × mes × espacio × tipo × epic

| Año | Mes | Espacio | Tipo | Epic | Tickets | SP |
|---|---|---|---|---|---|---|
| 2025 | Julio | AD | Error | — | 18 | 9 |
| 2025 | Julio | AD | Historia | — | 2 | 75 |
| 2025 | Julio | WS | Error | — | 6 | 16 |
| 2025 | Julio | WS | Historia | — | 24 | 130 |
| 2025 | Agosto | AD | Error | — | 1 | 1 |
| 2025 | Agosto | AD | Historia | — | 13 | 97 |
| 2025 | Agosto | WS | Historia | — | 15 | 105 |
| 2025 | Septiembre | AD | Error | — | 24 | 62 |
| 2025 | Septiembre | AD | Historia | — | 36 | 191 |
| 2025 | Septiembre | WS | Error | — | 1 | 1 |
| 2025 | Septiembre | WS | Historia | — | 34 | 272 |
| 2025 | Octubre | AD | Error | — | 13 | 43 |
| 2025 | Octubre | AD | Historia | — | 14 | 58 |
| 2025 | Octubre | WS | Error | — | 3 | 3 |
| 2025 | Octubre | WS | Historia | — | 12 | 76 |
| 2025 | Noviembre | AD | Error | — | 8 | 22 |
| 2025 | Noviembre | AD | Historia | — | 12 | 60 |
| 2025 | Noviembre | WS | Error | — | 5 | 17 |
| 2025 | Noviembre | WS | Historia | — | 22 | 150 |
| 2025 | Diciembre | AD | Error | — | 50 | 147 |
| 2025 | Diciembre | AD | Historia | — | 12 | 52 |
| 2025 | Diciembre | WS | Error | — | 10 | 32 |
| 2025 | Diciembre | WS | Historia | — | 10 | 36 |
| 2026 | Enero | AD | Error | Boton Simple 2.0 | 3 | 2 |
| 2026 | Enero | AD | Error | REQUERIMIENTOS INTERNOS AD | 1 | 1 |
| 2026 | Enero | AD | Error | SOPORTE | 3 | 4 |
| 2026 | Enero | AD | Historia | SOPORTE | 3 | 7 |
| 2026 | Enero | WS | Error | FCI Cuentas remuneradas: Ajustes finales Poincenot | 8 | 7 |
| 2026 | Enero | WS | Error | Impuestos wallet | 7 | 5 |
| 2026 | Enero | WS | Error | Mejorar integraciones: Poder dar soporte en altas cuenta | 1 | 1 |
| 2026 | Enero | WS | Error | REGRESIONES WS | 4 | 4 |
| 2026 | Enero | WS | Error | SOPORTE | 6 | 7.5 |
| 2026 | Enero | WS | Historia | API cripto: Transferencias internas | 5 | 23 |
| 2026 | Enero | WS | Historia | ASTROPAY: Consulta directa a Coelsa por un solo id Coelsa | 1 | 7 |
| 2026 | Enero | WS | Historia | Consulta DEBIN COELSA directo | 2 | 8 |
| 2026 | Enero | WS | Historia | FCI Cuentas remuneradas: Ajustes finales Poincenot | 4 | 10 |
| 2026 | Enero | WS | Historia | INICIATIVAS TECNICAS | 5 | 13.75 |
| 2026 | Enero | WS | Historia | Impuestos wallet | 1 | 1 |
| 2026 | Enero | WS | Historia | Mejorar integraciones: ABM de organizaciones | 2 | 4 |
| 2026 | Enero | WS | Historia | Mejorar integraciones: Poder dar soporte en altas cuenta | 2 | 10 |
| 2026 | Enero | WS | Historia | SOPORTE | 7 | 10 |
| 2026 | Febrero | AD | Error | Acomodar devoluciones parciales para COTO | 3 | 5 |
| 2026 | Febrero | AD | Error | Boton Simple 2.0 | 13 | 21.5 |
| 2026 | Febrero | AD | Error | Codigos externos en orden de venta | 2 | 2 |
| 2026 | Febrero | AD | Error | ECO Cerrado | 4 | 6 |
| 2026 | Febrero | AD | Error | Mejorar integraciones: ABM de canales de cobro | 2 | 2 |
| 2026 | Febrero | AD | Error | QRI PSP 184 acreditacion en wallet | 2 | 4 |
| 2026 | Febrero | AD | Error | REGRESIONES AD | 3 | 7 |
| 2026 | Febrero | AD | Error | REQUERIMIENTOS INTERNOS AD | 1 | 1 |
| 2026 | Febrero | AD | Error | SOPORTE | 2 | 2 |
| 2026 | Febrero | AD | Historia | Acomodar devoluciones parciales para COTO | 1 | 1 |
| 2026 | Febrero | AD | Historia | Carga masiva de deudas para ProvinciaNET | 1 | 15 |
| 2026 | Febrero | AD | Historia | DESA: Boton cancelar y filtros en apis | 3 | 9 |
| 2026 | Febrero | AD | Historia | ECO Cerrado | 5 | 19 |
| 2026 | Febrero | AD | Historia | INICIATIVAS TECNICAS | 1 | 1 |
| 2026 | Febrero | AD | Historia | Mejorar integraciones: Sanear "Crear Entidad" desde el admin | 2 | 4 |
| 2026 | Febrero | AD | Historia | REQUERIMIENTOS INTERNOS AD | 2 | 10 |
| 2026 | Febrero | AD | Historia | SOPORTE | 3 | 9 |
| 2026 | Febrero | WS | Historia | SOPORTE | 1 | 0 |
| 2026 | Marzo | AD | Error | Boton Simple 2.0 | 5 | 7 |
| 2026 | Marzo | AD | Error | Codigos externos en orden de venta | 3 | 3 |
| 2026 | Marzo | AD | Error | DESA: Boton cancelar y filtros en apis | 2 | 2 |
| 2026 | Marzo | AD | Error | ECO Cerrado | 1 | 1 |
| 2026 | Marzo | AD | Error | Mejorar integraciones: ABM de canales de cobro | 12 | 26 |
| 2026 | Marzo | AD | Error | Mejorar integraciones: Sanear "Crear Entidad" desde el admin | 1 | 1 |
| 2026 | Marzo | AD | Error | Ministerio de Justicia - Asociar productos a transaccion | 3 | 3 |
| 2026 | Marzo | AD | Error | POS | 1 | 3 |
| 2026 | Marzo | AD | Error | QRI PSP 184 acreditacion en wallet | 2 | 6 |
| 2026 | Marzo | AD | Error | REGRESIONES AD | 8 | 18 |
| 2026 | Marzo | AD | Error | SOPORTE | 11 | 19 |
| 2026 | Marzo | AD | Historia | Codigos externos en orden de venta | 5 | 17 |
| 2026 | Marzo | AD | Historia | DESA: Boton cancelar y filtros en apis | 1 | 3 |
| 2026 | Marzo | AD | Historia | INICIATIVAS TECNICAS | 4 | 8 |
| 2026 | Marzo | AD | Historia | Mejorar integraciones: ABM de canales de cobro | 11 | 55 |
| 2026 | Marzo | AD | Historia | Mejorar integraciones: Sanear "Crear Entidad" desde el admin | 1 | 7 |
| 2026 | Marzo | AD | Historia | Ministerio de Justicia - Asociar productos a transaccion | 4 | 16 |
| 2026 | Marzo | AD | Historia | SOPORTE | 1 | 1 |
| 2026 | Marzo | WS | Error | Consulta DEBIN COELSA directo | 4 | 1.75 |
| 2026 | Marzo | WS | Error | Consulta totalizadores CBU/CVU Coelsa - CONSULTA POR CUENTA | 1 | 0.25 |
| 2026 | Marzo | WS | Error | FCI Cuentas remuneradas: Ajustes finales Poincenot | 10 | 5.75 |
| 2026 | Marzo | WS | Error | Impuestos wallet | 1 | 7 |
| 2026 | Marzo | WS | Error | Mejorar integraciones: ABM de organizaciones | 1 | 0.5 |
| 2026 | Marzo | WS | Error | REGRESIONES WS | 4 | 2 |
| 2026 | Marzo | WS | Error | SOPORTE | 5 | 23.5 |
| 2026 | Marzo | WS | Historia | COE | 1 | 7 |
| 2026 | Marzo | WS | Historia | Consulta totalizadores CBU/CVU Coelsa - CONSULTA POR CUENTA | 1 | 3 |
| 2026 | Marzo | WS | Historia | FCI Cuentas remuneradas: Ajustes finales Poincenot | 4 | 12 |
| 2026 | Marzo | WS | Historia | INICIATIVAS TECNICAS | 10 | 39.5 |
| 2026 | Marzo | WS | Historia | Impuestos wallet | 2 | 4 |
| 2026 | Marzo | WS | Historia | Mejorar integraciones: ABM de organizaciones | 1 | 3 |
| 2026 | Marzo | WS | Historia | Pagos FX: APIs Alta de beneficiario | 4 | 28 |
| 2026 | Marzo | WS | Historia | Pagos FX: APIs Consulta de cotizacion | 3 | 25 |
| 2026 | Marzo | WS | Historia | Pagos FX: APIs Crear pago FX | 1 | 7 |
| 2026 | Marzo | WS | Historia | Pagos FX: Wrapper MC Move | 1 | 3 |
| 2026 | Marzo | WS | Historia | REQUERIMIENTOS INTERNOS WS | 1 | 3 |
| 2026 | Marzo | WS | Historia | SOPORTE | 9 | 27 |
| 2026 | Abril | AD | Error | Boton Simple 2.0 | 2 | 6 |
| 2026 | Abril | AD | Error | Codigos externos en orden de venta | 1 | 3 |
| 2026 | Abril | AD | Error | DESA: Boton cancelar y filtros en apis | 1 | 1 |
| 2026 | Abril | AD | Error | Mejorar integraciones: ABM de canales de cobro | 1 | 1 |
| 2026 | Abril | AD | Error | Mejorar integraciones: Errores y mejoras admin en general | 1 | 3 |
| 2026 | Abril | AD | Error | Mejorar integraciones: Sanear "Crear Entidad" desde el admin | 2 | 2 |
| 2026 | Abril | AD | Error | Ministerio de Justicia - Asociar productos a transaccion | 1 | 1 |
| 2026 | Abril | AD | Error | REGRESIONES AD | 2 | 4 |
| 2026 | Abril | AD | Error | REQUERIMIENTOS INTERNOS AD | 1 | 3 |
| 2026 | Abril | AD | Error | SOPORTE | 10 | 20 |
| 2026 | Abril | AD | Historia | Boton Simple 2.0 | 1 | 1 |
| 2026 | Abril | AD | Historia | Carga masiva de deudas para ProvinciaNET | 1 | 3 |
| 2026 | Abril | AD | Historia | Mejorar integraciones: Errores y mejoras admin en general | 1 | 3 |
| 2026 | Abril | AD | Historia | Mejorar integraciones: Sanear "Crear Entidad" desde el admin | 1 | 3 |
| 2026 | Abril | AD | Historia | Ministerio de Justicia - Asociar productos a transaccion | 2 | 4 |
| 2026 | Abril | AD | Historia | REQUERIMIENTOS INTERNOS AD | 1 | 3 |
| 2026 | Abril | AD | Historia | SOPORTE | 2 | 6 |
| 2026 | Abril | WS | Error | FCI Cuentas remuneradas: Ajustes finales Poincenot | 1 | 0.5 |
| 2026 | Abril | WS | Error | Mejorar integraciones: ABM de organizaciones | 1 | 0.5 |
| 2026 | Abril | WS | Error | Mejorar integraciones: Poder dar soporte en altas cuenta | 1 | 0.5 |
| 2026 | Abril | WS | Error | REGRESIONES AD | 1 | 0 |
| 2026 | Abril | WS | Error | REGRESIONES WS | 2 | 1.25 |
| 2026 | Abril | WS | Error | SOPORTE | 4 | 10 |
| 2026 | Abril | WS | Error | Transferencias pull en Ardid | 5 | 4 |
| 2026 | Abril | WS | Historia | COE | 2 | 18 |
| 2026 | Abril | WS | Historia | Contracargos en debin recurrente | 1 | 14 |
| 2026 | Abril | WS | Historia | INICIATIVAS TECNICAS | 3 | 17 |
| 2026 | Abril | WS | Historia | Mejorar recaudacion de impuestos wallet | 2 | 10 |
| 2026 | Abril | WS | Historia | Pagos FX MVP 2: APIs Alta de beneficiario | 1 | 3 |
| 2026 | Abril | WS | Historia | Pagos FX: APIs Alta de beneficiario | 2 | 6 |
| 2026 | Abril | WS | Historia | Pagos FX: APIs Consulta de cotizacion | 1 | 3 |
| 2026 | Abril | WS | Historia | Pagos FX: APIs Crear pago FX | 5 | 41 |
| 2026 | Abril | WS | Historia | Pagos FX: Webhooks operaciones FX | 1 | 15 |
| 2026 | Abril | WS | Historia | Pagos FX: Wrapper MC Move | 1 | 3 |
| 2026 | Abril | WS | Historia | Que pagos con QR pasen por Ardid | 3 | 13 |
| 2026 | Abril | WS | Historia | REQUERIMIENTOS INTERNOS WS | 2 | 6 |
| 2026 | Abril | WS | Historia | SOPORTE | 8 | 5.5 |
| 2026 | Mayo | AD | Error | Mejorar integraciones: ABM de canales de cobro | 2 | 6 |
| 2026 | Mayo | AD | Error | SOPORTE | 2 | 1 |
| 2026 | Mayo | AD | Historia | INICIATIVAS TECNICAS | 1 | 3 |
| 2026 | Mayo | WS | Error | Contracargos en debin recurrente | 2 | 1 |
| 2026 | Mayo | WS | Error | SOPORTE | 1 | 3 |
| 2026 | Mayo | WS | Historia | FCI Cuentas remuneradas: Ajustes finales Poincenot | 1 | 0 |
| 2026 | Mayo | WS | Historia | INICIATIVAS TECNICAS | 1 | 3 |
| 2026 | Mayo | WS | Historia | Pagos FX MVP 2: APIs Alta de beneficiario | 1 | 3 |
| 2026 | Mayo | WS | Historia | Pagos FX: APIs Crear pago FX | 1 | 3 |
| 2026 | Mayo | WS | Historia | Pagos FX: Wrapper MC Move | 1 | 3 |
| 2026 | Mayo | WS | Historia | SOPORTE | 1 | 1 |
| 2026 | Junio | AD | Error | Boton Simple 2.0 | 1 | 3 |
| 2026 | Junio | AD | Error | DESA: Boton cancelar y filtros en apis | 2 | 2 |
| 2026 | Junio | AD | Error | Mejorar integraciones: Errores y mejoras admin en general | 1 | 1 |
| 2026 | Junio | AD | Error | Mejorar integraciones: Sanear "Crear Entidad" desde el admin | 1 | 1 |
| 2026 | Junio | AD | Error | Pagos FX - Portal Web | 2 | 1.5 |
| 2026 | Junio | AD | Error | REGRESIONES AD | 5 | 11 |
| 2026 | Junio | AD | Error | SOPORTE | 7 | 13 |
| 2026 | Junio | AD | Historia | COE | 2 | 18 |
| 2026 | Junio | AD | Historia | Codigos externos en orden de venta | 1 | 1 |
| 2026 | Junio | AD | Historia | DESA: Boton cancelar y filtros en apis | 1 | 1 |
| 2026 | Junio | AD | Historia | INICIATIVAS TECNICAS | 2 | 2 |
| 2026 | Junio | AD | Historia | Mejorar integraciones: ABM de roles y usuarios | 1 | 1 |
| 2026 | Junio | AD | Historia | Mejorar integraciones: Sanear "Crear Entidad" desde el admin | 1 | 7 |
| 2026 | Junio | AD | Historia | Ministerio de Justicia - Cobro en POS | 1 | 3 |
| 2026 | Junio | AD | Historia | Pagos FX - Portal Web | 3 | 37 |
| 2026 | Junio | AD | Historia | REGRESIONES AD | 1 | 3 |
| 2026 | Junio | AD | Historia | SOPORTE | 1 | 3 |
| 2026 | Junio | WS | Error | Contracargos en debin recurrente | 1 | 0.5 |
| 2026 | Junio | WS | Error | FCI Cuentas remuneradas: Ajustes finales Poincenot | 4 | 4.25 |
| 2026 | Junio | WS | Error | REGRESIONES WS | 4 | 5 |
| 2026 | Junio | WS | Error | REQUERIMIENTOS INTERNOS WS | 1 | 0.25 |
| 2026 | Junio | WS | Error | SOPORTE | 4 | 7 |
| 2026 | Junio | WS | Error | Transferencias pull en Ardid | 1 | 0.25 |
| 2026 | Junio | WS | Historia | COE | 2 | 10 |
| 2026 | Junio | WS | Historia | Contracargos en debin recurrente | 2 | 10 |
| 2026 | Junio | WS | Historia | FCI Cuentas remuneradas: Ajustes finales Poincenot | 3 | 13 |
| 2026 | Junio | WS | Historia | INICIATIVAS TECNICAS | 4 | 14 |
| 2026 | Junio | WS | Historia | SOPORTE | 8 | 19.5 |

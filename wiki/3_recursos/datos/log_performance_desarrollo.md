# Log de Performance de Desarrollo — Base de datos del dashboard "Pulso de Delivery"

> **Última ingesta:** 2026-09-16 — `Histórico Tickets Publicados Jira.xlsx` (Octubre 2025 – Agosto 2026, AD + WS, 768 tickets).
>
> Este archivo es la **base de datos acumulada** del dashboard [`outputs/dashboard_performance_desarrollo.html`](../../outputs/dashboard_performance_desarrollo.html) ("Pulso de Delivery"), mantenida por la skill [`/dashboard_delivery`](../../.claude/skills/dashboard_delivery/SKILL.md). El PM deja en `raw/` el export histórico consolidado de tickets (reemplaza todo el historial que cubre) más, puntualmente, backfills de otras fuentes. Cada ingesta: (1) el pipeline mergea acá las filas nuevas con granularidad año × mes × espacio × tipo × epic — el archivo nuevo PISA los combos año×mes×espacio que trae —, (2) se regenera el dashboard embebiendo esta tabla como JSON, (3) el archivo rota a `4_archivos/historial_raw/`. **No hace falta releer los Excel históricos: este log es la fuente.**
>
> ⚠️ **Este reporte NO alimenta el conocimiento de producto de la wiki** (indicación del usuario 2026-07-13): es una métrica de management para medir al equipo de desarrollo por lo ENTREGADO en producción. El conocimiento de producto de las publicaciones lo maneja `/sync_releases`. El costo de ese desarrollo (USD/SP) se mide aparte, en [`log_costos_desarrollo.md`](log_costos_desarrollo.md).

## Metodología / criterios de agregación

- **Fuente (desde 2026-09-16):** export histórico consolidado de tickets (Jira, formato ticket-level con Mes numérico + columna Año propia + columna Estado), reemplazado por completo en cada invocación de la skill — el PM ya no manda un Excel incremental mensual. Se filtra a Estado en {Finalizada, No aplica} antes de sumar (única fuente de "publicado"; un export histórico trae de todo, incluido Bloqueado/EN QA). Puntualmente se suman backfills históricos de otras fuentes (formato agregado por versión) para tramos que el histórico consolidado no cubre.
- **Espacio:** prefijo de la clave del ticket (WS-123 → WS) en el formato ticket-level; columna PRODUCTO (WALLET→WS, COBRO→AD) en el formato agregado por versión.
- **Epic:** columna "Parent summary" de Jira (formato ticket-level), con trim de espacios. El formato agregado por versión **no trae Epic** — esos registros quedan con Epic vacío (`—`). El dashboard actual ("Pulso de Delivery") no tiene vistas por Epic; el Epic solo se usa para calcular el % de SP en mantenimiento (ver bullet siguiente) — un mes sin Epic conocida queda sin dato en esa métrica en vez de contarlo como no-mantenimiento.
- **SP nulos → 0**; tickets sin clave se descartan; valores de "Mes"/"Año"/"Estado" no reconocidos o no publicados se excluyen y se reportan.
- **Año:** viene de la propia columna Año del histórico consolidado; solo se asume `ANIO_DEFAULT` (ver `pipeline.py`) si algún origen puntual no trae esa columna (formato mensual legacy).
- **Epics BAU fijas** (usadas para el % de SP en mantenimiento del dashboard, ver `log_costos_desarrollo.md`/dashboard): SOPORTE, REGRESIONES WS, REGRESIONES AD, REGRESIONES OB, REGRESIONES SER, COE, INICIATIVAS TECNICAS.

## Registro de lotes ingeridos

| Fecha ingesta | Archivo fuente | Cobertura | Tickets | SP | Destino histórico |
|---|---|---|---|---|---|
| 2026-07-13 | `METRICAS JULIO 26 (Jira) 1 (1).xlsx` | Enero–Junio 2026, WS + AD | 415 | 1099.5 | `4_archivos/historial_raw/2026-07_reporte_pm_metricas_publicadas_ws_ad_ene-jun/` |
| 2026-07-14 | `PUBLICACIONES (1).xlsx` | Julio 2025 – Diciembre 2025, AD + WS | 345 | 1655 | `4_archivos/historial_raw/2026-07_backfill_historico/` |
| 2026-09-16 | `Histórico Tickets Publicados Jira.xlsx` | Octubre 2025 – Agosto 2026, AD + WS | 768 | 1932 | `4_archivos/historial_raw/2026-09_reporte_pm_metricas_publicadas/` |

## Resumen mensual (tickets / SP publicados)

| Año | Mes | AD | WS | Total |
|---|---|---|---|---|
| 2025 | Julio | 20 tk / 84 SP | 30 tk / 146 SP | **50 tk / 230 SP** |
| 2025 | Agosto | 14 tk / 98 SP | 15 tk / 105 SP | **29 tk / 203 SP** |
| 2025 | Septiembre | 60 tk / 253 SP | 35 tk / 273 SP | **95 tk / 526 SP** |
| 2025 | Octubre | 24 tk / 7 SP | 32 tk / 205 SP | **56 tk / 212 SP** |
| 2025 | Noviembre | 65 tk / 179.25 SP | 34 tk / 82.25 SP | **99 tk / 261.5 SP** |
| 2025 | Diciembre | 71 tk / 194 SP | 58 tk / 129 SP | **129 tk / 323 SP** |
| 2026 | Enero | 54 tk / 108.5 SP | 48 tk / 146.5 SP | **102 tk / 255 SP** |
| 2026 | Febrero | 45 tk / 129 SP | 33 tk / 118.25 SP | **78 tk / 247.25 SP** |
| 2026 | Marzo | 34 tk / 37 SP | 35 tk / 115 SP | **69 tk / 152 SP** |
| 2026 | Abril | 24 tk / 80 SP | 29 tk / 52 SP | **53 tk / 132 SP** |
| 2026 | Mayo | 22 tk / 27.5 SP | 13 tk / 25 SP | **35 tk / 52.5 SP** |
| 2026 | Junio | 9 tk / 14.5 SP | 22 tk / 30.5 SP | **31 tk / 45 SP** |
| 2026 | Julio | 12 tk / 12 SP | 17 tk / 20.25 SP | **29 tk / 32.25 SP** |
| 2026 | Agosto | 67 tk / 179.5 SP | 20 tk / 40 SP | **87 tk / 219.5 SP** |
| **Total** | **histórico** | **521 tk / 1403.25 SP** | **421 tk / 1487.75 SP** | **942 tk / 2891 SP** |

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
| 2025 | Octubre | AD | Error | DOLORES de Clientes | 5 | 1 |
| 2025 | Octubre | AD | Error | POS | 2 | 3 |
| 2025 | Octubre | AD | Historia | Boton Simple 2.0 | 1 | 0 |
| 2025 | Octubre | AD | Historia | DOLORES de Clientes | 6 | 0 |
| 2025 | Octubre | AD | Historia | Dolores de Soporte y Administracion | 2 | 0 |
| 2025 | Octubre | AD | Historia | Grupo DESA: requerimientos para salir a prod | 1 | 0 |
| 2025 | Octubre | AD | Historia | INICIATIVAS TECNICAS | 3 | 0 |
| 2025 | Octubre | AD | Historia | Mejorar integraciones: ABM de canales de cobro | 1 | 3 |
| 2025 | Octubre | AD | Historia | Mejorar integraciones: ABM de roles y usuarios | 3 | 0 |
| 2025 | Octubre | WS | Error | Integracion Wallet+Ardid | 1 | 1 |
| 2025 | Octubre | WS | Historia | API Cripto: Compra/venta | 4 | 36 |
| 2025 | Octubre | WS | Historia | API cripto: Transferencias internas | 5 | 23 |
| 2025 | Octubre | WS | Historia | Consulta DEBIN COELSA directo | 5 | 37 |
| 2025 | Octubre | WS | Historia | Cuentas para menores: MVP Arcos | 3 | 29 |
| 2025 | Octubre | WS | Historia | FCI Cuentas remuneradas: Ajustes finales Poincenot | 2 | 10 |
| 2025 | Octubre | WS | Historia | INICIATIVAS TECNICAS | 5 | 33 |
| 2025 | Octubre | WS | Historia | Impuestos wallet | 3 | 8 |
| 2025 | Octubre | WS | Historia | Motor general de recycle | 2 | 6 |
| 2025 | Octubre | WS | Historia | PIX rol emisor: Recibir devolucion | 1 | 15 |
| 2025 | Octubre | WS | Historia | QRI PSP 184 acreditacion en wallet | 1 | 7 |
| 2025 | Noviembre | AD | Error | Boton Simple 2.0 | 10 | 15 |
| 2025 | Noviembre | AD | Error | Cuotas CFT a clientes | 1 | 3 |
| 2025 | Noviembre | AD | Error | DOLORES de Clientes | 1 | 3 |
| 2025 | Noviembre | AD | Error | Grupo DESA: requerimientos para salir a prod | 2 | 0 |
| 2025 | Noviembre | AD | Error | Mejorar integraciones: ABM de canales de cobro | 6 | 12 |
| 2025 | Noviembre | AD | Error | POS | 1 | 3 |
| 2025 | Noviembre | AD | Error | QRI PSP 184 acreditacion en wallet | 2 | 4 |
| 2025 | Noviembre | AD | Error | REGRESIONES AD | 7 | 18 |
| 2025 | Noviembre | AD | Error | Reporting | 4 | 0 |
| 2025 | Noviembre | AD | Error | SOPORTE | 7 | 12.25 |
| 2025 | Noviembre | AD | Historia | Acomodar devoluciones parciales para COTO | 3 | 13 |
| 2025 | Noviembre | AD | Historia | ECO Cerrado | 3 | 17 |
| 2025 | Noviembre | AD | Historia | INICIATIVAS TECNICAS | 3 | 0 |
| 2025 | Noviembre | AD | Historia | Mejorar integraciones: ABM de canales de cobro | 9 | 44 |
| 2025 | Noviembre | AD | Historia | Mejorar integraciones: ABM de roles y usuarios | 2 | 22 |
| 2025 | Noviembre | AD | Historia | POS con PRISMA: Admin | 1 | 3 |
| 2025 | Noviembre | AD | Historia | SOPORTE | 3 | 10 |
| 2025 | Noviembre | WS | Error | API Cripto: Compra/venta | 1 | 3 |
| 2025 | Noviembre | WS | Error | FCI Cuentas remuneradas: Ajustes finales Poincenot | 4 | 7 |
| 2025 | Noviembre | WS | Error | Impuestos wallet | 5 | 0 |
| 2025 | Noviembre | WS | Error | REGRESIONES WS | 2 | 0 |
| 2025 | Noviembre | WS | Error | SOPORTE | 4 | 1 |
| 2025 | Noviembre | WS | Historia | API Cripto: Compra/venta | 1 | 3 |
| 2025 | Noviembre | WS | Historia | Consulta DEBIN COELSA directo | 1 | 3 |
| 2025 | Noviembre | WS | Historia | Consulta totalizadores CBU/CVU Coelsa - CONSULTA POR CUENTA | 2 | 14 |
| 2025 | Noviembre | WS | Historia | FCI Cuentas remuneradas: Ajustes finales Poincenot | 3 | 11 |
| 2025 | Noviembre | WS | Historia | INICIATIVAS TECNICAS | 2 | 15.25 |
| 2025 | Noviembre | WS | Historia | Pagos FX: Wrapper MC Move | 8 | 24 |
| 2025 | Noviembre | WS | Historia | REGRESIONES WS | 1 | 1 |
| 2025 | Diciembre | AD | Error | Acomodar devoluciones parciales para COTO | 6 | 12 |
| 2025 | Diciembre | AD | Error | Boton Simple 2.0 | 13 | 28 |
| 2025 | Diciembre | AD | Error | ECO Cerrado | 3 | 6 |
| 2025 | Diciembre | AD | Error | Mejorar integraciones: ABM de canales de cobro | 3 | 9 |
| 2025 | Diciembre | AD | Error | Mejorar integraciones: Errores y mejoras admin en general | 1 | 1 |
| 2025 | Diciembre | AD | Error | POS | 1 | 3 |
| 2025 | Diciembre | AD | Error | REGRESIONES AD | 8 | 16 |
| 2025 | Diciembre | AD | Error | SOPORTE | 5 | 9 |
| 2025 | Diciembre | AD | Historia | Acomodar devoluciones parciales para COTO | 1 | 1 |
| 2025 | Diciembre | AD | Historia | Cobrar QR con tarjetas (MODO) | 2 | 10 |
| 2025 | Diciembre | AD | Historia | DESA: Boton cancelar y filtros en apis | 4 | 12 |
| 2025 | Diciembre | AD | Historia | ECO Cerrado | 3 | 9 |
| 2025 | Diciembre | AD | Historia | INICIATIVAS TECNICAS | 2 | 3 |
| 2025 | Diciembre | AD | Historia | Mejorar integraciones: ABM de canales de cobro | 4 | 20 |
| 2025 | Diciembre | AD | Historia | Mejorar integraciones: ABM de roles y usuarios | 1 | 1 |
| 2025 | Diciembre | AD | Historia | Mejorar integraciones: Errores y mejoras admin en general | 2 | 6 |
| 2025 | Diciembre | AD | Historia | Mejorar integraciones: Sanear "Crear Entidad" desde el admin | 5 | 21 |
| 2025 | Diciembre | AD | Historia | Ministerio de Justicia - Asociar productos a transaccion | 2 | 6 |
| 2025 | Diciembre | AD | Historia | POS | 1 | 7 |
| 2025 | Diciembre | AD | Historia | REQUERIMIENTOS INTERNOS AD | 3 | 13 |
| 2025 | Diciembre | AD | Historia | SOPORTE | 1 | 1 |
| 2025 | Diciembre | WS | Error | Consulta DEBIN COELSA directo | 1 | 0.5 |
| 2025 | Diciembre | WS | Error | FCI Cuentas remuneradas: Ajustes finales Poincenot | 16 | 11.5 |
| 2025 | Diciembre | WS | Error | Impuestos wallet | 2 | 2 |
| 2025 | Diciembre | WS | Error | REGRESIONES WS | 6 | 3 |
| 2025 | Diciembre | WS | Error | SOPORTE | 5 | 8 |
| 2025 | Diciembre | WS | Historia | ASTROPAY: Consulta directa a Coelsa por un solo id Coelsa | 2 | 10 |
| 2025 | Diciembre | WS | Historia | Consulta DEBIN COELSA directo | 2 | 1 |
| 2025 | Diciembre | WS | Historia | Consulta totalizadores CBU/CVU Coelsa - CONSULTA POR CUENTA | 1 | 3 |
| 2025 | Diciembre | WS | Historia | FCI Cuentas remuneradas: Ajustes finales Poincenot | 5 | 9 |
| 2025 | Diciembre | WS | Historia | INICIATIVAS TECNICAS | 4 | 18 |
| 2025 | Diciembre | WS | Historia | Mejorar integraciones: ABM de organizaciones | 3 | 7 |
| 2025 | Diciembre | WS | Historia | Mejorar integraciones: Poder dar soporte en altas cuenta | 2 | 10 |
| 2025 | Diciembre | WS | Historia | Pagos FX: APIs Alta de beneficiario | 1 | 15 |
| 2025 | Diciembre | WS | Historia | Pagos FX: APIs Consulta de cotizacion | 2 | 18 |
| 2025 | Diciembre | WS | Historia | Pagos FX: Wrapper MC Move | 3 | 7 |
| 2025 | Diciembre | WS | Historia | SOPORTE | 3 | 6 |
| 2026 | Enero | AD | Error | Acomodar devoluciones parciales para COTO | 1 | 1 |
| 2026 | Enero | AD | Error | Boton Simple 2.0 | 15 | 22.5 |
| 2026 | Enero | AD | Error | ECO Cerrado | 3 | 3 |
| 2026 | Enero | AD | Error | INICIATIVAS TECNICAS | 1 | 1 |
| 2026 | Enero | AD | Error | Mejorar integraciones: ABM de canales de cobro | 2 | 2 |
| 2026 | Enero | AD | Error | Mejorar integraciones: Errores y mejoras admin en general | 2 | 4 |
| 2026 | Enero | AD | Error | Mejorar integraciones: Sanear "Crear Entidad" desde el admin | 3 | 3 |
| 2026 | Enero | AD | Error | QRI PSP 184 acreditacion en wallet | 1 | 3 |
| 2026 | Enero | AD | Error | REGRESIONES AD | 4 | 4 |
| 2026 | Enero | AD | Error | REQUERIMIENTOS INTERNOS AD | 2 | 2 |
| 2026 | Enero | AD | Error | SOPORTE | 7 | 12 |
| 2026 | Enero | AD | Historia | Carga masiva de deudas para ProvinciaNET | 1 | 15 |
| 2026 | Enero | AD | Historia | Codigos externos en orden de venta | 1 | 7 |
| 2026 | Enero | AD | Historia | INICIATIVAS TECNICAS | 6 | 14 |
| 2026 | Enero | AD | Historia | Mejorar integraciones: ABM de canales de cobro | 1 | 1 |
| 2026 | Enero | AD | Historia | Ministerio de Justicia - Asociar productos a transaccion | 1 | 7 |
| 2026 | Enero | AD | Historia | SOPORTE | 3 | 7 |
| 2026 | Enero | WS | Error | Consulta DEBIN COELSA directo | 3 | 0.75 |
| 2026 | Enero | WS | Error | FCI Cuentas remuneradas: Ajustes finales Poincenot | 4 | 4.25 |
| 2026 | Enero | WS | Error | Impuestos wallet | 2 | 10 |
| 2026 | Enero | WS | Error | Mejorar integraciones: Poder dar soporte en altas cuenta | 1 | 1 |
| 2026 | Enero | WS | Error | REGRESIONES WS | 3 | 2 |
| 2026 | Enero | WS | Error | SOPORTE | 6 | 11.5 |
| 2026 | Enero | WS | Historia | COE | 1 | 7 |
| 2026 | Enero | WS | Historia | FCI Cuentas remuneradas: Ajustes finales Poincenot | 5 | 17 |
| 2026 | Enero | WS | Historia | INICIATIVAS TECNICAS | 6 | 23 |
| 2026 | Enero | WS | Historia | Impuestos wallet | 1 | 1 |
| 2026 | Enero | WS | Historia | PAGOS FX | 1 | 7 |
| 2026 | Enero | WS | Historia | Pagos FX: APIs Alta de beneficiario | 3 | 9 |
| 2026 | Enero | WS | Historia | Pagos FX: APIs Crear pago FX | 3 | 25 |
| 2026 | Enero | WS | Historia | Pagos FX: Webhooks operaciones FX | 1 | 15 |
| 2026 | Enero | WS | Historia | Pagos FX: Wrapper MC Move | 1 | 3 |
| 2026 | Enero | WS | Historia | SOPORTE | 7 | 10 |
| 2026 | Febrero | AD | Error | Boton Simple 2.0 | 1 | 1 |
| 2026 | Febrero | AD | Error | Codigos externos en orden de venta | 3 | 5 |
| 2026 | Febrero | AD | Error | Mejorar integraciones: ABM de canales de cobro | 7 | 15 |
| 2026 | Febrero | AD | Error | REGRESIONES AD | 1 | 3 |
| 2026 | Febrero | AD | Error | REQUERIMIENTOS INTERNOS AD | 1 | 3 |
| 2026 | Febrero | AD | Error | SOPORTE | 11 | 33 |
| 2026 | Febrero | AD | Historia | COE | 1 | 15 |
| 2026 | Febrero | AD | Historia | Carga masiva de deudas para ProvinciaNET | 1 | 3 |
| 2026 | Febrero | AD | Historia | Cobrar QR con tarjetas (MODO) | 3 | 7 |
| 2026 | Febrero | AD | Historia | Codigos externos en orden de venta | 4 | 10 |
| 2026 | Febrero | AD | Historia | INICIATIVAS TECNICAS | 3 | 5 |
| 2026 | Febrero | AD | Historia | Ministerio de Justicia - Asociar productos a transaccion | 2 | 6 |
| 2026 | Febrero | AD | Historia | Ministerio de Justicia - Cobro en POS | 2 | 6 |
| 2026 | Febrero | AD | Historia | POS | 1 | 0 |
| 2026 | Febrero | AD | Historia | Pagos FX - Portal Web | 1 | 15 |
| 2026 | Febrero | AD | Historia | SOPORTE | 3 | 2 |
| 2026 | Febrero | WS | Error | COE | 1 | 15 |
| 2026 | Febrero | WS | Error | Consulta DEBIN COELSA directo | 1 | 1 |
| 2026 | Febrero | WS | Error | Consulta totalizadores CBU/CVU Coelsa - CONSULTA POR CUENTA | 1 | 0.25 |
| 2026 | Febrero | WS | Error | FCI Cuentas remuneradas: Ajustes finales Poincenot | 1 | 1 |
| 2026 | Febrero | WS | Error | Mejorar integraciones: ABM de organizaciones | 1 | 0.5 |
| 2026 | Febrero | WS | Error | Mejorar recaudacion de impuestos wallet | 1 | 0.5 |
| 2026 | Febrero | WS | Error | SOPORTE | 1 | 3 |
| 2026 | Febrero | WS | Historia | COE | 3 | 25 |
| 2026 | Febrero | WS | Historia | Consulta totalizadores CBU/CVU Coelsa - CONSULTA POR CUENTA | 1 | 3 |
| 2026 | Febrero | WS | Historia | FCI Cuentas remuneradas: Ajustes finales Poincenot | 1 | 3 |
| 2026 | Febrero | WS | Historia | INICIATIVAS TECNICAS | 5 | 13 |
| 2026 | Febrero | WS | Historia | Impuestos wallet | 1 | 3 |
| 2026 | Febrero | WS | Historia | Mejorar recaudacion de impuestos wallet | 2 | 10 |
| 2026 | Febrero | WS | Historia | Pagos FX: APIs Consulta de cotizacion | 1 | 3 |
| 2026 | Febrero | WS | Historia | Que pagos con QR pasen por Ardid | 3 | 13 |
| 2026 | Febrero | WS | Historia | REQUERIMIENTOS INTERNOS WS | 2 | 6 |
| 2026 | Febrero | WS | Historia | SOPORTE | 7 | 18 |
| 2026 | Marzo | AD | Error | Codigos externos en orden de venta | 4 | 4 |
| 2026 | Marzo | AD | Error | DESA: Boton cancelar y filtros en apis | 3 | 3 |
| 2026 | Marzo | AD | Error | INICIATIVAS TECNICAS | 1 | 0.25 |
| 2026 | Marzo | AD | Error | Mayoristas - Mejorar UX portal | 4 | 2.5 |
| 2026 | Marzo | AD | Error | Mejorar integraciones: Sanear "Crear Entidad" desde el admin | 1 | 1 |
| 2026 | Marzo | AD | Error | Ministerio de Justicia - Asociar productos a transaccion | 7 | 6.25 |
| 2026 | Marzo | AD | Error | REGRESIONES AD | 4 | 6 |
| 2026 | Marzo | AD | Error | SOPORTE | 4 | 6 |
| 2026 | Marzo | AD | Historia | Boton Simple 2.0 | 1 | 1 |
| 2026 | Marzo | AD | Historia | COE | 1 | 3 |
| 2026 | Marzo | AD | Historia | Codigos externos en orden de venta | 1 | 1 |
| 2026 | Marzo | AD | Historia | INICIATIVAS TECNICAS | 1 | 1 |
| 2026 | Marzo | AD | Historia | Ministerio de Justicia - Asociar productos a transaccion | 1 | 1 |
| 2026 | Marzo | AD | Historia | SOPORTE | 1 | 1 |
| 2026 | Marzo | WS | Error | Mejorar integraciones: Poder dar soporte en altas cuenta | 1 | 0.5 |
| 2026 | Marzo | WS | Error | REGRESIONES WS | 1 | 0.5 |
| 2026 | Marzo | WS | Error | SOPORTE | 5 | 7.5 |
| 2026 | Marzo | WS | Error | Transferencias pull en Ardid | 5 | 4 |
| 2026 | Marzo | WS | Historia | COE | 1 | 3 |
| 2026 | Marzo | WS | Historia | Contracargos en debin recurrente | 2 | 21 |
| 2026 | Marzo | WS | Historia | FCI Cuentas remuneradas: Ajustes finales Poincenot | 1 | 0.5 |
| 2026 | Marzo | WS | Historia | INICIATIVAS TECNICAS | 5 | 21 |
| 2026 | Marzo | WS | Historia | Pagos FX MVP 2: APIs Alta de beneficiario | 1 | 3 |
| 2026 | Marzo | WS | Historia | Pagos FX: APIs Alta de beneficiario | 1 | 3 |
| 2026 | Marzo | WS | Historia | Pagos FX: APIs Crear pago FX | 6 | 40 |
| 2026 | Marzo | WS | Historia | Pagos FX: Wrapper MC Move | 1 | 3 |
| 2026 | Marzo | WS | Historia | REQUERIMIENTOS INTERNOS WS | 1 | 3 |
| 2026 | Marzo | WS | Historia | SOPORTE | 4 | 5 |
| 2026 | Abril | AD | Error | INICIATIVAS TECNICAS | 1 | 7 |
| 2026 | Abril | AD | Error | Mayoristas - Mejorar UX portal | 1 | 1 |
| 2026 | Abril | AD | Error | Mejorar integraciones: ABM de canales de cobro | 1 | 3 |
| 2026 | Abril | AD | Error | Ministerio de Justicia - Asociar productos a transaccion | 1 | 1 |
| 2026 | Abril | AD | Error | REGRESIONES AD | 3 | 7 |
| 2026 | Abril | AD | Error | SOPORTE | 10 | 22 |
| 2026 | Abril | AD | Historia | Ministerio de Justicia - Asociar productos a transaccion | 1 | 1 |
| 2026 | Abril | AD | Historia | Pagos FX - Portal Web | 3 | 29 |
| 2026 | Abril | AD | Historia | REGRESIONES AD | 1 | 3 |
| 2026 | Abril | AD | Historia | SOPORTE | 2 | 6 |
| 2026 | Abril | WS | Error | Contracargos en debin recurrente | 2 | 1 |
| 2026 | Abril | WS | Error | FCI Cuentas remuneradas: Ajustes finales Poincenot | 1 | 0.25 |
| 2026 | Abril | WS | Error | REGRESIONES WS | 3 | 3.5 |
| 2026 | Abril | WS | Error | REQUERIMIENTOS INTERNOS WS | 2 | 0.5 |
| 2026 | Abril | WS | Error | SOPORTE | 3 | 9 |
| 2026 | Abril | WS | Error | Transferencias pull en Ardid | 1 | 0.25 |
| 2026 | Abril | WS | Historia | COE | 1 | 7 |
| 2026 | Abril | WS | Historia | FCI Cuentas remuneradas: Ajustes finales Poincenot | 1 | 3 |
| 2026 | Abril | WS | Historia | INICIATIVAS TECNICAS | 1 | 1 |
| 2026 | Abril | WS | Historia | Pagos FX MVP 2: APIs Alta de beneficiario | 1 | 3 |
| 2026 | Abril | WS | Historia | Pagos FX: APIs Consulta de cotizacion | 1 | 1 |
| 2026 | Abril | WS | Historia | Pagos FX: APIs Crear pago FX | 1 | 3 |
| 2026 | Abril | WS | Historia | Pagos FX: Wrapper MC Move | 1 | 3 |
| 2026 | Abril | WS | Historia | SOPORTE | 10 | 16.5 |
| 2026 | Mayo | AD | Error | DESA: Boton cancelar y filtros en apis | 1 | 1 |
| 2026 | Mayo | AD | Error | Mayoristas - Mejorar UX portal | 10 | 7.25 |
| 2026 | Mayo | AD | Error | REGRESIONES AD | 1 | 0.25 |
| 2026 | Mayo | AD | Error | SOPORTE | 7 | 12 |
| 2026 | Mayo | AD | Historia | Boton Simple 2.0 | 1 | 3 |
| 2026 | Mayo | AD | Historia | DESA: Boton cancelar y filtros en apis | 1 | 1 |
| 2026 | Mayo | AD | Historia | SOPORTE | 1 | 3 |
| 2026 | Mayo | WS | Error | REGRESIONES WS | 1 | 0.5 |
| 2026 | Mayo | WS | Error | SOPORTE | 4 | 5.5 |
| 2026 | Mayo | WS | Historia | COE | 1 | 3 |
| 2026 | Mayo | WS | Historia | Contracargos en debin recurrente | 1 | 3 |
| 2026 | Mayo | WS | Historia | FCI Cuentas remuneradas: Ajustes finales Poincenot | 1 | 0 |
| 2026 | Mayo | WS | Historia | INICIATIVAS TECNICAS | 1 | 3 |
| 2026 | Mayo | WS | Historia | REGRESIONES WS | 1 | 3 |
| 2026 | Mayo | WS | Historia | SOPORTE | 3 | 7 |
| 2026 | Junio | AD | Error | Pagos FX - Portal Web | 4 | 5.5 |
| 2026 | Junio | AD | Error | SOPORTE | 4 | 8 |
| 2026 | Junio | AD | Historia | SOPORTE | 1 | 1 |
| 2026 | Junio | WS | Error | Contracargos en debin recurrente | 1 | 0.5 |
| 2026 | Junio | WS | Error | FCI Cuentas remuneradas: Ajustes finales Poincenot | 5 | 3 |
| 2026 | Junio | WS | Error | REGRESIONES WS | 2 | 2 |
| 2026 | Junio | WS | Error | SOPORTE | 1 | 3 |
| 2026 | Junio | WS | Historia | BFF onboarding | 1 | 1 |
| 2026 | Junio | WS | Historia | Bajar tiempos de pagos QR | 1 | 0 |
| 2026 | Junio | WS | Historia | COE | 4 | 4.75 |
| 2026 | Junio | WS | Historia | Contracargos en debin recurrente | 2 | 4 |
| 2026 | Junio | WS | Historia | DEVOLVER TITULARES CUENTA | 1 | 3 |
| 2026 | Junio | WS | Historia | SOPORTE | 4 | 9.25 |
| 2026 | Julio | AD | Error | COE | 1 | 0 |
| 2026 | Julio | AD | Error | COTO - Nuevo archivo liquidacion | 5 | 5 |
| 2026 | Julio | AD | Error | ECO Cerrado | 1 | 1 |
| 2026 | Julio | AD | Error | REGRESIONES AD | 1 | 1 |
| 2026 | Julio | AD | Error | SOPORTE | 2 | 1 |
| 2026 | Julio | AD | Historia | INICIATIVAS TECNICAS | 1 | 3 |
| 2026 | Julio | AD | Historia | POS con PRISMA: Admin | 1 | 1 |
| 2026 | Julio | WS | Error | Contracargos en debin recurrente | 1 | 3 |
| 2026 | Julio | WS | Error | REGRESIONES WS | 2 | 6 |
| 2026 | Julio | WS | Error | SOPORTE | 4 | 2.5 |
| 2026 | Julio | WS | Historia | COE | 7 | 4.75 |
| 2026 | Julio | WS | Historia | SOPORTE | 3 | 4 |
| 2026 | Agosto | AD | Error | Arreglar transferencias salientes de Agentes de Cobros y Pagos | 2 | 6 |
| 2026 | Agosto | AD | Error | Botón Simple 2.0 | 2 | 4 |
| 2026 | Agosto | AD | Error | COTO - Nuevo archivo liquidaciÃ³n | 5 | 5 |
| 2026 | Agosto | AD | Error | Cuotas CFT a clientes | 1 | 3 |
| 2026 | Agosto | AD | Error | ECO Cerrado | 1 | 1 |
| 2026 | Agosto | AD | Error | INICIATIVAS TÉCNICAS | 2 | 14 |
| 2026 | Agosto | AD | Error | Mejorar integraciones: ABM de canales de cobro | 1 | 3 |
| 2026 | Agosto | AD | Error | Ministerio de Justicia - Asociar productos a transacciÃ³n | 1 | 1 |
| 2026 | Agosto | AD | Error | POS | 1 | 1 |
| 2026 | Agosto | AD | Error | POS con PRISMA: Admin | 1 | 1 |
| 2026 | Agosto | AD | Error | REGRESIONES AD | 4 | 4 |
| 2026 | Agosto | AD | Error | SOPORTE | 11 | 19 |
| 2026 | Agosto | AD | Historia | Acomodar devoluciones parciales para COTO | 1 | 7 |
| 2026 | Agosto | AD | Historia | Arcos Dorados: mapear productos de la orden de venta en items del Resolve (QR eco cerrado) | 1 | 3 |
| 2026 | Agosto | AD | Historia | Arreglar transferencias salientes de Agentes de Cobros y Pagos | 3 | 21 |
| 2026 | Agosto | AD | Historia | Botón Simple 2.0 | 1 | 3 |
| 2026 | Agosto | AD | Historia | COE | 3 | 11 |
| 2026 | Agosto | AD | Historia | Carga masiva de deudas para ProvinciaNET | 5 | 4.5 |
| 2026 | Agosto | AD | Historia | Cobrar QR con tarjetas (MODO) | 5 | 17 |
| 2026 | Agosto | AD | Historia | INICIATIVAS TÉCNICAS | 7 | 16 |
| 2026 | Agosto | AD | Historia | Ministerio de Justicia - Asociar productos a transacciÃ³n | 3 | 19 |
| 2026 | Agosto | AD | Historia | PMC: SVA | 1 | 3 |
| 2026 | Agosto | AD | Historia | POS | 1 | 1 |
| 2026 | Agosto | AD | Historia | POS con PRISMA: Admin | 2 | 8 |
| 2026 | Agosto | AD | Historia | SOPORTE | 2 | 4 |
| 2026 | Agosto | WS | Error | Contracargos en debin recurrente | 1 | 3 |
| 2026 | Agosto | WS | Error | FCI Cuentas remuneradas: Ajustes finales Poincenot | 1 | 1 |
| 2026 | Agosto | WS | Error | REGRESIONES WS | 2 | 3.5 |
| 2026 | Agosto | WS | Error | SOPORTE | 3 | 2 |
| 2026 | Agosto | WS | Historia | COE | 3 | 4.25 |
| 2026 | Agosto | WS | Historia | Carga masiva de deudas para ProvinciaNET | 1 | 0.25 |
| 2026 | Agosto | WS | Historia | Conciliar saldos totales | 1 | 7 |
| 2026 | Agosto | WS | Historia | Contracargos en debin recurrente | 1 | 3 |
| 2026 | Agosto | WS | Historia | INICIATIVAS TÉCNICAS | 3 | 3 |
| 2026 | Agosto | WS | Historia | REQUERIMIENTOS INTERNOS WS | 1 | 3 |
| 2026 | Agosto | WS | Historia | SOPORTE | 2 | 3 |
| 2026 | Agosto | WS | Historia | Totalizadores en alta cuenta | 1 | 7 |

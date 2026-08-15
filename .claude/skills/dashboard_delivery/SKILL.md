---
name: dashboard_delivery
description: Ingesta de TRES insumos y regeneración del dashboard "Performance de desarrollo" (outputs/dashboard_performance_desarrollo.html): (1) el reporte de publicaciones del PM (Excel en raw/, tickets Historia/Error publicados en producción con Story Points, espacio y Epic), mergeado contra wiki/2_areas/control/log_performance_desarrollo.md; (2) el stock de horas mensual que factura Fintexa (Excel "Stock de Horas - <Mes><Año>"), mergeado contra wiki/2_areas/control/log_costos_desarrollo.md y cruzado con el primero para la métrica USD/SP (cuánto cuesta un punto de historia); (3) el SLA de tickets Prioridad=Highest (CSV "tiempo por estado" exportado de Jira), mergeado contra wiki/2_areas/control/log_sla_highest.md — tiempo de resolución de urgencias (reclamos/bugs/incendios), requiere que Claude consulte Jira por MCP (fixVersions/releaseDate) antes de ingerir. Tolera columnas nuevas/reordenadas y formato .xlsm/.xlsx/.csv, auto-detecta los formatos de origen, y rota los archivos a 4_archivos/historial_raw/. Estos reportes miden al equipo de desarrollo por lo ENTREGADO, su costo y su SLA de urgencias — no alimentan el conocimiento de producto de la wiki.
when_to_use: Se activa cuando el usuario ejecuta /dashboard_delivery tras depositar en raw/ el Excel mensual de publicaciones del PM (formato "METRICAS <MES> <AÑO> (Jira)..."), el Excel de stock de horas que factura Fintexa (formato "Stock de Horas - <Mes><Año>") y/o el CSV de SLA de tickets Highest (export Jira "tiempo por estado" filtrado a Prioridad=Highest). Uso mensual, a principio de cada mes; los insumos pueden llegar juntos o por separado. Skill de fuente compartida: la corre solo el runner designado (ver `identidad.local.md`).
disable-model-invocation: true
argument-hint: ""
---

# 📊 INGESTA MENSUAL DE DELIVERY: /dashboard_delivery

## 🔒 Paso -1 obligatorio — verificar que sos el runner

Leé `identidad.local.md` (raíz del repo). Si `runner_fuentes_compartidas` no es `true`, **abortá** con un mensaje claro: esta skill lee una fuente objetiva compartida entre los tres PM/PO — correrla en más de un cerebro triplica trabajo. Avisale al usuario quién es el runner designado.

## 🎯 Por qué existe esta skill

El PM de Bind PSP deja todos los principios de mes, en `raw/`, un export de Jira con todo lo **publicado en producción** el mes anterior (espacios WS/AD, y a futuro OB/SER). El objetivo NO es medir cuánto se desarrolló, sino cuánto se **entregó realmente** — la métrica existe para presionar calidad y completitud de delivery, no esfuerzo. Por eso solo cuenta lo publicado (`fixVersion`/estado Finalizada o No aplica), nunca lo "en curso".

**Regla dura (decisión del usuario, 2026-07-13): este reporte NO toca el conocimiento de producto de la wiki.** No se mergea a `detalle_productos/`, no se cruza con IDEAs de `1_proyectos/`. Es una métrica de management pura. El conocimiento de producto de publicaciones lo cubre `/sync_releases` — no te pises con esa skill.

**Desde 2026-07-21, la skill suma un segundo insumo mensual: el stock de horas que factura Fintexa** (software factory tercerizada, que factura un stock de horas mensual variable en cantidad y en composición de perfiles). Cruzado con el SP publicado, arma la métrica **USD/SP** (cuánto cuesta un punto de historia y cómo evoluciona ese costo) — pestaña "USD por SP" del dashboard. Es una fuente independiente con su propio log (`log_costos_desarrollo.md`); no reemplaza ni se mezcla con el log de delivery.

**Desde 2026-07-27, la skill suma un tercer insumo: el SLA de tickets Prioridad=Highest** (reclamos de clientes, bugs urgentes, incendios — el PM responde por resolverlos ASAP). Mide, por mes de **creación** del ticket (no de resolución — decisión del usuario: "las urgencias creadas en junio tardaron X días", no "cuánto se resolvió en junio"), dos tiempos: **días hasta Finalizada** (entrada a ese estado, calculado del export de tiempo-por-estado) y **días hasta Publicación** (fecha REAL de release de la versión que lo resolvió, vía Jira). Pestaña "SLA Highest" (líneas, mediana) + 2 KPI globales con toggle mediana/promedio. Fuente independiente con su propio log (`log_sla_highest.md`); no se mezcla con delivery ni costos. **Requiere un paso manual de Claude antes de ingerir** (ver Paso 1bis abajo) — a diferencia de los otros dos insumos, este no es 100% automatizable porque el export de Jira no trae fecha de release de versión.

## 🔌 Mecánica: motor genérico + template parametrizado

Toda la lógica de parseo/agregación/escritura vive en [`scripts/pipeline.py`](scripts/pipeline.py) (Python + openpyxl). El dashboard HTML es un **template** en [`assets/dashboard_template.html`](assets/dashboard_template.html) con tres placeholders (`__DATA_JSON__`, `__COSTOS_JSON__`, `__SUBTITLE__`) que el pipeline completa con los datos acumulados — nunca edites a mano `outputs/dashboard_performance_desarrollo.html` directamente; editá el template si hace falta cambiar el diseño, y correlo de nuevo.

**Archivos de control (fuente de verdad acumulada), uno por insumo — espejo read-only de `CEREBRO_CORE`:**
- [`wiki/3_recursos/datos/log_performance_desarrollo.md`](../../../wiki/3_recursos/datos/log_performance_desarrollo.md) — tabla año × mes × espacio × tipo × epic (delivery: tickets/SP publicados).
- [`wiki/3_recursos/datos/log_costos_desarrollo.md`](../../../wiki/3_recursos/datos/log_costos_desarrollo.md) — tabla año × mes × espacio (horas/USD de desarrollo) + registro de tarifas por perfil con su origen (propia o heredada).
- [`wiki/3_recursos/datos/log_sla_highest.md`](../../../wiki/3_recursos/datos/log_sla_highest.md) — SLA de tickets Highest.

**Contrato de escritura (pipeline multi-PM, 2026-08-15):** esta skill ya no escribe esos tres archivos directo — son espejo read-only en este install. `pipeline.py ingest` siembra una copia de trabajo en `contexto_vivo/_staging_dashboard_delivery/` desde el espejo y lee/reescribe ahí, exactamente igual que antes (**nunca hace falta releer los Excel históricos**, ya archivados en `4_archivos/historial_raw/`). Al cerrar, empaquetá esa carpeta como **un item `tipo: dato`** en `wiki/1_proyectos/contexto_vivo/`, `destino_propuesto: 3_recursos/datos/` — `/context_merge` lo aplica por copia byte a byte (ver Paso 5). El dashboard HTML (`outputs/`) no es canon, se sigue escribiendo directo.

**Tres formatos de origen, auto-detectados por header (`sniff_and_read` en `pipeline.py`) — no hay que elegir comando según el archivo, `inspect`/`ingest` funcionan igual con cualquiera de los tres, e incluso con varios formatos mezclados en un mismo workbook (`sniff_and_read` devuelve una LISTA de resultados, no uno solo):**
1. **Ticket-level** (export Jira mensual del PM): una fila por ticket, columnas "Clave de incidencia"/"Mes"/Epic. No trae año → se asume `ANIO_DEFAULT` del pipeline. Alimenta el log de **delivery**.
2. **Agregado por versión** (backfills históricos puntuales, ej. el de 2025 ingerido 2026-07-14): una fila por versión publicada, columnas `SP-US`/`SP-BUGS`/`Q-US`/`Q-BUGS`/"AÑO PUBLICACIÓN". **Sin Epic** — los registros quedan con `epic=null` (no `"(sin epic)"`): las vistas "por Epic" del dashboard excluyen esos registros del todo, así que esos meses se ven genuinamente vacíos en esa métrica en vez de acumularse en un bucket gris. Las vistas "por tipo" (Historia/Error) sí los incluyen normalmente. Alimenta el log de **delivery**.
3. **Stock de horas** (factura mensual de Fintexa, backfill inicial 2026-07-21): una fila por recurso asignado, hoja titulada "Stock de Horas - `<Mes><Año>`" (ej. "Stock de Horas - JUN26"), columnas "Componente / Proyecto" y "Horas Mes". Un mismo workbook puede traer varias hojas de este formato (ej. un archivo de control con varios meses). Alimenta el log de **costos**. Reglas de imputación (decisión del usuario 2026-07-21):
   - Horas de desarrollo = todas las secciones salvo `SOPORTE` e `IT`.
   - Componente → espacio: Wallet/Wallet Services/Wallet APK → WS; Cobro y Admin/BP/BO → AD; Onboarding/Onboarding PJ/OB-93 Legajos → OB; Deuda → SER; Todos y Comité de Arquitectura → 50%/50% WS-AD. Componente no reconocido → fila descartada + `[WARN]`, nunca se adivina.
   - Costo = fila por fila, `horas × tarifa del perfil de esa fila` — nunca un valor hora promedio (ver metodología en `log_costos_desarrollo.md`).
   - Tarifas faltantes: se hereda la del mes conocido más cercano (empate → gana el anterior); el registro de tarifas queda auditado con su origen.

Si aparece un cuarto formato de Excel en el futuro, sumar su propio lector siguiendo el mismo patrón (`read_*_ws` + registrar su firma en el dispatcher) en vez de forzarlo dentro de uno existente. El CSV de SLA Highest es un dispatcher aparte (`sniff_csv_format`), separado de los tres formatos de Excel.

## Paso 0 — Verificar insumo

Confirmá que haya al menos un `.xlsx`/`.xlsm`/`.csv` en `raw/` (ignorá locks `~$*`). Si no hay nada, avisá al usuario y terminá sin tocar nada.

## Paso 1bis — SOLO si hay CSV de SLA Highest: generar el JSON de fechas reales de versión

El export de tickets Highest (`Clave`/`Estado`/`Creada` + columnas de tiempo-por-estado) **no trae fecha de release de versión** — antes de correr `inspect`/`ingest`, para cada ticket con `Estado = Finalizada` del CSV:
1. Consultá Jira por MCP (`searchJiraIssuesUsingJql`, `cloudId: "bindpsp.atlassian.net"`, `jql: "key in (...)"`, `fields: ["fixVersions"]`) — en tandas de ~100 claves (el resultado se guarda a archivo si excede el límite de tokens; leelo con Python en vez de reintentar con menos claves).
2. Para cada ticket, quedate con las `fixVersions` que tengan `released: true` y `releaseDate` no vacío.
3. Escribí un JSON compañero en `raw/`, **mismo nombre que el CSV + `.versions.json`** (ej. `raw/2026-07-27 18-17-Highest.versions.json`), mapeando `Clave -> [fechas ISO]`.

Sin este archivo, `pipeline.py` degrada TODOS los tickets Finalizada de ese lote a la fecha proxy (entrada a "Finalizada") para "días hasta Publicación" y lo advierte con `[WARN]` — no es un error fatal, pero perdés precisión. Los tickets sin ninguna versión released con fecha (versión aún no liberada, o sin fixVersion cargado) degradan igual a la proxy individualmente, aunque el JSON exista para el resto del lote.

## Paso 1 — Inspección previa (obligatoria antes de escribir)

Corré, desde la raíz del repo:
```
python .claude/skills/dashboard_delivery/scripts/pipeline.py inspect
```
Esto lee cada Excel/CSV de `raw/` **por nombre de columna** (tolerante a que el proveedor agregue, reordene o renombre columnas secundarias) y reporta sin escribir nada:
- Delivery: totales tickets/SP por mes × espacio, para que cruces a ojo contra lo que esperás del reporte.
- Costos: horas/USD por mes × espacio, con la tarifa usada (`propia` o `heredada de <mes>`) y perfiles sin tarifa conocida.
- SLA Highest: filas leídas, cuántos tickets nuevos vs. ya existentes en el log, y el warning de cobertura del JSON de versiones (ver Paso 1bis).
- `[WARN]` de degradaciones: tickets sin Story Points (→ computan 0), valores de "Mes" no reconocidos (→ **excluidos**), componentes de stock de horas no mapeados (→ fila descartada), perfiles sin tarifa (→ USD 0 para esas horas), tickets Highest sin versión released con fecha (→ degradan a proxy).
- `[NUEVAS COLUMNAS no contempladas]`: columnas que el PM agregó y el pipeline no usa. Evaluá si aportan una métrica que el usuario querría ver — si es así, no la agregues por tu cuenta al dashboard; capturala como item `tipo: gap` (Paso 5) y preguntale al usuario en tu reporte final (más cambios de UI = decisión del usuario, no tuya).
- `[OVERLAP]`: combos que ya existen en el log correspondiente (delivery o costos) y que esta corrida **pisaría**. Es normal si el proveedor corrige un mes ya cargado; sospechoso si pisa muchos meses viejos sin motivo — si no entendés por qué, preguntá antes de seguir.

**Si el script aborta (`[ABORT]`)**: el archivo no matcheó ninguno de los formatos conocidos (ticket-level, agregado-por-versión, stock de horas, o SLA Highest). No lo resuelvas adivinando una columna al azar — es la señal de un formato realmente nuevo. Capturá el problema como item `tipo: gap` (severidad Alta) y consultá al usuario cómo mapearlo antes de tocar `pipeline.py`.

## Paso 2 — Ingesta real

Si la inspección se ve razonable, corré:
```
python .claude/skills/dashboard_delivery/scripts/pipeline.py ingest
```
Esto mergea (reemplazando por combo, o por `Clave` en el caso de SLA) todos los Excel/CSV de `raw/` contra los logs acumulados — delivery por año×mes×espacio×tipo×epic, costos por año×mes×espacio, SLA por ticket —, reescribe los tres `.md` completos (metodología + registro de lotes + resumen + detalle; el de costos además con el registro de tarifas por perfil) y regenera `outputs/dashboard_performance_desarrollo.html` desde el template con los tres datasets embebidos como JSON.

## Paso 3 — Verificación end-to-end (obligatoria, no alcanza con que el script no falle)

Abrí el dashboard regenerado en el Browser pane (`python -m http.server` sobre `outputs/`, navegar, y **apagar el server al terminar** — no lo dejes corriendo) y confirmá:
- Las 6 pestañas cambian la métrica del eje Y y la escala se adapta; el eje X es cronológico (puede abarcar más de un año si hubo backfill) y se lee sin ambigüedad (`Jul'25`, `Ene'26`, ...).
- El filtro por espacio (Todos/AD/WS/OB/SER/ARD) funciona sin errores de consola, incluso para espacios sin datos todavía (deben degradar a vacío/0, no romper).
- Las vistas "por Epic" muestran vacío (no un bucket "sin epic") en los meses cuyo origen no traía Epic — es el comportamiento esperado, no un bug.
- **Pestaña "USD por SP":** dibuja líneas (no áreas apiladas); una por espacio + línea global punteada con "Todos", una sola línea al filtrar un espacio; los espacios sin SP publicados ese mes (hoy OB y SER) quedan en 0, no ocultos.
- **Pestaña "SLA Highest":** dibuja 2 líneas (mediana), eje X = mes de `Creada` del ticket; los meses con urgencias aún sin resolver se ven en itálica; el toggle Mediana/Promedio de las 2 KPI globales cambia el valor sin recargar el gráfico.
- Las KPIs (SP y tickets publicados, promedio SP/mes histórico, % BAU, % SOPORTE, % Error, USD/SP histórico, **mediana/promedio días hasta Finalizada y hasta Publicación**) cuadran contra el resumen que imprimió el Paso 2.
- Colores fijos: SOPORTE en rojo, resto de epics BAU (regresiones, COE, iniciativas técnicas) con color constante, epics nuevas en escala de grises; en USD/SP, cada espacio reusa el color de su `REGRESIONES <espacio>`.

## Paso 4 — Rotación de `raw/` (obligatoria, protocolo del CLAUDE.md)

Para cada Excel/CSV procesado: moverlo a `wiki/4_archivos/historial_raw/YYYY-MM_<slug>/` (mes de la corrida actual, no el mes de los datos). Slugs usados por `cmd_ingest`: `reporte_pm_metricas_publicadas` (ticket-level), `backfill_historico` (agregado-por-versión), `backfill_stock_horas_fintexa` (stock de horas), `sla_highest_jira` (SLA Highest). El CSV de SLA y su JSON compañero (`<csv>.versions.json`) se rotan juntos, al mismo destino. Confirmar `raw/` vacía en el reporte final al usuario.

## Paso 5 — Empaquetar y cerrar

1. **Empaquetá `contexto_vivo/_staging_dashboard_delivery/` como item `tipo: dato`** en `wiki/1_proyectos/contexto_vivo/`, `destino_propuesto: 3_recursos/datos/`. Cuerpo del item: resumen de qué cambió (ingesta <mes(es)> <espacio(s)>, N tickets / M SP; costos con horas/USD si aplicó; SLA Highest con N tickets y mediana de días si aplicó) — el merge lo usa para redactar su línea de changelog, no hace falta que redactes vos ese changelog.
2. Si hubo `[WARN]` o `[NUEVAS COLUMNAS]` sin resolver: capturalos como item `tipo: gap` (`destino_propuesto: 2_areas/gaps_y_preguntas.md`) y mencionalos al usuario explícitamente — no los archives en silencio.
3. Regenerá `contexto_vivo/index.md`. **Sin git** — el commit del repo personal lo hace el hook `SessionStart` una vez al día.

## ⚠️ Gotchas conocidos

- **`ANIO_DEFAULT` para el formato ticket-level:** el export mensual del PM no trae columna de año, así que el pipeline le asigna `ANIO_DEFAULT` (hoy 2026). Cuando el calendario cruce a 2027 sin que el PM cambie el formato, hay que bumpear esa constante a mano antes de la primera ingesta de 2027 (o, mejor, pedirle al PM que agregue una columna de año y leerla de ahí). El formato agregado-por-versión no tiene este problema: siempre trae "AÑO PUBLICACIÓN" explícito.
- **Epic ausente = `epic: null`, no `"(sin epic)"`:** es una decisión de diseño explícita (usuario, 2026-07-14) para que las vistas "por Epic" muestren esos meses genuinamente vacíos en vez de un bucket gris que mezclaría todo. Si alguna vez hace falta lo contrario (mostrar un bucket agregado), es un cambio de diseño a discutir con el usuario, no algo para decidir en la marcha.
- **Espacios OB/SER:** el dashboard y el filtro ya los contemplan aunque hoy no tengan datos (degradan a 0/vacío). No hace falta tocar nada cuando el PM empiece a incluirlos — el pipeline agrega cualquier espacio nuevo que aparezca en la clave del ticket o en `PRODUCTO` (`ESPACIOS = [...new Set([base + los de DATA])]` en el template; `VA_PRODUCTO_MAP` en `pipeline.py` para el formato agregado-por-versión).
- **Múltiples Excel a la vez en `raw/`:** el pipeline procesa todos, en orden alfabético de nombre de archivo (sea cual sea su formato); si dos traen el mismo combo año×mes×espacio, gana el último procesado. Si llegan dos archivos juntos (ej. una corrección, o un mes regular + un backfill), fijate en el orden antes de asumir cuál "gana".
- **SP nulos:** computan 0 automáticamente (no descartes el ticket, sigue contando como publicado).
- **Migración automática del log legacy:** `parse_log()` reconoce tanto el formato viejo de la tabla detalle (6 columnas, sin Año — asume `ANIO_DEFAULT`) como el nuevo (7 columnas, con Año). No hace falta migrar el archivo a mano; la primera corrida con el pipeline nuevo ya reescribe todo en 7 columnas.
- **Stock de horas — el período confiable es el nombre de la hoja, no A1 ni el rótulo "Total stock":** el proveedor no siempre actualiza esos textos (ej. una hoja "JUL25" con rótulo "Total stock Mayo 2025"). `read_stock_ws` parsea el período del título de la hoja (`STOCK_SHEET_RE`), nunca de esas celdas.
- **Stock de horas — bloques retroactivos post-"Total stock":** algún mes (ej. Sep'25) agrega, después de la fila "Total stock ...", un bloque de horas de un mes anterior no informado a tiempo. `read_stock_ws` corta el parseo en la primera fila que contenga "total stock" — si un mes futuro necesita sumar ese ajuste retroactivo, es una decisión a tomar con el usuario, no algo para inferir en automático.
- **Stock de horas — carry-forward de tarifas:** cuando el Excel de un mes no trae su propia tabla de precios, se hereda del mes conocido más cercano (empate → gana el anterior), resolviéndose contra **todo el historial acumulado en `log_costos_desarrollo.md`**, no solo contra los archivos del lote actual — por eso `cmd_ingest` junta los segmentos de TODOS los Excel de `raw/` antes de resolver tarifas (si lo hiciera archivo por archivo, un mes sin tabla propia procesado antes de encontrar la tarifa conocida más cercana quedaría en USD 0). Cada fila del registro de tarifas indica su origen (`propia` o `heredada de <mes>`) a modo de auditoría.
- **Stock de horas — mismo período en dos archivos:** igual que en delivery, si dos Excel traen la misma hoja de mes (ej. un archivo de control viejo y el archivo mensual dedicado), gana el último procesado en orden alfabético — no se suman ambos.
- **Componente/producto desconocido en el stock de horas:** la fila se descarta y se advierte con `[WARN]`, nunca se imputa por adivinanza. Ampliar `STOCK_COMPONENTE_MAP`/`STOCK_SPLIT` en `pipeline.py` si aparece un componente nuevo genuino.
- **Ventana de ingesta del stock de horas:** `STOCK_SKIP_PERIODS` excluye explícitamente los meses anteriores a la cobertura del log de delivery (hoy Ene'25 y Jun'25) — se muestran en `inspect` a modo informativo pero `ingest` los descarta.

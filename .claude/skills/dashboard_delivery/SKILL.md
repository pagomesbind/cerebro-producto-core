---
name: dashboard_delivery
description: Ingesta de insumos y regeneración del dashboard "Pulso de Delivery" (outputs/dashboard_performance_desarrollo.html — un único gráfico de línea con selector de métrica, tamaño de ventana móvil y espacio): (1) el export histórico consolidado de tickets del PM (Excel en raw/, TODO lo publicado en producción hasta la fecha — Historia/Error con Story Points, espacio, Epic, Estado y Año por fila), que reemplaza por completo el tramo que cubre en wiki/3_recursos/datos/log_performance_desarrollo.md; (2) el stock de horas mensual que factura Fintexa (Excel "Stock de Horas - <Mes><Año>"), mergeado contra wiki/3_recursos/datos/log_costos_desarrollo.md y cruzado con el primero para USD/SP, USD/Horas y Horas/SP; (3) opcionalmente el SLA de tickets Prioridad=Highest (CSV "tiempo por estado" exportado de Jira), que sigue acumulándose en wiki/3_recursos/datos/log_sla_highest.md aunque ya no se visualiza en este dashboard. Tolera columnas nuevas/reordenadas y formato .xlsm/.xlsx/.csv, auto-detecta los formatos de origen, salta (sin abortar la corrida) cualquier archivo de raw/ que no matchee ninguno, y rota los archivos procesados a 4_archivos/historial_raw/. Mide al equipo de desarrollo por lo ENTREGADO y su costo — no alimenta el conocimiento de producto de la wiki.
when_to_use: Se activa cuando el usuario ejecuta /dashboard_delivery tras depositar en raw/ el export histórico consolidado de tickets del PM (todo lo publicado hasta la fecha, no solo el mes) y el/los Excel de stock de horas de Fintexa de los meses nuevos a sumar (formato "Stock de Horas - <Mes><Año>"). Uso mensual, a principio de cada mes. Skill de fuente compartida: la corre solo el runner designado (ver `identidad.local.md`).
disable-model-invocation: true
argument-hint: ""
---

# 📊 INGESTA MENSUAL DE DELIVERY: /dashboard_delivery

## 🔒 Paso -1 obligatorio — verificar que sos el runner

Leé `identidad.local.md` (raíz del repo). Si `runner_fuentes_compartidas` no es `true`, **abortá** con un mensaje claro: esta skill lee una fuente objetiva compartida entre los tres PM/PO — correrla en más de un cerebro triplica trabajo. Avisale al usuario quién es el runner designado.

## 🎯 Por qué existe esta skill

El objetivo NO es medir cuánto se desarrolló, sino cuánto se **entregó realmente** — la métrica existe para presionar calidad y completitud de delivery, no esfuerzo. Por eso solo cuenta lo publicado (Estado Finalizada o No aplica), nunca lo "en curso".

**Regla dura (decisión del usuario, 2026-07-13): este reporte NO toca el conocimiento de producto de la wiki.** No se mergea a `detalle_productos/`, no se cruza con IDEAs de `1_proyectos/`. Es una métrica de management pura. El conocimiento de producto de publicaciones lo cubre `/sync_releases` — no te pises con esa skill.

**Desde 2026-07-21, la skill cruza el delivery con el stock de horas que factura Fintexa** (software factory tercerizada, que factura un stock de horas mensual variable en cantidad y en composición de perfiles) — de ahí salen USD, Horas, USD/Hora, Horas/SP y USD/SP. Es una fuente independiente con su propio log (`log_costos_desarrollo.md`); no reemplaza ni se mezcla con el log de delivery.

**Desde 2026-09-16, el PM dejó de mandar un Excel mensual incremental: ahora manda, en cada invocación, el export histórico consolidado completo** (todo lo publicado desde que existe registro, no solo el mes) — con Mes numérico, columna Año propia y columna Estado (a diferencia del viejo formato de texto en español sin año, que se cuenta como pre-filtrado). El pipeline lo trata como lo que es: un reemplazo completo de cada año×mes×espacio que el archivo cubre (ver `cmd_ingest`), filtrando primero a Estado ∈ {Finalizada, No aplica} — un export histórico trae de todo, no solo lo publicado.

**Rediseño del dashboard (2026-09-16, decisión del usuario):** "Pulso de Delivery" reemplazó el dashboard anterior de 6 pestañas (por Epic/tipo, USD por SP, SLA Highest) por un único gráfico de línea con tres selectores — métrica (SP, Horas, USD, USD/Horas, Horas/SP, USD/SP, % Mantenimiento), tamaño de ventana móvil (1/3/6 meses) y espacio — más 2 KPIs y una tabla de datos colapsable. Un período de N meses es **ventana móvil, sum/sum**: cada punto suma los últimos N meses (nunca promedia ratios mensuales), y un tamaño de ventana grande arranca más tarde en la serie porque necesita N meses de historia antes del primer punto — decisión explícita del usuario sobre la alternativa de bloques fijos no solapados. La curva usa interpolación monótona (Fritsch-Carlson), no Catmull-Rom: se ve suave pero nunca inventa un máximo/mínimo que no sea un punto real. Todo punto conocido se dibuja en la línea (aunque su etiqueta del eje X se omita si hay muchos puntos, para no amontonar). Colores: azul Bind (`#4c65e6`/`#33449e`, el mismo de `pdf_build`/`pptx_build`), no la paleta genérica anterior.

El **SLA Highest** (Paso 1bis y su log, más abajo) se sigue acumulando igual que antes — solo dejó de visualizarse en este HTML. Si en el futuro hace falta volver a mostrarlo (u otra vista adicional), es una decisión de diseño a discutir con el usuario, no algo para reintroducir por tu cuenta.

## 🔌 Mecánica: motor genérico + template parametrizado

Toda la lógica de parseo/agregación/escritura vive en [`scripts/pipeline.py`](scripts/pipeline.py) (Python + openpyxl). El dashboard HTML es un **template** en [`assets/dashboard_template.html`](assets/dashboard_template.html) con dos placeholders de datos (`__DATA_JSON__`, `__COSTOS_JSON__`, cada uno dentro de su propio `<script type="application/json">` — nunca dentro de un string JS entre comillas simples, porque texto libre de Jira con comillas dobles rompe ese escapado) más `__SUBTITLE__`; el propio template agrega delivery+costos a nivel mes×espacio y arma las ventanas móviles en el navegador — el pipeline nunca pre-agrega esa parte. Nunca edites a mano `outputs/dashboard_performance_desarrollo.html` directamente; editá el template si hace falta cambiar el diseño, y correlo de nuevo.

**Archivos de control (fuente de verdad acumulada), uno por insumo — espejo read-only de `CEREBRO_CORE`:**
- [`wiki/3_recursos/datos/log_performance_desarrollo.md`](../../../wiki/3_recursos/datos/log_performance_desarrollo.md) — tabla año × mes × espacio × tipo × epic (delivery: tickets/SP publicados).
- [`wiki/3_recursos/datos/log_costos_desarrollo.md`](../../../wiki/3_recursos/datos/log_costos_desarrollo.md) — tabla año × mes × espacio (horas/USD de desarrollo) + registro de tarifas por perfil con su origen (propia o heredada).
- [`wiki/3_recursos/datos/log_sla_highest.md`](../../../wiki/3_recursos/datos/log_sla_highest.md) — SLA de tickets Highest.

**Contrato de escritura (pipeline multi-PM, 2026-08-15):** esta skill ya no escribe esos tres archivos directo — son espejo read-only en este install. `pipeline.py ingest` siembra una copia de trabajo en `contexto_vivo/_staging_dashboard_delivery/` desde el espejo y lee/reescribe ahí, exactamente igual que antes (**nunca hace falta releer los Excel históricos**, ya archivados en `4_archivos/historial_raw/`). Al cerrar, empaquetá esa carpeta como **un item `tipo: dato`** en `wiki/1_proyectos/contexto_vivo/`, `destino_propuesto: 3_recursos/datos/` — `/context_merge` lo aplica por copia byte a byte (ver Paso 5). El dashboard HTML (`outputs/`) no es canon, se sigue escribiendo directo.

**Tres formatos de origen, auto-detectados por header (`sniff_and_read` en `pipeline.py`) — no hay que elegir comando según el archivo, `inspect`/`ingest` funcionan igual con cualquiera de los tres, e incluso con varios formatos mezclados en un mismo workbook (`sniff_and_read` devuelve una LISTA de resultados, no uno solo). Un archivo que no matchea ninguno se saltea con `[ABORT-ARCHIVO]` — no aborta el resto de la corrida; `raw/` puede traer, aparte, insumos de otras skills.**
1. **Ticket-level**, dos variantes (columnas "Clave de incidencia"/"Mes"/Epic en ambas):
   - **Export histórico consolidado** (el que manda el PM desde 2026-09-16, en cada invocación): Mes **numérico** (1-12) + columna **Año** propia + columna **Estado** → se filtra a Estado ∈ {Finalizada, No aplica} antes de sumar (única fuente de "publicado" — un histórico trae de todo, Bloqueado/EN QA incluido). Como siempre trae la historia completa, el upsert normal por año×mes×espacio ya logra el reemplazo total de cada combo que cubre — no hace falta lógica especial de "full reload".
   - **Reporte mensual legacy** (formato viejo, por si vuelve a aparecer): Mes en texto español, sin columna Año → se asume `ANIO_DEFAULT` del pipeline; sin columna Estado → se asume pre-filtrado a publicado, no se filtra nada más.
   Alimenta el log de **delivery** en ambos casos.
2. **Agregado por versión** (backfills históricos puntuales, ej. el de 2025 ingerido 2026-07-14): una fila por versión publicada, columnas `SP-US`/`SP-BUGS`/`Q-US`/`Q-BUGS`/"AÑO PUBLICACIÓN". **Sin Epic** — los registros quedan con `epic=null` (no `"(sin epic)"`): el % de SP en mantenimiento del dashboard excluye esos meses del todo (sin dato, no 0%) en vez de tratarlos como no-mantenimiento. El SP total sí los suma normalmente. Alimenta el log de **delivery**.
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

**Si el script reporta `[ABORT-ARCHIVO]`** para alguno: ese archivo puntual no matcheó ninguno de los formatos conocidos (ticket-level, agregado-por-versión, stock de horas, o SLA Highest) — se saltea solo, el resto de `raw/` sigue procesándose. No lo resuelvas adivinando una columna al azar: si el archivo saltado es uno de los insumos esperados de esta skill (no un archivo ajeno que quedó de otra tarea), es la señal de un formato realmente nuevo — capturá el problema como item `tipo: gap` (severidad Alta) y consultá al usuario cómo mapearlo antes de tocar `pipeline.py`.

## Paso 2 — Ingesta real

Si la inspección se ve razonable, corré:
```
python .claude/skills/dashboard_delivery/scripts/pipeline.py ingest
```
Esto mergea (reemplazando por combo, o por `Clave` en el caso de SLA) todos los Excel/CSV de `raw/` contra los logs acumulados — delivery por año×mes×espacio×tipo×epic, costos por año×mes×espacio, SLA por ticket —, reescribe los tres `.md` completos (metodología + registro de lotes + resumen + detalle; el de costos además con el registro de tarifas por perfil) y regenera `outputs/dashboard_performance_desarrollo.html` desde el template con delivery y costos embebidos como JSON (el SLA se acumula en su log pero ya no se embebe en este dashboard).

## Paso 3 — Verificación end-to-end (obligatoria, no alcanza con que el script no falle)

Abrí el dashboard regenerado en el Browser pane (`python -m http.server` sobre `outputs/`, navegar, y **apagar el server al terminar** — no lo dejes corriendo) y confirmá:
- Sin errores de consola al cargar (el bug clásico acá es un `JSON.parse` roto — ver gotcha de `</script>`/comillas más abajo si aparece uno).
- Los 7 botones de métrica (SP, Horas, USD, USD/Horas, Horas/SP, USD/SP, % Mantenimiento) cambian el título, la escala del eje Y y las KPIs; los 3 botones de tamaño de ventana (1/3/6 meses) cambian cuántos puntos se ven y desde qué mes arranca la serie (un tamaño mayor arranca más tarde — necesita esa cantidad de meses de historia).
- El filtro por espacio (Todos/AD/WS/OB/SER/ARD, o cualquier espacio nuevo que haya aparecido en los datos) funciona sin romper — un espacio sin SP publicado degrada a KPIs "—"/"sin datos" y una nota explicando por qué, no a un gráfico roto.
- **Cada punto conocido tiene un punto visible sobre la línea**, incluso si su etiqueta del eje X no se muestra (se thinnea si hay muchos puntos) — no debería faltar ningún punto por "amontonamiento".
- La curva es suave pero **no dibuja un máximo/mínimo entre dos puntos reales que no exista en los datos** — pasá el mouse por tramos con cambios bruscos de pendiente para confirmarlo (era el bug de Catmull-Rom que motivó cambiar a interpolación monótona).
- % Mantenimiento da vacío/sin dato en los meses que no tengan Epic conocida (backfills viejos sin ese detalle) — no un 0% ni un bucket inventado.
- La tabla de datos colapsable (`Ver tabla de datos`) lista todos los puntos visibles del período/métrica actual, más reciente primero.
- El tooltip al pasar el mouse muestra mes + valor del punto más cercano; el color del tema es azul Bind (`#4c65e6` claro / `#94a3f0` oscuro), no verde ni la paleta genérica anterior.

## Paso 4 — Rotación de `raw/` (obligatoria, protocolo del CLAUDE.md)

Para cada Excel/CSV procesado: moverlo a `wiki/4_archivos/historial_raw/YYYY-MM_<slug>/` (mes de la corrida actual, no el mes de los datos). Slugs usados por `cmd_ingest`: `reporte_pm_metricas_publicadas` (ticket-level), `backfill_historico` (agregado-por-versión), `backfill_stock_horas_fintexa` (stock de horas), `sla_highest_jira` (SLA Highest). El CSV de SLA y su JSON compañero (`<csv>.versions.json`) se rotan juntos, al mismo destino. Confirmar `raw/` vacía en el reporte final al usuario.

## Paso 5 — Empaquetar y cerrar

1. **Empaquetá `contexto_vivo/_staging_dashboard_delivery/` como item `tipo: dato`** en `wiki/1_proyectos/contexto_vivo/`, `destino_propuesto: 3_recursos/datos/`. Cuerpo del item: resumen de qué cambió (ingesta <mes(es)> <espacio(s)>, N tickets / M SP; costos con horas/USD si aplicó; SLA Highest con N tickets y mediana de días si aplicó) — el merge lo usa para redactar su línea de changelog, no hace falta que redactes vos ese changelog.
2. Si hubo `[WARN]` o `[NUEVAS COLUMNAS]` sin resolver: capturalos como item `tipo: gap` (`destino_propuesto: 2_areas/gaps_y_preguntas.md`) y mencionalos al usuario explícitamente — no los archives en silencio.
3. Regenerá `contexto_vivo/index.md`. **Sin git** — el commit del repo personal lo hace el hook `SessionStart` una vez al día.

## ⚠️ Gotchas conocidos

- **`ANIO_DEFAULT` casi nunca aplica ya:** el export histórico consolidado (el flujo normal desde 2026-09-16) siempre trae su propia columna Año por fila, así que este default solo entra en juego si alguna vez vuelve a llegar el formato mensual legacy sin esa columna. No hace falta bumpearlo a mano en el cambio de año para el flujo normal.
- **Estado sin columna → no se filtra nada:** si un ticket-level no trae columna "Estado" (el legacy mensual del PM), el pipeline asume que ya viene pre-filtrado a publicado y cuenta todo lo listado. Si alguna vez ese supuesto deja de valer (el PM manda un legacy con estados mezclados), hay que sumarle la columna Estado al archivo, no parchear la excepción en el pipeline.
- **`</script>` o comillas dobles en texto libre de Jira:** los datos van en `<script type="application/json">` (no en un string JS entre comillas simples) precisamente porque un Epic con comillas dobles adentro (ej. `Sanear "Crear Entidad"`) rompe el escapado si pasa por un string JS primero. `write_dashboard` además reemplaza cualquier `</script` literal por `<\/script` antes de embeber — si el error de consola es un `JSON.parse` roto después de editar el template, sospechá primero de este punto antes de tocar el pipeline.
- **Epic ausente = `epic: null`, no `"(sin epic)"`:** es una decisión de diseño explícita (usuario, 2026-07-14). El dashboard actual no tiene vistas por Epic, pero el Epic sigue alimentando el % de SP en mantenimiento — un mes sin Epic conocida queda sin dato en esa métrica en vez de contarlo como 0% o inventar un bucket.
- **Espacios OB/SER/ARD:** el dashboard y el filtro ya los contemplan aunque hoy no tengan SP publicado (degradan a 0/"sin datos", con nota explicativa). No hace falta tocar nada cuando el PM empiece a incluirlos — el template arma `ESPACIOS` dinámicamente a partir de lo que trae `DATA`/`COSTOS`, sumando cualquier prefijo nuevo a los de siempre (`ESPACIOS_BASE`); `VA_PRODUCTO_MAP` en `pipeline.py` sigue haciendo falta para el formato agregado-por-versión.
- **`[ABORT-ARCHIVO]` no aborta la corrida:** si `raw/` trae, aparte de los insumos de esta skill, algún archivo ajeno (de otra tarea del PM), el pipeline lo saltea con este aviso y sigue con el resto — no hace falta sacarlo de `raw/` antes de correr `inspect`/`ingest`, aunque igual conviene avisarle al usuario que quedó ahí por si es de otra skill.
- **Múltiples Excel a la vez en `raw/`:** el pipeline procesa todos, en orden alfabético de nombre de archivo (sea cual sea su formato); si dos traen el mismo combo año×mes×espacio, gana el último procesado. Si llegan dos archivos juntos (ej. una corrección, o un mes regular + un backfill), fijate en el orden antes de asumir cuál "gana".
- **SP nulos:** computan 0 automáticamente (no descartes el ticket, sigue contando como publicado).
- **Migración automática del log legacy:** `parse_log()` reconoce tanto el formato viejo de la tabla detalle (6 columnas, sin Año — asume `ANIO_DEFAULT`) como el nuevo (7 columnas, con Año). No hace falta migrar el archivo a mano; la primera corrida con el pipeline nuevo ya reescribe todo en 7 columnas.
- **Stock de horas — el período confiable es el nombre de la hoja, no A1 ni el rótulo "Total stock":** el proveedor no siempre actualiza esos textos (ej. una hoja "JUL25" con rótulo "Total stock Mayo 2025"). `read_stock_ws` parsea el período del título de la hoja (`STOCK_SHEET_RE`), nunca de esas celdas.
- **Stock de horas — bloques retroactivos post-"Total stock":** algún mes (ej. Sep'25) agrega, después de la fila "Total stock ...", un bloque de horas de un mes anterior no informado a tiempo. `read_stock_ws` corta el parseo en la primera fila que contenga "total stock" — si un mes futuro necesita sumar ese ajuste retroactivo, es una decisión a tomar con el usuario, no algo para inferir en automático.
- **Stock de horas — carry-forward de tarifas:** cuando el Excel de un mes no trae su propia tabla de precios, se hereda del mes conocido más cercano (empate → gana el anterior), resolviéndose contra **todo el historial acumulado en `log_costos_desarrollo.md`**, no solo contra los archivos del lote actual — por eso `cmd_ingest` junta los segmentos de TODOS los Excel de `raw/` antes de resolver tarifas (si lo hiciera archivo por archivo, un mes sin tabla propia procesado antes de encontrar la tarifa conocida más cercana quedaría en USD 0). Cada fila del registro de tarifas indica su origen (`propia` o `heredada de <mes>`) a modo de auditoría.
- **Stock de horas — mismo período en dos archivos:** igual que en delivery, si dos Excel traen la misma hoja de mes (ej. un archivo de control viejo y el archivo mensual dedicado), gana el último procesado en orden alfabético — no se suman ambos.
- **Componente/producto desconocido en el stock de horas:** la fila se descarta y se advierte con `[WARN]`, nunca se imputa por adivinanza. Ampliar `STOCK_COMPONENTE_MAP`/`STOCK_SPLIT` en `pipeline.py` si aparece un componente nuevo genuino.
- **Ventana de ingesta del stock de horas:** `STOCK_SKIP_PERIODS` excluye explícitamente los meses anteriores a la cobertura del log de delivery (hoy Ene'25 y Jun'25) — se muestran en `inspect` a modo informativo pero `ingest` los descarta.

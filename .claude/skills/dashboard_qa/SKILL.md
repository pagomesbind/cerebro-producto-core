---
name: dashboard_qa
description: Ingesta mensual del export de Jira "Tiempo QA" (CSV, tiempo acumulado por estado de cada ticket de desarrollo) y regeneración del dashboard "Performance de QA" (outputs/dashboard_performance_qa.html), mergeado contra wiki/3_recursos/datos/log_performance_qa.md (log por ticket, upsert por Clave — no por mes). Mide al equipo de QA de Bind PSP (Andrea Orsini, Bethania Tornari, Ana Moreno) en tres frentes: tiempo en QA, observaciones creadas ([OBS]/[DEF]/[REQ]) y tiempo por Story Point, con filtro por Proyecto y por Analista (Equipo QA agregado o una persona puntual/Otros), y eje X anclable a 3 fechas (creación / asignación a QA / resolución). Métrica de management del equipo de QA — no toca conocimiento de producto de la wiki.
when_to_use: Se activa cuando el usuario ejecuta /dashboard_qa tras depositar en raw/ un export CSV de Jira "Tiempo QA" (una fila por ticket, columnas de metadata + una columna de tiempo acumulado por cada estado del workflow). Uso mensual, a demanda — sin fecha fija como /dashboard_delivery, ya que el reporte lo genera el usuario manualmente desde Jira. Skill de fuente compartida: la corre solo el runner designado (ver `identidad.local.md`).
disable-model-invocation: true
argument-hint: ""
---

# 📊 INGESTA MENSUAL DE QA: /dashboard_qa

## 🔒 Paso -1 obligatorio — verificar que sos el runner

Leé `identidad.local.md` (raíz del repo). Si `runner_fuentes_compartidas` no es `true`, **abortá** con un mensaje claro: esta skill lee una fuente objetiva compartida entre los tres PM/PO. Avisale al usuario quién es el runner designado.

## 🎯 Por qué existe esta skill

El equipo de QA de Bind PSP (Andrea Orsini, Bethania Tornari, Ana Moreno — área IT, ver [`equipo.md`](../../../wiki/2_areas/overview_empresa/overview_equipo.md)) testea en staging los desarrollos del proveedor antes de aprobar el pase a producción (estado `EN QA` de Jira). No había ninguna métrica de cuánto tarda ese paso ni de cuántas observaciones encuentra — esta skill lo mide, con la misma filosofía que `/dashboard_delivery` pero para QA en vez de desarrollo: es una métrica de **management del equipo**, no alimenta el conocimiento de producto de `detalle_productos/`.

**Nace 2026-07-27**, a partir de un export manual de Jira que el usuario genera (columnas configurables desde el selector de columnas de Jira — no un formato estándar de la API). Decisiones de diseño completas en [`2_areas/direccion/decisiones.md`](../../../wiki/2_areas/direccion/decisiones.md) (2026-07-27).

## 🔌 Mecánica: motor + template, igual patrón que `/dashboard_delivery`

Toda la lógica de parseo/agregación/escritura vive en [`scripts/pipeline.py`](scripts/pipeline.py) (Python puro, sin dependencias — lee CSV con `csv.DictReader`). El dashboard HTML es un **template** en [`assets/dashboard_template.html`](assets/dashboard_template.html) con dos placeholders (`__DATA_JSON__`, `__SUBTITLE__`) que el pipeline completa con los tickets acumulados como JSON embebido — toda la agregación por mes/analista/proyecto ocurre en el navegador (JS), no en Python. **Nunca edites a mano** `outputs/dashboard_performance_qa.html`; editá el template si hace falta cambiar el diseño, y corré `ingest` de nuevo.

**Archivo de control (fuente de verdad acumulada) — espejo read-only de `CEREBRO_CORE`:** [`wiki/3_recursos/datos/log_performance_qa.md`](../../../wiki/3_recursos/datos/log_performance_qa.md) — a diferencia de `/dashboard_delivery` (que acumula agregados año×mes×espacio), este log acumula **una fila por ticket** (`Clave`), con upsert por clave en cada ingesta. Motivo: un ticket creado en un mes puede seguir en `EN QA` meses después — su tiempo en QA cambia entre exports. Guardando el detalle por ticket, cualquier export (completo o parcial del último mes) deja el estado acumulado correcto, y los agregados mensuales se recalculan enteros desde ese detalle en cada corrida — **nunca hace falta releer los CSV históricos**.

**Contrato de escritura (pipeline multi-PM, 2026-08-15):** esta skill ya no escribe ese log directo — es espejo read-only en este install. `pipeline.py ingest` siembra una copia de trabajo en `contexto_vivo/_staging_dashboard_qa/` desde el espejo y lee/reescribe ahí, exactamente igual que antes. Al cerrar, empaquetá esa carpeta como **un item `tipo: dato`** en `wiki/1_proyectos/contexto_vivo/`, `destino_propuesto: 3_recursos/datos/log_performance_qa.md` — `/context_merge` lo aplica por copia byte a byte (ver Paso 5). El dashboard HTML (`outputs/`) no es canon, se sigue escribiendo directo.

**Formato de origen — único conocido, sin auto-detección de variantes:** una fila por ticket, con columnas de metadata (`Clave`, `Tipo de Incidencia`, `Resumen`, `Estado`, `Creada`, `Proyecto`, `Persona asignada`, `Creador`, opcionalmente `Resuelta`/`Story Points`/`Prioridad`) + una columna por cada estado del workflow con el tiempo acumulado en formato Jira (`"1M 2w 3d 4h 5m"`, con signo opcional por token, ej. `"-1w"`). El proveedor parte un mismo estado lógico en varias columnas según la variante de workflow del proyecto (ej. `EN QA` / `EN QA-10269` / `EN QA-10234`) — `pipeline.py` las suma todas (`COLS_QA`, `COLS_DEFECTO`, `COLS_PRE_QA`). Cualquier columna de estado nueva que no esté ni en esas listas ni en `KNOWN_UNUSED_STATUS_COLS` dispara `[NUEVAS COLUMNAS]` en vez de ignorarse en silencio.

**Eje X con 3 anclas, "por asignación a QA" es la default (2026-07-27):** el pipeline calcula `mes_asignacion_qa` = mes de (`Creada` + Σ(columnas previas a `EN QA`: Backlog/Asignado/Listo para desarrollo/En curso, `COLS_PRE_QA`)) — el mes en que el ticket entró por primera vez a `EN QA`. Es la ancla del eje X con menos sesgo de censura de las 3 disponibles (creación/asignación a QA/resolución), porque el desfasaje creación→QA suele ser mucho más largo que el desfasaje QA→cierre. **No es una métrica de eje Y propia** — no tiene pestaña dedicada, solo determina en qué mes cae cada ticket para las 3 métricas existentes. Validado empíricamente que Σ(TODAS las columnas de tiempo) ≈ (fecha de export − `Creada`) — el estado terminal (`Finalizada`) sigue acumulando tiempo hasta el momento del export, no se congela en `Resuelta`. **Caveat sin resolver:** para tickets que rebotaron por `Con defecto` (columna `bounce`/`Rebote` en el log), no se puede distinguir si el tiempo en "En curso" fue todo previo a la primera llegada a QA o si incluye retrabajo posterior — de ser lo segundo, el ticket quedaría ubicado en un mes posterior al real bajo este eje. Se expone como KPI aparte ("Con rebote"), no se oculta el dato. Ver detalle completo en `2_areas/direccion/decisiones.md` (2026-07-27) y el gap abierto en `../../../wiki/2_areas/gaps_y_preguntas.md`.

## Paso 0 — Verificar insumo

Confirmá que haya al menos un `.csv` en `raw/` (ignorá locks `~$*`). Si no hay nada, avisá al usuario y terminá sin tocar nada.

## Paso 1 — Inspección previa (obligatoria antes de escribir)

Corré, desde la raíz del repo:
```
python .claude/skills/dashboard_qa/scripts/pipeline.py inspect
```
Reporta sin escribir nada:
- Filas leídas, observaciones (`[OBS]`/`[DEF]`/`[REQ]`) detectadas, tickets nuevos vs. ya existentes en el log (y cuántos de los que ya existían cambiaron de estado/tiempo — normal si el ticket seguía en curso en el export anterior).
- Resumen acumulado si se ingestara ahora: tickets totales, con QA cerrado, con Story Points, aún en `EN QA`, sin paso por QA, por proyecto, mediana/promedio global de días en QA, tickets por grupo (asignado) y observaciones por grupo (creador).
- `[WARN]`: tickets sin `Story Points` (quedan fuera de la métrica de tiempo por SP), tickets con `Creada` ilegible (excluidos), tickets con tiempo en QA recortado por superar el lag `Resuelta − Creada` (redondeo de "M").
- `[INFO]` si el export no trae `Resuelta` o `Story Points` — el dashboard degrada esas métricas para ese lote, no aborta.
- `[NUEVAS COLUMNAS no contempladas]`: columnas de estado que el pipeline no reconoce. Si es una variante nueva de un estado ya sumado (ej. otro `EN QA-XXXXX`), sumala a `COLS_QA`/`COLS_DEFECTO` en `pipeline.py` antes de ingestar. Si es un estado genuinamente nuevo, preguntale al usuario qué representa.

**Si el script aborta (`[ABORT]`):** falta alguna columna de metadata obligatoria (`Clave`, `Tipo de Incidencia`, `Resumen`, `Estado`, `Creada`, `Proyecto`, `Persona asignada`, `Creador`) o ninguna columna `EN QA*`. No adivines el mapeo — es señal de que el usuario exportó columnas distintas de Jira; confirmá con él el set de columnas correcto.

## Paso 2 — Ingesta real

Si la inspección se ve razonable, corré:
```
python .claude/skills/dashboard_qa/scripts/pipeline.py ingest
```
Esto mergea (upsert por `Clave`) todos los CSV de `raw/` contra el log acumulado, reescribe `log_performance_qa.md` completo (metodología + registro de lotes + resumen mensual de sanity check + detalle por ticket) y regenera `outputs/dashboard_performance_qa.html` desde el template con los tickets embebidos como JSON.

## Paso 3 — Verificación end-to-end (obligatoria, no alcanza con que el script no falle)

Abrí el dashboard regenerado en el Browser pane (`python -m http.server` sobre `outputs/`, navegar, y **apagar el server al terminar** — no lo dejes corriendo) y confirmá:
- **Orden de controles:** Proyecto / Analista / Estadístico (Promedio-Mediana) / Eje X (filtros generales) arriba de todo → KPIs → pestañas Tiempo en QA / Observaciones / Tiempo por SP justo encima del gráfico.
- **Filtro Proyecto** (Todos/ADQUIRENCIA/EMISIÓN/ONBOARDING/SERVICIOS/ARDID) y **filtro Analista** (Equipo QA agregado por default / Andrea Orsini / Bethania Tornari / Ana Moreno / Otros) combinables sin errores de consola, incluso en combinaciones casi vacías (ej. ARDID + una persona puntual → mensaje de "sin datos", no un gráfico roto).
- **Toggle Promedio/Mediana** es global: visible en las 3 pestañas, no se resetea al cambiar de tab, y afecta tanto el gráfico activo como las 3 tarjetas KPI que tienen noción de estadístico ("días en QA", "días hasta EN QA" y "horas/SP") — su etiqueta cambia según la selección.
- **Toggle Eje X con 3 valores** — Por creación / **Por asignación a QA (default)** / Por resolución: al pasar a "por creación" la curva de los últimos meses se derrumba artificialmente (censura estadística esperada — el desfasaje creación→QA es largo — no un bug, ver metodología en `log_performance_qa.md`); "por asignación a QA" ya viene sin ese problema, por eso es el default. Meses con cohorte incompleta marcados en itálica en el eje X (bajo "creación" o "asignación a QA"): tickets que caerían en ese mes pero siguen en `EN QA`. En la pestaña Observaciones, bajo "por asignación a QA" quedan sin graficar los tickets `[OBS]`/`[DEF]`/`[REQ]` que nunca acumularon tiempo en `EN QA` (14 de 853 al momento de escribir esto) — sí aparecen bajo "por creación"/"por resolución".
- **Gráfico de área** (una sola región por selección de Analista) en las 3 pestañas; con "Equipo QA" seleccionado, el tooltip desglosa el aporte de Andrea/Bethania/Ana; con "Otros" en la pestaña Observaciones, desglosa por persona real (Nicolás Colón, malzogaray, etc.).
- KPIs (tickets testeados, días en QA, días hasta EN QA, observaciones, horas/SP, aún en `EN QA`, sin paso por QA, con rebote a Con Defecto) cuadran contra el resumen que imprimió el Paso 2, para el scope de filtro vigente. Las 2 KPIs de "días hasta EN QA"/"con rebote" son informativas — no dependen de qué pestaña esté abierta.
- Light y dark mode.

## Paso 4 — Rotación de `raw/` (obligatoria, protocolo del CLAUDE.md)

Cada CSV procesado se mueve a `wiki/4_archivos/historial_raw/YYYY-MM_reporte_tiempo_qa/` (mes de la corrida actual). Si el usuario sube dos exports del mismo lote (ej. una corrección porque olvidó una columna), el segundo pisa al primero en el log — dejá una nota en el nombre del archivo rotado indicando cuál fue efectivamente procesado y cuál quedó superseded sin procesar, para que quede auditable. Confirmar `raw/` vacía en el reporte final al usuario.

## Paso 5 — Empaquetar y cerrar

1. **Empaquetá `contexto_vivo/_staging_dashboard_qa/` como item `tipo: dato`** en `wiki/1_proyectos/contexto_vivo/`, `destino_propuesto: 3_recursos/datos/log_performance_qa.md`. Cuerpo: resumen de la ingesta (`<mes(es)>`, N tickets, M observaciones) — el merge lo usa para su línea de changelog.
2. Si hubo `[WARN]` o `[NUEVAS COLUMNAS]` sin resolver: capturalos como item `tipo: gap` (`destino_propuesto: 2_areas/gaps_y_preguntas.md`) y mencionalos al usuario explícitamente.
3. Regenerá `contexto_vivo/index.md`. **Sin git** — el commit del repo personal lo hace el hook `SessionStart` una vez al día.

## ⚠️ Gotchas conocidos

- **El eje X por defecto es "Por asignación a QA" (mes en que el ticket entró a `EN QA`), NO mes de creación** — decisión explícita del usuario (2026-07-27, corregida el mismo día tras un primer intento con "por creación" como default). "Por creación" y "Por resolución" siguen disponibles como toggles secundarios, no se eliminaron. No cambies el default sin pedir permiso.
- **`Resuelta` y `Story Points` son opcionales en el export** (columnas que Jira agrega solo si el usuario las selecciona al exportar). Si un lote no las trae, el pipeline avisa con `[INFO]` y esas métricas quedan sin datos para ese lote — no aborta, no inventa valores.
- **Tiempo calendario, no hábil:** `M` (mes) se calibró empíricamente contra `Resuelta − Creada` real (30,44 días da el menor error agregado sobre el dataset de referencia); `w`=7 días, `d`=24h. No hay forma de convertir a horas hábiles sin las fechas de transición de estado, que el export no trae.
- **"Observación" = prefijo `[OBS]`/`[DEF]`/`[REQ]` en el Resumen**, no todo ticket tipo Error — ver `gestion_jira.md §1.3`. Los Error sin prefijo son bugs reportados directo en producción por Soporte, no hallazgos de QA en staging.
- **La mayoría de las observaciones las crea "Otros" (Producto/PM), no el equipo de QA** — es un hallazgo real del dato (ver gap abierto en `../../../wiki/2_areas/gaps_y_preguntas.md`, 2026-07-27), no un bug del pipeline. No trates de "corregir" la serie de Observaciones para que el equipo de QA aparezca como mayoría.
- **Equipo de QA = Andrea Orsini, Bethania Tornari, Ana Moreno** (`QA_TEAM` en `pipeline.py`, nombres tal como aparecen en el export de Jira — ej. `"Andrea ORSINI"`, `"Bethania"` sin apellido). Si el equipo de QA cambia de composición (alta/baja de analista), actualizar esa constante y `wiki/2_areas/overview_empresa/overview_equipo.md` en el mismo movimiento.
- **El eje "Por asignación a QA" puede ubicar mal de mes a tickets con rebote a `Con defecto`** (124 de 853, columna `Rebote`/campo `bounce`) — el export no trae la secuencia de transiciones, así que no se puede aislar si el retrabajo post-rebote se sumó de más al tramo "antes de QA" (el ticket quedaría en un mes posterior al real). Es un gap abierto (`../../../wiki/2_areas/gaps_y_preguntas.md`, 2026-07-27), no un bug — no intentes "corregirlo" sin el dato de transiciones real.
- **`min_defecto` (tiempo en estado "Con defecto") se guarda en el log y ya alimenta el flag `bounce`/KPI "Con rebote"** — el valor de duración en sí (cuánto tiempo pasó bloqueado por el defecto) sigue sin graficarse como métrica propia; queda disponible para una futura vista de "rebotes de QA" sin tener que reprocesar CSV históricos, si el usuario la pide más adelante.
- **Múltiples CSV a la vez en `raw/`:** se procesan en orden alfabético de nombre de archivo; si dos traen el mismo ticket, gana el último procesado (upsert simple, sin merge campo a campo).
- **Colores fijos por analista** (Andrea/Bethania/Ana/Otros/Equipo QA agregado) en el template — si se agrega un nuevo miembro al equipo, sumarle un color propio en `QA_COLORS` del template en vez de dejar que caiga en "Otros".

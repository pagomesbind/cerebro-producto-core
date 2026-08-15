---
name: sync_releases
description: Sincronizador incremental de versiones publicadas en producción (espacios de desarrollo AD/WS/OB/ARD/SER). Detecta versiones de Jira efectivamente publicadas (released + fecha pasada), ingiere TODOS sus tickets Error/Historia (vengan o no de una IDEA de Producto — bugs, pedidos satélite, urgencias de Soporte), mergea lo aprendido al conocimiento general de detalle_productos/ y mantiene un changelog de releases con mirada de Product Manager. No cruza contra los PRDs vivos de `1_proyectos/` (ver "División de responsabilidades" abajo). Apto para scheduled action semanal; para backfills o volúmenes grandes, usar el pipeline vía export XML (Paso 2-XML).
when_to_use: Se activa cuando el usuario ejecuta el comando de barra /sync_releases (sin argumento para barrer todo, o con argumento para un espacio/versión puntual), cuando el PM avisa que se publicó una versión nueva en producción, o como scheduled action semanal. Skill de fuente compartida: la corre solo el runner designado (ver `identidad.local.md`).
disable-model-invocation: true
argument-hint: "[opcional: ESPACIO o ESPACIO <versión>, ej. AD o AD 70.2, para barrer solo eso]"
---

# 🚀 SINCRONIZADOR DE VERSIONES PUBLICADAS EN PRODUCCIÓN: /sync_releases

## 🔒 Paso -1 obligatorio — verificar que sos el runner

Leé `identidad.local.md` (raíz del repo). Si `runner_fuentes_compartidas` no es `true`, **abortá** con un mensaje claro: esta skill lee una fuente objetiva compartida entre los tres PM/PO. Avisale al usuario quién es el runner designado.

## 🎯 Por qué existe esta skill

No todo lo que llega a producción nace de una IDEA de los PMs. Muchos tickets son **bugs corregidos o pedidos satélite** que entran por urgencias o reclamos del equipo de Soporte — y ese conocimiento es tan valioso como el de las IDEAs: enseña **cómo funcionan las cosas realmente** y avisa cuando **algo ahora funciona diferente**. Perderlo degrada la capacidad del Cerebro de dar soporte en discovery de producto.

**Regla acordada (decisión del usuario, 2026-07-08):** el Cerebro ingiere TODOS los tickets tipo `Error` e `Historia` asociados a versiones de Jira efectivamente publicadas, de todos los espacios de desarrollo.

**División de responsabilidades (histórica, actualizada 2026-08-15):** esta skill mira el delivery real por versión → conocimiento de producto en `detalle_productos/`. **`/sync_releases` NO cruza contra Epic Link ni toca `1_proyectos/`** — eso lo cubría `/sync_jira_ideas` (deprecada; se rehará más adelante). Mientras tanto, un ticket publicado relevante para un PRD vivo **no se refresca solo** — si detectás que un ticket de la versión toca un proyecto de `1_proyectos/`, avisalo en el reporte del barrido, pero no lo escribas vos (fuera del alcance de esta skill).

El PM de Bind PSP arma y coordina las publicaciones de versiones, y actualiza en Jira si se publicó y con qué fecha.

## 🔌 Conexión técnica

- **Instancia:** `bindpsp.atlassian.net`, cloudId `d07593ee-e5cd-4b6c-a371-d360063c167b`.
- **Espacios a barrer:** `AD` (Adquirencia), `WS` (Emisión/Wallet), `OB` (Onboarding), `ARD` (Ardid), `SER` (Pago Fácil → producto **Servicios**).
- **Fuera de alcance:** `PRD` (sin versiones; lo cubre `/sync_jira_ideas`), `QA` y `PQ` (test).
- **Tipos de ticket:** solo `Error` e `Historia`. Excluidos Test/Test Plan/Test Set/Test Execution/Sub Test Execution/Precondition/Subtarea (la JQL ya los filtra).
- **⚠️ Nombres de issuetype en JQL (costó 6 llamadas descubrirlo, 2026-07-08):** la JQL NO reconoce los nombres localizados al español que muestra la UI/API (`Error`, `Historia`) — devuelve 0 resultados sin error. Filtrá siempre con los nombres estándar en inglés: `issuetype in (Bug, Story)`.
- **⚠️ Sin filtro de estado del ticket:** a veces se publican tickets que no llegaron a Finalizado (sin riesgo, se acepta pasar a prod sin testear — confirmado: AD-1103 `EN QA` y AD-578 `Con defecto` en la versión publicada AD 70.1). El criterio de publicación es **de la versión, no del ticket**.
- **Criterio de versión publicada (decisión del usuario: confiar en Jira):** `released = true` **y** `releaseDate <= hoy`. No se pide confirmación previa; el reporte final lista lo ingestado para que el PM detecte a posteriori una versión marcada como publicada que en realidad se pospuso (si pasa: avisar al usuario y revertir/marcar la fila del log).
- **Herramientas:** `searchJiraIssuesUsingJql` y `getJiraIssue` (conector Atlassian). Si no están cargadas: `ToolSearch query:"select:searchJiraIssuesUsingJql,getJiraIssue"`.
- **Archivo de control (espejo read-only de `CEREBRO_CORE`):** [`wiki/3_recursos/datos/log_versiones_publicadas.md`](../../../wiki/3_recursos/datos/log_versiones_publicadas.md) — cabecera con último barrido y estado del backfill por espacio, tabla de versiones ingestadas con sus tickets. **Leelo siempre antes de arrancar.**
- **Changelog de producto (espejo, ídem):** [`wiki/3_recursos/datos/changelog_releases.md`](../../../wiki/3_recursos/datos/changelog_releases.md) — una entrada por versión, redactada como PM (ver Paso 4).
- **Contrato de escritura (pipeline multi-PM, 2026-08-15):** esta skill no tiene `pipeline.py` (todo el trabajo es lectura de Jira + redacción), así que no hay copia de trabajo que sembrar — el log y el changelog se leen del espejo de arriba (para dedupe y contexto) y la novedad de cada barrido se captura directo como items en `contexto_vivo/` (ver Paso 4), nunca escritos al espejo.

## 🏷️ Campos útiles a nivel ticket de desarrollo

| Campo | Qué es |
|---|---|
| `fixVersions[]` | `{name, released, releaseDate}` — la base de toda la detección. Un ticket puede tener 2+ versiones (base + FIX). |
| `customfield_10041` | Story Points reales del ticket (puede ser decimal). |
| `customfield_10014` | Epic Link — útil para agrupar tickets por tema/Epic al mergear a `detalle_productos/` (no se cruza contra `1_proyectos/`, ver "División de responsabilidades"). |
| `customfield_10289` | Link cruzado al Jira de Fintexa (contexto técnico adicional). |

## 🏃 Pipeline del barrido

### Paso 0 — Estado local y modo

1. Leé [`wiki/3_recursos/datos/log_versiones_publicadas.md`](../../../wiki/3_recursos/datos/log_versiones_publicadas.md): fecha de último barrido, versiones ya ingestadas (con sus keys de tickets), estado del backfill por espacio.
2. **Modo single:** con argumento `ESPACIO` (barrer solo ese espacio) o `ESPACIO <versión>` (solo esa versión, ej. `AD 70.2`). Al cerrar, actualizá igual los items de `contexto_vivo/`.
3. **Modo scheduled (no interactivo):** procesá todo el delta sin preguntas. Si el volumen excede lo razonable (5+ versiones nuevas), priorizá las más recientes y dejá el resto como pendiente explícito en el reporte y en el log.
4. **Modo interactivo:** tandas de ~2-3 versiones; al cerrar cada tanda, resumí y preguntá si seguir.

### Paso 1 — Identificar la próxima versión a trabajar (⛔ PROHIBIDO el inventario global)

**La unidad de trabajo es LA VERSIÓN, nunca el espacio entero.** No intentes traer todos los tickets de todas las versiones released de una vez: con historial largo la paginación no lo soporta (ver notas operativas) y retrasa el valor — versiones identificadas sin ingerir no aportan nada.

1. **Barrido incremental (caso normal):** `searchJiraIssuesUsingJql(jql='project = <X> AND fixVersion in releasedVersions(<X>) AND issuetype in (Bug, Story) ORDER BY fixVersion DESC', fields=["issuetype","fixVersions"], maxResults=20)` → con una página alcanza para ver las 1-3 versiones más recientes. Diff contra el log de control: la más reciente no logueada (con `releaseDate <= hoy`) es la próxima a trabajar.
2. **Backfill histórico:** la próxima versión es la inmediatamente anterior a la más vieja ya logueada — su nombre aparece en los `fixVersions` de cualquier enumeración previa; no hace falta redescubrirlo.
3. Diff contra el log de control:
   - **Versión nueva** (no logueada) → procesarla completa (Paso 2) **antes de mirar la siguiente**.
   - **Versión ya ingestada con tickets nuevos** (keys que no figuran en su fila) → ingesta puntual solo de esos tickets.
   - **Dedupe:** un ticket ya ingestado bajo otra versión (típico base + FIX) no se re-ingiere — anotalo en la fila nueva como "ya ingestado en <versión>".
   - **Sin cambios** → nada.

### Paso 2 — Procesar UNA versión por vez (enumerar → dedupe → fetch → merge → log)

Ciclo por versión, de la más reciente a la más vieja. **Cada versión se cierra completa (hasta su item de `contexto_vivo/` con la fila del log y la entrada de changelog) antes de tocar la siguiente** — así toda interrupción deja un estado limpio y retomable. En tandas largas: `/context_push` cada 2-3 versiones para no perder trabajo si se corta la sesión.

**2a. Enumerar los tickets de la versión — escalera de 3 niveles, presupuesto máx ~4 llamadas:**
- **Nivel 1:** `fixVersion = "<nombre exacto>" AND issuetype in (Bug, Story)`, `fields=["issuetype","fixVersions"]`, `maxResults=20` → si vuelven <20 nodos, la lista está completa en 1 llamada (caso típico: hotfixes y versiones menores).
- **Nivel 2 (página llena):** repetí la consulta dividida en `AND issuetype = Bug` y `AND issuetype = Story` por separado.
- **Nivel 3 (un lado sigue lleno):** UN intento de paginación **inmediata** (el `nextPageToken` caduca en segundos — solo sirve encadenado en la llamada siguiente, sin pasos intermedios) y/o UN rango `key >= WS-a AND key < WS-b`.
- **Presupuesto agotado →** registrá el tramo faltante como **pendiente explícito** en la fila del log (ej. "pendiente: Stories con key < WS-402") y **seguí con lo que tenés**. Nunca bisectar persiguiendo completitud total — el valor marginal no paga las llamadas.
- El resultado de la enumeración suele exceder el límite y caer en archivo temporal — **camino normal, no error**: parsealo con PowerShell:
   ```powershell
   $d = Get-Content -Raw "<ruta_del_temp>" | ConvertFrom-Json
   $d.issues.nodes | ForEach-Object { [PSCustomObject]@{Key=$_.key; Type=$_.fields.issuetype.name; Ver=($_.fields.fixVersions.name -join ';')} } | Format-Table -AutoSize
   ```

**2b. Dedupe-first contra la wiki (local, gratis — hacer SIEMPRE antes del fetch):** un Grep con las keys enumeradas (patrón `WS-x|WS-y|...`) sobre `wiki/`. Las keys que ya están documentadas (ingesta de IDEAs, versiones anteriores, Notion) solo reciben **atribución de versión** en el log — el fetch de detalle es únicamente para las keys nuevas. En backfill el overlap suele ser enorme (ej. el cluster FCI/PRD-103 cubría ~58 tickets ya documentados).

**2c. Fetch de detalle de las keys nuevas** en **lotes de 4-5** con `jql='key in (...)'` (esta forma **nunca falló** — solo la enumeración sufre timeouts) y **lista explícita de campos — NUNCA `*all`**: `fields=["summary","issuetype","status","description","comment","fixVersions","attachment","customfield_10041","customfield_10014","customfield_10289"], responseContentFormat="markdown"`. En `comment` están las decisiones y el "qué pasó de verdad" — leelos completos.

**2d. Imágenes embebidas** en description/comentarios (`![](blob:...)` / `![](attachment:...)`): cargá Chrome MCP (`ToolSearch query:"select:mcp__claude-in-chrome__tabs_context_mcp,mcp__claude-in-chrome__navigate,mcp__claude-in-chrome__computer,mcp__claude-in-chrome__read_page,mcp__claude-in-chrome__tabs_create_mcp"`), navegá al `webUrl` del ticket (`https://bindpsp.atlassian.net/browse/<KEY>`, requiere sesión de Jira logueada en la extensión), abrí la imagen en el lightbox nativo de Jira y tomá screenshot ahí (mucho más legible que el thumbnail inline). Volcá el aprendizaje en 1-3 frases citando de qué imagen viene. **Limitación conocida:** imágenes cross-tenant (pegadas desde el Jira de Fintexa, URL con `url=https://fintexa.atlassian.net/...`) no renderizan con la sesión de Bind PSP — si el texto alrededor ya describe el contenido, no es pérdida grave. Si falla la navegación o no hay sesión activa, no bloquees el resto de la ingesta: registrá el gap puntual y seguí.

**2e. Triage dentro de los retenidos:** puro ruido operativo sin aprendizaje (bump de versión, migración de infra, duplicado exacto, typo) → solo se registra en la fila del log, no se documenta en la wiki.

### Paso 2-XML — Alternativa para backfills o volúmenes grandes (recomendada por defecto en esos casos)

La paginación de la API de Jira se rompe con historiales largos (ver "ticket monstruo" en Notas operativas) — un backfill de varios espacios/versiones a la vez **no debería intentarse vía API**. En su lugar, pedile al usuario un **export XML de Jira**: un filtro `project in (AD, WS, OB, ARD, SER) AND fixVersion in releasedVersions(<cada proyecto>)` (o el subconjunto de espacios que falte) exportado a XML desde la UI de Jira, dejado en `raw/`. Con eso:

1. **Un script PowerShell parsea el XML una sola vez** y vuelca a `scratchpad/backfill/`: `inventario.csv` (Key, Proyecto, Versión, Tipo, Estado, SP, EpicName, Título) y **un archivo de texto por versión** (`tickets/<PROY>_<VERSION>.txt`) con, por ticket: key/tipo/estado/SP/epic + descripción (HTML→texto plano, cap ~2.500 caracteres) + comentarios (cap ~1.200 c/u, filtrando el boilerplate de "Automation for Jira" cuando solo repite las 4 preguntas sin contenido). El XML trae `description` y **comentarios completos** — se pierden únicamente los adjuntos (imágenes/PDFs) y el link a Fintexa; aceptable para un backfill.
2. **Fechas de releaseDate:** el XML no las trae (solo el nombre de la versión) — se resuelven aparte con 2-3 llamadas `key in (<1 key representativa por versión>)`, `fields=["fixVersions"]` (única llamada Jira de todo el pipeline).
3. **Dedupe-first** contra `log_versiones_publicadas.md` (keys ya logueadas → skip) y contra `wiki/` (keys ya documentadas → solo atribución) — igual que el Paso 2b, pero corrido una sola vez sobre el CSV completo en vez de por versión.
4. **Ingesta por versión** igual que el Paso 3 de siempre, pero leyendo el archivo de texto local (`Read`) en vez de hacer fetch a Jira — cero llamadas Jira para el detalle. Para versiones grandes (>800 líneas de archivo), primero `grep`/extraé solo las líneas `TITULO:`+`Epic=` de todas las tickets de la versión para armar un mapa de temas antes de leer el contenido completo ticket por ticket — permite agrupar por Epic/tema y detectar de un vistazo qué ya está cubierto conceptualmente en la wiki (mismo patrón: un Epic de Notion ya documentado a nivel de mecánica solo necesita **atribución de versión**, no prosa nueva).
5. Mismas reglas de destino, anti-regresión, log y changelog del Paso 3-4 de siempre. Commit cada 2-3 versiones o al cerrar un espacio completo.
6. **Al cerrar el backfill:** rotá el XML de `raw/` a `wiki/4_archivos/historial_raw/YYYY-MM_<nombre_lote>/` (protocolo de ingesta efímera) — `raw/` queda vacío.

### Paso 3 — Destino del conocimiento por ticket

**Todo ticket publicado genera SIEMPRE un item para `detalle_productos/`** — está en producción; aunque haya quedado apagado por feature flag, es un cambio real del producto y hay que saberlo.

1. **Item `tipo: conocimiento` en `contexto_vivo/`** por cada archivo temático afectado, con la lógica de delta de siempre: leé el `index.md` del producto (en el espejo) y el archivo temático candidato; si ya está 100% documentado → item solo de atribución de fuente; delta parcial → cuerpo con **solo lo nuevo**; contradicción → completá `contradice` citando Jira como fuente más reciente (el merge cierra el gap si existía). Si el cambio quedó publicado pero desactivado (feature flag/apagado), documentalo igual dejando explícito ese estado. Cabecera de fuente: `> Fuente: Jira bindpsp.atlassian.net, versión <ESPACIO X.Y> (publicada YYYY-MM-DD), ticket(s) <KEYs>`.
   - **Mapeo por defecto:** AD→`adquirencia/`, WS→`wallet/`, OB→`onboarding/`, ARD→`ardid/`, SER→`servicios/` (producto Servicios, nace con Pago Fácil MVP — `tipo_destino: crear_carpeta` en la primera ingesta si todavía no existe; overview de producto pendiente del usuario, gap registrado 2026-07-08).
   - Si el contenido del ticket claramente pertenece a otro producto (ej. un ticket WS que toca Agente de Cobros y Pagos), decidí por contenido; aplica a 2+ productos → un item por producto afectado (nunca un archivo `transversal/`; regla anti-cajón de `CLAUDE.md`).
   - **No guardes detalle ticket-por-ticket:** el item lleva lo aprendido al conocimiento general — qué cambió, cómo funciona ahora, qué comportamiento nuevo/corregido quedó en producción.
   - **No cruces contra `1_proyectos/` ni toques `proyecto.md` de ningún PRD** — fuera del alcance de esta skill (ver "División de responsabilidades" al inicio).
2. **Regla anti-regresión del backfill:** al ingerir versiones viejas, dejá explícito en el item que es contexto histórico/atribución, no verdad vigente — el merge nunca debe pisar con esto conocimiento que documenta comportamiento posterior.

### Paso 4 — Registro y changelog de producto

Ambos nacen como items en `contexto_vivo/` — el log y el changelog viven en el espejo, esta skill nunca los escribe directo:

1. **Item `tipo: dato`** con `destino_propuesto: 3_recursos/datos/log_versiones_publicadas.md`, `tipo_destino: actualizar` (append). Cuerpo: la fila nueva lista para insertar — Espacio | Versión | releaseDate | Fecha ingesta | Tickets ingestados (keys) | Destino / notas.
2. **Item `tipo: dato`** con `destino_propuesto: 3_recursos/datos/changelog_releases.md`, `tipo_destino: actualizar` (prepend, orden cronológico inverso). Cuerpo: la entrada completa ya redactada, `## YYYY-MM-DD — <ESPACIO> <versión> (<producto>)`, **como Product Manager**: el **qué valor se agregó** con cada cambio, no el cómo técnico. Bullets agrupados por tipo: **arreglos de errores**, **nuevos comportamientos**, **mejoras funcionales**, **mejoras de rendimiento**, **nuevos requerimientos**. Mencioná si algo quedó publicado pero apagado. Debe poder leerlo cualquier área de Bind PSP (Soporte, Comercial, C-levels) y entender qué cambió en el producto con esa versión.

### Paso 5 — Reporte del barrido

Generá `outputs/reportes_sync/YYYY-MM-DD_reporte_releases.md` **y mostralo en la terminal**:

1. **Versiones detectadas e ingestadas** por espacio (con fecha de publicación y cantidad de tickets — el PM valida acá si alguna en realidad se pospuso).
2. **Hallazgos clave** — "X ahora funciona distinto", bugs que revelan comportamiento no documentado, contradicciones con la wiki resueltas.
3. **Gaps nuevos** y pendientes (tandas de backfill restantes, tickets sin ingerir).

Si no hubo versiones nuevas → reporte de una línea "sin novedades desde YYYY-MM-DD".

### Paso 6 — Cierre

1. Gaps nuevos → item `tipo: gap` (`destino_propuesto: 2_areas/gaps_y_preguntas.md`); decisiones detectadas → item `tipo: decision` (`destino_propuesto: 2_areas/direccion/decisiones.md`); acciones/tareas del equipo de Producto detectadas en tickets → `wiki/1_proyectos/tareas.md` (personal, directo; si es de interés de todo el equipo, sumá además un item `tipo: tarea_equipo`).
2. Regenerá `contexto_vivo/index.md` con todos los items nuevos de esta corrida.
3. **Sin git.** El commit del repo personal lo hace el hook `SessionStart` una vez al día.
4. En modo interactivo: cerrá con el reporte y, si quedan versiones pendientes (backfill), preguntá si seguir con la próxima tanda.

## 📌 Notas operativas (ya costaron tiempo descubrir — respetarlas ahorra sesiones enteras)

- **⚠️ El "ticket monstruo" (2026-07-09):** si 2 consultas con ventanas de resultados que comparten un tramo dan timeout, NO es red ni carga del servidor — hay un ticket con contenido gigante en ese tramo, y **toda consulta cuya ventana de resultados lo incluya va a fallar** (paginación, rangos de key, `NOT IN`, `ORDER BY`, cualquier variante). No insistas: acotá el resto con rangos de key que lo esquiven, registrá el tramo del monstruo como pendiente en el log, y seguí. (Caso real: una Story de W 68 con key en [325,350) explicó TODOS los timeouts "misteriosos" de una sesión entera.)
- **El `nextPageToken` caduca en segundos** — solo funciona encadenado en la llamada inmediatamente siguiente a la que lo generó. Y aun fresco, falla si la página siguiente contiene al monstruo. Preferí siempre la escalera del Paso 2a antes que paginar.
- **`fields` NO filtra los campos default del conector** — cada nodo SIEMPRE trae summary, description, status, assignee y project (~4K chars/nodo); `fields` solo AGREGA campos (comment, customfields). El control de tamaño real es `maxResults` (≤20 para enumeración). Por eso toda enumeración termina en archivo temporal + parse PowerShell: camino normal, no error.
- **`key in (...)` para fetch de detalle nunca falló** — la fase de ingesta es confiable; solo la enumeración sufre. Lotes de 4-5.
- **NUNCA `fields=*all`** — payloads 5-10x más grandes por metadata inútil (avatares, customfields null, issuelinks anidados) y timeouts.
- Se detectaron respuestas cruzadas/duplicadas al lanzar 2+ llamadas Jira en paralelo — lanzá las llamadas Jira siempre de a una.
- **Issuetype en JQL va en inglés** (`Bug`, `Story`) aunque la API muestre `Error`/`Historia` — con los nombres en español devuelve 0 resultados sin error. Nombres de estado/versión también sensibles a mayúsculas — ante 0 resultados inesperados, verificá antes de asumir que no hay nada.
- Las funciones JQL `releasedVersions(<PROYECTO>)` requieren el proyecto como argumento — una por espacio, no combinables.
- `python3` no existe en esta máquina — todo parsing de JSON va por PowerShell (`ConvertFrom-Json`).

---
name: sync_notion_docs
description: Sincronizador incremental de Notion por Timestamps. Consolida todo el contenido de la base "Docs" en wiki/3_recursos/detalle_productos/, organizado por producto y luego por funcionalidad.
when_to_use: Se activa inmediatamente cuando el usuario ejecuta el comando de barra /sync_notion_docs para capturar novedades del equipo. Skill de fuente compartida: la corre solo el runner designado (ver `identidad.local.md`).
disable-model-invocation: true
argument-hint: ""
---

# ⚙️ MOTOR DE SINCRONIZACIÓN DIFERENCIAL Y CONSOLIDACIÓN: /sync_notion_docs

## 🔒 Paso -1 obligatorio — verificar que sos el runner

Leé `identidad.local.md` (raíz del repo). Si `runner_fuentes_compartidas` no es `true`, **abortá** con un mensaje claro: esta skill lee una fuente objetiva compartida entre los tres PM/PO. Avisale al usuario quién es el runner designado.

**Contrato de escritura (pipeline multi-PM, 2026-08-15):** `wiki/3_recursos/detalle_productos/` es espejo read-only en este install. Esta skill sigue leyendo de ahí para la idempotencia por timestamp (ver "Logic core" abajo) y sigue calculando qué sección escribir igual que antes — pero **nunca escribe directo**: cada sección nace como item `tipo: conocimiento` en `contexto_vivo/` (ver Paso 3).

## 🔌 CONEXIÓN TÉCNICA (Conector MCP Notion — workspace "Bind PSP")
- **Base fuente:** database "Docs" — `https://www.notion.so/bindpsp/2b7b3646c94b802b96a0e77cd7cb0d8e`
- **Data source (para queries):** `collection://2b7b3646-c94b-806b-b25b-000b057c0c94`
- **Herramientas MCP a usar** (prefijo `mcp__<id-conector>__notion-*`, resolver el ID de conector vigente con `ToolSearch query:"notion"` si no está cargado):
  - `notion-query-data-sources` (modo `sql`) — para el inventario completo de páginas en una sola llamada.
  - `notion-fetch` — para traer el contenido completo (Markdown) de cada página con delta positivo, pasando la `url` de la fila como `id`.
- **Query de inventario (Paso 0, obligatorio antes de cualquier fetch individual):**
  ```sql
  SELECT url, "Nombre", "Tipo", "Producto", "Estado", "Última edición", "Fecha de creación"
  FROM "collection://2b7b3646-c94b-806b-b25b-000b057c0c94"
  ```
- **Propiedades de la base:**
  | Propiedad | Tipo Notion | Uso en la skill |
  |---|---|---|
  | `Nombre` | title | Título del documento → usado para elegir sección/archivo temático |
  | `Tipo` | select (valores abiertos: `Manual para configuraciones`, `Capacitación interna`, `Documentación para clientes`, `Proceso`, y cualquier valor futuro) | Ya NO determina la carpeta de destino (ver rediseño abajo) — se documenta como metadata dentro de cada sección |
  | `Producto` | multi_select (valores abiertos, hoy incluye al menos: `WALLET`, `ADQUIRENCIA`, `AG COBROS Y PAGOS`, `ONBOARDING`, `SERVICIOS`, y cualquier producto futuro incluyendo accesorios como `ARDID`/`SISCRI`) | **Determina la carpeta de producto de destino** dentro de `detalle_productos/` |
  | `Última edición` | last_edited_time (ISO-8601) | Timestamp para el Filtro de Delta Temporal |
  | `Fecha de creación` | created_time (ISO-8601) | Referencia informativa |
  | `Estado` | status: `Sin empezar` / `En curso` / `Listo` | Filtro opcional — ver nota abajo |
  | `url` | — | Identificador estable de la página, usar como `id` |

  > **Filtro por Estado recomendado:** por defecto, procesar solo páginas con `Estado = "Listo"`. Si el usuario pide explícitamente sincronizar todo, ignorar este filtro.

## 🗂️ REDISEÑO DE DESTINO (reemplaza `conocimiento_interno/`)
Esta skill ya **no** escribe en `wiki/3_recursos/conocimiento_interno/` (carpeta retirada). El destino ahora es `wiki/3_recursos/detalle_productos/<producto>/`, siguiendo el modelo de 3 vías del Segundo Cerebro:

| Carpeta de `wiki/3_recursos/` | Regla | Quién escribe |
|---|---|---|
| `<producto>/apis_expuestas/` | Intocable por esta skill — solo texto literal del portal público, dominio exclusivo de `/sync_web`. | `/sync_web` |
| `arquitectura_sistema/` | Intocable por esta skill. | Ingesta manual |
| `detalle_productos/<producto>/` | **Destino de esta skill.** Todo conocimiento de Notion (manuales, capacitaciones, docs para clientes, procesos) — técnico o no, relevante a cualquier área de Bind PSP (Producto, Soporte, Comercial, Integraciones, Administración). | `/sync_notion_docs`, `/ingest` |

`wiki/2_areas/overview_productos/overview_<producto>.md` (overview de negocio vivo, mantenido directamente por el usuario) **nunca se toca** desde esta skill.

## 🧠 LOGIC CORE: IDEMPOTENCIA POR TIMESTAMP
1. Ejecuta la query de inventario del Paso 0 completa (una sola llamada a `notion-query-data-sources`, sin iterar página por página).
2. **Filtro de Novedad:** Para cada fila, si la `url` no aparece como `Fuente:` en ningún archivo existente bajo `wiki/3_recursos/detalle_productos/`, procésala como documento nuevo.
3. **Filtro de Delta Temporal:** Si la `url` ya existe localmente, compara `"Última edición"` (Notion) contra el valor `Última edición (Notion):` registrado en la mini-cabecera de esa sección (ver formato abajo). Si la fecha de Notion es **estrictamente más reciente**, llama a `notion-fetch` con esa `url` y actualiza esa sección puntual. De lo contrario, **ignora la página por completo** para optimizar el contexto.

## 🏷️ CLASIFICACIÓN — PRODUCTO DETERMINA LA CARPETA, TEMA DETERMINA EL ARCHIVO

### Paso 1: Determinar la carpeta de producto (obligatorio, sin listas cerradas)
1. Toma el valor completo de `Producto` (multi_select). Si tiene más de un valor, el **primero listado es el producto principal** (carpeta de destino); los demás quedan documentados como "también relevante para: [...]" en la mini-cabecera de la sección, y se agrega una línea de referencia cruzada en el `index.md` de esos productos secundarios (sin duplicar el contenido completo ahí).
2. Normaliza el valor de `Producto` a slug de carpeta existente: `WALLET` → `wallet`, `ADQUIRENCIA` → `adquirencia`, `AG COBROS Y PAGOS` → `agente_cobros_y_pagos`, `ONBOARDING` → `onboarding`, `ARDID` → `ardid`, `SISCRI` → `siscri`, `SERVICIOS` → `servicios`.
3. Si el valor de `Producto` es un producto nuevo no listado arriba (ej. `CONCILIADOR`) y **hay contenido real que sincronizar**, preguntá al usuario si corresponde crear `wiki/3_recursos/detalle_productos/<slug_nuevo>/` — marcá el item con `tipo_destino: crear_carpeta` (requiere permiso, lo pide `/context_merge` igual, pero adelantale la pregunta al usuario ahora si podés). Si el valor está vacío o no mapea a ningún producto concreto (y no aplica a ninguno de los productos ya listados), **no lo fuerces en ninguna carpeta ni inventes un `transversal/`** — capturalo como item `tipo: gap` y preguntá al usuario dónde va. Nunca se descarta ni se bloquea una página por tener un valor de `Producto` no visto antes.

### Paso 2: Determinar el archivo temático dentro de la carpeta de producto
1. Lee el `index.md` de la carpeta de producto destino — lista los archivos temáticos ya existentes y su contenido.
2. Si el tema de la página nueva (por su `Nombre` y contenido) encaja razonablemente en un archivo temático ya existente, **agregá la página como una nueva sección `##` dentro de ese archivo** — no crees un archivo nuevo por cada página de Notion. Esto es lo que mantiene `detalle_productos/` navegable en vez de fragmentarse en decenas de archivos de 1 página cada uno.
3. Si no encaja en ninguno, creá un archivo temático **nuevo con nombre descriptivo del tema** (ej. `debin_y_fondeo.md`, no `introduccion_de_fondeo_de_recaudadora_con_debin.md`) y agregalo a la tabla del `index.md`.

### Paso 3: Capturar la sección como item

Por cada archivo temático tocado (una página de Notion puede generar una sección nueva o actualizar una existente), **un item `tipo: conocimiento` en `contexto_vivo/`**, `destino_propuesto` = el archivo temático, `tipo_destino: actualizar` o `crear` según corresponda. El cuerpo del item lleva la sección lista para insertar, con esta mini-cabecera (compacta, no el bloque completo de metadata de versiones anteriores):
```markdown
## [Nombre de la página]

> Tipo: [valor de Tipo] · Producto(s): [valor(es) de Producto] · Última edición (Notion): YYYY-MM-DD · Fuente: [url]

[contenido completo de la página, literal — no resumir, no parafrasear]
```
**Advertencia de datos sensibles:** el contenido de Notion puede incluir IPs internas, curls contra ambientes productivos y datos reales de cuentas/comercios. Transcribir tal cual — `wiki/` es de lectura interna, no pública.

### Paso 4: Índices

Si la página tenía más de un `Producto`, sumá al item (o a uno aparte) la línea de referencia cruzada que va en el `index.md` de cada producto secundario. El resto de la actualización de índices (tabla del `index.md` de la carpeta de producto, alta en `wiki/index.md` si se creó una carpeta nueva) la hace `/context_merge` al aplicar los items — no hace falta que la calcules vos, pero dejá claro en el cuerpo del item qué cambió (archivo, tema, si es sección nueva o actualización).

## Paso 5 — Cierre

1. Regenerá `contexto_vivo/index.md` con todos los items nuevos de esta corrida, agrupados por producto.
2. **Sin git.** El commit del repo personal lo hace el hook `SessionStart` una vez al día.

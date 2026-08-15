---
name: sync_customers
description: Sincronizador incremental de la cartera de clientes de Bind PSP. Detecta clientes nuevos o actualizados en la base Notion "Legajos de clientes" desde el último barrido y actualiza wiki/2_areas/clientes/. No interactivo — apto para scheduled action semanal.
when_to_use: Se activa inmediatamente cuando el usuario ejecuta el comando de barra /sync_customers, o cuando corre como scheduled action automática. Skill de fuente compartida: la corre solo el runner designado (ver `identidad.local.md`).
disable-model-invocation: true
argument-hint: ""
---

# ⚙️ MOTOR DE SINCRONIZACIÓN DIFERENCIAL: /sync_customers

## 🔒 Paso -1 obligatorio — verificar que sos el runner

Leé `identidad.local.md` (raíz del repo). Si `runner_fuentes_compartidas` no es `true`, **abortá** con un mensaje claro: esta skill lee una fuente objetiva compartida entre los tres PM/PO. Avisale al usuario quién es el runner designado.

No interactivo: no preguntes nada al usuario durante la corrida. Ante ambigüedad, aplicá el mejor criterio disponible (ver reglas de mapeo abajo) y capturá la duda como item `tipo: gap` en `contexto_vivo/` en vez de bloquear.

**Contrato de escritura (pipeline multi-PM, 2026-08-15):** `wiki/2_areas/clientes/` es espejo read-only en este install. Esta skill sigue leyendo de ahí (para el fusion/dedupe de siempre) y calculando el contenido final igual que antes, pero **nunca lo escribe directo** — lo empaqueta como items `tipo: dato` en `contexto_vivo/` (ver Paso 3/5). `/context_merge` los aplica por copia byte a byte.

## 🔌 CONEXIÓN TÉCNICA (Conector MCP Notion — workspace "Bind PSP")
- **Base fuente:** database "Brochure Clientes Bind PSP" — página `13ab3646c94b80fc8211ffa4f0faaa84`, base inline "Legajos de clientes".
- **Data source (para queries SQL):** `collection://4a001976-ca20-4ab1-ad6b-6cf2e0559c01`
- **Herramientas MCP** (prefijo `mcp__<id-conector>__notion-*`, resolver el ID de conector vigente con `ToolSearch query:"notion"` si no está cargado):
  - `notion-query-data-sources` (modo `sql`) — inventario/delta en una sola llamada (o pocas, con `LIMIT`/`OFFSET` si el delta supera 100 filas).
  - `notion-fetch` — contenido completo de cada página con delta positivo, pasando la `url` de la fila como `id`.

## División de responsabilidades con `/sync_meetings` y `/sync_mails` (decisión del usuario, 2026-07-15)

Esta skill es la **única fuente de verdad y única autorizada a decidir altas/bajas de clientes** en `log_clientes.md` (carga masiva/incremental desde Notion). Pero `/sync_meetings` y `/sync_mails` **complementan** las fichas de `casos_de_uso_clientes.md` cuando una reunión o un mail revela algo nuevo sobre un cliente **ya existente** en `log_clientes.md` — capturan un item `tipo: conocimiento` con el hallazgo fechado para `Particularidades / cronología`, mismo criterio de fusión que usa esta skill (nunca reemplazan, solo agregan). Si esas skills detectan un cliente que no está en `log_clientes.md` en absoluto, no proponen nada — lo capturan como item `tipo: gap` para que este barrido lo levante desde Notion en su momento.

## 🚫 REGLAS DURAS (no negociables, heredadas de la carga inicial)
- Solo texto y **propiedades** de la página. Prohibido: abrir adjuntos (`<file>`, `<pdf>`), seguir subpáginas o sub-bases (ej. "Comercios que Recauda"/Merchants), seguir la relación `Epics`, descargar imágenes.
- Nunca guardar CUIT, CBU, contactos, emails, links a Drive/legales — ni en el log ni en la ficha.
- Pricing: guardar **esquema cualitativo y números reales** cuando estén disponibles (decisión registrada en `wiki/2_areas/direccion/decisiones.md`, 2026-07-07).
- El multi-select `Productos` de Comercial son **funcionalidades/canales**, no la taxonomía canónica de Bind. Mapear siempre con la tabla de `wiki/2_areas/clientes/index.md` — conservar la etiqueta original **y** el producto canónico. Etiqueta nueva no listada → mapear con mejor criterio, conservar el original, y registrar la duda en `../../../wiki/2_areas/gaps_y_preguntas.md`.
- Incluir siempre la propiedad **`STATUS Detallado`** en la query — es texto libre de Comercial con información operativa real (puede contradecir el `Estado del Cliente` formal; si contradice, documentar ambos y no "corregir" el estado por cuenta propia).
- Ficha en `casos_de_uso_clientes.md` solo si hay contenido sustantivo (más allá del template vacío, o `STATUS Detallado` con texto). Si no, el cliente queda solo con fila en el log (`—` en "Detalle").

## Paso 0 — Estado local
Lee la cabecera de `wiki/2_areas/clientes/log_clientes.md`:
```
> **Último barrido:** YYYY-MM-DD ...
```
Esa fecha es el filtro de corte para el Paso 1.

## Paso 1 — Inventario delta (una query SQL)
```sql
SELECT "Cliente", "Estado del Cliente", "Productos", "Rubro", "Tamaño", "Riesgo",
       "STATUS Detallado", "Fecha de creación", "Última edición", url
FROM "collection://4a001976-ca20-4ab1-ad6b-6cf2e0559c01"
WHERE "Última edición" > '<último barrido>'
```
`Fecha de creación` siempre es ≤ `Última edición`, así que este único filtro cubre tanto clientes nuevos como actualizados. Un cliente es **nuevo** si su `url` no está ya en `log_clientes.md`; si ya está, es una **actualización**. Paginar con `LIMIT`/`OFFSET` si el resultado supera 100 filas.

Si la query no devuelve filas: no hay deltas — ir directo al Paso 5 y reportar "sin cambios" (solo se actualiza la fecha de "Último barrido").

## Paso 2 — Contenido por cliente con delta
Para cada fila del delta, `notion-fetch` de su `url`. Aplicar las reglas duras de arriba (nada de adjuntos/subpáginas/Epics).

## Paso 3 — Calcular el contenido actualizado (mismo criterio de siempre, escritura vía item)
- **`log_clientes.md`:** cliente nuevo → agregar fila en la tabla del `Estado del Cliente` correspondiente (crear la sección `## <Estado> (N)` si es el primer cliente de ese estado). Cliente existente → actualizar la fila completa (Productos/Canónico/Rubro/Tamaño/Riesgo/Últ. ed./Detalle) in place, sin duplicar.
- **`casos_de_uso_clientes.md`:**
  - Cliente nuevo con contenido sustantivo → agregar sección `## <CLIENTE>` bajo el encabezado `# <ESTADO>` correspondiente (crear el encabezado de estado si no existe todavía), siguiendo el formato de ficha ya establecido (mini-cabecera + Modelo de negocio / Status detallado / Cómo opera los productos / Pricing / Volúmenes / Particularidades).
  - Cliente existente con ficha previa → **fusionar**, no reemplazar: actualizar la mini-cabecera (nueva `Última edición`), agregar contenido nuevo a `Particularidades / cronología` como entrada fechada, y actualizar Pricing/Modelo de negocio solo si el contenido nuevo los cambia. Conservar la cronología previa.
  - Cliente que pasa de "sin ficha" a "con contenido sustantivo" → crear la sección por primera vez y marcar `✅` en el log (era `—`).
- Aplicar siempre el mapeo Comercial → canónico de `index.md`. Si la página usa una etiqueta de `Productos` nueva, mapear con mejor criterio y capturar el gap (item `tipo: gap`).
- **Empaquetá cada archivo tocado como un item `tipo: dato` separado** en `contexto_vivo/` (`destino_propuesto: 2_areas/clientes/log_clientes.md` / `2_areas/clientes/casos_de_uso_clientes.md`), con el **contenido completo actualizado** del archivo como cuerpo — el merge lo aplica por copia byte a byte, sin criterio editorial.

## Paso 4 — Síntesis
Si los deltas de esta corrida revelan un patrón nuevo o rompen uno documentado (nuevo rubro con arquetipo propio, rango de pricing fuera de lo observado, motivo de baja no visto antes), capturalo como item `tipo: conocimiento` (`destino_propuesto: 2_areas/clientes/patrones_transversales.md`) — acá sí es prosa de síntesis, el merge la integra editorialmente. Si no hay nada que ajustar, no generes item.

## Paso 5 — Cierre
1. El item de `log_clientes.md` (Paso 3) ya lleva la fecha de `> **Último barrido:**` actualizada — no hace falta un paso aparte.
2. Si se creó una sección de estado nueva o cambió la tabla de mapeo Comercial→canónico, sumá `2_areas/clientes/index.md` como item `tipo: dato` también.
3. Si se detectaron dudas de mapeo o contradicciones `Estado del Cliente` vs. `STATUS Detallado`, capturalas como item `tipo: gap`.
4. Regenerá `contexto_vivo/index.md`. **Sin git** — el commit del repo personal lo hace el hook `SessionStart` una vez al día.
5. Si no hubo deltas (Paso 1 vacío): no generes ningún item, reportá "sin cambios" al usuario.

## Gotchas conocidos (de la carga inicial, 2026-07-07)
- La base puede superar 100 filas en un delta grande (ej. primera corrida tras mucho tiempo sin sincronizar) — paginar con `LIMIT`/`OFFSET`.
- Pueden existir páginas con `Cliente` (title) vacío — no descartarlas sin mirar el contenido; identificar el cliente real por el contenido de la página (ver caso Carrefour/BSF en la carga inicial) y dejar una nota si no se puede identificar.
- Pueden aparecer filas basura (páginas creadas por error a partir de un email reenviado, no un cliente real) — si el contenido de la página no describe un cliente, no ingerir como tal; registrar en `../../../wiki/2_areas/gaps_y_preguntas.md` y marcar `—` en el log.
- Un mismo cliente puede tener dos páginas duplicadas en distintos estados — si se detecta, verificar cuál tiene contenido real y marcar la otra como duplicado en el log y en `../../../wiki/2_areas/gaps_y_preguntas.md`, sin eliminar ninguna fila de Notion.
- El campo `STATUS Detallado` puede contradecir `Estado del Cliente` (ej. cliente "En producción" cuyo status detallado describe una baja, o viceversa) — documentar ambos tal cual están en Notion, no resolver la contradicción por cuenta propia.

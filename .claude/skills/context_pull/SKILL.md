---
name: context_pull
description: Lee los manifiestos de merge nuevos desde CEREBRO_CORE, reporta qué cambió en el canon compartido y qué items propios se ingirieron, avisa de novedades cross-PM dirigidas al usuario, y archiva los items propios ya ingeridos. No reinterpreta ni reingesta nada — el git pull y el espejo de 2_areas/3_recursos ya los hace el hook SessionStart automáticamente.
when_to_use: Se activa cuando el usuario ejecuta /context_pull, típicamente cuando el hook SessionStart avisa que hay manifiestos de merge nuevos sin leer.
disable-model-invocation: true
argument-hint: ""
---

# 📥 LECTURA DE MERGE: /context_pull

## 🎯 Por qué existe esta skill

El transporte mecánico (traer el canon actualizado del repo compartido al install personal) ya lo hace el hook `SessionStart` — `git pull` en el clon core + espejo de `wiki/2_areas/`, `wiki/3_recursos/`, `CLAUDE.md`, `.claude/skills/` y `.claude/settings.json`, sin intervención de ningún LLM. Esta skill es la parte que sí necesita criterio: leer los manifiestos que dejó `/context_merge`, contarte qué cambió y por qué te importa, y cerrar el ciclo de vida de tus propios items (de `en_cola`/`ingestado` a archivados).

**Esta skill nunca reinterpreta contenido ni vuelve a escribir nada del canon** — eso ya lo hizo `/context_merge` de forma determinística. Si reinterpretara, sería exactamente el defecto que este diseño evita: que cada instalación reconstruya el canon a su manera y las tres terminen distintas.

## 🏃 Pipeline

### Paso 1 — Verificar que el espejo está al día

1. Leé `identidad.local.md` para `ruta_clon_core`. Si está vacío o no existe, abortá — no hay nada que leer todavía.
2. Confirmá que el espejo local (`wiki/2_areas/`, `wiki/3_recursos/`, `CLAUDE.md`, `.claude/skills/`) coincide con el `HEAD` actual del clon core (`git rev-parse HEAD` en el clon core vs. la marca de tiempo del hook). Si el hook `SessionStart` no corrió hoy o falló, forzá vos el `git pull --ff-only` + espejo (mismo mecanismo que el hook, ver `.claude/scripts/session_sync.ps1`) antes de seguir — no leas manifiestos contra un espejo desactualizado.
3. Si el `pull --ff-only` falla (alguien escribió en tu espejo del install, lo cual no debería pasar si el hook `PreToolUse` está activo): reportalo como **error explícito** al usuario. No mergees a ciegas, no sobrescribas sin avisar.

### Paso 2 — Identificar manifiestos nuevos

Leé `wiki/1_proyectos/logs_sync/log_context.md` — el campo "Último `/context_merge` leído (manifiesto)" te dice desde qué fecha mirar. Listá los archivos `manifiestos/YYYY-MM-DD.md` del clon core con fecha posterior a esa marca (o todos, si es la primera corrida).

Si no hay manifiestos nuevos: reportá "sin novedades del canon desde <fecha>" y terminá.

### Paso 3 — Leer y resumir cada manifiesto

Por cada manifiesto nuevo, en orden cronológico:

1. **Qué cambió en el canon** — resumí la sección "Items ingeridos" agrupada por producto/tema, con los PM de origen. No hace falta leer los archivos completos del canon, el manifiesto ya trae lo esencial; si el usuario quiere el detalle completo de un cambio puntual, ahí sí abrí el archivo real.
2. **Tus propios items ingeridos** — de la tabla "Items ingeridos", filtrá los que son `pm: <vos>`. Estos son candidatos a archivar (Paso 4).
3. **Novedades dirigidas a vos** — la sección "Novedades para otro PM" de cada manifiesto, filtrada a `pm_destino: <vos>`. Esto es lo que cierra el loop cross-PM: alguien detectó algo sobre uno de tus proyectos y no pudo escribirlo en tu `1_proyectos/` (el merge no tiene acceso). Reportalo de forma destacada — es fácil de perder si se mezcla con el resto — y sugerile al usuario si conviene incorporarlo a su `proyecto.md` (decisión suya, no la tomes vos).
4. **Contradicciones abiertas** que te involucren (si alguno de tus items entró en el Protocolo de Contradicción) — señalalas explícitamente, con el link al gap que abrió el merge.
5. **Items tuyos que quedaron sin procesar** (pendientes de permiso, contradicción sin resolver) — avisale al usuario que siguen en `en_cola`, no se perdieron.

### Paso 4 — Archivar los items propios ya ingeridos

Para cada item tuyo con `estado: ingestado` (confirmado en el manifiesto): moveló de `wiki/1_proyectos/contexto_vivo/` a `wiki/4_archivos/contexto_ingestado/`. Ya no se lee como contexto vivo — el conocimiento vive en su destino real del canon.

### Paso 5 — Cierre

1. Actualizá `wiki/1_proyectos/logs_sync/log_context.md`: marcá el/los manifiesto(s) como leídos (fecha del más reciente procesado), una línea por corrida con el resumen.
2. Regenerá `wiki/1_proyectos/contexto_vivo/index.md` (los items archivados salen de la lista).
3. Cerrá con un resumen claro al usuario, en este orden: novedades dirigidas a vos (lo más importante, nunca lo entierres) → resto del canon que cambió → tus items ingeridos y archivados → pendientes tuyos que siguen sin mergear.
4. **Sin git en el repo personal más allá de lo que ya hizo el hook.** No hagas commits extra ni toques el clon core (esta skill es de solo lectura sobre `CEREBRO_CORE`).

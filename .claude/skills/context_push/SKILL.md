---
name: context_push
description: Sube los items de contexto_vivo/ listos (estado capturado) al repo compartido CEREBRO_CORE, marcándolos en_cola. Es el primer verbo del pipeline de sincronización multi-PM — no ingiere nada al canon, solo transporta. Apto para correr a diario.
when_to_use: Se activa cuando el usuario ejecuta /context_push, típicamente una vez por día (o al final de una sesión con items nuevos en contexto_vivo/).
disable-model-invocation: true
argument-hint: ""
---

# 📤 SUBIDA DE CONTEXTO: /context_push

## 🎯 Por qué existe esta skill

`wiki/1_proyectos/contexto_vivo/` es el buzón donde nace todo aporte al canon (`2_areas/`/`3_recursos/`) — pero mientras el item viva solo en el install personal, ningún otro PM lo ve y `/context_merge` no puede tocarlo. `/context_push` es el transporte: copia los items listos al repo compartido `CEREBRO_CORE`, sin interpretarlos ni redactarlos — el mismo texto, byte a byte. La ingesta real (decidir si algo entra al canon, resolver contradicciones entre PMs) es trabajo exclusivo de `/context_merge`, corrida por el líder.

Incremental por definición: solo toca items en `estado: capturado`. Correr esta skill dos veces seguidas sin capturar nada nuevo es un no-op.

## 🔌 Prerrequisitos

1. Leé `identidad.local.md` (raíz del repo). Necesitás `pm` (tu slug) y `ruta_clon_core` (la ruta local del clon de `CEREBRO_CORE`).
2. Si `ruta_clon_core` está vacío o la carpeta no existe: **abortá** con un mensaje claro — `CEREBRO_CORE` todavía no está clonado en esta máquina, no hay dónde subir nada. No hay fallback silencioso.
3. Si el clon existe pero tiene cambios locales sin commitear que no son tuyos (alguien más lo usó desde esta máquina), avisá y pedí confirmación antes de tocarlo.

## 🏃 Pipeline

### Paso 1 — Inventario

Leé `wiki/1_proyectos/contexto_vivo/index.md` y listá todos los archivos `.md` de la carpeta (salvo `index.md` y `_plantilla.md`) cuyo frontmatter tenga `estado: capturado`.

Si no hay ninguno: reportá "nada para subir" y terminá sin tocar el core.

### Paso 2 — Validar cada item antes de subir

Por cada item en `capturado`, verificá que el frontmatter esté completo:
- `id`, `pm`, `fecha_captura`, `fuente`, `producto`, `tema`, `tipo` presentes.
- `destino_propuesto` y `tipo_destino` presentes (excepción: si `tipo: iniciativa` sin `pm_destino`, `destino_propuesto` puede apuntar a `2_areas/direccion/iniciativas.md` por default).
- Si `tipo: iniciativa`, `proyecto` presente.
- Si `contradice` no está, debe decir explícitamente `"no"` (no puede faltar el campo).
- El cuerpo no está vacío.

**Si un item falla la validación:** no lo subas. Reportalo al usuario con el campo faltante exacto y dejalo en `capturado` — se sube en la próxima corrida una vez corregido. No bloquees el resto de items válidos por uno malo.

### Paso 3 — Copiar al core

Para cada item válido:
1. Copiá el archivo tal cual (sin modificar contenido) a `<ruta_clon_core>/contexto_vivo/<pm>/<id>.md`.
2. En el archivo **local** (el de `wiki/1_proyectos/contexto_vivo/`), actualizá el frontmatter: `estado: en_cola`. **El archivo sigue en su lugar** — no se mueve, no se borra. Sigue leyéndose como contexto vivo hasta que el merge lo ingiera.

### Paso 4 — Commit y push en el core

Dentro del clon de `CEREBRO_CORE` (nunca en el repo personal — esta skill no toca el repo personal en absoluto):
```
git add contexto_vivo/<pm>/
git commit -m "context_push: <pm> — N item(s) (YYYY-MM-DD)"
git push origin main
```
Si el push falla por un push concurrente de otro PM (`rejected — non-fast-forward`): `git pull --ff-only` y reintentá el push. Si el `pull --ff-only` también falla (conflicto real, poco probable ya que cada PM escribe solo su propia subcarpeta), avisá al usuario — no fuerces.

### Paso 5 — Cierre

1. Regenerá `wiki/1_proyectos/contexto_vivo/index.md` (los items pasados a `en_cola` siguen listados, con su estado actualizado).
2. Registrá la corrida en `wiki/1_proyectos/logs_sync/log_context.md`: fecha, cuántos items subidos, sus ids.
3. Reportá al usuario: qué se subió, qué quedó sin subir (por validación fallida) y por qué.
4. **Sin tocar el repo personal.** El snapshot de `1_proyectos/` (incluidos los items que pasaron a `en_cola`) lo hace el hook `SessionStart`, no esta skill.

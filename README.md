# CEREBRO_CORE — canon compartido del Segundo Cerebro de Bind PSP

Repo compartido entre los tres PM/PO del equipo de Producto (Pablo Gomes, Nicolás Colón, Luciana Rudaz). Contiene lo único que debe ser **idéntico** en las tres instalaciones personales del Cerebro:

- `wiki/2_areas/` — el contexto fijo de la empresa.
- `wiki/3_recursos/` — el detalle técnico y los stores de datos acumulados (`datos/`).
- `CLAUDE.md` — el manual de ruteo y las reglas del sistema.
- `.claude/skills/` — las skills base.
- `.claude/settings.json` — hooks del sistema (bloqueo de escritura sobre estas rutas en cada install, snapshot/pull automático).
- `contexto_vivo/<pm>/` — buzón: items subidos por `/context_push` desde cada instalación personal, a la espera de `/context_merge`.
- `manifiestos/` — un archivo por cada corrida de `/context_merge`, el recibo de qué se ingirió y qué quedó pendiente.

## Regla central

**Nadie escribe acá a mano.** Este repo solo se actualiza a través de tres skills, corridas desde una instalación personal del Cerebro:

- `/context_push` (cualquier PM, ~diario) — sube items de `contexto_vivo/` local a `contexto_vivo/<pm>/` acá.
- `/context_merge` (solo el líder, ~semanal) — el único proceso autorizado a escribir `wiki/2_areas/` y `wiki/3_recursos/` de este repo.
- `/context_pull` (cualquier PM) — junto con el hook `SessionStart` de cada install, trae este repo actualizado y espeja `wiki/2_areas/`, `wiki/3_recursos/`, `CLAUDE.md`, `.claude/skills/` y `.claude/settings.json` hacia la instalación personal.

Ver `CLAUDE.md` para el detalle completo del modelo y las reglas de escritura.

## Instalación de un PM/PO nuevo

Este repo se clona aparte de la instalación personal del Cerebro (nunca dentro de ella). La ruta local del clon se declara en `identidad.local.md` (raíz de la instalación personal, nunca versionado), campo `ruta_clon_core`.

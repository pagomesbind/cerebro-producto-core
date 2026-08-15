---
name: audit_wiki
description: Auditoría estructural corta de wiki/ — detecta carpetas sin index.md, links relativos rotos, archivos huérfanos, archivos de detalle_productos/ sin Estado declarado o por encima del umbral de fisión, y nombres de la lista negra anti-cajón. No arregla nada solo, reporta desvíos para decidir cómo resolverlos.
when_to_use: Se activa cuando el usuario escribe de forma explícita el comando /audit_wiki en la terminal, o cuando el Bibliotecario quiere verificar la salud estructural de la wiki después de una reorganización grande.
disable-model-invocation: true
argument-hint: ""
---

# /audit_wiki — Auditoría estructural del Segundo Cerebro

Convierte en algo verificable en ~30 segundos las reglas estructurales que `CLAUDE.md` exige por escrito (Regla de Integridad de Índices, reglas anti-cajón, estado declarado en `detalle_productos/`) — en vez de confiar en que cada skill las cumplió sola.

## Paso 1 — Ejecutar el script

```bash
python .claude/skills/audit_wiki/scripts/audit.py
```

Usá `--json` si necesitás el resultado estructurado para procesarlo (ej. filtrar solo una categoría, o compararlo contra una corrida anterior).

El script chequea, sobre todo `wiki/`:
1. **Carpetas sin `index.md`/`proyecto.md`** — excluye las 3 excepciones documentadas en `CLAUDE.md`: `artefactos/` (y cualquier cosa debajo), las carpetas-hoja de `apis_expuestas/<funcionalidad>/`, y los lotes de `historial_raw/`.
2. **Links relativos rotos** — todo `[texto](ruta/relativa.md)` que no resuelve a un archivo real (ignora URLs `http(s)://` y `mailto:`).
3. **Archivos `.md` huérfanos** — no mencionados en el `index.md` de su propia carpeta (heurística por nombre de archivo en el texto del índice; falsos positivos posibles si el índice referencia el archivo con texto de link distinto al nombre de archivo — revisar antes de actuar).
4. **`detalle_productos/` sin `Estado:` declarado o por encima de ~300 líneas** (umbral de fisión) — excluye `apis_expuestas/`, que tiene su propio estándar.
5. **Nombres de la lista negra anti-cajón** — carpetas `transversal/`, `otros/`, `varios/`, `misc/`, `general/`; archivos `otros_manuales.md`, `manuales_operativos.md`.

## Paso 2 — Reportar, no arreglar solo

Esta skill **nunca corrige nada por su cuenta**. Presentá el resultado al usuario agrupado por categoría, con el conteo total arriba. Para cada categoría con hallazgos:
- **Links rotos**: si el patrón sugiere que el archivo se movió (mismo nombre de archivo en otra carpeta de `wiki/`), proponé la ruta nueva probable, pero no reescribas el link sin decisión — a menos que el usuario haya pedido explícitamente "arreglá los links rotos", en cuyo caso sí podés aplicar el fix mecánico determinista y reportar qué corregiste.
- **Carpetas sin índice**: proponé crear el `index.md` faltante con el formato estándar (qué contiene, tabla `Archivo | Contenido`, ver también, pie con fecha) — pedí confirmación si la carpeta tiene contenido ambiguo.
- **Archivos sin `Estado:`**: no inventes el estado — preguntale al usuario si es `en producción`, `discovery — no construido`, o `documentación desactualizada / en disputa` antes de declararlo.
- **Nombres de lista negra**: son una violación directa de la regla anti-cajón — proponé un plan de desarme (a qué archivo/carpeta temática migra cada pieza) y ejecutalo solo con aprobación del usuario, igual que cualquier reorganización de `wiki/`.

## Paso 3 — Cierre

Si el usuario pidió (y aprobó) alguna corrección durante esta corrida: si la corrección cae en `1_proyectos/`, aplicala directo y verificá índices locales. Si cae en `2_areas/`/`3_recursos/` (el caso típico — la mayoría de lo que esta skill audita es canon), **no la apliques vos**: capturala como item `tipo: conocimiento` en `contexto_vivo/` con el fix exacto (`destino_propuesto` = el archivo a corregir, cuerpo = el contenido corregido o el delta preciso) para que `/context_merge` la aplique. Si la corrida fue solo de diagnóstico, no generes ningún item — es una consulta de lectura, no una ingesta.

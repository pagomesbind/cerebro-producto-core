---
name: pdf_build
description: Convierte lo que se trabajó en la sesión/proyecto (un documento, una decisión, un resumen) en un PDF prolijo y con identidad visual — carátula, índice con números de página, y componentes reutilizables (pasos, tarjetas, callouts, cronograma). Pensado para entregar a un tercero (otra área de Bind PSP, o un cliente externo). Se activa con /pdf_build.
when_to_use: Se activa cuando el usuario ejecuta /pdf_build, típicamente cuando pide "pasar esto en limpio a un PDF", armar un documento para entregarle a alguien fuera de esta sesión/proyecto, o reutilizar el diseño ya usado en un PDF anterior para un documento nuevo.
disable-model-invocation: true
argument-hint: "[qué contenido convertir — ej. 'el documento funcional de X' o 'un resumen de la decisión de Y']"
---

# 📄 PDF PROLIJO PARA ENTREGAR: /pdf_build

## Por qué existe esta skill

Ya armamos un PDF con carátula, secciones numeradas, tarjetas, pasos, callouts y cronograma que quedó prolijo y reutilizable — ver `references/template.html` y `references/design-system.md`, que documentan ese sistema de diseño completo (paleta, tipografía, componentes, y los 2-3 bugs concretos que ya pisamos y no hay que volver a pisar). Esta skill existe para no rearmar ese trabajo de diseño cada vez: reutiliza el mismo esquema para cualquier documento nuevo que haya que entregarle a un tercero.

**Regla dura, no negociable:** el PDF resultante es para alguien fuera de esta sesión — otra área de Bind PSP, o un cliente externo. **No puede contener ninguna referencia a este Cerebro**: nada de "wiki", "Cerebro", nombres de skills o comandos (`/algo`), rutas de archivo internas (`wiki/...`, `.claude/...`), ni links a este repositorio. Si el contenido fuente menciona algo de eso, se reescribe en limpio antes de entrar al documento — nunca se transcribe tal cual. Esto aplica incluso si el documento es para gente interna de Bind PSP: ellos tampoco necesitan ver la infraestructura con la que se armó.

## Cuándo NO usarla

- El usuario quiere un archivo de trabajo interno (notas, un artefacto que vive en `wiki/`) — esto es para el entregable final, no para el registro de proceso.
- El contenido ya es un PDF o no necesita rediseño — no uses esta skill solo para convertir un archivo sin agregarle valor de diseño.
- Es una sola idea suelta de una línea — el índice y la carátula no aportan nada si no hay al menos 2-3 secciones reales.

## 🏃 Pipeline

### Paso 1 — Confirmar la estructura del documento ANTES de construir nada

No arranques a escribir HTML todavía. Primero armá un esquema en texto plano: título del documento, y la lista de secciones en el orden en que van a aparecer (cada una con una frase de qué va a cubrir). Mostráselo al usuario y esperá su confirmación o sus ajustes — es mucho más barato reordenar una lista de viñetas que rehacer un PDF ya maquetado.

Si el contenido fuente ya existe en la sesión (un artefacto, una decisión, un resumen que se armó antes), proponé el esquema basándote en eso — no le pidas al usuario que te dicte la estructura desde cero si ya tenés con qué inferirla. Si falta contenido para alguna sección, decilo explícitamente en vez de inventarlo.

### Paso 2 — Identidad visual

**Por defecto, y sin necesidad de preguntar, usá la marca de Bind PSP** — paleta, tipografía y logo documentados en [`references/brand-bind-psp.md`](references/brand-bind-psp.md). Es la que ya quedó aprobada en la última versión (v1.6) del documento de La Virginia, y es el caso de uso más común de esta skill: documentos que salen de Bind PSP hacia un tercero.

Solo te apartás de ese default cuando el documento es explícitamente para **otra organización** (por ejemplo, un documento que arma un cliente externo con su propia identidad, no un documento de Bind PSP hacia ese cliente). En ese caso sí preguntá:
- **Logo:** ¿hay un archivo para usar? ¿En qué variante (color, monocromático, sobre fondo claro u oscuro)?
- **Paleta:** ¿tienen colores de marca definidos (manual de marca, hex codes)? Si no los tienen a mano, proponé una paleta neutra de 2 colores en vez de inventar algo al azar — ver `references/design-system.md` (sección "Palette") para derivar los tintes a partir de un solo color.
- **Tipografía:** solo usá una fuente de marca si existe el archivo real (ver "Fonts" en el mismo documento) — si no, usá la fuente de sistema del template tal cual.

No asumas una paleta/logo de una organización *distinta* de Bind PSP sin que el usuario lo confirme explícitamente — el default de Bind PSP (Paso 2) es la única excepción a "no asumir", justamente porque ya está confirmado y aprobado.

### Paso 3 — Sanitizar el contenido

Antes de volcar cualquier texto al HTML, repasalo buscando: nombres de skills/comandos, rutas de archivo internas, la palabra "Cerebro" o "wiki", links a este repositorio, jerga de proceso interno ("gap registrado en...", "según el artefacto..."). Reescribí esas partes en lenguaje que tenga sentido para alguien que nunca vio este sistema — la información sustantiva se queda, el andamiaje se cae.

### Paso 4 — Construir el HTML

Copiá `references/template.html` como punto de partida (no lo edites in place — es la plantilla reutilizable). Reemplazá los tokens `{{...}}` — con los valores de `references/brand-bind-psp.md` salvo que el Paso 2 haya determinado otra marca —, armá una sección `<section class="doc-section" data-toc-title="...">` por cada entrada confirmada en el Paso 1, y elegí de `references/design-system.md` los componentes que correspondan a cada sección (pasos numerados para un flujo, tarjetas para actores/opciones paralelas, callouts para advertencias, cronograma para fechas). El logo (el de `assets/logo-bind-psp-azul-mono.png` por defecto, u otro si corresponde) se embebe como `data:` URI en base64 en `{{LOGO_DATA_URI}}` — no lo referencies por ruta de archivo, el PDF final tiene que ser autocontenido.

### Paso 5 — Generar el PDF

```bash
python "<ruta a esta skill>/scripts/build_pdf.py" <tu_documento.html> outputs/<nombre-descriptivo>.pdf
```

**El PDF final siempre se genera directo en `outputs/`** (raíz del repo) — es un entregable, no un artefacto de proyecto ni un archivo de trabajo, así que no va a `wiki/`. Nombre descriptivo en minúsculas y guiones bajos, sin fecha (si se regenera una versión nueva, se sobreescribe el mismo archivo — no se acumulan `v1`, `v2`, `_final`, etc.). Los HTML intermedios y los PDFs de prueba del Paso 6 quedan en tu carpeta de scratch, nunca en `outputs/`.

El script hace un render en dos pasadas para que el índice tenga números de página reales (arranca en la carátula = página 1) — no necesitás calcular vos los números de página, ni tocar el marcador `<!--TOC_ROWS-->` a mano. Si no encuentra Chrome/Edge automáticamente, pasale `--chrome <ruta>`.

### Paso 6 — Revisar antes de entregar

Abrí el PDF resultante (herramienta de lectura) y mirá, página por página:
- ¿La carátula ocupa una sola página, sin desborde?
- ¿El índice tiene los números de página correctos y coincide con dónde arranca cada sección?
- ¿Alguna imagen (especialmente el logo) se ve deformada? (ver "Flexbox image distortion" en `design-system.md` si algo se ve estirado)
- ¿El pie de página con el número aparece en todas las hojas?
- ¿Quedó algún rastro de jerga interna que se te escapó en el Paso 3?

Si algo falla, corregí el HTML y volvé a correr el Paso 5 — no le entregues al usuario un PDF con defectos visuales pidiendo que "lo revise él".

### Paso 7 — Entregar

Confirmá que el PDF quedó en `outputs/` y mandáselo al usuario desde ahí. No lo publiques ni lo compartas por ningún otro canal — el usuario decide a quién se lo manda.

## Referencias

- [`references/template.html`](references/template.html) — plantilla base con todos los componentes, comentada.
- [`references/design-system.md`](references/design-system.md) — catálogo de componentes, guía de paleta/tipografía, y los problemas concretos ya resueltos (desborde de carátula, logo deformado por flexbox, por qué Chrome headless y no Weasyprint, restricciones del índice de 2 pasadas).
- [`references/brand-bind-psp.md`](references/brand-bind-psp.md) — paleta, fuente y logo de Bind PSP a usar por defecto (§ Paso 2).
- [`assets/logo-bind-psp-azul-mono.png`](assets/logo-bind-psp-azul-mono.png) — logo por defecto.
- [`scripts/build_pdf.py`](scripts/build_pdf.py) — build de 2 pasadas (HTML → PDF con índice real).

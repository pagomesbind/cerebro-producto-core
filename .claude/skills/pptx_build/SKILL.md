---
name: pptx_build
description: Convierte lo que se trabajó en la sesión/proyecto (un documento, una decisión, un resumen) en una presentación PowerPoint prolija y con identidad visual de Bind PSP — slides de título/sección oscuras, contenido claro, tarjetas, pasos, cronograma, divisores. Pensado para entregar a un tercero (otra área de Bind PSP, o un cliente externo). Se activa con /pptx_build.
when_to_use: Se activa cuando el usuario ejecuta /pptx_build, típicamente cuando pide armar una presentación o un deck para entregarle a alguien fuera de esta sesión/proyecto, o reutilizar el diseño ya usado en una presentación anterior para un documento nuevo.
disable-model-invocation: true
argument-hint: "[qué contenido convertir — ej. 'una presentación del documento funcional de X' o 'un resumen de la decisión de Y']"
---

# 📊 PRESENTACIÓN PROLIJA PARA ENTREGAR: /pptx_build

## Por qué existe esta skill

Es la contraparte de [`/pdf_build`](../pdf_build/SKILL.md) para presentaciones: mismo objetivo (convertir contenido de trabajo en un entregable prolijo para un tercero), mismo flujo de 7 pasos, pero **un sistema de diseño propio**, con paleta, tipografía y componentes distintos.

**Fuente de verdad: el "house style" confirmado el 2026-08-10** — el deck final que el usuario terminó a mano a partir del primer borrador de esta skill (`raw/onboarding_estrategico_reunion_entendimiento.pptx`). El template oficial de marketing (`template_bind.pptx`) fue el punto de partida para colores/tipografía/logo/flor/íconos, pero el usuario lo consideró demasiado rígido y orientado a marketing para uso interno — construyó un deck completo, lo ajustó a su criterio, y **ese resultado reemplaza por completo al template como referencia de diseño**. No vuelvas al template ni a sus layouts propios ante ninguna duda — está retirado.

**Regla dura, no negociable — igual que en `pdf_build`:** la presentación resultante es para alguien fuera de esta sesión. **No puede contener ninguna referencia a este Cerebro**: nada de "wiki", "Cerebro", nombres de skills o comandos (`/algo`), rutas de archivo internas, ni links a este repositorio. Se reescribe en limpio antes de entrar a un slide — nunca se transcribe tal cual, incluso si la presentación es para gente interna de Bind PSP.

## Cuándo NO usarla

- El usuario quiere un archivo de trabajo interno — esto es para el entregable final.
- El contenido no tiene una estructura de "varios puntos/secciones" — una sola idea suelta no justifica un deck; puede ser un mail o un mensaje.
- El usuario pidió específicamente un documento de lectura corrida (no una presentación) — ahí corresponde `/pdf_build`, no esta skill.

## 🏃 Pipeline

### Paso 1 — Confirmar la estructura ANTES de construir nada

Armá un esquema en texto plano: título de la presentación, y la lista de slides en orden (una frase de qué cubre cada uno, y si es slide de título/sección — fondo oscuro — o de contenido — fondo claro, ver Paso 4). Mostráselo al usuario y esperá confirmación antes de tocar código — reordenar una lista de viñetas es gratis, rehacer un deck maquetado no.

Si el contenido fuente ya existe en la sesión, proponé el esquema basándote en eso en vez de pedirle al usuario que dicte la estructura desde cero.

### Paso 2 — Identidad visual

**Por defecto, sin necesidad de preguntar, usá la marca de Bind PSP** documentada en [`references/brand-bind-psp.md`](references/brand-bind-psp.md) — el house style confirmado, no el template de marketing.

Tipografía: Figtree (heading/cards) — instalada y lista para usar, ver `brand-bind-psp.md` §Fonts si necesitás los nombres exactos de familia por peso (Figtree Light/Medium son familias propias, no un flag de negrita). El cuerpo de las cards es Figtree Light, no Inter.

Solo te apartás de la marca Bind PSP cuando la presentación es explícitamente para otra organización — ahí preguntá por logo/paleta/tipografía igual que describe `pdf_build/SKILL.md` Paso 2, con la misma lógica (no inventar una paleta neutra al azar si no la tenés, no forzar una fuente que no existe como archivo real).

### Paso 3 — Sanitizar el contenido

Mismo criterio que `pdf_build` Paso 3: repasá el contenido buscando nombres de skills/comandos, rutas internas, "Cerebro"/"wiki", jerga de proceso interno, y reescribilo en lenguaje que tenga sentido para alguien que nunca vio este sistema.

### Paso 4 — Construir el deck

Usá [`scripts/deck_helpers.py`](scripts/deck_helpers.py) — no reescribas desde cero tarjetas/listas/headers/títulos, ya están resueltas ahí. Patrón:

```python
import sys
sys.path.insert(0, "<ruta a esta skill>/scripts")
from deck_helpers import *

prs = new_presentation()          # canvas 10x5.625"
set_deck_name("Nombre del deck")  # define el kicker fijo de TODAS las slides de contenido

s = cover_slide(prs, eyebrow="Nombre del deck", title="Bajada de la portada")

s = section_break_slide(prs, block_label="BLOQUE 1", title="Nombre del bloque",
                         variant="dark")  # o "yellow"/"gray"

s = light_slide(prs)
page_title(s, "Título del slide", icon="ico-05")  # ícono obligatorio, ver assets/icons/INDEX.md
card_row(s, Inches(0.67), Inches(1.72), Inches(8.62), Inches(1.43), [
    dict(title="Primera cosa", body="Cuerpo en Figtree Light."),
    dict(title="Segunda cosa", body="..."),
    dict(title="Tercera cosa", body="..."),
])  # colorea cada card distinto automáticamente — ver el catálogo abajo

s = closing_slide(prs, "¡Gracias!", subtitle="Preguntas y comentarios")

prs.save("outputs/<nombre-descriptivo>.pptx")
```

**Llamá `set_deck_name()` una sola vez, antes de la primera slide de contenido.** El kicker de cada slide es fijo — `"BIND PSP | <NOMBRE DEL DECK>"` — no cambia por sección (eso se probó y se simplificó adrede, ver `design-system.md` §"Qué cambió del template de marketing").

**Todo `page_title()` lleva un ícono obligatorio** — elegilo de [`assets/icons/INDEX.md`](assets/icons/INDEX.md)/`INDEX.png` según el tema real del slide, no repitas el mismo por comodidad. No hay línea divisoria bajo el título ni badge de número de página — ambos se sacaron a propósito.

**No busques una única "slide de contenido" genérica — elegí el componente según qué estás explicando:**

| Necesitás explicar... | Función |
|---|---|
| 3 (o N) cosas en paralelo — causas, opciones, roles | `card_row()` (colorea cada card distinto solo) |
| Unos pocos números/estadísticas sueltas | `stat_row()` |
| 2-3 objetivos/prioridades con una etiqueta (KR, prioridad) | `okr_row()` |
| Quién construye/es dueño de qué (equipo → lista de capacidades) | `team_block()` |
| Una lista enumerada de riesgos, próximos pasos, decisiones | `list_rows()` (no uses `bullets()` para esto) |
| Una agenda / índice | `index_rows()` |
| Un flujo real (secuencia, user journey, antes/después) | `page_title()` + `slide.shapes.add_picture()` de la imagen/diagrama real, junto a un `card()` de contexto tipo "Ejemplo N" |
| Prosa que no encaja en nada de lo anterior | `bullets()` |

Ver [`references/design-system.md`](references/design-system.md) §"Reference component library" para el detalle de cada uno con coordenadas y el razonamiento.

**No fuerces la grilla exacta de un slide anterior si el contenido no encaja** (distinta cantidad de ítems, distintas proporciones) — lo que sí es no negociable: tipografía, la rotación de colores de las cards, el header (logo + kicker fijo + ícono de tema + título, sin divisor, sin badge de página), y los tratamientos de flor/logo en portada y quiebres de sección.

### Paso 5 — Generar y guardar

`prs.save("outputs/<nombre-descriptivo>.pptx")` directo, dentro del script del Paso 4 — no hay un paso de build separado como en `pdf_build` (no hace falta una segunda pasada: PowerPoint no tiene el problema del índice con números de página reales que sí tiene el PDF). **El archivo final siempre se guarda en `outputs/`** (raíz del repo), nombre descriptivo sin fecha, sobrescribiendo si se regenera — igual convención que `pdf_build`.

### Paso 6 — Revisar antes de entregar

Esta máquina no tiene LibreOffice instalado, así que `scripts/office/soffice.py` de la skill base `pptx` va a fallar acá — no insistas con eso, es una limitación del entorno, no del deck. En su lugar:

1. **Vista previa aproximada** — [`scripts/approx_render.py`](scripts/approx_render.py) rasteriza cada slide a PNG leyendo directamente las shapes del `.pptx` (no es un motor OOXML real: no hay kerning ni layout exacto, pero sí detecta solapamientos, elementos fuera de canvas, colores equivocados o assets faltantes — el error de diseño más caro de no detectar antes de entregar). Usalo así:
   ```bash
   python scripts/approx_render.py outputs/mi_deck.pptx /tmp/preview mi_deck
   ```
   y armá una hoja de contactos para revisar varios slides de un vistazo:
   ```python
   from PIL import Image
   import glob
   files = sorted(glob.glob("/tmp/preview/*.png"))
   w, h = Image.open(files[0]).size
   cols = 2
   sheet = Image.new("RGB", (w*cols+20, h*((len(files)+1)//cols)+30), (200,200,200))
   for i, f in enumerate(files):
       sheet.paste(Image.open(f), ((i%cols)*(w+10)+5, (i//cols)*(h+10)+5))
   sheet.save("/tmp/preview/_contact.png")
   ```
   Miralo con el `Read` tool antes de dar el deck por terminado — encontrar un ícono que no cargó o un título que se corta ahí es gratis; encontrarlo después de mandárselo al usuario, no.
2. `markitdown <deck>.pptx` — confirmá que el contenido y el orden son correctos, sin texto placeholder ni jerga interna que se haya colado.
3. Reabrí el archivo con `python-pptx` (`Presentation(path)`, contar slides/shapes) como chequeo mínimo de que el archivo no quedó corrupto — es más confiable que `scripts/office/validate.py` de la skill base acá, porque ese script falla por un problema de codificación de caracteres propio de Windows en este entorno (no un defecto real del deck) apenas hay texto con tildes.
4. Si el usuario puede abrirlo en su propia PowerPoint, pedile una revisión visual antes de dar la presentación por terminada — sigue siendo el chequeo que más importa; `approx_render.py` reduce el riesgo de sorpresas, no lo reemplaza.

### Paso 7 — Entregar

Confirmá que el archivo quedó en `outputs/` y mandáselo al usuario desde ahí. No lo publiques ni lo compartas por ningún otro canal.

## Referencias

- [`references/brand-bind-psp.md`](references/brand-bind-psp.md) — paleta, fuentes, escala tipográfica, logos, flor decorativa, íconos — el house style confirmado.
- [`references/design-system.md`](references/design-system.md) — catálogo de componentes por caso de uso ("necesito explicar 3 cosas" → `card_row()`, etc.), qué cambió respecto al template de marketing, y el razonamiento detrás de cada patrón.
- [`assets/`](assets/) — logos (`logo-wordmark-light/dark/black.png`), flor (`flower-yellow/dark/white.png`), `icons/` (~97 íconos en `black/`+`white/`, con `INDEX.md` e `INDEX.png`), `fonts/` (Figtree + Inter).
- [`scripts/deck_helpers.py`](scripts/deck_helpers.py) — funciones reutilizables del house style (portada/sección/contenido/cierre, títulos de dos runs, cards, listas enumeradas, filas de índice, OKR, equipos).
- [`scripts/approx_render.py`](scripts/approx_render.py) — vista previa aproximada a PNG para QA visual sin LibreOffice (ver Paso 6).

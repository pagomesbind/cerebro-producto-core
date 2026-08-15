# Design system reference — pptx_build

Component catalogue for the **house style**: confirmed 2026-08-10 from the user's
own final, hand-finished deck
(`raw/onboarding_estrategico_reunion_entendimiento.pptx`) — not from
`template_bind.pptx` (marketing's template) directly. The template was the
starting point for colors/fonts/logo/flower/icon assets, but the user judged
its own slide layouts too rigid and marketing-oriented for internal decks;
they built one deck by hand starting from a `pptx_build` draft, kept what
worked, changed what didn't, and this file (plus `deck_helpers.py`) now
encodes that result as the reusable reference — **it fully replaces the
marketing template as the source of truth. This skill produces PPTX only —
there is no sibling medium to reconcile with.**

## Contents
- [Canvas](#canvas)
- [What changed from the marketing template](#what-changed-from-the-marketing-template)
- [The two-run title](#the-two-run-title)
- [Slide rhythm — light/dark alternation](#slide-rhythm--lightdark-alternation)
- [Section-break flower placement](#section-break-flower-placement)
- [Every content slide's header](#every-content-slides-header)
- [Reference component library — pick by what you're explaining](#reference-component-library--pick-by-what-youre-explaining)
- [Cards and color rotation](#cards-and-color-rotation)
- [Fidelity vs. layout — what to copy and what not to](#fidelity-vs-layout--what-to-copy-and-what-not-to)

## Canvas

**10in × 5.625in** (16:9), unchanged from the template. `new_presentation()`
sets this. Keep it — every coordinate in `deck_helpers.py` is calibrated to
this canvas.

## What changed from the marketing template

Confirmed 2026-08-10, after the user built and hand-edited a full deck from
this skill's first draft. These are deliberate simplifications, not gaps to
"fix back" toward template fidelity:

1. **No page-number badge, anywhere, on any slide.** Dropped entirely.
   `add_page_badge()` and the badge image assets no longer exist in this
   skill — don't reintroduce them.
2. **No rule/divider under the page title.** `page_title()` used to draw one;
   it doesn't anymore. Content starts with more breathing room instead
   (~1.7-1.85in from the top, not ~1.35in).
3. **The kicker is now a fixed, deck-wide label, not a per-section one.**
   Every content slide's top-right kicker reads `"BIND PSP | <deck name>"`
   (bold + light run), where `<deck name>` is set once via `set_deck_name()`
   at the start of the build script — not `"BLOQUE 1 · Situación actual"`
   changing slide to slide. `add_kicker()` no longer takes section-context
   arguments.
4. **The topic icon-badge next to the title is now mandatory, not optional.**
   Every content slide carries a small `F5F400` circle with a real topic
   icon (see `assets/icons/INDEX.md`) to the left of its 43pt title.
   `page_title()`'s `icon` parameter is required — don't build a content
   slide without picking one.
5. **Two off-brand colors seen in manual edits were corrected, not adopted:**
   a Google-default blue (`4285F4`, used a dozen times for "KR"/priority tag
   labels) and a pure yellow (`FFFF00`, one card). Both are normalized back
   to the real brand tokens (`AZUL` `4B64E6`, `AMARILLO` `F5F400`) in this
   module — if you ever see either hex again in a source file, it's drift,
   fix it.

## The two-run title

Still the most identifying trait, kept from the template: a title textbox
is built from 1-3 paragraphs of 1-3 runs each with independently set
font/weight/size/color — e.g. the cover's `"Onboarding Estratégico"` (bold
amarillo) immediately followed by `"Reunión de entendimiento"` (light
blanco) as the next paragraph in the same shape. `multi_text()` is the
primitive; `cover_slide()` and `section_break_slide()` already use it for
the two places this shows up. The page title itself (`page_title()`) is
back to a single run, 43pt bold — that's the confirmed simplification, not
an oversight; don't force it into two tones.

## Slide rhythm — light/dark alternation

`cover_slide()` and `section_break_slide()` (dark/yellow/gray variants) mark
structural transitions; everything else is `light_slide()` + `page_title()`.
Keep this alternation deliberate — it's the main signal of "we're starting a
new part of the deck."

## Section-break flower placement

Confirmed unchanged from the template: the flower is cropped to roughly its
right half, displayed in a tall narrow (~1:2 width:height) box — never the
full square next to text. Pairing, also unchanged:

| Panel | Flower variant | Title/subtitle color | Divider color | Logo variant |
|---|---|---|---|---|
| `#222222` (dark) | yellow | amarillo / blanco | blanco | dark (white text) |
| `#F5F400` (yellow) | white | negro | negro | black (monochrome) |
| `#F3F3F3` (gray) | yellow | negro | negro | light (black text) |

`section_break_slide(variant="dark"|"yellow"|"gray")` applies this table
automatically.

## Every content slide's header

Composed by `page_title()` (which calls `add_header()` for you):

- **Small logo, top-left** — `add_logo_small()`, fixed at 0.17,0.13, 0.86×0.32.
- **Kicker, top-right** — `add_kicker()`: `"BIND PSP "` bold + `"| <DECK NAME>"`
  light, 9pt, from `set_deck_name()`. Call `set_deck_name()` once before
  building any content slide.
- **Topic icon-badge + title** — `F5F400` circle (0.615in) with a real icon
  from `assets/icons/INDEX.md`, immediately left of the 43pt bold title at
  x=1.378. No divider beneath.

There is no footer element anymore (no page badge) — a content slide's
bottom edge is whatever its content components leave it at.

## Reference component library — pick by what you're explaining

This is the actual point of the house style: **don't reinvent a layout for
every new deck** — recognize which of these the content maps to and reuse
the matching component, even if the title/wording is completely different
next time.

| You need to explain... | Use | Function |
|---|---|---|
| 3 (or N) parallel things — causes, reasons, options | Card row, different color each | `card_row()` |
| A handful of independent stats/numbers | Big-number tiles in a row | `stat_row()` (call N times, or loop) |
| 2-3 prioritized objectives/KRs | Label + big colored value card, stacked | `okr_row()` (call once per priority) |
| Who owns what / roles and their scope | Card row (one card per role) | `card_row()` |
| Who builds what (team → capability list) | Narrow name card + stacked caps list | `team_block()` |
| An enumerated list of risks, next steps, decisions | Colored dot + bold lead + body, one per row | `list_rows()` |
| An agenda / table of contents | Numbered rows with rules | `index_rows()` |
| A before/after or two-path comparison diagram | Hand-built with `rounded_card()` + `divider()`/connectors, small centered boxes — no dedicated helper, compose from primitives | — |
| A real technical flow / sequence / user journey | `page_title()` + `slide.shapes.add_picture()` of the actual diagram/screenshot, alongside a `card()` captioned "Ejemplo N" with context | — |
| General prose that doesn't fit a structured shape | Bulleted paragraph | `bullets()` |

Don't default to `bullets()` for content that's actually enumerated
risks/steps/decisions — `list_rows()` is confirmed to read better for that
shape and is now the preferred component for it.

## Cards and color rotation

`card()` is the base unit: rounded rect, an icon-in-circle badge inset
top-left **in the same color as the card's own fill** (it's meant to blend
in — the icon glyph itself, auto-picked black/white, is what provides
contrast), a bold title, a light body.

**When laying out a row of 2-4 cards, vary the fill across the row** — use
`card_row()`, which rotates through `CARD_PALETTE` (`AZUL`,
`AMARILLO_TINT`, `AMARILLO`, `SURFACE`) automatically unless you pass an
explicit `fill` per item. A whole row of flat gray `SURFACE` cards is the
one thing to actively avoid — confirmed repeatedly in the reference deck:
"3 things" cards, stat tiles, and role cards all alternate color instead of
using one uniform neutral fill.

Card body copy is **9pt Figtree Light**, not Inter — `card()`'s defaults
already reflect this. For a secondary/nested card heading style (seen on
smaller supporting cards next to a bigger diagram), pass
`title_font=FONT_HEAD_MEDIUM` instead of the default bold `FONT_HEAD`.

## Fidelity vs. layout — what to copy and what not to

Don't force new content into one of the *exact* slide compositions from the
reference deck if it doesn't fit (different number of items, different
proportions). What's **not negotiable**: canvas size, the type scale, card
fills/typography rotating per the palette, the header (logo + fixed kicker
+ mandatory topic icon + title, no divider, no page badge), and the
flower/logo/section-break treatments above. Matching those consistently is
what makes a new deck read as the same system as the reference deck, even
when its actual slide composition is new.

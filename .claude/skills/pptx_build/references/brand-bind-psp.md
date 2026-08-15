# Default brand: Bind PSP (PPTX) — house style

**Use these values by default, without asking**, for any presentation deck, unless
it's explicitly for a different organization. This skill produces **PPTX only** —
there is no PDF/other-medium sibling to reconcile with.

Source of truth: the user's own final, hand-finished deck
(`raw/onboarding_estrategico_reunion_entendimiento.pptx`, confirmed
2026-08-10). Colors, fonts, logo/flower/icon assets originally came from
`template_bind.pptx` (marketing's official template) — but the user judged
that template's own slide *layouts* too rigid and marketing-oriented for
internal work, built a real deck by hand from this skill's first draft, and
what they kept/changed/simplified is now the reference. **The marketing
template is fully retired as a design source** — don't fall back to it or
its own layouts even as a tiebreaker.

## Token values

```
primary (dominant):     F5F400   yellow — the deck's #1 color by weight and frequency
secondary accent:       4B64E6   blue — the ONLY blue token, see note below
secondary accent, dark: 33277F   navy — darker blue, for small text/icons on light-blue tint
pale yellow tint:       FDFDC7   card/highlight backgrounds
dark panel:              222222   full-slide dark background (title/section slides)
ink on light:            000000   pure black — real color used for text/icons on light slides
divider / muted text:    999999   rule lines, secondary text, dividers
surface (light gray):    F3F3F3   card backgrounds where a tint isn't called for
closing-panel gray:      EFEFEF   the closing "¡Gracias!" slide panel — distinct from F3F3F3
white:                    FFFFFF
```

**Two off-brand colors seen in the reference deck's manual edits, confirmed
corrected — not adopted (2026-08-10):**
- `4285F4` (a Google-Slides-default blue, not `4B64E6`) appeared a dozen
  times on "KR"/priority tag labels. Normalized to `AZUL` (`4B64E6`).
- `FFFF00` (pure yellow) appeared once, on a single card. Normalized to
  `AMARILLO` (`F5F400`).

If either hex ever resurfaces in a generated file, it's drift from manually
picking a nearby swatch in PowerPoint's UI, not a new accent — fix it back.

## Fonts

**Heading / component system: Figtree** (Bold, Regular, and two separate
registered families "Figtree Light" and "Figtree Medium" — not weight flags).
Card/paragraph body copy is set in **Figtree Light**, not Inter — Inter is
kept available (`FONT_BODY`) for general free-form paragraphs that aren't
trying to look like a house-style component, but essentially everything in
practice uses `FONT_CARD_BODY = "Figtree Light"`.

**Status: installed.** The user provided both families (Google Fonts, OFL-
licensed) via `raw/Figtree/` and `raw/Inter/`. The weights shipped in this
skill and installed on this machine (`%LOCALAPPDATA%\Microsoft\Windows\Fonts`):

```
assets/fonts/Figtree-Regular.ttf   → family "Figtree" (Regular)
assets/fonts/Figtree-Bold.ttf      → family "Figtree" (Bold — use bold=True)
assets/fonts/Figtree-Light.ttf     → family "Figtree Light" (own family name, not a weight flag)
assets/fonts/Figtree-Medium.ttf    → family "Figtree Medium" (same — own family name)
assets/fonts/Inter-Regular.ttf     → registers as "Inter 24pt" on this machine (see note)
assets/fonts/Inter-Bold.ttf        → registers as "Inter 24pt" Bold
```

**Font-name quirk to remember:** the static Inter files distributed today are
built from Inter's variable font at a fixed optical size, so this exact build
registers its family as **"Inter 24pt"**, not plain "Inter". Generated decks
still write the family name as plain `"Inter"` (`FONT_BODY` in
`scripts/deck_helpers.py`) because that's the name most Inter distributions
register under — "Inter 24pt" is a local-install detail of this font drop,
not something to propagate into generated files.

License files kept alongside the fonts: `assets/fonts/Figtree-OFL.txt`,
`assets/fonts/Inter-OFL.txt`.

## Typographic scale (confirmed values, 10in canvas)

| Role | pt | Family | Notes |
|---|---|---|---|
| Cover eyebrow / title | 40 / 26 | Figtree Bold / Figtree Light | two paragraphs, one textbox — `cover_slide()` |
| Section-break label / title / subtitle | 15 / 32 / 15 | Figtree Bold / Figtree Bold / Figtree Light | `section_break_slide()` |
| Page title | 43 | Figtree Bold | single run now — no divider beneath — `page_title()` |
| Page title's sub-label (optional) | 12 | Figtree Light, `999999` | `page_title(sub=...)` |
| Card title | 14 | Figtree Bold (or Figtree Medium for a secondary/nested card) | `card()` |
| Card body | 9 | **Figtree Light** (not Inter) | `card()` |
| Team-block capability line | 11 | Figtree Medium, ALL CAPS, `999999` | `team_block()` |
| List-row lead / body | 14 | Figtree Bold (colored) / Figtree Light | `list_rows()` |
| Index-row title / body | 13 / 10 | Figtree Bold / Figtree Light | `index_rows()` |
| Stat/OKR value | 28 | Figtree Medium (bold) | `stat_row()`, `okr_row()` |
| Stat label / OKR description | 10.5-11 | Figtree Light | `stat_row()`, `okr_row()` |
| Kicker (top-right, deck-wide) | 9 | Figtree Bold + Figtree Light | `"BIND PSP "` + `"| <NAME>"` — `add_kicker()` |
| Closing slide message | 54 | Figtree Bold | `closing_slide()` |

## Logos

Three wordmark variants — always match the variant to the slide/panel background:

- [`../assets/logo-wordmark-light.png`](../assets/logo-wordmark-light.png) — black text, yellow flower. Light/white backgrounds.
- [`../assets/logo-wordmark-dark.png`](../assets/logo-wordmark-dark.png) — white text, yellow flower. The `#222222` dark panel.
- [`../assets/logo-wordmark-black.png`](../assets/logo-wordmark-black.png) — black text, **black** flower (fully monochrome). The `#F5F400` yellow panel.

`add_logo()` / `add_logo_small()` take `variant="light"|"dark"|"black"`.

## Decorative flower mark

Three color variants, all the same yellow eight-point-star mark:

- [`../assets/flower-yellow.png`](../assets/flower-yellow.png) — on the dark `#222222` panel.
- [`../assets/flower-white.png`](../assets/flower-white.png) — on the yellow `#F5F400` panel.
- [`../assets/flower-dark.png`](../assets/flower-dark.png) — on light/gray panels.

**Never place the full square mark next to a title block without checking
clearance.** It's always cropped to roughly the right half of the source
square PNG, displayed in a ~1:2 width:height box — a tall narrow sliver, not
a wide star. `add_flower()` defaults (`width=2.09in, height=4.18in,
crop_left=0.499, crop_right=0.001`) already reproduce this — kept unchanged
from the template, still correct in the reference deck's own section-break
slides.

## Page-number badge — removed

**Confirmed dropped, 2026-08-10.** No slide in the reference deck carries a
page number. `add_page_badge()` no longer exists in `deck_helpers.py`, and
the badge image assets have been deleted from `assets/`. Don't add page
numbers back.

## Icon set

[`../assets/icons/`](../assets/icons/) — **~97 real line icons** (fintech
domain: bank, wallet, safe, alert, credit card, calculator, charts, invoice,
security shield, growth…), in `black/` and `white/` recolored variants. See
[`icons/INDEX.md`](../assets/icons/INDEX.md) for a number→description table
and curated shortlist, and [`icons/INDEX.png`](../assets/icons/INDEX.png)
for a contact sheet to browse visually.

**Confirmed mandatory on every content slide, 2026-08-10** — not optional.
Every content slide in the reference deck carries a topic-relevant icon in
the `F5F400` circle next to its title (`page_title(..., icon="ico-NN")`,
required parameter), plus most cards carry one too
(`card(..., icon="ico-NN")`) in a badge matching the card's own fill color.
Pick the icon that actually fits the slide's topic — don't reuse the same
one everywhere out of convenience; browse `INDEX.png` first.

## Section-marker / card icon-badge color

**Confirmed 2026-08-10: the icon badge is the SAME color as whatever it sits
on** (the title's badge is always `F5F400`; a card's icon badge matches that
card's own fill, even on `AZUL`/dark cards) — it's meant to blend in, not
pop as a contrasting chip. What actually provides contrast is the icon
glyph itself (auto-picked black or white by `icon_badge()`/`card()`based on
the fill's luminance). This reverses what an earlier version of this file
said (icon badge should contrast against its surroundings) — that was
correct for the marketing template, wrong for the house style.

## A trap in the (retired) marketing template

Kept for historical reference only, in case anything ever needs re-deriving
from `template_bind.pptx` again: its `ppt/theme/theme1.xml` and
`theme2.xml` are both stock, unmodified Google Slides themes — no real
branding lives there, all of it is direct formatting on individual shapes.
Trusting a theme file or a filename over actually rendered content is what
produced this file's original (wrong) claim that the icon set was generic
stock art. If you ever need to look at that template again, read shape XML
directly, don't trust `<a:clrScheme>`/`<a:fontScheme>`.

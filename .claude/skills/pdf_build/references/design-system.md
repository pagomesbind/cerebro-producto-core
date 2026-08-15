# Design system reference — pdf_build

This is the component catalogue and the list of things that went wrong while
building the first document this skill is based on. Read the relevant
section when you need it; you don't need to read this end-to-end before
building.

## Contents
- [Palette](#palette)
- [Fonts](#fonts)
- [Component catalogue](#component-catalogue)
- [Cover bleed — when to use it, why it broke things when misused](#cover-bleed)
- [Flexbox image distortion](#flexbox-image-distortion)
- [PDF generation mechanics](#pdf-generation-mechanics)
- [TOC / page-count constraints](#toc--page-count-constraints)
- [Margins](#margins)

## Palette

The template uses two accent roles, not a rainbow:
- **Primary** — the main accent. Section rule lines, numbered step badges,
  card headers, table header rows, links, the "positive outcome" state in
  any flow diagram.
- **Highlight** — a second accent used sparingly, for "pay attention to
  this" callouts (warnings, exceptions, things that could go wrong). If the
  brand only gives you one accent color, skip the highlight variant and
  reuse a tint of primary, or fall back to a neutral gray-on-cream — don't
  invent a color the brand doesn't have.

For each accent, you need three values: the solid color (borders, buttons,
badges), a darker shade (small text sitting on a tinted background — solid
color often fails contrast at 10px), and a light tint (~8-12% of the solid
color mixed into white — card/table/callout backgrounds). If you only have
the solid hex, compute the tint by mixing: `tint = solid * 0.12 + white * 0.88`.

If the person you're building this for gives you an actual brand manual,
use their documented palette and tints exactly — don't improvise a
"close enough" color. If they don't have one, ask what 1-2 colors they'd
like, or default to a neutral, professional pairing (e.g. a mid blue
primary, warm amber highlight) rather than picking something arbitrary.

## Fonts

Prefer whatever the brand's actual typeface is, but only embed it via
`@font-face` if you have the actual font file (system-installed or
provided) and can point to it with a real path. On Windows, common
geometric sans fonts often already live in `C:\Windows\Fonts\` (e.g.
`GOTHIC.TTF` for Century Gothic) — check before assuming you need a
download. If there's no available font file, don't fake it — just use a
clean system sans (`Segoe UI`, `Arial`) for everything. A document with one
honest font beats one that silently falls back and looks inconsistent with
what was promised.

Body copy should stay in a plain system sans regardless of the heading
font — display/geometric fonts get hard to read at 10-11px over long
paragraphs.

## Component catalogue

All defined in `template.html`, section-numbered comments match this list:

| Component | Class | Use for |
|---|---|---|
| Cover | `.cover` | Title page — logo, title, subtitle, version/date |
| Table of contents | `.toc-page` | Auto-filled by `build_pdf.py`, don't hand-edit rows |
| Section header | `h2` with `<span class="num">` | Every top-level section |
| Table | plain `<table>` | Structured comparisons, reference data |
| Numbered steps | `ol.step-list` | Sequential processes, workflows |
| Callout | `.callout` / `.callout.attention` | Important context / warnings |
| Entity cards | `.card-grid` + `.card` | 2-4 actors, options, or parallel features |
| Labeled list | `.labeled-list` | Item + one-line rationale ("what" + "why") |
| Timeline | `.timeline` | Milestone dates across a horizontal axis |
| Stage card | `.stage-card` | Content grouped under a phase/stage heading |
| Mockup tag | `.mock-tag` | Flag any illustrative/placeholder screen clearly |

Don't invent new top-level visual patterns unless none of these fit — reuse
before you improvise, that's the entire point of having a reference doc.

## Cover bleed

The cover in the template has a **white** background, same as the rest of
the document, so it needs no special handling — it's just a full-height
page like any other.

If a document needs a cover with a *different* background (e.g. a dark
brand color, full-bleed image) that must reach the physical edge of the
paper, past the `@page` margin, you'd normally do this with a negative
margin equal to the page margin, then compensating padding to bring content
back to the text column. **Only do this if the cover's background actually
differs from the page background.** The first version of this template did
it unconditionally (leftover from an earlier dark cover), and once the
cover background changed to match the rest of the page, the leftover
negative-margin/padding math combined with absolutely-positioned children
caused the title block to render partially off-page and the whole cover to
overflow onto a second, nearly blank page. If you add a bleeding cover,
verify page count is still 1 for the cover afterward (see
[TOC / page-count constraints](#toc--page-count-constraints)).

## Flexbox image distortion

If you put an `<img>` (like a logo) inside a `display:flex` container
without giving the image an explicit `width`, flexbox's default
`align-items: stretch` will stretch it to fill the cross-axis width,
squashing its aspect ratio — even though you only set a `height`. This
happened with a logo positioned via `flex-direction: column` in an earlier
version and it rendered visibly warped.

Two fixes, either works:
- Take the image out of flex flow entirely with `position: absolute`
  (what `template.html` does for the cover logo), or
- Keep it in flow but add `align-self: flex-start` (or `width: auto` isn't
  enough on its own — the stretch happens regardless of intrinsic size).

Always open the rendered PDF and actually look at any embedded image before
calling a build done — this class of bug is invisible in the HTML source,
it only shows up in the rendered output.

## PDF generation mechanics

Rendering is Chrome/Edge/Chromium headless print-to-pdf, driven by
`scripts/build_pdf.py`:

```
python build_pdf.py <input.html> <output.pdf>
```

The script auto-detects Chrome/Edge on Windows/macOS/Linux; pass
`--chrome <path>` if it can't find yours. Key flags it uses under the hood
(for reference, you don't need to run Chrome directly):
`--headless --disable-gpu --no-sandbox --no-pdf-header-footer
--print-to-pdf=<path>`. The `--no-pdf-header-footer` flag matters — without
it Chrome injects its own date/URL header and footer on every page, which
visually collides with the custom `@page` footer in the template.

Weasyprint was tried first as an alternative and rejected: it needs
GTK/Pango/Cairo native libraries that aren't installed by default on
Windows, and getting them installed is its own yak-shave. Chrome headless
needs nothing beyond Chrome already being on the machine.

## TOC / page-count constraints

`build_pdf.py` renders the document **twice**: once with placeholder TOC
rows to find out what page each section lands on, then again with the real
page numbers filled in. This only works if the TOC page occupies the same
number of physical pages both times — which it will, as long as:

- You don't add or remove TOC rows between the two passes (the script
  handles this correctly on its own, don't intervene).
- The TOC has few enough entries to fit on the one page reserved for it in
  the template (roughly 12-15 rows at the default font size). If you have
  more sections than that, either shrink `.toc-row` font-size, or accept a
  2-page TOC and extend `.toc-page`'s `page-break-after` handling — don't
  just hope it fits.
- Nothing else in the document changes between the two renders (the script
  guarantees this by using the same HTML source for both, minus the TOC
  marker).

If a section's title text also appears verbatim somewhere earlier in the
document (e.g. referenced in the TOC itself, or quoted in an earlier
section), the page-lookup could match the wrong occurrence. The script
searches forward from the previous match to avoid this, but keep section
titles reasonably distinct as a matter of course.

## Margins

Default in the template: A4, 20mm left / 10mm top / 10mm right / 10mm
bottom. The wider left margin reads better for dense paragraph text (gives
a visual gutter without wasting the whole page); it's not a hard rule —
if the person you're building for wants symmetric margins, change the
single `@page { margin: ... }` line and rerun. Nothing else in the
stylesheet depends on the specific values.

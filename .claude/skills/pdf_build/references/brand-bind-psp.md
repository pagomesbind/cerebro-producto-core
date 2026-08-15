# Default brand: Bind PSP

**Use these values by default, without asking, unless the document is explicitly
for a different organization** (e.g. a document being handed to an external
client under their own identity, not Bind PSP's). This is the exact palette,
font, and logo from the latest approved version (v1.6) of the La Virginia
onboarding document — the one this whole design system was built from. If a
newer Bind PSP brand manual shows up in `raw/` later and changes any of this,
update this file, don't just override it ad hoc per document.

## Token values

Drop these straight into `template.html`'s `:root` block:

```css
--brand-primary: #4C65E6;        /* azul */
--brand-primary-dark: #33449E;
--brand-primary-tint: #EEF1FD;
--brand-ink: #2E2E2E;            /* gris */
--brand-ink-soft: #55534f;
--brand-highlight: #F5F400;      /* amarillo */
--brand-highlight-tint: #FDFBD8;
--brand-highlight-border: #D6D400;
--brand-line: #E1E1DF;
--brand-surface: #F4F4F3;
```

## Font

`Century Gothic` for headings (`--font-heading`), system sans for body —
already installed on this machine at `C:\Windows\Fonts\GOTHIC.TTF` (regular)
and `C:\Windows\Fonts\GOTHICB.TTF` (bold). Embed with:

```css
@font-face {
  font-family: 'Century Gothic';
  src: url('file:///C:/Windows/Fonts/GOTHIC.TTF') format('truetype');
  font-weight: 400;
}
@font-face {
  font-family: 'Century Gothic';
  src: url('file:///C:/Windows/Fonts/GOTHICB.TTF') format('truetype');
  font-weight: 700;
}
```

Set `--font-heading: 'Century Gothic', 'Segoe UI', Arial, sans-serif;`. If
you're building on a machine where that font file isn't at this path, check
`C:\Windows\Fonts\` for it before falling back — don't silently drop to
`Segoe UI` without checking first, the whole point of a default brand is
that it should just work.

## Logo

[`../assets/logo-bind-psp-azul-mono.png`](../assets/logo-bind-psp-azul-mono.png)
— the monochromatic blue version (matches `--brand-primary`), on transparent
background. This is what goes in the cover's `{{LOGO_DATA_URI}}` slot by
default (base64-encode it — see Paso 4 in `SKILL.md`). Only swap to a
different logo variant (color, white-on-dark, etc.) if the specific document
calls for a different background treatment than the white cover in the
template — don't reach for a different logo file just for variety.

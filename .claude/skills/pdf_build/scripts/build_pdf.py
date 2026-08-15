#!/usr/bin/env python3
"""
Two-pass HTML -> PDF builder with an accurate table of contents.

Why two passes: a table of contents needs real page numbers, but you only
know what page a section lands on *after* the whole document is laid out.
So this script renders once with placeholder page numbers, reads back the
actual page each section starts on, fills in the real numbers, and renders
again. The second render is the only one you keep.

Usage:
    python build_pdf.py <input.html> <output.pdf> [--chrome PATH]

Expects the input HTML to contain:
  - Section markers: <section class="doc-section" data-toc-title="...">
    one per entry that should appear in the table of contents, in document
    order. The data-toc-title text is exactly what's printed in the TOC row.
  - A TOC insertion point: <!--TOC_ROWS--> somewhere inside the page that
    should hold the table of contents (typically right after the cover).
  - A footer that prints the page number via CSS (see reference template) —
    this script does not touch page numbering, only the TOC row content.

The @page CSS must already be final (margins, size) before running this —
changing page geometry between passes would invalidate the page map.
"""

import argparse
import re
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

try:
    from pypdf import PdfReader
except ImportError:
    sys.exit("Missing dependency: pip install pypdf")

TOC_MARKER = "<!--TOC_ROWS-->"
SECTION_RE = re.compile(
    r'<section[^>]*class="doc-section"[^>]*data-toc-title="([^"]*)"', re.IGNORECASE
)


def find_chrome() -> str:
    candidates = [
        r"C:\Program Files\Google\Chrome\Application\chrome.exe",
        r"C:\Program Files (x86)\Google\Chrome\Application\chrome.exe",
        r"C:\Program Files\Microsoft\Edge\Application\msedge.exe",
        r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe",
        "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome",
        "/usr/bin/google-chrome",
        "/usr/bin/google-chrome-stable",
        "/usr/bin/chromium-browser",
        "/usr/bin/chromium",
    ]
    for c in candidates:
        if Path(c).exists():
            return c
    found = shutil.which("chrome") or shutil.which("google-chrome") or shutil.which("chromium")
    if found:
        return found
    sys.exit(
        "Could not find a Chrome/Edge/Chromium executable. Pass --chrome <path> explicitly."
    )


def render_pdf(html_path: Path, pdf_path: Path, chrome: str) -> None:
    if pdf_path.exists():
        pdf_path.unlink()
    uri = html_path.resolve().as_uri()
    cmd = [
        chrome,
        "--headless",
        "--disable-gpu",
        "--no-sandbox",
        "--no-pdf-header-footer",
        f"--print-to-pdf={pdf_path.resolve()}",
        uri,
    ]
    result = subprocess.run(cmd, capture_output=True, text=True, timeout=60)
    if not pdf_path.exists():
        sys.exit(f"Chrome did not produce a PDF.\nstdout: {result.stdout}\nstderr: {result.stderr}")


HTML_COMMENT_RE = re.compile(r"<!--.*?-->", re.DOTALL)


def extract_section_titles(html: str) -> list[str]:
    # Strip comments first — the template's own instructional comments contain
    # an example "data-toc-title" attribute that would otherwise match too.
    titles = SECTION_RE.findall(HTML_COMMENT_RE.sub("", html))
    if not titles:
        sys.exit(
            'No <section class="doc-section" data-toc-title="..."> markers found. '
            "See the template for the expected structure."
        )
    return titles


def build_toc_rows(titles: list[str], page_for_title: dict[str, int]) -> str:
    rows = []
    for title in titles:
        page = page_for_title.get(title, "?")
        rows.append(
            f'<div class="toc-row"><span class="toc-title">{title}</span>'
            f'<span class="toc-dots"></span><span class="toc-page-num">{page}</span></div>'
        )
    return "\n".join(rows)


COVER_AND_TOC_PAGES = 2  # template contract: 1-page cover + 1-page TOC before any body section


def find_pages_for_titles(pdf_path: Path, titles: list[str]) -> dict[str, int]:
    reader = PdfReader(str(pdf_path))
    page_for_title: dict[str, int] = {}
    # Start after the cover+TOC pages, not at page 0 — a section's title text
    # also appears verbatim on the TOC page itself (that's the whole point of
    # a TOC), so searching from the very start would match the TOC listing
    # instead of the actual section and report every entry as landing on the
    # same page. If you change the template to add/remove cover or TOC pages,
    # update COVER_AND_TOC_PAGES to match.
    search_from = min(COVER_AND_TOC_PAGES, len(reader.pages) - 1)
    for title in titles:
        # Search strictly forward from the last match so repeated/similar
        # titles resolve to the correct, later occurrence. Whitespace is
        # stripped entirely (not just collapsed) before comparing: the TOC
        # row prints "1. Title" with a space after the number, but the
        # actual <h2> markup has no space between the "1." span and the
        # title text, and PDF text extraction doesn't reliably preserve
        # inline-element spacing either way — comparing on letters only
        # sidesteps both sources of drift.
        needle = re.sub(r"\s+", "", title)
        for i in range(search_from, len(reader.pages)):
            text = re.sub(r"\s+", "", reader.pages[i].extract_text() or "")
            if needle and needle in text:
                page_for_title[title] = i + 1  # 1-based, matches CSS counter(page)
                search_from = i
                break
        else:
            page_for_title[title] = None
    missing = [t for t, p in page_for_title.items() if p is None]
    if missing:
        print(
            "WARNING: could not locate these sections in the rendered PDF "
            f"(TOC will show '?'): {missing}",
            file=sys.stderr,
        )
    return page_for_title


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("input_html")
    ap.add_argument("output_pdf")
    ap.add_argument("--chrome", default=None, help="Path to Chrome/Edge/Chromium executable")
    args = ap.parse_args()

    html_path = Path(args.input_html)
    output_pdf = Path(args.output_pdf)
    chrome = args.chrome or find_chrome()

    html = html_path.read_text(encoding="utf-8")
    if TOC_MARKER not in html:
        sys.exit(f"Input HTML is missing the {TOC_MARKER} insertion point.")

    titles = extract_section_titles(html)

    with tempfile.TemporaryDirectory() as tmp:
        tmp = Path(tmp)

        # Pass 1: placeholder TOC (same row count/height as final -> same
        # page count), render, and read back which page each section lands on.
        placeholder_rows = build_toc_rows(titles, {t: "\u2014" for t in titles})
        pass1_html = tmp / "pass1.html"
        pass1_html.write_text(html.replace(TOC_MARKER, placeholder_rows), encoding="utf-8")
        pass1_pdf = tmp / "pass1.pdf"
        render_pdf(pass1_html, pass1_pdf, chrome)

        page_for_title = find_pages_for_titles(pass1_pdf, titles)

        # Pass 2: real TOC, final render.
        final_rows = build_toc_rows(titles, page_for_title)
        final_html = tmp / "final.html"
        final_html.write_text(html.replace(TOC_MARKER, final_rows), encoding="utf-8")
        render_pdf(final_html, output_pdf, chrome)

    print(f"Built {output_pdf} ({len(titles)} TOC entries)")
    for t in titles:
        print(f"  p.{page_for_title.get(t, '?')}  {t}")


if __name__ == "__main__":
    main()

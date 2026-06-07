"""
Portfolio PDF Generator — Shraddha Singh
Converts portfolio case study markdown files to styled PDFs.

Usage:
  ~/opt/anaconda3/bin/python second-brain/portfolio/generate_pdf.py

Output: PDF written next to the source .md file.
"""
import asyncio
import markdown
from pathlib import Path
from playwright.async_api import async_playwright

PORTFOLIO_DIR = Path(__file__).parent
CASE_STUDIES  = PORTFOLIO_DIR / "case-studies"

CASE_STUDY_CSS = """
@page { margin: 0; }

* { box-sizing: border-box; margin: 0; padding: 0; }

body {
    font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', 'Helvetica Neue', Arial, sans-serif;
    font-size: 10pt;
    line-height: 1.6;
    color: #1C2B39;
    background: #fff;
}

/* ── HEADER BAND ─────────────────────────────────── */

h1 {
    background: #0A2342;
    color: #fff;
    font-size: 22pt;
    font-weight: 700;
    letter-spacing: 2.5px;
    text-transform: uppercase;
    margin: 0;
    padding: 20px 40px 3px;
    line-height: 1.1;
}

h1 + p {
    background: #0A2342;
    margin: 0;
    padding: 3px 40px 12px;
    font-size: 10pt;
    color: #6FB3D8;
    letter-spacing: 0.3px;
    line-height: 1.3;
}

h1 + p strong {
    color: #6FB3D8;
    font-weight: 400;
}

h1 + p + p {
    background: #EBF2F8;
    border-bottom: 1.5px solid #B8CFDF;
    margin: 0;
    padding: 6px 40px 7px;
    font-size: 8.5pt;
    color: #34566B;
    line-height: 1.4;
}

h1 + p + p a {
    color: #1B6CA8;
    text-decoration: none;
}

h1 + p + p + hr {
    border: none;
    margin: 10px 0 0;
}

hr {
    border: none;
    border-top: 0.5px solid #C8D5E2;
    margin: 8px 40px 0;
}

/* ── SECTION HEADERS ─────────────────────────────── */

h2 {
    font-size: 8pt;
    font-weight: 700;
    text-transform: uppercase;
    letter-spacing: 2px;
    color: #0A2342;
    border-left: 3px solid #0A2342;
    padding: 0 0 0 10px;
    margin: 16px 40px 6px;
    line-height: 1.4;
    page-break-after: avoid;
}

/* ── SUBSECTION / COMPANY HEADERS ───────────────── */

h3 {
    font-size: 10.5pt;
    font-weight: 700;
    color: #0A2342;
    margin: 10px 40px 0;
    letter-spacing: 0.2px;
    page-break-after: avoid;
}

/* Status/Stack line directly after h3 — muted metadata */
h3 + p {
    font-size: 8.5pt;
    color: #4A6070;
    margin: 1px 40px 6px;
    line-height: 1.4;
}

h3 + p strong {
    color: #34566B;
    font-weight: 600;
}

h3 + p em {
    color: #6B7F8E;
    font-style: italic;
}

/* ── BODY TEXT ───────────────────────────────────── */

p {
    font-size: 10pt;
    color: #1C2B39;
    margin: 0 40px 7px;
    line-height: 1.6;
    page-break-inside: avoid;
}

/* Intro italic callout */
p em {
    font-style: italic;
    color: #4A6070;
}

/* ── SUB-LABELS (h4) — Writing, Research, API Design ── */

h4 {
    font-size: 9pt;
    font-weight: 700;
    color: #1B6CA8;
    margin: 10px 40px 3px;
    letter-spacing: 0.2px;
    text-transform: uppercase;
    page-break-after: avoid;
}

/* ── LISTS ───────────────────────────────────────── */

ul {
    margin: 3px 40px 8px 58px;
    padding: 0;
}

ol {
    margin: 3px 40px 8px 58px;
    padding: 0;
}

li {
    font-size: 10pt;
    line-height: 1.6;
    margin-bottom: 3px;
    color: #1C2B39;
    page-break-inside: avoid;
}

li strong {
    color: #0A2342;
}

/* ── TABLES ──────────────────────────────────────── */

table {
    width: calc(100% - 80px);
    margin: 5px 40px 10px;
    border-collapse: collapse;
    font-size: 9pt;
    line-height: 1.45;
    page-break-inside: avoid;
}

thead tr th {
    background: #0A2342;
    color: #fff;
    font-size: 7.5pt;
    font-weight: 700;
    letter-spacing: 1px;
    text-transform: uppercase;
    padding: 6px 10px;
    text-align: left;
}

td {
    padding: 5px 10px;
    vertical-align: top;
    border-bottom: 0.5px solid #DDE6EE;
    color: #2C3E50;
}

tr:nth-child(even) td {
    background: #F5F8FB;
}

td:first-child {
    font-weight: 600;
    color: #0A2342;
    width: 28%;
}

/* ── EMPHASIS ────────────────────────────────────── */

strong {
    font-weight: 700;
    color: #0A2342;
}

a {
    color: #1B6CA8;
    text-decoration: none;
}

blockquote {
    display: none;
}

/* ── SUBHEADINGS within body ─────────────────────── */

h4 {
    font-size: 9.5pt;
    font-weight: 700;
    color: #0A2342;
    margin: 8px 40px 3px;
    letter-spacing: 0.3px;
}
"""


def md_to_html(md_path: Path, css: str, title: str) -> str:
    text = md_path.read_text(encoding="utf-8")
    body = markdown.markdown(text, extensions=["tables", "fenced_code"])
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<title>{title}</title>
<style>{css}</style>
</head>
<body>
{body}
</body>
</html>"""


async def main():
    print("Portfolio PDF Generator — Shraddha Singh")
    print("=" * 50)

    target = CASE_STUDIES / "ai-leverage-pm.md"
    if not target.exists():
        print(f"  ✗ Not found: {target}")
        return

    out_pdf = CASE_STUDIES / "Shraddha_Singh_AI_Product_Management.pdf"

    async with async_playwright() as p:
        browser = await p.chromium.launch()
        page    = await browser.new_page()

        html = md_to_html(target, CASE_STUDY_CSS, "Shraddha Singh — AI Product Management")
        await page.set_content(html, wait_until="domcontentloaded")
        await page.pdf(
            path=str(out_pdf),
            format="A4",
            margin={"top": "0", "bottom": "10mm", "left": "0", "right": "0"},
            print_background=True,
        )
        await browser.close()

    print(f"  ✓ PDF written → {out_pdf.relative_to(out_pdf.parents[3])}")
    print(f"\nNext step: Upload to Google Drive and copy the shareable link.")


asyncio.run(main())

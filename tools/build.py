#!/usr/bin/env python3
"""Build the site's HTML pages from the sources in tools/pages/.

Why this exists: every page shares the same header, nav, footer and asset
links. Those shared parts live ONCE in this file; the per-page content and
<head> metadata live in tools/pages/<name>.html. The built pages in the repo
root are committed, so hosting (Cloudflare) needs no build step.

To change a page's content .... edit tools/pages/<name>.html, run this script.
To change nav, footer, fonts .. edit the templates below, run this script.
Never edit the root *.html files directly - the next build overwrites them.

Usage:  python3 tools/build.py            # builds every page
        python3 tools/build.py about      # builds one page

Source file format (tools/pages/<name>.html):
    <!-- page:head -->
      ... this page's <title>, meta, canonical, favicon, JSON-LD ...
    <!-- /page:head -->
    ... this page's <main> content (and any sections outside <main>) ...
"""
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
PAGES_DIR = Path(__file__).resolve().parent / "pages"

# Order here is the order of links in the nav.
NAV = [
    ("index.html", "Home"),
    ("about.html", "About Us"),
    ("volunteer.html", "Volunteer"),
    ("thrift.html", "Thrift Shop"),
    ("gift-shop.html", "Gift Shop"),
    ("impact.html", "Our Impact"),
    ("contact.html", "Contact"),
]

# Shared <head> additions: fonts, stylesheet, theme color.
ASSETS = """\
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Newsreader:ital,opsz,wght@0,6..72,400;0,6..72,500;0,6..72,600;1,6..72,400&display=swap" rel="stylesheet">
  <link rel="stylesheet" href="assets/css/site.css">
  <meta name="theme-color" content="#faf8f4">"""


def header(page: str) -> str:
    links = "\n".join(
        f'          <li><a href="{href}" class="nav__link"'
        f'{" aria-current=\"page\"" if href == page else ""}>{label}</a></li>'
        for href, label in NAV
    )
    return f"""\
  <a href="#main-content" class="skip-link">Skip to main content</a>

  <header class="site-header">
    <div class="site-header__inner">
      <a href="index.html" class="brand">
        <img src="assets/images/rih-emblem-160.png" alt="RIH Auxiliary Logo" width="32" height="32">
        <span>RIH Auxiliary</span>
      </a>
      <button class="nav-toggle" aria-controls="site-nav" aria-expanded="false" aria-label="Toggle navigation menu"><span></span></button>
      <nav class="nav" id="site-nav" aria-label="Main">
        <ul class="nav__list">
{links}
        </ul>
      </nav>
    </div>
  </header>
"""


FOOTER = """\
  <footer class="site-footer">
    <div class="container">
      <div class="footer__grid">
        <div class="footer__about">
          <h3>Royal Inland Hospital Auxiliary</h3>
          <p>Supporting healthcare excellence through community service and dedicated volunteerism.</p>
        </div>
        <div>
          <h3>Quick Links</h3>
          <ul class="footer__links">
            <li><a href="about.html">About Us</a></li>
            <li><a href="volunteer.html">Volunteer</a></li>
            <li><a href="thrift.html">Thrift Shop</a></li>
            <li><a href="gift-shop.html">Gift Shop</a></li>
          </ul>
        </div>
        <div class="footer__contact">
          <h3>Contact Information</h3>
          <p><strong>Thrift Shop:</strong> 146 Victoria Street<br>
          <strong>Thrift Phone:</strong> <a href="tel:+12503740487">250-374-0487</a><br>
          <strong>Gift Shop:</strong> 311 Columbia Street<br>
          <strong>Gift Phone:</strong> <a href="tel:+12508525569">250-852-5569</a> extension 20774</p>
        </div>
      </div>
      <div class="footer__bottom">
        <p>&copy; 2025 Royal Inland Hospital Afternoon Auxiliary. All rights reserved.</p>
      </div>
    </div>
  </footer>

  <script src="assets/js/site.js" defer></script>
"""

HEAD_RE = re.compile(r"<!-- page:head -->\n(.*?)<!-- /page:head -->\n", re.S)


def build(page: str) -> None:
    src = (PAGES_DIR / page).read_text()
    m = HEAD_RE.search(src)
    if not m:
        raise SystemExit(f"{page}: missing <!-- page:head --> ... <!-- /page:head --> block")
    head, body = m.group(1).rstrip(), src[m.end():].strip("\n")

    out = f"""<!DOCTYPE html>
<!-- BUILT FILE - do not edit. Source: tools/pages/{page}  Rebuild: python3 tools/build.py -->
<html lang="en">
<head>
{head}

{ASSETS}
</head>
<body>
{header(page)}
{body}

{FOOTER}</body>
</html>
"""
    (ROOT / page).write_text(out)
    print("built", page)


if __name__ == "__main__":
    names = [n if n.endswith(".html") else n + ".html" for n in sys.argv[1:]]
    for p in names or sorted(x.name for x in PAGES_DIR.glob("*.html")):
        build(p)

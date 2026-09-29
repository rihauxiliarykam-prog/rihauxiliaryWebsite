# Updating This Site — Maintainer's Guide

This guide is for whoever updates the site next (person or AI agent). It covers where
everything lives, how to make the most common updates, and how to check your work.

## The one rule

**The root `*.html` files are built output — never edit them directly.** Each one has a
banner comment saying so. Edit the sources, then rebuild:

```bash
python3 tools/build.py          # rebuilds every page (plain Python 3, no installs)
python3 tools/build.py about    # rebuilds one page
```

Commit both the source files and the rebuilt root files. Cloudflare serves the static
files as-is; there is no build step in deployment.

## Where things live

| To change... | Edit... |
|---|---|
| Text, images or sections of a page | `tools/pages/<page>.html` |
| A page's `<title>`, meta description, JSON-LD | the `<!-- page:head -->` block in `tools/pages/<page>.html` |
| Navigation links, footer, phone numbers, copyright year | templates at the top of `tools/build.py` |
| Colors, fonts, spacing, component styles | `assets/css/site.css` (design tokens in `:root` at the top, then one commented section per component) |
| Mobile menu or scroll animations | `assets/js/site.js` |
| Search-engine files | `sitemap.xml`, `robots.txt` (update `lastmod` when pages change) |

## Common tasks

### Update text on a page
Edit the wording in `tools/pages/<page>.html`, rebuild, done. Keep the Auxiliary's own
voice — do not rewrite or trim their content while making layout changes.

### Yearly "Recent Donations" update (Impact page)
This happens every year. In `tools/pages/impact.html`, find the `<!-- Recent Donations -->`
section. Add a new `<h3 class="donation-year">YEAR</h3>` plus a `<div class="donation-grid"
data-reveal-group>` **above** the previous year, and move nothing else. Each card follows
the existing pattern: photos in `.donation-photos` (one or two `<img>`), then department
(`.dept`), name (`<h4>`), and description.

### Add photos
- Resize to ~1200px on the long edge, JPEG quality ~75–80 (`sips -Z 1200 -s format jpeg
  -s formatOptions 80 in.jpg --out out.jpg` on macOS). Target under ~250KB per photo.
- Put them in `assets/images/Updated Photos/JPEG/` with a descriptive lowercase name.
- Always set `alt`, `width`, `height`, and `loading="lazy"` (except the hero image).
- The home hero image is special: it spans the full screen, so it ships two sizes via
  `srcset` (currently `hero-rih-1200.jpg` / `hero-rih-2200.jpg`). If you replace it, make
  the large size at least 2200px wide.
- The hero photo is CC BY-SA 3.0 from Wikimedia Commons; the credit line in the footer
  (in `tools/build.py`) must stay as long as that photo is used.

### Add a page
1. Copy an existing file in `tools/pages/`, update the `<!-- page:head -->` block and content.
2. Add the page to `NAV` in `tools/build.py`.
3. Add it to `sitemap.xml`.
4. Rebuild.

### Animations
Headings animate in when they carry `data-pullup` (plain-text headings only — the script
splits words). Grids animate their children when the container has `data-reveal-group`.
Both are optional attributes; leaving them off just means no animation. Everything is
transform/opacity only, is skipped under `prefers-reduced-motion`, and degrades to plain
visible content if JavaScript doesn't load.

## Checking your work

1. Preview locally: `python3 -m http.server 8765` in the repo root, then open
   `http://127.0.0.1:8765/`.
2. Check phone width (narrow the browser to ~375px): no horizontal scrolling anywhere,
   and the menu button opens the nav.
3. Click every link you touched; confirm images load.
4. If you changed shared templates, confirm the change appears on all seven pages.

## Deployment

The site is hosted on Cloudflare from this repo's `main` branch — merging to `main`
deploys it. `_redirects` sends traffic to the canonical domain `rih-auxiliary.com`.

## Content principles

- This is the official site of a volunteer hospital auxiliary: keep the tone warm and
  plain, keep the theme light, and never remove their content without being asked.
- Contact details (addresses, phone numbers, hours) appear in the footer template and on
  the Contact/Thrift/Gift pages — update every occurrence together.
- Photos of identifiable patients or volunteers need the Auxiliary's confirmation of
  consent before going live.

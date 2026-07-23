# MUQI / emuqi.com — Project Guide & Design System

Version: 3.0  
Status: Single source of truth for project context, design rules, and implementation practices  
Audience: Future AI coding models, frontend implementers, and reviewers  
Reference artifact: `blog/` article pages are the visual benchmark  
Changelog: V3.0 — merged PROJECT.md + README.md into this file; added project context, tech stack, deployment, SEO/GEO strategy; updated header to metallic gradient; Hero overlay reduced; Store/Contact border-radius restored  
Previous: V2.0 — orange VI, navigation geometry fix, About redesign, Application portfolio, Water Bottle images, Solutions three-pillar structure

---

## 0. Project Context

### 0.1 Company

**山东木齐健康科技有限公司 (MUQI Technology / MQ Health Tech)** — solid-state hydrogen materials company.

- CEO: 陈滨 (Martin Chen), Tsinghua MBA, 20yr international trade
- Founded 2011, national-level "专精特新小巨人" enterprise
- Core tech: ICR solid-state hydrogen sustained-release (vs SPE/PEM electrolysis — zero power, 18-24h half-life)
- Product matrix: 吃·喝·洗·护·泡 (eat-drink-wash-care-bath)
- 13 invention patents, 29 enterprise standards, 50+ test reports
- Operations: Jinan, Zibo, Hangzhou (China)
- Group companies: Muqi New Materials, Muyi Health, Bomiao Environmental, Muxi Technology, Muqi Longxin (factory)

### 0.2 Brand positioning

Hydrogen health · AI+manufacturing · Cross-border trade. "MUQI Inside" — brand-agnostic material & solution supplier.

### 0.3 Domain & deployment

| Role | Current | Notes |
|------|---------|-------|
| Primary domain | `emuqi.com` | DNS pointing to Hostinger (147.79.79.250) |
| GitHub repo | `mqtech-martin/emuqi` (SSH) | Source of truth for all code |
| Hostinger | `peru-eagle-941015.hostingersite.com` | Git auto-deploy from GitHub; pending emuqi.com binding |
| GitHub Pages | `mqtech-martin.github.io/emuqi/` | Backup/mirror, also auto-deploys on push |
| Blog/content | **Undecided** — Ghost Pro is one option under consideration; may use alternative platform | Not committed |

### 0.4 Tech stack

| Component | Technology | Purpose |
|-----------|-----------|---------|
| Main site | Static HTML/CSS/JS | Brand showcase, products, applications |
| Styles | `style.css` (shared) + inline `<style>` (blog) | DM Sans + Inter, orange VI |
| Hosting A | Hostinger (PHP/HTML) | Primary — Git auto-deploy |
| Hosting B | GitHub Pages | Mirror/backup |
| Deploy trigger | `git push origin main` | Both Hostinger and GitHub Pages auto-sync |
| Content platform | TBD (Ghost / other) | Blog, newsletter — not yet committed |

### 0.5 Directory structure

```
emuqi/
├── DESIGN.md              ← THIS FILE — single source of truth
├── index.html             # Homepage
├── about-*.html           # About page
├── product-*.html         # Products overview
├── hydrogen-health-application.html  # Applications portfolio
├── solutions-*.html       # Solutions (3 pillars)
├── contact-*.html         # Contact page
├── store.html             # Store placeholder
├── hub.html               # H2 Health Hub
├── blog-list-*.html       # Blog listing
├── hydrogen-*.html (×8)   # Product detail pages
├── blog/*.html (×16)      # Blog article pages
├── style.css              # Shared stylesheet
├── script.js              # Gallery + nav interactions
└── assets/
    └── images/            # ALL images (logos, products, blog, overview)
        ├── application-overview/  # Original Application page images
        ├── water-bottle/          # Water Bottle 11 original images
        └── ... (113+ images total)
```

**Rule**: All website assets (HTML, CSS, JS, images, fonts) must live inside this `emuqi/` directory. No external dependencies except Google Fonts CDN. This ensures the entire site is portable and self-contained.

### 0.6 Progress

**Completed:**
- [x] Full site rebuild from original Zyrosite (18 main pages + 16 blog articles)
- [x] All images downloaded and organized under `assets/images/`
- [x] DM Sans + Inter typography unified across all pages
- [x] Orange VI (#f47b20) replacing old gold (#c89a3c) — 35+ files
- [x] Navigation geometry fixed (73px header, 34px nav, no jitter between pages)
- [x] Metallic header gradient with inset highlight
- [x] Hero overlay reduced for brighter background visibility
- [x] Store nav with orange accent border + border-radius
- [x] Contact nav with deep navy + border-radius + 16px separation
- [x] Dropdown menus with deep navy gradient
- [x] About page redesign (editorial composition, stat band, alternating features)
- [x] Application page redesign (hero bands, gallery thumbnails, CTA summary)
- [x] Water Bottle detail page (11 original images, gallery, specs, feature cards)
- [x] 4 other product detail pages redesigned with gallery layout
- [x] Blog listing page (16 articles, 3-column grid)
- [x] Blog og:image fixes (5 files)
- [x] Footer unified (5-column, orange headings, social icons)
- [x] DESIGN.md V3.0 (this file — merged PROJECT.md + README.md)
- [x] Hostinger Git auto-deploy configured
- [x] GitHub → Hostinger auto-sync verified

**Pending:**
- [ ] Bind `emuqi.com` to Hostinger PHP/HTML site (currently shows old Zyrosite)
- [ ] SSL certificate for `emuqi.com` on Hostinger
- [ ] SEO/GEO optimization (meta tags, JSON-LD, OG, Twitter Cards) — all pages
- [ ] Solutions page content (3 pillars: hydrogen consumer, silver economy, hydrogen agriculture)
- [ ] Content platform decision (Ghost vs alternative)
- [ ] Social media integration strategy
- [ ] 4 remaining blog thumbnail images need original replacements

---

Build a restrained, credible B2B technology website for MUQI Technology, a solid-state hydrogen and functional ceramic materials manufacturer.

The site should feel like a technical editorial publication with a commercial product layer: calm, precise, premium, and evidence-oriented. The blog article pages are the reference standard for typography, hero treatment, spacing, color hierarchy, and footer tone. Root pages must not visually drift from that standard.

Success means:

- Every page uses the same visual language and navigation geometry.
- Page transitions do not cause the navigation to move, resize, or change weight.
- Product and blog images show the real product or the actual article subject whenever an original image exists.
- Navigation supports clear hover states and dropdowns without layout shift.
- Typography has visible hierarchy; product cards are not just an image followed by unstyled body text.
- The site remains readable and usable on desktop and mobile.

## 2. Product Context

MUQI sells and develops functional mineral ceramic materials and solid-state hydrogen applications for B2B customers, OEMs, distributors, and solution partners.

Primary content groups:

- Core materials: hydrogen-generating ceramic balls, MACA antibacterial ceramic balls, MPH+ alkaline/condensate materials.
- Hydrogen health applications: bottles, sachets, ceramic tablets, filter cartridges, foot-bath tablets.
- Solutions: hydrogen health consumer products, silver economy health products, hydrogen agriculture (cultivation and livestock).
- Editorial content: hydrogen health research, product development, materials, medicine, and industry events.

The site is a static HTML/CSS/JS site hosted through GitHub Pages. Keep implementation dependency-light and preserve relative paths.

## 3. Visual Foundations

### 3.1 Identity

Use the identity of an editorial web designer working for a materials science company: technical clarity first, with restrained premium details. Avoid generic SaaS, wellness spa, or decorative medical imagery.

### 3.2 Palette (V2.0 — Orange VI)

The brand accent color is now **orange** (`#f47b20`), matching the MUQI logo. The previous gold (`#c89a3c`) has been fully replaced across all 37 HTML files and `style.css`.

```css
--ink:       #1a1a2e;  /* primary text */
--navy:      #0a1628;  /* footer, dropdown base, deep surfaces, Contact button */
--blue-deep: #1a3a6e;  /* secondary navy, Contact hover */
--blue:      #1d4ed8;  /* links, action emphasis */
--orange:    #f47b20;  /* brand accent — logo dot, footer headings, buttons, metrics, section labels */
--orange-light: #ffad5a; /* orange hover variant for mission/block headings on dark backgrounds */
--paper:     #ffffff;
--surface:   #f5f6f8;
--muted:     #6b7280;
--light-on-dark: #f0ece4;
--dark-muted: #94a3b8;
--line:      #e2e8f0;
```

Four-color VI system:

| Role | Color | Usage |
|------|-------|-------|
| **Blue** | `#0a1628` / `#1a3a6e` / `#1d4ed8` | Structure: header, footer, dropdowns, hero gradient, Contact button |
| **White** | `#ffffff` / `#f5f6f8` | Content surfaces, card backgrounds, body text contrast |
| **Black** | `#1a1a2e` / `#4a4a5a` | Primary text, nav default state, wordmark |
| **Orange** | `#f47b20` | Brand accent: logo dot, footer section headings, CTA buttons, stat numbers, capability markers, section kickers, Store nav border |

Rules:

- Use navy/deep blue for structural surfaces and strong interaction states.
- Use **orange** for brand accents: logo dot, footer column headings, stat numbers, section labels, capability markers, CTA buttons, Store nav accent.
- Do not use purple gradients, neon colors, pastel wellness palettes, gold, or unrelated accent colors.
- Contact must use the same deep navy family as the footer: `#0a1628` default, `#1a3a6e` hover.
- Store is a distinct commerce entry point with an orange bottom-border accent (`box-shadow: inset 0 -2px 0 rgba(244,123,32,.65)`).

### 3.3 Typography

Load the same families everywhere:

```html
<link rel="preconnect" href="https://fonts.googleapis.com">
<link href="https://fonts.googleapis.com/css2?family=DM+Sans:wght@400;500;600;700&family=Inter:wght@400;500;600&display=swap" rel="stylesheet">
```

```css
body { font-family: "Inter", -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif; }
h1, h2, h3, h4, nav, .brand { font-family: "DM Sans", -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif; }
```

Type scale:

- Navigation: 14px, weight 500, line-height 18px (fixed).
- Brand wordmark: 17px, weight 700, with orange dot separator.
- Hero H1: 44px desktop, 30px mobile, weight 600, line-height 1.15.
- Page H1: 40px maximum, weight 600.
- Section H2: 30px, weight 600.
- Product card title: 18px, weight 600, line-height 1.3.
- Product card description: 14px, line-height 1.65, muted color.
- Article body: 16px, line-height 1.85.
- Small labels and metadata: 12px to 14px.

Never change navigation weight on hover. A hover state may change background and color, but the occupied width and font weight must remain stable to prevent jitter. Strong emphasis comes from deep navy fill, contrast, and a subtle shadow, not heavier text.

### 3.4 Hero (V3.0 — Brighter Overlay)

The confirmed hero treatment is:

```css
background:
  linear-gradient(135deg,
    rgba(10,22,40,.25) 0%,
    rgba(26,58,110,.20) 60%,
    rgba(29,78,216,.15) 100%),
  url("assets/images/hero-bg.png") center / cover no-repeat;
padding: 160px 40px 100px;
```

Hero text is white (`#fff`) with text shadows for readability on the brighter background:
- H1: `text-shadow: 0 2px 12px rgba(0,0,0,.5), 0 0 40px rgba(10,22,40,.3)`
- Subtitle: `text-shadow: 0 1px 8px rgba(0,0,0,.4)`

Do not revert to the old heavy overlay (55%/50%/40%) — it darkens the background image too much.

### 3.5 Navigation (V3.0 — Metallic Header + Geometry Fix)

**Header background**: metallic gray gradient, NOT plain white.

```css
background: linear-gradient(180deg, #e8eaed 0%, #d8dadf 40%, #cfd2d7 70%, #c5c8cd 100%);
border-bottom: 1px solid #b8bbc0;
box-shadow: 0 1px 3px rgba(0,0,0,0.06), inset 0 1px 0 rgba(255,255,255,0.65);
```

The `inset 0 1px 0 rgba(255,255,255,0.65)` creates a subtle top highlight that gives a brushed-metal feel.

**Store button**: `border-radius: 8px`, semi-transparent white background, orange bottom accent (`inset 0 -2px 0 rgba(244,123,32,.65)`), deep navy text. Hover: deep navy background.

**Contact button**: `border-radius: 8px`, deep navy (`#0a1628`) background, white text, `margin-left: 16px` from Store. Hover: `#1a3a6e`.

All pages — root, blog list, and blog articles — must use identical navigation geometry. The blog list page must load `style.css` in addition to any inline styles.

Confirmed dimensions (measured via CDP JavaScript):

| Metric | Value | Enforcement |
|--------|-------|-------------|
| Header height | **73px** | `header { height: 73px !important; box-sizing: border-box; }` |
| Header inner div height | **73px** | Same as header |
| Nav element height | **34px** | `header nav { height: 34px; }` |
| Nav link height | **34px** | `header nav > a { height: 34px; line-height: 18px; }` |
| Nav link font | **DM Sans, 14px, weight 500** | `!important` in CSS |
| Nav link padding | **8px 14px** | Fixed |
| Nav gap | **4px** | Fixed |
| Logo image height | **38px** | Fixed |
| Brand wordmark | **17px, weight 700** | Fixed |
| Contact left margin | **16px** from Store | `margin-left: 16px !important` |
| Store min-width | **78px** | `min-width: 78px` |
| Contact min-width | **94px** | `min-width: 94px` |

**Critical rules:**

1. `blog-list-hydrogen-health.html` must `<link rel="stylesheet" href="style.css">`.
2. Header must use `box-sizing: border-box` so the 1px bottom border does not add to the 73px total.
3. Nav links must never change `font-weight` on hover — only background and color.
4. Store uses class `nav-store` with orange bottom accent.
5. Contact uses class `nav-contact` with deep navy background and 16px left margin.
6. `white-space: nowrap` on `H2 Health Hub` and other long labels.

Default link state: `#4a4a5a` on the metallic gray header (`linear-gradient(180deg,#f2f3f5 0%,#e9eaec 100%)`).  
Hover/active state: deep navy `#0a1628` background with white text.  
Contact default: `#0a1628`; Contact hover: `#1a3a6e`.  
Store default: semi-transparent white with orange bottom border; Store hover: deep navy with orange bottom border.

### 3.6 Dropdowns

Products and Applications are dropdown-capable navigation items.

Dropdown rules:

- Open on hover for desktop and on click/tap for mobile.
- Use a deep navy gradient surface, not plain white:
  `linear-gradient(160deg, #0f1d36 0%, #1a3a6e 50%, #1d4ed8 100%)`.
- Radius: 16px; shadow: `0 16px 48px rgba(10,22,40,0.45)` plus inset white edge.
- Minimum width: 260px for Products, 280px for Applications.
- Each item has stable padding (14px 16px), a short descriptor, and a compact visual marker.
- Item hover uses a visible blue translucent highlight (`rgba(29,78,216,0.42)`) and a small horizontal translation at most 4px.
- The dropdown must not push page content or alter header height.
- Keep the trigger width stable when the arrow is present.

Avoid emoji as a permanent brand icon system. Existing temporary markers may remain only until replaced by local product icons or image thumbnails.

### 3.7 Product Cards

Product cards are framed tools/content units, not decorative floating cards inside other cards.

- Use a restrained border and small shadow; radius 8px to 12px.
- Image area: stable aspect ratio, no layout shift.
- Title sits in a clear hierarchy with DM Sans 600 and deep navy text.
- Add a short orange rule above the title when the card has no dedicated body wrapper.
- Description is Inter 14px with muted color and controlled line length.
- Keep card titles aligned across a row.
- Use real product images and product-specific alt text.
- Do not use one generic image for multiple unrelated products.

### 3.8 Application Portfolio Layout (V2.0)

The Applications page now uses a multi-section product portfolio instead of a simple card grid.

Each of the five products (Water Bottle, Alkaline Sachet, Ceramic Tablet, Filter Cartridge, Foot Bath Tablet) occupies a full alternating-width row:

- Left/right alternating layout (`.application-product` and `.application-product-reverse`).
- Each row: main image + thumbnail strip (2–4 additional images) + numbered section + title + description + bullet list + explore link.
- Main image: `aspect-ratio: 1.45; object-fit: contain` (not cover — preserves full product info).
- Thumbnails: grid of 3 columns, same aspect ratio.
- Section numbers: `01 / Drink`, `02 / Water`, `03 / Material`, `04 / Purify`, `05 / Care`.
- Orange bullet markers and orange arrow on explore links.

### 3.9 About Page Layout (V2.0)

The About page now uses an editorial composition instead of plain paragraphs.

Structure (top to bottom):

1. **Company overview image** — full-width `company-brief.png` at the top of the page, with orange section kicker.
2. **Intro section** — two-column grid: heading + description on left, orange-bordered dark gradient note card on right.
3. **Dark stat band** — three columns on `#0a1628` background with orange numbers (25 patents, 15 invention patents, 12 R&D team members). Divided by vertical white rules.
4. **Feature sections** (4 total, alternating left/right):
   - 01 / Company platform — Hydrogen+ strategy, subsidiaries, industry positions.
   - 02 / Research foundation — CAS collaboration, 2017/2019/2021 milestones.
   - 03 / Manufacturing discipline — 8000-ton production, ISO 9000, Jinan/Zibo/Hangzhou offices.
   - 04 / Global reach — international partners and channels.
5. **Capabilities row** — three small cards with colored top borders (blue, orange, light blue).
6. **Mission block** — full-width dark gradient panel with five horizontal rows (Mission, Vision, Values, Philosophy, Slogan). Each row: label (120px) + text (single-line, nowrap on desktop).

Rules:

- Feature images use `object-fit: contain` to avoid cropping information.
- Feature images have a 5px orange left border accent.
- Section kickers are orange, 12px, uppercase, letter-spacing 1.6px.
- Mission rows are laid out as flex column, not grid — five single-row items.

### 3.10 Footer

Footer is the structural anchor:

- Background: `#0a1628`.
- Five columns: Brand, Explore, Products, Applications, Contact.
- Desktop grid: `2fr 1fr 1fr 1fr 1fr`.
- Section headings: 12px, DM Sans 600, **orange** (`#f47b20`), uppercase, letter-spacing 1.5px.
- Links: 14px, `#94a3b8`; hover to `#f0ece4`.
- Bottom divider: low-contrast white line; copyright text in `#475569`.
- Copyright link `emuqi.com` in orange.
- Keep the same column order and spacing on every page.

## 4. Accessibility

- Every content image needs meaningful alt text; decorative logo images may use empty alt text only when adjacent brand text is present.
- Maintain visible keyboard focus styles for links and dropdown triggers.
- Do not rely on color alone for active state; use contrast, background, underline, or a small rule.
- Body text contrast must meet WCAG AA where practical.
- Dropdown content must remain reachable by keyboard and touch.
- Ensure mobile navigation does not overflow horizontally.
- Preserve stable dimensions to prevent content movement during font loading and hover.

## 5. Voice & Tone

The interface voice is concise, technical, and confident. It should sound like a materials supplier with real manufacturing and application experience.

Use:

- Specific product names and application terms.
- Short supporting explanations.
- Evidence-led wording.
- Clear B2B calls to action such as `Contact`, `Explore products`, and `Read more`.

Avoid:

- Empty marketing phrases such as "seamlessly unlock your potential".
- Unsupported medical promises.
- Excessive exclamation marks.
- Generic wellness copy that could belong to any health brand.

## 6. Implementation Practices

### 6.1 Source of truth

- `blog/*.html` is the visual reference for article typography and editorial spacing.
- `style.css` is the shared root-page stylesheet — **all pages must load it**, including `blog-list-hydrogen-health.html`.
- The navigation must be treated as one component even though the site is static HTML.
- Do not create a different inline navigation design for individual pages.
- Nav geometry rules live in `style.css` under `header`, `header nav`, `header nav > a`, `.nav-store`, `.nav-contact`.

### 6.2 Image mapping workflow

For every blog card:

1. Read the article title and first visual/body image.
2. Compare the card image to the article's original `og:image` or cover image.
3. Verify the referenced local file exists.
4. Check extension and case exactly.
5. If the original image cannot be retrieved, mark it clearly as `[IMAGE-SOURCE-UNVERIFIED]` in the implementation notes and do not present a generic gradient image as the final design.

The four files previously created as temporary substitutes are:

- `assets/images/tsingda-expo_2.jpg`
- `assets/images/hydrogen-terminology_2.jpg`
- `assets/images/ceramic-water-media-evolution_2.jpg`
- `assets/images/hydrogen-medicine-report_2.jpg`

These must be replaced with confirmed original article images when available.

### 6.3 Product image sourcing (V2.0)

For product detail pages and application cards:

1. Check `assets/images/` for existing product-specific images (e.g., `water-bottle-1.png`).
2. If insufficient, fetch the original product page from `https://emuqi.com/<product-slug>`.
3. Extract Zyrosite CDN image URLs: look for `assets.zyrosite.com/A0x1OjZW32F81Eg3/` filenames.
4. Download original-resolution images (remove `/cdn-cgi/image/format=auto,w=XXX,h=XXX,fit=crop/` segment).
5. Store in `assets/images/<product-slug>/` subdirectory (e.g., `assets/images/water-bottle/bottle-01.png`).
6. Use `object-fit: contain` (not `cover`) for product images that contain text, labels, or specifications.
7. Never crop product images in a way that removes visible information.

Water Bottle image set: 11 images downloaded from original site, stored in `assets/images/water-bottle/bottle-01.png` through `bottle-11.png`.

### 6.4 Solutions page structure (V2.0)

The Solutions page should present three clearly defined solution pillars:

1. **Hydrogen Health Consumer Products** — hydrogen water, topical products, wellness applications.
2. **Silver Economy Health Products** — healthy aging, aging-in-place, daily wellness, mobility, hydration, non-medical support. Reference: UN Silver Economy Forum, WHO Decade of Healthy Ageing.
3. **Hydrogen Agriculture** — crop cultivation (hydrogen-rich water irrigation, plant stress tolerance, fruit quality), livestock and aquaculture applications. Reference: PubMed studies on HRW in agriculture, FAO integrated systems.

Content rules:

- Use conservative, evidence-oriented language.
- Cite public research where available (PubMed, FAO, WHO, UN DESA).
- Do not make unsupported efficacy claims.
- Frame as "application directions" and "solution capabilities", not proven therapeutic outcomes.

### 6.5 Verification checklist

Before committing:

- Open Home, Products, Applications, Blog list, and one blog article locally.
- **Measure header height**: must be exactly 73px on all pages.
- **Measure nav link dimensions**: must be 34px height, DM Sans 14px, weight 500 on all pages.
- **Click from Blog to Solutions** and confirm no visual shift in navigation.
- Hover every nav item and confirm no horizontal or vertical jitter.
- Open Products and Applications dropdowns.
- Test dropdown links from both root pages and `/blog/` pages.
- Check Contact color against the Footer navy (`#0a1628`).
- Check Store has orange bottom accent.
- Check all footer headings are orange (`#f47b20`), not gold.
- Check desktop and mobile widths.
- Inspect the browser console for missing assets.
- Run a local asset audit for every `src` and `href` path.
- Confirm no temporary placeholder image remains in a final release.

## 7. Anti-Patterns

Do not introduce:

- Different font families between blog and root pages.
- Pages that do not load `style.css`.
- Header heights other than 73px.
- Nav link heights other than 34px.
- Light-blue hero gradients that contradict the blog standard.
- White-only dropdowns with no visual relationship to the footer.
- Hover font-weight changes that cause navigation jitter.
- Empty `href=""` links.
- Generic placeholder images presented as article-specific originals.
- Emoji-heavy navigation or product iconography.
- Unbounded product titles that change card heights.
- New rounded cards nested inside existing cards.
- Purple/cyan "AI dashboard" styling.
- Gold (`#c89a3c`) anywhere — use orange (`#f47b20`) instead.
- Unsupported product, medical, or performance claims.

## 8. Decision-Making

When a future model is unsure:

1. Prefer the existing blog article page over a new visual invention.
2. Prefer shared CSS (`style.css`) and stable geometry over page-specific inline overrides.
3. Prefer a real original image over a semantically approximate stock image.
4. Prefer navy structure and restrained **orange** accents over additional colors.
5. Prefer explicit, auditable fixes over broad rewrites.
6. Preserve user-confirmed behavior unless the user explicitly changes it.
7. When in doubt about navigation jitter, measure with CDP JavaScript, do not guess.

## 9. Workflow

### Before editing

- Read this document.
- Inspect the relevant existing page and its nearest blog reference.
- Search `assets/images/` before downloading or creating any image.
- Check `git status`; preserve unrelated user changes.

### During editing

- Make the smallest coherent change.
- Keep navigation markup and dimensions synchronized across all pages.
- Use stable CSS classes (`nav-store`, `nav-contact`) or a generated shared fragment; do not hand-tune one page only.
- Keep temporary image substitutions explicitly documented.
- Use `object-fit: contain` for any image containing text, specifications, or labels.

### After editing

- Run local server: `python3 -m http.server 8080` from this directory.
- Verify Home, Products, Applications, Blog list, and article pages.
- **Run CDP measurement**: `document.querySelector('header').offsetHeight` must return 73 on every page.
- Capture desktop and mobile screenshots.
- Run asset and console checks.
- Report unresolved image-source issues honestly.
- Commit only after local verification and user review when requested.

## Structure

The current site should be understood as these layers:

1. Global header and navigation: fixed 73px geometry, shared across root and blog pages via `style.css`.
2. Hero: dark blue scientific image treatment, with light editorial typography.
3. Page content: full-width sections with constrained inner containers.
4. About page: editorial composition with overview image, stat band, alternating feature sections, capabilities, and mission block.
5. Application page: alternating product portfolio rows with multi-image thumbnails.
6. Product detail pages: full product image set from original site, specifications, features, OEM/ODM inquiry.
7. Footer: five-column deep navy information architecture with orange headings.

Blog article pages add a layer between hero and footer: a centered white editorial article card with generous padding, metadata, images, callout boxes, FAQ, and CTA.

## Decision Trace

```json
[
  {
    "decision": "Use the confirmed blog article pages as the visual benchmark for the whole site.",
    "reason": "The user explicitly identified the blog area as the current standard for font, spacing, tone, and color.",
    "alternatives": ["Keep root pages on the older style.css system", "Create a new unrelated global theme"],
    "tradeoff": "Some existing root-page styling must be normalized, and older page-specific CSS may need cleanup."
  },
  {
    "decision": "Use DM Sans for display/UI text and Inter for body copy everywhere.",
    "reason": "This matches the blog standard and gives navigation, product titles, and editorial copy distinct but compatible roles.",
    "alternatives": ["Roboto plus Lato", "DM Sans for every text role"],
    "tradeoff": "The site depends on loading two Google font families and needs a sensible system fallback."
  },
  {
    "decision": "Replace gold (#c89a3c) with orange (#f47b20) as the brand accent color.",
    "reason": "The user identified the MUQI logo as orange and requested a unified four-color VI system: blue, white, black, orange.",
    "alternatives": ["Keep gold as accent", "Use a different orange shade"],
    "tradeoff": "All 37 HTML files and style.css required bulk replacement; any future gold references must be treated as errors."
  },
  {
    "decision": "Use #0a1628 as the Contact background and dropdown base.",
    "reason": "The user asked for Contact and emphasized navigation states to relate more strongly to the Footer color.",
    "alternatives": ["Keep #1d4ed8 as Contact blue", "Use the orange accent for all active navigation states"],
    "tradeoff": "Orange becomes a section/metric accent rather than the universal interaction color."
  },
  {
    "decision": "Use deep navy gradient dropdowns with blue/orange interaction highlights.",
    "reason": "A plain white dropdown looked disconnected from the established dark footer and hero system.",
    "alternatives": ["Plain white dropdown", "Solid orange dropdown", "Large image-based mega menu"],
    "tradeoff": "Dark menus require careful contrast and keyboard/focus testing."
  },
  {
    "decision": "Fix header height at 73px and nav height at 34px, enforced via style.css with !important.",
    "reason": "CDP measurement revealed blog-list page was 73px while solutions was 72px due to missing style.css link and inline style differences.",
    "alternatives": ["Use 72px everywhere", "Allow each page to set its own header height"],
    "tradeoff": "The 1px border-box difference must be accounted for; 73px includes the 1px bottom border."
  },
  {
    "decision": "Require blog-list-hydrogen-health.html to load style.css.",
    "reason": "Without the shared stylesheet, the blog list page used different fonts, line-heights, and header geometry than root pages, causing visible jitter on page transitions.",
    "alternatives": ["Duplicate all nav CSS inline in blog-list page", "Move blog-list page to a fully separate template"],
    "tradeoff": "The blog-list page now depends on style.css not conflicting with its existing inline <style> block."
  },
  {
    "decision": "Redesign About page with editorial composition: overview image, stat band, alternating feature sections, mission rows.",
    "reason": "The user requested color blocks, hierarchy, and design sophistication; the original page was plain paragraphs with no visual structure.",
    "alternatives": ["Keep the original paragraph layout", "Use a timeline instead of alternating features"],
    "tradeoff": "The About page is now significantly more complex to maintain; content changes require updating multiple CSS classes."
  },
  {
    "decision": "Redesign Applications page with five alternating product portfolio sections using full image sets.",
    "reason": "The user noted the original site had many more product images with animation and design layering; the simple 5-card grid was too sparse.",
    "alternatives": ["Keep simple card grid", "Use a carousel/gallery widget"],
    "tradeoff": "The page is longer but each product gets dedicated space for main image, thumbnails, description, and feature list."
  },
  {
    "decision": "Download 11 original Water Bottle images from Zyrosite CDN.",
    "reason": "The original product page had rich visual content (product shots, technology diagrams, lifestyle scenes, packaging) that the local 3-image set did not cover.",
    "alternatives": ["Use only the existing 3 images", "Create new product photography"],
    "tradeoff": "The images are large (13MB total); consider optimization for production deployment."
  },
  {
    "decision": "Treat the four current substitute blog images as temporary and unverified.",
    "reason": "The original article thumbnails are not yet confirmed, and generic substitutes should not be mistaken for source material.",
    "alternatives": ["Leave them as final images", "Remove the cards until originals are found"],
    "tradeoff": "The page remains visually complete but still has an explicit image-source debt."
  },
  {
    "decision": "Structure Solutions page around three pillars: hydrogen health consumer, silver economy, hydrogen agriculture.",
    "reason": "The user requested three specific solution directions with publicly sourced background content.",
    "alternatives": ["Keep single-topic agriculture page", "Create separate pages for each pillar"],
    "tradeoff": "The single page must balance three distinct audiences without diluting any one."
  }
]
```

## Final Anti-Slop Check

- Flagged and controlled: gradient hero. It is retained because it is a user-confirmed brand treatment, but it is a photographic dark-blue overlay, not a decorative purple/cyan glow.
- Flagged and controlled: repeated card grid. Cards are limited to real products/articles and use editorial hierarchy, stable imagery, and restrained framing.
- Avoided: emoji as final visual identity. Existing dropdown markers are temporary and should be replaced with consistent icon assets when the navigation is finalized.
- Avoided: hover-induced layout shift. Navigation weights and dimensions are fixed at 73px/34px/DM Sans 14px 500.
- Avoided: generic copy and unsupported claims.
- Avoided: gold accent color anywhere in the system.

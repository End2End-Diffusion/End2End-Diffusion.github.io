# Blog Design System — End2End Diffusion

## Overview

A blog system that merges the warm academic aesthetic of the existing site with Noumena-inspired radical simplicity. Text-first, distraction-free, optimized for long-form technical writing.

**Key principles:**
1. **Text-first** — No thumbnails, no decorative images. Content is the design.
2. **Warm academic** — Site's palette (terracotta, sage, ivory), not Noumena's cooler tones.
3. **Minimal chrome** — No search, no pagination, no share buttons.
4. **Self-contained** — Blog CSS/JS under `blog/static/`, posts with co-located assets.
5. **Progressive enhancement** — `text-wrap`, sidenotes, TOC gracefully degrade.
6. **No build system** — Static HTML/CSS, deployable to GitHub Pages as-is.

---

## 1. File & Directory Structure

```
blog/
├── DESIGN.md                       # This file
├── index.html                      # Blog listing page
├── static/
│   ├── css/
│   │   ├── blog-listing.css        # Listing page styles
│   │   └── post.css                # Blog post template styles
│   └── js/
│       └── blog.js                 # Theme toggle, series filter, TOC scroll
└── posts/
    ├── _template/
    │   └── index.html              # Copy this for new posts
    ├── 0001-post-slug/
    │   ├── index.html              # The post itself
    │   └── assets/                 # Post-specific images/media
    │       ├── figure-1.webp
    │       └── figure-2.webp
    └── 0002-another-post/
        ├── index.html
        └── assets/
```

**Conventions:**
- Each post lives in `blog/posts/<NNNN-slug>/index.html` (numbered + slug)
- Post numbers are zero-padded to 4 digits, sequential, permanent (deleting a post does not renumber others)
- Post assets go in `blog/posts/<slug>/assets/` — use `.webp` format
- Shared blog CSS lives in `blog/static/css/`
- Posts reuse site-wide CSS from `static/css/landing.css` (base variables + dark mode)
- Patterns from `static/css/paper-layout.css` and `static/css/paper-theme.css` are adapted (not imported directly to avoid variable collisions)

**URL structure:**
- Listing: `end2end-diffusion.github.io/blog/`
- Post: `end2end-diffusion.github.io/blog/posts/0001-post-slug/`

---

## 2. Blog Listing Page (`blog/index.html`)

### Layout
- Same container approach as landing page: centered, max-width 768px
- Reuse landing page header (logo + theme toggle) with added "Blog" nav link
- No thumbnails — text-only listing for radical simplicity

### Entry Design

Each entry is a vertical stack:

```
#0001  ·  Mar 2026  ·  [research]
Post Title Here (text-wrap: balance)
One-line description of the post.
```

**Structure per entry:**
- **Number**: `#0001` format, JetBrains Mono, 0.8125rem, muted color
- **Date**: Inter, 0.8125rem, muted, abbreviated month + year
- **Status badge**: Small pill — one of: `research`, `hypothesis`, `result`, `framing`, `note`
- **Title**: Lora, 1.125rem, weight 500, links to post, `text-wrap: balance`
- **Description**: Inter, 0.875rem, secondary color, single line
- Meta items separated by `·` (middle dot) on one line

**Spacing**: 2.25rem vertical gap between entries (`--blog-entry-gap`) — generous Noumena-style breathing room

### Filtering

**Desktop (≥1200px)**: Series sidebar, fixed right, 140px wide
- Monospace 11px labels
- Filters by toggling `display:none` on non-matching `data-series`

**Tablet (768px–1199px)**: Horizontal filter tabs above the list (like landing page filter pattern)

**Mobile (<768px)**: Filters hidden

All filtering is JavaScript toggle, no page reload.

### Visual Style
- Border-bottom separator between entries (1px, `--border-color`)
- On hover: left accent bar appears (4px, matching existing `publication-card::before` pattern from landing.css)
- No background color change on hover — keep it calm
- No pagination: all posts visible (post count stays manageable for research blog)

---

## 3. Blog Post Template (`blog/posts/<slug>/index.html`)

### Page Structure (top to bottom)

```html
<!-- Head: fonts, shared CSS, post.css -->
<!-- Theme init script (same as landing) -->

<body>
  <!-- 1. Top nav bar -->
  <nav class="post-nav">
    End2End Diffusion  /  Blog  /  Post Title
    [theme toggle]
  </nav>

  <!-- 2. Post header -->
  <header class="post-header">
    <div class="post-meta">
      <span class="post-number">#0001</span>
      <span class="post-status post-status--research">research</span>
      <time>March 17, 2026</time>
    </div>
    <h1 class="post-title">Title Here</h1>
    <p class="post-subtitle">Subtitle or one-line description</p>
    <div class="post-author">
      <span>Jaskirat Singh</span>
    </div>
    <div class="post-series">
      Series: <a href="/blog/?series=noumena">Noumena</a>
    </div>
  </header>

  <!-- 3. Content area with TOC + sidenotes -->
  <div class="post-layout">
    <!-- Fixed left TOC (desktop only, ≥1200px) -->
    <nav class="post-toc">
      <h4>Contents</h4>
      <ul>...</ul>
    </nav>

    <!-- Main reading column -->
    <article class="post-content">
      <!-- Sections with h2/h3 headings -->
      <!-- Sidenotes via <span class="sidenote"> -->
      <!-- Figures via <figure> -->
      <!-- Code blocks via <pre><code> -->
      <!-- Blockquotes, lists, etc. -->
    </article>
  </div>

  <!-- 4. Post footer -->
  <footer class="post-footer">
    <!-- Previous/Next post links -->
    <!-- Back to blog listing -->
  </footer>
</body>
```

### Content Column
- **Width: 640px** (optimal reading width, narrower than the 720px project pages)
- Centered with auto margins
- Padding: 1rem on mobile, 2rem on tablet+
- `text-wrap: pretty` on body paragraphs

### Table of Contents (Left)
- Adapt `.paper-toc` pattern from paper-layout.css
- Fixed left, 160px wide, visible at ≥1200px
- Position: `left: calc(50% - 320px - 160px - 40px)`
- Auto-generated from h2/h3 headings via JS (IntersectionObserver)
- Active section highlighting on scroll
- Sans-serif 0.85rem, uppercase "Contents" label

### Sidenotes (Tufte-style, Right)
- Desktop (≥1200px): Absolutely positioned right of content column, 180px wide
- Tablet/mobile (<1200px): Collapse inline as bordered callout blocks
- Triggered by `<aside class="blog-sidenote">` inside `<div class="sidenote-container">`
- Style: Inter, 0.8125rem, muted color, left-border accent

### Breakout Figures

Figures with class `.breakout` extend beyond the 640px column:

```css
.breakout {
    margin-left: -60px;
    margin-right: -60px;
    width: calc(100% + 120px);  /* 760px total */
}
```

On mobile (<768px), breakout collapses to full container width (no negative margins).

Regular figures: full content-width (640px), `<figure>` with `<figcaption>` below.
Caption: Inter, 0.875rem, muted, with "**Figure N.**" bold prefix.

### Code Blocks
- Background: `--paper-light` / dark mode equivalent
- Font: JetBrains Mono, 0.85rem
- Border-radius: 6px
- Padding: 1.5rem
- Horizontal scroll on overflow

### Blockquotes
- Left border: 4px solid `--accent-blue`
- Background: subtle `--paper-light`
- Italic serif text

### Paginator (Post Footer)

Three-part flex bar at bottom of each post:

```css
.post-paginator {
    display: flex;
    justify-content: space-between;
    border-top: 1px solid var(--blog-entry-border);
    padding-top: 2rem;
    margin-top: 4rem;
}
```

- `← Previous` / `Back to top` / `Next →`
- Omit prev on first post, next on latest
- Inter, 0.875rem, weight 500
- On mobile: abbreviate to `←` / `↑` / `→`

---

## 4. Typography

### Font Stack

Same Google Fonts as landing page, plus JetBrains Mono:
```html
<link href="https://fonts.googleapis.com/css2?family=Lora:ital,wght@0,400;0,500;0,600;0,700;1,400;1,500&family=Inter:wght@400;500;600;700&display=swap" rel="stylesheet">
<link href="https://fonts.googleapis.com/css2?family=JetBrains+Mono:wght@400;500&display=swap" rel="stylesheet">
```

### Size & Weight Reference

| Element | Font | Size | Weight | Line-height |
|---------|------|------|--------|-------------|
| **Post title** (h1) | Lora | 1.75rem (28px) | 400 | 1.3 |
| **Post subtitle** | Lora italic | 1.125rem (18px) | 400 | 1.5 |
| **Section heading** (h2) | Lora | 1.375rem (22px) | 500 | 1.3 |
| **Sub-heading** (h3) | Inter | 1.125rem (18px) | 600 | 1.4 |
| **Body text** | Lora | 1.0625rem (17px) | 400 | 1.8 |
| **Meta text** (date, badge) | Inter | 0.8125rem (13px) | 500 | 1.5 |
| **Entry number** (#0001) | JetBrains Mono | 0.8125rem (13px) | 400 | 1 |
| **Series labels** | JetBrains Mono | 0.6875rem (11px) | 400 | 1.5 |
| **Sidenotes** | Inter | 0.8125rem (13px) | 400 | 1.5 |
| **Figure captions** | Inter | 0.875rem (14px) | 400 | 1.5 |
| **TOC links** | Inter | 0.85rem | 400 | 1.5 |
| **Inline code** | JetBrains Mono | 0.9em | 400 | — |
| **Paginator** | Inter | 0.875rem | 500 | 1 |

### Special Typography
- `text-wrap: balance` on all post titles (listing + post page) — prevents orphans
- `text-wrap: pretty` on `.post-body p` — better line-breaking
- `font-variant-numeric: tabular-nums` on post numbers for alignment
- Letter-spacing: -0.01em on h1/h2 for tighter display type
- These are progressive enhancement; older browsers simply ignore them

---

## 5. Color & Theming

### Base Colors (inherited from landing.css)

**Light mode:**
| Role | Variable | Value |
|------|----------|-------|
| Page background | `--paper` | `#FAFAFA` |
| Text primary | `--text-primary` | `#1a1a1a` |
| Text secondary | `--text-secondary` | `#555` |
| Text muted | `--gray` | `#6B7280` |
| Accent | `--accent-blue` | `#2563eb` |
| Border | `--border-color` | `#e5e2dd` |

**Dark mode** (`[data-theme="dark"]`):
| Role | Variable | Value |
|------|----------|-------|
| Page background | `--paper` | `#0a0a0a` |
| Text primary | `--text-primary` | `#e8e6dc` |
| Text secondary | `--text-secondary` | `#9ca3af` |
| Accent | `--accent-blue` | `#60a5fa` |
| Border | `--border-color` | `#444` |

### Status Badge Colors — Warm Palette Mapping

Noumena's cool tones remapped to the site's warm academic palette:

| Status | Noumena | Site equivalent | CSS text var | CSS bg var |
|--------|---------|-----------------|--------------|------------|
| **research** | #4A90A4 (teal) | #6a9bcc (sky) | `--badge-research` | `--badge-research-bg` |
| **result** | #2d7557 (green) | #788c5d (olive) | `--badge-result` | `--badge-result-bg` |
| **hypothesis** | #4a6688 (blue-gray) | #7b7a8e (heather) | `--badge-hypothesis` | `--badge-hypothesis-bg` |
| **framing** | #8f5a35 (brown) | #cc785c (book-cloth) | `--badge-framing` | `--badge-framing-bg` |
| **note** | — (new) | #d4a27f (kraft) | `--badge-note` | `--badge-note-bg` |

### Blog CSS Variables

```css
:root {
    /* Layout */
    --blog-content-width: 640px;
    --blog-toc-width: 160px;
    --blog-sidenote-width: 180px;
    --blog-side-gap: 40px;

    /* Spacing */
    --blog-entry-gap: 2.25rem;
    --blog-heading-margin: 3.5rem;

    /* Surfaces (inherit from landing.css) */
    --blog-bg: var(--paper);
    --blog-entry-border: var(--border-color);
    --blog-entry-hover: var(--card-border-hover);

    /* Text (inherit from landing.css) */
    --blog-text: var(--text-primary);
    --blog-text-secondary: var(--text-secondary);
    --blog-text-muted: var(--gray);
    --blog-link: var(--accent-blue);

    /* Badge colors — light mode */
    --badge-research: #6a9bcc;
    --badge-research-bg: #e8f0f8;
    --badge-result: #788c5d;
    --badge-result-bg: #edf2e8;
    --badge-hypothesis: #7b7a8e;
    --badge-hypothesis-bg: #ededf2;
    --badge-framing: #cc785c;
    --badge-framing-bg: #f5ebe6;
    --badge-note: #d4a27f;
    --badge-note-bg: #f7f0e8;
}

[data-theme="dark"] {
    --badge-research: #7dafd6;
    --badge-research-bg: #1a2a38;
    --badge-result: #96ad7d;
    --badge-result-bg: #1a2518;
    --badge-hypothesis: #9e9db0;
    --badge-hypothesis-bg: #22222e;
    --badge-framing: #d9937d;
    --badge-framing-bg: #2e1f18;
    --badge-note: #dbb89a;
    --badge-note-bg: #2a2018;
}
```

### Badge Rendering

```css
.entry-badge {
    display: inline-block;
    padding: 2px 8px;
    border-radius: 3px;
    font-family: 'Inter', sans-serif;
    font-size: 0.6875rem;
    font-weight: 500;
    letter-spacing: 0.02em;
    text-transform: lowercase;
}

.badge-research   { color: var(--badge-research);   background: var(--badge-research-bg); }
.badge-result     { color: var(--badge-result);     background: var(--badge-result-bg); }
.badge-hypothesis { color: var(--badge-hypothesis); background: var(--badge-hypothesis-bg); }
.badge-framing    { color: var(--badge-framing);    background: var(--badge-framing-bg); }
.badge-note       { color: var(--badge-note);       background: var(--badge-note-bg); }
```

---

## 6. CSS Architecture

### What to Reuse

| Source | What | How |
|--------|------|-----|
| `landing.css` | Color vars, header, theme toggle, dark mode | Import via `<link>` before blog CSS |
| `paper-layout.css` | TOC positioning, sidenote toggle at 1200px | Adapt pattern in blog CSS (don't import — avoids variable collisions) |
| `paper-theme.css` | Callout box, code block patterns | Reference pattern, adapt with blog- prefix |
| `landing.js` | Theme toggle, filter logic | Replicate in `blog.js` |

### New CSS Files

**`blog/static/css/blog-listing.css`** (~150 lines)
- Blog-specific variables (layout, spacing, badges)
- Blog header and list container
- Entry layout (number, badge, date, title, desc)
- Series sidebar (desktop) and filter tabs (tablet)
- Hover effects
- Responsive adjustments

**`blog/static/css/post.css`** (~250 lines)
- Post breadcrumb nav
- Post header (meta, title, subtitle, author, series)
- Content column (640px)
- TOC positioning (fixed left at ≥1200px)
- Sidenote positioning (absolute right at ≥1200px, inline below)
- Breakout figure styling
- Code block and callout box styles
- Post paginator (prev/top/next)
- Dark mode overrides specific to blog

### CSS Loading Order

**Listing page:**
```html
<link rel="stylesheet" href="../static/css/landing.css">
<link rel="stylesheet" href="static/css/blog-listing.css">
```

**Post page:**
```html
<link rel="stylesheet" href="../../../static/css/landing.css">
<link rel="stylesheet" href="../../static/css/post.css">
```

### Naming Convention

- `blog-*` prefix for blog-specific classes
- `entry-*` for listing items
- `post-*` for post page elements
- `badge-*` for status badges
- `pag-*` for paginator
- Avoids collision with `article-*` (landing) and `paper-*` (project pages)

---

## 7. Navigation Integration

### Site Header (all pages)

Add a `<nav class="site-nav">` to the header on all pages:

```html
<header>
    <a href="/index.html" class="logo" style="font-size: 1.5rem;">End2End Diffusion</a>
    <div class="header-right">
        <nav class="site-nav">
            <a href="/index.html">Research</a>
            <a href="/blog/">Blog</a>
        </nav>
        <div class="header-divider"></div>
        <button class="theme-toggle" id="theme-toggle">
            <i class="fas fa-sun"></i>
            <i class="fas fa-moon"></i>
        </button>
    </div>
</header>
```

Site nav styling: Inter 0.875rem, weight 500, `--text-secondary` color, `--text-primary` on hover/active, subtle 2px bottom border on active.

### Blog Listing Page
- Same header as above with "Blog" link active
- Series sidebar or filter tabs for sub-navigation

### Blog Post Page
- Same header plus breadcrumb below:

```html
<nav class="blog-breadcrumb">
    <a href="../../">Blog</a>
    <span class="sep">/</span>
    <span>Post Title</span>
</nav>
```

Breadcrumb: Inter 0.875rem, muted color, max-width matches content column.

### Project Pages
- Add Blog link to their inline nav bars for consistency

---

## 8. Creating New Blog Posts (Template Process)

### Steps to create a new post:

1. **Find next number**: Check `blog/posts/` for highest existing number. Increment by 1, zero-pad to 4 digits.

2. **Create directory**: Copy `blog/posts/_template/` to `blog/posts/NNNN-your-slug/`
   - Slug: lowercase, hyphen-separated, descriptive (e.g., `0003-spatial-structure-matters`)

3. **Edit metadata** in the copied `index.html`:
   - `<title>` tag
   - OG/Twitter meta tags
   - Post number, date, status badge class, series name
   - Title in `<h1 class="post-title">`

4. **Write content** inside `<div class="post-body">`:
   - `<h2 id="section-name">` for sections (appear in TOC)
   - `<figure class="breakout">` for wide images
   - `<div class="sidenote-container">` + `<aside class="blog-sidenote">` for sidenotes
   - `<div class="blog-callout">` for findings

5. **Add images**: Place in `assets/` subdirectory, use `.webp` format

6. **Update listing**: Add new `<article class="blog-entry">` at TOP of `.blog-list` in `blog/index.html`

7. **Update paginator**: In previous latest post, add "Next →" link. In new post, set "← Previous".

8. **New series** (if applicable): Add `<li>` to series sidebar in `blog/index.html`

### Post numbering
- Sequential: `#0001`, `#0002`, `#0003`...
- Numbering is manual (no build system)
- Numbers are permanent — deleting a post does not renumber others
- Display in listing and on post page

### Status lifecycle
Posts can have one of these statuses, reflecting the research process:
- `note` — Quick thought or observation
- `hypothesis` — Proposed idea, not yet validated
- `research` — Active investigation or exploration
- `result` — Concluded findings
- `framing` — Setting context, defining terms, or positioning a question

---

## 9. Responsive Breakpoints

### Desktop (≥1200px)
- Content: 640px centered
- TOC: fixed left, 160px
- Sidenotes: absolute right, 180px
- Series sidebar (listing): fixed right, 140px
- Breakout figures: 760px

### Tablet (768px – 1199px)
- Content: 640px centered (auto padding)
- TOC: hidden
- Sidenotes: inline blocks with left border
- Series sidebar: horizontal filter tabs above list
- Breakout figures: full container width

### Mobile (≤767px)
- Content: 100% width, 1rem padding
- Post title: 1.375rem (22px)
- Body text: 1rem (16px)
- Entry meta: number + date + badge on one line, title below
- Paginator: abbreviated `←` / `↑` / `→`
- All interactive elements: minimum 44px tap target

### Small Mobile (≤479px)
- Padding: 0.75rem
- Entry meta may wrap

---

## 10. Dark / Light Mode

### Integration

Uses the exact same mechanism as the landing page:
1. `data-theme="dark"` attribute on `<html>`
2. `localStorage.getItem('theme')` for persistence
3. Same sun/moon toggle button with Font Awesome icons
4. `blog.js` includes the same toggle logic

### FOUC Prevention

Include in every blog page `<head>` before CSS:

```html
<script>
(function() {
    let theme = localStorage.getItem('theme');
    if (!theme) theme = 'dark';
    document.documentElement.setAttribute('data-theme', theme);
})();
</script>
```

### What Changes Between Modes

| Element | Light | Dark |
|---------|-------|------|
| Page background | #FAFAFA | #0a0a0a |
| Text primary | #1a1a1a | #e8e6dc |
| Text secondary | #555 | #9ca3af |
| Entry border | #e5e2dd | #374151 |
| Entry hover border | #1a1a1a | #fff |
| Badge backgrounds | Warm pastels | Muted dark variants |
| Sidenote border | #94a3b8 | #4a5568 |
| Code block bg | #f5f5f5 | #1e1e1e |
| Callout bg | #f8f9fa | #141414 |
| TOC links | #5e5d59 | #9ca3af |
| TOC active | var(--accent-blue) | #60a5fa |

All color changes use `transition: background-color 0.3s ease, color 0.3s ease` matching the landing page.

---

## 11. JavaScript Requirements

Minimal JS, no frameworks. Single file: `blog/static/js/blog.js`

1. **Theme toggle** — Reuse existing `landing.js` pattern (localStorage + `data-theme`)
2. **TOC active section** — IntersectionObserver on h2/h3 elements
3. **Series filter** — Simple DOM show/hide on listing page
4. **Sidenote positioning** — CSS-only on desktop; JS fallback for precise alignment (future)

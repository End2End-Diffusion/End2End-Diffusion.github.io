# Header Redesign Plan — Blog Posts

Merging k-a.in's editorial elegance with our warm academic blog template.
Goal: minimalist yet striking. Clean, editorial, with optional hero image that enhances without overwhelming.

---

## Design Philosophy

k-a.in treats posts like **chapters in a beautifully typeset book** — centered layout, ultra-light serif headings, thin decorative lines, generous whitespace. We borrow this "chapter opener" feel while keeping our warm academic palette and existing CSS architecture intact.

**Core principle**: The hero image is a *contained illustration*, not a full-bleed backdrop. Text never overlays the image. This keeps things clean and avoids readability issues across themes.

---

## 1. New Header HTML Structure

### With Hero Image

```html
<header class="post-header post-header--hero">
    <div class="post-meta">
        <span class="post-number">#0004</span>
        <span class="dot"></span>
        <span class="post-status post-status--research">research</span>
        <span class="dot"></span>
        <time class="post-date" datetime="2026-03-17">March 17, 2026</time>
    </div>
    <h1 class="post-title">On the Geometry of Latent Token Spaces</h1>
    <p class="post-subtitle">Investigating how pseudo-token embeddings organize spatial structure.</p>
    <div class="post-header-rule"></div>
    <figure class="post-hero-image">
        <img src="assets/hero.webp" alt="Descriptive alt text" loading="eager">
        <figcaption>Optional caption for the hero image.</figcaption>
    </figure>
    <div class="post-author">
        <a href="/">Jaskirat Singh</a>
        <span class="post-header-ornament">&#10022;</span>
    </div>
    <div class="post-series">
        Series: <a href="/blog/?series=noumena">Noumena</a>
    </div>
</header>
```

### Without Hero Image

```html
<header class="post-header">
    <div class="post-meta">
        <span class="post-number">#0004</span>
        <span class="dot"></span>
        <span class="post-status post-status--research">research</span>
        <span class="dot"></span>
        <time class="post-date" datetime="2026-03-17">March 17, 2026</time>
    </div>
    <h1 class="post-title">On the Geometry of Latent Token Spaces</h1>
    <p class="post-subtitle">Investigating how pseudo-token embeddings organize spatial structure.</p>
    <div class="post-header-rule"></div>
    <div class="post-author">
        <a href="/">Jaskirat Singh</a>
        <span class="post-header-ornament">&#10022;</span>
    </div>
    <div class="post-series">
        Series: <a href="/blog/?series=noumena">Noumena</a>
    </div>
</header>
```

### Key Structural Changes

1. **`post-header--hero` modifier class** — added when a hero image is present. Enables wider container and hero-specific spacing.
2. **`post-header-rule`** — thin decorative line (pseudo-element gradient) between subtitle and hero/author. Replaces the old `border-bottom` on the header.
3. **`post-hero-image`** — `<figure>` for the hero, contained inside the header. No full-bleed. Optional `<figcaption>`.
4. **`post-header-ornament`** — Unicode ✦ separator after author name, matching k-a.in's literary feel.

---

## 2. Image / Backdrop Treatment

### Approach: "Chapter Opener Illustration"

Inspired by k-a.in's mHC.html — the hero image is a **simple, contained `<img>`** that sits between the title/subtitle and the author line. No background-image, no overlay, no backdrop-filter.

```css
.post-hero-image {
    margin: var(--post-gap-xl) 0;
    padding: 0;
}

.post-hero-image img {
    width: 100%;
    height: auto;
    display: block;
    border-radius: 4px;
    /* Subtle warm shadow to lift it off the page */
    box-shadow: 0 4px 16px rgba(138, 115, 85, 0.08);
}

[data-theme="dark"] .post-hero-image img {
    box-shadow: 0 4px 16px rgba(0, 0, 0, 0.3);
    /* Very subtle brightness reduction for dark mode */
    filter: brightness(0.92);
}
```

### Why Not Full-Bleed / Overlay?

- Full-bleed heroes require gradient scrims for text readability, which break across light/dark modes
- Overlaid text on images creates accessibility issues
- k-a.in's contained approach is more book-like and editorial
- It's simpler CSS, fewer edge cases, and works reliably across all posts

### When a Hero Image Is Present (wider container)

The `--hero` modifier widens the header from 640px to **min(780px, 100%)** — giving the image more breathing room while keeping text at reading width.

```css
.post-header--hero {
    max-width: 780px;  /* wider than reading column for visual break */
}

/* But text stays at reading width */
.post-header--hero .post-title,
.post-header--hero .post-subtitle,
.post-header--hero .post-meta,
.post-header--hero .post-author,
.post-header--hero .post-series {
    max-width: var(--post-content-width);  /* 640px */
}
```

### Image Fallback / No-Image Posts

Posts without a hero simply omit the `post-header--hero` class and the `<figure>`. The header stays at 640px. The decorative rule and ornament still provide visual interest.

### Bottom Fade (Optional Enhancement)

If we want the hero image to blend into the page background, a gradient pseudo-element on the figure:

```css
.post-hero-image::after {
    content: '';
    position: absolute;
    bottom: 0;
    left: 0;
    right: 0;
    height: 60px;
    background: linear-gradient(to bottom, transparent, var(--post-bg));
    border-radius: 0 0 4px 4px;
    pointer-events: none;
}
```

This is **optional** — use only for images that benefit from a soft edge. Default is no fade.

---

## 3. Typography Refinements for Header Area

### Changes to Existing Styles

Borrow k-a.in's lighter, more spacious feel without changing fonts (keep Lora/Inter/JetBrains Mono for consistency):

```css
/* Refined post title — slightly lighter weight, more letter-spacing */
.post-title {
    font-weight: 500;           /* was 600 — softer, more editorial */
    letter-spacing: -0.01em;    /* was -0.015em — slightly opened */
    margin: 0 0 0.75rem 0;     /* was 0.5rem — more breathing room */
}

/* Refined subtitle */
.post-subtitle {
    font-size: 1.15rem;        /* was 1.2rem — slightly smaller for hierarchy */
    line-height: 1.6;          /* was 1.5 — more generous */
    margin: 0 0 var(--post-gap-md) 0;  /* tighter, rule provides separation */
}

/* Header bottom padding increased */
.post-header {
    padding: var(--post-gap-3xl) var(--post-gap-lg) var(--post-gap-2xl);
    border-bottom: none;       /* was 1px solid — replaced by decorative rule */
    text-align: center;        /* center everything, k-a.in style */
}

/* Meta line centered */
.post-meta {
    justify-content: center;   /* was default (flex-start) */
}

/* Author centered */
.post-author {
    text-align: center;
}

/* Series centered */
.post-series {
    text-align: center;
}
```

### New: Decorative Rule

Thin gradient line replacing the old `border-bottom`:

```css
.post-header-rule {
    width: 60px;
    height: 1px;
    margin: var(--post-gap-lg) auto;
    background: linear-gradient(
        90deg,
        transparent,
        var(--post-border),
        transparent
    );
    opacity: 0.6;
}
```

### New: Ornamental Separator

```css
.post-header-ornament {
    display: inline-block;
    margin-left: 0.75rem;
    font-size: 0.65rem;
    color: var(--post-text-muted);
    opacity: 0.5;
    letter-spacing: 0.5em;
    vertical-align: middle;
}
```

### New: Drop Cap on First Paragraph

k-a.in's signature touch — applied to the `.lead` paragraph:

```css
.post-content .lead::first-letter {
    float: left;
    font-family: var(--post-font-body);  /* Lora */
    font-size: 3.8em;
    font-weight: 400;
    line-height: 0.8;
    margin-right: 0.08em;
    margin-top: 0.05em;
    color: var(--post-accent);
}

[data-theme="dark"] .post-content .lead::first-letter {
    color: var(--post-accent);  /* #60a5fa in dark mode */
}
```

### New: Subtle Entrance Animation

```css
@keyframes fadeInUp {
    from {
        opacity: 0;
        transform: translateY(16px);
    }
    to {
        opacity: 1;
        transform: translateY(0);
    }
}

.post-header .post-meta {
    animation: fadeInUp 0.6s ease-out;
}

.post-header .post-title {
    animation: fadeInUp 0.6s ease-out 0.1s both;
}

.post-header .post-subtitle {
    animation: fadeInUp 0.6s ease-out 0.15s both;
}

.post-hero-image {
    animation: fadeInUp 0.6s ease-out 0.2s both;
}

.post-header .post-author {
    animation: fadeInUp 0.6s ease-out 0.25s both;
}

@media (prefers-reduced-motion: reduce) {
    .post-header * {
        animation: none !important;
    }
}
```

---

## 4. Posts With vs Without Hero Images

| Feature | With Hero (`post-header--hero`) | Without Hero |
|---------|-------------------------------|--------------|
| Header max-width | 780px | 640px (unchanged) |
| Hero image | `<figure class="post-hero-image">` present | Absent |
| Text alignment | Centered | Centered |
| Decorative rule | Between subtitle and image | Between subtitle and author |
| Drop cap | Yes (on `.lead`) | Yes (on `.lead`) |
| Ornament | After author | After author |
| Bottom border | None (rule replaces it) | None (rule replaces it) |
| Entrance animation | Yes (includes image stagger) | Yes (without image step) |

**Both variants look complete and intentional.** The no-hero version is not a "missing image" — it's a clean text-only header with the decorative rule providing the visual interest.

---

## 5. CSS Additions to post.css

### Summary of Changes

All changes go into `blog/static/css/post.css`. No new CSS files needed.

**Modify existing rules** (~15 lines changed):
- `.post-header` — remove `border-bottom`, add `text-align: center`
- `.post-meta` — add `justify-content: center`
- `.post-title` — adjust `font-weight` (500), `letter-spacing`, `margin`
- `.post-subtitle` — adjust `font-size`, `line-height`, `margin`
- `.post-author` — add `text-align: center`
- `.post-series` — add `text-align: center`

**New rules** (~80 lines):
- `.post-header--hero` (wider container modifier)
- `.post-header--hero` child max-width constraints
- `.post-header-rule` (decorative gradient line)
- `.post-header-ornament` (✦ separator)
- `.post-hero-image` + `img` + `figcaption` (hero figure)
- `.post-hero-image::after` (optional bottom fade)
- Dark mode variants for hero image
- `.post-content .lead::first-letter` (drop cap)
- `@keyframes fadeInUp` + animation assignments
- `@media (prefers-reduced-motion)` fallback

**Responsive adjustments** (~15 lines):
- Mobile hero image adjustments
- Mobile drop cap sizing
- Mobile header padding tweaks

**Total addition**: ~110 lines of CSS. Total modification: ~15 lines.

---

## 6. Responsive Behavior

### Desktop (>=1200px)
- Hero header at 780px with TOC and sidenotes visible
- Drop cap at 3.8em
- Full entrance animation sequence

### Tablet (768px-1199px)
- Hero header shrinks to min(780px, 100% - 2rem padding)
- Drop cap at 3.4em
- Animations play

### Mobile (<=767px)
- Header full width with 1rem padding
- Hero image fills container width, rounded corners reduced to 2px
- Drop cap at 3em
- Title font-size drops to 1.65rem (already handled by existing responsive rules)
- Meta line wraps naturally with `flex-wrap: wrap` + `justify-content: center`

### Small Mobile (<=400px)
- Drop cap at 2.8em or disabled entirely
- Hero image shadow removed (saves visual weight)

```css
@media (max-width: 767px) {
    .post-header--hero {
        max-width: 100%;
    }

    .post-hero-image img {
        border-radius: 2px;
    }

    .post-content .lead::first-letter {
        font-size: 3em;
    }
}

@media (max-width: 400px) {
    .post-content .lead::first-letter {
        font-size: 2.8em;
    }

    .post-hero-image img {
        box-shadow: none;
    }
}
```

---

## 7. Dark / Light Mode Considerations

All new elements use existing CSS custom properties — no new color variables needed.

| Element | Light Mode | Dark Mode |
|---------|-----------|-----------|
| Hero image shadow | `rgba(138, 115, 85, 0.08)` | `rgba(0, 0, 0, 0.3)` |
| Hero image filter | none | `brightness(0.92)` |
| Decorative rule | `var(--post-border)` with 0.6 opacity | Same (inherits dark border color) |
| Ornament | `var(--post-text-muted)` at 0.5 opacity | Same (inherits dark muted color) |
| Drop cap | `var(--post-accent)` — `#2563eb` | `var(--post-accent)` — `#60a5fa` |
| Bottom fade gradient | `transparent -> var(--post-bg)` | Same (inherits `#0a0a0a`) |
| Figcaption | `var(--post-text-muted)` | Same (inherits dark muted) |

**No additional `[data-theme="dark"]` rules needed beyond the hero image shadow and filter.**

---

## 8. Blog Listing Page — Thumbnail/Preview Integration

### Recommendation: Keep Text-Only Listing

The current listing page is intentionally text-first ("No thumbnails, no decorative images. Content is the design." — DESIGN.md). Adding thumbnails would undermine this principle.

### Optional Enhancement: Series-Level Visual Cues

Instead of per-post thumbnails, consider subtle series-level styling:

```html
<li data-series="noumena">
    <a href="posts/noumena/" class="post-card">
        <div class="post-meta">
            <span class="post-number">#0004</span>
            <!-- ... existing structure unchanged ... -->
        </div>
        <h2 class="post-title">...</h2>
        <p class="post-subtitle">...</p>
        <span class="post-series-tag">Noumena</span>
    </a>
</li>
```

**No HTML changes needed.** If we later want visual differentiation, options include:
- A thin colored left border per series (e.g., Noumena = sky blue, Scaling Laws = olive)
- A small icon or Unicode glyph next to the series tag
- A subtle background tint on hover, colored by series

These are future enhancements, not part of this header redesign scope.

---

## 9. Implementation Checklist

### HTML Changes
- [ ] In `blog/posts/noumena/index.html`:
  - Add `post-header--hero` class to `<header>` (if adding a hero image)
  - Add `<div class="post-header-rule"></div>` after subtitle
  - Add `<figure class="post-hero-image">` with an image (or skip if no hero)
  - Add `<span class="post-header-ornament">&#10022;</span>` after author link
  - Remove nothing — all existing elements stay

### CSS Changes
- [ ] In `blog/static/css/post.css`:
  - Modify `.post-header`: remove `border-bottom`, add `text-align: center`
  - Modify `.post-meta`: add `justify-content: center`
  - Modify `.post-title`: weight to 500, adjust spacing
  - Modify `.post-subtitle`: adjust size/spacing
  - Modify `.post-author`, `.post-series`: add `text-align: center`
  - Add `.post-header--hero` rules (wider container + child constraints)
  - Add `.post-header-rule` (decorative gradient line)
  - Add `.post-header-ornament` styles
  - Add `.post-hero-image` + img + figcaption styles
  - Add `.post-content .lead::first-letter` (drop cap)
  - Add `@keyframes fadeInUp` + animation assignments
  - Add `@media (prefers-reduced-motion)` fallback
  - Update responsive breakpoints for hero + drop cap
  - Add dark mode hero image adjustments

### Testing
- [ ] Verify post with hero image — all breakpoints
- [ ] Verify post without hero image — all breakpoints
- [ ] Toggle dark/light mode — no flash, correct colors
- [ ] Check reduced motion — animations disabled
- [ ] Verify TOC and sidenotes still work at 1100px+/1200px+
- [ ] Verify breadcrumb nav unchanged
- [ ] Check listing page — no regressions

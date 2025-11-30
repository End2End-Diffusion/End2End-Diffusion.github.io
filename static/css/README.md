# Paper Layout Template

Central template for academic project pages and blog posts.

## Template Location

```
/static/css/paper-layout.css
```

This is the **single source of truth** for shared layout styles. Edit here for global changes.

## Pages Using This Template

- `/irepa/` - iREPA project page
- `/repa-e-t2i/` - REPA-E T2I project page

---

## Quick Start for New Projects

### 1. Add CSS Import

In your HTML `<head>`, add the shared template **before** project-specific styles:

```html
<link rel="stylesheet" href="../static/css/paper-layout.css">
<link rel="stylesheet" href="./static/css/style.css">
<link rel="stylesheet" href="./static/css/custom.css">
```

### 2. Add d-article Override

In your project's `custom.css`:

```css
/* Use paper-layout content width */
d-article {
    display: block !important;
    max-width: var(--layout-content-width, 1037px);
    margin: 0 auto;
    padding: 0 20px;
}

d-article > * {
    width: 100%;
    max-width: 100%;
}
```

### 3. Set White Background

In your project's `style.css`:

```css
body {
    background-color: #ffffff;
}
```

### 4. Remove Width Expansion Patterns

Remove any `width: 150%` or `margin-left: -20%` rules from `.text`, `figure`, etc.

---

## CSS Variables

Customize these in your project CSS if needed:

```css
:root {
    --layout-toc-width: 180px;
    --layout-content-width: 1037px;
    --layout-sidenote-width: 220px;
    --layout-gap: 40px;
    --bg-page: #ffffff;
    --text-primary: #1a1a1a;
    --text-muted: #666;
    --accent: #2563eb;
    --border-light: #e5e5e5;
}
```

---

## Components

### Key Findings (Top Summary)

Numbered box at the top of the article:

```html
<div class="key-findings">
    <h4 class="key-findings-title">Key Findings</h4>
    <div class="key-finding">
        <span class="key-finding-number">1</span>
        <p class="key-finding-text"><strong>Bold claim.</strong> Supporting details.</p>
    </div>
    <div class="key-finding">
        <span class="key-finding-number">2</span>
        <p class="key-finding-text"><strong>Another finding.</strong> More details.</p>
    </div>
</div>
```

### Finding Box (Inline Callout)

Gray box after sections to highlight findings:

```html
<div class="finding-box">
    <ul>
        <li><strong>Finding 1:</strong> Description of the key finding from this section.</li>
    </ul>
</div>
```

### Sidenotes

Notes that appear in right margin on desktop, inline on mobile:

```html
<div class="sidenote-container">
    <p class="text">Main paragraph text goes here...</p>
    <aside class="sidenote">This note appears in the right margin on desktop.</aside>
</div>
```

### Sticky TOC

Table of contents that appears on left, hidden until user scrolls past header:

```html
<nav class="toc-container">
    <h4>Contents</h4>
    <ul>
        <li><a href="#section1">Section 1</a></li>
        <li><a href="#section2">Section 2</a></li>
        <li><a href="#section3">Section 3</a></li>
    </ul>
</nav>
```

**Required JavaScript** for TOC visibility on scroll:

```javascript
document.addEventListener('DOMContentLoaded', function() {
    const tocContainer = document.querySelector('.toc-container');
    const headerWrapper = document.querySelector('.header-wrapper');

    function updateTOC() {
        const scrollPos = window.scrollY;
        const headerBottom = headerWrapper ? headerWrapper.offsetTop + headerWrapper.offsetHeight : 400;

        if (scrollPos > headerBottom - 100) {
            tocContainer.classList.add('visible');
        } else {
            tocContainer.classList.remove('visible');
        }
    }

    window.addEventListener('scroll', updateTOC);
    updateTOC();
});
```

**Required CSS** in your project's `custom.css`:

```css
.toc-container {
    display: none;
}

@media (min-width: 1200px) {
    .toc-container {
        display: block;
        position: fixed;
        left: max(20px, calc(50% - var(--layout-content-width, 1037px)/2 - var(--layout-toc-width, 180px) - var(--layout-gap, 40px)));
        top: 120px;
        width: var(--layout-toc-width, 180px);
        font-size: 0.85em;
        line-height: 1.5;
        opacity: 0;
        transition: opacity 0.3s ease;
    }

    .toc-container.visible {
        opacity: 1;
    }

    .toc-container h4 {
        font-size: 0.75em;
        font-weight: 600;
        text-transform: uppercase;
        letter-spacing: 0.05em;
        color: var(--text-muted, #666);
        margin: 0 0 12px 0;
    }

    .toc-container ul {
        list-style: none;
        padding: 0;
        margin: 0;
    }

    .toc-container li {
        margin-bottom: 8px;
    }

    .toc-container a {
        color: var(--text-muted, #666);
        text-decoration: none;
        transition: color 0.2s ease;
    }

    .toc-container a:hover,
    .toc-container a.active {
        color: var(--accent, #2563eb);
    }
}
```

---

## Design Principles

1. **Consistent widths** - All content (text, figures, tables) uses same width
2. **White background** - Pure #ffffff, not #FAFAFA
3. **Same font for sidenotes** - Uses `font-family: inherit` (serif)
4. **Responsive** - TOC hidden on mobile, sidenotes become inline blocks
5. **No breakout patterns** - No `width: 150%` or negative margins

---

## Example: Reference Projects

- **irepa**: See `/irepa/index.html` and `/irepa/static/css/custom.css`
- **repa-e-t2i**: See `/repa-e-t2i/index.html` and `/repa-e-t2i/static/css/custom.css`

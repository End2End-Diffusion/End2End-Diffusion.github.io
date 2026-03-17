# End2End Diffusion Blog

A text-first research blog built with static HTML/CSS. No build system required.

## Creating a New Blog Post

### 1. Create the post directory

```
blog/posts/<slug>/
blog/posts/<slug>/index.html
blog/posts/<slug>/assets/      # optional, for images/figures
```

The `<slug>` should be a URL-friendly name (lowercase, hyphens, no spaces).

### 2. Copy an existing post

Copy `blog/posts/noumena/index.html` as your starting template.

### 3. Update the post metadata

Edit these sections in your new `index.html`:

**Head:**
- `<title>` — Post title + " — End2End Diffusion Blog"
- `<meta name="description">` — One-line summary
- Open Graph `og:title` and `og:description`

**Navigation breadcrumb:**
```html
<span class="current">Short Title</span>
```

**Post header:**
```html
<div class="post-meta">
    <span class="post-number">#0005</span>           <!-- sequential -->
    <span class="dot"></span>
    <span class="post-status post-status--research">research</span>  <!-- see statuses below -->
    <span class="dot"></span>
    <time class="post-date" datetime="2026-03-17">March 17, 2026</time>
</div>
<h1 class="post-title">Your Post Title</h1>
<p class="post-subtitle">Your subtitle or one-line description.</p>
<div class="post-author"><a href="/">Author Name</a></div>
<div class="post-series">Series: <a href="/blog/?series=your-series">Series Name</a></div>
```

**Post footer:** Update previous/next links.

### 4. Write your content

Use semantic HTML inside `<article class="post-content">`:

- **Headings**: `<h2 id="section-id">` and `<h3 id="sub-id">` (used for TOC)
- **Lead paragraph**: `<p class="lead">` for the first paragraph
- **Sidenotes**: `<aside class="sidenote"><span class="sidenote-number">N</span> Text</aside>`
- **Figures**: `<figure><img src="assets/..."><figcaption><strong>Figure N.</strong> Caption</figcaption></figure>`
- **Wide figures**: Add class `figure-wide` to `<figure>`
- **Code blocks**: `<pre><code><span class="code-label">Language</span>code here</code></pre>`
- **Math**: Use `$...$` for inline and `$$...$$` for display math (KaTeX)
- **Callouts**: `<div class="post-callout post-callout--finding">` or `--note`
- **Blockquotes**: Standard `<blockquote>`

### 5. Update the Table of Contents

Edit the `<nav class="post-toc">` in your post to match your headings:

```html
<li><a href="#section-id">Section Title</a></li>
<li class="toc-h3"><a href="#sub-id">Sub-section</a></li>
```

### 6. Add to the blog listing

Add a new `<li>` entry in `blog/index.html` inside `.post-list`:

```html
<li data-series="your-series">
    <a href="posts/<slug>/" class="post-card">
        <div class="post-meta">
            <span class="post-number">#0005</span>
            <span class="meta-dot">&bull;</span>
            <span class="status-badge status-badge--research">research</span>
            <time class="post-date" datetime="2026-03-17">Mar 17, 2026</time>
        </div>
        <h2 class="post-title">Post Title</h2>
        <p class="post-subtitle">One-line description.</p>
        <span class="post-series-tag">Series Name</span>
    </a>
</li>
```

Posts are listed newest-first. Insert your new entry at the top of the list.

### 7. Add series filter (if new series)

If this is a new series, add a filter pill in `blog/index.html`:

```html
<button class="series-pill" data-series="your-series" role="tab" aria-selected="false">Series Name</button>
```

## Post Statuses

| Status | Class suffix | Use for |
|--------|-------------|---------|
| `research` | `--research` | Active investigation or exploration |
| `hypothesis` | `--hypothesis` | Proposed idea, not yet validated |
| `result` | `--result` | Concluded findings |
| `note` | `--note` | Quick thought or observation |
| `tutorial` | `--tutorial` | How-to or educational content |

## Post Numbering

Sequential: `#0001`, `#0002`, `#0003`, etc. Numbering is manual — check the latest post number before creating a new one.

## CSS Architecture

| File | Purpose |
|------|---------|
| `/static/css/landing.css` | Site-wide theme variables, header styles |
| `/static/css/paper-theme.css` | Academic page components |
| `/blog/static/css/blog-listing.css` | Blog listing page layout |
| `/blog/static/css/post.css` | Blog post page layout and typography |

Posts load `paper-theme.css` + `post.css`. The listing page loads `landing.css` + `blog-listing.css`.

## Dark/Light Mode

Theme is controlled via `data-theme` attribute on `<html>` and persisted in `localStorage`. The theme init script in `<head>` prevents flash of wrong theme on load. Both blog pages include a theme toggle button.

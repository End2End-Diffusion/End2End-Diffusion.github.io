---
name: scholar-check
description: >
  Check and fix Google Scholar indexing compatibility across all project pages and blog posts.
  Audits citation_ meta tags, JSON-LD, RSS feed, sitemap.xml, robots.txt, canonical URLs,
  OG/Twitter tags — and updates any missing or outdated entries.
  Triggers on "/scholar-check", "check scholar indexing", "scholar compatibility".
---

# Google Scholar Compatibility Check

Audit all project pages and blog posts for Google Scholar indexing readiness, then fix any gaps.

## Key Context

- Site: https://end2end-diffusion.github.io (GitHub Pages, static HTML, no build system)
- Search Console: verified via `google084a818ded7c7eef.html` (NEVER delete this file)
- Full docs: `docs/google-indexing.md`
- Search Console link: https://search.google.com/search-console?resource_id=https%3A%2F%2Fend2end-diffusion.github.io%2F

## Pages to Check

Discover all pages dynamically:
1. **Project pages**: Glob for `*/index.html` at repo root (exclude `blog/`, `static/`, `node_modules/`, `docs/`)
2. **Blog posts**: Glob for `blog/posts/*/index.html`
3. **Blog listing**: `blog/index.html`
4. **Landing page**: `index.html`

## Required Meta Tags Reference

### Project Pages (Scholarly Content)

Every project page MUST have these in `<head>`. Without ALL THREE core tags, Scholar ignores the page entirely.

```html
<!-- === CORE (all 3 required or Scholar ignores the page) === -->
<meta name="citation_title" content="Paper Title Here">
<meta name="citation_author" content="Last, First">  <!-- ONE tag per author -->
<meta name="citation_publication_date" content="YYYY/MM/DD">

<!-- === STRONGLY RECOMMENDED (citation_pdf_url is essentially required) === -->
<meta name="citation_pdf_url" content="https://arxiv.org/pdf/XXXX.XXXXX">
<meta name="citation_arxiv_id" content="XXXX.XXXXX">
<meta name="citation_abstract" content="Paper abstract text...">
<meta name="citation_online_date" content="YYYY/MM/DD">
<meta name="citation_conference_title" content="ICCV 2025">  <!-- or citation_journal_title -->
<meta name="citation_language" content="en">
<meta name="citation_fulltext_html_url" content="https://end2end-diffusion.github.io/page-url/">

<!-- === DISCOVERY & SEO === -->
<link rel="canonical" href="https://end2end-diffusion.github.io/page-url/">
<link rel="alternate" type="application/rss+xml" title="End2End Diffusion Blog" href="https://end2end-diffusion.github.io/blog/rss.xml">
<meta name="robots" content="index, follow">

<!-- === OPEN GRAPH (complete set) === -->
<meta property="og:type" content="article">
<meta property="og:title" content="Paper Title">
<meta property="og:description" content="Paper description">
<meta property="og:url" content="https://end2end-diffusion.github.io/page-url/">
<meta property="og:image" content="https://end2end-diffusion.github.io/page-url/assets/thumbnail.webp">

<!-- === TWITTER === -->
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:title" content="Paper Title">
<meta name="twitter:description" content="Paper description">
<meta name="twitter:image" content="https://end2end-diffusion.github.io/page-url/assets/thumbnail.webp">

<!-- === JSON-LD STRUCTURED DATA === -->
<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "ScholarlyArticle",
  "headline": "Paper Title",
  "description": "Paper abstract",
  "author": [
    {"@type": "Person", "name": "First Last"}
  ],
  "datePublished": "YYYY-MM-DD",
  "publisher": {
    "@type": "Organization",
    "name": "End2End Diffusion",
    "url": "https://end2end-diffusion.github.io"
  },
  "url": "https://end2end-diffusion.github.io/page-url/",
  "sameAs": "https://arxiv.org/abs/XXXX.XXXXX",
  "isAccessibleForFree": true,
  "inLanguage": "en"
}
</script>
```

### Blog Posts

```html
<!-- === SCHOLAR (yes, research blog posts should have these) === -->
<meta name="citation_title" content="Post Title">
<meta name="citation_author" content="Singh, Jaskirat">
<meta name="citation_publication_date" content="YYYY/MM/DD">
<meta name="citation_online_date" content="YYYY/MM/DD">
<meta name="citation_abstract" content="Post description">
<meta name="citation_language" content="en">

<!-- === DISCOVERY (same as project pages) === -->
<link rel="canonical" href="https://end2end-diffusion.github.io/blog/posts/slug/">
<link rel="alternate" type="application/rss+xml" title="End2End Diffusion Blog" href="https://end2end-diffusion.github.io/blog/rss.xml">
<meta name="robots" content="index, follow">

<!-- === OG + TWITTER (same pattern as project pages) === -->

<!-- === JSON-LD === -->
<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "BlogPosting",
  "headline": "Post Title",
  "description": "Post description",
  "author": {"@type": "Person", "name": "Jaskirat Singh", "url": "https://1jsingh.github.io/"},
  "datePublished": "YYYY-MM-DD",
  "publisher": {"@type": "Organization", "name": "End2End Diffusion", "url": "https://end2end-diffusion.github.io"},
  "url": "https://end2end-diffusion.github.io/blog/posts/slug/",
  "mainEntityOfPage": "https://end2end-diffusion.github.io/blog/posts/slug/",
  "isAccessibleForFree": true,
  "inLanguage": "en",
  "isPartOf": {"@type": "Blog", "name": "End2End Diffusion Blog", "url": "https://end2end-diffusion.github.io/blog/"}
}
</script>
```

## Site-Wide Files to Maintain

### RSS Feed (`blog/rss.xml`)
- Must contain an `<item>` for EVERY blog post in `blog/posts/*/index.html`
- Each item needs: `<title>`, `<link>`, `<guid>`, `<description>`, `<dc:creator>`, `<pubDate>`, `<category>`
- `<lastBuildDate>` must match the most recent post date
- Format reference:
```xml
<item>
  <title>Post Title</title>
  <link>https://end2end-diffusion.github.io/blog/posts/slug/</link>
  <guid isPermaLink="true">https://end2end-diffusion.github.io/blog/posts/slug/</guid>
  <description>Post description.</description>
  <dc:creator>Jaskirat Singh</dc:creator>
  <pubDate>Fri, 20 Mar 2026 00:00:00 GMT</pubDate>
  <category>research</category>
  <category>SeriesName</category>
</item>
```

### Sitemap (`sitemap.xml`)
- Must contain a `<url>` entry for EVERY project page AND blog post
- Format:
```xml
<url>
  <loc>https://end2end-diffusion.github.io/page-url/</loc>
  <lastmod>YYYY-MM-DD</lastmod>
  <changefreq>monthly</changefreq>
  <priority>0.9</priority>  <!-- 0.9 for papers, 0.8 for blog posts, 0.7 for listing, 1.0 for landing -->
</url>
```

### Robots (`robots.txt`)
- Must exist, must allow Googlebot, must reference sitemap
- Don't modify unless adding specific blocks

### Landing Page (`index.html`)
- Must have JSON-LD `ResearchOrganization`, RSS link, canonical URL
- Must have Google verification meta tag: `<meta name="google-site-verification" content="f_YIC9wnnL29x38hrKkSeni26z6FnQ1CCyLnZOD6kJs">`

### Verification File
- `google084a818ded7c7eef.html` — NEVER delete, required for Search Console

## Per-Page Audit Checklist

For each **project page**, verify:

| Check | Required | Tag |
|-------|----------|-----|
| citation_title | MUST | `<meta name="citation_title">` |
| citation_author | MUST | `<meta name="citation_author">` (one per author) |
| citation_date | MUST | `<meta name="citation_publication_date">` |
| citation_pdf_url | CRITICAL | `<meta name="citation_pdf_url">` |
| citation_arxiv_id | If applicable | `<meta name="citation_arxiv_id">` |
| citation_abstract | Recommended | `<meta name="citation_abstract">` |
| citation_language | Recommended | `<meta name="citation_language" content="en">` |
| JSON-LD | Recommended | `ScholarlyArticle` or `BlogPosting` |
| canonical | Recommended | `<link rel="canonical">` |
| RSS link | Recommended | `<link rel="alternate" type="application/rss+xml">` |
| robots | Recommended | `<meta name="robots" content="index, follow">` |
| og:type | Recommended | `<meta property="og:type" content="article">` |
| og:title | Recommended | `<meta property="og:title">` |
| og:description | Recommended | `<meta property="og:description">` |
| og:url | Recommended | `<meta property="og:url">` |
| og:image | Recommended | `<meta property="og:image">` |
| twitter:card | Recommended | `<meta name="twitter:card">` |
| In sitemap | MUST | Entry in `/sitemap.xml` |
| In RSS | Blog only | Entry in `/blog/rss.xml` |

## Fix Procedure

When gaps are found:
1. **Report** a summary table of all pages with pass/fail per check
2. **Fix** missing meta tags by reading content from the page (title from `<title>`, authors from author sections, dates from visible dates, abstracts from description)
3. **Update** `sitemap.xml` with any new/missing pages
4. **Update** `blog/rss.xml` with any new/missing blog posts
5. **DO NOT** change CSS, layout, or visible content — only meta tags and site files
6. **Remind** user to request indexing in Search Console for any new pages

## Output Format

```
## Scholar Indexing Audit Results

### Page: /repa-e/
| Check | Status | Notes |
|-------|--------|-------|
| citation_title | PASS | "REPA-E: Unlocking VAE..." |
| citation_author | PASS | 6 authors |
| citation_pdf_url | PASS | arXiv PDF linked |
| JSON-LD | PASS | ScholarlyArticle |
| sitemap | PASS | Entry exists |
| ... | ... | ... |

### Site-Wide
| Check | Status | Notes |
|-------|--------|-------|
| RSS feed | PASS | 1 item, matches blog posts |
| sitemap.xml | FAIL | Missing /new-page/ |
| robots.txt | PASS | Allows all, references sitemap |
| verification file | PASS | google084a818ded7c7eef.html exists |

### Fixes Applied
- Added citation_title to /new-project/index.html
- Added <url> for /new-project/ to sitemap.xml
- Added <item> for new blog post to blog/rss.xml

### Manual Steps Required
- Request indexing in Search Console for: /new-project/, /blog/posts/new-post/
```

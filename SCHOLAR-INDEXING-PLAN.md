# Google Scholar Indexing Implementation Plan

This plan covers everything needed to get **end2end-diffusion.github.io** papers indexed by Google Scholar.

---

## 1. Citation Meta Tags Per Page

Google Scholar requires **Highwire Press** `citation_*` meta tags in the `<head>` of each page. These are the primary signal Scholar uses to identify and index academic papers. All tags must use the `name`/`content` attribute pattern.

### 1a. REPA-E (`/repa-e/index.html`)

```html
<!-- Google Scholar meta tags -->
<meta name="citation_title" content="REPA-E: Unlocking VAE for End-to-End Tuning with Latent Diffusion Transformers">
<meta name="citation_author" content="Leng, Xingjian">
<meta name="citation_author" content="Singh, Jaskirat">
<meta name="citation_author" content="Hou, Yunzhong">
<meta name="citation_author" content="Xing, Zhenchang">
<meta name="citation_author" content="Xie, Saining">
<meta name="citation_author" content="Zheng, Liang">
<meta name="citation_publication_date" content="2025/04/14">
<meta name="citation_online_date" content="2025/04/14">
<meta name="citation_arxiv_id" content="2504.10483">
<meta name="citation_abstract" content="We show that latent diffusion models and their VAE tokenizer can be effectively trained end-to-end using a simple representation-alignment (REPA) loss. REPA-E achieves state-of-the-art FID scores of 1.12 and 1.69 with and without classifier-free guidance on ImageNet 256x256.">
<meta name="citation_language" content="en">
<meta name="citation_pdf_url" content="https://arxiv.org/pdf/2504.10483">
```

### 1b. REPA-E for T2I (`/repa-e-t2i/index.html`)

```html
<!-- Google Scholar meta tags -->
<meta name="citation_title" content="Family of End-to-End Tuned VAEs for Supercharging T2I Diffusion Transformers">
<meta name="citation_author" content="Leng, Xingjian">
<meta name="citation_author" content="Singh, Jaskirat">
<meta name="citation_author" content="Murdock, Ryan">
<meta name="citation_author" content="Smith, Ethan">
<meta name="citation_author" content="Li, Rebecca">
<meta name="citation_author" content="Hou, Yunzhong">
<meta name="citation_author" content="Xing, Zhenchang">
<meta name="citation_author" content="Xie, Saining">
<meta name="citation_author" content="Zheng, Liang">
<meta name="citation_publication_date" content="2025">
<meta name="citation_online_date" content="2025">
<meta name="citation_technical_report_institution" content="End2End Diffusion">
<meta name="citation_abstract" content="We present REPA-E for T2I, a family of End-to-End Tuned VAEs for supercharging text-to-image generation training. End-to-end VAEs show superior performance over their original counterparts across all benchmarks without need for any additional representation alignment losses.">
<meta name="citation_language" content="en">
```

> **Note:** REPA-E-T2I does not have its own arXiv paper or PDF. It references the REPA-E arXiv ID. Since it's a separate work, do NOT add `citation_arxiv_id` or `citation_pdf_url` here unless/until it gets its own arXiv submission. Scholar can still index the page without a PDF.

### 1c. iREPA (`/irepa/index.html`)

```html
<!-- Google Scholar meta tags -->
<meta name="citation_title" content="What Matters for Representation Alignment: Global Information or Spatial Structure?">
<meta name="citation_author" content="Singh, Jaskirat">
<meta name="citation_author" content="Leng, Xingjian">
<meta name="citation_author" content="Wu, Zongze">
<meta name="citation_author" content="Zheng, Liang">
<meta name="citation_author" content="Zhang, Richard">
<meta name="citation_author" content="Shechtman, Eli">
<meta name="citation_author" content="Xie, Saining">
<meta name="citation_publication_date" content="2025/12/14">
<meta name="citation_online_date" content="2025/12/14">
<meta name="citation_arxiv_id" content="2512.10794">
<meta name="citation_abstract" content="We investigate what drives representation alignment in diffusion transformers: global semantic information or spatial structure? Through large-scale analysis, we show spatial structure matters more than ImageNet accuracy.">
<meta name="citation_language" content="en">
<meta name="citation_pdf_url" content="https://arxiv.org/pdf/2512.10794">
```

### 1d. Blog Post: Noumena (`/blog/posts/noumena/index.html`)

```html
<!-- Google Scholar meta tags -->
<meta name="citation_title" content="On the Geometry of Latent Token Spaces in End-to-End VAEs">
<meta name="citation_author" content="Singh, Jaskirat">
<meta name="citation_publication_date" content="2026/03/17">
<meta name="citation_online_date" content="2026/03/17">
<meta name="citation_abstract" content="Investigating how pseudo-token embeddings organize spatial structure during joint encoder-decoder training.">
<meta name="citation_language" content="en">
```

### 1e. Main Landing Page (`/index.html`)

The landing page is NOT a paper -- it is a group/lab homepage. **Do NOT add `citation_*` tags** to this page. Only add structured data (see Section 5).

---

## 2. Reusable Template Snippet for Blog Posts

For future blog posts that should be Scholar-indexed, use this template in the `<head>`:

```html
<!-- === Google Scholar Citation Tags === -->
<!-- REQUIRED: These tags are what Scholar uses to identify and index papers -->
<meta name="citation_title" content="TITLE_HERE">
<meta name="citation_author" content="LastName, FirstName">
<!-- Repeat citation_author for each author -->
<meta name="citation_publication_date" content="YYYY/MM/DD">
<meta name="citation_online_date" content="YYYY/MM/DD">

<!-- RECOMMENDED: Include when available -->
<meta name="citation_arxiv_id" content="XXXX.XXXXX">
<meta name="citation_pdf_url" content="https://arxiv.org/pdf/XXXX.XXXXX">
<meta name="citation_abstract" content="Abstract text here.">
<meta name="citation_language" content="en">

<!-- OPTIONAL: For conference/journal papers -->
<!-- <meta name="citation_conference_title" content="Conference Name"> -->
<!-- <meta name="citation_journal_title" content="Journal Name"> -->
<!-- <meta name="citation_volume" content="X"> -->
<!-- <meta name="citation_issue" content="X"> -->
<!-- <meta name="citation_firstpage" content="X"> -->
<!-- <meta name="citation_lastpage" content="X"> -->
<!-- <meta name="citation_doi" content="10.XXXX/XXXXX"> -->
```

### Key Rules for the Template

1. **Author format**: Always `LastName, FirstName` -- Scholar parses this format reliably.
2. **Date format**: Always `YYYY/MM/DD` or `YYYY` -- these are the only formats Scholar recognizes.
3. **One `citation_author` per author** -- never comma-separate multiple authors in one tag.
4. **`citation_title` must match** the visible `<title>` or `<h1>` on the page. Scholar cross-checks these.
5. **`citation_pdf_url`** must point to an accessible PDF. If no PDF exists, omit this tag entirely.

---

## 3. robots.txt

Create `/robots.txt` at the site root:

```
User-agent: *
Allow: /

User-agent: Googlebot
Allow: /

# Google Scholar bot
User-agent: Google-Scholar
Allow: /

Sitemap: https://end2end-diffusion.github.io/sitemap.xml
```

This is intentionally permissive. The site is a public academic project page -- there is no reason to block any crawler.

---

## 4. sitemap.xml

Create `/sitemap.xml` at the site root:

```xml
<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
  <!-- Main landing page -->
  <url>
    <loc>https://end2end-diffusion.github.io/</loc>
    <lastmod>2025-10-01</lastmod>
    <changefreq>monthly</changefreq>
    <priority>1.0</priority>
  </url>

  <!-- REPA-E paper page -->
  <url>
    <loc>https://end2end-diffusion.github.io/repa-e/</loc>
    <lastmod>2025-04-14</lastmod>
    <changefreq>monthly</changefreq>
    <priority>0.9</priority>
  </url>

  <!-- REPA-E for T2I paper page -->
  <url>
    <loc>https://end2end-diffusion.github.io/repa-e-t2i/</loc>
    <lastmod>2025-06-01</lastmod>
    <changefreq>monthly</changefreq>
    <priority>0.9</priority>
  </url>

  <!-- iREPA paper page -->
  <url>
    <loc>https://end2end-diffusion.github.io/irepa/</loc>
    <lastmod>2025-12-14</lastmod>
    <changefreq>monthly</changefreq>
    <priority>0.9</priority>
  </url>

  <!-- Blog listing -->
  <url>
    <loc>https://end2end-diffusion.github.io/blog/</loc>
    <lastmod>2026-03-17</lastmod>
    <changefreq>weekly</changefreq>
    <priority>0.7</priority>
  </url>

  <!-- Blog post: Noumena -->
  <url>
    <loc>https://end2end-diffusion.github.io/blog/posts/noumena/</loc>
    <lastmod>2026-03-17</lastmod>
    <changefreq>monthly</changefreq>
    <priority>0.8</priority>
  </url>
</urlset>
```

Update `<lastmod>` dates whenever a page is meaningfully updated. Add new `<url>` entries for each new blog post or paper page.

---

## 5. JSON-LD Structured Data

Add JSON-LD `<script type="application/ld+json">` blocks in the `<head>` of each page. This helps Google (regular search and Scholar) understand the content type.

### 5a. Paper Pages (REPA-E, REPA-E-T2I, iREPA)

Template (fill in per-paper values):

```html
<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "ScholarlyArticle",
  "headline": "PAPER_TITLE",
  "name": "PAPER_TITLE",
  "description": "ABSTRACT",
  "author": [
    {"@type": "Person", "name": "Xingjian Leng", "affiliation": {"@type": "Organization", "name": "ANU"}},
    {"@type": "Person", "name": "Jaskirat Singh", "affiliation": {"@type": "Organization", "name": "ANU"}}
  ],
  "datePublished": "2025-04-14",
  "dateModified": "2025-04-14",
  "publisher": {
    "@type": "Organization",
    "name": "End2End Diffusion",
    "url": "https://end2end-diffusion.github.io"
  },
  "url": "https://end2end-diffusion.github.io/repa-e/",
  "mainEntityOfPage": "https://end2end-diffusion.github.io/repa-e/",
  "isAccessibleForFree": true,
  "inLanguage": "en"
}
</script>
```

**For REPA-E and iREPA**, also add inside the JSON-LD:

```json
"sameAs": "https://arxiv.org/abs/ARXIV_ID",
"identifier": {
  "@type": "PropertyValue",
  "propertyID": "arXiv",
  "value": "ARXIV_ID"
}
```

### 5b. Blog Posts

```html
<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "BlogPosting",
  "headline": "On the Geometry of Latent Token Spaces in End-to-End VAEs",
  "description": "Investigating how pseudo-token embeddings organize spatial structure during joint encoder-decoder training.",
  "author": {
    "@type": "Person",
    "name": "Jaskirat Singh",
    "url": "https://1jsingh.github.io/"
  },
  "datePublished": "2026-03-17",
  "publisher": {
    "@type": "Organization",
    "name": "End2End Diffusion",
    "url": "https://end2end-diffusion.github.io"
  },
  "url": "https://end2end-diffusion.github.io/blog/posts/noumena/",
  "mainEntityOfPage": "https://end2end-diffusion.github.io/blog/posts/noumena/",
  "isAccessibleForFree": true,
  "inLanguage": "en",
  "isPartOf": {
    "@type": "Blog",
    "name": "End2End Diffusion Blog",
    "url": "https://end2end-diffusion.github.io/blog/"
  }
}
</script>
```

### 5c. Main Landing Page

```html
<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "ResearchOrganization",
  "name": "End2End Diffusion",
  "url": "https://end2end-diffusion.github.io",
  "description": "Advancing Visual Representation and Generation Through End-to-End Training",
  "member": [
    {"@type": "Person", "name": "Jaskirat Singh", "url": "https://1jsingh.github.io/"},
    {"@type": "Person", "name": "Xingjian Leng"}
  ]
}
</script>
```

---

## 6. PDF Linking Strategy

### Current State
No paper PDFs are hosted on the site. The only PDFs are icon assets.

### Recommendation

**Option A (Recommended): Link to arXiv PDFs**

For REPA-E and iREPA, which have arXiv submissions, use `citation_pdf_url` pointing to the arXiv PDF:
- REPA-E: `https://arxiv.org/pdf/2504.10483`
- iREPA: `https://arxiv.org/pdf/2512.10794`

Scholar already indexes arXiv papers directly. The `citation_pdf_url` on the project page tells Scholar that this page corresponds to that paper, helping it associate the project page as an additional version.

**Option B (Optional Enhancement): Host PDFs Locally**

If desired, host copies of the PDFs at predictable paths like `/repa-e/paper.pdf` and `/irepa/paper.pdf`, then use those as `citation_pdf_url`. This gives Scholar a direct link and makes the page more self-contained. However, this adds maintenance burden (keeping PDFs in sync with arXiv versions).

**For REPA-E-T2I**: No arXiv paper exists. Do NOT add a `citation_pdf_url`. Scholar can still index the page based on the HTML content and meta tags alone.

**For Blog Posts**: Blog posts are typically not PDFs. Omit `citation_pdf_url` unless you specifically create a PDF version.

---

## 7. Google Search Console Submission Steps

### 7a. Verify Site Ownership

1. Go to [Google Search Console](https://search.google.com/search-console)
2. Click "Add Property"
3. Enter `https://end2end-diffusion.github.io`
4. Choose verification method:
   - **Recommended for GitHub Pages**: HTML file upload -- download the verification file and add it to the repo root
   - Alternative: Add a `<meta name="google-site-verification" content="TOKEN">` tag to `/index.html`
5. Click "Verify"

### 7b. Submit Sitemap

1. In Search Console, go to "Sitemaps" in the left sidebar
2. Enter `sitemap.xml` in the "Add a new sitemap" field
3. Click "Submit"
4. Verify status shows "Success"

### 7c. Request Indexing for Key Pages

1. In Search Console, use the "URL Inspection" tool
2. Enter each paper page URL:
   - `https://end2end-diffusion.github.io/repa-e/`
   - `https://end2end-diffusion.github.io/repa-e-t2i/`
   - `https://end2end-diffusion.github.io/irepa/`
   - `https://end2end-diffusion.github.io/blog/posts/noumena/`
3. Click "Request Indexing" for each URL
4. This puts the page in a priority crawl queue

### 7d. Google Scholar Inclusion Request

Google Scholar has a separate inclusion process:

1. Go to [Google Scholar Inclusion](https://scholar.google.com/intl/en/scholar/inclusion.html)
2. Read the technical guidelines
3. Submit the site via the form at the bottom of the page
4. Use URL: `https://end2end-diffusion.github.io`
5. Describe the site as: "Academic research project pages for published papers on end-to-end diffusion model training"

**Important**: Scholar inclusion review can take **4-8 weeks**. There is no way to expedite this. The citation_ meta tags must be in place BEFORE submitting.

---

## 8. How to Verify Indexing Worked

### 8a. Google Scholar Verification

1. **Search by title**: Go to Google Scholar and search for the exact paper title in quotes:
   - `"REPA-E: Unlocking VAE for End-to-End Tuning with Latent Diffusion Transformers"`
   - `"What Matters for Representation Alignment: Global Information or Spatial Structure?"`
2. **Check for project page version**: The Scholar result should show multiple versions, including the end2end-diffusion.github.io URL
3. **Search by author**: Search `author:"Singh" author:"Leng"` and check if the papers appear
4. **Check Scholar profiles**: If authors have Google Scholar profiles, the papers should appear there

### 8b. Google Search Console Verification

1. Use "URL Inspection" tool to check each URL
2. Look for:
   - "URL is on Google" status
   - "Page indexing" section showing "Indexed"
   - "Enhancements" section showing structured data is detected
3. Check "Coverage" report for any crawl errors

### 8c. Rich Results Test

1. Go to [Rich Results Test](https://search.google.com/test/rich-results)
2. Enter each paper page URL
3. Verify that the `ScholarlyArticle` structured data is detected and valid

### 8d. Timeline

- **Google Search indexing**: 1-2 weeks after sitemap submission
- **Google Scholar indexing**: 4-8 weeks after inclusion request (can be longer)
- **Scholar profile updates**: A few days after Scholar indexes the paper

---

## 9. Ongoing Checklist for New Pages/Posts

When adding a new paper page or blog post:

- [ ] **Add `citation_*` meta tags** in `<head>` using the template from Section 2
  - `citation_title` (required)
  - `citation_author` for each author (required, format: `LastName, FirstName`)
  - `citation_publication_date` (required, format: `YYYY/MM/DD`)
  - `citation_arxiv_id` (if available)
  - `citation_pdf_url` (if PDF exists)
  - `citation_abstract` (recommended)
- [ ] **Add JSON-LD structured data** using the template from Section 5
  - Use `ScholarlyArticle` for paper pages
  - Use `BlogPosting` for blog posts
- [ ] **Update `/sitemap.xml`** with the new URL and correct `<lastmod>` date
- [ ] **Verify `<title>` matches `citation_title`** -- Scholar cross-checks these
- [ ] **Ensure OG tags are complete** -- `og:title`, `og:description`, `og:url`, `og:type`
- [ ] **Request indexing** in Google Search Console (URL Inspection > Request Indexing)
- [ ] **Test with Rich Results Test** to validate structured data
- [ ] **Check Scholar after 4-8 weeks** using title search

### Common Mistakes to Avoid

1. **Mismatched title**: `citation_title` and `<title>` / `<h1>` must be consistent
2. **Wrong date format**: Must be `YYYY/MM/DD`, not `YYYY-MM-DD` or other formats
3. **Missing author tags**: Each author needs their own `<meta name="citation_author">` tag
4. **Broken PDF links**: If `citation_pdf_url` returns a 404, Scholar may skip the page entirely
5. **JavaScript-rendered content**: Scholar has limited JS execution. All `citation_*` tags must be in the static HTML `<head>`, not injected by JavaScript
6. **Noindex directives**: Never add `<meta name="robots" content="noindex">` to paper pages

---

## Implementation Priority

1. **High priority**: Add `citation_*` meta tags to all 3 paper pages + blog post (this is the single most important change)
2. **High priority**: Create `robots.txt` and `sitemap.xml`
3. **Medium priority**: Add JSON-LD structured data
4. **Medium priority**: Set up Google Search Console and submit sitemap
5. **After deployment**: Submit to Google Scholar inclusion
6. **Ongoing**: Follow checklist for new content

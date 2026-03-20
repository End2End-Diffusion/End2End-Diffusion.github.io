# Google Scholar & Search Console Indexing

## Setup (Done)

- **Search Console verified** via HTML file (`google084a818ded7c7eef.html`) + meta tag in `index.html`
- **Sitemap** at `/sitemap.xml` — submitted to Search Console
- **RSS feed** at `/blog/rss.xml`
- **robots.txt** at `/robots.txt` — allows all crawlers, references sitemap
- **`citation_*` meta tags** on all project pages (repa-e, repa-e-t2i, irepa) and blog posts
- **JSON-LD structured data** on all pages (ScholarlyArticle / BlogPosting / ResearchOrganization)
- **Canonical URLs** and `robots: index, follow` on all pages

## When Adding a New Project Page

1. Add `citation_*` meta tags in `<head>`:
   ```html
   <meta name="citation_title" content="Paper Title">
   <meta name="citation_author" content="Last, First">  <!-- one per author -->
   <meta name="citation_publication_date" content="YYYY/MM/DD">
   <meta name="citation_pdf_url" content="https://arxiv.org/pdf/XXXX.XXXXX">
   <meta name="citation_arxiv_id" content="XXXX.XXXXX">
   <meta name="citation_abstract" content="...">
   <meta name="citation_language" content="en">
   ```

2. Add JSON-LD `ScholarlyArticle` structured data

3. Add canonical URL, RSS link, robots meta:
   ```html
   <link rel="canonical" href="https://end2end-diffusion.github.io/your-page/">
   <link rel="alternate" type="application/rss+xml" title="End2End Diffusion Blog" href="https://end2end-diffusion.github.io/blog/rss.xml">
   <meta name="robots" content="index, follow">
   ```

4. Complete OG/Twitter tags (og:type=article, og:title, og:description, og:url, og:image)

5. Add `<url>` entry to `/sitemap.xml`

6. **Request indexing** in Search Console: URL Inspection → paste URL → Request Indexing

## When Adding a New Blog Post

1. Add `citation_*` tags (title, author, date, abstract)
2. Add JSON-LD `BlogPosting` structured data
3. Add canonical URL, RSS link, robots meta
4. Add OG/Twitter tags
5. Add `<item>` to `/blog/rss.xml`
6. Add `<url>` to `/sitemap.xml`
7. Add entry to `/blog/index.html` post list
8. Request indexing in Search Console

## Search Console Access

- **URL**: https://search.google.com/search-console?resource_id=https%3A%2F%2Fend2end-diffusion.github.io%2F
- **Sitemaps**: Submit `sitemap.xml` (if "Couldn't fetch", wait a few hours and retry — or submit the full URL `https://end2end-diffusion.github.io/sitemap.xml`)
- **URL Inspection**: Paste any page URL → Request Indexing to add to priority crawl queue

## Verification

- Check indexing status: search `site:end2end-diffusion.github.io` on Google
- Check Scholar: search `site:end2end-diffusion.github.io` on Google Scholar
- Search Console Coverage report shows indexed vs excluded pages
- Individual URL status via URL Inspection tool

## Key Notes

- **repa-e-t2i** has no arXiv/PDF — Scholar may take longer to index. Consider creating a PDF version.
- Google crawls within days of requesting indexing. Scholar indexing takes weeks.
- The HTML verification file (`google084a818ded7c7eef.html`) must stay in the repo — don't delete it.
- Run `/scholar-check` skill periodically to audit all pages.

## Timeline

- 2026-03-20: Search Console verified, sitemap submitted, indexing requested for all pages

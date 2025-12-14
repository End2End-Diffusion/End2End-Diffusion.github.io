# Landing Page Improvement Todos

Track incremental improvements to the End2End-Diffusion landing page.

## Constraints Reminder
- **ONLY modify:** index.html, static/css/landing.css, static/js/landing.js
- **NEVER touch:** irepa/, repa-e/, repa-e-t2i/, or any other project directories
- **Style:** Professional research aesthetic, blue accent (#2563eb), no flashy effects

---

## High Priority

### Accessibility
- [x] Add proper semantic HTML5 landmarks (nav, main, section, article, footer) - Completed 2025-12-14
- [ ] Add aria-labels to interactive elements (theme toggle, filter buttons)
- [ ] Add skip-to-content link for keyboard users
- [ ] Improve image alt text descriptions for screen readers
- [ ] Add focus-visible styles for keyboard navigation

### Performance
- [ ] Add loading="lazy" to images below the fold
- [ ] Add fetchpriority="high" to hero/above-fold images
- [ ] Preload critical fonts

### Visual Polish
- [ ] Add subtle hover states to article cards (slight lift/shadow)
- [ ] Improve filter tab active state indicator (bottom border or background)
- [ ] Refine spacing consistency across sections
- [ ] Add subtle transition to featured banner cards on hover

---

## Medium Priority

### UX Improvements
- [ ] Add keyboard navigation support for filter tabs (arrow keys)
- [ ] Ensure all interactive elements have visible focus states
- [ ] Improve mobile touch targets (min 44px)
- [ ] Add smooth scroll behavior for any anchor links

### Content Enhancement
- [x] Add footer section with copyright, contact link, and year - Completed 2025-12-14 (added as part of semantic HTML task)
- [ ] Consider adding institution logos/affiliations
- [ ] Improve the mission statement typography hierarchy

### Code Quality
- [ ] Consolidate duplicate CSS rules in landing.css
- [ ] Add CSS comments for section organization
- [ ] Clean up any unused CSS variables or rules
- [ ] Improve JS code organization with descriptive comments

---

## Low Priority

- [ ] Add subtle loading state for filter transitions
- [ ] Consider adding a "scroll to top" indicator
- [ ] Add print stylesheet for academic users
- [ ] Test and fix any Safari-specific CSS issues
- [ ] Add prefers-reduced-motion media query support

---

## Ideas for Future
<!-- Add new ideas here as you discover them - there are NO LIMITS -->
<!-- Keep iterating and improving the landing page indefinitely -->
- [ ] Add structured data (JSON-LD) for research organization SEO
- [ ] Consider adding a brief stats/metrics section
- [ ] Explore subtle CSS grid improvements for article layout
- [ ] Add subtle parallax or scroll-based effects (keep professional)
- [ ] Improve contact section design
- [ ] Better visual hierarchy in featured banners section
- [ ] Add subtle background patterns or textures
- [ ] Improve typography scales and rhythm

---

## Completed
<!-- Move completed items here with date -->

### 2025-12-14
- [x] Add proper semantic HTML5 landmarks (nav, main, section, article, footer)
  - Wrapped header logo in `<nav>` element with aria-label
  - Changed mission statement `<div>` to `<section>` with aria-labelledby
  - Added aria-label to featured banners section
  - Added role="tablist" to filters for proper ARIA semantics
  - Wrapped research section heading in `<section>`
  - Changed contact block from `<div>` to `<section>`
  - Added `<footer>` element with copyright notice
- [x] Add footer section with copyright, contact link, and year (completed as part of above)


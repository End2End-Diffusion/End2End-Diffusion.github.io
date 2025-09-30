# Project Page Layout

```
┌─────────────────────────────────────────────────────────┐
│                        HEADER                            │
│  What matters for Representation Alignment:             │
│  Global Information or Spatial Structure?               │
│                                                          │
│  [arXiv] [PDF] [Code]                                   │
│                                                          │
│  (Optional: Flux-generated hero image - hidden by default)│
└─────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────┐
│                       AUTHORS                            │
│  Jaskirat Singh¹'² · Xingjian Leng² · Zongze Wu¹       │
│  Liang Zheng² · Richard Zhang¹ · Eli Shechtman¹       │
│  Saining Xie³                                           │
│                                                          │
│  ¹Adobe Research  ²ANU  ³NYU                           │
└─────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────┐
│                      ABSTRACT                            │
│  Representation alignment (REPA) guides generative...   │
│  [3 paragraph summary of your work]                     │
└─────────────────────────────────────────────────────────┘

╔═════════════════════════════════════════════════════════╗
║               ⭐ FIGURE 1: TEASER ⭐                     ║
║                                                          ║
║  [Your teaser-v2.png from paper - MAIN HIGHLIGHT]      ║
║                                                          ║
║  Caption: We investigate what drives representation      ║
║  alignment... Spatial structure, not global information ║
║  determines generation performance. SSM shows 3x higher  ║
║  correlation (|r| = 0.852) vs linear probing (|r| = 0.26)║
╚═════════════════════════════════════════════════════════╝

─────────────────────────────────────────────────────────

┌─────────────────────────────────────────────────────────┐
│                   KEY TAKEAWAYS                          │
│  ┌──────────────────────────────────────────────────┐  │
│  │ ① Higher Validation Accuracy ≠ Better Generation │  │
│  │   PE-Spatial-B (53.1%) beats PE-Core-G (82.8%)  │  │
│  └──────────────────────────────────────────────────┘  │
│  ┌──────────────────────────────────────────────────┐  │
│  │ ② Spatial Structure Drives Performance           │  │
│  │   SSM: |r| > 0.852 vs LP: |r| = 0.26           │  │
│  └──────────────────────────────────────────────────┘  │
│  ┌──────────────────────────────────────────────────┐  │
│  │ ③ Accentuating Spatial Features Improves         │  │
│  │   iREPA (<4 lines) improves convergence         │  │
│  └──────────────────────────────────────────────────┘  │
└─────────────────────────────────────────────────────────┘

─────────────────────────────────────────────────────────

┌─────────────────────────────────────────────────────────┐
│        MOTIVATION: GLOBAL INFORMATION MATTERS LESS       │
│                                                          │
│  • Recent vision encoders show surprising patterns      │
│  • SAM2 outperforms encoders with higher accuracy      │
│  • Adding global information can hurt generation        │
│                                                          │
│  Figure 2: Controlled experiments                       │
│  [controlled_experiments.png]                           │
└─────────────────────────────────────────────────────────┘

─────────────────────────────────────────────────────────

┌─────────────────────────────────────────────────────────┐
│      SPATIAL STRUCTURE METRIC PROVIDES BETTER SIGNAL     │
│                                                          │
│  • Spatial structure metrics defined                    │
│  • Large-scale analysis across 27 encoders             │
│  • |r| > 0.852 correlation with FID                    │
│                                                          │
│  Figure 3: Spatial structure correlation                │
│  [spatial_metrics_comparison-sit-b-2.png]              │
└─────────────────────────────────────────────────────────┘

─────────────────────────────────────────────────────────

┌─────────────────────────────────────────────────────────┐
│        iREPA: ACCENTUATING SPATIAL INFORMATION          │
│                                                          │
│  1. Spatial Normalization Layer                         │
│  2. Convolution Projection (replaces MLP)              │
│                                                          │
│  • <4 lines of code                                     │
│  • Works across encoders & model sizes                  │
└─────────────────────────────────────────────────────────┘

─────────────────────────────────────────────────────────

┌─────────────────────────────────────────────────────────┐
│      RESULTS: CONSISTENT IMPROVEMENTS ACROSS SETTINGS    │
│                                                          │
│  • Faster convergence vs baseline REPA                  │
│  • Works with all tested encoders                       │
│  • Consistent across SiT-B/L/XL                        │
│                                                          │
│  Figure 4: Convergence results                          │
│  [convergence_fid_v2.png]                              │
└─────────────────────────────────────────────────────────┘

─────────────────────────────────────────────────────────

┌─────────────────────────────────────────────────────────┐
│                      CONCLUSION                          │
│  Spatial structure, not global information, drives      │
│  representation alignment effectiveness.                │
└─────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────┐
│                       BIBTEX                             │
│  @article{singh2025irepa, ...}                          │
└─────────────────────────────────────────────────────────┘
```

## Key Visual Hierarchy

1. **Most Prominent**: Figure 1 (Teaser) - Your main finding visualization
2. **Second**: Key Takeaways (3 boxes with gradient backgrounds)
3. **Supporting**: Additional figures in each section

## Color Scheme

- Primary gradient: Deep blue (#667eea) → Purple (#764ba2)
- Background highlights: Light gray (#f8f9fa)
- Text: Dark gray (#333) for headings, medium gray (#666) for body
- Accents: Scholarly blue for links

## Spacing

- Large space around teaser figure (emphasized)
- Standard spacing between sections
- Compact spacing within takeaways (to keep them visually grouped)

## Interactive Elements

- All figures zoomable (click to enlarge)
- Smooth scrolling
- Hover effects on takeaway boxes
- Button hover states

---

**Current Status**:
- ✅ Teaser figure in prime position (Figure 1)
- ✅ 3 Key Takeaways styled and prominent
- ✅ All supporting figures included
- ⏳ Hero image placeholder (optional, generate with Flux)
- ⏳ Links need updating (arXiv, PDF, Code)
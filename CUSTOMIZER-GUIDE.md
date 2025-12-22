# Niche Site Customizer - Quick Guide

## What It Does
Asks you 6 questions and creates a customized copy of your 11ty template, ready for content.

## How to Use

### Method 1: Double-click (Windows)
Just double-click `CUSTOMIZE-SITE.bat`

### Method 2: Command line
```bash
python customize-niche.py
```

## The 6 Questions

1. **Niche**: "Camping Gear", "Power Tools", "Kitchen Appliances"
2. **Site Name**: "Camp Smart", "Tool Pro Reviews"
3. **Site Type**: 
   - Product Reviews (multiple products)
   - Single Product Review
   - Product Comparison
   - Deal/Coupon Site
   - Authority/Info Site
4. **Color**: Auto-suggested based on niche, or choose your own
5. **Target Audience**: Who are you helping?
6. **Folder Name**: What to call the new site folder

## What Gets Customized

✅ Site name and branding
✅ Hero section content
✅ Categories section titles
✅ Primary color throughout site
✅ Navigation and footer
✅ README with your details

## Example Session

```
Niche: Camping Gear
Site Name: Camp Smart
Type: Product Reviews
Color: Nature Green (#22c55e)
Audience: Families planning camping trips
Folder: camping-gear-site
```

Creates: `camping-gear-site/` ready to fill with ZimmWriter content!

## After Customization

```bash
cd camping-gear-site
npm run serve
```

Then add your ZimmWriter posts to `src/pages/posts/`

## Color Suggestions by Niche

- Power Tools/Home: Orange (#f97316)
- Camping/Outdoor: Green (#22c55e)
- Tech/Gadgets: Blue (#3b82f6)
- Kitchen/Cooking: Red (#ef4444)
- Pets: Purple (#a855f7)
- Finance: Dark Blue (#1e40af)
- Fitness: Red (#ef4444)
- Beauty: Pink (#ec4899)
- Travel: Sky Blue (#0ea5e9)

## Workflow

1. Run customizer → Create niche site
2. ZimmWriter → Generate posts
3. Copy posts to `src/pages/posts/`
4. Preview locally
5. Deploy to Vercel

**Time per site: 5 minutes setup + content**

#!/usr/bin/env python3
"""
Niche Site Customizer
Asks questions and auto-configures the 11ty affiliate template for a specific niche
"""

import json
import shutil
import os
import re
from pathlib import Path

# Color schemes by niche
NICHE_COLORS = {
    "power tools": {"primary": "#f97316", "name": "Energy Orange"},
    "home improvement": {"primary": "#f97316", "name": "Energy Orange"},
    "camping": {"primary": "#22c55e", "name": "Nature Green"},
    "outdoor": {"primary": "#16a34a", "name": "Forest Green"},
    "hiking": {"primary": "#22c55e", "name": "Nature Green"},
    "tech": {"primary": "#3b82f6", "name": "Tech Blue"},
    "gadgets": {"primary": "#3b82f6", "name": "Tech Blue"},
    "electronics": {"primary": "#1e40af", "name": "Deep Blue"},
    "kitchen": {"primary": "#ef4444", "name": "Warm Red"},
    "cooking": {"primary": "#f97316", "name": "Spice Orange"},
    "home": {"primary": "#f59e0b", "name": "Warm Amber"},
    "pets": {"primary": "#a855f7", "name": "Playful Purple"},
    "pet supplies": {"primary": "#8b5cf6", "name": "Pet Purple"},
    "finance": {"primary": "#1e40af", "name": "Trust Blue"},
    "business": {"primary": "#0f172a", "name": "Professional Dark"},
    "fitness": {"primary": "#ef4444", "name": "Energy Red"},
    "health": {"primary": "#22c55e", "name": "Health Green"},
    "beauty": {"primary": "#ec4899", "name": "Beauty Pink"},
    "fashion": {"primary": "#8b5cf6", "name": "Style Purple"},
    "automotive": {"primary": "#f97316", "name": "Speed Orange"},
    "travel": {"primary": "#0ea5e9", "name": "Sky Blue"},
}

def get_niche_color(niche):
    """Suggest color based on niche"""
    niche_lower = niche.lower()
    for key, value in NICHE_COLORS.items():
        if key in niche_lower:
            return value
    return {"primary": "#22c55e", "name": "Default Green"}

def ask_question(question, default=""):
    """Ask user a question with optional default"""
    if default:
        response = input(f"{question} [{default}]: ").strip()
        return response if response else default
    return input(f"{question}: ").strip()

def choose_from_list(question, options):
    """Present options and get user choice"""
    print(f"\n{question}")
    for i, option in enumerate(options, 1):
        print(f"  {i}. {option}")
    while True:
        choice = input("Choose (1-{}): ".format(len(options))).strip()
        if choice.isdigit() and 1 <= int(choice) <= len(options):
            return options[int(choice) - 1]
        print("Invalid choice, try again.")

def main():
    print("=" * 60)
    print("🚀 AFFILIATE SITE NICHE CUSTOMIZER")
    print("=" * 60)
    print("\nThis will create a customized copy of your template.\n")
    
    # Get template path
    template_dir = Path(__file__).parent / "my-site"
    if not template_dir.exists():
        print(f"❌ Error: Template not found at {template_dir}")
        return
    
    # Question 1: Niche
    print("\n📌 STEP 1: NICHE")
    niche = ask_question("What's your niche? (e.g., 'Camping Gear', 'Power Tools')")
    
    # Question 2: Site Name
    print("\n📌 STEP 2: BRANDING")
    site_name = ask_question(f"Site name/brand?", f"{niche} Pro")
    
    # Question 3: Site Type
    print("\n📌 STEP 3: SITE TYPE")
    site_type = choose_from_list(
        "What type of affiliate site?",
        [
            "Product Reviews (multiple products)",
            "Single Product Review Site",
            "Product Comparison Site",
            "Deal/Coupon Site",
            "Authority/Info Site"
        ]
    )
    
    # Question 4: Color
    print("\n📌 STEP 4: DESIGN")
    suggested_color = get_niche_color(niche)
    print(f"Suggested color for '{niche}': {suggested_color['name']} ({suggested_color['primary']})")
    use_suggested = ask_question("Use this color? (y/n)", "y").lower()
    
    if use_suggested == 'y':
        primary_color = suggested_color['primary']
    else:
        primary_color = ask_question("Enter hex color (e.g., #3b82f6)", suggested_color['primary'])
    
    # Question 5: Target audience
    print("\n📌 STEP 5: AUDIENCE")
    audience = ask_question("Who's your target audience?", "People looking for honest reviews")
    
    # Question 6: Folder name
    print("\n📌 STEP 6: PROJECT NAME")
    folder_name = ask_question(
        "Folder name for new site?",
        niche.lower().replace(" ", "-") + "-site"
    )
    
    # Summary
    print("\n" + "=" * 60)
    print("📋 SUMMARY")
    print("=" * 60)
    print(f"Niche: {niche}")
    print(f"Site Name: {site_name}")
    print(f"Type: {site_type}")
    print(f"Color: {primary_color}")
    print(f"Audience: {audience}")
    print(f"Folder: {folder_name}")
    print("=" * 60)
    
    proceed = ask_question("\nCreate this site? (y/n)", "y").lower()
    if proceed != 'y':
        print("Cancelled.")
        return
    
    # Create new site
    print("\n🔧 Creating customized site...")
    
    new_site_dir = template_dir.parent / folder_name
    if new_site_dir.exists():
        print(f"⚠️  Folder '{folder_name}' already exists!")
        overwrite = ask_question("Overwrite? (y/n)", "n").lower()
        if overwrite != 'y':
            print("Cancelled.")
            return
        shutil.rmtree(new_site_dir)
    
    # Copy template
    shutil.copytree(template_dir, new_site_dir)
    print(f"✅ Copied template to {folder_name}/")
    
    # Update siteContent.json
    content_file = new_site_dir / "src" / "data" / "siteContent.json"
    with open(content_file, 'r', encoding='utf-8') as f:
        site_content = json.load(f)
    
    # Customize content based on niche
    site_content['hero']['title'] = f"{niche} made easy"
    site_content['hero']['subtitle'] = f"Discover the best {niche.lower()} with confidence. {audience}."
    
    site_content['header']['logo_text'] = site_name.upper()
    
    # Customize categories based on site type
    if "Single Product" in site_type:
        site_content['categories']['title'] = f"WHY CHOOSE {niche.upper()}"
        site_content['categories']['subtitle'] = "Key benefits at a glance"
    elif "Comparison" in site_type:
        site_content['categories']['title'] = "COMPARE TOP PRODUCTS"
        site_content['categories']['subtitle'] = f"Find the perfect {niche.lower()} for your needs"
    else:
        site_content['categories']['title'] = f"TOP {niche.upper()} PICKS"
        site_content['categories']['subtitle'] = "Curated selections you can trust"
    
    site_content['reviews']['subtitle'] = f"Your trusted {niche.lower()} resource"
    site_content['testimonials']['subtitle'] = f"Real feedback from {niche.lower()} enthusiasts"
    
    # Save updated content
    with open(content_file, 'w', encoding='utf-8') as f:
        json.dump(site_content, f, indent=2)
    print(f"✅ Updated siteContent.json")
    
    # Update CSS colors
    global_css = new_site_dir / "src" / "assets" / "css" / "global.css"
    with open(global_css, 'r', encoding='utf-8') as f:
        css_content = f.read()
    
    # Replace primary color
    css_content = re.sub(
        r'--primary-color:\s*#[0-9a-fA-F]{6};',
        f'--primary-color: {primary_color};',
        css_content
    )
    
    with open(global_css, 'w', encoding='utf-8') as f:
        f.write(css_content)
    print(f"✅ Updated colors to {primary_color}")
    
    # Create README
    readme_content = f"""# {site_name}

**Niche:** {niche}
**Type:** {site_type}
**Primary Color:** {primary_color}
**Target Audience:** {audience}

## Quick Start

```bash
cd {folder_name}
npm run serve
```

Opens at http://localhost:8080

## Adding Content

Drop markdown files into `src/pages/posts/` and they'll auto-build.

## Deploy to Vercel

```bash
vercel
```

## Customization

- **Content:** Edit `src/data/siteContent.json`
- **Colors:** Edit `src/assets/css/global.css` (--primary-color)
- **Layout:** Edit components in `src/components/`
"""
    
    with open(new_site_dir / "README.md", 'w', encoding='utf-8') as f:
        f.write(readme_content)
    print(f"✅ Created README.md")
    
    print("\n" + "=" * 60)
    print("🎉 SUCCESS! Your customized site is ready!")
    print("=" * 60)
    print(f"\nLocation: {new_site_dir}")
    print(f"\nNext steps:")
    print(f"  1. cd \"{folder_name}\"")
    print(f"  2. npm run serve")
    print(f"  3. Add your ZimmWriter posts to src/pages/posts/")
    print(f"  4. Deploy to Vercel when ready")
    print("\n" + "=" * 60)

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\nCancelled by user.")
    except Exception as e:
        print(f"\n❌ Error: {e}")

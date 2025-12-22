"""
11ty Affiliate Template Customizer
Asks niche questions and auto-updates your template
"""

import json
import os
import shutil
from pathlib import Path

# Color mappings for different niches
NICHE_COLORS = {
    "power tools": "#f97316",
    "home improvement": "#f97316", 
    "camping": "#22c55e",
    "outdoor": "#22c55e",
    "tech": "#3b82f6",
    "gadgets": "#3b82f6",
    "kitchen": "#ef4444",
    "home": "#f59e0b",
    "pets": "#a855f7",
    "finance": "#1e40af",
    "business": "#1e40af"
}

def get_color_for_niche(niche):
    """Get recommended color based on niche"""
    niche_lower = niche.lower()
    for key, color in NICHE_COLORS.items():
        if key in niche_lower:
            return color
    return "#22c55e"  # Default green

def main():
    print("\n" + "="*60)
    print("11ty AFFILIATE TEMPLATE CUSTOMIZER")
    print("="*60 + "\n")
    
    # Get niche info
    site_name = input("Site name (e.g., 'Camp Smart', 'Tool Hub'): ").strip()
    niche = input("Niche (e.g., 'camping gear', 'power tools'): ").strip()
    hero_title = input("Hero headline (e.g., 'Find Your Perfect Tent'): ").strip()
    hero_subtitle = input("Hero subtitle (brief value prop): ").strip()
    
    # Category items
    print("\nEnter 3 main categories:")
    categories = []
    for i in range(1, 4):
        cat_title = input(f"  Category {i} title: ").strip()
        cat_desc = input(f"  Category {i} description: ").strip()
        categories.append({
            "title": cat_title,
            "description": cat_desc,
            "image": f"/assets/images/category-{i}.svg",
            "link": f"/category/{cat_title.lower().replace(' ', '-')}"
        })
    
    # Get recommended color
    recommended_color = get_color_for_niche(niche)
    print(f"\nRecommended color for {niche}: {recommended_color}")
    custom_color = input(f"Press Enter to use {recommended_color}, or enter custom hex: ").strip()
    primary_color = custom_color if custom_color else recommended_color
    
    # Paths
    template_path = Path("C:/Users/chipp/Documents/PARA-Life/21-Technology/21.01-AI-Tools/11ty template")
    
    print(f"\n" + "="*60)
    print("UPDATING TEMPLATE...")
    print("="*60)
    
    # Update siteContent.json
    content_file = template_path / "my-site/src/data/siteContent.json"
    with open(content_file, 'r') as f:
        content = json.load(f)
    
    # Update hero
    content['hero']['title'] = hero_title
    content['hero']['subtitle'] = hero_subtitle
    
    # Update header
    content['header']['logo_text'] = site_name.upper()
    
    # Update categories
    content['categories']['items'] = categories
    
    # Update reviews section
    content['reviews']['subtitle'] = f"Your {niche} solution"
    
    # Write updated content
    with open(content_file, 'w') as f:
        json.dump(content, f, indent=2)
    
    print(f"✓ Updated siteContent.json")
    
    # Update CSS color
    css_file = template_path / "my-site/src/assets/css/global.css"
    with open(css_file, 'r') as f:
        css_content = f.read()
    
    # Replace primary color
    css_content = css_content.replace('--primary-color: #22c55e;', f'--primary-color: {primary_color};')
    
    with open(css_file, 'w') as f:
        f.write(css_content)
    
    print(f"✓ Updated primary color to {primary_color}")
    
    print(f"\n" + "="*60)
    print("CUSTOMIZATION COMPLETE!")
    print("="*60)
    print(f"\nSite Name: {site_name}")
    print(f"Niche: {niche}")
    print(f"Primary Color: {primary_color}")
    print(f"\nNext steps:")
    print("1. Review changes at http://localhost:8081/")
    print("2. Add ZimmWriter posts to /pages/posts/")
    print("3. Deploy to Vercel")
    print("\n")

if __name__ == "__main__":
    main()

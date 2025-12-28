#!/usr/bin/env python3
"""
Generate a high-quality PDF from resume-modern.html using Playwright
Requires: pip install playwright && playwright install chromium
"""

import os
import sys
from pathlib import Path

def check_and_install_playwright():
    try:
        import playwright
    except ImportError:
        print("Installing playwright...")
        os.system("pip3 install playwright")
        os.system("playwright install chromium")
        print("Playwright installed successfully!")

def generate_pdf():
    check_and_install_playwright()
    
    from playwright.sync_api import sync_playwright
    
    # Get the directory where this script is located
    script_dir = Path(__file__).parent
    html_file = script_dir / 'resume-modern.html'
    output_file = script_dir / 'Peter_Sauer_Resume_2025.pdf'
    
    print(f"Reading HTML from: {html_file}")
    
    if not html_file.exists():
        print(f"❌ Error: {html_file} not found!")
        sys.exit(1)
    
    print("Launching browser...")
    
    with sync_playwright() as p:
        # Launch browser
        browser = p.chromium.launch()
        page = browser.new_page()
        
        # Load the HTML file
        page.goto(f'file://{html_file.absolute()}')
        
        # Wait for any fonts or resources to load
        page.wait_for_timeout(1000)
        
        print("Generating PDF...")
        
        # Generate PDF with high quality settings
        page.pdf(
            path=str(output_file),
            format='Letter',
            margin={
                'top': '0.5in',
                'right': '0.5in',
                'bottom': '0.5in',
                'left': '0.5in'
            },
            print_background=True,
            prefer_css_page_size=False
        )
        
        browser.close()
    
    print(f"✅ PDF generated successfully: {output_file}")
    print(f"   File size: {output_file.stat().st_size / 1024:.1f} KB")

if __name__ == '__main__':
    generate_pdf()

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Fetch content from Confluence pages

This script retrieves content from Confluence pages, handling authentication
through browser cookies/sessions.

Usage:
    python fetch_confluence.py <confluence_url> [--output <file>]

Examples:
    python fetch_confluence.py "https://confluence.shopee.io/pages/viewpage.action?pageId=3050869460"
    python fetch_confluence.py "https://confluence.shopee.io/pages/viewpage.action?pageId=3050869460" --output content.txt
"""

import sys
import argparse
import json
from pathlib import Path

try:
    import requests
    from bs4 import BeautifulSoup
except ImportError:
    print("Error: Required packages not installed.")
    print("Please install: pip install requests beautifulsoup4")
    sys.exit(1)


def get_browser_cookies():
    """
    Attempt to retrieve Confluence authentication cookies from browser.
    This is a placeholder - actual implementation would use browser-cookie3
    or similar library to access browser cookies.
    """
    try:
        # Try to use browser cookies for authentication
        # This requires browser-cookie3: pip install browser-cookie3
        import browser_cookie3
        
        # Try different browsers
        for browser_fn in [browser_cookie3.chrome, browser_cookie3.firefox, browser_cookie3.edge]:
            try:
                cookies = browser_fn(domain_name='shopee.io')
                return cookies
            except:
                continue
        
        return None
    except ImportError:
        print("Note: browser-cookie3 not installed. Install with: pip install browser-cookie3")
        return None


def fetch_confluence_page(url, output_file=None):
    """
    Fetch content from a Confluence page.
    
    Args:
        url: Confluence page URL
        output_file: Optional file path to save content
        
    Returns:
        dict: Page content including title, body text, and structure
    """
    print(f"Fetching Confluence page: {url}")
    
    # Set up session with cookies
    session = requests.Session()
    
    # Try to get browser cookies for authentication
    cookies = get_browser_cookies()
    if cookies:
        session.cookies.update(cookies)
        print("Using browser cookies for authentication")
    else:
        print("Warning: No authentication cookies found. Page may require login.")
    
    # Fetch the page
    try:
        response = session.get(url, timeout=30)
        response.raise_for_status()
    except requests.exceptions.RequestException as e:
        print(f"Error fetching page: {e}")
        print("\nIf the page requires authentication:")
        print("1. Log in to Confluence in your browser")
        print("2. Install browser-cookie3: pip install browser-cookie3")
        print("3. Run this script again")
        return None
    
    # Check if we got redirected to login
    if 'login' in response.url.lower():
        print("Error: Page requires authentication. Please log in to Confluence in your browser first.")
        return None
    
    # Parse the HTML
    soup = BeautifulSoup(response.content, 'html.parser')
    
    # Extract page title
    title_elem = soup.find('title')
    title = title_elem.get_text().strip() if title_elem else "Untitled"
    
    # Extract main content
    # Confluence typically uses id="main-content" or class="wiki-content"
    content_div = soup.find('div', {'id': 'main-content'}) or soup.find('div', {'class': 'wiki-content'})
    
    if not content_div:
        print("Warning: Could not find main content area. Extracting all text.")
        content_div = soup.find('body')
    
    # Extract structured content
    content = {
        'title': title,
        'url': url,
        'sections': [],
        'raw_text': ''
    }
    
    if content_div:
        # Extract headings and content
        for elem in content_div.find_all(['h1', 'h2', 'h3', 'h4', 'p', 'ul', 'ol']):
            if elem.name.startswith('h'):
                # Heading
                content['sections'].append({
                    'type': 'heading',
                    'level': int(elem.name[1]),
                    'text': elem.get_text().strip()
                })
            elif elem.name == 'p':
                # Paragraph
                text = elem.get_text().strip()
                if text:
                    content['sections'].append({
                        'type': 'paragraph',
                        'text': text
                    })
            elif elem.name in ['ul', 'ol']:
                # List
                items = [li.get_text().strip() for li in elem.find_all('li', recursive=False)]
                content['sections'].append({
                    'type': 'list',
                    'items': items
                })
        
        # Get raw text
        content['raw_text'] = content_div.get_text('\n', strip=True)
    
    # Save to file if specified
    if output_file:
        output_path = Path(output_file)
        with open(output_path, 'w', encoding='utf-8') as f:
            json.dump(content, f, ensure_ascii=False, indent=2)
        print(f"Content saved to: {output_path}")
    
    return content


def main():
    parser = argparse.ArgumentParser(description='Fetch content from Confluence pages')
    parser.add_argument('url', help='Confluence page URL')
    parser.add_argument('--output', '-o', help='Output file path (JSON format)')
    
    args = parser.parse_args()
    
    content = fetch_confluence_page(args.url, args.output)
    
    if content:
        print(f"\nSuccessfully fetched: {content['title']}")
        print(f"Sections found: {len(content['sections'])}")
        
        if not args.output:
            # Print summary to stdout
            print("\n--- Content Preview ---")
            print(content['raw_text'][:500] + "..." if len(content['raw_text']) > 500 else content['raw_text'])
        
        return 0
    else:
        print("\nFailed to fetch content.")
        return 1


if __name__ == "__main__":
    sys.exit(main())

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Generate formatted weekly report from content

This script takes work content and generates a formatted weekly report
following the standard template structure.

Usage:
    python generate_report.py --recipient "Name" --highlights "..." --others "..." --next-week "..."
    python generate_report.py --template <template_file> --content <content_json>

Examples:
    python generate_report.py --recipient "Ke Wang" --highlights "Project A\nProject B" --output report.txt
"""

import sys
import argparse
import json
from pathlib import Path
from datetime import datetime


DEFAULT_TEMPLATE = """Hi {recipient},

Below is the weekly report.

**Highlight**:

{highlights}

**Others**:

{others}

**Next Week Plan:**

{next_week}

Thanks,
{sender}
"""


def format_bullet_list(items, prefix="- ", indent=0):
    """
    Format a list of items with proper bullet points and indentation.
    
    Args:
        items: List of strings or nested structure
        prefix: Bullet prefix (default: "- ")
        indent: Indentation level
        
    Returns:
        Formatted string with bullet points
    """
    result = []
    indent_str = "    " * indent
    
    if isinstance(items, list):
        for item in items:
            if isinstance(item, dict):
                # Nested structure with category
                if 'category' in item:
                    result.append(f"{indent_str}{prefix}**{item['category']}**")
                if 'items' in item:
                    result.append(format_bullet_list(item['items'], prefix="- ", indent=indent+1))
            else:
                result.append(f"{indent_str}{prefix}{item}")
    elif isinstance(items, str):
        for line in items.strip().split('\n'):
            if line.strip():
                result.append(f"{indent_str}{prefix}{line.strip()}")
    
    return '\n'.join(result)


def format_others_section(items):
    """
    Format the Others section with special grouping using '>' prefix.
    
    Args:
        items: List of items or structured content
        
    Returns:
        Formatted string for Others section
    """
    result = []
    
    if isinstance(items, list):
        for item in items:
            if isinstance(item, dict):
                # Group header
                if 'group' in item:
                    result.append(f"> {item['group']}")
                if 'items' in item:
                    for sub_item in item['items']:
                        result.append(f"> - {sub_item}")
            else:
                result.append(f"> {item}")
    elif isinstance(items, str):
        for line in items.strip().split('\n'):
            if line.strip():
                if not line.strip().startswith('>'):
                    result.append(f"> {line.strip()}")
                else:
                    result.append(line.strip())
    
    return '\n'.join(result)


def generate_report(recipient, highlights, others, next_week, sender="[Your Name]", template=None):
    """
    Generate a formatted weekly report.
    
    Args:
        recipient: Email recipient name
        highlights: Highlight section content
        others: Others section content
        next_week: Next week plan content
        sender: Sender name (optional)
        template: Custom template string (optional)
        
    Returns:
        Formatted report string
    """
    # Use custom template or default
    template_str = template if template else DEFAULT_TEMPLATE
    
    # Format sections based on their type
    if isinstance(highlights, str):
        formatted_highlights = format_bullet_list(highlights, prefix="- ")
    else:
        formatted_highlights = format_bullet_list(highlights, prefix="- ")
    
    if isinstance(others, str):
        formatted_others = format_others_section(others)
    else:
        formatted_others = format_others_section(others)
    
    if isinstance(next_week, str):
        formatted_next_week = format_bullet_list(next_week, prefix="- ")
    else:
        formatted_next_week = format_bullet_list(next_week, prefix="- ")
    
    # Generate report
    report = template_str.format(
        recipient=recipient,
        highlights=formatted_highlights,
        others=formatted_others,
        next_week=formatted_next_week,
        sender=sender,
        date=datetime.now().strftime("%Y-%m-%d")
    )
    
    return report


def load_content_from_json(json_file):
    """
    Load content from JSON file (output from fetch_confluence.py).
    
    Args:
        json_file: Path to JSON file
        
    Returns:
        Dictionary with extracted content
    """
    with open(json_file, 'r', encoding='utf-8') as f:
        data = json.load(f)
    
    # This is a placeholder - actual implementation would need
    # intelligent parsing to categorize content into sections
    return {
        'highlights': data.get('raw_text', ''),
        'others': '',
        'next_week': ''
    }


def main():
    parser = argparse.ArgumentParser(description='Generate formatted weekly report')
    parser.add_argument('--recipient', '-r', required=True, help='Email recipient name')
    parser.add_argument('--sender', '-s', default='[Your Name]', help='Sender name')
    parser.add_argument('--highlights', help='Highlights section content')
    parser.add_argument('--others', help='Others section content')
    parser.add_argument('--next-week', help='Next week plan content')
    parser.add_argument('--content', help='JSON file with content (from fetch_confluence.py)')
    parser.add_argument('--template', help='Custom email template file')
    parser.add_argument('--output', '-o', help='Output file path')
    
    args = parser.parse_args()
    
    # Load template if specified
    template = None
    if args.template:
        with open(args.template, 'r', encoding='utf-8') as f:
            template = f.read()
    
    # Get content
    if args.content:
        # Load from JSON file
        content = load_content_from_json(args.content)
        highlights = content['highlights']
        others = content['others']
        next_week = content['next_week']
    else:
        # Use command line arguments
        highlights = args.highlights or ''
        others = args.others or ''
        next_week = args.next_week or ''
    
    # Generate report
    report = generate_report(
        recipient=args.recipient,
        highlights=highlights,
        others=others,
        next_week=next_week,
        sender=args.sender,
        template=template
    )
    
    # Output
    if args.output:
        output_path = Path(args.output)
        with open(output_path, 'w', encoding='utf-8') as f:
            f.write(report)
        print(f"Report saved to: {output_path}")
    else:
        print(report)
    
    return 0


if __name__ == "__main__":
    sys.exit(main())

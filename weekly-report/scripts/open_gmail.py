#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Open Gmail with pre-filled email content

This script opens Gmail in the default browser and creates a new compose
window with pre-filled subject and body content.

Usage:
    python open_gmail.py --subject "Weekly Report" --body "Email content here"
    python open_gmail.py --subject "Weekly Report" --body-file report.txt

Examples:
    python open_gmail.py --subject "Weekly Report" --body "Hi there, this is my report."
    python open_gmail.py --subject "Weekly Report" --body-file weekly_report.txt --to "recipient@example.com"
"""

import sys
import argparse
import webbrowser
from pathlib import Path
from urllib.parse import quote


def create_gmail_url(to=None, subject=None, body=None):
    """
    Create a Gmail compose URL with pre-filled fields.
    
    Args:
        to: Recipient email address
        subject: Email subject
        body: Email body content
        
    Returns:
        Gmail compose URL
    """
    # Base URL for Gmail compose
    url = "https://mail.google.com/mail/?view=cm&fs=1"
    
    # Add parameters
    if to:
        url += f"&to={quote(to)}"
    if subject:
        url += f"&su={quote(subject)}"
    if body:
        url += f"&body={quote(body)}"
    
    return url


def open_gmail(to=None, subject=None, body=None):
    """
    Open Gmail composer in default browser.
    
    Args:
        to: Recipient email address
        subject: Email subject
        body: Email body content
        
    Returns:
        True if successful, False otherwise
    """
    try:
        url = create_gmail_url(to=to, subject=subject, body=body)
        
        print(f"Opening Gmail in default browser...")
        if to:
            print(f"To: {to}")
        if subject:
            print(f"Subject: {subject}")
        if body:
            body_preview = body[:100] + "..." if len(body) > 100 else body
            print(f"Body preview: {body_preview}")
        
        webbrowser.open(url)
        print("\nGmail opened successfully!")
        print("Please review and send the email from your browser.")
        
        return True
    except Exception as e:
        print(f"Error opening Gmail: {e}")
        return False


def main():
    parser = argparse.ArgumentParser(description='Open Gmail with pre-filled email content')
    parser.add_argument('--to', help='Recipient email address')
    parser.add_argument('--subject', '-s', help='Email subject')
    parser.add_argument('--body', '-b', help='Email body content')
    parser.add_argument('--body-file', '-f', help='File containing email body content')
    
    args = parser.parse_args()
    
    # Get body content
    body = None
    if args.body_file:
        try:
            with open(args.body_file, 'r', encoding='utf-8') as f:
                body = f.read()
        except Exception as e:
            print(f"Error reading body file: {e}")
            return 1
    elif args.body:
        body = args.body
    
    # Validate that we have something to send
    if not args.subject and not body:
        print("Error: Must provide either --subject or --body/--body-file")
        parser.print_help()
        return 1
    
    # Open Gmail
    success = open_gmail(
        to=args.to,
        subject=args.subject,
        body=body
    )
    
    return 0 if success else 1


if __name__ == "__main__":
    sys.exit(main())

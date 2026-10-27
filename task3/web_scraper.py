"""
CodeAlpha Python Programming Internship
Task 3 (Idea 3): Webpage Title & Metadata Scraper
Author: Intern
Description: Automates fetching a webpage using `requests`, parsing its `<title>`
             and meta tags using regular expressions (`re`), and saving the result
             to a text file.
"""

import re
import sys
import os
import html
from datetime import datetime
from typing import Optional

# Safe UTF-8 console output setup
if hasattr(sys.stdout, 'reconfigure'):
    try:
        sys.stdout.reconfigure(encoding='utf-8', errors='replace')
    except Exception:
        pass

# Try importing requests, fallback to urllib if not present
try:
    import requests
    HAS_REQUESTS = True
except ImportError:
    import urllib.request
    HAS_REQUESTS = False

DEFAULT_URL = "https://example.com"
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DEFAULT_OUTPUT = os.path.join(BASE_DIR, "scraped_title.txt")


def fetch_html(url: str, timeout: int = 10) -> str:
    """Fetches the HTML source code of the webpage with standard User-Agent headers."""
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) CodeAlphaScraper/1.0"
    }

    if HAS_REQUESTS:
        response = requests.get(url, headers=headers, timeout=timeout)
        response.raise_for_status()
        return response.text
    else:
        req = urllib.request.Request(url, headers=headers)
        with urllib.request.urlopen(req, timeout=timeout) as resp:
            charset = resp.headers.get_content_charset() or 'utf-8'
            return resp.read().decode(charset, errors='replace')


def _clean_html_text(raw_text: str) -> str:
    """Removes nested tags, decodes HTML entities, and collapses whitespace."""
    text = re.sub(r"<[^>]+>", "", raw_text)
    text = html.unescape(text)
    return re.sub(r"\s+", " ", text).strip()


def scrape_page_title(
    url: str = DEFAULT_URL, output_file: Optional[str] = None
) -> dict:
    """
    Scrapes the title, h1 headings, and description from the specified URL,
    and saves the findings into an output text file.
    """
    if output_file is None:
        output_file = DEFAULT_OUTPUT

    print(f"\n[*] Fetching webpage: {url} ...")
    try:
        page_html = fetch_html(url)
    except Exception as e:
        print(f"[!] Network error fetching URL: {e}")
        return {}

    # Extract <title>...</title> using regex (allows attributes on the tag)
    title_match = re.search(r'<title[^>]*>(.*?)</title>', page_html, re.IGNORECASE | re.DOTALL)
    title = _clean_html_text(title_match.group(1)) if title_match else "No <title> tag found"

    # Also search for <h1> headings
    h1_matches = re.findall(r'<h1[^>]*>(.*?)</h1>', page_html, re.IGNORECASE | re.DOTALL)
    clean_h1s = [text for text in (_clean_html_text(h) for h in h1_matches) if text]

    # Search for meta description; accept name/content in either order
    meta_match = re.search(
        r'<meta[^>]*name=["\']description["\'][^>]*content=["\'](.*?)["\']',
        page_html,
        re.IGNORECASE | re.DOTALL,
    )
    if not meta_match:
        meta_match = re.search(
            r'<meta[^>]*content=["\'](.*?)["\'][^>]*name=["\']description["\']',
            page_html,
            re.IGNORECASE | re.DOTALL,
        )
    description = _clean_html_text(meta_match.group(1)) if meta_match else "None"

    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    # Display results in console
    print("\n" + "=" * 55)
    print("             WEBPAGE SCRAPING RESULTS             ")
    print("=" * 55)
    print(f"URL Scraped      : {url}")
    print(f"Extracted Title  : {title}")
    if clean_h1s:
        print(f"H1 Heading(s)    : {', '.join(clean_h1s)}")
    print(f"Meta Description : {description}")
    print(f"Timestamp        : {timestamp}")
    print("=" * 55)

    # Save to file
    with open(output_file, "w", encoding="utf-8") as f:
        f.write("=" * 55 + "\n")
        f.write("      CODEALPHA WEBPAGE TITLE SCRAPER RESULT      \n")
        f.write("=" * 55 + "\n")
        f.write(f"Scraped URL      : {url}\n")
        f.write(f"Page Title       : {title}\n")
        if clean_h1s:
            f.write(f"Heading (H1)     : {', '.join(clean_h1s)}\n")
        f.write(f"Meta Description : {description}\n")
        f.write(f"Scraped At       : {timestamp}\n")
        f.write("=" * 55 + "\n")

    print(f"[+] Saved scraped webpage details to: '{output_file}'\n")

    return {
        "url": url,
        "title": title,
        "headings": clean_h1s,
        "description": description
    }


def main():
    print("=" * 60)
    print("      CODEALPHA TASK AUTOMATION: WEBPAGE TITLE SCRAPER      ")
    print("=" * 60)
    print("1. Scrape Fixed Default Webpage (https://example.com)")
    print("2. Scrape Custom Webpage URL")
    print("3. Exit")

    choice = input("\nEnter choice (1-3): ").strip()

    if choice == "1":
        scrape_page_title(DEFAULT_URL)
    elif choice == "2":
        url = input("Enter website URL (e.g., https://example.com): ").strip()
        if not url.startswith("http://") and not url.startswith("https://"):
            url = "https://" + url
        scrape_page_title(url)
    elif choice == "3":
        print("Exiting. Goodbye!")
    else:
        print("[!] Invalid selection.")


if __name__ == "__main__":
    try:
        main()
    except (KeyboardInterrupt, EOFError):
        print("\nExiting. Goodbye!\n")

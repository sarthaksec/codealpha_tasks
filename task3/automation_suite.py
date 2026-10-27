"""
CodeAlpha Python Programming Internship
Task 3: Unified Task Automation Suite
Author: Intern
Description: An all-in-one menu interface combining all three task automation
             options:
             1. JPG File Organizer (os, shutil)
             2. Email Address Extractor (re, file handling)
             3. Webpage Title Scraper (requests, re)
"""

import sys
import os

# Safe UTF-8 console output setup
if hasattr(sys.stdout, 'reconfigure'):
    try:
        sys.stdout.reconfigure(encoding='utf-8', errors='replace')
    except Exception:
        pass

from file_organizer import (
    organize_jpg_files,
    create_demo_files,
    DEMO_SOURCE_DIR,
    DEMO_DEST_DIR,
)
from email_extractor import (
    extract_emails,
    create_sample_text_file,
    SAMPLE_INPUT,
    SAMPLE_OUTPUT,
)
from web_scraper import scrape_page_title, DEFAULT_URL


def main():
    while True:
        print("\n" + "=" * 60)
        print("        CODEALPHA TASK AUTOMATION MASTER SUITE        ")
        print("=" * 60)
        print("Choose an automation script to run:")
        print("1. File Organizer (Move .jpg images into target folder)")
        print("2. Email Extractor (Extract email addresses via regex)")
        print("3. Webpage Title Scraper (Scrape page title & meta info)")
        print("4. Run All 3 Automations in Demo Mode (Quick Showcase)")
        print("5. Exit")

        choice = input("\nEnter choice (1-5): ").strip()

        if choice == "1":
            print("\n--- Running JPG File Organizer ---")
            create_demo_files(DEMO_SOURCE_DIR)
            organize_jpg_files(DEMO_SOURCE_DIR, DEMO_DEST_DIR)

        elif choice == "2":
            print("\n--- Running Email Extractor ---")
            create_sample_text_file(SAMPLE_INPUT)
            extract_emails(SAMPLE_INPUT, SAMPLE_OUTPUT)

        elif choice == "3":
            print("\n--- Running Webpage Title Scraper ---")
            url = input(f"Enter URL (press Enter for default '{DEFAULT_URL}'): ").strip()
            if not url:
                url = DEFAULT_URL
            elif not url.startswith("http://") and not url.startswith("https://"):
                url = "https://" + url
            scrape_page_title(url)

        elif choice == "4":
            print("\n" + "#" * 60)
            print("       SHOWCASE: RUNNING ALL 3 AUTOMATION SCRIPTS       ")
            print("#" * 60)

            print("\n[Step 1/3] File Organizer Demonstration:")
            create_demo_files(DEMO_SOURCE_DIR)
            organize_jpg_files(DEMO_SOURCE_DIR, DEMO_DEST_DIR)

            print("\n[Step 2/3] Email Extractor Demonstration:")
            create_sample_text_file(SAMPLE_INPUT)
            extract_emails(SAMPLE_INPUT, SAMPLE_OUTPUT)

            print("\n[Step 3/3] Webpage Title Scraper Demonstration:")
            scrape_page_title(DEFAULT_URL)

            print("\n[+] All 3 automations completed successfully!")

        elif choice == "5":
            print("\nExiting CodeAlpha Task Automation Suite. Goodbye!\n")
            break
        else:
            print("[!] Invalid option. Please enter 1 to 5.")


if __name__ == "__main__":
    try:
        main()
    except (KeyboardInterrupt, EOFError):
        print("\nExiting. Goodbye!\n")

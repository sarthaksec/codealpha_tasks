"""
CodeAlpha Python Programming Internship
Task 3 (Idea 2): Email Address Extractor
Author: Intern
Description: Automates extracting all valid email addresses from any text file
             using regular expressions (`re`), deduplicating them, and saving
             the organized list to an output file.
"""

import re
import sys
import os

# Safe UTF-8 console output setup
if hasattr(sys.stdout, 'reconfigure'):
    try:
        sys.stdout.reconfigure(encoding='utf-8', errors='replace')
    except Exception:
        pass

# Sample files live beside this script so the command works from any cwd.
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
SAMPLE_INPUT = os.path.join(BASE_DIR, "sample_text_with_emails.txt")
SAMPLE_OUTPUT = os.path.join(BASE_DIR, "extracted_emails.txt")

# Regex for standard email addresses. Word boundaries prevent partial matches,
# domain labels cannot start/end with a hyphen, and the TLD is restricted to
# letters so trailing sentence punctuation is ignored.
EMAIL_REGEX = (
    r"\b[A-Za-z0-9._%+-]+@"
    r"(?:[A-Za-z0-9](?:[A-Za-z0-9-]*[A-Za-z0-9])?\.)+"
    r"[A-Za-z]{2,}\b"
)


def create_sample_text_file(filepath: str = SAMPLE_INPUT):
    """Creates a sample text file containing various emails embedded in text."""
    sample_content = """Hello Team,
Here are the contact details for the project coordinators:
- General queries: contact@codealpha.tech
- Technical lead: alice.johnson@example.com or support@example.co.uk
- Mentorship team: mentorship-help@codealpha.tech
- Placement officer: careers_info@codealpha.tech
- Duplicate test: contact@codealpha.tech
For emergencies, reach out to admin123@domain.org or contact@domain.net.

Thank you!
    """
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(sample_content.strip())
    print(f"[+] Created sample file with test text at: '{filepath}'")


def extract_emails(input_file: str, output_file: str) -> list:
    """
    Reads input_file, finds all matching emails using regex,
    deduplicates and sorts them, and writes the results to output_file.
    """
    if not os.path.exists(input_file):
        print(f"[!] Error: Input file '{input_file}' not found.")
        return []

    with open(input_file, "r", encoding="utf-8", errors="ignore") as f:
        content = f.read()

    # Find all email matches
    raw_matches = re.findall(EMAIL_REGEX, content)

    # Normalize to lowercase and remove duplicates while preserving uniqueness
    unique_emails = sorted(list({email.lower().rstrip('.') for email in raw_matches}))

    if not unique_emails:
        print(f"[!] No email addresses found in '{input_file}'.")
        return []

    # Write results to output file
    with open(output_file, "w", encoding="utf-8") as f:
        f.write("# Extracted Email Addresses\n")
        f.write(f"# Source: {os.path.basename(input_file)}\n")
        f.write(f"# Total Unique Found: {len(unique_emails)}\n")
        f.write("-" * 40 + "\n")
        for email in unique_emails:
            f.write(email + "\n")

    print(f"\n[+] Extraction Successful!")
    print(f"    - Total mentions found: {len(raw_matches)}")
    print(f"    - Unique emails identified: {len(unique_emails)}")
    print(f"    - Saved results to: '{output_file}'")
    print("\n--- Extracted Emails ---")
    for i, email in enumerate(unique_emails, 1):
        print(f" {i}. {email}")

    return unique_emails


def main():
    print("=" * 60)
    print("      CODEALPHA TASK AUTOMATION: EMAIL EXTRACTOR       ")
    print("=" * 60)
    print("1. Run with Demo Sample File (Auto-generates sample text & extracts)")
    print("2. Extract from a Custom Text File")
    print("3. Exit")

    choice = input("\nEnter choice (1-3): ").strip()

    if choice == "1":
        create_sample_text_file(SAMPLE_INPUT)
        extract_emails(SAMPLE_INPUT, SAMPLE_OUTPUT)
    elif choice == "2":
        in_file = input("Enter path to input text file: ").strip()
        out_file = input("Enter path for output file (default: extracted_emails.txt): ").strip()
        if not out_file:
            out_file = "extracted_emails.txt"
        extract_emails(in_file, out_file)
    elif choice == "3":
        print("Exiting. Goodbye!")
    else:
        print("[!] Invalid selection.")


if __name__ == "__main__":
    try:
        main()
    except (KeyboardInterrupt, EOFError):
        print("\nExiting. Goodbye!\n")

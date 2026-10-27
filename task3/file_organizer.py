"""
CodeAlpha Python Programming Internship
Task 3 (Idea 1): File Automation - Image & JPG Organizer
Author: Intern
Description: Automates organizing files by scanning a source folder, finding all .jpg
             (and related image) files, and moving them into a dedicated destination folder.
             Utilizes `os` and `shutil` modules.
"""

import os
import shutil
import sys

# Safe UTF-8 console output setup
if hasattr(sys.stdout, 'reconfigure'):
    try:
        sys.stdout.reconfigure(encoding='utf-8', errors='replace')
    except Exception:
        pass

# Demo folders live beside this script so the command works from any cwd.
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DEMO_SOURCE_DIR = os.path.join(BASE_DIR, "demo_source_files")
DEMO_DEST_DIR = os.path.join(BASE_DIR, "demo_organized_jpgs")


def create_demo_files(source_dir: str):
    """Creates temporary sample dummy files to demonstrate file movement."""
    os.makedirs(source_dir, exist_ok=True)
    sample_files = [
        "photo_vacation.jpg",
        "family_portrait.jpg",
        "profile_picture.jpg",
        "document.txt",
        "report.pdf",
        "notes.docx"
    ]
    created = []
    for fname in sample_files:
        fpath = os.path.join(source_dir, fname)
        if not os.path.exists(fpath):
            with open(fpath, "w", encoding="utf-8") as f:
                f.write(f"Sample content for {fname}")
            created.append(fname)

    if created:
        print(f"[+] Created {len(created)} sample test files in '{source_dir}':")
        for f in created:
            print(f"    - {f}")


def organize_jpg_files(source_dir: str, dest_dir: str, extensions: tuple = (".jpg", ".jpeg")) -> int:
    """
    Scans source_dir for files matching given extensions,
    and moves them to dest_dir.

    Returns the number of files moved.
    """
    if not os.path.exists(source_dir):
        print(f"[!] Error: Source directory '{source_dir}' does not exist.")
        return 0

    os.makedirs(dest_dir, exist_ok=True)

    moved_count = 0
    print(f"\n[*] Scanning '{source_dir}' for {extensions} files...")

    for filename in os.listdir(source_dir):
        source_file = os.path.join(source_dir, filename)

        # Check if it is a regular file and has matching extension (case-insensitive)
        if os.path.isfile(source_file) and filename.lower().endswith(extensions):
            dest_file = os.path.join(dest_dir, filename)

            # Handle file collision if destination file already exists
            if os.path.exists(dest_file):
                base, ext = os.path.splitext(filename)
                counter = 1
                while os.path.exists(os.path.join(dest_dir, f"{base}_{counter}{ext}")):
                    counter += 1
                dest_file = os.path.join(dest_dir, f"{base}_{counter}{ext}")

            shutil.move(source_file, dest_file)
            print(f"    -> Moved: {filename} ===> {os.path.basename(dest_file)}")
            moved_count += 1

    print(f"[+] Task Complete: Successfully moved {moved_count} image file(s) to '{dest_dir}'.\n")
    return moved_count


def main():
    print("=" * 60)
    print("      CODEALPHA TASK AUTOMATION: JPG FILE ORGANIZER       ")
    print("=" * 60)
    print("1. Run with Demo/Sample Files (Creates demo folder & moves .jpg)")
    print("2. Run on Custom Folders (Specify your own source and target)")
    print("3. Exit")

    choice = input("\nEnter choice (1-3): ").strip()

    if choice == "1":
        create_demo_files(DEMO_SOURCE_DIR)
        organize_jpg_files(DEMO_SOURCE_DIR, DEMO_DEST_DIR)
    elif choice == "2":
        source = input("Enter source directory path: ").strip()
        dest = input("Enter destination directory path: ").strip()
        if source and dest:
            organize_jpg_files(source, dest)
        else:
            print("[!] Invalid paths provided.")
    elif choice == "3":
        print("Exiting. Goodbye!")
    else:
        print("[!] Invalid selection.")


if __name__ == "__main__":
    try:
        main()
    except (KeyboardInterrupt, EOFError):
        print("\nExiting. Goodbye!\n")

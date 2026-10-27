# Task 3: Task Automation with Python Scripts (CodeAlpha Internship)

## 📌 Project Overview
Repetitive real-world workflows can consume valuable time and introduce human error. This project delivers a suite of modular Python scripts to automate common file system, text processing, and web operations.

While the assignment required picking **one** idea, **all three ideas** have been fully implemented and integrated with standalone interfaces as well as a unified master automation suite (`automation_suite.py`):
1. **JPG File Organizer (`file_organizer.py`)** — Moves and categorizes `.jpg` / image files between directories using `os` and `shutil`.
2. **Email Address Extractor (`email_extractor.py`)** — Parses arbitrary text to extract, deduplicate, and export valid email addresses using regular expressions (`re`).
3. **Webpage Title Scraper (`web_scraper.py`)** — Fetches live web pages using `requests`, parses HTML `<title>`, `<h1>`, and metadata tags, and saves the output to a text file.

---

## 🎯 Features & Implementations

### 1. File Organizer (`file_organizer.py`)
- Automatically identifies `.jpg` and `.jpeg` files in a source directory.
- Safely moves them to a specified target folder using `shutil.move()`.
- Built-in collision handling (avoids overwriting existing files by appending a numeric suffix).
- Includes one-click demo file generator to create sample files for testing.
- Demo folders (`demo_source_files/` and `demo_organized_jpgs/`) are created next to the script, so the tool works regardless of the directory you launch it from.

### 2. Email Address Extractor (`email_extractor.py`)
- Employs a boundary-aware RFC-style regex (`\b[A-Za-z0-9._%+-]+@(?:[A-Za-z0-9](?:[A-Za-z0-9-]*[A-Za-z0-9])?\.)+[A-Za-z]{2,}\b`) to extract valid emails from unstructured text while ignoring malformed addresses and trailing punctuation.
- Cleans and deduplicates addresses using Python sets.
- Writes sorted results to `extracted_emails.txt`.
- Built-in sample text generator for immediate verification.

### 3. Webpage Title Scraper (`web_scraper.py`)
- Sends HTTP requests using `requests` with standard user-agent headers.
- Regex extraction for `<title>`, `<h1>`, and `<meta name="description">` tags.
- Logs timestamps and saves structured outputs into `scraped_title.txt`.
- Defaults to `https://example.com` or accepts any user-provided URL.

---

## 🛠️ Concepts Used
- **File System Operations:** `os.listdir()`, `os.path.join()`, `os.path.splitext()`, `shutil.move()`.
- **Regular Expressions:** `re.findall()`, `re.search()`, pattern flags (`re.IGNORECASE | re.DOTALL`).
- **HTTP & Networking:** `requests.get()`, fallback to `urllib.request`.
- **File I/O:** Reading and writing files with UTF-8 encoding.

---

## 🚀 How to Run

Navigate to this directory:
```bash
cd Task3_Task_Automation
```

### Run the Master Automation Suite:
```bash
python automation_suite.py
```

### Or Run Individual Scripts Independently:
```bash
# 1. Run File Organizer
python file_organizer.py

# 2. Run Email Extractor
python email_extractor.py

# 3. Run Web Title Scraper
python web_scraper.py
```

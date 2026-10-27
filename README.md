# CodeAlpha Python Programming Internship — Tasks

This repository contains three completed tasks from the **CodeAlpha Python Programming Internship (CodeAlpha M1)**.

## Completed Tasks

| Folder | Project | Key Concepts |
| :---: | :--- | :--- |
| [`task1`](./task1) | **Hangman Game** — text-based word guessing game with 6 incorrect attempts and ASCII gallows art. | `random`, `while`, `if-else`, strings, lists, sets |
| [`task2`](./task2) | **Stock Portfolio Tracker** — calculates holding values and total investment using hardcoded prices, with TXT and CSV export. | dictionaries, arithmetic, input validation, file handling, `csv` |
| [`task3`](./task3) | **Task Automation Suite** — JPG file organizer, regex email extractor, and webpage title/metadata scraper. | `os`, `shutil`, `re`, `requests`, file handling |

Each task folder contains its own `README.md` with a detailed description, concepts used, and sample output.

## Requirements

- Python 3.8 or newer
- `requests` (used by the optional web scraper in Task 3)

Install the dependency:

```bash
pip install -r requirements.txt
```

## How to Run

Run each task from the repository root:

```bash
# Task 1: Hangman Game
python task1/hangman.py

# Task 2: Stock Portfolio Tracker
python task2/stock_tracker.py

# Task 3: Task Automation Suite
python task3/automation_suite.py
```

Task 3 can also be run as individual scripts:

```bash
python task3/file_organizer.py
python task3/email_extractor.py
python task3/web_scraper.py
```

## Sample Outputs

- `task2/portfolio_summary.txt` and `task2/portfolio_summary.csv` — sample portfolio reports.
- `task3/extracted_emails.txt` — sample regex extraction result.
- `task3/scraped_title.txt` — sample webpage metadata scrape.
- `task3/demo_source_files/` and `task3/demo_organized_jpgs/` — sample before/after folders for the file organizer.

## Notes

- Task 2 saves reports beside `stock_tracker.py` by default, so it works from any working directory.
- Task 3 creates its demo folders beside the automation scripts.
- The web scraper defaults to `https://example.com` and accepts any custom URL.

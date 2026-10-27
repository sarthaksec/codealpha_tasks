# Task 2: Stock Portfolio Tracker (CodeAlpha Internship)

## 📌 Project Overview
A simple, robust stock investment tracking tool developed in Python. It allows users to define a stock portfolio by selecting stock symbols and specifying share quantities. Using a hardcoded dictionary of stock market prices, the program calculates individual holding valuations, portfolio percentage weights, and overall total investment value. It also offers flexible export functionality to save results to `.txt` and `.csv` files.

---

## 🎯 Task Requirements & Features
- **Hardcoded Stock Dictionary:** Predefined dictionary mapping symbols to current USD prices (`AAPL`, `TSLA`, `GOOGL`, `MSFT`, `AMZN`, `NVDA`, `META`, `NFLX`).
- **User Input & Validation:**
  - Case-insensitive stock lookup (e.g. `aapl` or `AAPL`).
  - Validation ensuring quantities are strictly positive numbers.
  - Multi-entry support with cumulative addition for duplicate tickers.
- **Calculations & Analytics:**
  - Computes `Total Value = Quantity * Unit Price`.
  - Calculates overall portfolio total investment.
  - Calculates percentage share distribution across holdings.
- **Export Capabilities:**
  - Export formatted report to `portfolio_summary.txt`.
  - Export structured spreadsheet data to `portfolio_summary.csv`.
  - By default, both files are written beside the script, so the tracker works from any working directory.

---

## 🛠️ Concepts Used
- **Dictionaries:** Fast $O(1)$ stock price lookups and portfolio holdings map (`{symbol: quantity}`).
- **String Formatting:** Neatly aligned tabular displays using Python string format specifications.
- **Input/Output & Error Handling:** Validating numeric entries using `try...except ValueError`.
- **File Handling:** Utilizing standard Python `open()` and the built-in `csv` module for saving reports.

---

## 🚀 How to Run

1. Open your terminal or command prompt.
2. Navigate to this directory:
   ```bash
   cd Task2_Stock_Portfolio_Tracker
   ```
3. Run the script:
   ```bash
   python stock_tracker.py
   ```

---

## 📸 Sample Console Session & Output

```text
==================================================
     WELCOME TO CODEALPHA STOCK TRACKER     
==================================================

--- Main Menu ---
1. View Available Stocks & Prices
2. Add / Update Stocks in Portfolio
3. View Portfolio Summary & Total Value
4. Save Portfolio to Text File (.txt)
5. Save Portfolio to CSV Spreadsheet (.csv)
6. Clear Portfolio
7. Exit

Enter your choice (1-7): 2

====================================
      AVAILABLE STOCKS & PRICES     
====================================
Stock Symbol                    Price (USD)
------------------------------------
AAPL                            $        180.00
AMZN                            $        185.00
GOOGL                           $        140.00
META                            $        490.00
MSFT                            $        420.00
NFLX                            $        620.00
NVDA                            $        120.00
TSLA                            $        250.00
------------------------------------

Enter Stock Symbol (or 'done' to stop adding): AAPL
Enter quantity of shares for AAPL: 10
[+] Added 10.0 shares of AAPL. (Total AAPL shares: 10.0)
Add another stock? (y/n): y

Enter Stock Symbol (or 'done' to stop adding): TSLA
Enter quantity of shares for TSLA: 5
[+] Added 5.0 shares of TSLA. (Total TSLA shares: 5.0)
Add another stock? (y/n): n

--- Main Menu ---
...
Enter your choice (1-7): 3

=================================================================
                 PORTFOLIO SUMMARY REPORT                 
=================================================================
Symbol     Quantity     Unit Price     Total Value     Share % 
-----------------------------------------------------------------
AAPL       10.00        $180.00        $1800.00          59.0%
TSLA       5.00         $250.00        $1250.00          41.0%
-----------------------------------------------------------------
TOTAL PORTFOLIO INVESTMENT:                     $      3050.00
=================================================================
```

"""
CodeAlpha Python Programming Internship
Task 2: Stock Portfolio Tracker
Author: Intern
Description: A simple stock tracker that calculates total investment value based
             on user-defined quantities and hardcoded stock prices, with file export
             options (.txt and .csv).
"""

import os
import sys
import csv
from datetime import datetime
from typing import Optional

# Safe UTF-8 console output setup
if hasattr(sys.stdout, 'reconfigure'):
    try:
        sys.stdout.reconfigure(encoding='utf-8', errors='replace')
    except Exception:
        pass

# Resolve default export locations relative to this script, not the caller's cwd.
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# Hardcoded dictionary defining stock prices (in USD)
STOCK_PRICES = {
    "AAPL": 180.00,
    "TSLA": 250.00,
    "GOOGL": 140.00,
    "MSFT": 420.00,
    "AMZN": 185.00,
    "NVDA": 120.00,
    "META": 490.00,
    "NFLX": 620.00
}


def display_available_stocks():
    """Displays the predefined list of available stocks and their current prices."""
    print("\n" + "=" * 36)
    print("      AVAILABLE STOCKS & PRICES     ")
    print("=" * 36)
    print(f"{'Stock Symbol':<15} {'Price (USD)':>15}")
    print("-" * 36)
    for symbol, price in sorted(STOCK_PRICES.items()):
        print(f"{symbol:<15} ${price:>14.2f}")
    print("-" * 36)


def calculate_portfolio_totals(portfolio: dict) -> tuple:
    """
    Calculates detailed investment values for each holding and total portfolio value.
    Returns:
        (breakdown_list, total_investment)
    """
    total_investment = 0.0
    breakdown = []

    for symbol, qty in portfolio.items():
        price = STOCK_PRICES[symbol]
        value = qty * price
        total_investment += value
        breakdown.append({
            "symbol": symbol,
            "quantity": qty,
            "price": price,
            "value": value
        })

    return breakdown, total_investment


def display_portfolio_summary(portfolio: dict):
    """Prints a formatted tabular summary of the portfolio and total investment."""
    if not portfolio:
        print("\n[!] Portfolio is currently empty. Add stocks first.")
        return

    breakdown, total_investment = calculate_portfolio_totals(portfolio)

    print("\n" + "=" * 65)
    print("                 PORTFOLIO SUMMARY REPORT                 ")
    print("=" * 65)
    print(f"{'Symbol':<10} {'Quantity':<12} {'Unit Price':<14} {'Total Value':<15} {'Share %':<8}")
    print("-" * 65)

    for item in breakdown:
        share = (item["value"] / total_investment * 100) if total_investment > 0 else 0
        print(f"{item['symbol']:<10} {item['quantity']:<12.2f} ${item['price']:<13.2f} ${item['value']:<14.2f} {share:>6.1f}%")

    print("-" * 65)
    print(f"{'TOTAL PORTFOLIO INVESTMENT:':<48} ${total_investment:>13.2f}")
    print("=" * 65)


def save_portfolio_to_txt(portfolio: dict, filename: Optional[str] = None):
    """Saves the current portfolio report to a text file."""
    if filename is None:
        filename = os.path.join(BASE_DIR, "portfolio_summary.txt")
    if not portfolio:
        print("[!] Cannot save: portfolio is empty.")
        return

    breakdown, total_investment = calculate_portfolio_totals(portfolio)
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    with open(filename, "w", encoding="utf-8") as f:
        f.write("=" * 65 + "\n")
        f.write(f"           CODEALPHA STOCK PORTFOLIO REPORT\n")
        f.write(f"           Generated on: {timestamp}\n")
        f.write("=" * 65 + "\n")
        f.write(f"{'Symbol':<10} {'Quantity':<12} {'Unit Price':<14} {'Total Value':<15} {'Share %':<8}\n")
        f.write("-" * 65 + "\n")
        for item in breakdown:
            share = (item["value"] / total_investment * 100) if total_investment > 0 else 0
            f.write(f"{item['symbol']:<10} {item['quantity']:<12.2f} ${item['price']:<13.2f} ${item['value']:<14.2f} {share:>6.1f}%\n")
        f.write("-" * 65 + "\n")
        f.write(f"{'TOTAL PORTFOLIO INVESTMENT:':<48} ${total_investment:>13.2f}\n")
        f.write("=" * 65 + "\n")

    print(f"[+] Successfully saved portfolio summary to: {filename}")


def save_portfolio_to_csv(portfolio: dict, filename: Optional[str] = None):
    """Exports the portfolio holdings to a CSV spreadsheet file."""
    if filename is None:
        filename = os.path.join(BASE_DIR, "portfolio_summary.csv")
    if not portfolio:
        print("[!] Cannot save: portfolio is empty.")
        return

    breakdown, total_investment = calculate_portfolio_totals(portfolio)

    with open(filename, "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(["Stock Symbol", "Quantity", "Unit Price (USD)", "Total Value (USD)", "Portfolio Share (%)"])
        for item in breakdown:
            share = (item["value"] / total_investment * 100) if total_investment > 0 else 0
            writer.writerow([item["symbol"], f"{item['quantity']:.2f}", f"{item['price']:.2f}", f"{item['value']:.2f}", f"{share:.2f}"])
        writer.writerow([])
        writer.writerow(["TOTAL INVESTMENT", "", "", f"{total_investment:.2f}", "100.00%"])

    print(f"[+] Successfully exported portfolio to CSV: {filename}")


def add_stock_interactive(portfolio: dict):
    """Guides user to input stock name and quantity with validations."""
    display_available_stocks()
    while True:
        symbol = input("\nEnter Stock Symbol (or 'done' to stop adding): ").strip().upper()
        if symbol == "DONE":
            break
        if symbol not in STOCK_PRICES:
            print(f"[!] '{symbol}' is not in the predefined stock list. Available: {', '.join(STOCK_PRICES.keys())}")
            continue

        while True:
            qty_input = input(f"Enter quantity of shares for {symbol}: ").strip()
            try:
                qty = float(qty_input)
                if qty <= 0:
                    print("[!] Quantity must be greater than 0.")
                    continue
                break
            except ValueError:
                print("[!] Invalid quantity. Please enter a valid numeric value.")

        # Add or update portfolio
        portfolio[symbol] = portfolio.get(symbol, 0.0) + qty
        print(f"[+] Added {qty} shares of {symbol}. (Total {symbol} shares: {portfolio[symbol]})")

        cont = input("Add another stock? (y/n): ").strip().lower()
        if cont not in ("y", "yes"):
            break


def _run_main_menu():
    """Runs the interactive menu until the user chooses to exit."""
    portfolio = {}

    print("\n" + "=" * 50)
    print("     WELCOME TO CODEALPHA STOCK TRACKER     ")
    print("=" * 50)

    while True:
        print("\n--- Main Menu ---")
        print("1. View Available Stocks & Prices")
        print("2. Add / Update Stocks in Portfolio")
        print("3. View Portfolio Summary & Total Value")
        print("4. Save Portfolio to Text File (.txt)")
        print("5. Save Portfolio to CSV Spreadsheet (.csv)")
        print("6. Clear Portfolio")
        print("7. Exit")

        choice = input("\nEnter your choice (1-7): ").strip()

        if choice == "1":
            display_available_stocks()
        elif choice == "2":
            add_stock_interactive(portfolio)
        elif choice == "3":
            display_portfolio_summary(portfolio)
        elif choice == "4":
            display_portfolio_summary(portfolio)
            if portfolio:
                save_portfolio_to_txt(portfolio)
        elif choice == "5":
            display_portfolio_summary(portfolio)
            if portfolio:
                save_portfolio_to_csv(portfolio)
        elif choice == "6":
            portfolio.clear()
            print("[+] Portfolio has been cleared.")
        elif choice == "7":
            print("\nThank you for using CodeAlpha Stock Portfolio Tracker. Goodbye!\n")
            break
        else:
            print("[!] Invalid option. Please choose between 1 and 7.")


def main():
    """Entry point with graceful handling of Ctrl+C and closed input."""
    try:
        _run_main_menu()
    except (KeyboardInterrupt, EOFError):
        print("\n\nSession interrupted. Thank you for using CodeAlpha Stock Tracker!\n")


if __name__ == "__main__":
    main()

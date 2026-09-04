"""
Stock Portfolio Tracker
------------------------
A simple console app that:
- Lets the user enter stock names and quantities.
- Looks up prices from a hardcoded dictionary.
- Calculates total investment value.
- Saves a summary to a .txt or .csv file.
"""

import csv
from datetime import datetime

# Hardcoded stock prices (in USD)
STOCK_PRICES = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGL": 140,
    "AMZN": 178,
    "MSFT": 420,
    "META": 500,
    "NFLX": 680,
}


def show_available_stocks():
    print("\nAvailable stocks and prices:")
    for symbol, price in STOCK_PRICES.items():
        print(f"  {symbol:<6} ${price}")
    print()


def get_portfolio_input():
    """Collects stock symbol + quantity pairs from the user."""
    portfolio = []  # list of dicts: {symbol, quantity, price, value}

    print("Enter stock symbol and quantity (type 'done' as symbol to finish).")
    while True:
        symbol = input("Stock symbol: ").strip().upper()
        if symbol == "DONE":
            break

        if symbol not in STOCK_PRICES:
            print(f"  '{symbol}' not found in price list. Try one of: "
                  f"{', '.join(STOCK_PRICES.keys())}")
            continue

        qty_input = input(f"Quantity of {symbol}: ").strip()
        try:
            quantity = float(qty_input)
            if quantity <= 0:
                print("  Quantity must be greater than 0.")
                continue
        except ValueError:
            print("  Please enter a valid number for quantity.")
            continue

        price = STOCK_PRICES[symbol]
        value = price * quantity
        portfolio.append({
            "symbol": symbol,
            "quantity": quantity,
            "price": price,
            "value": value,
        })
        print(f"  Added: {quantity} x {symbol} @ ${price} = ${value:,.2f}\n")

    return portfolio


def calculate_total(portfolio):
    return sum(item["value"] for item in portfolio)


def display_summary(portfolio, total):
    print("\n" + "=" * 40)
    print("PORTFOLIO SUMMARY")
    print("=" * 40)
    if not portfolio:
        print("No stocks entered.")
        return
    for item in portfolio:
        print(f"{item['symbol']:<6} | Qty: {item['quantity']:<8} | "
              f"Price: ${item['price']:<8} | Value: ${item['value']:,.2f}")
    print("-" * 40)
    print(f"TOTAL INVESTMENT: ${total:,.2f}")
    print("=" * 40)


def save_to_file(portfolio, total):
    """Asks the user if/how they'd like to save the results."""
    choice = input("\nSave results to a file? (txt/csv/no): ").strip().lower()

    if choice not in ("txt", "csv"):
        print("Skipping file save.")
        return

    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    filename = f"portfolio_summary_{timestamp}.{choice}"

    if choice == "txt":
        with open(filename, "w") as f:
            f.write("Stock Portfolio Summary\n")
            f.write(f"Generated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
            f.write("=" * 40 + "\n")
            for item in portfolio:
                f.write(f"{item['symbol']:<6} | Qty: {item['quantity']:<8} | "
                        f"Price: ${item['price']:<8} | Value: ${item['value']:,.2f}\n")
            f.write("-" * 40 + "\n")
            f.write(f"TOTAL INVESTMENT: ${total:,.2f}\n")

    elif choice == "csv":
        with open(filename, "w", newline="") as f:
            writer = csv.writer(f)
            writer.writerow(["Symbol", "Quantity", "Price", "Value"])
            for item in portfolio:
                writer.writerow([item["symbol"], item["quantity"],
                                  item["price"], f"{item['value']:.2f}"])
            writer.writerow([])
            writer.writerow(["", "", "Total", f"{total:.2f}"])

    print(f"Saved to {filename}")


def main():
    print("=== Stock Portfolio Tracker ===")
    show_available_stocks()

    portfolio = get_portfolio_input()
    total = calculate_total(portfolio)

    display_summary(portfolio, total)
    save_to_file(portfolio, total)


if __name__ == "__main__":
    main()

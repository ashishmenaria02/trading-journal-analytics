import pandas as pd
from datetime import datetime

FILENAME = "trades.csv"

def add_trade():
    print("📝 New Trade Entry")
    date = input("Date (YYYY-MM-DD): ")
    instrument = input("Instrument (e.g., BankNifty): ")
    direction = input("Direction (Buy/Sell): ")
    entry_price = float(input("Entry Price: "))
    exit_price = float(input("Exit Price: "))
    quantity = int(input("Quantity: "))
    reason = input("Reason for Trade: ")

    # PnL Calculation
    pnl = (exit_price - entry_price) * quantity if direction.lower() == "buy" else (entry_price - exit_price) * quantity

    data = {
        "Date": [date],
        "Instrument": [instrument],
        "Direction": [direction],
        "Entry": [entry_price],
        "Exit": [exit_price],
        "Qty": [quantity],
        "PnL": [pnl],
        "Reason": [reason]
    }

    df = pd.DataFrame(data)

    try:
        existing = pd.read_csv(FILENAME)
        df = pd.concat([existing, df], ignore_index=True)
    except FileNotFoundError:
        pass  # if no trades.csv yet

    df.to_csv(FILENAME, index=False)
    print(f"✅ Trade Saved! PnL: ₹{pnl}")

if __name__ == "__main__":
    add_trade()

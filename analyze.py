import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("trades.csv")

total_trades = len(df)
winning_trades = df[df['PnL'] > 0]
losing_trades = df[df['PnL'] < 0]
total_pnl = df['PnL'].sum()
avg_win = winning_trades['PnL'].mean() if not winning_trades.empty else 0
avg_loss = losing_trades['PnL'].mean() if not losing_trades.empty else 0
win_rate = (len(winning_trades) / total_trades) * 100 if total_trades > 0 else 0

print("📊 Trading Journal Analytics")
print(f"Total Trades: {total_trades}")
print(f"Win Rate: {win_rate:.2f}%")
print(f"Total Profit/Loss: ₹{total_pnl:.2f}")
print(f"Average Winning Trade: ₹{avg_win:.2f}")
print(f"Average Losing Trade: ₹{avg_loss:.2f}")

# Optional: Profit/Loss chart
df['PnL'].plot(kind='bar', title='PnL per Trade', color=['green' if x > 0 else 'red' for x in df['PnL']])
plt.xlabel('Trade #')
plt.ylabel('PnL (₹)')
plt.tight_layout()
plt.show()

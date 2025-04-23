import pandas as pd
import os
from datetime import datetime

def update_coin_profits():
    log_file = "trade_log.csv"
    output_file = "coin_profits.csv"

    if not os.path.exists(log_file):
        print("📭 No trade log yet. Skipping profit update.")
        return

    df = pd.read_csv(log_file)
    if df.empty:
        print("📭 Trade log is empty. Skipping profit update.")
        return


    df['price'] = pd.to_numeric(df['price'], errors='coerce')
    df['volume'] = pd.to_numeric(df['volume'], errors='coerce')

    profits = df.groupby('pair').apply(
        lambda g: pd.Series({
            'amount_spent': (g['price'] * g['volume']).sum(),
            'volume': g['volume'].sum(),
            'avg_price_paid': (g['price'] * g['volume']).sum() / g['volume'].sum() if g['volume'].sum() else 0
        })
    ).reset_index()

    profits.to_csv(output_file, index=False)
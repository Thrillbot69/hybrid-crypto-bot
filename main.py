import json
import time
import os
from datetime import datetime
import pandas as pd
from dotenv import load_dotenv

from coin_profit_tracker import update_coin_profits

# Load .env
load_dotenv()

# Optional: Replace with actual logic from rsi_bot and scalper_bot
def execute_rsi_strategy(coin, settings):
    print(f"📈 Executing RSI strategy for {coin}...")
    time.sleep(0.1)  # Placeholder

def execute_scalper_strategy(coin, settings):
    print(f"⚡ Executing Scalper strategy for {coin}...")
    time.sleep(0.1)  # Placeholder

def load_strategy_config():
    with open("config.json", "r") as f:
        return json.load(f)

def run_bot():
    config = load_strategy_config()
    print("🤖 Running Hybrid Bot...")
    for coin, settings in config.items():
        strategy = settings["strategy"]
        print(f"⏳ {coin} - {strategy} mode")
        if strategy == "RSI":
            execute_rsi_strategy(coin, settings)
        elif strategy == "Scalper":
            execute_scalper_strategy(coin, settings)
        else:
            print(f"⚠️ Unknown strategy for {coin}")
    print("✅ Cycle complete. Sleeping for 60 seconds...\n")

if __name__ == "__main__":
    while True:
        run_bot()
        update_coin_profits()
        time.sleep(60)
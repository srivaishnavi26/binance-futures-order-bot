import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import argparse
from src.market_orders import place_market_order
from src.limit_orders import place_limit_order
from src.advanced.stop_limit import place_stop_limit_order
from src.advanced.oco import place_oco_order
from src.advanced.twap import place_twap_order
from src.advanced.grid_strategy import run_grid

parser = argparse.ArgumentParser(description="Binance Futures Trading Bot CLI")

parser.add_argument("order_type", help="MARKET / LIMIT / STOP-LIMIT / OCO / TWAP / GRID")
parser.add_argument("symbol", help="Trading pair e.g. BTCUSDT")
parser.add_argument("side", help="BUY or SELL")
parser.add_argument("quantity", help="Order quantity")

args = parser.parse_args()

order_type = args.order_type.upper()

if order_type == "MARKET":
    place_market_order(args.symbol, args.side, args.quantity)

elif order_type == "LIMIT":
    price = input("Enter Limit Price: ")
    place_limit_order(args.symbol, args.side, args.quantity, price)

elif order_type == "STOP-LIMIT":
    stop_price = input("Enter Stop Price: ")
    limit_price = input("Enter Limit Price: ")
    place_stop_limit_order(args.symbol, args.side, args.quantity, stop_price, limit_price)

elif order_type == "OCO":
    take_profit = input("Enter Take Profit Price: ")
    stop_loss = input("Enter Stop Loss Price: ")
    place_oco_order(args.symbol, args.side, args.quantity, take_profit, stop_loss)

elif order_type == "TWAP":
    chunks = input("Enter number of chunks: ")
    delay = input("Delay between chunks (seconds): ")
    place_twap_order(args.symbol, args.side, args.quantity, chunks, delay)

elif order_type == "GRID":
    lower = input("Enter Lower Price: ")
    upper = input("Enter Upper Price: ")
    grids = input("Enter number of grid levels: ")
    run_grid(args.symbol, args.side, args.quantity, lower, upper, grids)


else:
    print(f"Order type '{args.order_type}' not supported yet.")

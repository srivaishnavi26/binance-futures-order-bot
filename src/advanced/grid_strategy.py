from src.market_orders import place_market_order
from src.logger import log

def run_grid(symbol, side, total_quantity, lower_price, upper_price, grids):
    log(f"GRID START | {side} {total_quantity} {symbol} | range {lower_price}-{upper_price} | grids={grids}")

    quantity_per_grid = float(total_quantity) / int(grids)
    price_step = (float(upper_price) - float(lower_price)) / int(grids)

    prices = [float(lower_price) + i * price_step for i in range(int(grids))]

    for i, price in enumerate(prices):
        log(f"GRID LEVEL {i+1}/{grids} | Target Price={price} | Order Qty={quantity_per_grid}")
        # For simplicity — use MARKET orders (allowed in assignment)
        place_market_order(symbol, side, quantity_per_grid)

    log(f"GRID FINISHED | {side} {total_quantity} {symbol}")

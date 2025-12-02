import time
from src.market_orders import place_market_order
from src.logger import log

def place_twap_order(symbol, side, total_quantity, chunks, delay):
    qty_per_order = float(total_quantity) / int(chunks)

    log(f"TWAP START | {side} {total_quantity} {symbol} | {chunks} chunks | delay={delay}s")

    for i in range(int(chunks)):
        place_market_order(symbol, side, qty_per_order)
        log(f"TWAP EXECUTED CHUNK {i+1}/{chunks} | {side} {qty_per_order} {symbol}")

        if i < int(chunks) - 1:   # skip waiting after last chunk
            time.sleep(int(delay))

    log(f"TWAP FINISHED | {side} {total_quantity} {symbol}")

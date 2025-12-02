from src.client import get_client
from src.logger import log

client = get_client()

def place_market_order(symbol, side, quantity):
    try:
        order = client.futures_create_order(
            symbol=symbol,
            side=side.upper(),
            type="MARKET",
            quantity=float(quantity),
        )
        log(f"MARKET ORDER SUCCESS | {side} {quantity} {symbol} | OrderId: {order['orderId']}")
        return order

    except Exception as e:
        log(f"MARKET ORDER FAILED | {side} {quantity} {symbol} | Error: {str(e)}")
        return None

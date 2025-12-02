from src.client import get_client
from src.logger import log

client = get_client()

def place_stop_limit_order(symbol, side, quantity, stop_price, limit_price):
    try:
        order = client.futures_create_order(
            symbol=symbol,
            side=side.upper(),
            type="STOP",
            stopPrice=float(stop_price),
            price=float(limit_price),
            timeInForce="GTC",
            quantity=float(quantity)
        )
        log(f"STOP-LIMIT SUCCESS | {side} {quantity} {symbol} | Stop={stop_price} Limit={limit_price} | OrderId: {order['orderId']}")
        return order

    except Exception as e:
        log(f"STOP-LIMIT FAILED | {side} {quantity} {symbol} | Stop={stop_price} Limit={limit_price} | Error: {str(e)}")
        return None

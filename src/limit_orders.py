from src.client import get_client
from src.logger import log

client = get_client()

def place_limit_order(symbol, side, quantity, price):
    try:
        order = client.futures_create_order(
            symbol=symbol,
            side=side.upper(),
            type="LIMIT",
            timeInForce="GTC",  # Good-Til-Cancelled
            quantity=float(quantity),
            price=float(price)
        )
        log(f"LIMIT ORDER SUCCESS | {side} {quantity} {symbol} @ {price} | OrderId: {order['orderId']}")
        return order

    except Exception as e:
        log(f"LIMIT ORDER FAILED | {side} {quantity} {symbol} @ {price} | Error: {str(e)}")
        return None

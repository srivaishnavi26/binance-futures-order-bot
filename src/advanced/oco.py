from src.client import get_client
from src.logger import log

client = get_client()

def place_oco_order(symbol, side, quantity, take_profit_price, stop_loss_price):
    try:
        # Take profit
        tp = client.futures_create_order(
            symbol=symbol,
            side=side.upper(),
            type="TAKE_PROFIT_MARKET",
            stopPrice=float(take_profit_price),
            quantity=float(quantity)
        )

        # Stop loss
        sl = client.futures_create_order(
            symbol=symbol,
            side=side.upper(),
            type="STOP_MARKET",
            stopPrice=float(stop_loss_price),
            quantity=float(quantity)
        )

        log(f"OCO SUCCESS | {side} {quantity} {symbol} | TP={take_profit_price} SL={stop_loss_price} | TPid={tp['orderId']} SLid={sl['orderId']}")
        return tp, sl

    except Exception as e:
        log(f"OCO FAILED | {side} {quantity} {symbol} | TP={take_profit_price} SL={stop_loss_price} | Error: {str(e)}")
        return None

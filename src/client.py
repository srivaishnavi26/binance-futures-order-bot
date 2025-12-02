import os
from dotenv import load_dotenv
from binance.client import Client

# Load .env file
load_dotenv()

def get_client():
    api_key = os.getenv("BINANCE_API_KEY")
    api_secret = os.getenv("BINANCE_API_SECRET")

    if not api_key or not api_secret:
        raise Exception("Missing Binance API keys. Please add them to .env file.")

    # Use TESTNET for safety
    client = Client(api_key, api_secret, testnet=True)
    return client

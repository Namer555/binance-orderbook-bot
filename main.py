import time
from binance.client import Client
from binance.enums import *

api_key = "YOUR_API_KEY"
api_secret = "YOUR_API_SECRET"

client = Client(api_key, api_secret)

symbol = "BTCUSDT"

def get_order_book(symbol):
    depth = client.get_order_book(symbol=symbol, limit=100)
    bids = depth['bids']
    asks = depth['asks']
    highest_bid = max(bids, key=lambda x: float(x[1]))
    highest_ask = max(asks, key=lambda x: float(x[1]))
    return float(highest_bid[0]), float(highest_ask[0])

while True:
    bid, ask = get_order_book(symbol)
    print(f"Highest BID: {bid}, Highest ASK: {ask}")
    time.sleep(2)

import json
import time

import requests
from exchange_pairs.utils import CompareToken as ct, GetTokens as gt


def get_hitbtc_depth(symbol):
    url = f"https://api.hitbtc.com/api/2/public/orderbook/{symbol}"
    statuscode = 0
    while statuscode != 200:
        response = 0
        try:
            response = requests.get(url=url)
        except (
                requests.ConnectionError,
                requests.exceptions.ReadTimeout,
                requests.exceptions.Timeout,
                requests.exceptions.ConnectTimeout,
        ) as e:
            time.sleep(1)
            statuscode = 0
            print(e)
        if response:
            statuscode = response.status_code
    return json.loads(response.content)


def init():
    all_compared_tokens = gt(module='all', _all=True).tokens()
    for token in all_compared_tokens:
        print(token)
    print(len(all_compared_tokens))
    symbols = ['OPTBTC']
    depth = get_hitbtc_depth(symbols[0])
    asks = []
    for ask in depth['ask']:
        asks.append([ask['price'], ask['size']])
    print(asks)
    compare = ct(buy_from='hitbtc', buy_symbol='PLRBTC', buy_prices=asks, buy_volume=0,
                 sell_to='uniswap', sell_symbol='OPT', sell_prices=0.00235603, sell_volume=1,
                 contract='0x4fe5851c9af07df9e5ad8217afae1ea72737ebda', profit_percent=1,
                 currency=0.031639).compare()
    print(compare)


if __name__ == '__main__':
    init()

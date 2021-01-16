import json

import requests

from .models import Hotbit

API_URL = 'https://api.hotbit.io/api/v1/allticker'

prices = []


def set_prices(token, symbol, buy, sell, volume):
    prices.append({token: [symbol, buy, sell, volume]})


def get_eth_btc(token, limit):
    response = requests.get(f'https://api.hotbit.io/api/v1/order.depth?market={token}&limit={limit}&interval=1e-8')
    asks = json.loads(response.content)['result']['asks']
    bids = json.loads(response.content)['result']['bids']
    all_ask = 0
    for ask in asks:
        # print(ask[0], ask[1])
        all_ask += float(ask[0])

    all_bid = 0
    for bid in bids:
        # print(bid[0], bid[1])
        all_bid += float(bid[0])
    return 1 / (all_ask / len(asks)), 1 / (all_bid / len(bids))


def get_ticker():
    currency = get_eth_btc('ETH/BTC', 20)
    ask_btc = currency[0]
    bit_btc = currency[1]
    token = ''
    response = requests.get(url=API_URL)
    jData = sorted(json.loads(response.content)['ticker'], key=lambda x: x['symbol'], reverse=False)
    for data in jData:
        if 'USDT' not in data['symbol']:
            buy = float(data['buy'])
            sell = float(data['sell'])
            volume = float(data['vol'])
            token = data['symbol'].replace('_ETH', '').replace('_BTC', '')
            if (buy > 0 or sell > 0) and volume > 0:
                if 'BTC' in data['symbol'] and 'ETH' not in data['symbol']:
                    buy = buy * ask_btc
                    sell = sell * ask_btc
                    set_prices(token, data['symbol'].replace('_BTC', '') + '/BTC', buy, sell, volume)
                else:
                    set_prices(token, data['symbol'].replace('_ETH', '') + '/ETH', buy, sell, volume)


def currencies_update(token, symbol, buy, sell, volume):
    pair_id = Hotbit.objects.filter(symbol=symbol).values('id')
    if len(pair_id) > 0:
        Hotbit.objects.filter(id=pair_id[0]['id']).update(exch_direction=token, symbol=symbol, buy=buy, sell=sell,
                                                          volume=volume)
    else:
        pair = Hotbit(exch_direction=token, symbol=symbol, buy=buy, sell=sell, volume=volume, is_active=True)
        pair.save()


def set_currencies():
    get_ticker()
    for price in prices:
        token = list(price.keys())[0]
        p = list(list(price.values()))[0]
        currencies_update(token, p[0], p[1], p[2], p[3])


# set_currencies()

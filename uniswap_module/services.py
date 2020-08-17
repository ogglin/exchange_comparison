import requests
import json

from .models import Uniswap

koef = 0.99


def currencies_update(direction, lowest_ask, highest_bid):
    pair_id = Uniswap.objects.filter(exch_direction=direction).values('id')
    if len(pair_id) > 0:
        pair = Uniswap(id=pair_id[0]['id'], exch_direction=direction, lowest_ask=lowest_ask, highest_bid=highest_bid)
    else:
        pair = Uniswap(exch_direction=direction, lowest_ask=lowest_ask, highest_bid=highest_bid)
    pair.save()


def set_currencies():
    url = 'https://api.kyber.network/market'
    # response = requests.get(url=url, proxies=proxies)
    response = requests.get(url=url)
    jData = json.loads(response.content)['data']
    print(jData)
    for data in jData:
        direction = data['pair']
        highest_bid = data['current_bid']
        lowest_ask = data['current_ask']
        print(direction)
        print(highest_bid)
        print(lowest_ask)
        currencies_update(direction, lowest_ask, highest_bid)


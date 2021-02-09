import requests
import json

from .models import Kyber

koef = 0.99


def currencies_update(direction, lowest_ask, highest_bid, token_id, volume):
    pair_id = Kyber.objects.filter(exch_direction=direction).values('id')
    if len(pair_id) > 0:
        Kyber.objects.filter(id=pair_id[0]['id']).update(lowest_ask=lowest_ask, highest_bid=highest_bid,
                                                         token_id=token_id, volume=volume)
    else:
        pair = Kyber(exch_direction=direction, lowest_ask=lowest_ask, highest_bid=highest_bid,
                     token_id=token_id, volume=volume, is_active=True)
        pair.save()


def set_currencies():
    url = 'https://api.kyber.network/market'
    # response = requests.get(url=url, proxies=proxies)
    response = requests.get(url=url)
    jData = json.loads(response.content)['data']
    Kyber.objects.all().update(volume=0)
    for data in jData:
        direction = data['pair'].replace('ETH_', '')
        highest_bid = data['current_bid']
        lowest_ask = data['current_ask']
        token_id = data['base_address']
        volume = float(data['eth_24h_volume'])
        if volume > 0:
            currencies_update(direction, lowest_ask, highest_bid, token_id, volume)

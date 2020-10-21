import json

import requests

from .models import *


def currencies_update(token_pair, ask, bid):
    print(token_pair, ask, bid)
    pair_id = Idex.objects.filter(exch_direction=token_pair).values('id')
    if len(pair_id) > 0:
        Idex.objects.filter(id=pair_id[0]['id']).update(exch_direction=token_pair, lowest_ask=ask, highest_bid=bid)
    else:
        pair = Idex(exch_direction=token_pair, lowest_ask=ask, highest_bid=bid, is_active=True)
        pair.save()


def set_currencies():
    ask = 0
    bid = 0
    url = 'https://api.idex.io/v1/tickers'
    response = requests.get(url=url)
    jData = json.loads(response.content)
    for data in jData:
        token_pair = data['market'].replace('ETH', '').replace('-', '')
        if data['ask']:
            ask = data['ask']
        if data['bid']:
            bid = data['bid']
        currencies_update(token_pair, ask, bid)


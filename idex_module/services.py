import datetime
import json

import requests

from .models import *


def currencies_update(token_pair, ask, bid, volume):
    # print(token_pair, ask, bid, volume)
    pair_id = Idex.objects.filter(exch_direction=token_pair).values('id')
    if len(pair_id) > 0:
        Idex.objects.filter(id=pair_id[0]['id']).update(lowest_ask=ask, highest_bid=bid, volume=volume)
    else:
        pair = Idex(exch_direction=token_pair, lowest_ask=ask, highest_bid=bid, is_active=True, volume=volume)
        pair.save()


def set_currencies():
    # print('start idex: ' + str(datetime.datetime.now()))
    url = 'https://api.idex.io/v1/tickers'
    response = requests.get(url=url)
    jData = json.loads(response.content)
    Idex.objects.all().update(volume=0)
    for data in jData:
        ask = 0
        bid = 0
        token_pair = data['market'].replace('ETH', '').replace('-', '')
        if data['ask']:
            ask = data['ask']
        if data['bid']:
            bid = data['bid']
        volume = float(data['quoteVolume'])
        if volume > 0:
            currencies_update(token_pair, ask, bid, volume)
    # print('end idex: ' + str(datetime.datetime.now()))


def idex_init():
    while True:
        set_currencies()

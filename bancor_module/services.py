import requests
import json

from .models import Bancor

koef = 0.99


def currencies_update(direction, lowest_ask, highest_bid, name, link_id):
    pair_id = Bancor.objects.filter(exch_direction=direction).values('id')
    if len(pair_id) > 0:
        pair = Bancor(id=pair_id[0]['id'], exch_direction=direction, lowest_ask=lowest_ask, highest_bid=highest_bid,
                      name=name, link_id=link_id)
    else:
        pair = Bancor(exch_direction=direction, lowest_ask=lowest_ask, highest_bid=highest_bid, name=name,
                      link_id=link_id)
    pair.save()


def set_currencies():
    proxies = {
        'http': '46.102.73.244:53281',
        'https': '199.91.203.210:3128'
    }
    url = 'https://api.bancor.network/0.1/currencies/tokens?limit=9999&skip=0&fromCurrencyCode=ETH&includeTotal=true&orderBy=code&sortOrder=asc&skip=0'
    # response = requests.get(url=url, proxies=proxies)
    response = requests.get(url=url)
    jData = json.loads(response.content)['data']['page']
    for data in jData:
        direction = data['code']
        highest_bid = data['price']
        lowest_ask = data['price'] * koef
        name = data['name']
        link_id = data['id']
        print(direction)
        print(highest_bid)
        print(lowest_ask)
        print(name)
        print(link_id)
        print('/********************/')



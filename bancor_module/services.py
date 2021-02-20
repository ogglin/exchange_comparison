import datetime
import json

import requests
from asgiref.sync import sync_to_async

from .models import Bancor

koef = 0.99


def currencies_update(direction, lowest_ask, highest_bid, name, link_id, volume):
    pair_id = Bancor.objects.filter(exch_direction=direction).values('id')
    if len(pair_id) > 0:
        Bancor.objects.filter(id=pair_id[0]['id']).update(lowest_ask=lowest_ask, volume=volume,
                                                          highest_bid=highest_bid, name=name, link_id=link_id)
    else:
        pair = Bancor(exch_direction=direction, lowest_ask=lowest_ask, highest_bid=highest_bid, name=name,
                      volume=volume, link_id=link_id, is_active=True)
        pair.save()


@sync_to_async
def set_currencies():
    proxies = {
        'http': '87.76.35.86:35782',
        'https': '162.144.37.206:3838'
    }
    url = 'https://api.bancor.network/0.1/currencies/tokens?limit=9999&skip=0&fromCurrencyCode=ETH&includeTotal=true&orderBy=code&sortOrder=asc&skip=0'
    # response = requests.get(url=url, proxies=proxies)
    try:
        response = requests.get(url=url)
        jData = json.loads(response.content)['data']['page']
        Bancor.objects.all().update(volume=0)
        for data in jData:
            if data['price'] is not None:
                direction = data['code']
                highest_bid = data['price'] * koef
                lowest_ask = data['price']
                name = data['name']
                link_id = data['id']
                volume = float(data['liquidityDepth'])
                if volume > 0:
                    currencies_update(direction, lowest_ask, highest_bid, name, link_id, volume)
    except:
        pass


async def bankor_init():
    print('start bankor: ' + str(datetime.datetime.now()))
    while True:
        await set_currencies()
        # print('end bankor: ' + str(datetime.datetime.now()))

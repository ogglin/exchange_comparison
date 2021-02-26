import datetime
import json
import time

import requests
from asgiref.sync import sync_to_async

from .models import *

idex_tikers_set = []


@sync_to_async
def tikers_set_idex():
    # print('start idex tickers: ' + str(datetime.datetime.now()))
    global idex_tikers_set
    url = 'https://api.idex.io/v1/tickers'
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
    jData = json.loads(response.content)
    if len(idex_tikers_set) == 0:
        for data in jData:
            ask = 0
            bid = 0
            token = data['market'].replace('ETH', '').replace('-', '')
            if data['ask']:
                ask = float(data['ask'])
            if data['bid']:
                bid = float(data['bid'])
            volume = float(data['quoteVolume'])
            idex_tikers_set.append({'token': token, 'ask': ask, 'bid': bid, 'volume': volume})
    else:
        for data in jData:
            ask = 0
            bid = 0
            token = data['market'].replace('ETH', '').replace('-', '')
            if data['ask']:
                ask = float(data['ask'])
            if data['bid']:
                bid = float(data['bid'])
            volume = float(data['quoteVolume'])
            for i, tiker in enumerate(idex_tikers_set):
                if tiker['token'] == token:
                    idex_tikers_set[i]['ask'] = ask
                    idex_tikers_set[i]['bid'] = bid
                    idex_tikers_set[i]['volume'] = volume

    # print('end idex tickers: ' + str(datetime.datetime.now()))


@sync_to_async
def currencies_update():
    # print('start idex currency update: ' + str(datetime.datetime.now()))
    update_list = []
    objs = Idex.objects.all().order_by('id')
    for data in idex_tikers_set:
        obj = objs.get(exch_direction=data['token'])
        if obj:
            obj.lowest_ask = data['ask']
            obj.highest_bid = data['bid']
            obj.volume = data['volume']
            update_list.append(obj)
        else:
            pair = Idex(exch_direction=data['token'], lowest_ask=data['ask'], highest_bid=data['bid'], is_active=True,
                        volume=data['volume'])
            pair.save()
    Idex.objects.bulk_update(update_list, ['lowest_ask', 'highest_bid', 'volume'])
    # print('end idex currency update: ' + str(datetime.datetime.now()))


async def tikers_set_idex_init():
    while True:
        await tikers_set_idex()


async def idex_init():
    print('start idex_init: ' + str(datetime.datetime.now()))
    while True:
        await currencies_update()
    # print('end idex: ' + str(datetime.datetime.now()))

# idex_init()

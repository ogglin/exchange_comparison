import datetime
import json

import requests
from asgiref.sync import sync_to_async

from exchange_pairs.models import TrustedPairs
import exchange_pairs.services as exch_serv
from .models import Uniswap, UniswapOne

koef = 0.99


def currencies_update_v1(direction, lowest_ask, highest_bid, tokenid, volume):
    pair_id = UniswapOne.objects.filter(tokenid__icontains=tokenid).values('id')
    if len(pair_id) > 0:
        UniswapOne.objects.filter(id=pair_id[0]['id']).update(exch_direction=direction, lowest_ask=lowest_ask,
                                                              volume=volume, highest_bid=highest_bid, tokenid=tokenid)
    else:
        pair = UniswapOne(exch_direction=direction, lowest_ask=lowest_ask, highest_bid=highest_bid, is_active=True,
                          volume=volume, tokenid=tokenid)
        pair.save()


@sync_to_async
def currencies_update_v2():
    update_list = []
    objs = Uniswap.objects.all().order_by('id')
    if len(exch_serv.uniswap_prices_set) > 0:
        print('start currencies_update_v2: ' + str(datetime.datetime.now()))
        for data in exch_serv.uniswap_prices_set:
            try:
                obj = objs.get(tokenid__icontains=data[1])
                obj.lowest_ask = data[5]
                obj.highest_bid = data[4]
                obj.volume = data[6]
                update_list.append(obj)
            except:
                pair = Uniswap(exch_direction=data[3], lowest_ask=data[5], highest_bid=data[4],
                               is_active=True, volume=data[6], tokenid=data[1])
                pair.save()
        Uniswap.objects.bulk_update(update_list, ['lowest_ask', 'highest_bid', 'volume'])
        print('end currencies_update_v2: ' + str(datetime.datetime.now()))


@sync_to_async
def get_uni_1():
    trusted_tokens = TrustedPairs.objects.all().values()
    url_v1 = 'https://api.thegraph.com/subgraphs/name/graphprotocol/uniswap'
    UniswapOne.objects.all().update(volume=0)
    for i in range(5):
        req_v1 = f'''
                    {{"query":"{{exchanges(first: 1000, skip: {i * 1000}) {{ ethBalance ethLiquidity tokenAddress price tokenName tokenSymbol}}}}","variables":{{}}}}
                '''
        try:
            response = requests.post(url=url_v1, data=req_v1)
            jData = json.loads(response.content)['data']
            for data in jData['exchanges']:
                if float(data['ethLiquidity']) > 0 and float(data['ethBalance']) > 1:
                    direction = data['tokenSymbol']
                    lowest_ask = 1.003 / float(data['price'])
                    highest_bid = lowest_ask * koef
                    tokenid = data['tokenAddress']
                    volume = float(data['ethBalance'])
                    if volume > 0:
                        for row in trusted_tokens:
                            if row['token'].lower() == direction.lower() and row['contract'].lower() == tokenid.lower():
                                currencies_update_v1(direction, lowest_ask, highest_bid, tokenid, volume)
        except:
            pass


async def uniswap_v1_init():
    print('start uniswap_v1: ' + str(datetime.datetime.now()))
    while True:
        await get_uni_1()
        # print('end uniswap_v1: ' + str(datetime.datetime.now()))


async def uniswap_v2_init():
    print('start uniswap_v2: ' + str(datetime.datetime.now()))
    while True:
        await currencies_update_v2()
        # print('end uniswap_v2: ' + str(datetime.datetime.now()))
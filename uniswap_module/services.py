import datetime
import json

import requests
from asgiref.sync import sync_to_async

from exchange_pairs.models import TrustedPairs
from .models import Uniswap, UniswapOne

koef = 0.99


def currencies_update_v1(direction, lowest_ask, highest_bid, tokenid, volume):
    pair_id = UniswapOne.objects.filter(tokenid=tokenid).values('id')
    if len(pair_id) > 0:
        UniswapOne.objects.filter(id=pair_id[0]['id']).update(exch_direction=direction, lowest_ask=lowest_ask,
                                                              volume=volume, highest_bid=highest_bid, tokenid=tokenid)
    else:
        pair = UniswapOne(exch_direction=direction, lowest_ask=lowest_ask, highest_bid=highest_bid, is_active=True,
                          volume=volume, tokenid=tokenid)
        pair.save()


def currencies_update_v2(direction, lowest_ask, highest_bid, tokenid, volume):
    pair_id = Uniswap.objects.filter(tokenid=tokenid).values('id')
    if len(pair_id) > 0:
        Uniswap.objects.filter(id=pair_id[0]['id']).update(exch_direction=direction, lowest_ask=lowest_ask,
                                                           volume=volume, highest_bid=highest_bid, tokenid=tokenid)
    else:
        pair = Uniswap(exch_direction=direction, lowest_ask=lowest_ask, highest_bid=highest_bid, is_active=True,
                       volume=volume, tokenid=tokenid)
        pair.save()


@sync_to_async
def get_uni_1():
    trusted_tokens = TrustedPairs.objects.all().values()
    url_v1 = 'https://api.thegraph.com/subgraphs/name/graphprotocol/uniswap'
    # uni_one_res = []
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
                                # print(direction, lowest_ask, highest_bid, tokenid, volume)
                                # uni_one_res.append({direction, lowest_ask, highest_bid, tokenid, volume})
                                currencies_update_v1(direction, lowest_ask, highest_bid, tokenid, volume)
        except:
            pass


@sync_to_async
def get_uni_2():
    # token_uni2 = Uniswap.objects.all().values()
    trusted_tokens = TrustedPairs.objects.filter(contract__isnull=False, is_active=True).values()
    url_v2 = 'https://api.thegraph.com/subgraphs/name/uniswap/uniswap-v2'
    for token in trusted_tokens:
        tokenid = token['contract'].lower()
        token = token['token']
        req = {'query': '{token(id: "' + tokenid + '"){ symbol totalLiquidity derivedETH } }'}
        try:
            response = requests.post(url=url_v2, data=json.dumps(req))
            jData = json.loads(response.content)['data']['token']
            if jData is not None and jData['totalLiquidity'] is not None and jData['derivedETH'] is not None:
                highest_bid = float(jData['derivedETH']) * koef
                lowest_ask = float(jData['derivedETH'])
                volume = float(jData['totalLiquidity'])
                currencies_update_v2(token, lowest_ask, highest_bid, tokenid, volume)
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
        await get_uni_2()
        # print('end uniswap_v2: ' + str(datetime.datetime.now()))

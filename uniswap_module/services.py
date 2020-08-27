import requests
import json

from .models import Uniswap, UniswapOne

koef = 0.99


def currencies_update_v1(direction, lowest_ask, highest_bid, tokenid):
    pair_id = UniswapOne.objects.filter(exch_direction=direction).values('id')
    if len(pair_id) > 0:
        pair = UniswapOne(id=pair_id[0]['id'], exch_direction=direction, lowest_ask=lowest_ask, highest_bid=highest_bid)
    else:
        pair = UniswapOne(exch_direction=direction, lowest_ask=lowest_ask, highest_bid=highest_bid, is_active=True, tokenid=tokenid)
    pair.save()


def currencies_update_v2(direction, lowest_ask, highest_bid, tokenid):
    pair_id = Uniswap.objects.filter(exch_direction=direction).values('id')
    if len(pair_id) > 0:
        pair = Uniswap(id=pair_id[0]['id'], exch_direction=direction, lowest_ask=lowest_ask, highest_bid=highest_bid)
    else:
        pair = Uniswap(exch_direction=direction, lowest_ask=lowest_ask, highest_bid=highest_bid, is_active=True, tokenid=tokenid)
    pair.save()


# req_v2 = f'''
# {{"query":"{{ pairs(first: 1000, skip: {page * 1000}) {{token0Price token1Price token0 {{id symbol name derivedETH tradeVolume}} token1 {{id symbol name derivedETH tradeVolume}} }} }}","variables":{{}}}}
# '''


def set_currencies_v1(date):
    url_v1 = 'https://api.thegraph.com/subgraphs/name/graphprotocol/uniswap'
    response = requests.post(url=url_v1, data=date)
    jData = json.loads(response.content)['data']
    for data in jData['exchanges']:
        if float(data['ethLiquidity']) > 0 and float(data['ethBalance']) > 1:
            direction = data['tokenSymbol']
            lowest_ask = 1.003 / float(data['price'])
            highest_bid = lowest_ask * koef
            tokenid = data['tokenAddress']
            currencies_update_v1(direction, lowest_ask, highest_bid, tokenid)


def set_currencies_v2(date):
    # proxies = {
    #     'http': '46.102.73.244:53281',
    #     'https': '199.91.203.210:3128'
    # }
    url_v2 = 'https://api.thegraph.com/subgraphs/name/uniswap/uniswap-v2'
    # response = requests.post(url=url_v2, data=req_v2, proxies=proxies)
    response = requests.post(url=url_v2, data=date)
    jData = json.loads(response.content)['data']
    for data in jData['tokens']:
        if float(data['derivedETH']) > 0:
            direction = data['symbol']
            highest_bid = float(data['derivedETH']) * koef
            lowest_ask = float(data['derivedETH'])
            tokenid = data['id']
            currencies_update_v2(direction, lowest_ask, highest_bid, tokenid)


def set_all_currencies():
    pages_v1 = 4
    pages_v2 = 6
    for i in range(pages_v2):
        req_v2 = f'''
            {{"query":"{{ tokens (first: 1000, skip: {i * 1000}) {{ id derivedETH symbol name totalLiquidity tradeVolume }} }}","variables":{{}}}}
        '''
        set_currencies_v2(req_v2)

    for i in range(pages_v1):
        req_v1 = f'''
            {{"query":"{{exchanges(first: 1000, skip: {i * 1000}) {{ ethBalance ethLiquidity tokenAddress price tokenName tokenSymbol}}}}","variables":{{}}}}
        '''
        set_currencies_v1(req_v1)



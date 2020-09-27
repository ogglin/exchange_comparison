import json

import requests

from exchange_pairs.models import TrustedPairs, CustomSql
from .models import Uniswap, UniswapOne

koef = 0.99


def currencies_update_v1(direction, lowest_ask, highest_bid, tokenid):
    pair_id = UniswapOne.objects.filter(exch_direction=direction).values('id')
    if len(pair_id) > 0:
        UniswapOne.objects.filter(id=pair_id[0]['id']).update(exch_direction=direction, lowest_ask=lowest_ask,
                                                              highest_bid=highest_bid, tokenid=tokenid)
    else:
        pair = UniswapOne(exch_direction=direction, lowest_ask=lowest_ask, highest_bid=highest_bid, is_active=True,
                          tokenid=tokenid)
        pair.save()


def currencies_update_v2(direction, lowest_ask, highest_bid, tokenid):
    pair_id = Uniswap.objects.filter(exch_direction=direction).values('id')
    if len(pair_id) > 0:
        Uniswap.objects.filter(id=pair_id[0]['id']).update(exch_direction=direction, lowest_ask=lowest_ask,
                                                           highest_bid=highest_bid, tokenid=tokenid)
    else:
        pair = Uniswap(exch_direction=direction, lowest_ask=lowest_ask, highest_bid=highest_bid, is_active=True,
                       tokenid=tokenid)
        pair.save()


def set_currencies_v1(date, trusted_tokens):
    url_v1 = 'https://api.thegraph.com/subgraphs/name/graphprotocol/uniswap'
    response = requests.post(url=url_v1, data=date)
    jData = json.loads(response.content)['data']
    for data in jData['exchanges']:
        if float(data['ethLiquidity']) > 0 and float(data['ethBalance']) > 1:
            direction = data['tokenSymbol']
            lowest_ask = 1.003 / float(data['price'])
            highest_bid = lowest_ask * koef
            tokenid = data['tokenAddress']
            for row in trusted_tokens:
                if row['token'] == direction and row['contract'] == tokenid:
                    currencies_update_v1(direction, lowest_ask, highest_bid, tokenid)


def set_currencies_v2(date, trusted_tokens):
    # proxies = {
    #     'http': '46.102.73.244:53281',
    #     'https': '199.91.203.210:3128'
    # }
    url_v2 = 'https://api.thegraph.com/subgraphs/name/uniswap/uniswap-v2'
    # response = requests.post(url=url_v2, data=date, proxies=proxies)
    response = requests.post(url=url_v2, data=date)
    print(json.loads(response.content)['data'])
    jData = json.loads(response.content)['data']
    # for data in jData['tokens']:
    #     if data['totalLiquidity'] is not None:
    #         if float(data['derivedETH']) > 0 and float(data['totalLiquidity']) > 1:
    #             direction = data['symbol']
    #             highest_bid = float(data['derivedETH']) * koef
    #             lowest_ask = float(data['derivedETH'])
    #             tokenid = data['id']
    #             for row in trusted_tokens:
    #                 if row['token'] == direction and row['contract'] == tokenid:
    #                     currencies_update_v2(direction, lowest_ask, highest_bid, tokenid)


def set_all_currencies():
    trusted_tokens = TrustedPairs.objects.all().values()
    # trusted_tokens = []
    pages_v1 = 4
    pages_v2 = 8
    for i in range(pages_v2):
        req_v2 = f'''
            {{"query":"{{ tokens (first: 1000, skip: {i * 1000}) {{ id derivedETH symbol name totalLiquidity tradeVolume }} }}","variables":{{}}}}
        '''
        set_currencies_v2(req_v2, trusted_tokens)

    for i in range(pages_v1):
        req_v1 = f'''
            {{"query":"{{exchanges(first: 1000, skip: {i * 1000}) {{ ethBalance ethLiquidity tokenAddress price tokenName tokenSymbol}}}}","variables":{{}}}}
        '''
        set_currencies_v1(req_v1, trusted_tokens)
    CustomSql.objects.raw('''
        UPDATE exchange_pairs SET uniswap_direction_id = s.id
        FROM (SELECT mu.id, mu.exch_direction FROM module_uniswap mu
        LEFT JOIN exchange_pairs ep ON replace(ep.exch_direction, 'ETH_', '') = mu.exch_direction) s
        WHERE s.exch_direction = replace(exchange_pairs.exch_direction, 'ETH_', '');

        UPDATE exchange_pairs SET uniswap_one_direction_id = s.id
        FROM (SELECT muo.id, muo.exch_direction FROM module_uniswap_one muo
        LEFT JOIN exchange_pairs ep ON replace(ep.exch_direction, 'ETH_', '') = muo.exch_direction) s
        WHERE s.exch_direction = replace(exchange_pairs.exch_direction, 'ETH_', '');
	''')


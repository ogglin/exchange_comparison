import datetime
import json
import csv
import requests

from exchange_pairs.models import TrustedPairs, CustomSql
from .models import Uniswap, UniswapOne

koef = 0.99


def currencies_update_v1(direction, lowest_ask, highest_bid, tokenid, volume):
    pair_id = UniswapOne.objects.filter(exch_direction=direction).values('id')
    if len(pair_id) > 0:
        UniswapOne.objects.filter(id=pair_id[0]['id']).update(exch_direction=direction, lowest_ask=lowest_ask,
                                                              volume=volume, highest_bid=highest_bid, tokenid=tokenid)
    else:
        pair = UniswapOne(exch_direction=direction, lowest_ask=lowest_ask, highest_bid=highest_bid, is_active=True,
                          volume=volume, tokenid=tokenid)
        pair.save()


def currencies_update_v2(direction, lowest_ask, highest_bid, tokenid, volume):
    pair_id = Uniswap.objects.filter(exch_direction=direction).values('id')
    if len(pair_id) > 0:
        Uniswap.objects.filter(id=pair_id[0]['id']).update(exch_direction=direction, lowest_ask=lowest_ask,
                                                           volume=volume, highest_bid=highest_bid, tokenid=tokenid)
    else:
        pair = Uniswap(exch_direction=direction, lowest_ask=lowest_ask, highest_bid=highest_bid, is_active=True,
                       volume=volume, tokenid=tokenid)
        pair.save()


def set_currencies_v1(date, trusted_tokens):
    url_v1 = 'https://api.thegraph.com/subgraphs/name/graphprotocol/uniswap'
    response = requests.post(url=url_v1, data=date)
    try:
        jData = json.loads(response.content)['data']
        UniswapOne.objects.filter.uptade(volume=0)
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


def set_currencies_v2(date, trusted_tokens):
    # proxies = {
    #     'http': '46.102.73.244:53281',
    #     'https': '199.91.203.210:3128'
    # }
    url_v2 = 'https://api.thegraph.com/subgraphs/name/uniswap/uniswap-v2'
    # response = requests.post(url=url_v2, data=date, proxies=proxies)
    response = requests.post(url=url_v2, data=date)
    try:
        jData = json.loads(response.content)['data']
        Uniswap.objects.filter.uptade(volume=0)
        for data in jData['tokens']:
            if data['totalLiquidity'] is not None:
                if float(data['derivedETH']) > 0 and float(data['totalLiquidity']) > 1:
                    direction = data['symbol']
                    highest_bid = float(data['derivedETH']) * koef
                    lowest_ask = float(data['derivedETH'])
                    tokenid = data['id']
                    volume = float(data['totalLiquidity'])
                    if volume > 0:
                        for row in trusted_tokens:
                            if row['token'].lower() == direction.lower() and row['contract'].lower() == tokenid.lower():
                                currencies_update_v2(direction, lowest_ask, highest_bid, tokenid, volume)
    except:
        pass


def get_uni2_price(tokenid, token):
    url_v2 = 'https://api.thegraph.com/subgraphs/name/uniswap/uniswap-v2'
    req = {'query': '{token(id: "' + tokenid + '"){ symbol totalLiquidity derivedETH } }'}
    response = requests.post(url=url_v2, data=json.dumps(req))
    jData = json.loads(response.content)['data']['token']
    if jData is not None and jData['totalLiquidity'] is not None:
        if float(jData['derivedETH']) > 0 and float(jData['totalLiquidity']) > 1:
            highest_bid = float(jData['derivedETH']) * koef
            lowest_ask = float(jData['derivedETH'])
            volume = float(jData['totalLiquidity'])
            currencies_update_v2(token, lowest_ask, highest_bid, tokenid, volume)


def set_all_currencies():
    trusted_tokens = TrustedPairs.objects.all().values()
    token_uni2 = Uniswap.objects.all().values()
    # token_uni = UniswapOne.objects.all().values()
    # print(token_uni)
    for token in token_uni2:
        get_uni2_price(token['tokenid'].lower(), token['exch_direction'])

    # trusted_tokens = []
    # with open('trusted_pairs.csv', newline='') as File:
    #     reader = csv.reader(File)
    #     for row in reader:
    #         trusted_tokens.append(row)
    # pages_v1 = 5
    # pages_v2 = 19
    # for i in range(pages_v2):
    #     req_v2 = f'''
    #         {{"query":"{{ tokens (first: 1000, skip: {i * 1000}) {{ id derivedETH symbol name totalLiquidity tradeVolume }} }}","variables":{{}}}}
    #     '''
    #     set_currencies_v2(req_v2, trusted_tokens)
    #
    for i in range(5):
        req_v1 = f'''
            {{"query":"{{exchanges(first: 1000, skip: {i * 1000}) {{ ethBalance ethLiquidity tokenAddress price tokenName tokenSymbol}}}}","variables":{{}}}}
        '''
        set_currencies_v1(req_v1, trusted_tokens)
    # CustomSql.objects.raw('''
    #     UPDATE exchange_pairs SET uniswap_direction_id = s.id
    #     FROM (SELECT mu.id, mu.exch_direction FROM module_uniswap mu
    #     LEFT JOIN exchange_pairs ep ON ep.exch_direction = mu.exch_direction) s
    #     WHERE s.exch_direction = exchange_pairs.exch_direction;
    #
    #     UPDATE exchange_pairs SET uniswap_one_direction_id = s.id
    #     FROM (SELECT muo.id, muo.exch_direction FROM module_uniswap_one muo
    #     LEFT JOIN exchange_pairs ep ON ep.exch_direction = muo.exch_direction) s
    #     WHERE s.exch_direction = exchange_pairs.exch_direction;
    #     ''')


# set_all_currencies()
def uniswap_init():
    while True:
        print('start uniswap: ' + str(datetime.datetime.now()))
        set_all_currencies()
        print('end uniswap: ' + str(datetime.datetime.now()))

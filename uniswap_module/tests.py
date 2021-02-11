import json

import requests
from django.test import TestCase

# Create your tests here.

koef = 0.99


def uniswap_v1_init():
    url_v1 = 'https://api.thegraph.com/subgraphs/name/graphprotocol/uniswap'
    for i in range(5):
        print(i)
        req_v1 = f'''
            {{"query":"{{exchanges(first: 1000, skip: {i * 1000}) {{ ethBalance ethLiquidity tokenAddress price tokenName tokenSymbol}}}}","variables":{{}}}}
        '''
        print(req_v1)
        response = requests.post(url=url_v1, data=req_v1)
        try:
            jData = json.loads(response.content)['data']
            for data in jData['exchanges']:
                if float(data['ethLiquidity']) > 0 and float(data['ethBalance']) > 1:
                    direction = data['tokenSymbol']
                    lowest_ask = 1.003 / float(data['price'])
                    highest_bid = lowest_ask * koef
                    tokenid = data['tokenAddress']
                    volume = float(data['ethBalance'])
                    if volume > 0:
                        print(direction, lowest_ask, highest_bid, tokenid, volume)
        except:
            pass


uniswap_v1_init()

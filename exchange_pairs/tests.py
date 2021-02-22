import json

import requests
from django.test import TestCase


# Create your tests here.
from exchange_comparison.utils import _query

def set_new_token():
    # url = 'https://api.hotbit.io/api/v1/asset.list'
    url = 'https://api.1inch.exchange/v2.0/tokens'
    response = requests.get(url=url)
    jData = json.loads(response.content)['tokens']
    for data in jData:
        # print(jData[data])
        token = jData[data]['symbol']
        decimals = jData[data]['decimals']
        contract = jData[data]['address']
        row = f"INSERT INTO trusted_pairs(token, contract, decimals, is_active, tsymbol) VALUES ('{token}', '{contract}', {decimals}, 'f', '{token}') ON CONFLICT (token) DO UPDATE SET contract = '{contract}';"
        # row = f"INSERT INTO trusted_pairs(token, contract, decimals, is_active, tsymbol) VALUES ('{token}', NULL, {decimals}, 'f', '{token}');"
        print(row)
        resp = _query(row)
        print(resp)


# set_new_token()

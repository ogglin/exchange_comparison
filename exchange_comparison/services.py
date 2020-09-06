import requests
import json

from exchange_pairs.models import ComparePairs, TrustedPairs, CustomSql
from .models import *


def token_update(token, contract, decimals):
    token_id = ComparePairs.objects.filter(token=token).values('id')
    if len(token_id) > 0:
        pass
    else:
        compare = ComparePairs(token=token, contract=contract, decimals=decimals, is_active=True)
        trusted = TrustedPairs(token=token, contract=contract, decimals=decimals, is_active=True)
        compare.save()
        trusted.save()


def token_set():
    token = None
    contract = None
    decimals = None
    url = 'https://api.idex.market/returnCurrencies'
    response = requests.get(url=url)
    jData = json.loads(response.content)
    for key in jData.keys():
        token = key
        for item in jData[key].items():
            if str(item[0]) == 'address':
                if item[1] != 'N/A':
                    contract = item[1]
                else:
                    contract = None
            if str(item[0]) == 'decimals':
                if item[1] != 'N/A':
                    decimals = item[1]
                else:
                    decimals = None
        token_update(token, contract, decimals)

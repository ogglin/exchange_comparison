import requests
import json

from exchange_pairs.models import ComparePairs, TrustedPairs, CustomSql
from uniswap_module.models import *
# from bancor_module.models import *
# from kyber_module.models import *
# from .models import *


def token_update(token, contract, decimals):
    compare_id = ComparePairs.objects.filter(token=token).values('id')
    trusted_id = ComparePairs.objects.filter(token=token).values('id')
    uni_id = Uniswap.objects.filter(token=token).values('id')
    uni_one_id = UniswapOne.objects.filter(token=token).values('id')
    # bankor_id = Bancor.objects.filter(token=token).values('id')
    # kyber_id = Kyber.objects.filter(token=token).values('id')
    if len(compare_id) > 0:
        ComparePairs.objects.filter(id=compare_id[0]['id']).update(contract=contract, decimals=decimals)
    else:
        compare = ComparePairs(token=token, contract=contract, decimals=decimals, is_active=True)
        compare.save()
    if len(trusted_id) > 0:
        TrustedPairs.objects.filter(id=trusted_id[0]['id']).update(contract=contract, decimals=decimals)
    else:
        trusted = TrustedPairs(token=token, contract=contract, decimals=decimals, is_active=True)
        trusted.save()
    if len(uni_id) > 0:
        Uniswap.objects.filter(id=uni_id[0]['id']).update(tokenid=contract)
    if len(uni_one_id) > 0:
        UniswapOne.objects.filter(id=uni_one_id[0]['id']).update(tokenid=contract)
    # if len(bankor_id) > 0:
    #     Bancor.objects.filter(id=bankor_id[0]['id']).update(contract=contract, decimals=decimals)
    # if len(kyber_id) > 0:
    #     Kyber.objects.filter(id=kyber_id[0]['id']).update(contract=contract, decimals=decimals)


def token_set():
    token = None
    contract = None
    decimals = None
    url = 'https://api.idex.market/returnCurrencies'
    response = requests.get(url=url)
    jData = json.loads(response.content)
    for key in jData.keys():
        token = key
        print(token)
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

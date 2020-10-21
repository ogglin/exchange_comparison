import requests
import json

from exchange_pairs.models import ComparePairs, TrustedPairs, CustomSql
from uniswap_module.models import *
# from bancor_module.models import *
# from kyber_module.models import *
# from .models import *


def token_update(token, contract, decimals):
    compare_id = ComparePairs.objects.filter(token=token).values('id')
    if len(compare_id) > 0:
        ComparePairs.objects.filter(id=compare_id[0]['id']).update(contract=contract, decimals=decimals)
    else:
        compare = ComparePairs(token=token, contract=contract, decimals=decimals, is_active=True)
        compare.save()

    trusted_id = TrustedPairs.objects.filter(token=token).values('id')
    if len(trusted_id) > 0:
        TrustedPairs.objects.filter(id=trusted_id[0]['id']).update(contract=contract, decimals=decimals)
    else:
        trusted = TrustedPairs(token=token, contract=contract, decimals=decimals, is_active=True)
        trusted.save()

    uni_id = Uniswap.objects.filter(exch_direction=token).values('id')
    if len(uni_id) > 0:
        Uniswap.objects.filter(id=uni_id[0]['id']).update(tokenid=contract)

    uni_one_id = UniswapOne.objects.filter(exch_direction=token).values('id')
    if len(uni_one_id) > 0:
        UniswapOne.objects.filter(id=uni_one_id[0]['id']).update(tokenid=contract)

    # bankor_id = Bancor.objects.filter(token=token).values('id')
    # if len(bankor_id) > 0:
    #     Bancor.objects.filter(id=bankor_id[0]['id']).update(contract=contract, decimals=decimals)

    # kyber_id = Kyber.objects.filter(token=token).values('id')
    # if len(kyber_id) > 0:
    #     Kyber.objects.filter(id=kyber_id[0]['id']).update(contract=contract, decimals=decimals)


def token_set():
    url = 'https://api.idex.io/v1/assets'
    response = requests.get(url=url)
    jData = json.loads(response.content)
    for data in jData:
        token = data['symbol']
        contract = data['contractAddress']
        decimals = data['assetDecimals']
        token_update(token, contract, decimals)

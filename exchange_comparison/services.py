import datetime
import time

import requests
import json

from asgiref.sync import sync_to_async

from exchange_pairs.models import ComparePairs, TrustedPairs, CustomSql, ExchangePairs, Settings
from hotbit_module.models import Hotbit
from idex_module.models import Idex
from idex_module.socket_services import _query
from uniswap_module.models import *
from bancor_module.models import *
from kyber_module.models import *


# from .models import *

@sync_to_async
def token_exchange_set():
    _query(f'REFRESH MATERIALIZED VIEW "all_compare_tokens";')
    trusted_pair = list(TrustedPairs.objects.filter(is_active=True).values_list())
    for pair in trusted_pair:
        token = pair[1]
        exch_pair_id = ExchangePairs.objects.filter(exch_direction=token).values('id')
        if len(exch_pair_id) > 0:
            pass
        else:
            exch_pairs = ExchangePairs(exch_direction=token)
            exch_pairs.save()

        idex_id = Idex.objects.filter(exch_direction=token, is_active=True).values('id')
        if len(idex_id) > 0:
            ExchangePairs.objects.filter(exch_direction=token).update(idex_direction=idex_id[0]['id'])
        else:
            ExchangePairs.objects.filter(exch_direction=token).update(idex_direction=None)

        hotbit_id = Hotbit.objects.filter(exch_direction=token, is_active=True).values('id')
        if len(hotbit_id) > 0:
            ExchangePairs.objects.filter(exch_direction=token).update(hotbit=hotbit_id[0]['id'])
        else:
            ExchangePairs.objects.filter(exch_direction=token).update(hotbit=None)

        uniswap_id = Uniswap.objects.filter(exch_direction=token, is_active=True).values('id')
        if len(uniswap_id) > 0:
            ExchangePairs.objects.filter(exch_direction=token).update(uniswap_direction=uniswap_id[0]['id'])
        else:
            ExchangePairs.objects.filter(exch_direction=token).update(uniswap_direction=None)

        uniswap_one_id = UniswapOne.objects.filter(exch_direction=token, is_active=True).values('id')
        if len(uniswap_one_id) > 0:
            ExchangePairs.objects.filter(exch_direction=token).update(uniswap_one_direction=uniswap_one_id[0]['id'])
        else:
            ExchangePairs.objects.filter(exch_direction=token).update(uniswap_one_direction=None)

        bancor_id = Bancor.objects.filter(exch_direction=token, is_active=True).values('id')
        if len(bancor_id) > 0:
            ExchangePairs.objects.filter(exch_direction=token).update(bancor_direction=bancor_id[0]['id'])
        else:
            ExchangePairs.objects.filter(exch_direction=token).update(bancor_direction=None)

        kyber_id = Kyber.objects.filter(exch_direction=token, is_active=True).values('id')
        if len(kyber_id) > 0:
            ExchangePairs.objects.filter(exch_direction=token).update(kyber_direction=kyber_id[0]['id'])
        else:
            ExchangePairs.objects.filter(exch_direction=token).update(kyber_direction=None)


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


@sync_to_async
def set_gas():
    try:
        time.sleep(2)
        url = 'https://api.etherscan.io/api?module=gastracker&action=gasoracle&apikey=7EERE6KTUK3UH5X9CPAK63CTP93SJRF1NI'
        response = requests.get(url=url)
        jData = json.loads(response.content)['result']
        _query(f"UPDATE settings SET gas_fast = {jData['FastGasPrice']}, gas_normal={jData['ProposeGasPrice']} WHERE id = 1;")
    except:
        pass


@sync_to_async
def usd_currency_update():
    try:
        time.sleep(1)
        url = 'https://api.hotbit.io/api/v1/market.status?market=ETH/USDT&period=10'
        response = requests.get(url=url)
        jData = json.loads(response.content)['result']
        _query(f"UPDATE settings SET currency_usd = {jData['last']} WHERE id = 1;")
    except:
        pass


async def exchange_set_init():
    print('start exchanges: ' + str(datetime.datetime.now()))
    while True:
        await token_exchange_set()
        # print('end exchanges: ' + str(datetime.datetime.now()))


async def set_gas_currency_init():
    while True:
        await set_gas()
        await usd_currency_update()

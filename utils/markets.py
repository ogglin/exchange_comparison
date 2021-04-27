import json
import time

import requests
import urllib3
from asgiref.sync import sync_to_async

from bilaxy_module.models import BilaxyMarkets
from exchange_pairs.models import TrustedPairs
from hitbtc_module.models import HitbtcMarkets
from hotbit_module.models import HotbitMarkets
from idex_module.models import IdexMarkets
from uniswap_module.models import UniswapMarkets, Uniswap


def get_url_content(url):
    statuscode = 0
    response = None
    while statuscode != 200:
        response = 0
        try:
            response = requests.get(url=url)
        except (
                requests.ConnectionError,
                requests.exceptions.ReadTimeout,
                requests.exceptions.Timeout,
                requests.exceptions.ConnectTimeout,
        ) as e:
            time.sleep(1)
            statuscode = 0
            print(e)
        if response:
            statuscode = response.status_code
    return response.content


def set_hotbit_market():
    url = 'https://api.hotbit.io/api/v1/market.list'
    markets = json.loads(get_url_content(url))['result']
    for market in markets:
        m = market['name']
        t = market['stock']
        if len(HotbitMarkets.objects.filter(market=m)) < 1:
            obj = HotbitMarkets(market=m, token=t, tsymbol=t, is_active=True)
            obj.save()
            print(m, t)


def set_hitbtc_market():
    url = 'https://api.hitbtc.com/api/2/public/symbol'
    markets = json.loads(get_url_content(url))
    for market in markets:
        m = market['id']
        t = market['baseCurrency']
        if len(HitbtcMarkets.objects.filter(market=m)) < 1:
            obj = HitbtcMarkets(market=m, token=t, tsymbol=t, is_active=True)
            obj.save()
            print(m, t)


def set_idex_market():
    url = 'https://api.idex.io/v1/markets'
    markets = json.loads(get_url_content(url))
    for market in markets:
        m = market['market']
        t = market['baseAsset']
        if len(IdexMarkets.objects.filter(market=m)) < 1:
            obj = IdexMarkets(market=m, token=t, tsymbol=t, is_active=True)
            obj.save()
            print(m, t)


def set_bilaxy_market():
    url = 'https://newapi.bilaxy.com/v1/pairs'
    markets = json.loads(get_url_content(url))
    for key, market in markets.items():
        m = key
        t = market['base']
        a = market['trade_enabled']
        if len(BilaxyMarkets.objects.filter(market=m)) < 1:
            obj = BilaxyMarkets(market=m, token=t, tsymbol=t, is_active=a)
            obj.save()
            print(m, t, a)


@sync_to_async
def set_uniswap_market():
    # http = urllib3.PoolManager()
    # url = 'https://api.thegraph.com/subgraphs/name/uniswap/uniswap-v2'
    # all_i = 7
    # for i in range(all_i):
    #     req = json.dumps({'query': '{tokens(first:1000, skip:' + str(i*1000) + ')  {id symbol name}}'}).encode('utf-8')
    #     response = http.request('POST', url, body=req)
    #     # try:
    #     markets = json.loads(response.data.decode('utf-8'))['data']['tokens']
    #     for market in markets:
    #         c = market['id']
    #         m = market['symbol'].strip()
    #         t = market['name'].strip()
    #         if len(UniswapMarkets.objects.filter(market=m)) < 1:
    #             print(c, m, t)
    #             obj = UniswapMarkets(market=m, token=t, tokenid=c, is_active=False)
    #             obj.save()
    tmarkets = TrustedPairs.objects.filter(contract__isnull=False)
    umarkets = Uniswap.objects.all()
    for tm in tmarkets:
        # print(tm.contract)
        uObj = Uniswap.objects.filter(tokenid=tm.contract)
        if len(uObj) > 1:
            obj = Uniswap.objects.get(tokenid=tm.contract)[0]
            obj.tsymbol = tm.tsymbol
            obj.is_active = True
        else:
            try:
                obj = Uniswap(tokenid=tm.contract, highest_bid=0, lowest_ask=0, volume=0, tsymbol=tm.tsymbol,
                              exch_direction=tm.token, is_active=True)
                obj.save()
            except:
                pass



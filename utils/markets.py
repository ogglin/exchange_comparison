import json
import time

import requests
from asgiref.sync import sync_to_async

from bilaxy_module.models import BilaxyMarkets
from hitbtc_module.models import HitbtcMarkets
from hotbit_module.models import HotbitMarkets
from idex_module.models import IdexMarkets


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

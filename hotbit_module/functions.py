import asyncio
import concurrent.futures
import json
import math
import time

import aiohttp
import requests
from aiohttp_socks import SocksConnector
from asgiref.sync import sync_to_async

import exchange_pairs.services as ex_serv
from exchange_pairs.models import Settings, TrustedPairs
from exchange_pairs.utils import CompareToken as ct, ResultPrepare as rprep, proxys
from .models import Hotbit

API_URL = 'https://api.hotbit.io/api/v1/allticker'

prices = []
PRODUCERS_COUNT = 20
idex_tiker_all = None


async def get_hotbit_depth(symbol, proxy):
    url = f"https://api.hotbit.io/api/v1/order.depth?interval=1e-8&&limit=20&market={symbol}"
    socks_url = 'socks5://' + proxy[2] + ':' + proxy[3] + '@' + proxy[0] + ':' + proxy[1]
    connector = SocksConnector.from_url(socks_url)
    isTD = True
    while isTD:
        try:
            async with aiohttp.ClientSession(connector=connector) as session:
                async with session.get(url) as response:
                    html = await response.text()
                    jhtml = json.loads(html)
                    if jhtml['error'] is None:
                        isTD = False
                        return jhtml['result']
                    elif jhtml['error']:
                        isTD = False
                        print(jhtml['error'])
                        return None
                    else:
                        isTD = True
        except:
            time.sleep(1)


async def compare_markets(htoken, all_tokens, percent, currency, proxy):
    hotbit_depth = await get_hotbit_depth(htoken[3], proxy)
    # print(token, percent, currency, proxy, exch, hitbtc_deth)
    compare_result = []
    if hotbit_depth:
        for token in all_tokens:
            if token[0] == htoken[0]:
                compare_result.append(
                    ct(buy_from='hitbtc', buy_symbol=htoken[3], buy_prices=hotbit_depth['asks'], buy_volume=0,
                       sell_to=token[2], sell_prices=token[4], sell_volume=1, sell_symbol=token[3],
                       contract=token[1], profit_percent=percent, currency=currency).compare())
                compare_result.append(
                    ct(buy_from=token[2], buy_symbol=token[3], buy_prices=token[4], buy_volume=0, sell_to='hitbtc',
                       sell_prices=hotbit_depth['bids'], sell_volume=1, sell_symbol=htoken[3],
                       contract=token[1], profit_percent=percent, currency=currency).compare())
                return compare_result


async def init_compare(hotbit_tokens, all_tokens, percent, currency):
    async_tasks = []
    cnt = 0
    for htoken in hotbit_tokens:
        async_tasks.append(compare_markets(htoken, all_tokens, percent, currency, proxys[cnt]))
        cnt += 1
        if cnt >= len(proxys):
            cnt = 0
    results = await asyncio.gather(*async_tasks)
    return results


def hotbit_profits():
    setting = Settings.objects.all()[0]
    percent = setting.market_percent / 100 * setting.market_koef
    isTD = True
    hotbit_tokens = []
    all_tokens = []
    while isTD:
        if len(ex_serv.all_compared_tokens) > 0:
            for token in ex_serv.all_compared_tokens:
                if 'hotbit' in token[2]:
                    hotbit_tokens.append(token)
                else:
                    all_tokens.append(token)
            isTD = False
        else:
            isTD = True
            time.sleep(1)
            print('wait for tokens')
    get_eth_btc()
    currency = Settings.objects.all().values()[0]['currency']
    all_result = []
    xlen = math.ceil(len(hotbit_tokens) / 200)
    n = 0
    for i in range(xlen):
        parts_hotbit_tokens = []
        for htoken in hotbit_tokens:
            if n <= 200 + 200 * i:
                n += 1
                parts_hotbit_tokens.append(htoken)
        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)
        loop = asyncio.get_event_loop()
        loop.set_default_executor(concurrent.futures.ThreadPoolExecutor(max_workers=20))
        init_result = loop.run_until_complete(init_compare(parts_hotbit_tokens, all_tokens, percent, currency))
        loop.close()
        all_result.extend(init_result)
    compare_result = rprep(all_result=all_result, exchanger='hotbit').result()
    return compare_result


# Set Prices
def set_prices(symbol, buy, sell, volume):
    prices.append([symbol, buy, sell, volume])


def get_eth_btc():
    try:
        response = requests.get(f'https://api.hotbit.io/api/v1/market.status?market=ETH/BTC&period=10')
        Settings.objects.filter(id=1).update(currency=float(json.loads(response.content)['result']['last']))
        return float(json.loads(response.content)['result']['last'])
    except:
        return getattr(Settings.objects.get(pk=1), 'currency')


def get_ticker():
    currency = get_eth_btc()
    resp_get = True
    while resp_get:
        try:
            response = requests.get(url=API_URL)
            resp_get = False
        except:
            resp_get = True
    jData = sorted(json.loads(response.content)['ticker'], key=lambda x: x['symbol'], reverse=False)
    for data in jData:
        if 'USDT' not in data['symbol']:
            buy = float(data['high'])
            sell = float(data['buy'])
            volume = float(data['vol'])
            if (buy > 0 or sell > 0) and volume > 0:
                if 'ETH_BTC' in data['symbol']:
                    set_prices('ETH/BTC', 1 / buy, 1 / sell, volume)
                elif 'BTC' in data['symbol'] and 'ETH' not in data['symbol']:
                    set_prices(data['symbol'], buy, sell, volume)
                else:
                    set_prices(data['symbol'], buy, sell, volume)


def currencies_update(symbol, buy, sell, volume):
    pair_id = Hotbit.objects.filter(symbol=symbol.replace('_', '/')).values('id')
    if len(pair_id) > 0:
        Hotbit.objects.filter(id=pair_id[0]['id']).update(buy=buy, sell=sell, volume=volume)
    else:
        pair = Hotbit(exch_direction=symbol, symbol=symbol.replace('_', '/'), buy=buy, sell=sell, volume=volume,
                      is_active=True, decimals=18)
        pair.save()


@sync_to_async
def set_currencies():
    get_ticker()
    for p in prices:
        currencies_update(p[0], p[1], p[2], p[3])

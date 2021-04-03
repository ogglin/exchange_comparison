import asyncio
import concurrent.futures
import json
import math
import time

import requests
from asgiref.sync import sync_to_async

import exchange_pairs.services as ex_serv
from exchange_pairs.models import Settings
from exchange_pairs.utils import CompareToken as ct, ResultPrepare as rprep, proxys
from utils.gets import get_hotbit_depth, get_hitbtc_depth
from .models import Hotbit

API_URL = 'https://api.hotbit.io/api/v1/allticker'

prices = []
PRODUCERS_COUNT = 20
idex_tiker_all = None


async def compare_markets(htoken, all_tokens, percent, currency, proxy, currencyUSD):
    hotbit_depth = await get_hotbit_depth(htoken[3], proxy)
    compare_result = []
    if hotbit_depth:
        for token in all_tokens:
            if token[0] == htoken[0] and 'usd' not in token[0].lower() and 'usd' not in htoken[0].lower():
                c_bids = None
                # if 'idex' in token[2]:
                #     idex_depth = await get_idex_depth(token[3], proxy)
                #     if idex_depth:
                #         if len(idex_depth['bids']) > 0:
                #             c_bids = idex_depth['bids']
                #         else:
                #             c_bids = None
                #     else:
                #         c_bids = None
                if 'hitbtc' in token[2]:
                    hitbtc_deth = await get_hitbtc_depth(token[3], proxy)
                    if hitbtc_deth:
                        c_bids = []
                        for bid in hitbtc_deth['bid']:
                            c_bids.append([bid['price'], bid['size']])
                else:
                    c_bids = token[4]
                compare_result.append(
                    ct(buy_from='hotbit', buy_symbol=htoken[3], buy_prices=hotbit_depth['asks'], buy_volume=0,
                       sell_to=token[2], sell_prices=c_bids, sell_volume=1, sell_symbol=token[3],
                       contract=token[1], profit_percent=percent, currency=currency, currencyUSD=currencyUSD).compare())
                if 'bancor' in token[2] or 'uniswap' in token[2] or 'kyber' in token[2] or 'uniswap_one' in token[2]:
                    compare_result.append(
                        ct(buy_from=token[2], buy_symbol=token[3], buy_prices=token[5], buy_volume=0, sell_to='hotbit',
                           sell_prices=hotbit_depth['bids'], sell_volume=1, sell_symbol=htoken[3],
                           contract=token[1], profit_percent=percent, currency=currency, currencyUSD=currencyUSD).compare())
    return compare_result


async def init_compare(hotbit_tokens, all_tokens, percent, currency, currencyUSD):
    async_tasks = []
    cnt = 0
    for htoken in hotbit_tokens:
        async_tasks.append(compare_markets(htoken, all_tokens, percent, currency, proxys[cnt], currencyUSD))
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
    get_eth_btc()
    currency = Settings.objects.all().values()[0]['currency']
    currencyUSD = Settings.objects.all().values()[0]['currencyUSD']
    all_result = []
    xlen = math.ceil(len(hotbit_tokens) / 200)
    for i in range(xlen):
        parts_hotbit_tokens = []
        for hi, htoken in enumerate(hotbit_tokens):
            if 200 * i <= hi < 200 * (i + 1):
                parts_hotbit_tokens.append(htoken)
        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)
        loop = asyncio.get_event_loop()
        loop.set_default_executor(concurrent.futures.ThreadPoolExecutor(max_workers=20))
        init_result = loop.run_until_complete(init_compare(parts_hotbit_tokens, all_tokens, percent, currency, currencyUSD))
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

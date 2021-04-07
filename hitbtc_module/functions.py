import asyncio
import concurrent.futures
import json
import math
import time
from datetime import datetime

import requests
from django.db import transaction

from asgiref.sync import sync_to_async

from exchange_pairs.models import Settings
import exchange_pairs.services as ex_serv
from exchange_pairs.utils import CompareToken as ct, ResultPrepare as rprep, proxys
from hitbtc_module.models import Hitbtc
from utils.gets import get_hotbit_depth, get_hitbtc_depth

hitbtc_tikers_set = []


@sync_to_async
def currencies_update():
    with transaction.atomic():
        for data in hitbtc_tikers_set:
            pair_id = Hitbtc.objects.filter(symbol=data['symbol']).values('id')
            if len(pair_id) > 0:
                Hitbtc.objects.filter(id=pair_id[0]['id']).update(buy=data['ask'], sell=data['bid'],
                                                                  volume=data['volume'])
            else:
                pair = Hitbtc(exch_direction=data['token'], buy=data['ask'], sell=data['bid'], is_active=True,
                              volume=data['volume'], symbol=data['symbol'])
                pair.save()


async def get_tiker():
    global hitbtc_tikers_set
    url = 'https://api.hitbtc.com/api/2/public/ticker'
    statuscode = 0
    while statuscode != 200:
        response = 0
        try:
            response = requests.get(url=url)
            hitbtc_tikers_set = []
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
    jData = json.loads(response.content)
    for jd in jData:
        if 'ETH' in jd['symbol'] or 'BTC' in jd['symbol']:
            exch_direction = jd['symbol'].replace('ETH', '').replace('BTC', '')
            buy = jd['ask']
            sell = jd['bid']
            symbol = jd['symbol']
            volume = jd['volume']
            hitbtc_tikers_set.append(
                {'token': exch_direction, 'ask': buy, 'bid': sell, 'volume': volume, 'symbol': symbol})
    await currencies_update()
    # print('end tiker update', datetime.datetime.now())


async def hitbtc_tiker_init():
    while True:
        # print('start tiker update', datetime.datetime.now())
        await get_tiker()


async def compare_markets(htoken, all_tokens, percent, currency, proxy, currencyUSD):
    hitbtc_deth = await get_hitbtc_depth(htoken[3], proxy)
    asks = []
    bids = []
    compare_result = []
    if hitbtc_deth:
        for token in all_tokens:
            # print(token)
            # print(hitbtc_deth)
            if token[0] == htoken[0] and 'usd' not in token[0].lower() and 'usd' not in htoken[0].lower():
                c_bids = None
                # if 'idex' in token[2]:
                #     idex_depth = await get_idex_depth(token[3], proxy)
                #     if idex_depth:
                #         if len(idex_depth['bids']) > 0:
                #             c_bids = idex_depth['bids']
                if 'hotbit' in token[2]:
                    hotbit_depth = await get_hotbit_depth(token[3], proxy)
                    if hotbit_depth:
                        c_bids = hotbit_depth['bids']
                else:
                    c_bids = token[4]
                for ask in hitbtc_deth['ask']:
                    asks.append([ask['price'], ask['size']])
                compare_result.append(
                    ct(buy_from='hitbtc', buy_symbol=htoken[3], buy_prices=asks, buy_volume=0, sell_to=token[2],
                       sell_prices=c_bids, sell_volume=1, sell_symbol=token[3],
                       contract=token[1], profit_percent=percent, currency=currency, currencyUSD=currencyUSD).compare())
                if 'bancor' in token[2] or 'uniswap' in token[2] or 'kyber' in token[2] or 'uniswap_one' in token[2]:
                    for bid in hitbtc_deth['bid']:
                        bids.append([bid['price'], bid['size']])
                    compare_result.append(
                        ct(buy_from=token[2], buy_symbol=token[3], buy_prices=token[5], buy_volume=1, sell_to='hitbtc',
                           sell_prices=bids, sell_volume=0, sell_symbol=htoken[3],
                           contract=token[1], profit_percent=percent, currency=currency, currencyUSD=currencyUSD).compare())
    return compare_result


async def init_compare(hitbtc_tokens, all_tokens, percent, currency, currencyUSD):
    async_tasks = []
    cnt = 0
    for htoken in hitbtc_tokens:
        async_tasks.append(compare_markets(htoken, all_tokens, percent, currency, proxys[cnt], currencyUSD))
        cnt += 1
        if cnt >= len(proxys):
            cnt = 0
    results = await asyncio.gather(*async_tasks)
    return results


# @sync_to_async
def hitbtc_profits():
    # print('hitbtc_profits start', datetime.now())
    setting = Settings.objects.all()[0]
    percent = setting.market_percent / 100 * setting.market_koef
    # tsymbol, contract, site, token, sell, buy, volume
    isTD = True
    hitbtc_tokens = []
    all_tokens = []
    while isTD:
        if len(ex_serv.all_compared_tokens) > 0:
            # print(len(ex_serv.all_compared_tokens))
            for token in ex_serv.all_compared_tokens:
                if 'hitbtc' in token[2]:
                    hitbtc_tokens.append(token)
                else:
                    all_tokens.append(token)
            isTD = False
            # print(len(hitbtc_tokens))
        else:
            isTD = True
            time.sleep(1)
    currency = Settings.objects.all().values()[0]['currency']
    currencyUSD = Settings.objects.all().values()[0]['currency_usd']
    all_result = []
    xlen = math.ceil(len(hitbtc_tokens) / 200)
    for i in range(xlen):
        parts_hitbtc_tokens = []
        for hi, htoken in enumerate(hitbtc_tokens):
            if 200 * i <= hi < 200 * (i + 1):
                parts_hitbtc_tokens.append(htoken)
        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)
        loop = asyncio.get_event_loop()
        loop.set_default_executor(concurrent.futures.ThreadPoolExecutor(max_workers=200))
        # print('hitbtc loop start', datetime.now())
        init_result = loop.run_until_complete(init_compare(parts_hitbtc_tokens, all_tokens, percent, currency, currencyUSD))
        loop.close()
        # print('hitbtc loop  end', datetime.now())
        all_result.extend(init_result)
    # print('hitbtc_profits end', datetime.now())
    compare_result = rprep(all_result=all_result, exchanger='hitbtc').result()
    return compare_result

# async def hitbtc_profits_init():
#     while True:
#         await hitbtc_profits()
#
#
# if __name__ == '__main__':
#     hitbtc_profits()

import asyncio
import concurrent.futures
import datetime
import json
import math
import time

import aiohttp
import requests
from aiohttp_socks import SocksConnector
from asgiref.sync import sync_to_async

from exchange_pairs.models import Settings
import exchange_pairs.services as ex_serv
from exchange_pairs.utils import CompareToken as ct, ResultPrepare as rprep, proxys
from hitbtc_module.models import Hitbtc

hitbtc_tikers_set = []


@sync_to_async
def currencies_update():
    # print('start idex currency update: ' + str(datetime.datetime.now()))
    update_list = []
    objs = Hitbtc.objects.all().order_by('id')
    if len(objs) > 0:
        for data in hitbtc_tikers_set:
            try:
                obj = objs.get(exch_direction=data['token'])
                obj.lowest_ask = data['ask']
                obj.highest_bid = data['bid']
                obj.volume = data['volume']
                update_list.append(obj)
            except:
                pair = Hitbtc(exch_direction=data['token'], buy=data['ask'], sell=data['bid'], is_active=True,
                              volume=data['volume'], symbol=data['symbol'])
                pair.save()
    else:
        for data in hitbtc_tikers_set:
            pair = Hitbtc(exch_direction=data['token'], buy=data['ask'], sell=data['bid'], is_active=True,
                          volume=data['volume'], symbol=data['symbol'])
            pair.save()
    Hitbtc.objects.bulk_update(update_list, ['buy', 'sell', 'volume'])
    # print('end idex currency update: ' + str(datetime.datetime.now()))


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
    print('tiker update', datetime.datetime.now())


async def hitbtc_tiker_init():
    while True:
        await get_tiker()


async def get_hitbtc_depth(symbol, proxy):
    url = f"https://api.hitbtc.com/api/2/public/orderbook/{symbol.replace('/', '')}"
    socks_url = 'socks5://' + proxy[2] + ':' + proxy[3] + '@' + proxy[0] + ':' + proxy[1]
    connector = SocksConnector.from_url(socks_url)
    isTD = True
    while isTD:
        try:
            async with aiohttp.ClientSession(connector=connector) as session:
                async with session.get(url) as response:
                    html = await response.text()
                    jhtml = json.loads(html)
                    if jhtml['ask']:
                        isTD = False
                        return jhtml
                    elif jhtml['error']:
                        isTD = False
                        print(jhtml['error'])
                        return None
                    else:
                        isTD = True
        except:
            time.sleep(1)


async def compare_markets(htoken, all_tokens, percent, currency, proxy):
    hitbtc_deth = await get_hitbtc_depth(htoken[3], proxy)
    # print(token, percent, currency, proxy, exch, hitbtc_deth)
    asks = []
    bids = []
    compare_result = []
    if hitbtc_deth:
        for token in all_tokens:
            if token[0] == htoken[0]:
                for ask in hitbtc_deth['ask']:
                    asks.append([ask['price'], ask['size']])
                compare_result.append(
                    ct(buy_from='hitbtc', buy_symbol=htoken[3], buy_prices=asks, buy_volume=0, sell_to=token[2],
                       sell_prices=token[4], sell_volume=1, sell_symbol=token[3],
                       contract=token[1], profit_percent=percent, currency=currency).compare())
                for bid in hitbtc_deth['bid']:
                    bids.append([bid['price'], bid['size']])
                compare_result.append(
                    ct(buy_from=token[2], buy_symbol=token[3], buy_prices=token[5], buy_volume=1, sell_to='hitbtc',
                       sell_prices=bids, sell_volume=0, sell_symbol=htoken[3],
                       contract=token[1], profit_percent=percent, currency=currency).compare())
                return compare_result


async def init_compare(hitbtc_tokens, all_tokens, percent, currency):
    async_tasks = []
    cnt = 0
    for htoken in hitbtc_tokens:
        async_tasks.append(compare_markets(htoken, all_tokens, percent, currency, proxys[cnt]))
        cnt += 1
        if cnt >= len(proxys):
            cnt = 0
    results = await asyncio.gather(*async_tasks)
    return results


# @sync_to_async
def hitbtc_profits():
    # global all_compared_tokens
    print('hitbtc_profits start', datetime.datetime.now())
    setting = Settings.objects.all()[0]
    percent = setting.market_percent / 100 * setting.market_koef
    # tsymbol, contract, site, token, sell, buy, volume
    isTD = True
    hitbtc_tokens = []
    all_tokens = []
    while isTD:
        if len(ex_serv.all_compared_tokens) > 0:
            for token in ex_serv.all_compared_tokens:
                if 'hitbtc' in token[2]:
                    hitbtc_tokens.append(token)
                else:
                    all_tokens.append(token)
            isTD = False
        else:
            isTD = True
            time.sleep(1)
            print('wait for tokens')
    currency = Settings.objects.all().values()[0]['currency']
    all_result = []
    xlen = math.ceil(len(hitbtc_tokens) / 200)
    n = 0
    for i in range(xlen):
        parts_hitbtc_tokens = []
        for htoken in hitbtc_tokens:
            if n <= 200 + 200 * i:
                n += 1
                parts_hitbtc_tokens.append(htoken)
        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)
        loop = asyncio.get_event_loop()
        loop.set_default_executor(concurrent.futures.ThreadPoolExecutor(max_workers=20))
        init_result = loop.run_until_complete(init_compare(hitbtc_tokens, all_tokens, percent, currency))
        loop.close()
        all_result.extend(init_result)
    print('hitbtc_profits end', datetime.datetime.now())
    compare_result = rprep(all_result=all_result, exchanger='hitbtc').result()
    return compare_result

# async def hitbtc_profits_init():
#     while True:
#         await hitbtc_profits()
#
#
# if __name__ == '__main__':
#     hitbtc_profits()

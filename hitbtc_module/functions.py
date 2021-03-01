import asyncio
import concurrent.futures
import json
import time

import aiohttp
import requests
from aiohttp_socks import SocksConnector
from asgiref.sync import sync_to_async

from exchange_comparison.utils import _query
from exchange_pairs.models import Settings
from hitbtc_module.models import Hitbtc
from hotbit_module.functions import proxys

from exchange_pairs.utils import CompareToken as ct

hitbtc_tikers_set = []


@sync_to_async
def currencies_update():
    # print('start idex currency update: ' + str(datetime.datetime.now()))
    update_list = []
    objs = Hitbtc.objects.all().order_by('id')
    for data in hitbtc_tikers_set:
        obj = objs.get(exch_direction=data['token'])
        if obj:
            obj.lowest_ask = data['ask']
            obj.highest_bid = data['bid']
            obj.volume = data['volume']
            update_list.append(obj)
        else:
            pair = Hitbtc(exch_direction=data['token'], lowest_ask=data['ask'], highest_bid=data['bid'], is_active=True,
                          volume=data['volume'], symbol=data['symbol'])
            pair.save()
    Hitbtc.objects.bulk_update(update_list, ['lowest_ask', 'highest_bid', 'volume'])
    # print('end idex currency update: ' + str(datetime.datetime.now()))


@sync_to_async
def get_tiker():
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
    currencies_update()


async def hitbtc_tiker_init():
    while True:
        await get_tiker()


async def get_hitbtc_depth(symbol, proxy):
    url = f"https://api.hitbtc.com/api/2/public/orderbook/{symbol}"
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
                        return jhtml
                    elif jhtml['error']:
                        isTD = False
                        print(jhtml['error'])
                        return None
                    else:
                        isTD = True
        except:
            time.sleep(1)


async def compare_markets(symbol, percent, currency, proxy):
    hotbit_deth = await get_hitbtc_depth(symbol[1], proxy)
    if hotbit_deth:
        return ct('hitbtc', hotbit_deth['asks'], 0, symbol[4], symbol[3], 1, symbol[1],
              symbol[2], 1, 1).compare()


async def init_compare(all_symbols, percent, currency):
    async_tasks = []
    # print('start collect symbols ' + str(len(symbols)) + ' :' + str(datetime.datetime.now()))
    cnt = 0
    for symbol in all_symbols:
        async_tasks.append(compare_markets(symbol, percent, currency, proxys[cnt]))
        cnt += 1
        if cnt >= len(proxys):
            cnt = 0
    # print('end  collect symbols: ' + str(len(async_tasks)) + str(datetime.datetime.now()))
    results = await asyncio.gather(*async_tasks)
    return results


def hitbtc_profits():
    setting = Settings.objects.all()[0]
    percent = setting.market_percent / 100 * setting.market_koef
    all_symbols = _query(f'')
    currency = Settings.objects.all().values()[0]['currency']
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    loop = asyncio.get_event_loop()
    loop.set_default_executor(concurrent.futures.ThreadPoolExecutor(max_workers=20))
    init_result = loop.run_until_complete(init_compare(all_symbols, percent, currency))
    compare_result = []

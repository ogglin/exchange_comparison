import asyncio
import concurrent.futures
import json
import math
import time

import aiohttp
from aiohttp_socks import SocksConnector

from exchange_pairs.models import Settings
from exchange_pairs.utils import CompareToken as ct, ResultPrepare as rprep, proxys
import exchange_pairs.services as ex_serv


async def get_idex_depth(symbol, proxy, dtime):
    # time.sleep(dtime)
    url = f"https://api.idex.io/v1/orderbook?market={symbol}-ETH&level=2&limit=20"
    socks_url = 'socks5://' + proxy[2] + ':' + proxy[3] + '@' + proxy[0] + ':' + proxy[1]
    connector = SocksConnector.from_url(socks_url)
    isTD = True
    while isTD:
        try:
            async with aiohttp.ClientSession(connector=connector) as session:
                async with session.get(url) as response:
                    html = await response.text()
                    jhtml = json.loads(html)
                    if 'sequence' in html:
                        isTD = False
                        return jhtml
                    elif 'code' in html:
                        isTD = False
                        return None
        except:
            time.sleep(2)


async def compare_markets(itoken, all_tokens, percent, currency, proxy, dtime):
    idex_depth = await get_idex_depth(itoken[3], proxy, dtime)
    compare_result = []
    if idex_depth:
        for token in all_tokens:
            if token[0] == itoken[0]:
                if len(idex_depth['asks']) > 0:
                    compare_result.append(
                        ct(buy_from='idex', buy_symbol=itoken[3], buy_prices=idex_depth['asks'], buy_volume=0,
                           sell_to=token[2], sell_prices=token[4], sell_volume=1, sell_symbol=token[3],
                           contract=token[1], profit_percent=percent, currency=currency).compare())
                if len(idex_depth['bids']) > 0 and ('bancor' in token[2] or 'uniswap' in token[2] or 'kyber' in token[2] or 'uniswap_one' in token[2]):
                    compare_result.append(
                        ct(buy_from=token[2], buy_symbol=token[3], buy_prices=token[5], buy_volume=0, sell_to='idex',
                           sell_prices=idex_depth['bids'], sell_volume=1, sell_symbol=itoken[3],
                           contract=token[1], profit_percent=percent, currency=currency).compare())
                return compare_result


async def init_compare(idex_tokens, all_tokens, percent, currency):
    async_tasks = []
    cnt = 0
    dtime = 0
    for itoken in idex_tokens:
        async_tasks.append(compare_markets(itoken, all_tokens, percent, currency, proxys[cnt], dtime))
        cnt += 1
        if cnt >= len(proxys):
            cnt = 0
            dtime += 0.4
    results = await asyncio.gather(*async_tasks)
    return results


# @sync_to_async
def idex_profits():
    setting = Settings.objects.all()[0]
    percent = setting.market_percent / 100 * setting.market_koef
    isTD = True
    idex_tokens = []
    all_tokens = []
    while isTD:
        if len(ex_serv.all_compared_tokens) > 0:
            for token in ex_serv.all_compared_tokens:
                if 'idex' in token[2]:
                    idex_tokens.append(token)
                else:
                    all_tokens.append(token)
            isTD = False
        else:
            isTD = True
            time.sleep(1)
            print('wait for tokens')
    currency = Settings.objects.all().values()[0]['currency']
    all_result = []
    xlen = math.ceil(len(idex_tokens) / 200)
    n = 0
    for i in range(xlen):
        parts_idex_tokens = []
        for itoken in idex_tokens:
            if n <= 200 + 200 * i:
                n += 1
                parts_idex_tokens.append(itoken)
        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)
        loop = asyncio.get_event_loop()
        loop.set_default_executor(concurrent.futures.ThreadPoolExecutor(max_workers=20))
        init_result = loop.run_until_complete(init_compare(parts_idex_tokens, all_tokens, percent, currency))
        loop.close()
        all_result.extend(init_result)
    compare_result = rprep(all_result=all_result, exchanger='hotbit').result()
    return compare_result

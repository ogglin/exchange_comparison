import asyncio
import concurrent.futures
import math
import time

import exchange_pairs.services as ex_serv
from exchange_pairs.models import Settings
from exchange_pairs.utils import CompareToken as ct, ResultPrepare as rprep, proxys
from utils.gets import get_hotbit_depth, get_idex_depth, get_hitbtc_depth


async def compare_markets(itoken, all_tokens, percent, currency, proxy, cnt, currencyUSD):
    idex_depth = await get_idex_depth(itoken[3], cnt)
    compare_result = []
    if idex_depth:
        for token in all_tokens:
            if token[0] == itoken[0] and 'usd' not in token[0].lower() and 'usd' not in itoken[0].lower():
                # idex_depth = {'asks': itoken[5], 'bids': itoken[4]}
                c_bids = None
                if 'hotbit' in token[2]:
                    hotbit_depth = await get_hotbit_depth(token[3], proxy)
                    if hotbit_depth:
                        c_bids = hotbit_depth['bids']
                elif 'hitbtc' in token[2]:
                    hitbtc_deth = await get_hitbtc_depth(token[3], proxy)
                    if hitbtc_deth:
                        c_bids = []
                        for bid in hitbtc_deth['bid']:
                            c_bids.append([bid['price'], bid['size']])
                else:
                    c_bids = token[4]
                if idex_depth['asks']:
                    compare_result.append(
                        ct(buy_from='idex', buy_symbol=itoken[3], buy_prices=idex_depth['asks'], buy_volume=0,
                           sell_to=token[2], sell_prices=c_bids, sell_volume=1, sell_symbol=token[3],
                           contract=token[1], profit_percent=percent, currency=currency, currencyUSD=currencyUSD).compare())
                if idex_depth['bids'] and ('bancor' in token[2] or 'uniswap' in token[2] or 'kyber' in token[2]
                                                    or 'uniswap_one' in token[2]):
                    compare_result.append(
                        ct(buy_from=token[2], buy_symbol=token[3], buy_prices=token[5], buy_volume=0, sell_to='idex',
                           sell_prices=idex_depth['bids'], sell_volume=1, sell_symbol=itoken[3],
                           contract=token[1], profit_percent=percent, currency=currency, currencyUSD=currencyUSD).compare())
    return compare_result


async def init_compare(idex_tokens, all_tokens, percent, currency, currencyUSD):
    async_tasks = []
    cnt = 0
    print('idex_tokens', len(idex_tokens))
    for itoken in idex_tokens:
        async_tasks.append(compare_markets(itoken, all_tokens, percent, currency, proxys[cnt], cnt, currencyUSD))
        cnt += 1
        if cnt >= len(proxys):
            cnt = 0
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
    currency = Settings.objects.all().values()[0]['currency']
    currencyUSD = Settings.objects.all().values()[0]['currencyUSD']
    all_result = []
    xlen = math.ceil(len(idex_tokens) / 200)
    for i in range(xlen):
        parts_idex_tokens = []
        for hi, htoken in enumerate(idex_tokens):
            if 200 * i <= hi < 200 * (i + 1):
                parts_idex_tokens.append(htoken)
        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)
        loop = asyncio.get_event_loop()
        loop.set_default_executor(concurrent.futures.ThreadPoolExecutor(max_workers=20))
        init_result = loop.run_until_complete(init_compare(parts_idex_tokens, all_tokens, percent, currency, currencyUSD))
        loop.close()
        all_result.extend(init_result)
    compare_result = rprep(all_result=all_result, exchanger='hotbit').result()
    return compare_result

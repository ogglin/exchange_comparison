import asyncio
import concurrent.futures
import math
import time
from datetime import datetime

import exchange_pairs.services as ex_serv
from exchange_pairs.models import Settings
from exchange_pairs.utils import CompareToken as ct, ResultPrepare as rprep, proxys
from utils.gets import get_hotbit_depth, get_hitbtc_depth, get_bilaxy_depth


async def compare_markets(btoken, all_tokens, percent, currency, proxy, currencyUSD):
    bilaxy_depth = await get_bilaxy_depth(btoken[3], proxy)
    compare_result = []
    if bilaxy_depth:
        for token in all_tokens:
            if token[0] == btoken[0] and 'usd' not in token[0].lower() and 'usd' not in btoken[0].lower():
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
                elif 'hotbit' in token[2]:
                    hotbit_depth = await get_hotbit_depth(token[3], proxy)
                    if hotbit_depth:
                        c_bids = hotbit_depth['bids']
                    else:
                        c_bids = None
                elif 'idex' in token[2]:
                    c_bids = None
                elif 'uniswap' in token[2]:
                    c_bids = token[4]
                else:
                    c_bids = None
                compare_result.append(
                    ct(buy_from='bilaxy', buy_symbol=btoken[3], buy_prices=bilaxy_depth['asks'], buy_volume=0,
                       sell_to=token[2], sell_prices=c_bids, sell_volume=1, sell_symbol=token[3],
                       contract=token[1], profit_percent=percent, currency=currency, currencyUSD=currencyUSD).compare())
                if 'bancor' in token[2] or 'uniswap' in token[2] or 'kyber' in token[2] or 'uniswap_one' in token[2]:
                    compare_result.append(
                        ct(buy_from=token[2], buy_symbol=token[3], buy_prices=token[5], buy_volume=0, sell_to='bilaxy',
                           sell_prices=bilaxy_depth['bids'], sell_volume=1, sell_symbol=btoken[3],
                           contract=token[1], profit_percent=percent, currency=currency,
                           currencyUSD=currencyUSD).compare())
    return compare_result


async def init_compare(bilaxy_tokens, all_tokens, percent, currency, currencyUSD):
    async_tasks = []
    cnt = 0
    for btoken in bilaxy_tokens:
        async_tasks.append(compare_markets(btoken, all_tokens, percent, currency, proxys[cnt], currencyUSD))
        cnt += 1
        if cnt >= len(proxys):
            cnt = 0
    results = await asyncio.gather(*async_tasks)
    return results


def bilaxy_profits():
    # print('bilaxy_profits start', datetime.now())
    setting = Settings.objects.all()[0]
    percent = setting.market_percent / 100 * setting.market_koef
    isTD = True
    bilaxy_tokens = []
    all_tokens = []
    while isTD:
        if len(ex_serv.all_compared_tokens) > 0:
            # print(len(ex_serv.all_compared_tokens), datetime.now())
            for token in ex_serv.all_compared_tokens:
                if 'bilaxy' in token[2]:
                    bilaxy_tokens.append(token)
                else:
                    all_tokens.append(token)
            isTD = False
            # print(len(bilaxy_tokens))
        else:
            isTD = True
            time.sleep(1)
    currency = Settings.objects.all().values()[0]['currency']
    currencyUSD = Settings.objects.all().values()[0]['currency_usd']
    all_result = []
    xlen = math.ceil(len(bilaxy_tokens) / 200)
    for i in range(xlen):
        part_bilaxy_tokens = []
        for hi, btoken in enumerate(bilaxy_tokens):
            if 200 * i <= hi < 200 * (i + 1):
                part_bilaxy_tokens.append(btoken)
        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)
        loop = asyncio.get_event_loop()
        loop.set_default_executor(concurrent.futures.ThreadPoolExecutor(max_workers=200))
        # print('bilaxy loop start', datetime.now())
        init_result = loop.run_until_complete(
            init_compare(part_bilaxy_tokens, all_tokens, percent, currency, currencyUSD))
        loop.close()
        # print('bilaxy loop end', datetime.now())
        all_result.extend(init_result)
    # print('bilaxy_profits end', datetime.now())
    compare_result = rprep(all_result=all_result, exchanger='bilaxy').result()
    return compare_result

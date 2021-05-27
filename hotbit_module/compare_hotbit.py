import asyncio
import concurrent.futures
import time
from datetime import datetime
from asgiref.sync import sync_to_async
from django.db import transaction
from django.db.models import Q
import exchange_comparison.global_vars as gv
from exchange_pairs.models import Settings, ProfitExchanges
from exchange_pairs.utils import CompareToken as ct, ResultPrepare as rprep, get_token_depth

counts = len(gv.proxys4) * 10


async def compare(tsymbol, bids, asks, itoken, direction, all_tokens, currency, currencyUSD, percent):
    # print(tsymbol, bids, asks, token, direction, currency, currencyUSD, percent)
    compare_result = []
    """(self, buy_from, buy_symbol, buy_prices, buy_volume, sell_to, sell_symbol, sell_prices, sell_volume,
                 contract, profit_percent, currency, currencyUSD)"""
    for token in all_tokens:
        if token[0] == tsymbol and 'usd' not in token[0].lower() and 'usd' not in tsymbol.lower():
            c_bids = get_token_depth(token)
            if asks:
                compare_result.append(
                    ct(buy_from='hotbit', buy_symbol=itoken, buy_prices=asks, buy_volume=0,
                       sell_to=token[2], sell_prices=c_bids, sell_volume=1, sell_symbol=token[3],
                       contract=token[1], profit_percent=percent, currency=currency, currencyUSD=currencyUSD).compare())
            if bids and ('bancor' in token[2] or 'uniswap' in token[2] or 'kyber' in token[2]
                         or 'uniswap_one' in token[2]):
                compare_result.append(
                    ct(buy_from=token[2], buy_symbol=token[3], buy_prices=token[5], buy_volume=0, sell_to='hotbit',
                       sell_prices=bids, sell_volume=1, sell_symbol=itoken,
                       contract=token[1], profit_percent=percent, currency=currency, currencyUSD=currencyUSD).compare())
    return compare_result


async def make_compare(tokens, all_tokens, currency, currencyUSD, percent):
    async_tasks = []
    for key, value in tokens.items():
        try:
            if len(value[0]['bids']) > 0 and len(value[0]['asks']) > 0:
                async_tasks.append(compare(value[1], value[0]['bids'], value[0]['asks'], key, value[2], all_tokens,
                                           currency, currencyUSD, percent))
        except:
            pass
    results = await asyncio.gather(*async_tasks)
    return results


@sync_to_async
def compare_init():
    setting = Settings.objects.all()[0]
    percent = setting.market_percent / 100 * setting.market_koef
    currency = setting.currency
    currencyUSD = setting.currency_usd
    all_tokens = []
    isTD = True
    while isTD:
        if len(gv.replica_hotbit) > 0 and len(gv.all_compared_tokens) > 0:
            isTD = False
            for token in gv.all_compared_tokens:
                if 'hotbit' not in token[2]:
                    all_tokens.append(token)
        else:
            isTD = True
            time.sleep(1)
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    loop = asyncio.get_event_loop()
    loop.set_default_executor(concurrent.futures.ThreadPoolExecutor(max_workers=counts))
    all_result = loop.run_until_complete(make_compare(gv.replica_hotbit, all_tokens, currency, currencyUSD, percent))
    loop.close()
    compare_result = rprep(all_result=all_result, exchanger='hotbit').result()
    print('hotbit_result', compare_result)
    ProfitExchanges.objects.filter(Q(buy_name__icontains='hotbit') | (
            Q(sell_name__icontains='hotbit') & ~Q(buy_name__icontains='idex') & ~Q(
        buy_name__icontains='hitbit')) & ~Q(buy_name__icontains='bilaxy')).delete()
    with transaction.atomic():
        for result in compare_result:
            pair = ProfitExchanges(pair=result['pair'], buy_name=result['buy_name'], buy=result['buy'],
                                   buy_ask=result['buy_ask'], buyurl=result['buyurl'], sell_name=result['sell_name'],
                                   sell=result['sell'], sell_bid=result['sell_bid'], percent=result['percent'],
                                   tokenid=result['tokenid'], sellurl=result['sellurl'],
                                   sell_symbol=result['sell_symbol'], contract=result['contract'])
            pair.save()
    return compare_result


async def init_compare_hotbit():
    while True:
        tstart = datetime.now()
        await compare_init()
        print('hotbit compare time: ', str(datetime.now() - tstart))

import asyncio
import concurrent.futures
import datetime
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


async def compare_markets(symbol, percent, currency, proxy):
    hotbit_deth = await get_hitbtc_depth(symbol[1], proxy)
    asks = []
    if hotbit_deth:
        for ask in hotbit_deth['ask']:
            asks.append([ask['price'], ask['size']])
        return ct(buy_from='hitbtc', buy_prices=asks, buy_volume=0, sell_to=symbol[3], sell_prices=symbol[4],
                  sell_volume=1, buy_symbol=symbol[1], sell_symbol=symbol[0],
                  contract=symbol[6], profit_percent=percent, currency=currency).compare()


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


# @sync_to_async
def hitbtc_profits():
    print('hitbtc_profits start', datetime.datetime.now())
    setting = Settings.objects.all()[0]
    percent = setting.market_percent / 100 * setting.market_koef
    all_symbols = _query(f'''WITH idex as (SELECT mi.exch_direction, mh.symbol, mh.decimals, 'idex' as site,  
        mi.highest_bid, mi.lowest_ask, tp.contract, mi.volume, mh.is_active FROM trusted_pairs tp 
        LEFT JOIN module_hitbtc mh ON mh.tsymbol = tp.tsymbol 
        LEFT JOIN module_idex mi ON mi.tsymbol = mh.tsymbol WHERE mi.exch_direction is not null and tp.is_active is true
         and mh.is_active is true and mi.is_active is true),  
        hotbit as (SELECT mhb.symbol, mh.symbol, mh.decimals, 'hotbit' as site,  
        mhb.sell, mhb.buy, tp.contract, mhb.volume, mh.is_active FROM trusted_pairs tp 
        LEFT JOIN module_hitbtc mh ON mh.tsymbol = tp.tsymbol 
        LEFT JOIN module_hotbit mhb ON mhb.tsymbol = mh.tsymbol WHERE mhb.exch_direction is not null and tp.is_active is true
         and mh.is_active is true  and mhb.is_active is true),
        kyber as (SELECT mk.exch_direction, mh.symbol, mh.decimals, 'kyber' as site, mk.highest_bid, mk.lowest_ask, 
        tp.contract, mk.volume, mh.is_active FROM trusted_pairs tp 
        LEFT JOIN module_hitbtc mh ON mh.tsymbol = tp.tsymbol 
        LEFT JOIN module_kyber mk ON mk.tsymbol = mh.tsymbol WHERE mk.exch_direction is not null and 
        tp.is_active is true and mh.is_active is true and mk.is_active is true ),
        uniswap as (SELECT mu.exch_direction, mh.symbol, mh.decimals, 'uniswap' as site, mu.highest_bid, mu.lowest_ask, 
        tp.contract, mu.volume , mh.is_active 
        FROM trusted_pairs tp 
        LEFT JOIN module_hitbtc mh ON mh.tsymbol = tp.tsymbol 
        LEFT JOIN module_uniswap mu ON mu.tsymbol = mh.tsymbol WHERE mu.exch_direction is not null and 
        tp.is_active is true and mh.is_active is true and mu.is_active is true)
        SELECT * FROM idex UNION ALL SELECT * FROM hotbit UNION ALL SELECT * FROM kyber UNION ALL SELECT * FROM uniswap;''')
    currency = Settings.objects.all().values()[0]['currency']
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    loop = asyncio.get_event_loop()
    loop.set_default_executor(concurrent.futures.ThreadPoolExecutor(max_workers=20))
    init_result = loop.run_until_complete(init_compare(all_symbols, percent, currency))
    print('hitbtc_profits end', datetime.datetime.now())
    compare_result = []
    for result in init_result:
        if result:
            pair = result['symbol'].replace('ETH', '').replace('BTC', '')
            sell_symbol = result['sell_symbol']
            buy_name = result['buy_from']
            buy = result['buy_price']
            sell_name = result['sell_to']
            sell = result['sell_price']
            percent = result['percent']
            contract = result['contract']
            tokenid = '0x0000000000000000000000000000000000000000000000000000000000000000'
            if 'hitbtc' in buy_name:
                buyurl = 'https://hitbtc.com/' + pair + '-to-btc'
            if 'hotbit' in buy_name:
                buyurl = 'https://www.hotbit.io/exchange?symbol=' + sell_symbol.replace('/', '_')
            if buy_name == 'idex':
                buyurl = 'https://exchange.idex.io/trading/' + pair + '-ETH'
            # if result[0][1] == 'BANKOR':
            #     buyurl = 'https://app.bancor.network/eth/swap?from=0xEeeeeEeeeEeEeeEeEeEeeEEEeeeeEeeeeeeeEEeE&to=' + \
            #              result[0][8]
            if buy_name == 'kyber':
                buyurl = 'https://kyberswap.com/swap/eth-' + pair
            if buy_name == 'uniswap':
                buyurl = 'https://app.uniswap.org/#/swap?outputCurrency=' + str(contract)
            # if result[0][1] == 'UNISWAP_ONE':
            #     buyurl = 'https://app.uniswap.org/#/swap?outputCurrency=' + str(result[0][8]) + '&use=v1'

            if 'hitbtc' in sell_name:
                sellurl = 'https://hitbtc.com/' + pair + '-to-btc'
            if 'hotbit' in sell_name:
                sellurl = 'https://www.hotbit.io/exchange?symbol=' + sell_symbol.replace('/', '_')
            if sell_name == 'idex':
                sellurl = 'https://exchange.idex.io/trading/' + pair + '-ETH'
            # if result[0][4] == 'BANKOR':
            #     sellurl = 'https://app.bancor.network/eth/swap?from=' + result[0][
            #         8] + '&to=0xEeeeeEeeeEeEeeEeEeEeeEEEeeeeEeeeeeeeEEeE'
            if sell_name == 'kyber':
                sellurl = 'https://kyberswap.com/swap/eth-' + pair
            if sell_name == 'uniswap':
                sellurl = 'https://app.uniswap.org/#/swap?outputCurrency=' + str(contract)
            # if result[0][4] == 'UNISWAP_ONE':
            #     sellurl = 'https://app.uniswap.org/#/swap?outputCurrency=' + str(result[0][8]) + '&use=v1'
            compare_result.append(
                {'pair': result['symbol'], 'buy_name': buy_name, 'buy': buy, 'sell_name': sell_name, 'sell': sell,
                 'percent': percent, 'tokenid': tokenid, 'buyurl': buyurl, 'sellurl': sellurl})
    loop.close()
    return compare_result

# async def hitbtc_profits_init():
#     while True:
#         await hitbtc_profits()
#
#
# if __name__ == '__main__':
#     hitbtc_profits()

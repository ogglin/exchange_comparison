import asyncio
import concurrent.futures
import json

import aiohttp
from aiohttp_socks import SocksConnector
from asgiref.sync import sync_to_async

from exchange_comparison.utils import _query
from exchange_pairs.models import Settings
from idex_module.models import Idex
from idex_module.services import idex_tikers_set


async def get_idex_depth(symbol, proxy):
    url = f"https://api.idex.io/v1/orderbook?market={symbol}-ETH&level=2&limit=20"
    socks_url = 'socks5://' + proxy[2] + ':' + proxy[3] + '@' + proxy[0] + ':' + proxy[1]
    connector = SocksConnector.from_url(socks_url)
    async with aiohttp.ClientSession(connector=connector) as session:
        async with session.get(url) as response:
            html = await response.text()
            jhtml = json.loads(html)
            if jhtml['code'] is None:
                return jhtml
            else:
                return None


async def compare_symbol(symbol, idex, percent):
    # print('/*************')
    # print(symbol)
    # print(idex)
    pair = symbol[0]
    tokenid = symbol[4]
    result = []
    # From idex to exch
    if symbol[2] > idex['ask'] > 0:
        sellurl = ''
        buy_name = 'IDEX'
        buyurl = 'https://exchange.idex.io/trading/' + pair + '-ETH'
        sell_name = symbol[1].lower()
        if sell_name == 'uniswap':
            sellurl = 'https://app.uniswap.org/#/swap?outputCurrency=' + str(tokenid)
        elif sell_name == 'kyber':
            sellurl = 'https://kyberswap.com/swap/eth-' + pair
        elif sell_name == 'bankor':
            sellurl = 'https://app.bancor.network/eth/swap?from=' + str(
                tokenid) + '&to=0xEeeeeEeeeEeEeeEeEeEeeEEEeeeeEeeeeeeeEEeE'
        elif sell_name == 'uniswap_one':
            sellurl = 'https://app.uniswap.org/#/swap?outputCurrency=' + str(tokenid) + '&use=v1'
        buy = idex['ask']
        sell = symbol[2]
        profit_percent = (sell - buy) / buy * 100
        result.append({'pair': pair, 'buy_name': buy_name, 'buy': buy, 'sell_name': sell_name, 'sell': sell,
                       'percent': profit_percent, 'tokenid': tokenid, 'buyurl': buyurl, 'sellurl': sellurl})
        # print(result)
    # From exch to idex
    if idex['bid'] > symbol[3] > 0:
        buyurl = ''
        buy_name = symbol[1].lower()
        if buy_name == 'uniswap':
            buyurl = 'https://app.uniswap.org/#/swap?outputCurrency=' + str(tokenid)
        elif buy_name == 'kyber':
            buyurl = 'https://kyberswap.com/swap/eth-' + pair
        elif buy_name == 'bankor':
            buyurl = 'https://app.bancor.network/eth/swap?from=0xEeeeeEeeeEeEeeEeEeEeeEEEeeeeEeeeeeeeEEeE&to=' + str(
                tokenid)
        elif buy_name == 'uniswap_one':
            'https://app.uniswap.org/#/swap?outputCurrency=' + str(tokenid) + '&use=v1'
        sell_name = 'IDEX'
        sellurl = 'https://exchange.idex.io/trading/' + pair + '-ETH'
        buy = symbol[3]
        sell = idex['bid']
        profit_percent = (sell - buy) / buy * 100
        result.append({'pair': pair, 'buy_name': buy_name, 'buy': buy, 'sell_name': sell_name, 'sell': sell,
                       'percent': profit_percent, 'tokenid': tokenid, 'buyurl': buyurl, 'sellurl': sellurl})
        # print(result)
    # print('*************/')
    return result


async def init_compare(all_symbols, all_idex, percent):
    async_tasks = []
    while len(all_idex) < 1 and len(all_symbols) < 1:
        await asyncio.sleep(0.2)
    for idex in all_idex:
        for symbol in all_symbols:
            if symbol[0] == idex['token'] and 'usd' not in idex['token'].lower():
                async_tasks.append(compare_symbol(symbol, idex, percent))
    results = await asyncio.gather(*async_tasks)
    return results


# @sync_to_async
def idex_profits():
    setting = Settings.objects.all()[0]
    percent = setting.market_percent / 100 * setting.market_koef
    # all_idex = _query("SELECT * FROM module_idex WHERE is_active is TRUE ORDER BY exch_direction;")
    all_symbols = _query(f'''WITH bankor as (
            SELECT mb.exch_direction, 'bankor' as site, mb.highest_bid, mb.lowest_ask, mb.link_id token_id, mb.volume FROM exchange_pairs 
            LEFT JOIN module_idex mi ON mi.id = idex_direction_id 
            LEFT JOIN module_bancor mb ON mb.id = bancor_direction_id
            WHERE idex_direction_id is not null and bancor_direction_id is not null ORDER BY hotbit_id
            ), kyber as (
            SELECT mk.exch_direction, 'kyber' as site, mk.highest_bid, mk.lowest_ask, mk.token_id, mk.volume FROM exchange_pairs 
            LEFT JOIN module_idex mi ON mi.id = idex_direction_id 
            LEFT JOIN module_kyber mk ON mk.id = kyber_direction_id
            WHERE idex_direction_id is not null and kyber_direction_id is not null ORDER BY exch_direction
            ), uniswap as (
            SELECT mu.exch_direction, 'uniswap' as site, mu.highest_bid, mu.lowest_ask, lower(mu.tokenid) token_id, mu.volume FROM exchange_pairs 
            LEFT JOIN module_idex mi ON mi.id = idex_direction_id 
            LEFT JOIN module_uniswap mu ON mu.id = uniswap_direction_id
            WHERE idex_direction_id is not null and uniswap_direction_id is not null ORDER BY exch_direction
            ) SELECT * FROM uniswap 
            UNION ALL SELECT * FROM bankor 
            UNION ALL SELECT * FROM kyber;''')
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    loop = asyncio.get_event_loop()
    loop.set_default_executor(concurrent.futures.ThreadPoolExecutor(max_workers=20))
    init_result = loop.run_until_complete(init_compare(all_symbols, idex_tikers_set, percent))
    compare_result = []
    for result in init_result:
        if len(result) > 0:
            for r in result:
                compare_result.append({'pair': r['pair'], 'buy_name': r['buy_name'], 'buy': r['buy'],
                                       'sell_name': r['sell_name'], 'sell': r['sell'], 'percent': r['percent'],
                                       'tokenid': r['tokenid'], 'buyurl': r['buyurl'], 'sellurl': r['sellurl']})
    loop.close()
    return compare_result

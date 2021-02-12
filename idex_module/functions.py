import asyncio
import concurrent.futures

from exchange_comparison.utils import _query
from exchange_pairs.models import Settings
from idex_module.models import Idex


async def compare_symbol(symbol, idex, percent):
    # print('/*************')
    # print(symbol)
    # print(idex)
    pair = symbol[0]
    tokenid = symbol[6]
    result = []
    # From idex to exch
    if symbol[4] > idex[2] + idex[2]*percent/100 > 0:
        sellurl = ''
        buy_name = 'IDEX'
        buyurl = 'https://exchange.idex.io/trading/' + pair + '-ETH'
        sell_name = symbol[3].upper()
        if sell_name == 'uniswap':
            sellurl = 'https://app.uniswap.org/#/swap?outputCurrency=' + str(tokenid)
        elif sell_name == 'kyber':
            sellurl = 'https://kyberswap.com/swap/eth-' + pair
        elif sell_name == 'bankor':
            sellurl = 'https://app.bancor.network/eth/swap?from=' + str(tokenid) + '&to=0xEeeeeEeeeEeEeeEeEeEeeEEEeeeeEeeeeeeeEEeE'
        elif sell_name == 'uniswap_one':
            sellurl = 'https://app.uniswap.org/#/swap?outputCurrency=' + str(tokenid) + '&use=v1'
        buy = idex[2]
        sell = symbol[4]
        profit_percent = (sell - buy) / buy * 100
        result.append({'pair': pair, 'buy_name': buy_name, 'buy': buy, 'sell_name': sell_name, 'sell': sell,
                                   'percent': profit_percent, 'tokenid': tokenid, 'buyurl': buyurl, 'sellurl': sellurl})
        # print(result)
    # From exch to idex
    if idex[3] > symbol[5] + symbol[5]/percent/100 > 0:
        buyurl = ''
        buy_name = symbol[3].upper()
        if buy_name == 'uniswap':
            buyurl = 'https://app.uniswap.org/#/swap?outputCurrency=' + str(tokenid)
        elif buy_name == 'kyber':
            buyurl = 'https://kyberswap.com/swap/eth-' + pair
        elif buy_name == 'bankor':
            buyurl = 'https://app.bancor.network/eth/swap?from=0xEeeeeEeeeEeEeeEeEeEeeEEEeeeeEeeeeeeeEEeE&to=' + str(tokenid)
        elif buy_name == 'uniswap_one':
            'https://app.uniswap.org/#/swap?outputCurrency=' + str(tokenid) + '&use=v1'
        sell_name = 'IDEX'
        sellurl = 'https://exchange.idex.io/trading/' + pair + '-ETH'
        buy = symbol[5]
        sell = idex[3]
        profit_percent = (sell - buy) / buy * 100
        result.append({'pair': pair, 'buy_name': buy_name, 'buy': buy, 'sell_name': sell_name, 'sell': sell,
                                   'percent': profit_percent, 'tokenid': tokenid, 'buyurl': buyurl, 'sellurl': sellurl})
        # print(result)
    # print('*************/')
    return result


async def init_compare(all_symbols, all_idex, percent):
    async_tasks = []
    for idex in all_idex:
        for symbol in all_symbols:
            if symbol[0] == idex[1]:
                async_tasks.append(compare_symbol(symbol, idex, percent))
    results = await asyncio.gather(*async_tasks)
    return results


def idex_profits():
    setting = Settings.objects.all()[0]
    percent = setting.market_percent / 100 * setting.market_koef
    all_idex = _query("SELECT * FROM module_idex WHERE volume >= 0")
    all_symbols = _query(f"WITH bankor as (SELECT mb.exch_direction, mh.symbol, mh.decimals, "
                         f"'bankor' as site, mb.highest_bid, mb.lowest_ask, mb.link_id token_id, mb.volume "
                         f"FROM exchange_pairs LEFT JOIN module_hotbit mh ON mh.id = hotbit_id "
                         f"LEFT JOIN module_bancor mb ON mb.id = bancor_direction_id "
                         f"WHERE hotbit_id is not null and bancor_direction_id is not null and mb.volume >= 1 "
                         f"ORDER BY hotbit_id), kyber as (SELECT mk.exch_direction, mh.symbol, mh.decimals, "
                         f"'kyber' as site, mk.highest_bid, mk.lowest_ask, mk.token_id, mk.volume FROM exchange_pairs "
                         f"LEFT JOIN module_hotbit mh ON mh.id = hotbit_id "
                         f"LEFT JOIN module_kyber mk ON mk.id = kyber_direction_id "
                         f"WHERE hotbit_id is not null and kyber_direction_id is not null and mk.volume >= 1 "
                         f"ORDER BY hotbit_id), uniswap as (SELECT mu.exch_direction, mh.symbol, mh.decimals, "
                         f"'uniswap' as site, mu.highest_bid, mu.lowest_ask, lower(mu.tokenid) token_id, mu.volume "
                         f"FROM exchange_pairs LEFT JOIN module_hotbit mh ON mh.id = hotbit_id "
                         f"LEFT JOIN module_uniswap mu ON mu.id = uniswap_direction_id "
                         f"WHERE hotbit_id is not null and uniswap_direction_id is not null and mu.volume >= 1 "
                         f"ORDER BY hotbit_id), uniswap_one as (SELECT muo.exch_direction, mh.symbol, mh.decimals, "
                         f"'uniswap_one' as site, muo.highest_bid, muo.lowest_ask, lower(muo.tokenid) token_id, "
                         f"muo.volume FROM exchange_pairs LEFT JOIN module_hotbit mh ON mh.id = hotbit_id "
                         f"LEFT JOIN module_uniswap_one muo ON muo.id = exchange_pairs.uniswap_one_direction_id "
                         f"WHERE hotbit_id IS NOT NULL AND uniswap_one_direction_id IS NOT NULL  AND muo.volume >=1 "
                         f"ORDER BY hotbit_id) SELECT * FROM uniswap "
                         f"UNION ALL SELECT * FROM bankor "
                         f"UNION ALL SELECT * FROM kyber "
                         f"UNION ALL SELECT * FROM uniswap_one;")
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    loop = asyncio.get_event_loop()
    loop.set_default_executor(concurrent.futures.ThreadPoolExecutor(max_workers=20))
    init_result = loop.run_until_complete(init_compare(all_symbols, all_idex, percent))
    compare_result = []
    for result in init_result:
        if len(result) > 0:
            # print(result)
            for r in result:
                compare_result.append({'pair': r['pair'], 'buy_name': r['buy_name'], 'buy': r['buy'],
                                       'sell_name': r['sell_name'], 'sell': r['sell'], 'percent': r['percent'],
                                       'tokenid': r['tokenid'], 'buyurl': r['buyurl'], 'sellurl': r['sellurl']})
    loop.close()
    return compare_result

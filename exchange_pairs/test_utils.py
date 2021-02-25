import asyncio
import concurrent.futures
import datetime

from asgiref.sync import async_to_sync, sync_to_async

from exchange_comparison.utils import _query, _query_cols
from exchange_pairs.models import SettingsModules
from hotbit_module.functions import get_hotbit_depth
from .utils import CompareToken as ct

proxys = [
    ['193.111.152.28', '16881', 'user53105', '3x7cyr'],
    ['185.161.211.209', '16881', 'user53105', '3x7cyr'],
    ['193.111.155.237', '16881', 'user53105', '3x7cyr'],
    ['193.111.152.168', '16881', 'user53105', '3x7cyr'],
    ['185.20.187.218', '16881', 'user53105', '3x7cyr'],
    ['193.111.154.67', '16881', 'user53105', '3x7cyr'],
    ['185.161.209.185', '16881', 'user53105', '3x7cyr'],
    ['185.36.189.145', '16881', 'user53105', '3x7cyr'],
    ['185.36.190.130', '16881', 'user53105', '3x7cyr'],
    ['193.111.152.90', '16881', 'user53105', '3x7cyr'],
    ['213.32.84.200', '11565', 'user53105', '3x7cyr'],
    ['213.32.84.143', '11565', 'user53105', '3x7cyr'],
    ['79.137.15.162', '11565', 'user53105', '3x7cyr'],
    ['213.32.84.176', '11565', 'user53105', '3x7cyr'],
    ['147.135.175.235', '11565', 'user53105', '3x7cyr'],
    ['178.32.67.197', '11565', 'user53105', '3x7cyr'],
    ['178.32.67.151', '11565', 'user53105', '3x7cyr'],
    ['213.32.84.202', '11565', 'user53105', '3x7cyr'],
    ['147.135.206.67', '11565', 'user53105', '3x7cyr'],
    ['213.32.84.46', '11565', 'user53105', '3x7cyr'],
]


async def to_compare(from_symbol, to_symbols, to_sell, proxy):
    hotbit_deth = await get_hotbit_depth(from_symbol[0], proxy)
    to_symbol = None
    for s in to_symbols:
        if from_symbol[1] == s[1]:
            to_symbol = s
    if to_symbol:
        return ct('hotbit', hotbit_deth['asks'], 0, to_sell, to_symbol[2], 1, from_symbol[1],
                  from_symbol[2], 1, 1).compare()
    else:
        return None


@async_to_sync
async def init_compares(compare, cnt):
    async_tasks = []
    cnt += 1
    if cnt >= len(proxys):
        cnt = 0
    if compare['idex']:
        print(compare)
    if compare['bancor']:
        print(compare)
    if compare['kyber']:
        print(compare)
    if compare['uniswap']:
        print(compare)
    if compare['uniswap_one']:
        print(compare)
    if compare['hotbit']:
        print(compare)
    if compare['hitbtc']:
        print(compare)
    # print(len(async_tasks))
    # results = await asyncio.gather(*async_tasks)
    # return results


def to_compare_check(columns, symbols):
    count = 0
    tsymbol = symbols[0]
    contact = symbols[1].lower()
    idex = None
    bancor = None
    kyber = None
    uniswap = None
    uniswap_one = None
    hotbit = None
    hitbtc = None
    for i, ex in enumerate(columns):
        if 'idex' == ex and symbols[i] is not None:
            idex = symbols[i]
            count += 1
        if 'bancor' == ex and symbols[i] is not None:
            bancor = symbols[i]
            count += 1
        if 'kyber' == ex and symbols[i] is not None:
            kyber = symbols[i]
            count += 1
        if 'uniswap' == ex and symbols[i] is not None:
            uniswap = symbols[i]
            count += 1
        if 'uniswap_one' == ex and symbols[i] is not None:
            uniswap_one = symbols[i]
            count += 1
        if 'hotbit' == ex and symbols[i] is not None:
            hotbit = symbols[i]
            count += 1
        if 'hitbtc' == ex and symbols[i] is not None:
            hitbtc = symbols[i]
            count += 1
    if count > 1:
        return {'tsymbol': tsymbol, 'contact': contact, 'idex': idex, 'bancor': bancor, 'kyber': kyber,
                'uniswap': uniswap, 'uniswap_one': uniswap_one, 'hotbit': hotbit, 'hitbtc': hitbtc}
    else:
        return None


# @async_to_sync
def init_test():
    compare_symbols, compare_columns = _query_cols(f'SELECT * FROM all_compare_tokens;')
    print('Symbols query ready:', datetime.datetime.now())
    all_compare = []
    for symbols in compare_symbols:
        compare = to_compare_check(compare_columns, symbols)
        if compare:
            all_compare.append(compare)
    print(all_compare[2])
    print(len(all_compare))
    init_compares(all_compare[2], 0)
    # print(result)
    # loop = asyncio.new_event_loop()
    # asyncio.set_event_loop(loop)
    # loop = asyncio.get_event_loop()
    # loop.set_default_executor(concurrent.futures.ThreadPoolExecutor(max_workers=20))
    # compare_results = loop.run_until_complete(init_compares())
    #
    # print(compare_results)
    # loop.close()

# init()

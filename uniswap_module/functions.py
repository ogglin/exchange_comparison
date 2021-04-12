import asyncio
import concurrent.futures
import datetime
import json
import multiprocessing
from functools import partial
from multiprocessing.pool import ThreadPool
from time import time as timer

import urllib3
from asgiref.sync import sync_to_async

from exchange_comparison.utils import _query

koef = 0.99


@sync_to_async
def get_uni_2():
    # print('start get tokens uniswap_v2: ' + str(datetime.datetime.now()))
    trusted_tokens = _query(
        f'''SELECT lower(tp.contract) contract, tp.tsymbol, mu.exch_direction token FROM trusted_pairs tp 
            LEFT JOIN module_uniswap mu ON lower(mu.tsymbol) = lower(tp.tsymbol) and tp.contract is not null 
            LEFT JOIN settings_modules ON settings_modules.module_name = 'uniswap' WHERE mu.exch_direction is not null 
            and tp.is_active is true AND mu.is_active is true AND length(tp.contract) > 40;''')
    ioloop = asyncio.new_event_loop()
    asyncio.set_event_loop(ioloop)
    ioloop.set_default_executor(concurrent.futures.ThreadPoolExecutor(max_workers=200))
    ioloop = asyncio.get_event_loop()
    results = ioloop.run_until_complete(asynchronous(trusted_tokens))
    ioloop.close()
    # print('end get tokens uniswap_v2: ' + str(datetime.datetime.now()))
    return results


async def asynchronous(trusted_tokens):
    tokens = []
    for i, t in enumerate(trusted_tokens):
        tkn = [t[0].lower(), t[1]]
        tokens.append(tkn)

    def fetch_url(lock, tokenid):
        http = urllib3.PoolManager()
        url_v2 = 'https://api.thegraph.com/subgraphs/name/uniswap/uniswap-v2'
        req = json.dumps({'query': '{token(id: "' + tokenid[0] + '"){ symbol totalLiquidity derivedETH } }'}).encode(
            'utf-8')
        try:
            response = http.request('POST', url_v2, body=req)
            return tokenid[0], json.loads(response.data.decode('utf-8'))['data']['token'], tokenid[1], None
        except Exception as e:
            print(e)
            return None, None, None, e

    start = timer()
    l = multiprocessing.Lock()
    func = partial(fetch_url, l)
    results = ThreadPool(100).map(func, tokens)
    uniswap_prices = []
    for tokenid, jData, tsymbol, error in results:
        if error is None:
            # print("fetched in %ss" % (timer() - start))
            if jData is not None and jData['totalLiquidity'] is not None and jData['derivedETH'] is not None:
                highest_bid = float(jData['derivedETH']) * koef
                lowest_ask = float(jData['derivedETH'])
                volume = float(jData['totalLiquidity'])
                token = jData['symbol']
                uniswap_prices.append([tsymbol, tokenid, 'uniswap', token, highest_bid, lowest_ask, volume])
        else:
            print("error fetching: ", error)

    # print("Elapsed Time: %s" % (timer() - start,), 'uniswap_prices_set length: ', len(uniswap_prices))
    return uniswap_prices

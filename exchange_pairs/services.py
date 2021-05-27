import asyncio
import time
from datetime import datetime

from asgiref.sync import sync_to_async

import exchange_comparison.global_vars as gv
from exchange_pairs.utils import GetTokens as gt
from uniswap_module.functions import get_uni_2


async def get_tokens():
    gv.uniswap_prices_set = await get_uni_2()
    gv.all_compared_tokens = gt(module='all', _all=True).tokens()
    gv.all_compared_tokens.extend(gv.uniswap_prices_set)
    return True


# async def set_all_compared_tokens():
#     loop = asyncio.new_event_loop()
#     asyncio.set_event_loop(loop)
#     loop = asyncio.get_event_loop()
#     result = loop.run_until_complete(get_tokens())
#     loop.close()
#     return result


async def init_all_compared_tokens():
    print('set compared_tokens start: ', str(datetime.now()))
    while True:
        start = datetime.now()
        await get_tokens()
        print('set compared_tokens time: ', str(datetime.now() - start))

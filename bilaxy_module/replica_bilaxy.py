import asyncio
import concurrent.futures
import math
import time
from datetime import datetime

from asgiref.sync import sync_to_async

import exchange_comparison.global_vars as gv
from exchange_pairs.utils import GetTokens as gt
from exchange_comparison.market_depth import get_bilaxy_depth

counts = len(gv.proxys1) * 10


async def get_depth(token, tsymbol, cnt):
    depth = await get_bilaxy_depth(token, cnt)
    direction = None
    if '_ETH' in token:
        direction = 'ETH'
    if '_BTC' in token:
        direction = 'BTC'
    if '_USD' in token:
        direction = 'USD'
    return {token: [depth, tsymbol, direction]}


async def init_make(tokens):
    async_tasks = []
    cnt = 0
    for token in tokens:
        async_tasks.append(get_depth(token[3], token[0], cnt))
        cnt += 1
        if cnt >= len(gv.proxys1):
            cnt = 0
    results = await asyncio.gather(*async_tasks)
    return results


@sync_to_async
def make_replica():
    replica = {}
    tokens = gt(module='bilaxy', _all=False).tokens()
    xlen = math.ceil(len(tokens) / counts)
    # print(len(tokens))
    for i in range(xlen):
        parts_tokens = []
        for hi, htoken in enumerate(tokens):
            if counts * i <= hi < counts * (i + 1):
                parts_tokens.append(htoken)
        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)
        loop = asyncio.get_event_loop()
        loop.set_default_executor(concurrent.futures.ThreadPoolExecutor(max_workers=counts))
        # print('bilaxy loop start', datetime.now())
        init_result = loop.run_until_complete(init_make(parts_tokens))
        # print('bilaxy loop end', datetime.now())
        loop.close()
        for res in init_result:
            replica.update(res)
        time.sleep(1)
    gv.replica_bilaxy = replica
    # print(gv.replica_bilaxy)
    # print(len(gv.replica_bilaxy))
    # print('//====================================//')
    return True


async def init_replica_bilaxy():
    print('bilaxy start replica')
    while True:
        tstart = datetime.now()
        await make_replica()
        print('bilaxy replica create time: ', str(datetime.now() - tstart))

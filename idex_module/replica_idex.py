import asyncio
import concurrent.futures
import math
import time
from datetime import datetime

from asgiref.sync import sync_to_async

import exchange_comparison.global_vars as gv
from exchange_pairs.utils import GetTokens as gt
from exchange_comparison.market_depth import get_idex_depth

counts = len(gv.proxys2) * 10


async def get_depth(token, tsymbol, cnt):
    depth = await get_idex_depth(token, cnt)
    direction = None
    if '-ETH' in token:
        direction = 'ETH'
    if '-BTC' in token:
        direction = 'BTC'
    if '-USD' in token:
        direction = 'USD'
    return {token: [depth, tsymbol, direction]}


async def init_make(tokens):
    async_tasks = []
    cnt = 0
    for token in tokens:
        async_tasks.append(get_depth(token[3], token[0], cnt))
        cnt += 1
        if cnt >= len(gv.proxys2):
            cnt = 0
    results = await asyncio.gather(*async_tasks)
    return results


@sync_to_async
def make_replica():
    replica = {}
    tokens = gt(module='idex', _all=False).tokens()
    xlen = math.ceil(len(tokens) / counts)
    for i in range(xlen):
        parts_tokens = []
        for hi, htoken in enumerate(tokens):
            if counts * i <= hi < counts * (i + 1):
                parts_tokens.append(htoken)
        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)
        loop = asyncio.get_event_loop()
        loop.set_default_executor(concurrent.futures.ThreadPoolExecutor(max_workers=counts))
        # print('idex loop start', datetime.now())
        init_result = loop.run_until_complete(init_make(parts_tokens))
        # print('idex loop end', datetime.now())
        loop.close()
        for res in init_result:
            replica.update(res)
        time.sleep(1)
    gv.replica_idex = replica
    # print(type(gv.replica_idex), len(gv.replica_idex))
    # print(gv.replica_idex)
    # print('//====================================//')


async def init_replica_idex():
    while True:
        tstart = datetime.now()
        await make_replica()
        print('idex replica create time: ', str(datetime.now() - tstart))

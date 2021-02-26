import asyncio
import concurrent.futures

from bancor_module.services import bankor_init
from exchange_comparison.services import exchange_set_init
from exchange_pairs.functions import exchanges_idex, exchanges_hotbit
from idex_module.services import idex_init, tikers_set_idex_init
from kyber_module.services import kyber_init
from uniswap_module.services import uniswap_v2_init, uniswap_v1_init


def init_start():
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    loop = asyncio.get_event_loop()
    loop.set_default_executor(concurrent.futures.ThreadPoolExecutor(max_workers=20))
    async_tasks = [
        # tikers_set_idex_init(),
        # idex_init(),
        # exchanges_idex(),
        # exchanges_hotbit(),
        # bankor_init(),
        # kyber_init(),
        uniswap_v2_init(),
        # uniswap_v1_init(),
        # exchange_set_init()
    ]
    loop.run_until_complete(asyncio.gather(*async_tasks))


if __name__ == '__main__':
    init_start()

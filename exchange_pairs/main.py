import asyncio
import concurrent.futures

from bancor_module.services import bankor_init
from exchange_comparison.services import exchange_set_init
from exchange_pairs.functions import exchanges_idex, exchanges_hotbit, exchanges_hitbtc
from hitbtc_module.functions import hitbtc_tiker_init
from idex_module.services import idex_init, tikers_set_idex_init
from idex_module.socket_services import get_wss
from kyber_module.services import kyber_init
from uniswap_module.services import uniswap_v2_init, uniswap_v1_init


def init_start():
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    loop = asyncio.get_event_loop()
    loop.set_default_executor(concurrent.futures.ThreadPoolExecutor(max_workers=20))
    async_tasks = [
        tikers_set_idex_init(),
        idex_init(),
        exchanges_idex(),
        exchanges_hotbit(),
        # hitbtc_tiker_init(),
        # exchanges_hitbtc(),
        bankor_init(),
        kyber_init(),
        uniswap_v2_init(),
        uniswap_v1_init(),
        exchange_set_init(),
        get_wss()
    ]
    loop.run_until_complete(asyncio.gather(*async_tasks))


def init_start_test():
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    loop = asyncio.get_event_loop()
    loop.set_default_executor(concurrent.futures.ThreadPoolExecutor(max_workers=20))
    async_tasks = [
        # tikers_set_idex_init(),
        # idex_init(),
        # exchanges_idex(),
        # exchanges_hotbit(),
        hitbtc_tiker_init(),
        # hitbtc_profits_init(),
        # bankor_init(),
        # kyber_init(),
        # uniswap_v2_init(),
        # uniswap_v1_init(),
        # exchange_set_init()
    ]
    loop.run_until_complete(asyncio.gather(*async_tasks))


if __name__ == '__main__':
    init_start()

import asyncio
import concurrent.futures
import threading
from multiprocessing import Process

from bancor_module.services import bankor_init
from exchange_pairs.functions import exchanges_init
from idex_module.services import idex_init
from kyber_module.services import kyber_init
from uniswap_module.services import uniswap_v2_init, uniswap_v1_init


def init_start():
    # loop = asyncio.get_running_loop()
    # async_tasks = [
    #     exchanges_init(),
    #     idex_init(),
    #     bankor_init(),
    #     kyber_init(),
    #     uniswap_v2_init(),
    #     uniswap_v1_init(),
    # ]
    # results = await asyncio.gather(*async_tasks)

    Process(target=exchanges_init()).start()
    Process(target=idex_init()).start()
    Process(target=bankor_init()).start()
    Process(target=kyber_init()).start()
    Process(target=uniswap_v2_init()).start()
    Process(target=uniswap_v1_init()).start()

    # exthread = threading.Thread(target=exchanges_init())
    # ithread = threading.Thread(target=idex_init())
    # bthread = threading.Thread(target=bankor_init())
    # kthread = threading.Thread(target=kyber_init())
    # uhread = threading.Thread(target=uniswap_v2_init())
    # uothread = threading.Thread(target=uniswap_v1_init())
    # exthread.start()
    # ithread.start()
    # bthread.start()
    # kthread.start()
    # uhread.start()
    # uothread.start()

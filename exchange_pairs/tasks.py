from datetime import timedelta

from celery.task import task, periodic_task
from celery.signals import celeryd_after_setup, celeryd_init

from bancor_module.services import bankor_init
from exchange_pairs.functions import exchanges_init
from idex_module.services import idex_init
from kyber_module.services import kyber_init
from uniswap_module.services import uniswap_v1_init, uniswap_v2_init

uniswap_v1 = True
uniswap_v2 = True
kyber = True
idex = True
hotbit = True
bankor = True
exchanges = True


@periodic_task(queue='uniswap_one', options={'queue': 'uniswap_one'}, ignore_result=True,
               run_every=(timedelta(seconds=11)))
def uniswap_one_currencies_update():
    global uniswap_v1
    if uniswap_v1:
        uniswap_v1 = False
        while True:
            uniswap_v1_init()
    # try:
    #
    # except:
    #     print("Unexpected error:", sys.exc_info()[0])
    #     raise


@periodic_task(queue='uniswap', options={'queue': 'uniswap'}, ignore_result=True, run_every=(timedelta(seconds=11)))
def uniswap_currencies_update():
    global uniswap_v2
    if uniswap_v2:
        uniswap_v2 = False
        while True:
            uniswap_v2_init()
    # try:
    #     pass
    # except:
    #     print("Unexpected error:", sys.exc_info()[0])
    #     raise


@periodic_task(queue='kyber', options={'queue': 'kyber'}, ignore_result=True, run_every=(timedelta(seconds=11)))
def kyber_currencies_update():
    global kyber
    if kyber:
        kyber = False
        while True:
            kyber_init()
    # try:
    #     pass
    # except:
    #     print("Unexpected error:", sys.exc_info()[0])
    #     raise


@periodic_task(queue='bancor', options={'queue': 'bancor'}, ignore_result=True, run_every=(timedelta(seconds=11)))
def bancor_currencies_update():
    global bankor
    if bankor:
        bankor = False
        while True:
            bankor_init()
    # try:
    #     pass
    # except:
    #     print("Unexpected error:", sys.exc_info()[0])
    #     raise


@periodic_task(queue='idex', options={'queue': 'idex'}, ignore_result=True, run_every=(timedelta(seconds=11)))
def idex_currencies_update():
    global idex
    if idex:
        idex = False
        while True:
            idex_init()
    # try:
    #     pass
    # except:
    #     print("Unexpected error:", sys.exc_info()[0])
    #     raise


@periodic_task(queue='exchanges', options={'queue': 'exchanges'}, ignore_result=True, run_every=(timedelta(seconds=11)))
def exchanges_currencies_update():
    global exchanges
    if exchanges:
        exchanges = False
        while True:
            exchanges_init()
    # try:
    #     pass
    # except:
    #     print("Unexpected error:", sys.exc_info()[0])
    #     raise


# uniswap_one_currencies_update.apply_async((), retry=False)
# uniswap_currencies_update.apply_async((), retry=False)
# kyber_currencies_update.apply_async((), retry=False)
# bancor_currencies_update.apply_async((), retry=False)
# idex_currencies_update.apply_async((), retry=False)
# hotbit_currencies_update.apply_async((), retry=False)


@celeryd_after_setup.connect
def setup_direct_queue(sender, instance, **kwargs):
    queue_name = '{0}.dq'.format(sender)  # sender is the nodename of the worker
    print('setup_direct_queue')
    print(queue_name)
    # instance.app.amqp.queues.select_add(queue_name)


@celeryd_init.connect
def start_tasks(sender=None, conf=None, **kwargs):
    print('worker start', sender)
    # uniswap_one_currencies_update()
    # uniswap_currencies_update()
    # kyber_currencies_update()
    # bancor_currencies_update()
    # idex_currencies_update()
    # hotbit_currencies_update()

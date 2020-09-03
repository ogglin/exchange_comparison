import sys
from datetime import timedelta

from celery.task import periodic_task

from .services import set_all_currencies


@periodic_task(run_every=(timedelta(seconds=20)))
def currencies_uniswap_update():
    try:
        print('Uniswap collect data try')
        set_all_currencies()
        print('Uniswap data collected')
    except:
        print("Unexpected error:", sys.exc_info()[0])
        raise

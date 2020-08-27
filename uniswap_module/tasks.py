import sys
from datetime import timedelta

from celery.task import periodic_task

from .services import set_all_currencies


@periodic_task(run_every=(timedelta(seconds=20)))
def currencies_beat_update():
    try:
        print('try collect Uniswap data')
        set_all_currencies()
        print('Uniswap data collected')
    except:
        print("Unexpected error:", sys.exc_info()[0])
        raise

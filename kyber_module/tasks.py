import sys
from datetime import timedelta

from celery.task import periodic_task

from exchange_comparison._celery import app
from .services import set_currencies


@periodic_task(run_every=(timedelta(seconds=30)))
def currencies_beat_update():
    try:
        print('try collect Kyber update')
        set_currencies()
        print('Kyber data collected')
    except:
        print("Unexpected error:", sys.exc_info()[0])
        raise

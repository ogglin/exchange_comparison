import sys
from datetime import timedelta

from celery.task import periodic_task

from exchange_comparison._celery import app
from .services import set_currencies


@periodic_task(run_every=(timedelta(seconds=5)))
def currencies_kyber_update():
    try:
        print('Kyber collect update try')
        set_currencies()
        print('Kyber data collected')
    except:
        print("Unexpected error:", sys.exc_info()[0])
        raise

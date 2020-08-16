import sys
from datetime import timedelta

from celery.task import periodic_task

from exchange_comparison._celery import app
from .services import set_currencies


@periodic_task(run_every=(timedelta(seconds=45)))
def currencies_beat_update():
    try:
        print('try collect Bancor update')
        set_currencies()
        print('Bancor data collected')
    except:
        print("Unexpected error:", sys.exc_info()[0])
        raise

import sys
from datetime import timedelta

from exchange_comparison._celery import app
from celery.task import periodic_task

from .services import set_currencies


@periodic_task(run_every=(timedelta(seconds=2)))
# @app.task()
def bancor_currencies_update():
    try:
        print('Bancor collect update try')
        set_currencies()
        print('Bancor data collected')
    except:
        print("Unexpected error:", sys.exc_info()[0])
        raise

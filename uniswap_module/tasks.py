import sys
from datetime import timedelta

from celery.task import periodic_task
from exchange_comparison._celery import app
from .services import set_all_currencies


@periodic_task(run_every=(timedelta(seconds=70)), queue='high',
               options={'queue': 'high'})
# @app.task()
def uniswap_currencies_update():
    try:
        print('Uniswap collect data try')
        set_all_currencies()
        print('Uniswap data collected')
    except:
        print("Unexpected error:", sys.exc_info()[0])
        raise

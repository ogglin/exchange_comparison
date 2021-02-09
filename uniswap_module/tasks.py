import sys
from datetime import timedelta

from celery.task import periodic_task

from .services import set_all_currencies


@periodic_task(run_every=(timedelta(seconds=200)), queue='uniswap', options={'uniswap': 'uniswap'}, ignore_result=True)
# @app.task()
def uniswap_currencies_update():
    try:
        print('Uniswap collect data try')
        set_all_currencies()
        print('Uniswap data collected')
    except:
        print("Unexpected error:", sys.exc_info()[0])
        raise

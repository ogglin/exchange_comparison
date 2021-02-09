import datetime
import sys

from celery.task import periodic_task, task

from .services import uniswap_init


# @periodic_task(run_every=(timedelta(seconds=200)), queue='uniswap', options={'uniswap': 'uniswap'}, ignore_result=True)
@task(queue='uniswap', options={'uniswap': 'uniswap'}, ignore_result=True)
def uniswap_currencies_update():
    try:
        uniswap_init()
    except:
        print("Unexpected error:", sys.exc_info()[0])
        raise

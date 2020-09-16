import sys
from datetime import timedelta

from celery.task import periodic_task
from exchange_comparison._celery import app
from .services import set_currencies


# @app.task
# def currencies_update():
#     print('collect Idex update')
#     set_currencies()

@periodic_task(run_every=(timedelta(seconds=5)), queue='normal',
               options={'queue': 'normal'})
# @app.task()
def idex_currencies_update():
    try:
        print('Idex collect update try')
        set_currencies()
        print('Idex data collected')
    except:
        print("Unexpected error:", sys.exc_info()[0])
        raise

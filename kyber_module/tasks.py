import sys
from datetime import timedelta

from celery.task import periodic_task

from exchange_comparison._celery import app
from .services import set_currencies


@periodic_task(run_every=(timedelta(seconds=10)), queue='low',
               options={'queue': 'low'})
# @app.task()
def kyber_currencies_update():
    try:
        print('Kyber collect update try')
        set_currencies()
        print('Kyber data collected')
    except:
        print("Unexpected error:", sys.exc_info()[0])
        raise

import sys
from datetime import timedelta

from celery.task import periodic_task

from exchange_comparison._celery import app
from .services import set_currencies


@periodic_task(run_every=(timedelta(seconds=10)), queue='kyber', options={'queue': 'kyber'}, ignore_result=True)
# @app.task()
def kyber_currencies_update():
    try:
        set_currencies()
    except:
        print("Unexpected error:", sys.exc_info()[0])
        raise

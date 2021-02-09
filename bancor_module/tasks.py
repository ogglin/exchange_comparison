import sys
from datetime import timedelta

from exchange_comparison._celery import app
from celery.task import periodic_task

from .services import set_currencies


@periodic_task(run_every=(timedelta(seconds=10)), queue='bancor',
               options={'queue': 'bancor'})
# @app.task()
def bancor_currencies_update():
    try:
        set_currencies()
    except:
        print("Unexpected error:", sys.exc_info()[0])
        raise

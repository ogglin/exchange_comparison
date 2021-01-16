import sys
from datetime import timedelta

from celery.task import periodic_task

from .functions import set_currencies


@periodic_task(run_every=(timedelta(seconds=10)), queue='normal',
               options={'queue': 'normal'})
def hotbit_currencies_update():
    try:
        set_currencies()
    except:
        print("Unexpected error:", sys.exc_info()[0])
        raise

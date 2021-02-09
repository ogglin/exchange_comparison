import sys
from datetime import timedelta

from celery.task import periodic_task

from .services import set_currencies


@periodic_task(run_every=(timedelta(seconds=7)), queue='idex',
               options={'queue': 'idex'})
def idex_currencies_update():
    try:
        set_currencies()
    except:
        print("Unexpected error:", sys.exc_info()[0])
        raise

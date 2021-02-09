import datetime
import sys
from datetime import timedelta

from celery.task import periodic_task, task

from .services import idex_init


# @periodic_task(run_every=(timedelta(seconds=7)), queue='idex', options={'queue': 'idex'}, ignore_result=True)
@task(queue='idex', options={'queue': 'idex'}, ignore_result=True)
def idex_currencies_update():
    try:
        idex_init()
    except:
        print("Unexpected error:", sys.exc_info()[0])
        raise

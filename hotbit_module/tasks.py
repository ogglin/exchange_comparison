import datetime
import sys
from datetime import timedelta

from celery.task import periodic_task, task

from .functions import hotbit_init


# @periodic_task(run_every=(timedelta(seconds=7)), queue='hotbit', options={'queue': 'hotbit'}, ignore_result=True)
@task(ignore_result=True, queue='hotbit', options={'queue': 'hotbit'})
def hotbit_profits():
    try:
        hotbit_init()
    except:
        print("Unexpected error:", sys.exc_info()[0])
        raise


# @periodic_task(run_every=(timedelta(seconds=600)), queue='high',
#                options={'queue': 'high'})
# def hotbit_currencies_update():
#     try:
#         set_currencies()
#     except:
#         print("Unexpected error:", sys.exc_info()[0])
#         raise

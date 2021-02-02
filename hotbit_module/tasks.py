import sys
from datetime import timedelta

from celery.task import periodic_task

from .functions import set_currencies, save_profits


@periodic_task(run_every=(timedelta(seconds=15)), queue='high',
               options={'queue': 'high'})
def hotbit_profits():
    try:
        save_profits()
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

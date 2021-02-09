import datetime
import sys

from celery.task import task

from .services import bankor_init


# @periodic_task(run_every=(timedelta(seconds=10)), queue='bancor', options={'queue': 'bancor'}, ignore_result=True)
@task(queue='bancor', options={'queue': 'bancor'}, ignore_result=True)
def bancor_currencies_update():
    try:
        print('start bancor: ' + str(datetime.datetime.now()))
        bankor_init()
        print('end bancor: ' + str(datetime.datetime.now()))
    except:
        print("Unexpected error:", sys.exc_info()[0])
        raise

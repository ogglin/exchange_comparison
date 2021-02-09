import sys

from celery.task import periodic_task, task

from .services import kyber_init


# @periodic_task(run_every=(timedelta(seconds=10)), queue='kyber', options={'queue': 'kyber'}, ignore_result=True)
@task(queue='kyber', options={'queue': 'kyber'}, ignore_result=True)
def kyber_currencies_update():
    try:
        # kyber_init()
        pass
    except:
        print("Unexpected error:", sys.exc_info()[0])
        raise

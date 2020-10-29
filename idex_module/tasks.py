import sys
from datetime import datetime, timedelta

from celery.task import periodic_task
from exchange_comparison._celery import app
from .services import set_currencies
from .socket_services import get_wss


@app.task(bind=True)
def websock(self):
    print('Try Idex websocket connect ' + str(datetime.now() + timedelta(seconds=10)))
    get_wss()


started_at = datetime.utcnow() + timedelta(hours=3, seconds=10)
print(datetime.utcnow() + timedelta(hours=3, seconds=10))
print(datetime.now() + timedelta(seconds=10))
websock.apply_async(eta=started_at)


@periodic_task(run_every=(timedelta(seconds=5)), queue='normal',
               options={'queue': 'normal'})
def idex_currencies_update():
    try:
        set_currencies()
    except:
        print("Unexpected error:", sys.exc_info()[0])
        raise

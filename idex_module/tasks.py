import sys
from datetime import datetime, timedelta

from celery.task import periodic_task
from exchange_comparison._celery import app
from .services import set_currencies
from .socket_services import get_wss


@app.task
def websock():
    print('Idex websocket connect try')
    get_wss()


today = datetime.utcnow() + timedelta(seconds=5)
websock.apply_async((), eta=today)


@periodic_task(run_every=(timedelta(seconds=5)), queue='normal',
               options={'queue': 'normal'})
def idex_currencies_update():
    try:
        print('Idex collect update try')
        set_currencies()
        print('Idex data collected')
    except:
        print("Unexpected error:", sys.exc_info()[0])
        raise

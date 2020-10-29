import sys
from datetime import datetime, timedelta

from celery.task import periodic_task
from exchange_comparison._celery import app
from .services import set_currencies
from .socket_services import get_wss


@app.task(bind=True)
# @app.shared_task(bind=True)
def websock(time):
    print('Try Idex websocket connect' + time)
    get_wss()


started_at = datetime.utcnow() + timedelta(seconds=5)
websock.apply_async((str(started_at), ), eta=started_at)


@periodic_task(run_every=(timedelta(seconds=5)), queue='normal',
               options={'queue': 'normal'})
def idex_currencies_update():
    try:
        set_currencies()
    except:
        print("Unexpected error:", sys.exc_info()[0])
        raise

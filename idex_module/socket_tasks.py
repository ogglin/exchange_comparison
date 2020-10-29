from datetime import datetime, timedelta

from exchange_comparison._celery import app
from .socket_services import get_wss


@app.task(bind=True, task_acks_late=True, worker_prefetch_multiplier=1)
def websock(*args, **kwargs):
    print('Try Idex websocket connect ' + str(datetime.utcnow() + timedelta(hours=3)))
    get_wss()


started_at = datetime.utcnow() + timedelta(hours=3, seconds=30)
websock.apply_async((), countdown=30)



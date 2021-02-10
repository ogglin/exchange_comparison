from __future__ import absolute_import, unicode_literals

import os
from datetime import timedelta

from celery import Celery
from celery.schedules import crontab
from kombu import Exchange, Queue

from exchange_comparison import settings

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'exchange_comparison.settings')

app = Celery('exchange_comparison')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)

app.conf.task_default_queue = 'normal'
app.conf.task_queues = {
    Queue('normal', Exchange('normal'), routing_key='normal'),
    Queue('idex', Exchange('idex'), routing_key='idex'),
    Queue('uniswap', Exchange('uniswap'), routing_key='uniswap'),
    Queue('uniswap_one', Exchange('uniswap_one'), routing_key='uniswap_one'),
    Queue('bancor', Exchange('bancor'), routing_key='bancor'),
    Queue('kyber', Exchange('kyber'), routing_key='kyber'),
    Queue('hotbit', Exchange('hotbit'), routing_key='hotbit'),
}
app.conf.task_default_exchange = 'tasks'
app.conf.task_default_exchange_type = 'topic'
app.conf.task_default_routing_key = 'task.normal'


task_routes = {
    # 'idex_module.tasks.*': {'queue': 'idex'},
    # 'uniswap_module.tasks.*': {'queue': 'uniswap'},
    # 'bancor_module.tasks.*': {'queue': 'bancor'},
    # 'kyber_module.tasks.*': {'queue': 'kyber'},
    # 'hotbit_module.tasks.*': {'queue': 'hotbit'},
}

# celery beat tasks
app.conf.beat_schedule = {
    'tokens_update-1-minute': {
        'task': 'exchange_comparison.tasks.tokens_update',
        'schedule': crontab(minute='*/1'),
    },
    'uniswap_one_currencies_update': {
        'task': 'exchange_pairs.tasks.uniswap_one_currencies_update',
        'schedule': timedelta(seconds=10),
    },
    'uniswap_currencies_update': {
        'task': 'exchange_pairs.tasks.uniswap_currencies_update',
        'schedule': timedelta(seconds=10),
    },
    'kyber_currencies_update': {
        'task': 'exchange_pairs.tasks.kyber_currencies_update',
        'schedule': timedelta(seconds=10),
    },
    'bancor_currencies_update': {
        'task': 'exchange_pairs.tasks.bancor_currencies_update',
        'schedule': timedelta(seconds=10),
    },
    'idex_currencies_update': {
        'task': 'exchange_pairs.tasks.idex_currencies_update',
        'schedule': timedelta(seconds=10),
    },
    'hotbit_currencies_update': {
        'task': 'exchange_pairs.tasks.hotbit_currencies_update',
        'schedule': timedelta(seconds=10),
    }
    # 'websocket_run': {
    #     'task': 'idex_module.socket_tasks.websock',
    #     'schedule': crontab(minute='*/1'),
    # },
}

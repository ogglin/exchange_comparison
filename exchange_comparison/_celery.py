from __future__ import absolute_import, unicode_literals

import os

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
    Queue('high', Exchange('high'), routing_key='high'),
    Queue('normal', Exchange('normal'), routing_key='normal'),
    Queue('low', Exchange('low'), routing_key='low'),
}
app.conf.task_default_exchange = 'tasks'
app.conf.task_default_exchange_type = 'topic'
app.conf.task_default_routing_key = 'task.normal'

task_routes = {
    'idex_module.tasks.*': {'queue': 'normal'},
    'uniswap_module.tasks.*': {'queue': 'high'},
    'bancor_module.tasks.*': {'queue': 'low'},
    'kyber_module.tasks.*': {'queue': 'low'},
}

# celery beat tasks
app.conf.beat_schedule = {
    'tokens_update-1-minute': {
        'task': 'exchange_comparison.tasks.tokens_update',
        'schedule': crontab(minute='*/1'),
    },
}

from __future__ import absolute_import, unicode_literals
import os
from celery import Celery
from celery.schedules import crontab

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'exchange_comparison.settings')

app = Celery('exchange_comparison')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()

# celery beat tasks
app.conf.beat_schedule = {
    # 'send-span-every-1-minute': {
    #     'task': 'exchange_comparison.tasks.hello_world',
    #     'schedule': crontab(minute='*/1'),
    # },
}

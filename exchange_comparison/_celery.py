from __future__ import absolute_import, unicode_literals
import os
from celery import Celery
from celery.schedules import crontab

from exchange_comparison import settings

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'exchange_comparison.settings')

app = Celery('exchange_comparison')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)

# celery beat tasks
app.conf.beat_schedule = {
    'tokens_update-1-minute': {
        'task': 'exchange_comparison.tasks.tokens_update',
        'schedule': crontab(minute='*/1'),
    },
}

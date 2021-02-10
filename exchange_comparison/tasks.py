import sys
from datetime import timedelta

from celery.signals import celeryd_init
from celery.task import periodic_task, task
from django.core.mail import send_mail

from bancor_module.services import bankor_init
from exchange_comparison._celery import app
from hotbit_module.functions import hotbit_init
from idex_module.services import idex_init
from kyber_module.services import kyber_init
from send_mail.models import Contacts
from send_mail.services import send
from uniswap_module.services import uniswap_v1_init, uniswap_v2_init
from .services import token_set, token_exchange_set


@periodic_task(run_every=(timedelta(minutes=120)), ignore_result=True)
def token_exchange():
    try:
        print('Try set exchange tokens')
        token_exchange_set()
        print('Tokens exchange set')
    except:
        print("Unexpected error:", sys.exc_info()[0])
        raise


# @task(queue='uniswap_one', options={'queue': 'uniswap_one'}, ignore_result=True)
@periodic_task(queue='uniswap_one', options={'queue': 'uniswap_one'}, ignore_result=True)
async def uniswap_one_currencies_update():
    while True:
        uniswap_v1_init()
    # try:
    #
    # except:
    #     print("Unexpected error:", sys.exc_info()[0])
    #     raise


@periodic_task(queue='uniswap', options={'queue': 'uniswap'}, ignore_result=True)
async def uniswap_currencies_update():
    while True:
        uniswap_v2_init()
    # try:
    #     pass
    # except:
    #     print("Unexpected error:", sys.exc_info()[0])
    #     raise


@periodic_task(queue='kyber', options={'queue': 'kyber'}, ignore_result=True)
async def kyber_currencies_update():
    while True:
        kyber_init()
    # try:
    #     pass
    # except:
    #     print("Unexpected error:", sys.exc_info()[0])
    #     raise


@periodic_task(queue='idex', options={'queue': 'idex'}, ignore_result=True)
async def idex_currencies_update():
    while True:
        idex_init()
    # try:
    #     pass
    # except:
    #     print("Unexpected error:", sys.exc_info()[0])
    #     raise


@periodic_task(queue='hotbit', options={'queue': 'hotbit'})
async def hotbit_currencies_update():
    while True:
        hotbit_init()
    # try:
    #     pass
    # except:
    #     print("Unexpected error:", sys.exc_info()[0])
    #     raise


@periodic_task(queue='bancor', options={'queue': 'bancor'})
async def bancor_currencies_update():
    while True:
        bankor_init()
    # try:
    #     pass
    # except:
    #     print("Unexpected error:", sys.exc_info()[0])
    #     raise


@app.task()
def tokens_update():
    try:
        print('Try set new tokens')
        token_set()
        print('Tokens data collected')
    except:
        print("Unexpected error:", sys.exc_info()[0])
        raise


@app.task()
def send_spam_email(user_email):
    send(user_email)


@app.task()
def send_beat_email():
    for contact in Contacts.objects.all():
        send_mail(
            'Это рассылка писем',
            'Рассылка важной информации каждую минуту',
            'info@exchc.ru',
            [contact.email],
            fail_silently=False,
        )


uniswap_one_currencies_update.apply_async((), retry=False)
uniswap_currencies_update.apply_async((), retry=False)
kyber_currencies_update.apply_async((), retry=False)
bancor_currencies_update.apply_async((), retry=False)
idex_currencies_update.apply_async((), retry=False)
hotbit_currencies_update.apply_async((), retry=False)

# from celery.signals import celeryd_after_setup


# @celeryd_after_setup.connect
# def setup_direct_queue(sender, instance, **kwargs):
#     queue_name = '{0}.dq'.format(sender)  # sender is the nodename of the worker
#     print('setup_direct_queue')
#     print(queue_name)
#     # instance.app.amqp.queues.select_add(queue_name)
#
#
# @celeryd_init.connect
# def start_tasks(sender=None, conf=None, **kwargs):
#     print('worker start', sender)
#     # uniswap_one_currencies_update()
#     # uniswap_currencies_update()
#     # kyber_currencies_update()
#     # bancor_currencies_update()
#     # idex_currencies_update()
#     # hotbit_currencies_update()

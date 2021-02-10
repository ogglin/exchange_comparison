import sys
from datetime import timedelta

from celery.task import periodic_task
from django.core.mail import send_mail

from exchange_comparison._celery import app
from send_mail.models import Contacts
from send_mail.services import send
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

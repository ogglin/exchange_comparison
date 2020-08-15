from celery import shared_task
from django.core.mail import send_mail

from exchange_comparison._celery import app
from send_mail.models import Contacts
from send_mail.services import send


@shared_task
def hello_world():
    print('Hello World!')


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

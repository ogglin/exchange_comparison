from django.core.mail import send_mail


def send(user_mail):
    send_mail(
        'Это рассылка писем',
        'Рассылка важной информации',
        'info@exchc.ru',
        [user_mail],
        fail_silently=False,
    )

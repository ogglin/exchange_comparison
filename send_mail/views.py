from django.views.generic import CreateView
from .models import Contacts
from .forms import ContactForm
from exchange_comparison.tasks import send_spam_email


# Create your views here.
from .services import send


class ContactView(CreateView):
    """Email Form"""
    model = Contacts
    form_class = ContactForm
    success_url = '/'
    template_name = 'main/contact.html'

    def form_valid(self, form):
        form.save()
        # send(form.instance.email)
        send_spam_email.delay(form.instance.email)
        return super().form_valid(form)

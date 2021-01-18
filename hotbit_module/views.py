from django.shortcuts import render

from exchange_comparison.services import token_exchange_set
from .functions import set_currencies


# Create your views here.
def hotbit(request):
    # set_currencies()
    token_exchange_set()
    return render(request)

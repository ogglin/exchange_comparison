from django.shortcuts import render
from .socket_services import *


# Create your views here.
def idex(request):
    data = get_wss()
    return render(request, 'idex/idex.html', {'data': data})

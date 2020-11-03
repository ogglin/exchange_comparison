from django.shortcuts import render

# Create your views here.
from uniswap_module.services import set_all_currencies


def idex(request):
    data = set_all_currencies()
    return render(request, 'idex/idex.html', {'data': data})

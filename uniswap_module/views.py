import json

import requests
from rest_framework.response import Response
from rest_framework.views import APIView

# Create your views here.
from exchange_pairs.models import TrustedPairs
from uniswap_module.models import UniswapOne, Uniswap
from uniswap_module.services import uniswap_v1_init


class uniswap(APIView):
    # token_exchange_set()

    def get(self, request):
        data = uniswap_v1_init()
        return Response(data)

    def post(self, request):
        data = UniswapOne.objects.all()
        return Response(data)

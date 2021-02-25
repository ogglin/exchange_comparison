import json

import requests
from rest_framework.response import Response
from rest_framework.views import APIView

from exchange_pairs.models import ProfitExchanges
from hotbit_module.functions import hotbit_profits


def get_profits():
    return ProfitExchanges.objects.all()


class hitbtc(APIView):
    # token_exchange_set()

    def get(self, request):
        # print('start: ' + str(datetime.datetime.now()))
        if request.GET['symbol']:
            url = "https://api.hotbit.io/api/v1/order.depth?interval=1e-8&&limit=20&market=" + request.GET['symbol']
        else:
            url = "https://api.hotbit.io/api/v1/order.depth?interval=1e-8&&limit=20&market="
        payload = {}
        headers = {}
        response = requests.request("GET", url, headers=headers, data=payload)
        # print('end: ' + str(datetime.datetime.now()))
        return Response(json.loads(response.text))

    def post(self, request):
        hotbit_result = hotbit_profits()
        return Response(hotbit_result)

import requests
import json

from rest_framework.response import Response
from rest_framework.views import APIView


# Create your views here.

class hotbit(APIView):
    # token_exchange_set()

    def get(self, request):
        if request.GET['symbol']:
            url = "https://api.hotbit.io/api/v1/order.depth?interval=1e-8&&limit=20&market="+request.GET['symbol']
        else:
            url = "https://api.hotbit.io/api/v1/order.depth?interval=1e-8&&limit=20&market="
        payload = {}
        headers = {}
        response = requests.request("GET", url, headers=headers, data=payload)
        return Response(json.loads(response.text))

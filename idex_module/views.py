from rest_framework.response import Response
from rest_framework.views import APIView

from .functions import idex_profits


# Create your views here.


class idex(APIView):

    def get(self, request):
        # hotbit_result = hotbit_profits()
        idex_result = idex_profits()
        results = []
        # idex_init()
        # exchanges_init()
        # for result in hotbit_result:
        #     results.append(result)
        for result in idex_result:
            results.append(result)
        return Response(results)

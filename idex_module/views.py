from rest_framework.response import Response
from rest_framework.views import APIView

from .functions import idex_profits


# Create your views here.
class idex(APIView):

    def get(self, request):
        idex_result = idex_profits()
        return Response(idex_result)

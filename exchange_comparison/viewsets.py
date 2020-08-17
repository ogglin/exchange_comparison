from rest_framework import routers, serializers, viewsets
from .serializers import *


# ViewSets define the view behavior.
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class IdexViewSet(viewsets.ModelViewSet):
    queryset = Idex.objects.all()
    serializer_class = IdexSerializer


class BancorViewSet(viewsets.ModelViewSet):
    queryset = Bancor.objects.all()
    serializer_class = BancorSerializer


class KyberViewSet(viewsets.ModelViewSet):
    queryset = Kyber.objects.all()
    serializer_class = KyberSerializer


class UniswapViewSet(viewsets.ModelViewSet):
    queryset = Uniswap.objects.all()
    serializer_class = UniswapSerializer

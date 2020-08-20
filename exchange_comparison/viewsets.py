from rest_framework import viewsets
from rest_framework_api_key.permissions import HasAPIKey

from .serializers import *


# ViewSets define the view behavior.
class UserViewSet(viewsets.ModelViewSet):
    permission_classes = [HasAPIKey]
    queryset = User.objects.all()
    serializer_class = UserSerializer


class IdexViewSet(viewsets.ModelViewSet):
    permission_classes = [HasAPIKey]
    queryset = Idex.objects.all()
    serializer_class = IdexSerializer


class BancorViewSet(viewsets.ModelViewSet):
    permission_classes = [HasAPIKey]
    queryset = Bancor.objects.all()
    serializer_class = BancorSerializer


class KyberViewSet(viewsets.ModelViewSet):
    permission_classes = [HasAPIKey]
    queryset = Kyber.objects.all()
    serializer_class = KyberSerializer


class UniswapViewSet(viewsets.ModelViewSet):
    permission_classes = [HasAPIKey]
    queryset = Uniswap.objects.all()
    serializer_class = UniswapSerializer


class ExchangePairSet(viewsets.ModelViewSet):
    permission_classes = [HasAPIKey]
    queryset = CustomSql.objects.raw('''
        SELECT ep.id, ep.exch_direction, mi.highest_bid idexbid, mi.lowest_ask idexask, 
        mb.highest_bid bancorbid, mb.lowest_ask bancorask, mb.link_id bancorid, 
        mk.highest_bid kyberbid, mk.lowest_ask kyberask FROM exchange_pairs ep 
        LEFT JOIN module_idex mi ON ep.idex_direction_id = mi.id 
        LEFT JOIN module_bancor mb ON ep.bancor_direction_id = mb.id 
        LEFT JOIN module_kyber mk ON ep.kyber_direction_id = mk.id 
        WHERE idex_direction_id is not null and (bancor_direction_id is not null or kyber_direction_id is not null) 
        ORDER BY ep.id''')
    serializer_class = ExchangePairSerializer

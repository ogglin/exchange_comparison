import psycopg2
from django.db import connection
from rest_framework import viewsets
from rest_framework_api_key.permissions import HasAPIKey

from .serializers import *


def ec_custom_sql():
    with connection.cursor() as cur:
        q = '''
        SELECT ep.id, ep.exch_direction, mi.highest_bid idexbid, mi.lowest_ask idexask, 
        mb.highest_bid bancorbid, mb.lowest_ask bancorask, mb.link_id bancorid, 
        mk.highest_bid kyberbid, mk.lowest_ask kyberask FROM exchange_pairs ep 
        LEFT JOIN module_idex mi ON ep.idex_direction_id = mi.id 
        LEFT JOIN module_bancor mb ON ep.bancor_direction_id = mb.id 
        LEFT JOIN module_kyber mk ON ep.kyber_direction_id = mk.id 
        WHERE idex_direction_id is not null and (bancor_direction_id is not null or kyber_direction_id is not null) 
        ORDER BY ep.exch_direction'''
        try:
            cur.execute(q)
            data = cur.fetchall()
        except psycopg2.DatabaseError as err:
            print("Error: ", err)
        else:
            columns = [col[0] for col in cur.description]
            return [
                dict(zip(columns, row))
                for row in cur.fetchall()
            ]
        finally:
            connection.commit()


# ViewSets define the view behavior.
class UserViewSet(viewsets.ModelViewSet):
    permission_classes = [HasAPIKey]
    queryset = User.objects.all()
    serializer_class = UserSerializer


class IdexViewSet(viewsets.ModelViewSet):
    permission_classes = [HasAPIKey]
    queryset = Idex.objects.all()
    serializer_class = IdexSerializer


class HotbitViewSet(viewsets.ModelViewSet):
    permission_classes = [HasAPIKey]
    queryset = Hotbit.objects.all()
    serializer_class = HotbitSerializer


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


class UniswapOneViewSet(viewsets.ModelViewSet):
    permission_classes = [HasAPIKey]
    queryset = UniswapOne.objects.all()
    serializer_class = UniswapOneSerializer


class SettingsViewSet(viewsets.ModelViewSet):
    permission_classes = [HasAPIKey]
    queryset = Settings.objects.all()
    serializer_class = SettingsSerializer


class TrustedPairsSet(viewsets.ModelViewSet):
    permission_classes = [HasAPIKey]
    queryset = TrustedPairs.objects.filter(is_active=True)
    serializer_class = TrustedPairsSerializer


class WebsocketLogSet(viewsets.ModelViewSet):
    permission_classes = [HasAPIKey]
    queryset = WebsocketLog.objects.order_by('-id')[:40]
    serializer_class = WebsocketLogSerializer


class ExchangePairViewSet(viewsets.ModelViewSet):
    permission_classes = [HasAPIKey]
    queryset = ExchangePairs.objects.all()
    serializer_class = ExchangePairViewSerializer


class ExchangePairSet(viewsets.ModelViewSet):
    permission_classes = [HasAPIKey]
    queryset = CustomSql.objects.raw('''
        SELECT tp.id, tp.token exch_direction, 
            mi.highest_bid idexbid, mi.lowest_ask idexask, 
            mb.highest_bid bancorbid, mb.lowest_ask bancorask, mb.link_id bancorid,
            mk.highest_bid kyberbid, mk.lowest_ask kyberask,
            mu.highest_bid uniswapbid, mu.lowest_ask uniswapask, mu.tokenid uniswapid,
            muo.highest_bid uniswaponebid, muo.lowest_ask uniswaponeask, muo.tokenid uniswaponeid
            FROM trusted_pairs tp
            LEFT JOIN module_idex mi ON lower(tp.token) = lower(mi.exch_direction) AND mi.is_active
            LEFT JOIN module_bancor mb ON lower(tp.token) = lower(mb.exch_direction) AND mb.is_active
            LEFT JOIN module_kyber mk ON lower(tp.token) = lower(mk.exch_direction) AND mk.is_active
            LEFT JOIN module_uniswap mu ON lower(tp.token) = lower(mu.exch_direction) AND mu.is_active 
            AND lower(tp.contract) = lower(mu.tokenid)
            LEFT JOIN module_uniswap_one muo ON lower(tp.token) = lower(muo.exch_direction) AND muo.is_active 
            AND lower(tp.contract) = lower(muo.tokenid)
            WHERE tp.is_active = TRUE and (
            mi.highest_bid is not null or mi.lowest_ask is not null or 
            mb.lowest_ask is not null or mb.lowest_ask is not null or 
            mk.lowest_ask is not null or mk.lowest_ask is not null or 
            mu.lowest_ask is not null or mu.lowest_ask is not null or 
            muo.lowest_ask is not null or	muo.lowest_ask is not null 
            ) ORDER BY tp.token
        ''')
    serializer_class = ExchangePairSerializer

    def get_queryset(self):
        assert self.queryset is not None, (
                "'%s' should either include a `queryset` attribute, "
                "or override the `get_queryset()` method."
                % self.__class__.__name__
        )
        queryset = CustomSql.objects.raw('''
        SELECT tp.id, tp.token exch_direction, 
            mi.highest_bid idexbid, mi.lowest_ask idexask, 
            mb.highest_bid bancorbid, mb.lowest_ask bancorask, mb.link_id bancorid,
            mk.highest_bid kyberbid, mk.lowest_ask kyberask,
            mu.highest_bid uniswapbid, mu.lowest_ask uniswapask, mu.tokenid uniswapid,
            muo.highest_bid uniswaponebid, muo.lowest_ask uniswaponeask, muo.tokenid uniswaponeid
            FROM trusted_pairs tp
            LEFT JOIN module_idex mi ON lower(tp.token) = lower(mi.exch_direction) AND mi.is_active
            LEFT JOIN module_bancor mb ON lower(tp.token) = lower(mb.exch_direction) AND mb.is_active
            LEFT JOIN module_kyber mk ON lower(tp.token) = lower(mk.exch_direction) AND mk.is_active
            LEFT JOIN module_uniswap mu ON lower(tp.token) = lower(mu.exch_direction) AND mu.is_active 
            AND lower(tp.contract) = lower(mu.tokenid)
            LEFT JOIN module_uniswap_one muo ON lower(tp.token) = lower(muo.exch_direction) AND muo.is_active 
            AND lower(tp.contract) = lower(muo.tokenid)
            WHERE tp.is_active = TRUE and (
            mi.highest_bid is not null or mi.lowest_ask is not null or 
            mb.lowest_ask is not null or mb.lowest_ask is not null or 
            mk.lowest_ask is not null or mk.lowest_ask is not null or 
            mu.lowest_ask is not null or mu.lowest_ask is not null or 
            muo.lowest_ask is not null or	muo.lowest_ask is not null 
            ) ORDER BY tp.token
        ''')
        return queryset


class SettingsModulesViewSet(viewsets.ModelViewSet):
    permission_classes = [HasAPIKey]
    queryset = SettingsModules.objects.all()
    serializer_class = SettingsModulesSerializer


class ProfitExchangesViewSet(viewsets.ModelViewSet):
    permission_classes = [HasAPIKey]
    queryset = ProfitExchanges.objects.all()
    serializer_class = ProfitExchangesSerializer

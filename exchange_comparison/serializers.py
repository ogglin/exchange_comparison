from rest_framework import serializers
from django.contrib.auth.models import User
from idex_module.models import Idex
from bancor_module.models import Bancor
from kyber_module.models import Kyber
from uniswap_module.models import Uniswap, UniswapOne
from exchange_pairs.models import CustomSql, Settings


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'is_staff']


class IdexSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Idex
        fields = ['exch_direction', 'lowest_ask', 'highest_bid']


class BancorSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Bancor
        fields = ['exch_direction', 'lowest_ask', 'highest_bid', 'link_id']


class KyberSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Kyber
        fields = ['exch_direction', 'lowest_ask', 'highest_bid']


class UniswapSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Uniswap
        fields = ['exch_direction', 'lowest_ask', 'highest_bid']


class UniswapOneSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = UniswapOne
        fields = ['exch_direction', 'lowest_ask', 'highest_bid']


class ExchangePairSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = CustomSql
        fields = ['id', 'exch_direction', 'idexbid', 'idexask', 'bancorbid', 'bancorask', 'bancorid', 'kyberbid',
                  'kyberask', 'uniswapbid', 'uniswapask', 'uniswaponebid', 'uniswaponeask']


class SettingsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Settings
        fields = ['timeout_refresh_data', 'timeout_notice', 'koef_top', 'koef_low', 'koef_push']

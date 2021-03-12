from rest_framework import serializers
from django.contrib.auth.models import User
from idex_module.models import Idex
from hotbit_module.models import Hotbit
from bancor_module.models import Bancor
from kyber_module.models import Kyber
from uniswap_module.models import Uniswap, UniswapOne
from exchange_pairs.models import CustomSql, Settings, SettingsModules, TrustedPairs, WebsocketLog, ExchangePairs, \
    ProfitExchanges


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'is_staff']


class HotbitSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Hotbit
        fields = ['exch_direction', 'buy', 'sell', 'symbol', 'is_active', 'volume']


class IdexSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Idex
        fields = ['exch_direction', 'lowest_ask', 'highest_bid', 'volume']


class BancorSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Bancor
        fields = ['exch_direction', 'lowest_ask', 'highest_bid', 'link_id', 'volume']


class KyberSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Kyber
        fields = ['exch_direction', 'lowest_ask', 'highest_bid', 'volume']


class UniswapSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Uniswap
        fields = ['exch_direction', 'lowest_ask', 'highest_bid', 'volume']


class UniswapOneSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = UniswapOne
        fields = ['exch_direction', 'lowest_ask', 'highest_bid', 'volume']


class ExchangePairViewSerializer(serializers.ModelSerializer):
    class Meta:
        model = ExchangePairs
        fields = ['exch_direction', 'idex_direction', 'uniswap_direction', 'uniswap_one_direction', 'bancor_direction',
                  'kyber_direction', 'hotbit']


class ExchangePairSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = CustomSql
        fields = ['tsymbol', 'contract', 'exch_direction', 'sell', 'buy', 'site']


class SettingsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Settings
        fields = ['timeout_refresh_data', 'timeout_notice', 'koef_top', 'koef_low', 'koef_push', 'freeze_percent',
                  'api_keys', 'currency', 'gas_normal', 'gas_fast']


class SettingsModulesSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = SettingsModules
        fields = ['module_name', 'is_active']


class ProfitExchangesSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = ProfitExchanges
        fields = ['pair', 'buy_name', 'buy', 'sell_name', 'sell', 'percent', 'tokenid', 'buyurl', 'sellurl', 'buy_ask',
                  'sell_bid', 'sell_symbol']


class TrustedPairsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = TrustedPairs
        fields = ['token', ]


class WebsocketLogSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = WebsocketLog
        fields = ['datetime', 'log']

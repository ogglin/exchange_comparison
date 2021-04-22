from django.db import models

from hotbit_module.models import Hotbit
from idex_module.models import Idex
from bancor_module.models import Bancor
from kyber_module.models import Kyber
from uniswap_module.models import Uniswap, UniswapOne


class TrustedPairs(models.Model):
    token = models.CharField(max_length=20, blank=False, null=False)
    tsymbol = models.CharField(max_length=100, blank=True, null=True)
    contract = models.CharField(max_length=100, blank=False, null=False)
    decimals = models.IntegerField(null=True)
    token_name = models.CharField(max_length=255, blank=True, null=True)
    is_active = models.BooleanField(verbose_name='Активный', blank=False, null=False)

    def __str__(self):
        return self.token

    class Meta:
        db_table = 'trusted_pairs'
        verbose_name = 'Trusted pair'
        verbose_name_plural = 'Trusted pairs'


class ComparePairs(models.Model):
    token = models.CharField(max_length=20, blank=False, null=False)
    tsymbol = models.CharField(max_length=100, blank=True, null=True)
    contract = models.CharField(max_length=100, blank=False, null=False)
    decimals = models.IntegerField(null=True)
    is_active = models.BooleanField(verbose_name='Активный', blank=False, null=False)

    def __str__(self):
        return self.token

    class Meta:
        db_table = 'compare_pairs'
        verbose_name = 'Compare pair'
        verbose_name_plural = 'Compare pairs'


class ExchangePairs(models.Model):
    exch_direction = models.CharField(max_length=20, blank=False, null=False)
    idex_direction = models.ForeignKey(Idex, on_delete=models.DO_NOTHING, related_name='+', null=True, blank=True)
    uniswap_direction = models.ForeignKey(Uniswap, on_delete=models.DO_NOTHING, related_name='+', null=True, blank=True)
    uniswap_one_direction = models.ForeignKey(UniswapOne, on_delete=models.DO_NOTHING, related_name='+', null=True,
                                              blank=True)
    bancor_direction = models.ForeignKey(Bancor, on_delete=models.DO_NOTHING, related_name='+', null=True, blank=True)
    kyber_direction = models.ForeignKey(Kyber, on_delete=models.DO_NOTHING, related_name='+', null=True, blank=True)
    hotbit = models.ForeignKey(Hotbit, on_delete=models.DO_NOTHING, related_name='+', null=True, blank=True)

    def __str__(self):
        return self.exch_direction

    class Meta:
        db_table = 'exchange_pairs'
        verbose_name = 'Exchange pair'
        verbose_name_plural = 'Exchange pairs'


class Settings(models.Model):
    timeout_refresh_data = models.IntegerField(verbose_name='Интервал обновления данных')
    timeout_notice = models.IntegerField(verbose_name='Интервал показа нотификаций')
    koef_top = models.FloatField(verbose_name='Коэффициет топ %', help_text='красная строка')
    koef_low = models.FloatField(verbose_name='Коэффициет минимума %', help_text='зеленая строка')
    koef_push = models.FloatField(verbose_name='Коэффициет в % ', help_text='для пуш уведомлений')
    freeze_percent = models.FloatField(verbose_name='Процент заморозки ', help_text='в %', default=1)
    api_keys = models.JSONField(verbose_name='API keys', null=True, blank=True)
    market_percent = models.FloatField(verbose_name='Процент бирж', help_text='для сравнения бирж в %', null=True,
                                       blank=True)
    market_koef = models.FloatField(verbose_name='Коэффициет бирж', help_text='учет отклонения для сравнения бирж в %',
                                    null=True, blank=True)
    currency = models.FloatField(verbose_name='ETH/BTC', help_text='Курс ETH к BTC', null=True, blank=True)
    currency_usd = models.FloatField(verbose_name='ETH/USD', help_text='Курс ETH к USD', null=True, blank=True)
    gas_normal = models.IntegerField()
    gas_fast = models.IntegerField()

    def __str__(self):
        return 'Кастройки коэффициентов'

    class Meta:
        db_table = 'settings'
        verbose_name = 'Настройка'
        verbose_name_plural = 'Настройки'


class SettingsModules(models.Model):
    module_name = models.CharField(verbose_name='Модуль', max_length=200, blank=False, null=False)
    is_active = models.BooleanField(verbose_name='Включен', blank=False, null=False)

    def __str__(self):
        return self.module_name

    class Meta:
        db_table = 'settings_modules'
        verbose_name = 'Настройка модуля'
        verbose_name_plural = 'Настройки модулей'


class WebsocketLog(models.Model):
    datetime = models.DateTimeField(verbose_name='Дата', auto_now_add=True, editable=False)
    log = models.TextField(verbose_name='Лог')
    buy_url = models.CharField(null=True, blank=True, max_length=255)
    sell_url = models.CharField(null=True, blank=True, max_length=255)
    type = models.CharField(null=True, blank=True, max_length=255)
    site = models.CharField(null=True, blank=True, max_length=255)
    percent = models.FloatField(default=0, blank=True, null=True)
    token = models.CharField(null=True, blank=True, max_length=255)
    price = models.FloatField(default=0, blank=True, null=True)
    sprice = models.FloatField(default=0, blank=True, null=True)

    def __str__(self):
        return self.log

    class Meta:
        db_table = 'websocket_log'
        verbose_name = 'Логи вебсокета'
        verbose_name_plural = 'Лог вебсокета'


class CustomSql(models.Model):
    tsymbol = models.CharField(max_length=100)
    contract = models.CharField(max_length=100)
    exch_direction = models.CharField(max_length=100)
    sell = models.FloatField()
    buy = models.FloatField()
    site = models.CharField(max_length=100)

    class Meta:
        managed = False


class ProfitExchanges(models.Model):
    pair = models.CharField(max_length=100)
    buy_name = models.CharField(max_length=100)
    buy = models.FloatField(max_length=100)
    sell_name = models.CharField(max_length=100)
    sell = models.FloatField(max_length=100)
    percent = models.FloatField(max_length=100)
    tokenid = models.CharField(max_length=100)
    buyurl = models.CharField(max_length=200)
    sellurl = models.CharField(max_length=200)
    buy_ask = models.FloatField(max_length=100)
    sell_bid = models.FloatField(max_length=100)
    sell_symbol = models.CharField(max_length=100, null=True, blank=True)
    contract = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return self.pair

    class Meta:
        db_table = 'profit_exchanges'
        verbose_name = 'Выгодные обмены'
        verbose_name_plural = 'Выгодный обмен'

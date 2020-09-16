from django.db import models
from idex_module.models import Idex
from bancor_module.models import Bancor
from kyber_module.models import Kyber
from uniswap_module.models import Uniswap, UniswapOne


class TrustedPairs(models.Model):
    token = models.CharField(max_length=20, blank=False, null=False)
    contract = models.CharField(max_length=100, blank=False, null=False)
    decimals = models.IntegerField(null=True)
    is_active = models.BooleanField(verbose_name='Активный', blank=False, null=False)

    def __str__(self):
        return self.token

    class Meta:
        db_table = 'trusted_pairs'
        verbose_name = 'Trusted pair'
        verbose_name_plural = 'Trusted pairs'


class ComparePairs(models.Model):
    token = models.CharField(max_length=20, blank=False, null=False)
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


class CustomSql(models.Model):
    exch_direction = models.CharField(max_length=100)
    idexbid = models.FloatField()
    idexask = models.FloatField()
    bancorbid = models.FloatField()
    bancorask = models.FloatField()
    bancorid = models.CharField(max_length=255)
    kyberbid = models.FloatField()
    kyberask = models.FloatField()
    uniswaponebid = models.FloatField()
    uniswaponeask = models.FloatField()
    uniswaponeid = models.CharField(max_length=500)
    uniswapbid = models.FloatField()
    uniswapask = models.FloatField()
    uniswapid = models.CharField(max_length=500)

    class Meta:
        managed = False

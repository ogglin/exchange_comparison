from django.db import models
from idex_module.models import Idex
from bancor_module.models import Bancor
from kyber_module.models import Kyber
from uniswap_module.models import Uniswap, UniswapOne


# Create your models here.

class ExchangePairs(models.Model):
    exch_direction = models.CharField(max_length=20, blank=False, null=False)
    idex_direction = models.ForeignKey(Idex, on_delete=models.DO_NOTHING, related_name='+', null=True, blank=True)
    uniswap_direction = models.ForeignKey(Uniswap, on_delete=models.DO_NOTHING, related_name='+', null=True, blank=True)
    uniswap_one_direction = models.ForeignKey(UniswapOne, on_delete=models.DO_NOTHING, related_name='+', null=True, blank=True)
    bancor_direction = models.ForeignKey(Bancor, on_delete=models.DO_NOTHING, related_name='+', null=True, blank=True)
    kyber_direction = models.ForeignKey(Kyber, on_delete=models.DO_NOTHING, related_name='+', null=True, blank=True)

    def __str__(self):
        return self.exch_direction

    class Meta:
        db_table = 'exchange_pairs'
        verbose_name = 'ExchangePair'
        verbose_name_plural = 'ExchangePairs'


class Settings(models.Model):
    timeout_refresh_data = models.IntegerField(verbose_name='Интервал обновления данных')
    timeout_notice = models.IntegerField(verbose_name='Интервал показа нотификаций')
    koef_top = models.FloatField(verbose_name='Коэффициет топ %', help_text='красная строка')
    koef_low = models.FloatField(verbose_name='Коэффициет минимума %', help_text='зеленая строка')
    koef_push = models.FloatField(verbose_name='Коэффициет в % ', help_text='для пуш уведомлений')

    class Meta:
        db_table = 'settings'
        verbose_name = 'Настройка'
        verbose_name_plural = 'Настройки'


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

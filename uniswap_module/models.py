from django.db import models


# Create your models here.

class Uniswap(models.Model):
    exch_direction = models.CharField(max_length=256, blank=False, null=False)
    tsymbol = models.CharField(max_length=100, blank=True, null=True)
    highest_bid = models.FloatField(blank=True, null=True)
    lowest_ask = models.FloatField(blank=True, null=True)
    tokenid = models.CharField(max_length=500, default='')
    volume = models.FloatField(blank=True, null=True)
    is_active = models.BooleanField(verbose_name='Активный', blank=False, null=False)

    def __str__(self):
        return self.exch_direction

    class Meta:
        db_table = 'module_uniswap'


class UniswapOne(models.Model):
    exch_direction = models.CharField(max_length=256, blank=False, null=False)
    tsymbol = models.CharField(max_length=100, blank=True, null=True)
    highest_bid = models.FloatField()
    lowest_ask = models.FloatField()
    tokenid = models.CharField(max_length=500, default='')
    volume = models.FloatField()
    is_active = models.BooleanField(verbose_name='Активный', blank=False, null=False)

    def __str__(self):
        return self.exch_direction

    class Meta:
        db_table = 'module_uniswap_one'


class UniswapMarkets(models.Model):
    market = models.CharField(max_length=100, blank=False, null=False, unique=True)
    token = models.CharField(max_length=256, blank=True, null=True)
    tokenid = models.CharField(max_length=256, blank=True, null=True)
    tsymbol = models.CharField(max_length=100, blank=True, null=True)
    is_active = models.BooleanField(verbose_name='Активный', blank=False, null=False)

    def __str__(self):
        return self.token

    class Meta:
        db_table = 'uniswap_markets'

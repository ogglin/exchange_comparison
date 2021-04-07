from django.db import models


# Create your models here.


class Idex(models.Model):
    exch_direction = models.CharField(max_length=20, blank=False, null=False)
    tsymbol = models.CharField(max_length=100, blank=True, null=True)
    lowest_ask = models.FloatField()
    highest_bid = models.FloatField()
    token_id = models.CharField(max_length=50, blank=True, null=True)
    volume = models.FloatField()
    is_active = models.BooleanField(verbose_name='Активный', blank=False, null=False)

    def __str__(self):
        return self.exch_direction

    class Meta:
        db_table = 'module_idex'


class IdexSocketLog(models.Model):
    log = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.log

    class Meta:
        db_table = 'idex_socket_log'


class IdexMarkets(models.Model):
    market = models.CharField(max_length=30, blank=False, null=False, unique=True)
    token = models.CharField(max_length=30, blank=True, null=True)
    tsymbol = models.CharField(max_length=100, blank=True, null=True)
    is_active = models.BooleanField(verbose_name='Активный', blank=False, null=False)

    def __str__(self):
        return self.token

    class Meta:
        db_table = 'idex_markets'
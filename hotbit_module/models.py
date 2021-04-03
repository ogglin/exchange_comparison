from django.db import models


# Create your models here.

class Hotbit(models.Model):
    exch_direction = models.CharField(max_length=30, blank=False, null=False)
    buy = models.FloatField(null=True)
    sell = models.FloatField(null=True)
    symbol = models.CharField(max_length=30, blank=False, null=False)
    tsymbol = models.CharField(max_length=100, blank=True, null=True)
    volume = models.FloatField(max_length=30, blank=True, null=True)
    contract = models.CharField(max_length=100, blank=True, null=True)
    decimals = models.IntegerField(blank=True, null=True)
    is_active = models.BooleanField(verbose_name='Активный', blank=False, null=False)

    def __str__(self):
        return self.symbol

    class Meta:
        db_table = 'module_hotbit'


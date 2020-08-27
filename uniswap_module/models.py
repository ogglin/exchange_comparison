from django.db import models


# Create your models here.

class Uniswap(models.Model):
    exch_direction = models.CharField(max_length=256, blank=False, null=False)
    highest_bid = models.FloatField()
    lowest_ask = models.FloatField()
    is_active = models.BooleanField(default=True, verbose_name='Активный')

    def __str__(self):
        return self.exch_direction

    class Meta:
        db_table = 'module_uniswap'


class UniswapOne(models.Model):
    exch_direction = models.CharField(max_length=256, blank=False, null=False)
    highest_bid = models.FloatField()
    lowest_ask = models.FloatField()
    is_active = models.BooleanField(default=True, verbose_name='Активный')

    def __str__(self):
        return self.exch_direction

    class Meta:
        db_table = 'module_uniswap_one'

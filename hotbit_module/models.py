from django.db import models


# Create your models here.

class Hotbit(models.Model):
    exch_direction = models.CharField(max_length=30, blank=False, null=False)
    buy = models.FloatField()
    sell = models.FloatField()
    symbol = models.CharField(max_length=30, blank=False, null=False)
    volume = models.FloatField(max_length=30, blank=False, null=False)
    contract = models.CharField(max_length=100, blank=True, null=True)
    decimals = models.IntegerField(blank=True, null=True)
    is_active = models.BooleanField(verbose_name='Активный', blank=False, null=False)

    def __str__(self):
        return self.exch_direction

    class Meta:
        db_table = 'module_hotbit'


from django.db import models


# Create your models here.

class Uniswap(models.Model):
    exch_direction = models.CharField(max_length=20, blank=False, null=False)
    highest_bid = models.FloatField()
    lowest_ask = models.FloatField()

    def __str__(self):
        return self.exch_direction

    class Meta:
        db_table = 'module_uniswap'

from django.db import models
from idex_module.models import Idex
from bancor_module.models import Bancor
from kyber_module.models import Kyber
from uniswap_module.models import Uniswap


# Create your models here.

class ExchangePairs(models.Model):
    exch_direction = models.CharField(max_length=20, blank=False, null=False)
    idex_direction = models.ForeignKey(Idex, on_delete=models.DO_NOTHING, related_name='+')
    uniswap_direction = models.ForeignKey(Uniswap, on_delete=models.DO_NOTHING, related_name='+')
    bancor_direction = models.ForeignKey(Bancor, on_delete=models.DO_NOTHING, related_name='+')
    kyber_direction = models.ForeignKey(Kyber, on_delete=models.DO_NOTHING, related_name='+')

    def __str__(self):
        return self.exch_direction

    class Meta:
        db_table = 'exchange_pairs'

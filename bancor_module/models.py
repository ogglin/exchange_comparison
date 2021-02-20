from django.db import models


# Create your models here.

class Bancor(models.Model):
    exch_direction = models.CharField(max_length=20, blank=False, null=False)
    highest_bid = models.FloatField()
    lowest_ask = models.FloatField()
    name = models.CharField(max_length=100, blank=False, null=False)
    tsymbol = models.CharField(max_length=100, blank=True, null=True)
    link_id = models.CharField(max_length=100, blank=False, null=False)
    volume = models.FloatField(default=0)
    is_active = models.BooleanField(verbose_name='Активный', blank=False, null=False)

    def __str__(self):
        return self.exch_direction

    class Meta:
        db_table = 'module_bancor'

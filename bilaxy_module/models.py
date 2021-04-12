from django.db import models


# Create your models here.
class BilaxyMarkets(models.Model):
    market = models.CharField(max_length=30, blank=False, null=False, unique=True)
    token = models.CharField(max_length=30, blank=True, null=True)
    tsymbol = models.CharField(max_length=100, blank=True, null=True)
    is_active = models.BooleanField(verbose_name='Активный', blank=False, null=False)

    def __str__(self):
        return self.token

    class Meta:
        db_table = 'bilaxy_markets'

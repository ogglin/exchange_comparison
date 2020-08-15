from django.db import models


# Create your models here.

class Bancor(models.Model):
    exch_direction = models.CharField(max_length=20, blank=False, null=False)
    highest_bid = models.FloatField()
    lowest_ask = models.FloatField()
    name = models.CharField(max_length=100, blank=False, null=False)
    link_id = models.CharField(max_length=100, blank=False, null=False)

    def __str__(self):
        return self.exch_direction

from django.contrib import admin
from .models import *

# Register your models here.
@admin.register(ExchangePairs)
class ExchangePairAdmin(admin.ModelAdmin):
    list_display = ('exch_direction', 'idex_direction', 'uniswap_direction', 'bancor_direction', 'kyber_direction')

# admin.site.register(ExchangePairs)

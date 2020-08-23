from django.contrib import admin
from .models import *


# Register your models here.
@admin.register(ExchangePairs)
class ExchangePairAdmin(admin.ModelAdmin):
    list_display = ('exch_direction', 'idex_direction', 'uniswap_direction', 'bancor_direction', 'kyber_direction')


@admin.register(Settings)
class SettingsAdmin(admin.ModelAdmin):
    list_display = ('timeout_refresh_data', 'timeout_notice', 'koef_top', 'koef_low')

# admin.site.register(ExchangePairs)

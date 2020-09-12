from django.contrib import admin
from .models import *


# Register your models here.
@admin.register(ExchangePairs)
class ExchangePairAdmin(admin.ModelAdmin):
    list_display = ('exch_direction', 'idex_direction', 'uniswap_direction', 'bancor_direction', 'kyber_direction')
    search_fields = ('exch_direction',)


@admin.register(Settings)
class SettingsAdmin(admin.ModelAdmin):
    list_display = ('timeout_refresh_data', 'timeout_notice', 'koef_top', 'koef_low', 'koef_push')


@admin.register(SettingsModules)
class SettingsModulesAdmin(admin.ModelAdmin):
    list_display = ('module_name', 'is_active')


@admin.register(TrustedPairs)
class TrustedPairsAdmin(admin.ModelAdmin):
    list_display = ('token', 'contract', 'decimals', 'is_active')
    list_filter = ('is_active',)
    search_fields = ('token', )
# admin.site.register(ExchangePairs)

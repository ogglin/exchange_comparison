from django.contrib import admin
from .models import *


# Register your models here.
# @admin.register(Hotbit)
# class HotbitAdmin(admin.ModelAdmin):
#     list_display = ('exch_direction', 'symbol', 'tsymbol', 'contract', 'decimals', 'is_active')
#     search_fields = ('exch_direction', 'symbol', 'tsymbol',)


@admin.register(HotbitMarkets)
class HotbitMarketsAdmin(admin.ModelAdmin):
    list_display = ('market', 'token', 'tsymbol', 'is_active')
    search_fields = ('market', 'tsymbol',)
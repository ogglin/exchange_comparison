from django.contrib import admin
from .models import *


# Register your models here.
@admin.register(Hitbtc)
class HitbtcAdmin(admin.ModelAdmin):
    list_display = ('exch_direction', 'symbol', 'tsymbol', 'contract', 'decimals', 'is_active')
    search_fields = ('exch_direction', 'symbol', 'tsymbol',)

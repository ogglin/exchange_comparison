from django.contrib import admin
from .models import *

from utils.admin_utils import activate, deactivate


# Register your models here.
# @admin.register(Idex)
# class IdexAdmin(admin.ModelAdmin):
#     list_display = ('exch_direction', 'tsymbol', 'is_active')
#     search_fields = ('exch_direction', 'tsymbol',)


@admin.register(IdexMarkets)
class IdexMarketsAdmin(admin.ModelAdmin):
    list_display = ('market', 'token', 'tsymbol', 'is_active')
    search_fields = ('market', 'tsymbol',)
    actions = [activate, deactivate]

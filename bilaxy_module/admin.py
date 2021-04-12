from django.contrib import admin
from bilaxy_module.models import BilaxyMarkets


# Register your models here.
@admin.register(BilaxyMarkets)
class BilaxyMarketsAdmin(admin.ModelAdmin):
    list_display = ('market', 'token', 'tsymbol', 'is_active')
    search_fields = ('market', 'tsymbol',)

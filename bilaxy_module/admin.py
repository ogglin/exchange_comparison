from django.contrib import admin
from bilaxy_module.models import BilaxyMarkets


def activate(modeladmin, request, queryset):
    queryset.update(is_active=True)


activate.short_description = "Активировать"


def deactivate(modeladmin, request, queryset):
    queryset.update(is_active=False)


deactivate.short_description = "Деактивировать"


# Register your models here.
@admin.register(BilaxyMarkets)
class BilaxyMarketsAdmin(admin.ModelAdmin):
    list_display = ('market', 'token', 'tsymbol', 'is_active')
    search_fields = ('market', 'tsymbol',)
    actions = [activate, deactivate]

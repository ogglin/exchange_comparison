from django.contrib import admin

from .models import *


# Register your models here.
@admin.register(Bancor)
class BancorAdmin(admin.ModelAdmin):
    list_display = ('exch_direction', 'is_active')
    search_fields = ('exch_direction',)

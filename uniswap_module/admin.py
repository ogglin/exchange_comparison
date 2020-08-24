from django.contrib import admin
from .models import *


# Register your models here.
@admin.register(Uniswap)
class BancorAdmin(admin.ModelAdmin):
    list_display = ('exch_direction', 'is_active')

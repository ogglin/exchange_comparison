from django.contrib import admin
from .models import *


# Register your models here.
@admin.register(Uniswap)
class UniswapAdmin(admin.ModelAdmin):
    list_display = ('exch_direction', 'is_active')


@admin.register(UniswapOne)
class UniswapOneAdmin(admin.ModelAdmin):
    list_display = ('exch_direction', 'is_active')
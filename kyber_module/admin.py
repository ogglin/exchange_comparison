from django.contrib import admin
from .models import *


# Register your models here.
@admin.register(Kyber)
class KyberAdmin(admin.ModelAdmin):
    list_display = ('exch_direction', 'is_active')
    search_fields = ('exch_direction',)

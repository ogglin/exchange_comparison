from django.contrib import admin
from .models import *


# Register your models here.
@admin.register(Idex)
class IdexAdmin(admin.ModelAdmin):
    list_display = ('exch_direction', 'tsymbol', 'is_active')
    search_fields = ('exch_direction', 'tsymbol',)

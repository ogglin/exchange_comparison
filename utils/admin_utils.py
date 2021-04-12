def activate(modeladmin, request, queryset):
    queryset.update(is_active=True)


activate.short_description = "Активировать"


def deactivate(modeladmin, request, queryset):
    queryset.update(is_active=False)


deactivate.short_description = "Деактивировать"

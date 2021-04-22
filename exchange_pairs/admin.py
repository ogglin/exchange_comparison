from django.conf.urls import url
from django.contrib import admin
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.utils.html import format_html

from .models import *


# Register your models here.
@admin.register(ExchangePairs)
class ExchangePairAdmin(admin.ModelAdmin):
    list_display = ('exch_direction', 'idex_direction', 'uniswap_direction', 'bancor_direction', 'kyber_direction', 'hotbit')
    search_fields = ('exch_direction',)


@admin.register(Settings)
class SettingsAdmin(admin.ModelAdmin):
    list_display = ('timeout_refresh_data', 'timeout_notice', 'koef_top', 'koef_low', 'koef_push')


@admin.register(SettingsModules)
class SettingsModulesAdmin(admin.ModelAdmin):
    list_display = ('module_name', 'is_active')


@admin.register(TrustedPairs)
class TrustedPairsAdmin(admin.ModelAdmin):
    list_display = ('token', 'contract', 'tsymbol', 'decimals', 'is_active', 'token_actions',)
    list_filter = ('is_active',)
    search_fields = ('token', 'tsymbol', 'contract',)

    def get_urls(self):
        urls = super().get_urls()
        custom_urls = [
            url(r'^(?P<token_id>.+)/uniswap/$', self.process_uniswap, kwargs=[], name='token-uniswap'),
            # url(
            #     r'^(?P<token_id>.+)/withdraw/$',
            #     self.admin_site.admin_view(self.process_withdraw),
            #     name='account-withdraw',
            # ),
        ]
        return custom_urls + urls

    def token_actions(self, obj):
        # TODO: Render action buttons
        return format_html(
            '<a class="button" href="{}">Uniswap</a> ',
            # '<a class="button" href="{}">Withdraw</a>',
            # reverse('admin:account-deposit', args=[obj.pk]),
            reverse('admin:token-uniswap', args=[obj.pk]),
        )
    token_actions.short_description = 'Token Actions'
    token_actions.allow_tags = True

    def process_uniswap(self, request, token_id, *args, **kwargs):
        obj = TrustedPairs.objects.get(id=token_id)
        try:
            uniObj = Uniswap.objects.get(tokenid__icontains=obj.contract)
            uniObj.tsymbol = obj.tsymbol
            uniObj.is_active = True
            uniObj.save()
        except:
            obj = Uniswap(tokenid=obj.contract, highest_bid=0, lowest_ask=0, volume=0, tsymbol=obj.tsymbol, exch_direction=obj.token, is_active=True)
            obj.save()
        return HttpResponseRedirect("/admin/exchange_pairs/trustedpairs/")
        # TODO
    def process_withdraw(self):
        pass
        # TODO


@admin.register(WebsocketLog)
class WebsocketLogAdmin(admin.ModelAdmin):
    list_display = ('datetime', 'log')
    list_filter = ('datetime',)
    search_fields = ('datetime',)

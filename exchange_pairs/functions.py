import datetime
import time

from asgiref.sync import sync_to_async
from django.db import transaction
from django.db.models import Q

from exchange_pairs.models import ProfitExchanges
from exchange_pairs.services import set_all_compared_tokens
from hitbtc_module.functions import hitbtc_profits
from hotbit_module.functions import hotbit_profits, set_currencies
from idex_module.functions import idex_profits


@sync_to_async
def idex_result():
    idex_result = idex_profits()
    ProfitExchanges.objects.filter(Q(buy_name__icontains='idex') | (
            Q(sell_name__icontains='idex') & ~Q(buy_name__icontains='hotbit') & ~Q(
        buy_name__icontains='hitbit'))).delete()
    with transaction.atomic():
        for result in idex_result:
            pair = ProfitExchanges(pair=result['pair'], buy_name=result['buy_name'], buy=result['buy'],
                                   buy_ask=result['buy_ask'], buyurl=result['buyurl'], sell_name=result['sell_name'],
                                   sell=result['sell'], sell_bid=result['sell_bid'], percent=result['percent'],
                                   tokenid=result['tokenid'], sellurl=result['sellurl'],
                                   sell_symbol=result['sell_symbol'])
            pair.save()


@sync_to_async
def hotbit_result():
    hotbit_result = hotbit_profits()
    ProfitExchanges.objects.filter(Q(buy_name__icontains='hotbit') | (
            Q(sell_name__icontains='hotbit') & ~Q(buy_name__icontains='idex') & ~Q(
        buy_name__icontains='hitbit'))).delete()
    with transaction.atomic():
        for result in hotbit_result:
            pair = ProfitExchanges(pair=result['pair'], buy_name=result['buy_name'], buy=result['buy'],
                                   buy_ask=result['buy_ask'], buyurl=result['buyurl'], sell_name=result['sell_name'],
                                   sell=result['sell'], sell_bid=result['sell_bid'], percent=result['percent'],
                                   tokenid=result['tokenid'], sellurl=result['sellurl'],
                                   sell_symbol=result['sell_symbol'])
            pair.save()


@sync_to_async
def hitbtc_result():
    hitbtc_result = hitbtc_profits()
    ProfitExchanges.objects.filter(Q(buy_name__icontains='hitbtc') | (
                Q(sell_name__icontains='hitbtc') & ~Q(buy_name__icontains='hotbit') & ~Q(
            buy_name__icontains='idex'))).delete()
    with transaction.atomic():
        for result in hitbtc_result:
            pair = ProfitExchanges(pair=result['pair'], buy_name=result['buy_name'], buy=result['buy'],
                                   buy_ask=result['buy_ask'], buyurl=result['buyurl'], sell_name=result['sell_name'],
                                   sell=result['sell'], sell_bid=result['sell_bid'], percent=result['percent'],
                                   tokenid=result['tokenid'], sellurl=result['sellurl'],
                                   sell_symbol=result['sell_symbol'])
            pair.save()


async def init_all_compared_tokens():
    print('start set compared_tokens: ' + str(datetime.datetime.now()))
    while True:
        await set_all_compared_tokens()


async def exchanges_idex():
    print('start idex exchanges: ' + str(datetime.datetime.now()))
    while True:
        await idex_result()
        # print('end idex exchanges: ' + str(datetime.datetime.now()))


async def tiker_hotbit():
    print('start hotbit tiker: ' + str(datetime.datetime.now()))
    while True:
        await set_currencies()


async def exchanges_hotbit():
    print('start hotbit exchanges: ' + str(datetime.datetime.now()))
    while True:
        await hotbit_result()
        # print('end exchanges: ' + str(datetime.datetime.now()))


async def exchanges_hitbtc():
    print('start hitbtc exchanges: ' + str(datetime.datetime.now()))
    while True:
        await hitbtc_result()

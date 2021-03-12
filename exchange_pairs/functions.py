import datetime
import time

from asgiref.sync import sync_to_async
from django.db import transaction
from django.db.models import Q

from exchange_pairs.models import ProfitExchanges
from exchange_pairs.services import set_all_compared_tokens
from hitbtc_module.functions import hitbtc_profits
from hotbit_module.functions import hotbit_profits
from idex_module.functions import idex_profits


@sync_to_async
def idex_result():
    idex_result = idex_profits()
    ProfitExchanges.objects.filter(Q(buy_name__icontains='idex') | Q(sell_name__icontains='idex')).delete()
    with transaction.atomic():
        for result in idex_result:
            pair = ProfitExchanges(pair=result['pair'], buy_name=result['buy_name'], buy=result['buy'], buy_ask=0,
                                   sell_bid=0,
                                   sell_name=result['sell_name'], sell=result['sell'], percent=result['percent'],
                                   tokenid=result['tokenid'], buyurl=result['buyurl'], sellurl=result['sellurl'])
            pair.save()


@sync_to_async
def hotbit_result():
    hotbit_result = hotbit_profits()
    ProfitExchanges.objects.filter(Q(buy_name__icontains='hotbit') | Q(sell_name__icontains='hotbit')).delete()
    with transaction.atomic():
        for result in hotbit_result:
            pair = ProfitExchanges(pair=result['pair'], buy_name=result['buy_name'], buy=result['buy'], buy_ask=0,
                                   sell_bid=0,
                                   sell_name=result['sell_name'], sell=result['sell'], percent=result['percent'],
                                   tokenid=result['tokenid'], buyurl=result['buyurl'], sellurl=result['sellurl'])
            pair.save()


@sync_to_async
def hitbtc_result():
    hitbtc_result = hitbtc_profits()
    ProfitExchanges.objects.filter(Q(buy_name__icontains='hitbtc') | Q(sell_name__icontains='hitbtc')).delete()
    with transaction.atomic():
        for result in hitbtc_result:
            pair = ProfitExchanges(pair=result['pair'], buy_name=result['buy_name'], buy=result['buy'],
                                   buy_ask=result['buy_ask'], buyurl=result['buyurl'],
                                   sell_name=result['sell_name'], sell=result['sell'], sell_bid=result['sell_bid'],
                                   percent=result['percent'], tokenid=result['tokenid'], sellurl=result['sellurl'])
            pair.save()


async def init_all_compared_tokens():
    print('start set compared_tokens: ' + str(datetime.datetime.now()))
    while True:
        await set_all_compared_tokens()


async def exchanges_idex():
    while True:
        print('start idex exchanges: ' + str(datetime.datetime.now()))
        await idex_result()
        print('end idex exchanges: ' + str(datetime.datetime.now()))


async def exchanges_hotbit():
    print('start hotbit exchanges: ' + str(datetime.datetime.now()))
    while True:
        await hotbit_result()
        # print('end exchanges: ' + str(datetime.datetime.now()))


async def exchanges_hitbtc():
    print('start hotbit exchanges: ' + str(datetime.datetime.now()))
    while True:
        await hitbtc_result()

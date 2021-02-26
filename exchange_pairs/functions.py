import datetime
import time

from asgiref.sync import sync_to_async
from django.db.models import Q

from exchange_pairs.models import ProfitExchanges
from hotbit_module.functions import hotbit_profits
from idex_module.functions import idex_profits


@sync_to_async
def idex_result():
    print('start idex exchanges: ' + str(datetime.datetime.now()))
    idex_result = idex_profits()
    ProfitExchanges.objects.filter(Q(buy_name__contains='IDEX') | Q(sell_name__contains='IDEX')).delete()
    for result in idex_result:
        pair = ProfitExchanges(pair=result['pair'], buy_name=result['buy_name'], buy=result['buy'],
                               sell_name=result['sell_name'], sell=result['sell'], percent=result['percent'],
                               tokenid=result['tokenid'], buyurl=result['buyurl'], sellurl=result['sellurl'])
        pair.save()
    print('start idex exchanges: ' + str(datetime.datetime.now()))


@sync_to_async
def hotbit_result():
    hotbit_result = hotbit_profits()
    ProfitExchanges.objects.filter(Q(buy_name__contains='HOTBIT') | Q(sell_name__contains='HOTBIT')).delete()
    for result in hotbit_result:
        pair = ProfitExchanges(pair=result['pair'], buy_name=result['buy_name'], buy=result['buy'],
                               sell_name=result['sell_name'], sell=result['sell'], percent=result['percent'],
                               tokenid=result['tokenid'], buyurl=result['buyurl'], sellurl=result['sellurl'])
        pair.save()


async def exchanges_idex():
    while True:
        await idex_result()
        # print('end exchanges: ' + str(datetime.datetime.now()))


async def exchanges_hotbit():
    print('start hotbit exchanges: ' + str(datetime.datetime.now()))
    while True:
        await hotbit_result()
        # print('end exchanges: ' + str(datetime.datetime.now()))

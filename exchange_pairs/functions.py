import datetime

from exchange_pairs.models import ProfitExchanges
from hotbit_module.functions import hotbit_profits
from idex_module.functions import idex_profits


def exchanges_profits():
    hotbit_result = hotbit_profits()
    idex_result = idex_profits()
    id = 0
    ProfitExchanges.objects.all().delete()
    for result in hotbit_result:
        id += 1
        pair = ProfitExchanges(id=id, pair=result['pair'], buy_name=result['buy_name'], buy=result['buy'],
                               sell_name=result['sell_name'], sell=result['sell'], percent=result['percent'],
                               tokenid=result['tokenid'], buyurl=result['buyurl'], sellurl=result['sellurl'])
        pair.save()
    for result in idex_result:
        id += 1
        pair = ProfitExchanges(id=id, pair=result['pair'], buy_name=result['buy_name'], buy=result['buy'],
                               sell_name=result['sell_name'], sell=result['sell'], percent=result['percent'],
                               tokenid=result['tokenid'], buyurl=result['buyurl'], sellurl=result['sellurl'])
        pair.save()


def exchanges_init():
    while True:
        print('start exchanges: ' + str(datetime.datetime.now()))
        exchanges_profits()
        print('end exchanges: ' + str(datetime.datetime.now()))

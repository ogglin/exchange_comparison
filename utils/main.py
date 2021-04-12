from pathlib import Path

from asgiref.sync import sync_to_async

# from utils.markets import set_hotbit_market, set_hitbtc_market, set_idex_market
# from utils.parse_etherscan import set_new_token
from utils.markets import set_bilaxy_market
from utils.parse_files import get_file

TEMP_DIR = str(Path(__file__).resolve(strict=True).parent.parent) + '/temp/'
# file = TEMP_DIR + 'контракты хит бтс2.txt'
file = TEMP_DIR + 'ХОТ бит контракт 07 04.txt'


@sync_to_async
def init_utest():
    # get_file(file)
    # set_new_token()
    # set_hotbit_market()
    # set_hitbtc_market()
    # set_idex_market()
    # set_bilaxy_market()
    pass


if __name__ == '__main__':
    get_file(file)

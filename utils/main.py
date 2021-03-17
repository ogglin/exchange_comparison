import csv
from pathlib import Path
from exchange_pairs.models import TrustedPairs
from hitbtc_module.models import Hitbtc
from hotbit_module.models import Hotbit

TEMP_DIR = str(Path(__file__).resolve(strict=True).parent.parent) + '/temp/'
file = TEMP_DIR + 'hitbtc2.csv'


def get_file(f):
    with open(f, newline='') as fc:
        reader = csv.reader(fc)
        p_file = list(reader)
    objs = Hitbtc.objects.all().order_by('id')
    new_symbols = []
    for p in p_file:
        token = p[0].split(';')
        contract = token[0]
        name = token[1]
        symbol = token[2]
        for pair in objs:
            if pair.exch_direction.lower() == symbol.lower():
                if pair.contract:
                    if pair.contract.lower() == contract.lower():
                        pass
                        print('True contract', symbol, pair.contract, contract)
                        pair.tsymbol = symbol
                        pair.save()
                    else:
                        print('fake', symbol, pair.contract, contract)
                else:
                    print('no contract, save new vals', token)
                    pair.contract = contract
                    pair.tsymbol = symbol
                    pair.save()
            # else:
                # print('Not match:', token, pair.contract, contract)
                # new_symbols.append(token)
    # print('Not match:', new_symbols)

        # else:
        #     print('New token')
        #     print(name, symbol, contract)


def init_utest():
    pass


if __name__ == '__main__':
    get_file(file)

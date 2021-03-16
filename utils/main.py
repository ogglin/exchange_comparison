import csv
from pathlib import Path
from exchange_pairs.models import TrustedPairs

TEMP_DIR = str(Path(__file__).resolve(strict=True).parent.parent) + '/temp/'
file = TEMP_DIR + 'export-address-token.csv'


def get_file(f):
    with open(f, newline='') as fc:
        reader = csv.reader(fc)
        p_file = list(reader)
    objs = TrustedPairs.objects.all().order_by('id')
    new_symbols = []
    for p in p_file:
        token = p[0].split(';')
        contract = token[0]
        name = token[1]
        symbol = token[2]
        for pair in objs:
            if pair.token.lower() == symbol.lower():
                # print('Match', token, pair, pair.contract)
                if pair.contract:
                    if pair.contract.lower() == contract.lower():
                        pass
                        # print('True contract', symbol, pair.contract, contract)
                        # pair.token_name = name
                        # pair.save()
                    else:
                        print(symbol, pair.contract, contract)
                else:
                    print('no contract, save new vals', token)
                    pair.contract = contract
                    pair.token_name = name
                    pair.save()
            # else:
                # print('Not match:', token, pair.contract, contract)
                # new_symbols.append(token)
    # print('Not match:', new_symbols)

        # else:
        #     print('New token')
        #     print(name, symbol, contract)


def init_utest():
    get_file(file)


if __name__ == '__main__':
    get_file(file)

import csv
import re

from exchange_pairs.models import TrustedPairs


# from hitbtc_module.models import Hitbtc
# from hotbit_module.models import Hotbit


def get_file(f):
    with open(f, newline='') as fc:
        reader = csv.reader(fc)
        p_file = list(reader)
        idx = 0
        el = []
        all_el = []
        f_elems = []
        for p in p_file:
            if idx < 3:
                el.extend(p)
                idx += 1
            else:
                all_el.append(el)
                el = []
                el.extend(p)
                idx = 1
        for ae in all_el:
            name = re.sub(r'[.]', '', ae[0])
            contract = ae[1]
            symbol = re.sub(r'[.]', '', re.search(r'^[^\t]*', ae[2]).group(0))
            # print(name, contract, symbol)
            f_elems.append([name, contract, symbol])
    tobjs = TrustedPairs.objects.all()
    for fe in f_elems:
        print(fe)
        for pair in tobjs:
            if pair.contract is not None:
                if pair.contract.lower() == fe[1].lower():
                    try:
                        pair.tsymbol = fe[2]
                        pair.token_name = fe[0]
                        pair.is_active = True
                        pair.save()
                    except:
                        try:
                            pair.tsymbol = fe[2]+'_hot'
                            pair.token_name = fe[0]
                            pair.is_active = True
                            pair.save()
                        except:
                            print(fe[0].lower(), pair.token.lower(), pair.contract, fe[2], fe[1])
        # try:
        #     print('try')
        #     tpair = TrustedPairs.objects.filter(contract__icontains=fe[1].lower()).all()
        #     if len(tpair) < 1:
        #         spair = TrustedPairs(token=fe[0], contract=fe[1].lower(), tsymbol=fe[2], token_name=fe[0],
        #                              is_active=True)
        #         spair.save()
        # except:
        #     pass

    # objs = Hitbtc.objects.all().order_by('id')
    # new_symbols = []
    # for p in p_file:
    #     token = p[0].split(';')
    #     contract = token[0]
    #     name = token[1]
    #     symbol = token[2]
    #     for pair in objs:
    #         if pair.exch_direction.lower() == symbol.lower():
    #             if pair.contract:
    #                 if pair.contract.lower() == contract.lower():
    #                     pass
    #                     print('True contract', symbol, pair.contract, contract)
    #                     pair.tsymbol = symbol
    #                     pair.save()
    #                 else:
    #                     print('fake', symbol, pair.contract, contract)
    #             else:
    #                 print('no contract, save new vals', token)
    #                 pair.contract = contract
    #                 pair.tsymbol = symbol
    #                 pair.save()
    #         # else:
    #             # print('Not match:', token, pair.contract, contract)
    #             # new_symbols.append(token)
    # # print('Not match:', new_symbols)
    #
    #     # else:
    #     #     print('New token')
    #     #     print(name, symbol, contract)
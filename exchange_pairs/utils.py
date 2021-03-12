from exchange_comparison.utils import _query

proxys = [
    ['193.111.152.28', '16881', 'user53105', '3x7cyr'],
    ['185.161.211.209', '16881', 'user53105', '3x7cyr'],
    ['193.111.155.237', '16881', 'user53105', '3x7cyr'],
    ['193.111.152.168', '16881', 'user53105', '3x7cyr'],
    ['185.20.187.218', '16881', 'user53105', '3x7cyr'],
    ['193.111.154.67', '16881', 'user53105', '3x7cyr'],
    ['185.161.209.185', '16881', 'user53105', '3x7cyr'],
    ['185.36.189.145', '16881', 'user53105', '3x7cyr'],
    ['185.36.190.130', '16881', 'user53105', '3x7cyr'],
    ['193.111.152.90', '16881', 'user53105', '3x7cyr'],
    ['213.32.84.200', '11565', 'user53105', '3x7cyr'],
    ['213.32.84.143', '11565', 'user53105', '3x7cyr'],
    ['79.137.15.162', '11565', 'user53105', '3x7cyr'],
    ['213.32.84.176', '11565', 'user53105', '3x7cyr'],
    ['147.135.175.235', '11565', 'user53105', '3x7cyr'],
    ['178.32.67.197', '11565', 'user53105', '3x7cyr'],
    ['178.32.67.151', '11565', 'user53105', '3x7cyr'],
    ['213.32.84.202', '11565', 'user53105', '3x7cyr'],
    ['147.135.206.67', '11565', 'user53105', '3x7cyr'],
    ['213.32.84.46', '11565', 'user53105', '3x7cyr'],
]


class CompareToken(object):
    buy_price = 0
    sell_price = 0
    percent = 0
    vol = 0.8
    e_vol = 1

    def __init__(self, buy_from, buy_symbol, buy_prices, buy_volume, sell_to, sell_symbol, sell_prices, sell_volume,
                 contract, profit_percent, currency):
        """Constructor"""
        self.buy_from = buy_from
        self.buy_symbol = buy_symbol
        self.asks = buy_prices
        self.buy_volume = buy_volume
        self.sell_to = sell_to
        self.sell_symbol = sell_symbol
        self.bids = sell_prices
        self.sell_volume = sell_volume
        self.contract = contract
        self.profit_percent = profit_percent
        self.buy_currency = currency
        self.sell_currency = currency

    def compare(self):
        """Compare tokens"""
        """Set buy price"""
        if 'btc' not in self.buy_symbol.lower():
            self.buy_currency = 1
        if 'btc' not in self.sell_symbol.lower():
            self.sell_currency = 1
        if isinstance(self.asks, list):
            self.buy_price = 0
            self.buy_volume = 0
            for ask in self.asks:
                if self.buy_volume <= self.e_vol:
                    self.buy_price = float(ask[0])
                    self.buy_volume += float(ask[1]) * float(ask[0]) / self.buy_currency
        else:
            self.buy_price = self.asks

        """Set sell price"""
        if isinstance(self.bids, list):
            self.sell_price = 0
            self.sell_volume = 0
            for bid in self.bids:
                if self.sell_volume <= self.e_vol:
                    self.sell_price = float(bid[0])
                    self.sell_volume += float(bid[1]) * float(bid[0]) / self.sell_currency
        else:
            self.sell_price = self.bids

        """Check profit and return it"""
        if self.buy_price / self.buy_currency > 0 and self.sell_price / self.sell_currency > 0 and self.buy_volume > self.vol and self.sell_volume > self.vol:
            self.percent = (
                                   self.sell_price / self.sell_currency - self.buy_price / self.buy_currency) / self.sell_price / self.sell_currency * 100
            profit = {
                'buy_from': self.buy_from.lower(),
                'buy_symbol': self.buy_symbol,
                'buy_price': self.buy_price / self.buy_currency,
                'buy_volume': self.buy_volume,
                'buy_ask': self.buy_price,
                'sell_to': self.sell_to.lower(),
                'sell_symbol': self.sell_symbol,
                'sell_price': self.sell_price / self.sell_currency,
                'sell_volume': self.sell_volume,
                'sell_bid': self.sell_price,
                'percent': self.percent,
                'contract': self.contract,
            }
        else:
            profit = None
        if self.percent > self.profit_percent:
            return profit
        else:
            return None


class GetTokens(object):
    at = None

    def __init__(self, module, _all: bool):
        # Get module name
        """Constructor"""
        self.module = module
        self._all = _all

    def __idex(self):
        return _query('''
            SELECT tp.tsymbol, lower(tp.contract), 'idex' as site, mi.exch_direction token, mi.highest_bid, mi.lowest_ask, 
            mi.volume FROM trusted_pairs tp LEFT JOIN module_idex mi ON lower(mi.tsymbol) = lower(tp.tsymbol) and 
            tp.contract is not null LEFT JOIN settings_modules ON settings_modules.module_name = 'idex' 
            WHERE mi.exch_direction is not null  and tp.is_active is true AND mi.is_active is true and 
            settings_modules.is_active is true;''')

    def __hotbit(self):
        return _query('''
            SELECT tp.tsymbol, lower(tp.contract), 'hotbit' as site, mh.symbol token, mh.sell, mh.buy, mh.volume 
            FROM trusted_pairs tp LEFT JOIN module_hotbit mh ON lower(mh.tsymbol) = lower(tp.tsymbol) and 
            tp.contract is not null LEFT JOIN settings_modules ON settings_modules.module_name = 'hotbit' 
            WHERE mh.exch_direction is not null  and tp.is_active is true AND mh.is_active is true and 
            settings_modules.is_active is true;''')

    def __hitbtc(self):
        return _query('''
            SELECT tp.tsymbol, lower(tp.contract), 'hitbtc' as site, mh.symbol token, mh.sell, mh.buy, mh.volume 
            FROM trusted_pairs tp LEFT JOIN module_hitbtc mh ON lower(mh.tsymbol) = lower(tp.tsymbol) and 
            tp.contract is not null LEFT JOIN settings_modules ON settings_modules.module_name = 'hitbtc' 
            WHERE mh.exch_direction is not null and tp.is_active is true AND mh.is_active is true and 
            settings_modules.is_active is true;''')

    def __uniswap(self):
        return _query('''
            SELECT tp.tsymbol, lower(tp.contract), 'uniswap' as site, mu.exch_direction token, mu.highest_bid sell, 
            mu.lowest_ask buy, mu.volume FROM trusted_pairs tp 
            LEFT JOIN module_uniswap mu ON lower(mu.tsymbol) = lower(tp.tsymbol) and tp.contract is not null 
            LEFT JOIN settings_modules ON settings_modules.module_name = 'uniswap' WHERE mu.exch_direction is not null 
            and tp.is_active is true AND mu.is_active is true and settings_modules.is_active is true 
            and (mu.highest_bid > 0 or mu.lowest_ask > 0);''')

    def __bancor(self):
        return _query('''
            SELECT tp.tsymbol, lower(tp.contract), 'bancor' as site, mb.exch_direction token, mb.highest_bid sell, 
            mb.lowest_ask buy, mb.volume FROM trusted_pairs tp 
            LEFT JOIN module_bancor mb ON lower(mb.tsymbol) = lower(tp.tsymbol) and tp.contract is not null 
            LEFT JOIN settings_modules ON settings_modules.module_name = 'bancor' WHERE mb.exch_direction is not null 
            and tp.is_active is true AND mb.is_active is true and settings_modules.is_active is true 
            and (mb.highest_bid > 0 or mb.lowest_ask > 0);''')

    def __kyber(self):
        return _query('''
            SELECT tp.tsymbol, lower(tp.contract), 'kyber' as site, mk.exch_direction token, mk.highest_bid sell, 
            mk.lowest_ask buy, mk.volume FROM trusted_pairs tp 
            LEFT JOIN module_kyber mk ON lower(mk.tsymbol) = lower(tp.tsymbol) and tp.contract is not null 
            LEFT JOIN settings_modules ON settings_modules.module_name = 'kyber' WHERE mk.exch_direction is not null 
            and tp.is_active is true AND mk.is_active is true and settings_modules.is_active is true 
            and (mk.highest_bid > 0 or mk.lowest_ask > 0);''')

    def tokens(self):
        if self._all:
            self.at = []
            if 'idex' not in self.module:
                self.at.extend(self.__idex())
            if 'hotbit' not in self.module:
                self.at.extend(self.__hotbit())
            if 'hitbtc' not in self.module:
                self.at.extend(self.__hitbtc())
            if 'uniswap' not in self.module:
                self.at.extend(self.__uniswap())
            if 'bancor' not in self.module:
                self.at.extend(self.__bancor())
            if 'kyber' not in self.module:
                self.at.extend(self.__kyber())

            return self.at
        else:
            # Markets
            if 'idex' in self.module:
                self.at = self.__idex()
            if 'hotbit' in self.module:
                self.at = self.__hotbit()
            if 'hitbtc' in self.module:
                self.at = self.__hitbtc()

            # Exchangers
            if 'uniswap' in self.module:
                self.at = self.__uniswap()
            if 'bancor' in self.module:
                self.at = self.__bancor()
            if 'kyber' in self.module:
                self.at = self.__kyber()
        return self.at


class ResultPrepare(object):
    rpo = None

    def __init__(self, all_result, exchanger):
        # Get module name
        """Constructor"""
        self.all_result = all_result
        self.exchanger = exchanger

    def result(self):
        compare_result = []
        for results in self.all_result:
            if results:
                for result in results:
                    if result:
                        buy_name = result['buy_from']
                        pair = result['buy_symbol'].replace('ETH', '').replace('BTC', '')
                        buy = result['buy_price']
                        buy_ask = result['buy_ask']
                        sell_name = result['sell_to']
                        sell_symbol = result['sell_symbol']
                        sell = result['sell_price']
                        sell_bid = result['sell_bid']
                        percent = result['percent']
                        contract = result['contract']
                        tokenid = '0x0000000000000000000000000000000000000000000000000000000000000000'
                        if 'hitbtc' in buy_name:
                            if 'ETH' in result['buy_symbol']:
                                buyurl = 'https://hitbtc.com/' + pair + '-to-eth'
                            if 'BTC' in result['buy_symbol']:
                                buyurl = 'https://hitbtc.com/' + pair + '-to-btc'
                        if 'hotbit' in buy_name:
                            buyurl = 'https://www.hotbit.io/exchange?symbol=' + sell_symbol.replace('/', '_')
                        if buy_name == 'idex':
                            buyurl = 'https://exchange.idex.io/trading/' + pair + '-ETH'
                        if buy_name == 'bankor':
                            buyurl = 'https://app.bancor.network/eth/swap?from=0xEeeeeEeeeEeEeeEeEeEeeEEEeeeeEeeeeeeeEEeE&to=' + \
                                     str(contract)
                        if buy_name == 'kyber':
                            buyurl = 'https://kyberswap.com/swap/eth-' + pair
                        if buy_name == 'uniswap':
                            buyurl = 'https://app.uniswap.org/#/swap?outputCurrency=' + str(contract)
                        if buy_name == 'uniswap_one':
                            buyurl = 'https://app.uniswap.org/#/swap?outputCurrency=' + str(contract) + '&use=v1'

                        if 'hitbtc' in sell_name:
                            if 'ETH' in result['buy_symbol']:
                                sellurl = 'https://hitbtc.com/' + pair + '-to-eth'
                            if 'BTC' in result['buy_symbol']:
                                sellurl = 'https://hitbtc.com/' + pair + '-to-btc'
                        if 'hotbit' in sell_name:
                            sellurl = 'https://www.hotbit.io/exchange?symbol=' + sell_symbol.replace('/', '_')
                        if sell_name == 'idex':
                            sellurl = 'https://exchange.idex.io/trading/' + pair + '-ETH'
                        if sell_name == 'bankor':
                            sellurl = 'https://app.bancor.network/eth/swap?from=' + str(contract) \
                                      + '&to=0xEeeeeEeeeEeEeeEeEeEeeEEEeeeeEeeeeeeeEEeE'
                        if sell_name == 'kyber':
                            sellurl = 'https://kyberswap.com/swap/eth-' + pair
                        if sell_name == 'uniswap':
                            sellurl = 'https://app.uniswap.org/#/swap?outputCurrency=' + str(contract)
                        if sell_name == 'uniswap_one':
                            sellurl = 'https://app.uniswap.org/#/swap?outputCurrency=' + str(contract) + '&use=v1'
                        compare_result.append(
                            {'pair': result['buy_symbol'], 'buy_name': buy_name, 'buy': buy, 'buy_ask': buy_ask,
                             'sell_name': sell_name, 'sell': sell, 'sell_bid': sell_bid,
                             'percent': percent, 'tokenid': tokenid, 'buyurl': buyurl, 'sellurl': sellurl})
        return compare_result

class CompareToken(object):
    buy_price = 0
    sell_price = 0
    percent = 0
    vol = 0.8
    e_vol = 1

    def __init__(self, buy_from, buy_symbol, buy_prices, buy_volume, sell_to, sell_symbol, sell_prices, sell_volume,
                 contract, profit_percent, currency):
        # print(buy_from, asks, buy_volume, sell_to, bids, sell_volume, symbol, contract, profit_percent, currency)
        """Constructor"""
        self.buy_from = buy_from
        self.asks = buy_prices
        self.sell_to = sell_to
        self.bids = sell_prices
        self.buy_symbol = buy_symbol
        self.sell_symbol = sell_symbol
        self.contract = contract
        self.profit_percent = profit_percent
        self.buy_currency = currency
        self.sell_currency = currency
        self.buy_volume = buy_volume
        self.sell_volume = sell_volume

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
                    self.buy_price = float(ask[0]) / self.buy_currency
                    self.buy_volume += float(ask[1]) * float(ask[0]) / self.buy_currency
                    # print(float(ask[0]))
                    # print(self.buy_price)
                    # print(self.buy_volume)
                    # print('-------------')
        else:
            self.buy_price = self.asks

        """Set sell price"""
        if isinstance(self.bids, list):
            self.sell_price = 0
            self.sell_volume = 0
            for bid in self.bids:
                if self.sell_volume <= self.e_vol:
                    self.sell_price = float(bid[0]) / self.sell_currency
                    self.sell_volume += float(bid[1]) * float(bid[0]) / self.sell_currency
        else:
            self.sell_price = self.bids

        """Check profit and return it"""
        if self.buy_price > 0 and self.sell_price > 0 and self.buy_volume > self.vol and self.sell_volume > self.vol:
            self.percent = (self.sell_price - self.buy_price) / self.sell_price * 100
            profit = {'symbol': self.buy_symbol, 'percent': self.percent, 'contract': self.contract,
                      'buy_from': self.buy_from, 'buy_price': self.buy_price, 'buy_volume': self.buy_volume,
                      'sell_to': self.sell_to, 'sell_price': self.sell_price, 'sell_volume': self.sell_volume}
        else:
            profit = None
        # print(profit)
        if self.percent > self.profit_percent:
            return profit
        else:
            return None

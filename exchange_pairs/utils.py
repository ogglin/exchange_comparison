class CompareToken(object):
    buy_price = 0
    sell_price = 0
    percent = 0
    vol = 0.8
    e_vol = 1

    def __init__(self, buy_from, asks, buy_volume, sell_to, bids, sell_volume, symbol, contract, profit_percent,
                 currency):
        # print(buy_from, asks, buy_volume, sell_to, bids, sell_volume, symbol, contract, profit_percent, currency)
        """Constructor"""
        self.buy_from = buy_from
        self.asks = asks
        self.sell_to = sell_to
        self.bids = bids
        self.symbol = symbol
        self.contract = contract
        self.profit_percent = profit_percent
        self.currency = currency
        self.buy_volume = buy_volume
        self.sell_volume = sell_volume

    def compare(self):
        """Compare tokens"""
        """Set buy price"""
        if isinstance(self.asks, list):
            self.buy_price = 0
            self.buy_volume = 0
            for ask in self.asks:
                if self.buy_volume <= self.e_vol:
                    self.buy_price = float(ask[0]) / self.currency
                    self.buy_volume += float(ask[1]) * float(ask[0]) / self.currency
        else:
            self.buy_price = self.asks

        """Set sell price"""
        if isinstance(self.bids, list):
            self.sell_price = 0
            self.sell_volume = 0
            for bid in self.bids:
                if self.sell_volume <= self.e_vol:
                    self.sell_price = float(bid[0]) / self.currency
                    self.sell_volume += float(bid[1]) * float(bid[0]) / self.currency
        else:
            self.sell_price = self.bids

        """Check profit and return it"""
        if self.buy_price > 0 and self.sell_price > 0 and self.buy_volume > self.vol and self.sell_volume > self.vol:
            self.percent = (self.sell_price - self.buy_price) / self.sell_price * 100
            profit = {'symbol': self.symbol, 'percent': self.percent, 'contract': self.contract,
                      'buy_from': self.buy_from, 'buy_price': self.buy_price, 'buy_volume': self.buy_volume,
                      'sell_to': self.sell_to, 'sell_price': self.sell_price, 'sell_volume': self.sell_volume}
        else:
            profit = None
        if self.percent > self.profit_percent:
            return profit
        else:
            return None
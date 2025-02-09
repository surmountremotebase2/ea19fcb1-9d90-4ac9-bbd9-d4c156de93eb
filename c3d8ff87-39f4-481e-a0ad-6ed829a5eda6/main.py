from surmount.base_class import Strategy, TargetAllocation, backtest
from surmount.logging import log

class TradingStrategy(Strategy):
    def __init__(self):
        self.tickers = ["SPY", "GLD"]
        self.weights = [60, 40]
        self.count = 0

    @property
    def interval(self):
        return "1day"

    @property
    def assets(self):
        return self.tickers

    def run(self, data):
        self.count += 1
        if (self.count % 30 == 1):
            allocation_dict = {'SPY':60, 'GLD':40}
            return TargetAllocation(allocation_dict)
        return None
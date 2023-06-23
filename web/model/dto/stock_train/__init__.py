class StockTrain:
    def __init__(self, date, open, close, high, low, volume, higher=0):
        self.date = date
        self.close = close
        self.open = open
        self.high = high
        self.low = low
        self.volume = volume
        self.higher = higher

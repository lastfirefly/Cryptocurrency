class DimCoin:
    def __init__(self, cryptoCoin: object):
        self.dfCoin = cryptoCoin

    def Symbol(self):
        return self.dfCoin['Symbol']
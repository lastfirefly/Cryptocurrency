class ProcessCoin:
    def __init__(self, cryptoCoin: object):
        self.dfCoin = cryptoCoin

    def getName(self):
        return self.dfCoin['Name'].drop_duplicates()

    def setTypeCoin(self):
        coin = self.dfCoin['Symbol'].drop_duplicates()
        return coin.map({
            "BNB": "cryptocurrency",
            "BTC": "cryptocurrency",
            "ADA": "cryptocurrency",
            "DOGE": "cryptocurrency",
            "ETH": "cryptocurrency",
            "DOT": "cryptocurrency",
            "USDT": "stablecoin",
            "UNI": "cryptocurrency",
            "USDC": "stablecoin",
            "XRP": "cryptocurrency"
        })

    def setCreationDate(self):
        coin = self.dfCoin['Symbol'].drop_duplicates()
        return coin.map({
            "BNB": "2017-07-25",
            "BTC": "2009-01-03",
            "ADA": "2017-09-29",
            "DOGE": "2013-12-06",
            "ETH": "2015-07-30",
            "DOT": "2020-05-26",
            "USDT": "2014-10-06",
            "UNI": "2020-09-17",
            "USDC": "2018-09-26",
            "XRP": "2012-08-01"
        })



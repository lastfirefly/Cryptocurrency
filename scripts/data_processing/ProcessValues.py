class ProcessValues():
    def __init__(self, cryptoCoin: object):
        self.df = cryptoCoin

    def MaxMin(self):
        return self.__GetColumns('High', 'Low')

    def OpenClose(self):
        return self.__GetColumns('Open', 'Close')

    def Marketcap(self):
        return self.__GetColumns('Marketcap')

    def __GetColumns(self, *args: str):
        query = self.df[list(args)] if len(args) > 1 else self.df[args[0]]
        return query

import pandas as pd

class ProcessDate:
    def __init__(self, cryptoCoin: object):
        self.dfDate = pd.to_datetime(cryptoCoin['Date'])

    def FullDate(self):
        return list(self.dfDate.dt.strftime('%Y-%m-%d'))

    def WeekDay(self):
        dfDay = self.dfDate.dt.weekday
        return list(dfDay.map({ 0: "Dom",
            1: "Seg", 2: "Ter", 3: "Qua",
            4: "Qui", 5: "Sex", 6: "Sáb"
        }))

    def MonthDay(self):
        return list(self.dfDate.dt.day)    

    def Month(self):
        return list(self.dfDate.dt.month)

    def Year(self):
        return list(self.dfDate.dt.year)
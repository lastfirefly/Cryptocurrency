import pandas as pd

class ProcessDate:
    def __init__(self, cryptoCoin: object):
        self.dfDate = pd.to_datetime(cryptoCoin['Date'])

    def FullDate(self):
        return self.dfDate.dt.strftime('%d-%m-%Y')

    def WeekDay(self):
        dfDay = self.dfDate.dt.weekday
        return dfDay.map({ 0: "Domingo",
            1: "Seg", 2: "Ter", 3: "Qua",
            4: "Qui", 5: "Sex", 6: "Sáb"
        })

    def MonthDay(self):
        return self.dfDate.dt.day    

    def Year(self):
        return self.dfDate.dt.year
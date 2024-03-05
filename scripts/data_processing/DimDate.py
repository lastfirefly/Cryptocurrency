import pandas as pd

class DimDate:
    def __init__(self, cryptoCoin: object):
        self.dfDate = pd.to_datetime(cryptoCoin['Date'])

    def FullDate(self):
        return self.dfDate.dt.strftime('%Y-%m-%d')

    def WeekDay(self):
        dfDay = self.dfDate.dt.weekday
        return dfDay.map({ 0: "Domingo",
            1: "Segunda-Feira", 2: "Terça-Feira", 3: "Quarta-Feira",
            4: "Quinta-Feira", 5: "Sexta-Feira", 6: "Sábado"
        })

    def MonthDay(self):
        return self.dfDate.dt.day    

    def Fortnight(self):
        monthDays = self.MonthDay()
        listFortnight = []
        for day in monthDays.values:
            if day <= 15:
                listFortnight.append('1º')
            else:
                listFortnight.append('2º')
        self.dfDate['Quinzena'] = listFortnight
        return self.dfDate['Quinzena']

    def Month(self):
        months = self.dfDate.dt.month
        return months.map({
            1: "Janeiro", 2: "Fevereiro", 3: "Março", 4: "Abril",
            5: "Maio", 6: "Junho", 7: "Julho", 8: "Agosto",
            9: "Setembro", 10: "Outubro", 11: "Novembro", 12: "Dezembro"
        })

    def Quarter(self):
        months = self.dfDate.dt.month
        return months.apply(lambda m: "1º" if m in range(1,4) 
                        else("2º" if m in range(4,7) 
                            else("3º" if m in range(7,10) 
                                else "4º")))

    def Semester(self):
        months = self.dfDate.dt.month
        return months.apply(lambda m: "1º" if m in range(1,7) else "2º")

    def Year(self):
        return self.dfDate.dt.year
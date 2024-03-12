import pandas as pd
import os
from scripts.data_processing.ProcessCoin import ProcessCoin
from scripts.data_processing.ProcessDate import ProcessDate
from scripts.data_processing.ProcessValues import ProcessValues
from scripts.load.LoadData import LoadData
from database.Ddl import Ddl
from database.Database import Database

dataSource = './data/source_data/'

crypto = {
        "BNB": 1, "BTC": 2,
        "ADA": 3, "DOGE": 4,
        "ETH": 5, "DOT": 6,
        "USDT": 7, "UNI": 8,
        "USDC": 9, "XRP": 10
}

dateValues = {
    "data_completa": [],
    "diasemana": [],
    "diames": [],
    "mes": [],
    "ano": [],
    "id_moeda": []
}

infoCoinValues = {
    "nome": [],
    "tipo_moeda": [],
    "data_criacao": []
}

values = {
    "marketcap_dia": [],
    "valor_abre": [],
    "valor_fecha": [],
    "valor_min": [],
    "valor_max": [],
    "id_moeda": []
}

for arquive in os.listdir(dataSource):
    df = pd.read_csv(f'{dataSource}/{arquive}')
    df = df.drop(columns=['SNo'])

    fCoin = ProcessCoin(df)
    fDate = ProcessDate(df)
    fValues = ProcessValues(df)

    id_crypto = df['Symbol']

    dateValues["id_moeda"].extend(id_crypto.map(crypto))
    dateValues['data_completa'].extend(fDate.FullDate())
    dateValues['diasemana'].extend(fDate.WeekDay())
    dateValues['diames'].extend(fDate.MonthDay())
    dateValues['mes'].extend(fDate.Month())
    dateValues['ano'].extend(fDate.Year())

    infoCoinValues['nome'].extend(fCoin.getName())
    infoCoinValues['tipo_moeda'].extend(fCoin.setTypeCoin())
    infoCoinValues['data_criacao'].extend(fCoin.setCreationDate())

    values["id_moeda"].extend(id_crypto.map(crypto))
    values['marketcap_dia'].extend(fValues.Marketcap())
    values['valor_abre'].extend(fValues.OpenClose()['Open'])
    values['valor_fecha'].extend(fValues.OpenClose()['Close'])
    values['valor_max'].extend(fValues.MaxMin()['High'])
    values['valor_min'].extend(fValues.MaxMin()['Low'])
    
dfDate = pd.DataFrame(dateValues)
dfValues = pd.DataFrame(values)
dfCoin = pd.DataFrame(infoCoinValues)
dfDayValue = pd.DataFrame()
dfDayValue['idCalendario'] = list(range(1, len(dfDate) + 1))
dfDayValue['idMoeda'] = dfDate['id_moeda']
dfDayValue['idValores'] = list(range(1, len(dfValues) + 1))
dfCoin['idCalendario'] = dfDayValue['idCalendario']
dfValues['idCalendario'] = dfDayValue['idCalendario']

ddl = Ddl()
databaseName = "cryptocurrency"

ddl.CreateDatabase(databaseName)
ddl.Use(databaseName)

tables = {}
tables['MoedasInfo'] = ('''
    CREATE TABLE moedas_info (
    idmoedas_info INT PRIMARY KEY NOT NULL auto_increment, 
    nome VARCHAR(15) NOT NULL,
    tipo_moeda VARCHAR(20) NOT NULL,
    data_criacao DATE NOT NULL
    ) ENGINE=InnoDB
''')

tables['Calendario'] = ('''
    CREATE TABLE calendario (
    idcalendario INT PRIMARY KEY NOT NULL auto_increment,
    datacompleta DATE,
    diasemana CHAR(3),
    diames INT NOT NULL,
    mes INT NOT NULL,
    ano INT NOT NULL,
    idmoedas_info INT NOT NULL
    ) ENGINE=InnoDB
''')

tables['MarketcapDia'] = ('''
    CREATE TABLE marketcap_dia(
    idmarketcap_dia INT PRIMARY KEY NOT NULL auto_increment,
    valor_marketcap FLOAT NOT NULL,
    idmoedas_info INT,
    idcalendario INT
    ) ENGINE=InnoDB
''')

tables['AbreFechaDia'] = ('''
    CREATE TABLE abrefecha_dia(
    idabrefecha_dia INT PRIMARY KEY NOT NULL auto_increment,
    valor_abert FLOAT NOT NULL,
    valor_fech FLOAT NOT NULL,
    idmoedas_info INT,
    idcalendario INT
    ) ENGINE=InnoDB
''')

tables['MinMaxDia'] = ('''
    CREATE TABLE minmax_dia(
    idminmax_dia INT PRIMARY KEY NOT NULL auto_increment,
    max_valor FLOAT NOT NULL,
    min_valor FLOAT NOT NULL,
    idmoedas_info INT,
    idcalendario INT
    ) ENGINE=InnoDB
''')

tables['ValorDia'] = ('''
    CREATE TABLE valor_dia(
    idvalor_dia INT PRIMARY KEY NOT NULL auto_increment,
    idmoedas_info INT,
    idmarketcap_dia INT,
    idabrefecha_dia INT,
    idminmax_dia INT,
    idcalendario INT
    ) ENGINE=InnoDB
''')

ddl.CreateTables(tables)

load = LoadData()
load.Load(('calendario', dfDate), ('moedas_info', dfCoin), ('marketcap_dia', dfValues), ('abrefecha_dia', dfValues), ('minmax', dfValues), ('valor_dia', dfDayValue))

tablesAlter = {}

tablesAlter['MarketcapDia'] = ('''
    ALTER TABLE marketcap_dia
    ADD CONSTRAINT marketcapfk_idCalendario
    FOREIGN KEY (idcalendario) REFERENCES calendario(idcalendario)
''')

tablesAlter['AbreFechaDia'] = ('''
    ALTER TABLE abrefecha_dia
    ADD CONSTRAINT abrefechafk_idCalendario
    FOREIGN KEY (idcalendario) REFERENCES calendario(idcalendario)
''')

tablesAlter['MinMaxDia'] = ('''
    ALTER TABLE minmax_dia
    ADD CONSTRAINT minmaxfk_idCalendario
    FOREIGN KEY (idcalendario) REFERENCES calendario(idcalendario)
''')

tablesAlter['ValorDia'] = ('''
    ALTER TABLE valor_dia
    ADD CONSTRAINT valorfk_calendario
    FOREIGN KEY (idcalendario) REFERENCES calendario(idcalendario),
    ADD CONSTRAINT valorfk_moeda
    FOREIGN KEY (idmoedas_info) REFERENCES moedas_info(idmoedas_info),
    ADD CONSTRAINT valorfk_marketcap
    FOREIGN KEY (idmarketcap_dia) REFERENCES marketcap_dia(idmarketcap_dia),
    ADD CONSTRAINT valorfk_abrefecha
    FOREIGN KEY (idabrefecha_dia) REFERENCES abrefecha_dia(idabrefecha_dia),
    ADD CONSTRAINT valorfk_minmax
    FOREIGN KEY (idminmax_dia) REFERENCES minmax_dia(idminmax_dia)
''')

tablesAlter['calendario'] = ('''
    ALTER TABLE calendario
    ADD CONSTRAINT calendariofk_idmoeda
    FOREIGN KEY (idmoedas_info) REFERENCES moedas_info(idmoedas_info)
''')

ddl.AlterTable(tablesAlter)

Database().closeConnection()



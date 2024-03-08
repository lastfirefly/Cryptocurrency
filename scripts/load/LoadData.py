from __future__ import print_function
import mysql.connector

class LoadData():
    def __init__(self, config: dict, dataFrame: object):
        self.config = config
        self.dataFrame = dataFrame

    def Load(self, table: str):
        cursor = self.__cursor()

        for index, row in self.dataFrame.iterrows():
            match table:
                case "moedas_info":
                    sql = "INSERT INTO moedas_info (nome, tipo_moeda, data_criacao) VALUES (%s, %s, %s)"
                    values = (row['nome'], row['tipo_moeda'], row['data_criacao'])
                    break
                case "calendario":
                    sql = "INSERT INTO calendario (diasemana, diames, mes, ano) VALUES (%s, %s, %s, %s)"
                    values = (row['diasemana'], row['diames'], row['mes'], row['ano'])
                    break
                case "marketcap_dia":
                    sql = "INSERT INTO marketcap_dia (valor_marketcap) VALUES (%s)"
                    values = (row['marketcap_dia'],)
                    break
                case "abrefecha_dia":
                    sql = "INSERT INTO abrefecha_dia (valor_abert, valor_fech) VALUES (%s, %s)"
                    values = (row['valor_aberto'], row['valor_fechado'])
                    break
                case "minmax":
                    sql = "INSERT INTO minmax (max_valor, min_valor) VALUES (%s, %s)"
                    values = (row['max_valor'], row['min_valor'])
                    break
            
            cursor.execute(sql, values)
            cursor.commit()
            cursor.close()

    def __cursor(self):
        cnx = mysql.connector.connect(**self.config)
        return cnx.cursor()

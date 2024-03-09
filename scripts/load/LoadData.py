import mysql.connector

class LoadData():
    def __init__(self):
        self.cnx = mysql.connector.connect(host="localhost", user="root", database="cryptocurrency")
        self.cursor = self.cnx.cursor()

    def Load(self, *args: list) -> None:
        closeConnection = False

        if args and args[-1] == True:
            closeConnection = True
            args = args[:-1]

        for arg in args:
            table, dataFrame = arg
            for _, row in dataFrame.iterrows():
                match table:
                    case "moedas_info":
                        sql = "INSERT INTO moedas_info (nome, tipo_moeda, data_criacao) VALUES (%s, %s, %s)"
                        values = (row['nome'], row['tipo_moeda'], row['data_criacao'])
                    case "calendario":
                        sql = "INSERT INTO calendario (datacompleta, diasemana, diames, mes, ano) VALUES (%s, %s, %s, %s, %s)"
                        values = (row['data_completa'], row['diasemana'], row['diames'], row['mes'], row['ano'])
                    case "marketcap_dia":
                        sql = "INSERT INTO marketcap_dia (valor_marketcap) VALUES (%s)"
                        values = (row['marketcap_dia'],)
                    case "abrefecha_dia":
                        sql = "INSERT INTO abrefecha_dia (valor_abert, valor_fech) VALUES (%s, %s)"
                        values = (row['valor_abre'], row['valor_fecha'])
                    case "minmax":
                        sql = "INSERT INTO minmax_dia (max_valor, min_valor) VALUES (%s, %s)"
                        values = (row['valor_max'], row['valor_max'])
                
                self.cursor.execute(sql, values)

        if closeConnection:
            self.cnx.commit()
            self.cursor.close()
            self.cnx.close()
            print('FOI CARALHO')

from database.Database import Database

class LoadData:
    def __init__(self):
        self.db = Database()

    def Load(self, *args: list) -> None:
        self.db.cursor.execute("USE cryptocurrency")

        for arg in args:
            table, dataFrame = arg
            for _, row in dataFrame.iterrows():
                match table:
                    case "valor_dia":
                        sql = "INSERT INTO valor_dia (idmoedas_info, idmarketcap_dia, idabrefecha_dia, idminmax_dia, idcalendario)\
                            VALUES (%s, %s, %s, %s, %s)"
                        values = (int(row['idMoeda']), int(row['idValores']), int(row['idValores']), int(row['idValores']), int(row['idCalendario']))
                    case "moedas_info":
                        sql = "INSERT INTO moedas_info (nome, tipo_moeda, data_criacao) VALUES (%s, %s, %s)"
                        values = (str(row['nome']), str(row['tipo_moeda']), str(row['data_criacao']))
                    case "calendario":
                        sql = "INSERT INTO calendario (datacompleta, diasemana, diames, mes, ano, idmoedas_info) VALUES (%s, %s, %s, %s, %s, %s)"
                        values = (str(row['data_completa']), str(row['diasemana']), str(row['diames']), str(row['mes']), str(row['ano']), int(row['id_moeda']))
                    case "marketcap_dia":
                        sql = "INSERT INTO marketcap_dia (valor_marketcap, idmoedas_info, idcalendario) VALUES (%s, %s, %s)"
                        values = (float(row['marketcap_dia']), int(row['id_moeda']), int(row['idCalendario']))
                    case "abrefecha_dia":
                        sql = "INSERT INTO abrefecha_dia (valor_abert, valor_fech, idmoedas_info, idcalendario) VALUES (%s, %s, %s, %s)"
                        values = (float(row['valor_abre']), float(row['valor_fecha']), int(row['id_moeda']), int(row['idCalendario']))
                    case "minmax":
                        sql = "INSERT INTO minmax_dia (max_valor, min_valor, idmoedas_info, idcalendario) VALUES (%s, %s, %s, %s)"
                        values = (float(row['valor_max']), float(row['valor_max']), int(row['id_moeda']), int(row['idCalendario']))
                
                print(f"Inserting into {table} with values: {values}")
                self.db.cursor.execute(sql, values)
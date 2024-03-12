from database.Database import Database

class Ddl:
    def __init__(self):
        self.db = Database()

    def CreateDatabase(self, databaseName: str) -> None:
        try:
            self.db.cursor.execute(f"CREATE DATABASE IF NOT EXISTS {databaseName} DEFAULT CHARACTER SET 'utf8'")
            print(f"Creating database {databaseName}")
        except self.db.error as err:
            print(f"Failed creating database: {err}")
            exit(1)

    def Use(self, databaseName: str) -> None:
        try:
            connection = self.db.get_connection()
            cursor = connection.cursor()
            cursor.execute(f"USE {databaseName}")
            connection.database = databaseName
            cursor.close()
        except self.db.error as err:
            print(f"Database {databaseName} does not exist.")
            if err.errno == self.db.errorcode.ER_BAD_DB_ERROR:
                self.CreateDatabase(databaseName)
                print(f"Database {databaseName} created successfully")
                connection.database = databaseName
            else:
                print(err)

    def CreateTables(self, tables: dict) -> None:
        for tableName in tables:
            tableDescription = tables[tableName]
            try:
                print(f"Creating {tableName}: ", end='')
                self.db.cursor.execute(tableDescription)
            except self.db.error as err:
                if err.errno == self.db.errorcode.ER_TABLE_EXISTS_ERROR:
                    print('already exists.\n')
                elif err.errno != self.db.errorcode.ER_TABLE_EXISTS_ERROR:
                    print(err.msg)
                else:
                    print("OK\n")

    def AlterTable(self, tablesAlter: dict):
        for tableName in tablesAlter:
            tableAlteration = tablesAlter[tableName]
            try:
                print(f"Altering {tableName}: ", end='')
                self.db.cursor.execute(tableAlteration)
                print("OK")
            except self.db.error as err:
                if err.errno != self.db.errorcode.ER_TABLE_EXISTS_ERROR:
                    print(err.msg)

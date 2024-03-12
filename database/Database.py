import mysql.connector
from mysql.connector import Error as MySQLError
from mysql.connector import errorcode as MySQLErrorcode

class Database: 
    def __init__(self):
        self.cnx = mysql.connector.connect(host="localhost", user="root")
        self.cursor = self.cnx.cursor()
        self.error = MySQLError
        self.errorcode = MySQLErrorcode

    def get_connection(self):
        return self.cnx

    def closeConnection(self):
        self.cnx.commit()
        self.cursor.close()
        self.cnx.close()
        print("Close Connection")
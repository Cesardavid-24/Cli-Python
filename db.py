import mysql.connector as mariadb 
from decouple import config
#con el metodo commit se le da persistencia a los datos en la base de datos
class DataBase():

    def __init__(self):
        try:
            self.connection = mariadb.connect(
            host=config('DB_HOST') , port=config('DB_PORT')
            ,user=config('DB_USER'),password=config('DB_PASSWORD'), database=config('DB_TABLE')
            )
        except mariadb.Error as error:
            print("Error: {}" .format(error))

    def disconect(self):
        if self.connection:
            self.connection.close()

    def execute_query(self, query):
        cursor = self.connection.cursor()
        try:
            cursor.execute(query)
    
            cursor.execute(query)
            self.connection.commit()
            return True
        except mariadb.Error as error:
            print("Error: {}" .format(error))
    
    def fetch_data(self ,query):
        cursor = self.connection.cursor()
        try:
            cursor.execute(query)
            data = cursor.fetchall()
            return data
        except mariadb.Error as error:
            print("Error: {}" .format(error))
            return ()
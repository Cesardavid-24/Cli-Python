from db import DataBase
manager = DataBase()

def get_data(query):
    data = manager.fetch_data(query)
    manager.disconect()
    return data

def set_data(query):
    mesage = manager.execute_query(query)
    manager.disconect()
    return mesage

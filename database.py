from config import config_wb
import psycopg2

def commect_bd():
    try:
        connection = psycopg2.connect(
            database=config_wb["database"],
            user=config_wb["user"],
            password=config_wb["password"],
            host=config_wb["host"],
            port=config_wb["port"],
        )
        connection.autocommit = True
        return connection
    except Exception as ex:
        print(ex)
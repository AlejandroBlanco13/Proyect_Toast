import psycopg2

class Database:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            # Configurar la conexión a PostgreSQL
            cls._instance = psycopg2.connect(
                dbname="toast",
                user="postgres",
                password="a123",
                host="localhost"
            )
        return cls._instance

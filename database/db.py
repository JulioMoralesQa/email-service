import sys
import psycopg2

# import the connect library for psycopg2
from psycopg2 import connect
# import the error handling libraries for psycopg2
from psycopg2 import OperationalError, errorcodes, errors

from psycopg2 import DatabaseError
from decouple import config

def get_connection():
    try:
                # Establecer la conexión
                connection = psycopg2.connect(
                host=config('PGSQL_HOST'),
                database=config('PGSQL_DATABASE'),
                user=config('PGSQL_USER'),
                password=config('PGSQL_PASSWORD'),
                port=config('PGSQL_PORT'))
                # Configurar la codificación del cliente a UTF8
                connection.set_client_encoding('UTF8')
        
                return connection
    except DatabaseError as ex:
        raise ex

from database.db import get_connection
from flask import jsonify
import numpy as np
import jsonpickle
import json



class StandardModel():

    @classmethod
    def standar_crud(self, store_procedure,params):
        #print(store_procedure)
        #print(params)
        try:
            #obtiene conexion con la base de datos
            connection = get_connection()
            #crear un cursor
            with connection.cursor() as cursor:
                #ejecutar el procedimiento almacenado
                cursor.callproc(store_procedure,params)
                #confirmar la transaccion
                connection.commit()
                # Si el procedimiento almacenado retorna valores, puedes obtenerlos
                row = cursor.fetchone() # o fetchall(), dependiendo de tu procedimiento
                #se evalua si existe respuesta para obtener el valor que se encuentra en la primera columna
                if row != None:
                    responsedb = row[0]
            # Cerrar la conexión
            connection.close()
            #retorna los datos obtenidos
            return responsedb
        except Exception as ex:
            raise Exception(ex)
            connection.rollback()
            connection.close()
        finally:
            if connection is not None:
                connection.close()

    @classmethod
    def standar_query(self, store_procedure,params):
        try:
            #obtiene conexion con la base de datos
            connection = get_connection()
            #crear un cursor
            with connection.cursor() as cursor:
                #ejecutar el procedimiento almacenado que retornara una consulta en formato json
                cursor.callproc(store_procedure,params)
                #confirmar la transaccion
                connection.commit()
                # Si el procedimiento almacenado retorna valores, puedes obtenerlos
                row = cursor.fetchone() # o fetchall(), dependiendo de tu procedimiento
                #se evalua si existe respuesta para obtener el valor que se encuentra en la primera columna
                if row != None:
                    responsequery = row[0]

            # Cerrar la conexión
            connection.close()
            #retorna los datos obtenidos
            return responsequery
        except Exception as ex:
            raise Exception(ex)
            connection.rollback()
            connection.close()
        finally:
            if connection is not None:
                connection.close()   
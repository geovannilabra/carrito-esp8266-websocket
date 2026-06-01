import mysql.connector
from mysql.connector import Error

class IoTModel:
    def __init__(self):
        self.config = {
            'user': 'admin',
            'password': 'Admin12345#!',
            'host': 'instancia-iot.ckrl886ovzzl.us-east-1.rds.amazonaws.com',
            'database': 'carrito_iot'
        }

    def _execute_sp(self, sp_name, params=None, fetch=False):
        try:
            conn = mysql.connector.connect(**self.config)
            cursor = conn.cursor(dictionary=True)
            if params:
                cursor.callproc(sp_name, params)
            else:
                cursor.callproc(sp_name)
            
            conn.commit()
            
            result = None
            if fetch:
                # Recuperar resultados de los result sets del SP
                for res in cursor.stored_results():
                    result = res.fetchone()
            
            cursor.close()
            conn.close()
            return result
        except Error as e:
            print(f"Error en BD: {e}")
            return None

    def obtener_ultimo_movimiento(self):
        return self._execute_sp('sp_obtener_ultimo_movimiento', fetch=True)

    def actualizar_parametro(self, clave, valor):
        return self._execute_sp('sp_actualizar_parametro', [clave, valor])

    def registrar_movimiento(self, id_mov, id_disp, origen):
        return self._execute_sp('sp_registrar_movimiento', [id_mov, id_disp, origen])
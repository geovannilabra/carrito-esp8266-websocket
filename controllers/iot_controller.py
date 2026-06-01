from models.database import IoTModel
from flask import jsonify

class IoTController:
    def __init__(self):
        self.model = IoTModel()

    def get_last_move(self):
        data = self.model.obtener_ultimo_movimiento()
        return data if data else {"error": "No hay movimientos"}

    def update_param(self, data):
        clave = data.get('clave')
        valor = data.get('valor')
        self.model.actualizar_parametro(clave, valor)
        return {"status": "success", "msg": f"Parámetro {clave} actualizado"}

    def post_move(self, data):
        id_mov = data.get('id_movimiento')
        id_disp = data.get('id_dispositivo')
        origen = data.get('origen', 'WEB')
        self.model.registrar_movimiento(id_mov, id_disp, origen)
        return {"status": "success", "msg": "Movimiento registrado"}
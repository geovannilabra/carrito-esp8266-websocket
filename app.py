from flask import Flask, request, jsonify
from flask_sock import Sock
from flask_cors import CORS
from controllers.iot_controller import IoTController
import json
import time

app = Flask(__name__)
CORS(app)

sock = Sock(app)
controller = IoTController()

# --- RUTAS REST API ---

@app.route('/full/movimiento', methods=['POST'])
def registrar():
    return jsonify(controller.post_move(request.json))

@app.route('/full/parametro', methods=['PUT'])
def actualizar():
    return jsonify(controller.update_param(request.json))

@app.route('/full/ultimo_movimiento', methods=['GET'])
def obtener_ultimo():
    return jsonify(controller.get_last_move())

# --- WEBSOCKET PARA TIEMPO REAL (ESP8266) ---

@sock.route('/ws/carrito')
def live_move(ws):
    """
    El ESP8266 se conecta aquí. 
    Enviará el último movimiento cada vez que cambie en la BD.
    """
    last_sent_time = None
    
    while True:
        data = controller.get_last_move()
        
        # Solo enviamos si el movimiento es nuevo (basado en fecha_hora)
        if data.get('fecha_hora') != last_sent_time:
            
            # Aseguramos que el ID sea un entero por si AWS lo regresa como string
            try:
                id_mov = int(data.get('id_movimiento'))
            except (TypeError, ValueError):
                id_mov = 0
            
            # --- LÓGICA DE CONTROL CONTINUO SOLICITADA ---
            # Si el movimiento es 1 (Adelante) o 2 (Atrás), forzamos 1 hora en milisegundos
            if id_mov in [1, 2]:
                data['MITime'] = 3600000 
                data['MDTime'] = 3600000
                print(f"--> [CONTROL API] Marcha constante para ID {id_mov}")
            # ------------------------------------------------------------
            
            ws.send(json.dumps(data, default=str))
            last_sent_time = data.get('fecha_hora')
        
        time.sleep(0.2) # Frecuencia de muestreo para el sensor/motor

if __name__ == '__main__':
    # Ejecución en puerto 5000 para cualquier IP
    app.run(host='0.0.0.0', port=5000, debug=True)
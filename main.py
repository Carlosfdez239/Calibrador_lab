import tkinter as tk
import json
from gui_config import NoriaGUI, crear_menu_superior
from motor_control import mover_a_angulo
from sensor_zero import esperar_cero
from log_config import configurar_logger
from excel_report import registrar_parada

modo_log = "debug"
logger = configurar_logger(modo_log)

def cambiar_modo_logger(nuevo_modo):
    global logger
    logger = configurar_logger(nuevo_modo)
    logger.info(f"Modo cambiado a: {nuevo_modo}")

root = tk.Tk()
crear_menu_superior(root, cambiar_modo_logger)
gui = NoriaGUI(root)
root.mainloop()

esperar_cero(logger)

with open("paradas.json") as f:
    paradas = json.load(f)

for parada in paradas:
    angulo = parada["angulo"]
    sentido = parada["sentido"]
    datos = mover_a_angulo(logger, angulo, sentido, microstepping=16)
    registrar_parada(datos)
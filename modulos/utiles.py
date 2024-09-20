# Importa modulo de fecha
from datetime import datetime

def pedir_fecha(mensaje):
    while True:
        fecha_str = input(mensaje)
        try:
            # Convertir la cadena de entrada en un objeto de fecha
            fecha = datetime.strptime(fecha_str, "%Y-%m-%d")
            if(fecha>=datetime.now()):
                return fecha
            else:
                print("La fecha debe ser superior al día de hoy.")
        except ValueError:
            print("Formato incorrecto. Usa el formato YYYY-MM-DD.")

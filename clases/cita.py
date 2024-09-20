from datetime import datetime

class Cita:
    def __init__(self, doctor, paciente, fecha):
        self.doctor = doctor
        self.paciente = paciente
        self.fecha = fecha

    def __str__(self):
        return f"Cita para {self.paciente.nombre} el {self.fecha.date()} con el Dr. {self.doctor.nombre}"

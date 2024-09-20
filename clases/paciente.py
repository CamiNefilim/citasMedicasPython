class Paciente:
    def __init__(self, run, nombre):
        self.run = run
        self.nombre = nombre

    def __str__(self):
        return f"Paciente: {self.nombre} - RUN: {self.run}"
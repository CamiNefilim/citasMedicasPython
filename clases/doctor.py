class Doctor:
    def __init__(self, run, nombre, valor):
        self.run = run
        self.nombre = nombre
        self.valor = valor
    
    def __str__(self):
        return f"Dr. {self.nombre} - RUN: {self.run} - Valor cita: ${self.valor}"
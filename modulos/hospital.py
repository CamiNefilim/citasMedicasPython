from clases import Cita, Doctor, Paciente
from datetime import datetime, timedelta

def agregar_doctor(hospital, doctor):
    hospital.doctores.append(doctor)

def agregar_paciente(hospital, paciente):
    hospital.pacientes.append(paciente)

def doctor_disponible(hospital, doctor, fecha):
    # Verificamos si el doctor tiene una reserva para la fecha entregada
    for cita in hospital.citas:
        if cita.doctor == doctor and cita.fecha == fecha:
            return False  # Si hay cita el doctor no está disponible
    return True  # Si no hay cita el doctor está disponible

def actualiza_doctores_disponibles(hospital, fecha):
    # Filtrar doctores disponibles
    hospital.doctores_disponibles = [doc for doc in hospital.doctores if doctor_disponible(hospital, doc, fecha)]
    
def obtener_doctor(run, hospital):
    for doctor in hospital.doctores_disponibles:
        if(doctor.run == run):
            return doctor
    return None

def obtener_paciente(run, hospital):
    for paciente in hospital.pacientes:
        if(paciente.run == run):
            return paciente
    return None

def obtener_cita(run, hospital):
    for cita in hospital.citas:
        if(cita.paciente.run == run):
            return cita
    return None

def agendar_cita(hospital, doctor, paciente, fecha):
    cita = Cita(doctor, paciente, fecha)
    hospital.citas.append(cita)
    return cita

def reagendar_cita(hospital, cita, doctor, paciente, fecha):
    hospital.citas.remove(cita)
    nueva_cita = Cita(doctor, paciente, fecha)
    hospital.citas.append(nueva_cita)
    return nueva_cita

def mostrar_comprobante(cita):
    print("\n--- Comprobante de Reserva Cita ---")
    print(f"Dr: {cita.doctor.nombre}")
    print(f"Paciente: {cita.paciente.nombre}")
    print(f"Fecha: {cita.fecha.strftime('%Y-%m-%d')}")
    print(f"Costo total: ${cita.doctor.valor}")
    print("--- Gracias por su preferencia ---\n")

def consultar_citas(hospital):    
    if(len(hospital.citas)>0):
        print("Citas agendadas:")
        for cita in hospital.citas:
            print(cita)
    else:
        print("No se encontraron citas registradas.")

def enviar_recordatorios(hospital):
    flag = True
    tres_dias = datetime.now() + timedelta(days=3)
    for cita in hospital.citas:
        if cita.fecha <= tres_dias:
            flag = False
            print(f"Recordatorio: {cita}")
    if flag:
        print("No se encontraron recordatorios.")

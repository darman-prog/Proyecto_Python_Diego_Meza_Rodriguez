# -*- coding: utf-8 -*-
import json
import faker

def guardar_datos_trainer(datos_trainer,ruta_archivo):
    with open(ruta_archivo,"a") as archivo:
        json.dump(datos_trainer,archivo)
        
        archivo.write('\n')
        
def ver_horarios():
    opcion_horario = input("Escoje diurno o nocturno").strip().lower()
    horario_Diurno = [
        {"artemis": "6 AM Hasta 2 PM"},
        {"Sputnik": "6 AM Hasta 2 PM"},
        {"Apolo": "6 AM Hasta 2 PM"}
    ]
    horario_Nocturno = [
        {"Artemis": "2 PM Hasta 10 PM"},
        {"Sputnik": "2 PM Hasta 10 PM"},
        {"Apolo": "2 PM Hasta 10 PM"}
    ]

    if opcion_horario == "diurno":
        print(horario_Diurno)
    elif opcion_horario == "nocturno":
        print(horario_Nocturno)


def cargar_documentos():
    try:
        with open("campers_Documentacion.json", "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return []

def generar_documentos():
    try:
        with open("campers_Documentacion.json", "r") as file:
            documento = json.load(file)
            if len(documento) >= 198:
                return documento[:198]
    except FileNotFoundError:
        pass
    
    documentos_iniciales = []
    for _ in range(30):
        nombre_de_camper = faker.name()
        cedula = faker.unique.ssn()
        numero_celular = faker.phone_number()
        acudiente = faker.name()
        estado = faker.random_element(elements=('En proceso de ingreso', 'Inscrito', 'Aprobado', 'Cursando', 'Graduado', 'Expulsado', 'Retirado'))
        riesgo = faker.random_element(elements=('Alto', 'Medio', 'Bajo'))
        direccion = faker.street_address()
        numero_fijo = faker.numerify('6#########')

        documento = {
            "Nombre Del aspirante": nombre_de_camper,
            "Riesgo Del camper": riesgo,
            "Direccion Del camper": direccion,
            "Cedula Del aspirante": cedula,
            "Numero De celular Del aspirante": numero_celular,
            "Numero fijo Del aspirante": numero_fijo,
            "Nombre Del acudiente": acudiente,
            "Estado Del camper": estado,
        }

        documentos_iniciales.append(documento)

    with open("campers_Documentacion.json", "w") as file:
        json.dump(documentos_iniciales, file)

    return documentos_iniciales

def guardar_camper_en_json(camper, archivo_json):
    try:
        with open(archivo_json, 'r+') as file:
            data = json.load(file)
            data["campers"].append(camper)
            file.seek(0)
            json.dump(data, file, indent=4)
    except FileNotFoundError:
        print("El archivo JSON no existe.")

def guardar_documentos(documentos):
    with open("campers_Documentacion.json", "w") as file:
        json.dump(documentos, file, indent=4)


def guardar_documentos(documentos):
    with open("campers_Documentacion.json", "w") as file:
        json.dump(documentos, file, indent=4)

def ordenar_documentos_por_nombre(documentos):
    return sorted(documentos, key=lambda camper: camper.get("Nombre Completo", ""))

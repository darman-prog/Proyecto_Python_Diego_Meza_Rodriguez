import json
from faker import Faker
import os

# Función para guardar datos del trainer
def guardar_datos_trainer(datos_trainer):
    try:
        with open("trainers.json", "a") as archivo:
            archivo.write(','.join(map(str, datos_trainer)) + '\n')
    except FileNotFoundError:
        print("No se encontró el archivo 'trainers.json'.")

# Función para cargar documentos (campers)
def cargar_documentos():
    try:
        with open("campers_Documentacion.json", "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return []

# Función para guardar documentos (campers)
def guardar_documentos(documentos):
    with open("campers_Documentacion.json", "w") as file:
        json.dump(documentos, file, indent=4)

# Función para guardar datos de la coordinadora
def guardar_datos_coordinadora(datos_coordinadora):
    try:
        with open("trainers.json", "r") as archivo:
            trainers_existente = json.load(archivo)
    except FileNotFoundError:
        trainers_existente = []

    trainers_existente.append(datos_coordinadora)

    try:
        with open("trainers.json", "w") as archivo:
            json.dump(trainers_existente, archivo, indent=2)
        print("Los datos de la coordinadora han sido guardados exitosamente ")
    except FileNotFoundError:
        print("No se encontró el archivo 'trainers.json'.")

# Función para generar documentos (campers)
def generar_documentos():
    faker = Faker("es_CO")
    try:
        with open("campers_Documentacion.json", "r") as file:
            documento = json.load(file)
            if len(documento) >= 198:
                return documento[:198]
    except FileNotFoundError:
        pass
    
    documentos_iniciales = []
    for _ in range(50):
        nombre_de_camper = faker.name()
        cedula = faker.unique.ssn()
        numero_celular = faker.phone_number()
        acudiente = faker.name()
        estado = faker.random_element(elements=('En proceso de ingreso', 'Aprobado', 'Cursando', 'Graduado', 'Expulsado', 'Retirado'))
        riesgo = faker.random_element(elements=('Alto', 'Medio', 'Bajo'))
        direccion = faker.street_address()
        numero_fijo = faker.numerify('6#########')

        documento = {
            "Nombre Del Camper": nombre_de_camper,
            "Riesgo Del Camper": riesgo,
            "Direccion Del Camper": direccion,
            "Cedula Del Camper": cedula,
            "Numero De celular Del Camper": numero_celular,
            "Numero fijo Del aspirante": numero_fijo,
            "Nombre Del acudiente del camper": acudiente,
            "Estado Del camper": estado,
            "Ruta":""
        }

        if estado in ["Aprobado", "Cursando"]:
            documento["Ruta"] = faker.random_element(elements=("Ruta NodeJS", "Ruta Java", "Ruta NetCore"))

        documentos_iniciales.append(documento)

    with open("campers_Documentacion.json", "w") as file:
        json.dump(documentos_iniciales, file)

    return documentos_iniciales

# Función para generar trainers de Campusland
def generar_trainers_campusland():
    faker = Faker("es_CO")
    if os.path.isfile("trainers.json"):
        print("El archivo JSON ya existe. No se creará uno nuevo.")
        return None
    
    numero_trainers = 6
    trainers = []
    for _ in range(numero_trainers):
        trainer = {
            "Nombre": faker.name(),
            "Documento": faker.unique.random_number(digits=10),
            "Numero Telefono": faker.phone_number(),
            "Ruta": faker.random_element(elements=("Ruta NodeJS", "Ruta Java", "Ruta NetCore")),
            "Salon Asignado": faker.random_element(elements=("Sputnik", "Apolo", "Artemis"))
        }
        trainers.append(trainer)

    with open("trainers.json", "w") as file:
        json.dump(trainers, file,)
    
    return trainers

# Definición de las rutas de entrenamiento
rutas_entrenamiento = {
    "Ruta NodeJS": {
        "Modulos": ["NodeJS", "Express", "MongoDB"],
        "SGDB_principal": "MongoDB",
        "SGDB_alternativo": "MySQL"
    },
    "Ruta Java": {
        "Modulos": ["Java", "Spring Boot", "Hibernate"],
        "SGDB_principal": "MySQL",
        "SGDB_alternativo": "PostgreSQL"
    },
    "Ruta NetCore": {
        "Modulos": ["NetCore", "Entity Framework", "SQL Server"],
        "SGDB_principal": "SQL Server",
        "SGDB_alternativo": "PostgreSQL"
    },
    "Fundamentos de programación": {
        "Modulos": ["Introducción a la algoritmia", "PSeInt", "Python"],
        "SGDB_principal": "Ninguno",
        "SGDB_alternativo": "Ninguno"
    },
    "Programación Web": {
        "Modulos": ["HTML", "CSS", "Bootstrap"],
        "SGDB_principal": "Ninguno",
        "SGDB_alternativo": "Ninguno"
    },
    "Programación formal": {
        "Modulos": ["Java", "JavaScript", "C#"],
        "SGDB_principal": "Ninguno",
        "SGDB_alternativo": "Ninguno"
    },
    "Bases de datos": {
        "Modulos": ["MySQL", "MongoDB", "PostgreSQL"],
        "SGDB_principal": "Ninguno",
        "SGDB_alternativo": "Ninguno"
    },
    "Backend": {
        "Modulos": ["NetCore", "Spring Boot", "NodeJS y Express"],
        "SGDB_principal": "Ninguno",
        "SGDB_alternativo": "Ninguno"
    }
}


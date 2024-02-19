import json
#ver campers general
def ver_documentos():
    try:
        with open("campers_Documentacion.json", "r") as file:
            documentos = json.load(file)
            for documento in documentos:
                print(documento)
    except FileNotFoundError:
        print("No se encontraron documentos.")


#reportes de campers en riesgo y estados generales
def listar_camper_por_estado(estado):
    try:
        with open("campers_Documentacion.json", "r") as file:
            documentos = json.load(file)
            campers_filtrados = [camper for camper in documentos if "Estado Del camper" in camper and camper["Estado Del camper"] == estado]
            for camper in campers_filtrados:
                print(camper)
    except FileNotFoundError:
        print("No se encontraron documentos.")


def listar_camper_por_riesgo(riesgo):
    try:
        with open("campers_Documentacion.json", "r") as file:
            documentos = json.load(file)
            campers_filtrados = [camper for camper in documentos if "Riesgo Del Camper" in camper and camper["Riesgo Del Camper"] == riesgo]
            for camper in campers_filtrados:
                print(camper)
    except FileNotFoundError:
        print("No se encontraron documentos.")
#fin 

def imprimir_trainers():
    try:
        with open("trainers.json", "r") as file:
            trainers = json.load(file)
            if trainers:
                print("Datos de los Trainers:")
                for index, trainer in enumerate(trainers, 1):
                    print(f"Trainer {index}:")
                    print(f"Nombre: {trainer['Nombre']}")
                    print(f"Documento: {trainer['Documento']}")
                    print(f"Número de Teléfono: {trainer['Numero Telefono']}")
                    print(f"Ruta: {trainer['Ruta']}")  # Muestra la ruta seleccionada para el entrenador
                    print(f"Salón Asignado: {trainer['Salon Asignado']}")
                    print()
            else:
                print("No se encontraron trainers en el archivo JSON.")
    except FileNotFoundError:
        print("El archivo 'trainers.json' no existe.")

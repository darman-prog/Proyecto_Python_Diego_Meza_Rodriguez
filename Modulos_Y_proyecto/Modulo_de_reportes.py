import os
import json
from utils import generar_documentos
from utils import cargar_documentos
from utils import guardar_documentos
from utils import ordenar_documentos_por_nombre


def campers_incristos_lista():
    
    if os.path.exists("Campers_Documentacion.json"):
        listado_de_documentos = cargar_documentos()
    else:
        listado_de_documentos = generar_documentos()
        guardar_documentos(listado_de_documentos)
        campers_inscritos_ordenados = ordenar_documentos_por_nombre(listado_de_documentos)
        for camper in campers_inscritos_ordenados:
          print(camper)

def listar_trainers():
    try:
        with open("datos_trainers.json","r") as file :
            trainers = json.load(file)

            for trainer in trainers:
                 print("Nombre:", trainer["nombre"])
                 print("Teléfono:", trainer["telefono"])
                 print("Documento:", trainer["documento"])
                 print("Conocimientos:", trainer["conocimientos"])
                 print()  
    except FileNotFoundError:
        print("Archivo json No existe")



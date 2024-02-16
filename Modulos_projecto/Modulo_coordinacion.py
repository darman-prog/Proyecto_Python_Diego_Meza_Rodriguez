import os
from utils import guardar_camper_en_json
from utils import generar_documentos
from utils import guardar_documentos
from utils import cargar_documentos
from utils import ordenar_documentos_por_nombre
from Proyecto_Python import listado_de_campers



def agregar_camper():
    camper = {}

    print("Ingresa los Datos del Camper que Deseas Agregar")

    while True:
        nombre_completo = input("Ingresa el Nombre completo del Camper: ").strip()
        if nombre_completo:
            camper["Nombre Completo"] = nombre_completo
            break
        else:
            print("El nombre no puede estar vacío. Por favor, ingrésalo nuevamente.")

    while True:
        try:
            documento = int(input("Ingresa número de documento: "))
            camper["Documento"] = documento
            break
        except ValueError:
            print("Ingresa un Documento válido (número entero)")

    direccion = input("Ingresa la dirección del Camper: ").strip()
    if direccion:
        camper["Dirección"] = direccion
    else:
        print("La dirección no puede estar vacía. Por favor, ingrésala nuevamente.")

    acudiente = input("Ingresa el nombre del acudiente: ").strip()
    if acudiente:
        camper["Acudiente"] = acudiente
    else:
        print("El nombre del acudiente no puede estar vacío. Por favor, ingrésalo nuevamente.")

    while True:
        try:
            telefono_celular = int(input("Ingresa el número de celular del Camper: "))
            camper["Teléfono Celular"] = telefono_celular
            break
        except ValueError:
            print("Ingresa número de teléfono válido (número entero)")

    while True:
        try:
            telefono_fijo = int(input("Ahora Ingresa el Número Fijo del Camper: "))
            camper["Teléfono Fijo"] = telefono_fijo
            break
        except ValueError:
            print("Ingresa número de teléfono válido (número entero)")

    estado = input("Ingresa estado en la que se encuentra el camper: ")
    camper["Estado"] = estado

    riesgo = input("Ingresa el riesgo del camper: ")
    camper["Riesgo"] = riesgo

    print("Camper Agregado Exitosamente")

    guardar_camper_en_json(camper, "campers_Documentacion.json")  # Guardar el camper en el archivo JSON

    return camper


archivo_json_existente = "campers_Documentacion.json"

def campers_incristos_lista():
    
    if os.path.exists("Campers_Documentacion.json"):
        listado_de_documentos = cargar_documentos()
    else:
        listado_de_documentos = generar_documentos()
        guardar_documentos(listado_de_documentos)
        campers_inscritos_ordenados = ordenar_documentos_por_nombre(listado_de_documentos)
        for camper in campers_inscritos_ordenados:
          print(camper)

def eliminar_camper(nombre_completo, listado_de_campers):
    for camper in listado_de_campers:
        if camper["Nombre Completo"].lower() == nombre_completo.lower():
            listado_de_campers.remove(camper)
            print(f"El camper {nombre_completo} ha sido eliminado.")
            guardar_documentos(listado_de_campers)  
            return True
    print(f"No se encontró ningún camper con el nombre {nombre_completo}.")
    return False       


def Coordinadora_Registro_Notas():
    nombre_completo = input("Ingresa nombre del camper que deseas buscar").lower()
    for camper in listado_de_campers:
        if camper["Nombre Completo"].lower() == nombre_completo:
            nota_teorica = float(input("Ingresa Nota Teorica: "))
            nota_practica = float(input("Ingresa Nota Practica: "))
            
            promedio = (nota_teorica + nota_practica) / 2
            if promedio >= 60:
                print("El camper está aprobado con un promedio de", promedio)
                camper["Estado"] = "Aprobado"
            else:
                print("El camper no está aprobado con un promedio de", promedio)

            break
    else:
        print("Camper no encontrado")


def Coordinadora_Registro_Notas():
    nombre_completo = input("Ingresa nombre del camper que deseas buscar").lower()
    for camper in listado_de_campers:
        if camper["Nombre Completo"].lower() == nombre_completo:
            nota_teorica = float(input("Ingresa Nota Teorica: "))
            nota_practica = float(input("Ingresa Nota Practica: "))
            
            promedio = (nota_teorica + nota_practica) / 2
            if promedio >= 60:
                print("El camper está aprobado con un promedio de", promedio)
                camper["Estado"] = "Aprobado"
            else:
                print("El camper no está aprobado con un promedio de", promedio)

            break
    else:
        print("Camper no encontrado")

def campers_incristos_lista():
    
    if os.path.exists("Campers_Documentacion.json"):
        listado_de_documentos = cargar_documentos()
    else:
        listado_de_documentos = generar_documentos()
        guardar_documentos(listado_de_documentos)
        campers_inscritos_ordenados = ordenar_documentos_por_nombre(listado_de_documentos)
        for camper in campers_inscritos_ordenados:
          print(camper)

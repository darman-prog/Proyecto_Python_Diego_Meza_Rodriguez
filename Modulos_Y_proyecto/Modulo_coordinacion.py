import json
from faker import Faker
from utils import cargar_documentos, guardar_documentos, guardar_datos_coordinadora, rutas_entrenamiento

# Registro de notas de coordinadora
def evaluar_campers():
    campers = cargar_documentos() #cargamos el documento json con los campers
    
    print("Lista de Campers Inscritos:")
    for i, camper in enumerate(campers, 1): #enumeramos los campers inscritos
        print(f"{i}. {camper['Nombre Del Camper']}")

    for camper in campers:
        if camper["Estado Del camper"] == "Inscrito": #creamos una condicion que si el camper se encuentra inscrito no le asignara una ruta
            ruta = None
            while ruta not in ["NodeJS", "Java", "NetCore"]:
                ruta = input(f"Seleccione la ruta de entrenamiento para {camper['Nombre Del Camper']} (NodeJS, Java, NetCore): ") # asignamos o modificamos una ruta al camper elegido
                if ruta == "NodeJS":
                    ruta = rutas_entrenamiento["Ruta NodeJS"]
                elif ruta == "Java":
                    ruta = rutas_entrenamiento["Ruta Java"]
                elif ruta == "NetCore":
                    ruta = rutas_entrenamiento["Ruta NetCore"]
                else:
                    print("Ruta no válida. Intente de nuevo.")

            camper["Ruta de Entrenamiento"] = ruta

            nota_teorica = float(input(f"Ingrese la nota teórica para el camper {camper['Nombre Del Camper']}: "))
            nota_practica = float(input(f"Ingrese la nota práctica para el camper {camper['Nombre Del Camper']}: "))
            proyectos = float(input(f"Ingrese la nota de los proyectos para el camper {camper['Nombre Del Camper']}: "))
            tareas = float(input(f"Ingrese la nota de las tareas para el camper {camper['Nombre Del Camper']}: "))
            
            promedio = (nota_teorica + nota_practica + proyectos + tareas) / 4
            if promedio >= 60:
                camper["Estado Del camper"] = "Aprobado"
                camper["Riesgo Del Camper"] = "Medio"
            else:
                camper["Estado Del camper"] = "Rendimiento bajo"
                camper["Riesgo Del Camper"] = "Medio"

            guardar_documentos(campers)

# Registro de notas de coordinadora
def Coordinadora_Registro_Notas():
    documentos = cargar_documentos()
    
    print("Lista de Campers:")
    for i, camper in enumerate(documentos, 1):
        print(f"{i}. {camper['Nombre Del Camper']}")

    while True:
        try:
            opcion = int(input("Ingresa el número del camper que deseas buscar (0 para cancelar): "))
            if opcion == 0:
                print("Operación cancelada.")
                return
            elif 1 <= opcion <= len(documentos):
                camper = documentos[opcion - 1]
                nota_teorica = float(input(f"Ingrese la nota teórica para el camper {camper['Nombre Del Camper']}: "))
                nota_practica = float(input(f"Ingrese la nota práctica para el camper {camper['Nombre Del Camper']}: "))
                proyectos = float(input(f"Ingrese la nota de los proyectos para el camper {camper['Nombre Del Camper']}: "))
                tareas = float(input(f"Ingrese la nota de las tareas para el camper {camper['Nombre Del Camper']}: "))
                promedio = (nota_teorica + nota_practica + proyectos + tareas) / 4
                if promedio >= 60:
                    print(f"El camper {camper['Nombre Del Camper']} pasó con éxito el módulo con un promedio de {promedio}")
                    camper["Riesgo Del Camper"] = "Paso con éxito"
                else:
                    print(f"El camper {camper['Nombre Del Camper']} no pasó el módulo con un promedio de {promedio}")
                    camper["Riesgo Del Camper"] = "Alto"

                guardar_documentos(documentos)  
                break
            else:
                print("Número de camper inválido. Por favor, ingresa un número válido.")
        except ValueError:
            print("Ingresa un número entero.")

# Agregar y eliminar camper            
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

    documentos = cargar_documentos()  # Cargar los documentos existentes
    documentos.append(camper)  # Agregar el nuevo camper
    guardar_documentos(documentos)  # Guardar los documentos actualizados

    return camper

def eliminar_camper():
    try:
        with open("campers_Documentacion.json", "r") as file:
            documentos = json.load(file)
    except FileNotFoundError:
        print("No se encontró el archivo de documentos.")
        return

    if not documentos:
        print("No hay campers para eliminar.")
        return

    print("Lista de Campers:")
    for i, camper in enumerate(documentos, 1):
        print(f"{i}. {camper.get('Nombre Del Camper', 'Nombre no disponible')}")

    while True:
        try:
            opcion = int(input("Ingresa el número del camper que deseas eliminar (0 para cancelar): "))
            if opcion == 0:
                print("Operación cancelada.")
                return
            elif 1 <= opcion <= len(documentos):
                del documentos[opcion - 1]
                with open("campers_Documentacion.json", "w") as file:
                    json.dump(documentos, file, indent=4)
                print("Camper eliminado correctamente.")
                return
            else:
                print("Número de camper inválido. Por favor, ingresa un número válido.")
        except ValueError:
            print("Ingresa un número entero.")

# Coordinadora ingresar trainer
def registro_coordinadora():
    datos_coordinadora = {}
    print("Bienvenida al Registro de Trainer por parte de la Coordinadora")
    print("Por favor, ingresa los datos del nuevo Trainer")
    
    while True:
        nombre = input("Ingresa el nombre completo del nuevo Trainer: ")
        if nombre:
            datos_coordinadora["Nombre"] = nombre
            break
        else:
            print("El nombre no puede estar vacío. Por favor, ingrésalo nuevamente.")
        
    while True:
        try:
            numero_telefonico = int(input("Ingresa el número telefónico del nuevo Trainer: "))
            datos_coordinadora["Documento"] = numero_telefonico
            break
        except ValueError:
            print("Ingresa un número de teléfono válido.")
    
    while True:
        try:
            documento = int(input("Ingresa el número de documento del nuevo Trainer: "))
            datos_coordinadora["Numero Telefono"] = documento
            break
        except ValueError:
            print("Ingresa un número de documento válido.")
    
    while True:
        ruta = input("Ingresa la ruta asignada para el nuevo Trainer: ")
        if ruta:
            datos_coordinadora["Ruta"] = ruta
            break
        else:
            print("La ruta no puede estar vacía. Por favor, ingrésala nuevamente.")

    while True:
        salon_asignado = input("Ingresa el salón asignado para el nuevo Trainer: ")
        if salon_asignado:
            datos_coordinadora["Salon Asignado"] = salon_asignado
            break
        else:
            print("El salón no puede estar vacío. Por favor, ingrésalo nuevamente.")

    guardar_datos_coordinadora(datos_coordinadora)

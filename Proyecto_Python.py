# -*- coding: utf-8 -*-
from faker import Faker
import json
import os
from Modulo_menus import menu_trainer
from Modulo_menus import menu_rol
from Modulo_trainer import registro_trainer
from Modulo_coordinacion import agregar_camper
from utils import cargar_documentos
from Modulo_coordinacion import listar_trainers
from Modulo_coordinacion import listado_de_campers

# def ver_horarios():
#     opcion_horario = input("Escoje diurno o nocturno").strip().lower()
#     horario_Diurno = [
#         {"artemis": "6 AM Hasta 2 PM"},
#         {"Sputnik": "6 AM Hasta 2 PM"},
#         {"Apolo": "6 AM Hasta 2 PM"}
#     ]
#     horario_Nocturno = [
#         {"Artemis": "2 PM Hasta 10 PM"},
#         {"Sputnik": "2 PM Hasta 10 PM"},
#         {"Apolo": "2 PM Hasta 10 PM"}
#     ]

#     if opcion_horario == "diurno":
#         print(horario_Diurno)
#     elif opcion_horario == "nocturno":
#         print(horario_Nocturno)

"""listado_de_campers = []"""
"""def agregar_camper():
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
"""

"""def guardar_camper_en_json(camper, archivo_json):
    try:
        with open(archivo_json, 'r+') as file:
            data = json.load(file)
            data["campers"].append(camper)
            file.seek(0)
            json.dump(data, file, indent=4)
    except FileNotFoundError:
        print("El archivo JSON no existe.")

archivo_json_existente = "campers_Documentacion.json"
"""

faker = Faker('es_CO')

def listar_camper_por_estado(lista_camper, estado):
    """Filtra y devuelve una lista de campers que tienen el estado especificado."""
    campers_filtrados = []
    for camper in lista_camper:
        if camper['Estado Del camper'] == estado:
            campers_filtrados.append(camper)
    return campers_filtrados

def crear_trainers_por_defecto():
    trainers_por_defecto = [
        {"nombre": "William Jose restrepo garcia", "telefono": "123456789", "documento": "123456789A", "conocimientos": "Backend"},
        {"nombre": "Jose maurcio zaragosa ardila", "telefono": "987654321", "documento": "987654321B", "conocimientos": "JavaScript y Python"},
        {"nombre": "edwin romario lopez rodriguez", "telefono": "111222333", "documento": "111222333C", "conocimientos": "Java y MongDB"},
        {"nombre": "diana alejandra muñoz hernandez", "telefono": "444555666", "documento": "444555666", "conocimientos": "C++ y MySQL"},
        {"nombre": "Roberto jose Silva ", "telefono": "777888999", "documento": "777888999E", "conocimientos": "FrontEnd"},
        {"nombre": "Trainer6", "telefono": "000111222", "documento": "000111222F", "conocimientos": "CSS y HTML"}
    ]

    ruta_archivo = os.path.join("Archivos json","trainers.json")

    with open("trainers.json", "w") as file:
        json.dump(trainers_por_defecto, file, indent=4)
"""
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
"""

def generar_documentos():
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

def cargar_documentos():
    try:
        with open("campers_Documentacion.json", "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return []


def guardar_documentos(documentos):
    with open("campers_Documentacion.json", "w") as file:
        json.dump(documentos, file, indent=4)


def guardar_documentos(documentos):
    with open("campers_Documentacion.json", "w") as file:
        json.dump(documentos, file, indent=4)



Areas_de_entrenamiento = {
    "Ruta NodeJS": {
        
        "Modulos": ["NodeJS", "Express", "MongoDB"]
    },
    "Ruta Java": {
       
        "Modulos": ["Java", "Spring Boot", "Hibernate"]
    },
    "Ruta Netcore": {
    
        "Modulos": ["NetCore", "Entity Framework", "SQL Server"]
    },
    "Fundamentos de programación": {
        
        "Modulos": ["Introducción a la algoritmia", "PSeInt", "Python"]
    },
    "Programación Web": {
        "Modulos": ["HTML", "CSS", "Bootstrap"]
    },
    "Programación formal": {
        "Modulos": ["Java", "JavaScript", "C#"]
    },
    "Bases de datos": {
        "Modulos": ["MySQL", "MongoDB", "PostgreSQL"]
    },
    "Backend": {
        "duracion_meses":2,
        "Modulos": ["NetCore", "Spring Boot", "NodeJS y Express"]
    }
}


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

def eliminar_camper(nombre_completo, listado_de_campers):
    for camper in listado_de_campers:
        if camper["Nombre Completo"].lower() == nombre_completo.lower():
            listado_de_campers.remove(camper)
            print(f"El camper {nombre_completo} ha sido eliminado.")
            guardar_documentos(listado_de_campers)  
            return True
    print(f"No se encontró ningún camper con el nombre {nombre_completo}.")
    return False



def evaluar_campers():
    for camper in listado_de_campers:
        for modulo in camper["Modulos"]:
            
            nota_final = (modulo["Nota_teorica"] * 0.3) + (modulo["Nota_practica"] * 0.6) + (modulo["Trabajos"] * 0.1)
            
           
            if nota_final >= 60:
                modulo["Estado"] = "Aprobado"
            else:
                modulo["Estado"] = "Rendimiento bajo"
                
               
                
            modulo["Nota_final"] = nota_final

        
        rendimientos = [modulo["Estado"] for modulo in camper["Modulos"]]
        if "Rendimiento bajo" in rendimientos:
            camper["Estado"] = "Rendimiento bajo"
        else:
            camper["Estado"] = "Aprobado"

      
        index = listado_de_campers.index(camper)
        listado_de_campers[index] = camper

def menu_rol():
    while True:
        print("                                               ")
        print("                                               ")
        print("-------- Escoje un Rol Para ingresar ----------")
        print("          1. Coordinador                       ")  
        print("          2. Trainer                           ")
        print("          3. Camper                            ")
        print("          4. Salir                             ")
        print("_______________________________________________")      
     
        while True:
            try:
                opcion_de_rol = int(input("Escoje un número designado para cada rol para ingresar: "))
                break
            except ValueError:
                print("Ingresa otra vez.")
                
        if opcion_de_rol == 1:
            print("Escribe la Contraseña para Entrar a Rol de Coordinacion")
            while True:
                try:
                    contraseña = int(input("Ingresa la contraseña: "))
                    if contraseña == 1234:
                        print("Bienvenido Coordinador/a")
                        menu_coordinadora()
                        break
                    else:
                        print("Contraseña incorrecta. Intenta nuevamente.")
                except ValueError:
                    print("Ingresa un valor numérico para la contraseña.")
                    
        elif opcion_de_rol == 2:
            print("Escribe la Contraseña para Entrar a Rol de Trainer")
            while True:
                try:
                    contraseña_trainer = int(input("Ingresa la contraseña "))
                    if contraseña_trainer == 5678:
                        print("Bienvenido Trainer ")
                        menu_trainer()
                        break
                    else:
                        print("Contraseña incorrecta. Intenta nuevamente.")
                except ValueError:
                    print("Ingresa un Valor Numèrico para Entrar a Rol de Trainer")         
        elif opcion_de_rol == 3:
            print("Bienvenido Camper")
            menu_Camper()
            break
        elif opcion_de_rol == 4:
            print("Saliendo Del Programa...")
            return  
        else:
            print("Ingresa Opcion valida")

def menu_Camper():
    while True:
        print("________Bienvenido Camper_________")
        print("        1.Registro De Camper      ")
        print("        2.Salir                         ")
        opcion_camper = int(input("Ingresa el numero asignado para cada Opcion Para ingresar"))
        if opcion_camper == 1:
             Registro_de_camper()
             break
        elif opcion_camper == 2:
            menu_rol()
            break
# def menu_trainer():
#     while True:
#         print("_____________Bienvenido Trainer______________")
#         print("             1.Registro De Trainer           ")
#         print("             2.Horarios                    ") 
#         print("             3.salir                               ")
#         opcion_trainer = int(input("ingresa el numero desigando para ingresar a una Opcion"))
#         if opcion_trainer == 1:
#             registro_trainer()
#         elif opcion_trainer ==2:
#               ver_horarios()
#         elif opcion_trainer ==3:
#             break

# def guardar_datos_trainer(datos_trainer,ruta_archivo):
#     with open(ruta_archivo,"a") as archivo:
#         json.dump(datos_trainer,archivo)
        
#         archivo.write('\n')

# def registro_trainer():
#     datos_trainer = []
#     print("Bienvenido a Registro de Trainer")
#     print(" Ingresa Tus Datos Para Registrarte En el sistema y Asignarte una Clase ")
#     while True:
#        try: 
#          nombre = input(" Ingresa tu nombre Completo ")
#          break
#        except ValueError:
#            print("Ingresa Nombre Valido")  
        
#     datos_trainer.append(nombre)
    
#     while True:
#        try:
#           numero_de_trainer = int(input("Ingresa tu Numero Telefonico"))
#           break       
#        except ValueError:
#            print ("Ingresa Numero valido")
#     datos_trainer.append(numero_de_trainer)
    
#     while True:
#        try:
#            documento_trainer=int(input("Ingresa Tu numero de Documento"))
#            break       
#        except ValueError:
#            print ("Ingresa Numero valido")
#     datos_trainer.append(documento_trainer)
#     while True:
#        try:
#             Conocimientos_trainer = input("Que Conocimientos Tienes En Programacion ")
#             break
#        except ValueError:
#             print("Ingresa Otra vez")       
#     datos_trainer.append(Conocimientos_trainer)
#     ruta_archivo = "datos_trainer.json"  
    
#     guardar_datos_trainer(datos_trainer, ruta_archivo)


def Registro_de_camper():
    Registro_manual_de_camper = []

    while True:
        nombre_completo = input("Ingresa tu Nombre Completo: ")
        Registro_manual_de_camper.append(nombre_completo)

        if nombre_completo:
            break
        else:
            print("El nombre no puede estar vacío. Por favor, ingrésalo nuevamente.")

    while True:
        try:
            Documento_de_camper = int(input("Ingresa número de documento: "))
            Registro_manual_de_camper.append(Documento_de_camper)
            break
        except ValueError:
            print("Ingresa un Documento válido (número entero)")

    direcion = input("Ingresa tu dirección: ")
    Registro_manual_de_camper.append(direcion)

    if not direcion:
        print("La dirección no puede estar vacía. Por favor, ingrésala nuevamente.")

    acudiente = input("Ingresa el nombre de tu acudiente: ")
    Registro_manual_de_camper.append(acudiente)

    if not acudiente:
        print("El nombre del acudiente no puede estar vacío. Por favor, ingrésalo nuevamente.")

    while True:
        try:
            telefono_de_contacto = int(input("Ingresa tu número celular: "))
            Registro_manual_de_camper.append(telefono_de_contacto)
            break
        except ValueError:
            print("Ingresa número de teléfono válido (número entero)")

    while True:
        try:
            telefono_de_fijo = int(input("Ahora Ingresa tu número fijo: "))
            Registro_manual_de_camper.append(telefono_de_fijo)
            break
        except ValueError:
            print("Ingresa número de teléfono válido (número entero)")

    print("Elige el estado en el que te encuentras:")
    print("1. En proceso de ingreso")
    print("2. Inscrito")
    print("3. Aprobado")
    print("4. Cursando")
    print("5. Graduado")
    print("6. Expulsado")
    print("7. Retirado")

    while True:
        opcion_estado = input("Selecciona una opción: ")

        if opcion_estado == "1":
            estado = "En proceso de ingreso"
            break
        elif opcion_estado == "2":
            estado = "Inscrito"
            break
        elif opcion_estado == "3":
            estado = "Aprobado"
            break
        elif opcion_estado == "4":
            estado = "Cursando"
            break
        elif opcion_estado == "5":
            estado = "Graduado"
            break
        elif opcion_estado == "6":
            estado = "Expulsado"
            break
        elif opcion_estado == "7":
            estado = "Retirado"
            break
        else:
            print("Opción inválida. Por favor, selecciona una opción válida.")

    Registro_manual_de_camper.append(estado)

    riesgo = input("Ingresa el riesgo del camper: ")
    Registro_manual_de_camper.append(riesgo)
    
    print("Registro Terminado. Próximamente te Contactaremos.")
    return Registro_manual_de_camper

def guardar_documentos(documentos):
    with open("campers_Documentacion.json", "w") as file:
        json.dump(documentos, file, indent=4)

def asignar_camper_a_ruta(camper, ruta, listado_de_rutas):
    if len(ruta["campers"]) < 33:  
        ruta["campers"].append(camper)
        print(f"Camper {camper['Nombre Completo']} asignado a la ruta {ruta['nombre']}.")
    else:
        print(f"No se puede asignar al camper {camper['Nombre Completo']} a la ruta {ruta['nombre']} porque está completa.")

   
    index = listado_de_rutas.index(ruta)
    listado_de_rutas[index] = ruta




def listar_camper_y_trainer_por_ruta(listado_de_rutas, nombre_ruta):
    for ruta in listado_de_rutas:
        if ruta["nombre"] == nombre_ruta:
            print(f"Campers en la ruta {nombre_ruta}:")
            for camper in ruta["campers"]:
                print(camper["Nombre Completo"])

            print(f"Trainer de la ruta {nombre_ruta}: {ruta['trainer']}")
            break
    else:
        print(f"No se encontró la ruta {nombre_ruta}.")



def listar_camper_por_riesgo(listado_de_camper, riesgo):
    campers_por_riesgo = [camper for camper in listado_de_camper if camper["Riesgo"] == riesgo]
    return campers_por_riesgo


def campers_incristos_lista():
    
    if os.path.exists("Campers_Documentacion.json"):
        listado_de_documentos = cargar_documentos()
    else:
        listado_de_documentos = generar_documentos()
        guardar_documentos(listado_de_documentos)
        campers_inscritos_ordenados = ordenar_documentos_por_nombre(listado_de_documentos)
        for camper in campers_inscritos_ordenados:
          print(camper)
       
def ordenar_documentos_por_nombre(documentos):
    return sorted(documentos, key=lambda camper: camper.get("Nombre Completo", ""))


def menu_coordinadora():
    while True:
        print("___________Campusland_________________  ")
   
        print("____________ (Menu) ____________________")
        
        print("     Coordinacion Academica             ") 
         
        print("1. Campers inscritos/Agregar Camper/eliminar registro de camper                    ")
        print("2. Registro de Notas de Campers                                                    ")
        print("3. Lista de trainers/Registro de Trainer                                           ")
        print("4. Estados de Campers/                                                             ")
        print("5. Salir Del Programa                                                              ")

        print("____________________________________________                                       ")

        while True:
            try:
                opcion = int(input("Selecciona un número designado para cada opción para ingresar: "))
                break
            except ValueError:
                print("Ingresa un numero del 1 al5 ")

        if opcion == 1:
            print("Ingresaste a Campers Inscritos/Agregar Camper ")
            while True:
                
                print("1. agregar Camper ")
                print("2. Ver Campers Inscritos")
                print("3. Eliminar Registro De camper")
                print("4. para volver Al menu Principal")

                try:
                    opcion1 = int(input("Que Opcion eliges: "))
                except ValueError:
                    print("Ingresa Una Opcion valida")

                if opcion1 == 1:
                    agregar_camper() 
                    break
                elif opcion1 == 2:  
                    campers_incristos_lista()
                    break
                elif opcion1 == 3:
                    nombre_completo = input("Ingresa el nombre completo del camper que deseas eliminar: ")
                    eliminar_camper(nombre_completo,listado_de_campers)
                    break
                elif opcion1 == 4:
                    break
                else:
                    print("Ingresa Opcion valida")
        elif opcion == 2:
                Coordinadora_Registro_Notas()
                break 
        elif opcion == 3:
            print("Ingresaste Trainers Activos")
            while True:
                print("1. Listado De trainers ")
                print("2. Registrar Trainer   ")
                print("3. salir del programa  ")
                try:
                  opcion3 = int(input("Escoje una Opcion del 1 al 3"))
                  break
                except ValueError:
                    print("Error Ingresa Un numero entero")
                if opcion3 == 1:
                    listar_trainers()
                    break
                elif opcion3 == 2:
                    registro_trainer() 
                    break
                elif opcion3 == 3:
                    break
                else:
                    print("Opcion invalida")
        elif opcion == 4:
           print("Ingresaste a Estados de Campers")
           estado = input("Ingresa el estado para ver campers: ")
           campers_por_estado = listar_camper_por_estado(listar_camper_por_estado, estado)
           for camper in campers_por_estado:
              print(camper)
        
        elif opcion == 5:
          print("Saliendo Del Programa")
          break
        else:
            print("Ingresa Opcion valida")



menu_rol()

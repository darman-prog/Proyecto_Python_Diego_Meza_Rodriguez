from faker import Faker
import random

def ver_horarios():
   opcion_horario=input("Escoje Diurno o Nocturno").lower()
   horario_Diurno =[
         {     
        "artemis":"6 AM Hasta 2 PM ",
         },
       {
        "Sputnik":"6 AM Hasta 2 PM ",
       },
       {
        "Apolo":"6 AM Hasta 2 PM "
    }                    
    ]
   horario_Nocturno = [
{"Artemis":"2 PM Hasta 10 PM"
 },
{
"Sputnik":"2 PM Hasta 10 PM" 
},
{"Apolo":"2 PM Hasta 10 PM"
 }
    ]
   if opcion_horario=="diurno":
     print(horario_Diurno)
   elif opcion_horario == "nocturno": 
       print(horario_Nocturno)


listado_de_campers = []
def agregar_camper():
    campers = []

    print("Ingresa los Datos del Camper que Deseas Agregar")

    while True:
        try: 
            nombre_completo = input("Ingresa el Nombre completo del Camper: ")
            campers.append(nombre_completo)
            break
        except ValueError:
            print("Ingresa Un Nombre valido")

    while True:
        try:
            Documento = int(input("Ingresa numero de documento: "))
            campers.append(Documento)
            break
        except ValueError:
            print("Ingresa Un Documento valido")

    while True:
        direcion = input("Ingresa la direccion del Camper: ")
        campers.append(direcion)
        break

    while True:
        acudiente = input("Ingresa el nombre del acudiente: ")
        campers.append(acudiente)
        break

    while True:
        try:
            telefono_de_contacto = int(input("Ingresa el numero de celular del Camper: "))
            campers.append(telefono_de_contacto)
            break
        except ValueError:
            print("Ingresa numero de telefono valido")

    while True:
        try:
            telefono_de_fijo = int(input("Ahora Ingresa el Numero Fijo del Camper: "))
            campers.append(telefono_de_fijo)
            break
        except ValueError:
            print("Ingresa numero de fijo valido")

    while True:
        estado = input("Ingresa estado en la que se encuentra el camper: ")
        campers.append(estado)
        break

    while True:
        Riesgo = input("Ingresa el riesgo del camper: ")
        campers.append(Riesgo)
        break
    
    print("Camper Agregado")
    listado_de_campers.append(campers)
  
    return campers
def Registro_de_camper():
    Registro_manual_de_camper = []

    while True:
        nombre_completo = input("Ingresa tu Nombre Completo: ")
        if nombre_completo.strip(): 
            Registro_manual_de_camper.append(nombre_completo)
            break
        else:
            print("El nombre no puede estar vacío. Por favor, ingrésalo nuevamente.")

    while True:
        try:
            Documento_de_camper = int(input("Ingresa numero de documento: "))
            Registro_manual_de_camper.append(Documento_de_camper)
            break
        except ValueError:
            print("Ingresa Un Documento valido (número entero)")

    direcion = input("Ingresa tu dirección: ")
    if direcion.strip(): 
        Registro_manual_de_camper.append(direcion)
    else:
        print("La dirección no puede estar vacía. Por favor, ingrésala nuevamente.")

    acudiente = input("Ingresa el nombre de tu acudiente: ")
    if acudiente.strip():  
        Registro_manual_de_camper.append(acudiente)
    else:
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

    estado = input("Ingresa estado en la que se encuentra el camper: ")
    if estado.strip():  
        Registro_manual_de_camper.append(estado)
    else:
        print("El estado no puede estar vacío. Por favor, ingrésalo nuevamente.")

    riesgo = input("Ingresa el riesgo del camper: ")
    if riesgo.strip(): 
        Registro_manual_de_camper.append(riesgo)
    else:
        print("El riesgo no puede estar vacío. Por favor, ingrésalo nuevamente.")

    print("Registro Terminado. Proximamente te Contactaremos.")
    return Registro_manual_de_camper




fake = Faker('es_CO')

import json

listado_de_documentos=[]
def generar_documentos():
   try:
    with open("campers_Documentacion.json","r") as file:
        documento=json.load(file)
        if len(documento) >= 198:
            return documento[:198]
   except FileNotFoundError:
    pass
   
    documentos = []
    nuevo_documentos = []
    for _ in range(198-len(documentos)):
        nombre_de_camper = fake.name()
        cedula = fake.unique.ssn()
        numero_celular = fake.phone_number()
        acudiente = fake.name()
        estado = fake.random_element(elements=('En proceso de ingreso', 'Inscrito', 'Aprobado', 'Cursando', 'Graduado', 'Expulsado', 'Retirado'))
        riesgo = fake.random_element(elements=('Alto', 'Medio', 'Bajo'))
        direccion = fake.street_address()
        numero_fijo = fake.numerify('6#########')

        documento = {
            "Nombre Del aspirante": nombre_de_camper,
            "Riesgo Del camper": riesgo,
            "Direccion Del camper": direccion,
            "Cedula Del aspirante": cedula,
            "Numero De celular Del aspirante": numero_celular,
            "Numero fijo Del aspirante": numero_fijo,
            "Nombre Del acudiente": acudiente,
            "Notas":[random.randint(10,100), random.randint(10,100)],
            "Estado Del camper": estado,
        }


        nuevo_documentos.append(documento)
   
    if documentos:
        documentos.extend(nuevo_documentos)
    else:
        documentos = nuevo_documentos


        with open("Campers_Documentacion.json", 'w') as file:
              json.dump(documentos, file)
   
    return documentos

listado_de_documentos = generar_documentos()




Areas_de_entrenamiento = {
    "Ruta NodeJS": {
        "Capacidad": 33,
        "Modulos": ["NodeJS", "Express", "MongoDB"]
    },
    "Ruta Java": {
        "Capacidad": 33,
        "Modulos": ["Java", "Spring Boot", "Hibernate"]
    },
    "Ruta Netcore": {
        "Capacidad": 33,
        "Modulos": ["NetCore", "Entity Framework", "SQL Server"]
    },
    "Fundamentos de programación": {
        "Capacidad": 33,
        "Modulos": ["Introducción a la algoritmia", "PSeInt", "Python"]
    },
    "Programación Web": {
        "Capacidad": 33,
        "Modulos": ["HTML", "CSS", "Bootstrap"]
    },
    "Programación formal": {
        "Capacidad": 33,
        "Modulos": ["Java", "JavaScript", "C#"]
    },
    "Bases de datos": {
        "Capacidad": 33,
        "Modulos": ["MySQL", "MongoDB", "PostgreSQL"]
    },
    "Backend": {
        "Capacidad": 33,
        "duracion_meses":2,
        "Modulos": ["NetCore", "Spring Boot", "NodeJS y Express"]
    }
}

def Coordinadora_Registro_Notas():
    nombre_completo = input("Ingresa nombre del camper que deseas buscar")
    for camper in listado_de_campers:
        if camper["Nombre Completo"]==nombre_completo:
            nota_teorica =float(input("Ingresa Nota Teorica"))
            nota_practica=float(input("ingresa Nota Practica"))
            
            promedio = (nota_teorica+nota_practica)/2
            
            if promedio >= 60:
                print("El camper está aprobado con un promedio de", promedio)
                camper["Estado"] = "Aprobado"
            else:
                print("El camper no está aprobado con un promedio de", promedio)

            break
    else:
        print("Camper no encontrado")
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
            print("")



def registro_trainer():
    


def menu_trainer():
    while True:
        print("_____________Bienvenido Trainer______________")
        print("             1.Registro De Trainer           ")
        print("             2.Horarios                    ") 
        print("             3.salir                               ")
        opcion_trainer = int(input("ingresa el numero desigando para ingresar a una Opcion"))
        if opcion_trainer == 1:
            
def menu_coordinadora():
    while True:
        print("___________Campusland_________________")
   
        print("____________ (Menu) ____________________")
        print("      (Coordinacion Academica)                           ") 
         
        print("1. Campers Inscritos/Agregar Camper ")
        print("2. Coordinacion Academica/Registro de Notas de Campers ")
        print("3. Trainers Activos/Rutas Asignadas ")
        print("4. Estados de Campers/Informacion de campers           ")
        print("5. Salir Del Programa               ")

        print("____________________________________________")

        while True:
            try:
                opcion = int(input("Selecciona un número designado para cada opción para ingresar: "))
                break
            except ValueError:
                print("Ingresa un numero del 1/5")

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
                    print("Campers Inscritos Hasta la Fecha")
                    for camper in listado_de_documentos:
                        print(camper)
                    break
                elif opcion1 == 3:
                    break
                else:
                    print("Ingresa Opcion valida")

        elif opcion == 2:
            print("Ingresaste Coordinacion Academica")
            while True:
                
                print("1.Registro de Notas")
                print("2.Eliminar Camper")
                print("3. para volver Al menu principal")
                
                try:
                    opcion2 = int(input("Ingresa Una Opcion valida"))
                except ValueError:
                    print("Ingresa Opcion valida")
                
                if opcion2 == 1:
                    print("Ingresaste Registro de Notas")
                    Coordinadora_Registro_Notas()
                           
                elif opcion2 == 2:
                    print("Ingresaste a Eliminar Camper ") 
                elif opcion2 == 3:
                    break 
                else:
                    print("ingresa opcion valida")  
        elif opcion == 3:
            print("Ingresaste Trainers Activos")

        elif opcion == 4:
            print("Ingresaste a Estados de Campers")

        elif opcion == 5:
            print("Saliendo Del Programa")
            break

        else:
            print("Ingresa Opcion valida")

listado_de_documentos = generar_documentos()



menu_rol()


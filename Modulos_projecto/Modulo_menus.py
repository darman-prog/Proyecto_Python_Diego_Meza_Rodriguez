
from Modulos_proyecto.Modulo_trainer import registro_trainer
from utils import ver_horarios
from utils import Registro_de_camper
from Modulo_coordinacion import agregar_camper
from Modulo_coordinacion import eliminar_camper
from Modulo_coordinacion import listar_camper_por_estado
from Modulo_coordinacion import Coordinadora_Registro_Notas
from Modulo_coordinacion import campers_incristos_lista
from Proyecto_Python import listado_de_campers
from Proyecto_Python import listar_trainers

def menu_trainer():
    while True:
        print("_____________Bienvenido Trainer______________")
        print("             1.Registro De Trainer           ")
        print("             2.Horarios                    ") 
        print("             3.salir                               ")
        opcion_trainer = int(input("ingresa el numero desigando para ingresar a una Opcion"))
        if opcion_trainer == 1:
            registro_trainer()
        elif opcion_trainer ==2:
              ver_horarios()
        elif opcion_trainer ==3:
            break


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
                    eliminar_camper(nombre_completo, listado_de_campers)
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


import Modulo_coordinacion
import Modulo_campers
import Modulo_de_reportes 
import Modulo_menus 
import Modulo_trainer
import utils


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
            Modulo_menus.menu_Camper()
            break
        elif opcion_de_rol == 4:
            print("Saliendo Del Programa...")
            return  
        else:
            print("Ingresa Opcion valida")

def menu_coordinadora():
    while True:
        print("___________Campusland_________________  ")
   
        print("____________ (Menu) ____________________")
        
        print("     Coordinacion Academica             ") 
         
        print("1. Campers inscritos/Agregar Camper/eliminar registro de camper                    ")
        print("2. Registro de Notas de Campers                                                    ")
        print("3. Lista de trainers activos/Registro de Trainer                                           ")
        print("4. Estados de Campers                                                             ")
        print("5. Evaluar Camper/Asignar Ruta                                                             ")
        print("6. Salir del menu                                                                 ")
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
                    Modulo_coordinacion.agregar_camper() 
                    break
                elif opcion1 == 2:  
                    Modulo_de_reportes.ver_documentos()
                    break
                elif opcion1 == 3:
                    Modulo_coordinacion.eliminar_camper()
                    break
                elif opcion1 == 4:
                    break
                else:
                    print("Ingresa Opcion valida")
        elif opcion == 2:
            Modulo_coordinacion.Coordinadora_Registro_Notas()
            break 
        elif opcion == 3:
            while True:
                print("1. Listado De trainers ")
                print("2. Registrar Trainer   ")
                print("3. salir del programa  ")
                try:
                    opcion3 = int(input("Escoje una Opcion del 1 al 3: "))
                except ValueError:
                    print("Error: Ingresa un número entero.")
                    continue

                if opcion3 == 1:
                    Modulo_de_reportes.imprimir_trainers()
                elif opcion3 == 2:
                    Modulo_coordinacion.registro_coordinadora() 
                elif opcion3 == 3:
                    break
                else:
                    print("Opcion invalida")
        elif opcion == 4:
            while True:  
                print("bienvenido a estados de campers escoje una Opcion  ")
                print("1.campers Inscritos           ")
                print("2.campers en estado de riesgo ")
                print("3.Salir del menu                       ")
                print("4.Evaluar campers ")
                try:
                    estado_opcion = int(input("para selecionar una opcion escribe 1 o 2 y para salir 3"))
                except ValueError:
                    print("Ingresa Otra vez") 
                if estado_opcion == 1:
                    Modulo_de_reportes.listar_camper_por_estado("Inscrito")
                    break
                elif estado_opcion == 2:
                    Modulo_de_reportes.listar_camper_por_riesgo("Alto")
                    break
                elif estado_opcion == 3:
                    break
        elif opcion == 5:
            Modulo_coordinacion.evaluar_campers()
        elif opcion == 6:
            print("Saliendo Del menu....... ")
            break     
        else:
            print("Ingresa Opcion valida")

def menu_trainer():
    while True:
        print("_____________Bienvenido Trainer______________")
        print("             1.Registro De Trainer           ")
        print("             2.Horarios                    ") 
        print("             3.salir                               ")
        opcion_trainer = int(input("ingresa el numero desigando para ingresar a una Opcion"))
        if opcion_trainer == 1:
            Modulo_trainer.registro_trainer()
        elif opcion_trainer == 2:
           Modulo_trainer.ver_horarios()
        elif opcion_trainer == 3:
            break

def menu_Camper():
    while True:
        print("________Bienvenido Camper_________")
        print("        1.Registro De Camper      ")
        print("        2.Salir                         ")
        opcion_camper = int(input("Ingresa el numero asignado para cada Opcion Para ingresar"))
        if opcion_camper == 1:
            Modulo_campers.Registro_de_camper()
            break
        elif opcion_camper == 2:
            menu_rol()
            break

utils.generar_documentos()
utils.generar_trainers_campusland()
Modulo_menus.menu_rol()

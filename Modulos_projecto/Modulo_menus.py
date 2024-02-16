from Modulo_trainer import registro_trainer
from utils import ver_horarios
from utils import Registro_de_camper


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

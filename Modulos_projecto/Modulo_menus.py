from Modulo_trainer import registro_trainer
from utils import ver_horarios

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
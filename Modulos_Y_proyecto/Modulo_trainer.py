from utils import guardar_datos_trainer #aca estan los datos guardados de trainer
#registro en el sistema de trainer nuevo
def registro_trainer():
    datos_trainer = []
    print("Bienvenido al Registro de Trainer")
    print("Ingresa tus datos para registrarte en el sistema ")
    
    while True:
        nombre = input("Ingresa tu nombre completo: ")
        if nombre:
            datos_trainer.append(nombre)
            break
        else:
            print("El nombre no puede estar vacío. Por favor, ingrésalo nuevamente.")
        
    while True:
        try:
            numero_de_trainer = int(input("Ingresa tu número telefónico: "))
            datos_trainer.append(numero_de_trainer)
            break
        except ValueError:
            print("Ingresa un número de teléfono válido.")
    
    while True:
        try:
            documento_trainer = int(input("Ingresa tu número de documento: "))
            datos_trainer.append(documento_trainer)
            break
        except ValueError:
            print("Ingresa un número de documento válido.")
    
    conocimientos_trainer = input("Conocimientos de Programacion ")
    datos_trainer.append(conocimientos_trainer)

    while True:
        salon_asignado = input("Ingresa el salón asignado: ")
        if salon_asignado:
            datos_trainer.append(salon_asignado)
            break
        else:
            print("El salón no puede estar vacío. Por favor, ingrésalo nuevamente.")

    while True:
        ruta_asignada = input(" Ingresa la ruta asignada: ")
        if ruta_asignada:
            datos_trainer.append(ruta_asignada)
            break
        else:
            print("La ruta no puede estar vacía. Por favor, ingrésala nuevamente.")
    
    print(" Trainer Agregado Exitosamente!! ")
    guardar_datos_trainer(datos_trainer)

#ver horarios para el trainer
def ver_horarios():
     opcion_horario = input("Escoje diurno o nocturno").strip().lower()
     horario_Diurno = [
         {"artemis": "6 AM Hasta 2 PM"},
         {"Sputnik": "6 AM Hasta 2 PM"},
         {"Apolo": "6 AM Hasta 2 PM"}
     ]
     horario_Nocturno = [
         {"Artemis": "2 PM Hasta 10 PM"},
         {"Sputnik": "2 PM Hasta 10 PM"},
         {"Apolo": "2 PM Hasta 10 P M"}
     ]

     if opcion_horario == "diurno":
         print(horario_Diurno)
     elif opcion_horario == "nocturno":
        print(horario_Nocturno)

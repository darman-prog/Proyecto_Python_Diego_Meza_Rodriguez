import json



def guardar_datos_trainer(datos_trainer,ruta_archivo):
    with open(ruta_archivo,"a") as archivo:
        json.dump(datos_trainer,archivo)
        
        archivo.write('\n')

def registro_trainer():
    datos_trainer = []
    print("Bienvenido a Registro de Trainer")
    print(" Ingresa Tus Datos Para Registrarte En el sistema y Asignarte una Clase ")
    while True:
       try: 
         nombre = input(" Ingresa tu nombre Completo ")
         break
       except ValueError:
           print("Ingresa Nombre Valido")  
        
    datos_trainer.append(nombre)
    
    while True:
       try:
          numero_de_trainer = int(input("Ingresa tu Numero Telefonico"))
          break       
       except ValueError:
           print ("Ingresa Numero valido")
    datos_trainer.append(numero_de_trainer)
    
    while True:
       try:
           documento_trainer=int(input("Ingresa Tu numero de Documento"))
           break       
       except ValueError:
           print ("Ingresa Numero valido")
    datos_trainer.append(documento_trainer)
    while True:
       try:
            Conocimientos_trainer = input("Que Conocimientos Tienes En Programacion ")
            break
       except ValueError:
            print("Ingresa Otra vez")       
    datos_trainer.append(Conocimientos_trainer)
    ruta_archivo = "datos_trainer.json"  
    
    guardar_datos_trainer(datos_trainer, ruta_archivo)
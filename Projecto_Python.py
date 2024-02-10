listado_de_campers=[]
def agregar_camper(nombre_completo,direcion,acudiente,telefono_de_contacto,telefono_de_fijo,estado,Riesgo):
 campers = []
 
 print( "Ingresa los Datos del Camper que Deseas Agregar" )  
 
 while True:  
  try:
      nombre_completo=input("Ingresa el Nombre completo del Camper")
      break  
  except ValueError("Ingresa nombre valido"):
   campers.append(nombre_completo)
 
 while True:
    try: 
       direcion=input("Ingresa la direccion del Camper")
       break
    except ValueError("Ingresa direccion valida"):
  
     campers.append(direcion)
 
 while True:
  try:
      acudiente=input("Ingresa el nombre del acudiente ")
      break
  except ValueError("ingrese Nombre del acudiente Correctamente"):  
    
    campers.append(acudiente)
 
 while True:
    try:
        telefono_de_contacto = int(input("Ingresa el numero del Camper"))
        break
    except ValueError:
     print("Ingresa numero de telefono valido")
    
 campers.append(telefono_de_contacto)

 while True:
    try:
        telefono_de_fijo = int(input("Ahora Ingresa el Numero Fijo del Camper"))
        break    
    except ValueError:
     print("ingresa numero de fijo valido")
 
 campers.append(telefono_de_fijo)
 
 while True:
    try:
        estado=input("Ingresa estado en la que se encuentra el camper")
        break
    except ValueError:
        print("Ingresa un estado valido")
 
    campers.append(estado)
 while True:
    try: 
        Riesgo=input("Ingresa el riesgo del camper")
        break
    except ValueError:
        print("Ingresa un Riesgo valido")
 campers.append(Riesgo) 

agregar_camper(nombre_completo=(),direcion=(),acudiente=(),telefono_de_contacto=(),telefono_de_fijo=(),estado=(),Riesgo=())

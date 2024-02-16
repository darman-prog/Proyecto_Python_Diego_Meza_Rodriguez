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
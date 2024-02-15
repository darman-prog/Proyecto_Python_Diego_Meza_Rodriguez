

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
        {"Apolo": "2 PM Hasta 10 PM"}
    ]

    if opcion_horario == "diurno":
        print(horario_Diurno)
    elif opcion_horario == "nocturno":
        print(horario_Nocturno)
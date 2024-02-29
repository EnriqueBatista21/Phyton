#Opciones


def opcion_1():
    print("Has seleccionado la opción 1")

def opcion_2():
    print("Has seleccionado la opción 2")

def opcion_3():
    print("Has seleccionado la opción 3")

def salir():
    print("Saliendo del programa")
    exit()

menu = {
    '1': opcion_1,
    '2': opcion_2,
    '3': opcion_3,
    '4': salir
}

while True:
    # Mostrar el menú
    print("\n=== Menú ===")
    for key, value in menu.items():
        print(f"{key}. {value.__name__.replace('opcion_', 'Opción ')}")

    # Obtener la elección del usuario
    opcion = input("Selecciona una opción (1-4): ")

    # Realizar acciones basadas en la opción seleccionada
    accion = menu.get(opcion)
    if accion:
        accion()
    else:
        print("Opción no válida. Por favor, selecciona una opción válida.")

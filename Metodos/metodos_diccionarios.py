diccionario = {
    "nombre": 'Enrique',
    "apellido": 'Batista',
    "ingresos": 10000
}

#keys nos devuelve las claves de un diccionario
claves = diccionario.keys()

#obtener un elemento con get()
nombre = diccionario.get("nombre")

#elmininar todos los elementos del diccionario
diccionario.clear()

#eliminando un elemento del diccionario se puede mas de un elemento
diccionario.pop("nombre")

#obteniendo un elemento dic_items iterable
diccionario_iterable = diccionario.items()


print(nombre)


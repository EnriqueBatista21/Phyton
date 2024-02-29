#creando lista con list()
lista = list(["Hola","Putos"])
print(len(lista)) #Cantidad de elementos de la lista

#agregando elementos a la lista
lista.append("Perros")

#agregando un elemento a la lista con un indice especifico, si ya existe recorre el elemento existente'
lista.insert(2,"XD")

#agregar varios elementos a lista
lista.extend(["XD2,X3",False])

#eliminando un elemento de la lista por indice, con -1 elimina el ultimo elemento y asi sucesivamente
lista.pop(0)

#removiendo un elemento por su valor
lista.remove("XD")


print(lista)
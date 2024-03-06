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

#removiendo un elemento por su valor si este se encuentra en la lista
lista.remove("XD")

#elmiminando todos lo elementos
lista.clear()

#ordenando elementos
lista.sort()#menor a mayor
lista.sort(reverse=True)#mayor a manor

#invirtiendo lo elementos de una lista
lista.reverse()


print(lista)
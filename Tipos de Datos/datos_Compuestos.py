#Pueden ser Modificadas
lista = ["Kike","Pipe",True,1.73]
print(lista[1])
#No pueden ser modificadas
tupla = ("Kike","Pipe",True,1.73)

#ESTO NO SE PUEDE
#tupla[1] = "Ola"

#ESTO SI
#lista[1] = "Ola"

print(tupla[0])

#Creando un conjunto set, tampoco se puede modificar
#No se accede a los datos mediante indices, solo iterando
#No permite repetir valores

conjunto = {"Hola","Rayo",False,1,73}
print(conjunto)

#creando diccionario, la estructura es key : value y separamos por comas
#se accede mediante claves
diccionario = {
    'nombre': "Enrique Batista",
    'altura': 1.73,
    'XD': True
}
print(diccionario["nombre"])

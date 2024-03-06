#creando diccionario con dict()
diccionario = dict(nombre = "enrique", apellido = "batista")
print(diccionario )
print("\n")
#las lista no pueden ser claves las tuplas si
#diccionario = {("dalto","rancio"):"xd"}
#usamos frozenset para meter conjuntos
diccionario = {frozenset(["enrique","batista"]):"xdxdxd"}
print(diccionario )
print("\n")
#creando con fromkeys(), valor por defecto = none
diccionario = dict.fromkeys(["nombre","apellido"])
print(diccionario )
print("\n")
#creando con fromkeys(), valor por defecto = "pepe"
diccionario = dict.fromkeys(["Enrique","Batista"],"pepe")
print(diccionario )
print("\n")
#si no lo creamos con una lista, el primer dato sera iterable para los demas
dic = dict.fromkeys("HOLA","Enrique")
print(dic)
print("\n")
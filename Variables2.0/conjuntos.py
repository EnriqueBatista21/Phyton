#creando un conjunto con set
conjunto = set(["dato1","dato2"])

#metiendo un conjunto dentro de otro conjunto
conjunto1 = frozenset(["dato1","dato2"])
conjunto2 = {conjunto1,"dato3"}
print(conjunto2)

#toeoria de conjuntos
#Un subconjunto A contiene datos de un conjunto B
#B es un superconjunto de A que contiene todo A y mas datos
#Puede ser de manera inversa

conjunto1 = {1,3,5,7}
conjunto2 = {1,3,7}

#comprobando que conjunto 2 es subconjunto de conjunto 1
resultado = conjunto2.issubset(conjunto1)
print(resultado)

#comprobando que conjunto 1 es superconjunto de conjunto 2
resultado = conjunto1.issuperset(conjunto2)
print(resultado)


#Verificar si hay algun numero en comun
res = conjunto2.isdisjoint(conjunto1)
print(res)
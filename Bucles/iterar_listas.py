
animales = ["perro","gato","cocodrilo"]
numeros = [10,2,4]

#recorriendo la lista animales
for animal in animales:
    print(f"Ahora la variable animal es = {animal}" )

#recorriendo lista numeros y multiplicandolos por 5
for numero in numeros:
    res = numero * 5
    print(res)    

#se pueden iterar al mismo tiempo solo si tienen la misma cantidad de datos
for animal, numero in zip(animales,numeros):
    print(f"Recorriendo lista animales: {animal}")
    print(f"Recorriendo lista numeros: {numero}")

for num in range(5,10):
    print(num)

#forma optima de recorrer por indice
for num in enumerate(numeros):
    print(num)
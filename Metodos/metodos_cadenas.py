cadena1 = "Hola, Perro , gordo"
cadena2 = "Bienvenido paps"
lista = ["Pepe"]
#print(dir(lista)) #Dir te muestra lo que puedes hacer con el objeto

mayusculas = cadena1.upper() #Convierte a mayusculas

minusculas = cadena1.lower() #Convierte a minusculas

primer_letra_mayus = "pepe dijo".capitalize() #Convierte la primer letra a mayuscula y lo demas a minuscula

#buscando una cadena en otra cadena
busqueda = cadena1.find("sos") #Busca y muestra la posicion, si no encuentra regresa -1

#busqueda igual, si no encuentra lanza una excepcion
busqueda2 = cadena1.index("a")

#si es numerico true, si no, false
es_numerico = cadena1.isnumeric()

#si es alfanumerico true, solo letras
es_alfanum = cadena1.isalpha()

#Concurrencias en una cadena, devuelve cuantas veces se repite
coincidencias = cadena1.count("a")

#Contamos la cantidad de caracteres en una cadena, es un metodo
num_caracteres = len(cadena1)

#verificamos si una cadena empieza con otra cadena dada, true o false
empieza_con = cadena1.startswith("H") #True

#Veridicamos si termina
termina_con = cadena1.endswith("la") #True

#Reemplaza un pedazo de la cadena, por otra nueva
cadena_nueva = cadena1.replace("la","lu")

#Separar cadenas con la cadena que le pasemos
cadena_separada = cadena1.split(",")


print(cadena_separada)

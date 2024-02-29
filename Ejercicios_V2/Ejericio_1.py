#promedios
otros_cursos_min = 2.5
otros_cursos_max = 7
otros_cursos_prom = 4
dalt_curso = 1.5

#diferencias de duracion

dif_min = 100 - (dalt_curso / otros_cursos_min *100)
dif_max = 100 - (dalt_curso *1000 // otros_cursos_max /10)
dif_prom = 100 - (dalt_curso / otros_cursos_prom *100)

print(f"{dif_min}% mas rapido que el mas rapido")
print(f"{dif_max}% mas rapido que el mas lento")
print(f"{dif_prom}% mas rapido que el promedio")

import random

suma=0
promedio=0
desviacion=0
rango=random.randint(10,25)

vector=[round(random.random()*100)for i in range(rango)]
for i in range(rango):
    suma+=vector[i]
    promedio=suma//rango
    vector.sort()
    tamaño=len(vector)
    tamaño_division=tamaño-1
desviacion=(suma-promedio)**2
division=desviacion//tamaño_division
resultado=division**0.5

print("La lista es:", vector)
print("El tamaño de la lista es:", rango)
print("La desviasion estandar es:",resultado)
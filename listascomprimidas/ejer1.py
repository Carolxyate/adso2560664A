import random

promedio=0
suma=0
rango=random.randint(10,25)

vector=[round(random.random()*100)for i in range(rango)]
for i in range(rango):
    suma+=vector[i]
print(suma)
premedio=suma//rango
print("El rango de la lista es:",rango)
print("Los valores de la lista son:", vector)
print("El promedio de los valores es:", promedio)

for n in vector:
    if n<promedio:
        print("El numero", n, "es menor al promedio")
    elif n>promedio:
        print("El numnero", n, "es mayor al promedio")
    elif n==promedio:
        print("El numnero", n, "es igual al promedio")
        

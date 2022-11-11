import random
suma=0
promedio=0
rango=random.randint(10,25)
vector=[round(random.random()*100)for i in range(rango)]
for i in range(rango):
    suma+=vector[i]
    promedio=suma//rango
    
print("El rango de la lista es:",rango)
print("Los elementos de la lista son:",vector)
print("La suma de los elementos de la lista es:",suma)
print("El promedio de los elementos de la lista es:",promedio)
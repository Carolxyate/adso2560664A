import random

rango=random.randint(10,25)
vector=[round(random.random()*100)for i in range(rango)]
print("La lista sin ordenar es:",vector)
intercambio=True
while intercambio:
    intercambio=False
    for i in range(len(vector)-1):
        if vector[i]<vector[i+1]:
            vector[i],vector[i+1]=vector[i+1],vector[i]
            intercambio=True
vector2=vector[:]
intercambio2=True
while intercambio2:
    intercambio2=False
    for j in range(len(vector2)-1):
        if vector2[j]>vector2[j+1]:
            vector2[j],vector2[j+1]=vector2[j+1],vector2[j]
            intercambio2=True
            
print("La lista ordenada en forma descendiente es:", vector)
print("La lista ordenada en forma ascendente es:", vector2)


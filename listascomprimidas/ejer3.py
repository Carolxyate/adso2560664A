import random

total_pares=0
total_impares=0
promedio_impares=0
rango=random.randint(10,25)
vector=[round(random.random()*100)for i in range(rango)]

par=[x for x in vector if x%2==0]
for x in range(len(par)):
    total_pares+=par[x]
impar=[x for x in vector if x%2!=0]
for x in range(len(impar)):
    total_impares+=impar[x]

promedio_impares=(total_impares//len(impar))

print("La longitud de la lista es:", rango, "y los valores de la lista son: ",vector)
print("La suma de los pares fue:", total_pares)
print("El promedio de los impares es:",promedio_impares)

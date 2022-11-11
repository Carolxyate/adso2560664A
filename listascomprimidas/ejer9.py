import random

rango=random.randint(10,25)
vector=[round(random.random()*100)for i in range(rango)]
print("La lista sin ordenar es:",vector)

vector.sort()
print("La lista ordenada es:",vector)
mitad=int(rango//2)

if rango %2==0:
    mediana=(vector[mitad-1]+vector[mitad])//2
else:
    mediana=vector[mitad]
print("La longitud del vector es:", rango)
print("La mediana del vector es:",mediana)

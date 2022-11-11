import random
random1=[]
rango= random.randint(10,25)
mediana=0
longitud=len(random1)

for i in range (rango):
    random1.append(round(random.random()*100))
    random1.sort()
    longitud = len(random1)
    if longitud%2 > 0:
        mediana = random1[longitud // 2]
print("La lista es: ", random1)
print("La mediana de la lista es: ", mediana)
import random

cont=0
posicion=""
rango=random.randint(10,25)
vector=[round(random.random()*100)for i in range(rango)]
print(vector)

numero=int(imput("Elija el numero: "))

for i in range(rango):
    if numero==vector[i]:
        posicion+=str(i)+" "
        cont+=1
if cont==0:
    vector.append(numero)
    print("El numero se agrego al final de la lista")
    print(vector)
else:
    if cont==1:
        print("El numero de la lista",numero," esta 1 vez y esta en la posicion",posicion)
    else:
        print("El numero de la lista",numero,"esta",cont,"veces y esta en las posiciones",posicion)

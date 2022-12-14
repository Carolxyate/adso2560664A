import random
def llenar_lista(lista):
    lista=[round(random.randrange(100))for i in range(random.randint(10,25))]
    return lista

lista=llenar_lista(list)
lista.sort()
rango=len(lista)

def par(lista):
    total_pares=0
    par=[x for x in lista if x%2==0]
    for x in range(len(par)):
        total_pares+=par[x]
    return total_pares

def impar(lista):
    total_impares=0
    impar=[x for x in lista if x%2!=0]
    for x in range(len(impar)):
        total_impares+=impar[x]
    promedio_impares=(total_impares//len(impar))
    return promedio_impares

print("La longitud de la lista es: ",rango, "y los valores de la lista son: ",lista)
print("La suma de los pares fue: ",par(lista))
print("El promedio de los impares es: ",impar(lista))

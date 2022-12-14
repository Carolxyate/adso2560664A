import random
def llenar_lista(lista):
    lista=[round(random.randrange(100))for i in range(random.randint(10,25))]
    return lista

lista=llenar_lista(list)
lista.sort() #se organiza la  lista
rango=len(lista)

def mediana(lista):
    mitad=int(rango//2) # la mitas es el rango entre 2
    if rango%2==0: #si el rango es divisible entre 2,se sumaran los dos valores mas cercanosa la mitad y se dividiran entre 2
        mediana=(lista[mitad-1]+lista[mitad])//2
    else: #si no, solo toma el valor central
        mediana=lista[mitad]
    return mediana
print(lista)
print("la longitud de la lista es: ", rango)
print("la mediana de la lista es: ",mediana(lista))
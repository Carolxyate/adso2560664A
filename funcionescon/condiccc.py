#Encuentre la suma y el promedio de los números de la lista - Arreglos
import random
def sumandprom_lista(lista):
    suma = 0
    contador = 0
    for numero in lista:
        suma+=numero
        contador+=1
        promedio=suma//contador
        print("La suma es: ", suma)
    return "El promedio es:", promedio

numero = random1=[]
rango= random.randint(10,25)
for i in range (rango):
        random1.append(round(random.random()*100))
print(numero)
print(sumandprom_lista(numero))
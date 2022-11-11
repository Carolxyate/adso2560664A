import random

vector=[]
aux=True
A=0
B=1
C=1
while aux:
    rango=int(input("Elija la cantidad de elementos a ejecutar de la serie de Fibonacci: "))
    if rango>=5 and rango<=20:
        aux=False
    else:
        print("Deben de ser minimo 5 elementos y maximo 20")

for i in range(rango):
    C=A+B
    A=B
    B=C
    vector.append(C)
print("La ñista con los valores de fibonacci hasta la posicion insertada es:",vector)
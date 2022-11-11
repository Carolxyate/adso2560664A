import random

tam=random.randint(10,25)
vector=[]
veccant=[]
for i in range(tam):
    vector.append(round(random.random()*100))
print(vector)
cont=0
var1=0
cant=0
var2=0
for i in range(tam):
    cont+=1
    var1+=vector[i]  
    prom=var1//cont  
print('la suma de los numeros es ',var1,)
print('el promedio es ',prom)#('el promedio es ',var1//cont)
for n in vector:
    if n < prom:
        print('el numero',n,' es menor al promedio ')
    if n > prom:
        print('el numero ',n,'es mayor al promedio ')
    else:
        print('el numero ',n,' es igual al promedio')
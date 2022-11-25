#condicionales encadenadas
#Al ingresar dos numeros, muestre si son mayor, menor o iguales 

num=int(input("ingrese el primer numero: "))
n=int(input("ingrese el primer numero: "))
if num < n:
    print(num, "es menor que", n)
elif num > n:
    print (num, "es mayor que", n)
else:
    print (num, "y",n, "son iguales")
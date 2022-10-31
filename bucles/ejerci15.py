num=int(input("Digite un numero entero positivo: "))
n=num+1
if num > 0:
    while n >0:
        for i in range(1, n):
            print(i , end=" ")
        n-=1
        print()
else:
    print("El numero no esta dentro de los parametros")

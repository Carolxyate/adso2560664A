n = int(input("Introduzca un numero para determinar sus divisores= "))
i = 1

print("Los divisores son: ")
while(n >=1):
 if n%i == 0:
  print(i)
 i+=1
 
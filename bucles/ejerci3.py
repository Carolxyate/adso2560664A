i=1
conter = 0
suma = 0

n = int(input("Ingrese un numero para determinar si es perfecto: "))

while(n > i):
 if n%i ==0:
  conter=i
 i+=1

for i in range(conter + 1):
  suma+=1

if n == suma:
 print("El numero", n, " es perfecto")
else:
 print("El numero ", n, " no es perfecto")
 

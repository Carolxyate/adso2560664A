for n in range(2,1000):
  i=1
  c = 0

  while(n >= i):
   if n%i ==0:
    c+=1
   i+=1
  if not c > 2 or n <=1:
   print("El numero ", n, " es primo")
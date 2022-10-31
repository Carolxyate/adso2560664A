x=int(input("Ponga la base: "))
y=int(input("Ponga el exponente: "))
i=1
opera=x
while(i<y):
    i+=1
    opera*=x
if y<=0:
    opera=1
print(opera)

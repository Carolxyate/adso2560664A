#9 de bucles
#exponente y base

x=0
y=0
def base(x,y):
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
    return "  "

print(base(x,y))



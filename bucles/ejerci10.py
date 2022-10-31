n=int(input("Ponga el primer numero: "))
m=int(input("Ponga el segundo numero: "))
while not (m == 0):
    a=n
    b=m
    if n < 0:
        n=-a
        m=b
    if m < 0:
        n=a
        m=-b
    else:
        n= b
        m= a%b
print(n)

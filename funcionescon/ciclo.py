def numero(num):
    r = 0
    n = int(input("Ingrse un numero de hasta 9 cifras: "))
    while n !=0:
        c = n % 10
        r = r * 10 + c
        n = n // 10
        return n
print(numero)
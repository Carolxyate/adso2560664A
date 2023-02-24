def divi(n):
    try:
        for i in range(n+1):
            if n%i==0:
                print("Divisor",i)
    except ArithmeticError:
        print("Indeterminación")
    except TypeError:
        print(type(n),"tipo de dato no soportado")
v=(input("Escriba numero:"))
divi(v)
print("Continua en esta linea")
print('El programa continua en esta linea')
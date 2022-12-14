#Solicitar 2 números al usuario e imprimir el cociente y el residuo del mayor en el menor 
#Ciclos
def divisor_residuo(dividendo1, divisor):
    if dividendo1 % divisor == 0:
        print("La división es exacta. Cociente :", (divisor // dividendo1))
    else:
        print("La división no es exacta. Cociente: ", (divisor % dividendo1))
    return dividendo1, divisor

print(divisor_residuo(9,2))
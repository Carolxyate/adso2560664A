A = input("Ingrese las horas trabajadaS: ")
B = float(A)
C = B - 40
D = (40 * 2600) + (C * 5000)
E = B * 2600
if B > 40:
    print("El salario es: ", D)
elif B < 40:
    print("El salario es: ", E)
    

A = int(input("Ingrese coeficiente de la variable cuadratica: "))
B = int(input("Ingrese coeficiente de la variable lineal: "))
C = int(input("Ingrese termino independiente: "))
x1 = 0
x2 = 0

if((B**2)- 4*A*C) < 0:
    print("La solucion de la ecuacion es con numeros complejos")
else:
    x1 = ((B**2-(4*A*C))-B**0.5)/(2*A)
    x2 = ((B**2-(4*A*C))-B**0.5)/(2*A)
    print("Las soluciones de la ecuacion son: ", x1, x2)
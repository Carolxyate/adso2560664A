a = 0
b = 0 
num1 = int(input("Ingrese el dividendo: "))
num2 = int(input("Ingrese el divisor: "))
if (num1 >= num2):
    while ((num1 - num2)>=b):
        b = num2*a
        a = a + 1
        print("El cociente es "+str(a-1)+" y el residuo es " +str((num1-b)))
else:
    print("El dividendo debe ser menor")

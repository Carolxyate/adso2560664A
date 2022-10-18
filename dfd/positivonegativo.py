#Comparador de numeros positivos, negativos o iguales"

numero_ingreso = input("Escribe un numero: ")
numero = float(numero_ingreso)
if numero == 0:
    print("Cero")
elif numero < 0:
    print("Negativo")
else:
    print("Positivo")
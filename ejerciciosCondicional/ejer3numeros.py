numero1 = int(input("Ingrese el primer numero:"))
numero2 = int(input("Ingrese el primer numero:"))
numero3 = int(input("Ingrese el primer numero:"))

menor = min(numero1, numero2, numero3)
mayor = max(numero1, numero2, numero3)
medio = (numero1 + numero2 + numero3) - menor - mayor 

print(menor, medio, mayor)
s
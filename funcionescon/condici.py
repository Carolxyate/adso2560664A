
def iguales(a,b,c):
    numero1=0
    numero2=0
    numero3=0
    if numero1 == numero2 and numero2 == numero3:
        print("los 3 numeros son iguales")
    elif numero1 == numero2 and numero2 != numero3:
        print("solo hay 2 numeros iguales")
    elif numero1 != numero2 and numero2 == numero3:
        print("solo hay 2 numeros iguales")
    elif numero1 != numero3 and numero2 == numero3:
        print("solo hay 2 numeros iguales")
    elif numero1 == numero3 and numero2 != numero3:
        print("solo hay 2 numeros iguales")
    else: 
        print("los 3 numeros son diferentes")  

iguales(3,9,6)
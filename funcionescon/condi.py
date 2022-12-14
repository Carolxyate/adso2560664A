
def cifras(num):
    if num<0 and num>9999:
        print("el numero ingresado es invalido")
    else:
        if num>=0 and num<=9:
            print("El numero tiene 1 cifra")
        elif num>=10 and num<=99:
            print("El numero ingresado tiene 2 cifras")
        elif num>=100 and num<=999:
            print("El numero ingresado tiene 3 cifras")
        elif num>=1000 and num<=9999:
            print("El numero ingresado tiene 4 cifras")
        elif num>=10000:
            print("El numero ingresado es invalido")

cifras (100)
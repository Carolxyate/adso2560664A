def operacion():
    num1 = input("Ingrese el primer número: ")
    cadena = input("Ingrese una cadena de texto: ")
    
    try:
        num1 = float(num1)
        resultado = num1 + cadena
        print(f"El resultado de la operación es {resultado}.")
    except TypeError:
        print("Los tipos de datos no son compatibles para realizar la operación. Intente con otros valores.")
operacion()
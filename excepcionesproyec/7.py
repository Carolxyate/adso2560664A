def multiplos():
    num = input("Ingrese un número entero: ")
    
    try:
        num = int(num)
        for i in range(1, 11):
            print(num * i)
    except ValueError:
        print("Debe ingresar un número entero. Intente nuevamente.")
multiplos()

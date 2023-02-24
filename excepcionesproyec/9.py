def keyboard():
    try:
        while True:
            ingrese=int(input("ingrese su edad: "))
            print("su edad es:", ingrese)
            break
    except KeyboardInterrupt:
        cerrar=input("estas seguro de cerrar el programa? (S/N)")
        if cerrar.upper()=="S":
            print("aplicacion cerrada por usuario")
    except:
        print("no has ingresado un numero vuelve a intentarlo")
            
            
keyboard()
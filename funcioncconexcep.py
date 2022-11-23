def funcion(A,B,C):
    signo=input("Ingrese el signo: ")
    if signo=="+":
        funcion_cua=(-B+((B**2-4*A*C)*0.5))//(2*A)
        return funcion_cua
    elif signo=="-":
        funcion_cua=(-B-((B**2-4*A*C)*0.5))//(2*A)
        return funcion_cua

while True:
    try:
        P = input("¿Desea colocar el valor de A?: ")
        if P == "si":
            A = int(input("Ingrese el valor de A: "))
        P = input("¿Desea colocar el valor de B?: ")
        if P == "si":
            B = int(input("Ingrese el valor de B: "))
        P = input("¿Desea colocar el valor de C?: ")
        if P == "si":
            C = int(input("Ingrese el valor de C: "))
        if A==0 and B==0 and C==0:
            print("finalizado")
            break
        print(funcion(A,B,C))
    except ValueError:
        print("Los elementos son incorrectos")
    except ZeroDivisionError:
        print("Por cero no se puede")
    except:
        print("Los datos son incorrectos")
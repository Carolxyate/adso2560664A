def numerolarge():
    j = 5.0
    try:
        for i in range(1,1000):
            j = j**i
            print(j)
    except OverflowError:
        print("Error de Overflow ha ocurrido")
    except:
        print("Algo salio mal")

numerolarge()
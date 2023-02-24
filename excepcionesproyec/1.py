def nombre(x):
    try:
        print(x)
    except NameError:
        print("La variable X no esta definida")
    except:
        print("Algo esta mal")
    return None

nombre()
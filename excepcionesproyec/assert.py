def err(o):
    try:
        assert o>200 and o<300
        print("El valor entra en el rango",o)
    except AssertionError:
        print("El valor no entra en el rango",o)
o=int(input("Ingrese un numero al azar:"))
err(o)
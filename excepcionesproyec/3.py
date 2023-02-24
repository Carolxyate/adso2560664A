#ValueError

def error():
    try:
        a = 10
        a.append(6)
    except AttributeError:
        print("Es un error de atributo")

error()

#cuantas veces se repite un caracter dado

def contar_repetidos():
    letra1=str(input("ingrese una palabra: "))
    n=str(input("ingrese una letra: "))
    contar=letra1.count(n)
    print(contar , "cantida de veces que se repite")
    
contar_repetidos()


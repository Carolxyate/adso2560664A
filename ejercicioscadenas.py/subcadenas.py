# Imprima todas las subcadenas que salen de una cadena comenzando con las dos primeras letras, luego 
#tres primeras y así sucesivamente hasta llegar a la última.
def cad(i):
    longitud = len(cadena)
    for i in range(2, longitud+1):
        for j in range(longitud-i+1):
            subcadena = cadena[j:j+i]
            print(subcadena)

cadena = input("Ingresa una cadena de texto: ")
cad(cadena)
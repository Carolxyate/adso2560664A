#cuantas veces se repite un caracter dado
"""
def contar_repetidos():
    letra1=str(input("ingrese una palabra: "))
    n=str(input("ingrese una letra: "))
    contar=letra1.count(n)
    print(contar , "cantida de veces que se repite")
    
contar_repetidos()"""


#- Solicite cadena e imprimala en todas las formas posibles en cuanto a mayusculas y minusculas

"""def mayusculas():
    print("seleccione si en mayuscula o minuscula")
    palabra=str(input("ingrese una de las opciones"))
    if palabra=="mayuscula":
        print("ingrese una palabra en minuscula")
        n=str(input("ingrese una palabra: "))
        conta2=n.upper()
        print(conta2)
    else:
        print("ingrese una palabra en mayuscula")
        n=str(input("ingrese una palabra: "))
        conta2=n.lower()
        print(conta2)

mayusculas()"""

#- - Pida una cadena por teclado y diga cual es su valor al sumar sus codigos
#- Cual es el valor numerico de acuerdo a los códigos del alfabeto

"""def suma():
    lista=[]
    sum=0
    cod2=str(input("ingrese letras alazar"))
    for i in cod2:
        valor=ord(i)
        lista.append(valor)
    for x in lista:
        sum+=x
        
    print(sum)
    print(lista)
    
suma()"""

#- Cuantas letras del abecedario estan en la cadena, si estan repetidas cuentela solo una vez

"""def abecedario():
    abecedario2="abcdefghijklmnopqrstuvwxyzdkjavsfbailsdfllahidb"
    volver=[]
    tamaño=(len(abecedario2))
    for i in abecedario2:
        if i not in volver:
            volver.append(i)
    tamaño2=(len(volver))
    print("abecedario")
    print(volver)
    print("el abecedario tiene un tamaño de:",tamaño )
    print("el abecedario sin repetir tiene",tamaño2)

abecedario()  """  


#Invente un cifrado de texto tipo murcielago o César. Puede utilizar alguna formula matemática para este fin.
def murci():
    texto=input('Escriba su palabra o frase: ').lower()
    codigo=['m','u','r','c','i','e','l','a','g','o'] #es una lista
    print("murcielago")
    print("0123456789")
    salida=''
    """if texto in codigo:"""
    for i in range(len(texto)):
                if texto[i] in codigo:
                    salida+=str(codigo.index(texto[i]))
                
    print(salida)
        
murci()
        
    
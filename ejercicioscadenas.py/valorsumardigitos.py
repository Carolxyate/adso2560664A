#- - Pida una cadena por teclado y diga cual es su valor al sumar sus codigos
#- Cual es el valor numerico de acuerdo a los códigos del alfabeto

def suma():
    lista=[]
    sum=0
    cod2=str(input("ingrese letras alazar: "))
    for i in cod2:
        valor=ord(i)
        lista.append(valor)
    for x in lista:
        sum+=x
        
    print(sum)
    print(lista)
    
suma()
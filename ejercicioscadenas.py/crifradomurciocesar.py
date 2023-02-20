#Invente un cifrado de texto tipo murcielago o César. Puede utilizar alguna formula matemática para este fin.
"""def murci():
    texto=input('Escriba su palabra o frase: ').lower()
    codigo=['m','u','r','c','i','e','l','a','g','o'] #es una lista
    print("murcielago")
    print("0123456789")
    salida=''
    if texto in codigo:
    for i in range(len(texto)):
                if texto[i] in codigo:
                    salida+=str(codigo.index(texto[i]))
                
    print(salida)
        
murci()"""

def cifrado_cesar(cadena, desplazamiento):
    cifrado = ""
    for caracter in cadena:
        if caracter.isalpha():
            # Convertir a mayúsculas para facilitar el cifrado
            caracter = caracter.upper()
            # Aplicar la fórmula de cifrado
            codigo = ord(caracter) + desplazamiento
            # Si se sale del rango de letras mayúsculas, volver al inicio
            if codigo > ord('Z'):
                codigo -= 26
            cifrado += chr(codigo)
        else:
            # Mantener los caracteres que no sean letras
            cifrado += caracter
    return cifrado


cadena_original = "Que nadie te diga que no"
desplazamiento = 2
cadena_cifrada = cifrado_cesar(cadena_original, desplazamiento)
print(cadena_cifrada)


#descrifrar
cadena_descifrada = cifrado_cesar(cadena_cifrada, -desplazamiento)
print(cadena_descifrada)
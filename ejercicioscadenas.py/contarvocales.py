#De una cadena diga cuantas vocales tiene, cuantas consonantes, cuantas vocales con tilde y cuantos caracteres especiales.
def contar_caracteres(frase):
    vocales = 0
    consonantes = 0
    vocales_tilde = 0
    especiales = 0
    for caracter in frase:
        if caracter.isalpha():
            if caracter in 'aeiouAEIOU':
                vocales += 1
                if caracter in 'áéíóúÁÉÍÓÚ':
                    vocales_tilde += 1
            else:
                consonantes += 1
        else:
            especiales += 1
    print('La frase contiene', vocales, 'vocales,', consonantes, 'consonantes,', vocales_tilde, 'vocales con tilde y', especiales, 'caracteres especiales.')

frase = input('Ingrese una frase: ')
contar_caracteres(frase)
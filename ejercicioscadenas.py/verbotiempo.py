#Determinar en que tiempo esta conjugado un verbo
def tiempo_verbo(verbo):
    if verbo.endswith('i'):
        return 'Pasado'
    elif verbo.endswith('o'):
        return 'Presente'
    elif verbo.endswith('e'):
        return 'futuro'
    else:
        return 'Verbo desconocido'
verbo = 'comere'
#verbo=input("ingrese verbo en primera persona: ")
print(tiempo_verbo(verbo)) # Resultado: Presente
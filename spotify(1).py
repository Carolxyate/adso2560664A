spotify={}
def menu():
    if genero in spotify:
        spotify[genero] += (artista,)
    else:
        spotify[genero] = (artista,)
    
        


genero=input("ingrese el genero: ")
artista=input("ingrese el artista: ")
cancion=input("ingrese una cancion: ")
duracion=input("ingrese la duracion: ")
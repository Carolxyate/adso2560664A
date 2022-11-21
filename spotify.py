spotify={}
def artista(spotify):
    artista=input("ingrese el artista: ")
    spotify.update({artista:{}}) 
    return spotify
def informacionartista(spotify):
    cancion=input("Ingrese el nombre del cancion: ")
    genero=input("Ingrese el genero musical: ")
    duracion=input("Ingrese la duracion en formato xx(mm):xx(ss): ")
    if artista in spotify:
        spotify.update({artista:{"cancion":cancion,"genero":genero,"duracion":duracion}})
    return spotify
def buscar_artista(spotify): 

    
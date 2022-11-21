spotify={}
def artista(spotify):
    artista=input("ingrese el artista: ")
    spotify.update({artista:{}}) 
    return spotify
def informacionartista(spotify):
    artista=input("ingrese el artista: ")
    if artista not in spotify:
        print('El artista no se encuentra, agreguelo primero')
        return spotify
    cancion=input("Ingrese el nombre del cancion: ")
    genero=input("Ingrese el genero musical: ")
    duracion=input("Ingrese la duracion en formato xx(mm):xx(ss): ")
    if artista in spotify:
        spotify.update({artista:{"cancion":cancion,"genero":genero,"duracion":duracion}})
        
def buscarcancion(spotify):
    buscar=input("que cancion quiere buscar:  ")
    for i in sorted(spotify.values()):
        if buscar==i['cancion']:
            print("la cancion",buscar, "se encuentra en spotify y su duracion es:",i["duracion"])
            return None
    print("la cancion no se encuentra, ingrese el nombre primero")
    
def buscarartista(spotify):
    buscar=input("que artista desea buscar: ")
    for x in (spotify.keys()):
        if buscar==x:
            print("el artista",buscar, "se encuentra en spotify y su genero es:",spotify[x]["genero"])
            return None
    print("el artista no se encuentra, ingrese la cancion con el artista")
    
def eliminarartista(spotify):
    buscar=input("Que artista desea eliminar?: ")
    for i in sorted(spotify.keys()):
        if buscar==i:
            del spotify[i]
            print("La cancion",buscar,"fue eliminada correctamente")
            return None
    print("la cancion no se encuentra, ingrese primero el nombre")
    
def mayor(spotify):
    may=int
    mayor_valor=0
    for j in (spotify.keys()):
        minutos=spotify[j]["duracion"][0]
        minutos+=spotify[j]["duracion"][1]
        segundos=spotify[j]["duracion"][3]
        segundos+=spotify[j]["duracion"][4]
        segundos=int(segundos)+int(minutos)*60
        if mayor_valor<=segundos:
            mayor_valor=segundos
            may=spotify[j]['cancion']
            
    print("la cancion mas larga es:", may)
    
def menor(spotify):
    menor = dict
    menor_valor=9e99999
    for x in (spotify.keys()):
        minutos=spotify[x]["duracion"][0]
        minutos+=spotify[x]["duracion"][1]
        segundos=spotify[x]["duracion"][3]
        segundos+=spotify[x]["duracion"][4]
        segundos=int(segundos)+int(minutos)*60
        if menor_valor>=segundos:
            menor_valor=segundos
            menor=spotify[x]['cancion']
            
    print("la cancion mas corta es", menor)
           
while True:
    print("1-ingresar artista")
    print("2-ingresar infromacion de la cancion")
    print("3-eliminar artista")
    print("4-buscar cancion")
    print("5-buscar artista")
    print("6-Cancion mas larga")
    print("7-cancion mas corta")
    print("8-Todas las canciones")
    ctrl=int(input("ingrese la opcion que desee: ")) #tipo strin

    match ctrl:
        case 1:
            print(artista(spotify))
        case 2:
            print(informacionartista(spotify))
        case 3:
            print(eliminarartista(spotify))
        case 4:
            print(buscarcancion(spotify))
        case 5:
            print(buscarartista(spotify))
        case 6:
            print(mayor(spotify))
        case 7:
            print(menor(spotify))
        case 8:
            print("Estas todas las canciones agregadas; ",spotify)
        case _:
            print("opcion invalida")
            break
    

    
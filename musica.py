artista=input("ingrese el nombre del artista: ")
genero=input("ingrese el genero: ")

spotify_art = {}

dictti={"canciones":{"nombre":"save of teers",
                     "duracion":"4:15",
            }

            
        
while True:
    name = input("Ingrese el nombre de la cancion: ")
    if name == '':
        break
    
    
  score = int(input("Ingrese la duracion de la cancion en minutos(0-6): "))
    if score in range(0,6):
        break


def buscar_cancion(spotify):
    buscar=input('¿Que cancion desea buscar?: ') 
    for i in sorted(spotify.keys()):
        if buscar==i:
            print('La cancion',buscar,'se encuentra en spotify y su duracion es:',spotify[i]['duracion']) 
            return None 
    print('La cancion no se encuentra, ingrese el nombre primero') 


def spotify():
    art=input("ingrese el nombre del artista")
    genero=input("ingrese el genero: ")
    art.append(genero)
    musica+=art and genero
    print(spotify)
        
        
def mayor(spotify): 
    mayor=dict 
    mayor_valor=0 
    for a in (spotify.keys()): 
        minutos=spotify[a]['duracion'][0] 
        minutos+=spotify[a]['duracion'][1] 
        segundos=spotify[a]['duracion'][3] 
        segundos+=spotify[a]['duracion'][4] 
        segundos= int(segundos)+int(minutos)*60 
        if mayor_valor<=segundos: 
            mayor_valor=segundos 
            mayor=a 
print('La cancion mas larga es',mayor)


    while True:
    pedir=int(input('Presione 1 para agregar una cancion \n Presione 2 para agregar informacion detallada a una cancion ya agregada \n Presione 3 para buscar un artista \n Preione 4 para buscar una cancion \n Presione 5 para eliminar una cancion \n Presione 6 para mostrar todo lo agregado \n Presione 7 para mostrar la cancion mas larga \n Presione 8 para mostrar la cancion mas corta \n Presione 9 para finalizar el programa: '))

    if pedir==1: 
        (cancion(spotify)) 
    elif pedir==2: 
        (agregar_info_cancion(spotify)) 
    elif pedir==3: 
        (buscar_artista(spotify)) 
    elif pedir==4: 
        (buscar_cancion(spotify)) 
    elif pedir==5:
        (eliminar_cancion(spotify)) 
    elif pedir==6: 
        print('Todas las canciones agregada son las siguientes:',spotify) #Imprime el diccionario
    elif pedir==7: 
        mayor(spotify) 
    elif pedir==8: 
        menor(spotify) 
    elif pedir==9: 
        break 
    else:
        print('El numero no es valido') 
    os.system('pause') 
















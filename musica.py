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



    while True:
    pedir=int(input('Presione 1 para agregar una cancion \n Presione 2 para agregar informacion detallada a una cancion ya agregada \n Presione 3 para buscar un artista \n Preione 4 para buscar una cancion \n Presione 5 para eliminar una cancion \n Presione 6 para mostrar todo lo agregado \n Presione 7 para mostrar la cancion mas larga \n Presione 8 para mostrar la cancion mas corta \n Presione 9 para finalizar el programa: '))

    if pedir==1: #Si pedir es igual a 1
        (cancion(spotify)) #Funcion de agregar cancion
    elif pedir==2: #Si pedir es igual a 2
        (agregar_info_cancion(spotify)) #Funcion de agregar info de cancion
    elif pedir==3: #Si pedir es igual a 3
        (buscar_artista(spotify)) #Funcion de buscar un artista
    elif pedir==4: #Si pedir es igual a 4
        (buscar_cancion(spotify)) #Funcion de buscar una cancion
    elif pedir==5: #Si pedir es igual a 5
        (eliminar_cancion(spotify)) #Funcion de eliminar una cancion
    elif pedir==6: #Si pedir es igual a 6
        print('Todas las canciones agregada son las siguientes:',spotify) #Imprime el diccionario
    elif pedir==7: #Si pedir es igual a 7
        mayor(spotify) #Funcion de la cancion mas larga
    elif pedir==8: #Si pedir es igual a 8
        menor(spotify) #Funcion de la cancion mas corta
    elif pedir==9: #Si pedir es igual a 9
        break #Finaliza con un break el programa
    else:
        print('El numero no es valido') #Si no se inserta alguno de estos numeros, el programa saca este mensaje y vuelve a pedir
    os.system('pause') #Se invoca de nuevo "os" para que al final de cada proceso realizado, inserte el siguiente mensaje: 
    #Presione una tecla para continuar . . .
















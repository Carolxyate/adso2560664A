artista=input("ingrese el nombre del artista: ")
genero=input("ingrese el genero: ")

spotify_art = {}

while True:
    name = input("Ingrese el nombre de la cancion: ")
    if name == '':
        break
    
    
    score = int(input("Ingrese la duracion de la cancion en minutos(0-6): "))
    if score in range(0,6):
        break

for name in sorted(spotify_art.keys()):
    adding = 0
    counter = 0
    for score in spotify_art[name]:
        adding += score
        counter += 1
    print(name, ":", adding / counter)

def spotify():
    art=input("ingrese el nombre del artista")
    genero=input("ingrese el genero: ")
    art.append(genero)
    musica+=art and genero
    print(spotify)

dictti={"canciones":{"nombre":"save of teers",
                     "duracion":"4:15",
            }

















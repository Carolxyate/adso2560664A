def leer_archivo():
    try:
        nombre_archivo = input("Ingrese el nombre del archivo: ")
        archivo = open(nombre_archivo, "r")
        contenido = archivo.read()
        print("El contenido del archivo es:", contenido)
    except FileNotFoundError:
        print("No se encontró el archivo.")
leer_archivo()
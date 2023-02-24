
def index():
    try:
        ingrese=input("ingresedigito: ")
        datos=[5,4,7,8,9,5,6]
        busqueda=100
        for i in ingrese:
            if i not in datos:
                datos.append(ingrese)
        print(datos[busqueda])
        
    
    except IndexError:
        print("el indice no esta en la lista :) ")
    
    
index()
    
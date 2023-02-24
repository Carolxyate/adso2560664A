def edad():#se crea una funcion sin parametros 
    try:
        tuedad=int(input("introduce tu edad"))#se crea una variable que solicita ingresar un valor entero
        print(f'tu edad es  {tuedad}')#imprime la edad ingresada(se mezcla la cadena de texto con la variable)
        #print('Tu edad es ',tuedad)
    except ValueError as e:   #se crea un except que se ejecuta si se ingresa un valor difirente a un numero y se renombra 
        print(e)#imprime el error incorporado en python
        print("La edad debe ser un valor numerico...")#imprime el mensaje si se ejecuta el error
        edad()#se llama la funcion y sigue ejecutando hasta que se ingrese un valor difrente a un numero para que se ejecute el except
    
edad()#se llama la funcion